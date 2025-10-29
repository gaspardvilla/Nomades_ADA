import numpy as np
import pandas as pd


def w3_decision_trees(path, seed = 47689):
    np.random.seed(seed)

    # Random generation of the data
    X = np.sort(5 * np.random.rand(80, 1), axis=0)
    y = np.sin(X).ravel()
    y[::5] += 3 * (0.5 - np.random.rand(16))

    X_ = np.sort(np.random.rand(20, 1), axis=0)
    y_ = np.sin(X_).ravel()

    # Add it to X and y
    X = np.concatenate((X, X_), axis=0)
    y = np.concatenate((y, y_), axis=0)

    # Save to csv using pandas
    pd.DataFrame({
        'x': X.flatten(),
        'y': y
    }).to_csv(f'{path}/decision_trees.csv', index=False)
