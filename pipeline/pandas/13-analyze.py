#!/usr/bin/env python3
"""Module to compute descriptive statistics of a DataFrame."""


def analyze(df):
    """Compute descriptive statistics for all columns except Timestamp.

    Args:
        df: The input pandas DataFrame.

    Returns:
        The descriptive statistics as a pandas DataFrame.
    """
    return df.drop(columns=['Timestamp']).describe()
