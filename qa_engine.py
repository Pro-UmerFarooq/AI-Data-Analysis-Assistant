# qa_engine.py

import pandas as pd


def answer_question(df, question):
    """
    Answer simple natural language questions about the dataset.
    """

    question = question.lower().strip()

    numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()
    categorical_columns = df.select_dtypes(include=["object", "category"]).columns.tolist()

    # --------------------------
    # Number of rows
    # --------------------------
    if "rows" in question or "records" in question:
        return f"The dataset contains {len(df)} rows."

    # --------------------------
    # Number of columns
    # --------------------------
    if "columns" in question:
        return f"The dataset contains {len(df.columns)} columns."

    # --------------------------
    # Missing values
    # --------------------------
    if "missing" in question:
        total_missing = df.isnull().sum().sum()
        return f"There are {total_missing} missing values."

    # --------------------------
    # Average
    # --------------------------
    if "average" in question or "mean" in question:

        for col in numeric_columns:
            if col.lower() in question:
                return f"The average of {col} is {df[col].mean():.2f}"

    # --------------------------
    # Maximum
    # --------------------------
    if "maximum" in question or "highest" in question or "max" in question:

        for col in numeric_columns:
            if col.lower() in question:
                return f"The maximum value of {col} is {df[col].max()}"

    # --------------------------
    # Minimum
    # --------------------------
    if "minimum" in question or "lowest" in question or "min" in question:

        for col in numeric_columns:
            if col.lower() in question:
                return f"The minimum value of {col} is {df[col].min()}"

    # --------------------------
    # Most common category
    # --------------------------
    if "most common" in question or "most frequent" in question:

        for col in categorical_columns:
            if col.lower() in question:
                value = df[col].mode()[0]
                return f"The most common value in {col} is '{value}'."

    # --------------------------
    # Unique values
    # --------------------------
    if "unique" in question:

        for col in df.columns:
            if col.lower() in question:
                return f"{col} contains {df[col].nunique()} unique values."

    # --------------------------
    # Column list
    # --------------------------
    if "column" in question:
        return ", ".join(df.columns)

    return (
        "Sorry, I couldn't understand the question.\n\n"
        "Try questions like:\n"
        "- How many rows?\n"
        "- What is the average sales?\n"
        "- What is the maximum age?\n"
        "- What is the most common city?"
    )