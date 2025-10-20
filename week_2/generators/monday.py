# Import necessary libraries
import pandas as pd
import numpy as np
from datetime import datetime



def w2_sales(path, seed):
    """
    Generate a sales dataset for the second day of the week.

    Parameters:
        - path: Path to save the dataset
        - seed: Random seed for reproducible data
    """

    # Set random seed for reproducible data
    np.random.seed(seed)

    # Create the sales dataset
    n_rows = 1000
    products = ['Laptop', 'Phone', 'T-Shirt', 'Jeans', 'Novel', 'Cookbook', 'TV', 'Headphones', 
            'Shoes', 'Jacket', 'Textbook', 'Magazine', 'Tablet', 'Speaker', 'Dress', 'Sweater']

    categories = ['Electronics', 'Clothing', 'Books', 'Home']
    regions = ['North', 'South', 'East', 'West']

    # Generate random data
    data = {
        'Product': np.random.choice(products, n_rows),
        'Category': np.random.choice(categories, n_rows, p=[0.3, 0.25, 0.2, 0.25]),
        'Price': np.round(np.random.lognormal(4, 0.8, n_rows), 2),
        'Quantity': np.random.randint(1, 10, n_rows),
        'Date': pd.date_range('2024-01-01', periods=n_rows, freq='D'),
        'Region': np.random.choice(regions, n_rows)
    }

    # Create DataFrame
    df = pd.DataFrame(data)
    df.to_csv(f'{path}/sales.csv', index=False)



def w2_waves(path, seed):
    """
    Generate synthetic surfing wave forecasting time series dataset
    
    Parameters:
    - path: Directory to save the dataset
    - seed: Random seed for reproducibility
    """
    # Set random seed
    np.random.seed(seed)
    
    # Create datetime range: Aug 1 - Sept 30, 2024 (61 days, 24 hours each)
    start_date = datetime(2024, 8, 1, 0, 0, 0)
    end_date = datetime(2024, 9, 30, 23, 0, 0)
    datetime_range = pd.date_range(start=start_date, end=end_date, freq='H')
    
    # Wind and wave directions
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    
    # Initialize arrays
    wind_directions = []
    wave_directions = []
    wind_speeds = []
    wave_heights = []
    temperatures = []
    humidities = []
    pressures = []
    tide_levels = []
    swell_periods = []
    
    # Generate data with simplified patterns
    for i, dt in enumerate(datetime_range):
        hour = dt.hour
        day_of_week = dt.weekday()  # 0=Monday, 6=Sunday
        month = dt.month
        
        # Wind speed: stronger during day hours (10-16h)
        if 10 <= hour <= 16:
            wind_speed = np.random.normal(25, 5)  # Higher during day
        else:
            wind_speed = np.random.normal(15, 3)  # Lower at night
        
        wind_speed = max(0, min(45, wind_speed))
        wind_speeds.append(wind_speed)
        
        # Wind direction (random, no specific pattern)
        wind_direction = np.random.choice(directions)
        wind_directions.append(wind_direction)
        
        # Wave height: higher on Wednesdays (2) and Sundays (6), higher in September
        base_height = 1.5
        
        # Day of week effect: Wednesday and Sunday higher
        if day_of_week == 2:
            day_effect = 0.6
        elif day_of_week == 6:
            day_effect = 0.3
        else:
            day_effect = 0
        
        # Month effect: September higher than August
        month_effect = 0.3 if month == 9 else 0
        
        # Add some randomness
        noise = np.random.normal(0, 0.2)
        
        wave_height = base_height + day_effect + month_effect + noise
        wave_height = max(0.1, min(3.0, wave_height))
        wave_heights.append(wave_height)
        
        # Wave direction (random, no specific pattern)
        wave_direction = np.random.choice(directions)
        wave_directions.append(wave_direction)
        
        # Temperature (random, no specific pattern)
        temp = np.random.normal(22, 3)
        temp = max(15, min(30, temp))
        temperatures.append(temp)
        
        # Humidity (random, no specific pattern)
        humidity = np.random.uniform(30, 90)
        humidities.append(humidity)
        
        # Pressure (random, no specific pattern)
        pressure = np.random.normal(1013, 10)
        pressure = max(980, min(1030, pressure))
        pressures.append(pressure)
        
        # Tide level (random, no specific pattern)
        tide_level = np.random.uniform(0, 5)
        tide_levels.append(tide_level)
        
        # Swell period (random, no specific pattern)
        swell_period = np.random.uniform(5, 20)
        swell_periods.append(swell_period)
    
    # Create DataFrame
    df = pd.DataFrame({
        'datetime': datetime_range,
        'wind_direction': wind_directions,
        'wave_height': wave_heights,
        'wave_direction': wave_directions,
        'wind_speed': wind_speeds,
        'temperature': temperatures,
        'humidity': humidities,
        'pressure': pressures,
        'tide_level': tide_levels,
        'swell_period': swell_periods
    })
    
    # Round numerical values for realism
    df['wave_height'] = df['wave_height'].round(2)
    df['wind_speed'] = df['wind_speed'].round(1)
    df['temperature'] = df['temperature'].round(1)
    df['humidity'] = df['humidity'].round(1)
    df['pressure'] = df['pressure'].round(1)
    df['tide_level'] = df['tide_level'].round(2)
    df['swell_period'] = df['swell_period'].round(1)
    
    # Set datetime as index
    df.set_index('datetime', inplace=True)
    df.to_csv(f"{path}/waves.csv")
