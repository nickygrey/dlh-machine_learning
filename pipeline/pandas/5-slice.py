#!/usr/bin/env python3
"""Module to slice specific columns and rows from a DataFrame."""


def slice(df):
    """Extract specific columns and select every 60th row.

    Args:
        df: The input pandas DataFrame.

    Returns:
        The sliced pandas DataFrame.
    """
    columns = ['High', 'Low', 'Close', 'Volume_(BTC)']
    return df[columns].iloc[::60]
