#!/usr/bin/env python3
"""Module to sort a pandas DataFrame by a specific column."""


def high(df):
    """Sort the DataFrame by the High price column in descending order.

    Args:
        df: The input pandas DataFrame.

    Returns:
        The sorted pandas DataFrame.
    """
    return df.sort_values(by='High', ascending=False)
