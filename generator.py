import os
import numpy as np
from week_2.generators.monday import w2_sales, w2_waves
from week_2.generators.wednesday import w2_ci

if __name__ == '__main__':
    # Fix the path and the seed
    seed = 47689
    np.random.seed(seed)
    path = 'data'

    # Create the data folder if it doesn't exist
    os.makedirs(path, exist_ok = True)
    os.makedirs(f'{path}/week_2', exist_ok = True)
    os.makedirs(f'{path}/week_3', exist_ok = True)

    # Run generators for week 2
    w2_sales(f'{path}/week_2', seed)
    w2_waves(f'{path}/week_2', seed)
    w2_ci(f'{path}/week_2', seed)
