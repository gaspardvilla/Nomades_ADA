import os
import numpy as np
from week_2.generators.monday import monday2_generator

if __name__ == '__main__':
    # Fix the path and the seed
    seed = 47689
    np.random.seed(seed)
    path = 'data'

    # Create the data folder if it doesn't exist
    os.makedirs(path, exist_ok = True)

    # Run generators for each day
    monday2_generator(path, seed)
