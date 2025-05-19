import numpy as np
import pandas as pd


def generate_overfitting_data(nb_samples=100, path='data'):
    # Generate data
    x = np.random.uniform(0, 10, nb_samples)
    y = x**2 + np.random.normal(0, 5, nb_samples)
    
    # Save to csv using pandas
    pd.DataFrame({
        'x': x,
        'y': y
    }).to_csv(f'{path}/overfitting_data.csv', index=False)
    