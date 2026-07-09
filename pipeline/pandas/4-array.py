#!/usr/bin/env python3
"""Module to extract specific data from a DataFrame as a numpy array."""


def array(df):
    """Extract the last 10 rows of High and Close columns as a numpy array.

    Args:
        df: The input pandas DataFrame.

    Returns:
        The last 10 rows of the High and Close columns as a numpy array.
    """
    return df[['High', 'Close']].tail(10).to_numpy()
