# visualization.py

import os
import matplotlib.pyplot as plt
import pandas as pd


# Create charts folder if it doesn't exist
os.makedirs("charts", exist_ok=True)


def bar_chart(df):
    """
    Create a bar chart for the first categorical column.
    """

    categorical = df.select_dtypes(include=["object", "category"])

    if categorical.empty:
        return None

    column = categorical.columns[0]

    counts = df[column].value_counts().head(10)

    plt.figure(figsize=(8,5))
    counts.plot(kind="bar", color="skyblue")

    plt.title(f"Top 10 {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.xticks(rotation=45)

    plt.tight_layout()

    path = "charts/bar_chart.png"

    plt.savefig(path)

    plt.close()

    return path


def pie_chart(df):
    """
    Create pie chart from first categorical column.
    """

    categorical = df.select_dtypes(include=["object", "category"])

    if categorical.empty:
        return None

    column = categorical.columns[0]

    counts = df[column].value_counts().head(5)

    plt.figure(figsize=(6,6))

    counts.plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.title(column)

    plt.ylabel("")

    plt.tight_layout()

    path = "charts/pie_chart.png"

    plt.savefig(path)

    plt.close()

    return path


def histogram(df):
    """
    Histogram of first numerical column.
    """

    numeric = df.select_dtypes(include=["number"])

    if numeric.empty:
        return None

    column = numeric.columns[0]

    plt.figure(figsize=(8,5))

    plt.hist(df[column], bins=20)

    plt.title(f"{column} Distribution")
    plt.xlabel(column)
    plt.ylabel("Frequency")

    plt.tight_layout()

    path = "charts/histogram.png"

    plt.savefig(path)

    plt.close()

    return path


def scatter_plot(df):
    """
    Scatter plot of first two numeric columns.
    """

    numeric = df.select_dtypes(include=["number"])

    if len(numeric.columns) < 2:
        return None

    x = numeric.columns[0]
    y = numeric.columns[1]

    plt.figure(figsize=(8,5))
    plt.scatter(df[x], df[y], alpha=0.7)

    plt.xlabel(x)
    plt.ylabel(y)

    plt.title(f"{x} vs {y}")

    plt.tight_layout()

    path = "charts/scatter_plot.png"

    plt.savefig(path)

    plt.close()

    return path


def generate_chart(df):
    """
    Automatically choose the best chart.
    """

    categorical = df.select_dtypes(include=["object", "category"])
    numeric = df.select_dtypes(include=["number"])

    if not categorical.empty:
        return bar_chart(df)

    elif len(numeric.columns) >= 2:
        return scatter_plot(df)

    elif len(numeric.columns) == 1:
        return histogram(df)

    return None