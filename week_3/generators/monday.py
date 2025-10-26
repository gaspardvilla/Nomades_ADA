import numpy as np
import pandas as pd


def w3_overfitting(path, nb_samples = 100, seed = 47689):
    # Generate data
    np.random.seed(seed)
    x = np.random.uniform(0, 10, nb_samples)
    y = x**2 + np.random.normal(0, 5, nb_samples)
    
    # Save to csv using pandas
    pd.DataFrame({
        'x': x,
        'y': y
    }).to_csv(f'{path}/overfitting_data.csv', index=False)
    

def w3_knn(path, nb_samples = 10000, seed = 47689):
    # Generate data
    np.random.seed(seed)
    coord_x = np.random.uniform(0, 10, nb_samples)
    coord_y = np.random.uniform(0, 10, nb_samples)
    target = np.zeros(nb_samples)

    # Mark as 1 all points in a circle of radius 2 centered at (3, 4)
    target[np.sqrt((coord_x - 3)**2 + (coord_y - 4)**2) < 2] = 1
    target[(6 <= coord_x) & (coord_x <= 9) & (7 <= coord_y) & (coord_y <= 8)] = 1
    target[(0 <= coord_x) & (coord_x <= 0.1) & (9.5 <= coord_y) & (coord_y <= 10)] = 1
    
    # Save to csv using pandas
    pd.DataFrame({
        'coord_x': coord_y,
        'coord_y': coord_x,
        'target': target
    }).to_csv(f'{path}/knn_dataset.csv', index=False)


    # Testing set
    x = np.random.uniform(0, 10, 50)
    y = np.random.uniform(0, 10, 50)
    target = np.zeros(50)

    # Mark as 1 all points in a circle of radius 2 centered at (3, 4)
    target[np.sqrt((x - 3)**2 + (y - 4)**2) < 2] = 1
    target[(6 <= x) & (x <= 9) & (7 <= y) & (y <= 8)] = 1
    target[(0 <= x) & (x <= 0.1) & (9.5 <= y) & (y <= 10)] = 1
    
    # Add 50 random points in [0, 0.1] x [9.5, 10]
    x_add = np.random.uniform(0, 0.1, 50)
    y_add = np.random.uniform(9.5, 10, 50)
    target_add = np.zeros(50) + 1
    
    # Save to csv using pandas
    pd.DataFrame({
        'coord_x': np.concatenate((y, y_add)),
        'coord_y': np.concatenate((x, x_add)),
        'target': np.concatenate((target, target_add))
    }).to_csv(f'{path}/knn_testset.csv', index=False)
