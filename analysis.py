# analysis.py

import pandas as pd


def get_dataset_info(df):
    """
    Returns basic dataset information.
    """

    info = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns),
        "data_types": df.dtypes.astype(str),
        "missing_values": df.isnull().sum(),
        "duplicate_rows": df.duplicated().sum()
    }

    return info


def numerical_summary(df):
    """
    Returns statistical summary for numerical columns.
    """

    numeric_df = df.select_dtypes(include=["number"])

    if numeric_df.empty:
        return None

    return numeric_df.describe().T


def categorical_summary(df):
    """
    Returns value counts for categorical columns.
    """

    categorical = {}

    cat_columns = df.select_dtypes(include=["object", "category"]).columns

    for column in cat_columns:
        categorical[column] = df[column].value_counts()

    return categorical


def missing_value_table(df):
    """
    Returns missing values table.
    """

    missing = pd.DataFrame({
        "Column": df.columns,
        "Missing Values": df.isnull().sum().values,
        "Percentage": (
            df.isnull().sum().values / len(df) * 100
        ).round(2)
    })

    return missing


def unique_values(df):
    """
    Returns number of unique values in every column.
    """

    unique = pd.DataFrame({
        "Column": df.columns,
        "Unique Values": df.nunique().values
    })

    return unique


def correlation_matrix(df):
    """
    Returns correlation matrix of numeric columns.
    """

    numeric = df.select_dtypes(include=["number"])

    if numeric.empty:
        return None

    return numeric.corr()


def dataset_report(df):
    """
    Creates one complete report dictionary.
    """

    report = {
        "info": get_dataset_info(df),
        "statistics": numerical_summary(df),
        "categorical": categorical_summary(df),
        "missing": missing_value_table(df),
        "unique": unique_values(df),
        "correlation": correlation_matrix(df)
    }
    

    return report

