# Import necessary libraries
import pandas as pd
import numpy as np

def monday2_generator(path, seed):
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

    # Save to csv using pandas
    df.to_csv(f'{path}/week_2/monday.csv', index=False)
    df.to_excel(f'{path}/week_2/monday.xlsx', index=False)
    df.to_json(f'{path}/week_2/monday.json', index=False)
