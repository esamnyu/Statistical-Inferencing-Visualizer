import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np

def clean_data(df, strategy='mean'):
    """
    Cleans the DataFrame by imputing missing values.
    :param df: pandas DataFrame
    :param strategy: Strategy to impute missing values ('mean', 'median', 'most_frequent')
    :return: Cleaned DataFrame
    """
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if strategy == 'mean':
                df[col].fillna(df[col].mean(), inplace=True)
            elif strategy == 'median':
                df[col].fillna(df[col].median(), inplace=True)
            elif strategy == 'most_frequent':
                df[col].fillna(df[col].mode()[0], inplace=True)
    return df

def normalize_data(df, columns):
    """
    Applies Min-Max normalization to the specified columns.
    :param df: pandas DataFrame
    :param columns: List of columns to normalize
    :return: DataFrame with normalized columns
    """
    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

def standardize_data(df, columns):
    """
    Standardizes the specified columns (mean=0, std=1).
    :param df: pandas DataFrame
    :param columns: List of columns to standardize
    :return: DataFrame with standardized columns
    """
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

def split_dataset(df, target, test_size=0.2, random_state=None):
    """
    Splits the dataset into training and testing sets.
    :param df: pandas DataFrame
    :param target: Name of the target column
    :param test_size: Proportion of the dataset to include in the test split
    :param random_state: Controls the shuffling applied to the data before applying the split
    :return: X_train, X_test, y_train, y_test
    """
    X = df.drop(target, axis=1)
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

def generate_synthetic_data(size=100, random_state=None):
    """
    Generates synthetic data for testing.
    :param size: Size of the dataset to generate
    :param random_state: Seed for random number generator
    :return: Synthetic DataFrame
    """
    np.random.seed(random_state)
    X = np.random.rand(size, 2)  # Generate random data
    y = np.random.randint(0, 2, size)  # Binary target
    df = pd.DataFrame(np.column_stack([X, y]), columns=['Feature1', 'Feature2', 'Target'])
    return df
