# utils.py

import pandas as pd


def load_csv(uploaded_file):
    """
    Safely load a CSV file.
    """
    return pd.read_csv(uploaded_file)


def validate_dataframe(df):
    """
    Check if DataFrame is valid.
    """
    return df is not None and not df.empty


def get_numeric_columns(df):
    return df.select_dtypes(include=["number"]).columns.tolist()


def get_categorical_columns(df):
    return df.select_dtypes(include=["object", "category"]).columns.tolist()


def format_number(number):
    try:
        return "{:,}".format(number)
    except Exception:
        return number


def dataframe_shape(df):
    return {
        "rows": df.shape[0],
        "columns": df.shape[1]
    }


def total_missing(df):
    return int(df.isnull().sum().sum())


def duplicate_rows(df):
    return int(df.duplicated().sum())


def memory_usage(df):
    memory = df.memory_usage(deep=True).sum()
    return round(memory / (1024 * 1024), 2)


def dataset_overview(df):
    return {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": total_missing(df),
        "Duplicate Rows": duplicate_rows(df),
        "Memory Usage (MB)": memory_usage(df)
    }


def top_rows(df, rows=5):
    return df.head(rows)


def bottom_rows(df, rows=5):
    return df.tail(rows)


def column_summary(df):
    return pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Missing": df.isnull().sum().values,
        "Unique": df.nunique().values
    })


def get_download_csv(df):
    return df.to_csv(index=False).encode("utf-8")