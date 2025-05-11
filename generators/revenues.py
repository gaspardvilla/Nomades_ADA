import numpy as np
import pandas as pd
from pandas._libs.lib import fast_multiget
from scipy.stats import lognorm, randint

def generate_revenue_dataset(n_samples, seed, path):
    # Fix the seed
    np.random.seed(seed)
    
    # Family size [None, Small, Medium, Large]
    family_sizes = ['No family', 'Small', 'Medium', 'Large']
    family_size = np.random.choice(family_sizes, n_samples, 
                                 p = [0.3, 0.5, 0.15, 0.05])

    # Age distribution (20-65 years) - different means for different family sizes
    age_no_family = np.random.normal(20, 4, size=len(family_size[family_size == 'No family'])).astype(int)
    age_small = np.random.normal(35, 10, size=len(family_size[family_size == 'Small'])).astype(int)
    age_medium = np.random.normal(60, 20, size=len(family_size[family_size == 'Medium'])).astype(int)
    age_large = np.random.normal(75, 8, size=len(family_size[family_size == 'Large'])).astype(int)

    # Combine all ages and clip
    ages = np.zeros(n_samples)
    ages[family_size == 'No family'] = age_no_family
    ages[family_size == 'Small'] = age_small
    ages[family_size == 'Medium'] = age_medium
    ages[family_size == 'Large'] = age_large
    ages = np.clip(ages, 0, 120).astype(int)
    
    # Education levels (3 levels: Basic, Intermediate, Advanced)
    education_levels = ['Basic', 'Intermediate', 'Advanced']
    education = np.random.choice(education_levels, n_samples, 
                                 p = [0.3, 0.6, 0.1])
    
    # Annual revenue distribution (log-normal distribution)
    # Mean in log-space: 11.5 (corresponds to ~100k CHF)
    # Standard deviation in log-space
    revenue_basic = lognorm.rvs(s=0.2, scale=np.exp(11.0), size=len(education[education == 'Basic']))  # Lower mean for Basic
    revenue_intermediate = lognorm.rvs(s=0.6, scale=np.exp(11.5), size=len(education[education == 'Intermediate']))  # Medium mean
    revenue_advanced = lognorm.rvs(s=0.5, scale=np.exp(12.0), size=len(education[education == 'Advanced']))  # Higher mean for Advanced

    # Combine all revenues
    revenues = np.zeros(n_samples)
    revenues[education == 'Basic'] = revenue_basic
    revenues[education == 'Intermediate'] = revenue_intermediate
    revenues[education == 'Advanced'] = revenue_advanced
    
    # Create DataFrame
    df = pd.DataFrame({
        'Age': ages,
        'Family_Size': family_size,
        'Education_Level': education,
        'Annual_Revenue_CHF': revenues
    })
    df.to_csv(f"{path}/revenue_data.csv", index = False)
    return df