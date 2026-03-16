"""
Module 2 — Drill 2: Pipeline Basics

Write the two functions below from memory.
Remove the TODO: comments and pass statements as you implement each function.
Do not change the function signatures.
"""

import pandas as pd


def clean_column(series):
    """Fill NaN values with the series median. Returns the cleaned Series.

    Args:
        series (pd.Series): A pandas Series that may contain NaN values.

    Returns:
        pd.Series: The Series with NaN values replaced by the median.
    """
    cleaned_series = series.fillna(series.median())
    return cleaned_series


def compute_revenue(quantity, price):
    """Multiply quantity and price element-wise. Returns a revenue Series.

    Args:
        quantity (pd.Series): A Series of unit quantities.
        price (pd.Series): A Series of unit prices.

    Returns:
        pd.Series: Element-wise product of quantity and price.
    """
    revenue = quantity * price
    return revenue
    
