#!/usr/bin/env python3
"""Module to sort and transpose a pandas DataFrame."""


def flip_switch(df):
    """Sort the DataFrame in reverse chronological order and transpose it.

    Args:
        df: The input pandas DataFrame.

    Returns:
        The transformed pandas DataFrame.
    """
    return df.sort_index(ascending=False).T
