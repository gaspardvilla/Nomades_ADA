import os
import numpy as np
from revenues import generate_revenue_dataset
from time_series import generate_brownian_motion
from houses import generate_houses_dataset

if __name__ == '__main__':

    # Fix the path and the seed
    seed = 47689
    path = '/Users/gaspardvilla/Local/NAT/nat_ada/data'

    # Create the data folder if it doesn't exist
    os.makedirs(path, exist_ok=True)

    # Run all generators
    generate_revenue_dataset(1000, seed, path)
    generate_brownian_motion(seed, path)
    generate_houses_dataset(3000, seed, path)