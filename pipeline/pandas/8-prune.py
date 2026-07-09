#!/usr/bin/env python3
"""Module to prune NaN values from a specific column in a DataFrame."""


def prune(df):
    """Remove any entries where the Close column has NaN values.

    Args:
        df: The input pandas DataFrame.

    Returns:
        The pruned pandas DataFrame.
    """
    return df.dropna(subset=['Close'])
