import pandas as pd


def clean_data(df):
    """
    Cleans the dataset by:
    - Removing duplicate rows
    - Filling missing numerical values with mean
    """
    df = df.drop_duplicates()

    numeric_columns = df.select_dtypes(include=["number"]).columns

    for col in numeric_columns:
        df[col] = df[col].fillna(df[col].mean())

    return df


def get_feature_columns():
    return [
        "Temperature",
        "Rainfall",
        "Humidity",
        "Area",
        "Nitrogen",
        "Phosphorus",
        "Potassium"
    ]