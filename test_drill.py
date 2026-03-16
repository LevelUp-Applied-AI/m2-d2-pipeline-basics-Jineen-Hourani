"""
Module 2 — Drill 2: Learner Test File

Write your two pytest test functions below.
The autograder will run these as part of the CI check.
"""

import pandas as pd
import numpy as np
from drill_functions import clean_column, compute_revenue


def test_clean_column():
    # Create a pd.Series with at least one NaN value
    series_with_nan = pd.Series([10.0, 20.0, np.nan, 30.0, 15.0, np.nan, 25.0])
    # Call clean_column() on it
    result = clean_column(series_with_nan)
    # Assert no NaN values remain in the result
    assert result.isna().sum() == 0, "There should be no NaN values left."
    # Assert the NaN was filled with the correct median value
    assert result[2] == result[5] == 20.0, "The NaN should have been replaced by the median (20.0)."


def test_compute_revenue():
    # Create two small pd.Series (quantity and price)
    quantity = pd.Series([2, 5, 10])
    price = pd.Series([10.0, 20.0, 5.0])
    # Call compute_revenue() on them
    result = compute_revenue(quantity, price)
    # Assert the result matches the expected element-wise product
    pd.testing.assert_series_equal(result, pd.Series([20.0, 100.0, 50.0]))
