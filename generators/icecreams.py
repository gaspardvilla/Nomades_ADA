import numpy as np
import pandas as pd

def ice_cream_sales_drowning_deaths(path):
    # Simulate data for 12 months
    np.random.seed(42)
    months = np.arange(1, 13)
    temperature = 10 + 10 * np.sin((months - 1) * np.pi / 6) + np.random.normal(0, 1, 12)  # warmer in summer

    # Ice cream sales increase with temperature (in thousands of units)
    ice_cream_sales = 20 + 5 * temperature + np.random.normal(0, 5, 12)

    # Drowning deaths increase with temperature (per month)
    drowning_deaths = 5 + 0.8 * temperature + np.random.normal(0, 2, 12)

    # Put in a DataFrame
    df = pd.DataFrame({
        'Month': months,
        'IceCreamSales': ice_cream_sales,
        'DrowningDeaths': drowning_deaths
    })

    # Save to csv using pandas
    pd.DataFrame(df).to_csv(f'{path}/ice_cream_sales_drowning_deaths.csv', index=False)

    # Put in a DataFrame
    df = pd.DataFrame({
        'Month': months,
        'Temperature': temperature,
        'IceCreamSales': ice_cream_sales,
        'DrowningDeaths': drowning_deaths
    })

    # Save to csv using pandas
    pd.DataFrame(df).to_csv(f'{path}/ice_cream_sales_drowning_deaths_temperature.csv', index=False)


    # Non-linear relationship
    x = np.linspace(-1, 1, 200)
    y = x**2 + np.random.normal(0, 0.02, size=200)
    df = pd.DataFrame({
        'x': x,
        'y': y
    })
    pd.DataFrame(df).to_csv(f'{path}/non_linear_relationship.csv', index=False)