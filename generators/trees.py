import numpy as np
import pandas as pd


def generate_tree_data(path):
    # Random generation of the data
    X = np.sort(5 * np.random.rand(80, 1), axis=0)
    y = np.sin(X).ravel()
    y[::5] += 3 * (0.5 - np.random.rand(16))

    # Save to csv using pandas
    pd.DataFrame({
        'x': X.flatten(),
        'y': y
    }).to_csv(f'{path}/tree_data.csv', index=False)