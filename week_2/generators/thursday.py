import pandas as pd
import numpy as np
import random
import os


def w2_titanic(path, seed):
    # Random seed
    np.random.seed(seed)
    random.seed(seed)

    # Check data exists or raise error
    if not os.path.exists(f'{path}/titanic/train.csv'):
        raise FileNotFoundError(f'{path}/titanic/train.csv not found. Please \
                                  load the data first at: https://www.kaggle.com/competitions/titanic/data.')
    
    # Load data set
    input_path = f'{path}/titanic/train.csv'
    output_path = f'{path}/titanic.csv'
    df = pd.read_csv(input_path)

    # Make it dirty
    df = add_duplicates(df)
    df = add_outliers(df)
    df = add_missing_data(df)

    # # Convert to numeric first, then to nullable int
    # df['PassengerId'] = pd.to_numeric(df['PassengerId'], errors='coerce').astype('Int64')
    # df['Survived'] = pd.to_numeric(df['Survived'], errors='coerce').astype('Int64')
    # df['Pclass'] = pd.to_numeric(df['Pclass'], errors='coerce').astype('Int64')
    # df['Age'] = pd.to_numeric(df['Age'], errors='coerce').astype('Int64')
    # df['SibSp'] = pd.to_numeric(df['SibSp'], errors='coerce').astype('Int64')
    # df['Parch'] = pd.to_numeric(df['Parch'], errors='coerce').astype('Int64')

    # Save the data set
    df.to_csv(output_path, index=False)


def add_duplicates(df, duplicate_rate = 0.08):
    n_duplicates = int(len(df) * duplicate_rate)
    duplicate_indices = np.random.choice(df.index, size=n_duplicates, replace=False)
    
    # Create duplicates by adding Nan values to some columns
    duplicates = []
    for idx in duplicate_indices:
        duplicate_row = df.loc[idx].copy()
        for column in df.columns:
            if np.random.random() < 0.5:
                duplicate_row[column] = np.nan
        duplicates.append(duplicate_row)
    
    # Add duplicates to the dataset
    return pd.concat([df, pd.DataFrame(duplicates)], ignore_index=True)


def add_outliers(df, outlier_rate = 0.02):
    n_outliers = int(len(df) * outlier_rate)
    outlier_indices = np.random.choice(df.index, size=n_outliers, replace=False)
    
    # Create outliers by adding extreme values to some columns
    outliers = []
    for idx in outlier_indices:
        outlier_row = df.loc[idx].copy()
        columns_values = [('Age', [0, 105, 120, 150]), 
                          ('SibSp', [0, 10, 20, 30]), 
                          ('Parch', [0, 10, 20, 30]), 
                          ('Fare', [-50, -10, 1000, 2000])]
        for column, values in columns_values:
            if np.random.random() < 0.5:
                outlier_row[column] = np.random.choice(values)
        outliers.append(outlier_row)
    
    df.loc[outlier_indices] = outliers
    return df


def add_missing_data(df, missing_rate = 0.2):
    n_missing = int(len(df) * missing_rate)
    missing_indices = np.random.choice(df.index, size=n_missing, replace=False)
    
    # Create missing data by adding Nan values to some columns
    missing = []
    for idx in missing_indices:
        missing_row = df.loc[idx].copy()
        for column in df.columns:
            if np.random.random() < 0.5:
                missing_row[column] = np.nan
        missing.append(missing_row)
    
    df.loc[missing_indices] = missing
    return df


def w2_ice_cream(path, seed):
    # Random seed
    np.random.seed(seed)
    random.seed(seed)

    # Simulate data for 12 months
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
