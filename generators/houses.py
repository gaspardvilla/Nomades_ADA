import numpy as np
import pandas as pd
from scipy.stats import lognorm

def generate_houses_dataset(n_samples, seed, path):
    """
    Generate a dataset of houses with various attributes
    
    Parameters:
    - n_samples: Number of houses to generate
    - seed: Random seed for reproducibility
    - path: Path to save the dataset
    
    Returns:
    - DataFrame containing house attributes
    """
    # Set random seed
    np.random.seed(seed)
    
    # Wall types with probabilities
    wall_types = ['concrete', 'brick', 'wood']
    wall_probs = [0.6, 0.3, 0.1]  # Concrete is most common, wood is rarest
    data_walls = np.random.choice(wall_types, size=n_samples, p=wall_probs)

    # Distance from downtown in km (distributed regarding wall type)
    data_dist_downtown = np.zeros(n_samples)
    data_dist_downtown[data_walls == 'concrete'] = lognorm.rvs(s=0.7, scale=np.exp(3), size=len(data_walls[data_walls == 'concrete']))
    data_dist_downtown[data_walls == 'brick'] = lognorm.rvs(s=0.2, scale=np.exp(1), size=len(data_walls[data_walls == 'brick']))
    data_dist_downtown[data_walls == 'wood'] = lognorm.rvs(s=1.5, scale=np.exp(10), size=len(data_walls[data_walls == 'wood']))

    # Garden size (linearly dependant of the distance from downtown and the wall type and
    # adding white noise)
    data_garden_size = np.zeros(n_samples)
    data_garden_size[data_walls == 'concrete'] = data_dist_downtown[data_walls == 'concrete'] * .5 + np.random.normal(0, 3, len(data_walls[data_walls == 'concrete']))
    data_garden_size[data_walls == 'wood'] = data_dist_downtown[data_walls == 'wood'] * 10 + np.random.normal(0, 10, len(data_walls[data_walls == 'wood']))

    # Surface area (logistic distribution regarding the distance from downtown)
    data_surface = np.clip(lognorm.rvs(s=0.3, scale=120, size=n_samples) * (data_dist_downtown / 10), 40, 500)
    
    # Pool (boolean, with 20% chance of having a pool if distance from downtown is larger than 4km)
    data_pool = np.zeros(n_samples)
    data_pool[data_dist_downtown > 4] = np.random.choice([True, False], size=len(data_dist_downtown[data_dist_downtown > 4]), p=[0.2, 0.8])
    
    # Generate house attributes
    data = {
        # Garden size in square meters (linearly dependant of the distance from downtown and the wall type and adding white noise)
        'garden_size': data_garden_size,
        
        # Distance from downtown in km (skewed towards closer distances)
        'distance_downtown_km': data_dist_downtown,
        
        # Surface area in square meters (logistic distribution regarding the distance from downtown)
        'surface_m2': data_surface,
        
        # Number of floors (1-4, with 1 being most common)
        'floors': np.random.choice([1, 2, 3, 4], size=n_samples, p=[0.5, 0.3, 0.15, 0.05]),
        
        # Wall type
        'wall_type': data_walls,
        
        # Pool (boolean, with 20% chance of having a pool if distance from downtown is larger than 4km)
        'has_pool': data_pool
    }
    
    # Calculate base price based on attributes
    df = pd.DataFrame(data)
    
    # Base price per square meter (higher for better wall types)
    price_per_m2 = {
        'concrete': 5000,
        'brick': 4500,
        'wood': 4000
    }

    # Calculate price based on attributes
    df['price'] = (
        # Base price based on surface and wall type (in €/m²)
        df['surface_m2'] * df['wall_type'].map(price_per_m2) +
        # Premium for garden (500 per m², capped at 2000m²)
        np.minimum(df['garden_size'], 2000) * 500 +
        # Premium for pool (only if garden is at least 100m²)
        (df['has_pool'].astype(bool) & (df['garden_size'] >= 100)).astype(int) * 50000 +
        # Premium for being closer to downtown (exponential decrease)
        np.exp(-df['distance_downtown_km'] / 5) * 200000 +
        # Premium for additional floors
        (df['floors'] - 1) * 15000 +
        # Add some random noise
        np.random.normal(0, 50000, n_samples)
    )

    # Ensure price is within realistic bounds and round to nearest 1000
    df['price'] = np.round(np.clip(df['price'], 300000, 3000000) / 1000) * 1000
    
    # Save to CSV
    df.to_csv(f"{path}/boston_houses_data.csv", index=False)
    return df