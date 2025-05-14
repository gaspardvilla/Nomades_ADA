import numpy as np
import pandas as pd


def generate_ci(path):
    # Build data set from normal distribution with mean = 12 and std = 6
    mu = 12
    sigma = 6
    n = 1000
    x = np.random.normal(mu, sigma, n)

    # Save to csv using pandas
    pd.DataFrame(x).to_csv(f'{path}/normal_ci.csv', index=False)

    # Build data set from exponential distribution with lmabda = 1/12
    lambda_ = 12
    n = 1000
    x = np.random.exponential(lambda_, n)

    # Save to csv using pandas
    pd.DataFrame(x).to_csv(f'{path}/exponential_ci.csv', index=False)