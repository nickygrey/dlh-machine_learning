#!/usr/bin/env python3
"""Module to extract specific data from a DataFrame as a numpy array."""
import pandas as pd


def array(df):
    """Extract the last 10 rows of High and Close columns as a numpy array.

    Args:
        df (pandas.DataFrame): The input DataFrame.

    Returns:
        numpy.ndarray: The last 10 rows of the High and Close columns.
    """
    return df[['High', 'Close']].tail(10).to_numpy()
