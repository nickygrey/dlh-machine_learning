#!/usr/bin/env python3
"""Module to set a column as the index of a pandas DataFrame."""


def index(df):
    """Set the Timestamp column as the index of the DataFrame.

    Args:
        df: The input pandas DataFrame.

    Returns:
        The modified pandas DataFrame with Timestamp as the index.
    """
    return df.set_index('Timestamp')
