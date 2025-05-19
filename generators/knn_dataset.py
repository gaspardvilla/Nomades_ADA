import numpy as np
import pandas as pd

def generate_knn_dataset(path='data'):
    # Generate data
    coord_x = np.random.uniform(0, 10, 10000)
    coord_y = np.random.uniform(0, 10, 10000)
    target = np.zeros(10000)

    # Mark as 1 all points in a circle of radius 2 centered at (3, 4)
    target[np.sqrt((coord_x - 3)**2 + (coord_y - 4)**2) < 2] = 1
    target[(6 <= coord_x) & (coord_x <= 9) & (7 <= coord_y) & (coord_y <= 8)] = 1
    target[(0 <= coord_x) & (coord_x <= 0.1) & (9.5 <= coord_y) & (coord_y <= 10)] = 1
    print(len(target[(0 <= coord_x) & (coord_x <= 0.1) & (9.5 <= coord_y) & (coord_y <= 10)]))
    
    # Save to csv using pandas
    pd.DataFrame({
        'coord_x': coord_y,
        'coord_y': coord_x,
        'target': target
    }).to_csv(f'{path}/knn_dataset.csv', index=False)