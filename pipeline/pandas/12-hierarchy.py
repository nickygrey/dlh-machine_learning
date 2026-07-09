#!/usr/bin/env python3
"""Module to rearrange and filter hierarchical dataframes."""
import pandas as pd

index = __import__('10-index').index


def hierarchy(df1, df2):
    """Concatenate two dataframes, swap index levels, sort, and slice.

    Args:
        df1: The coinbase pandas DataFrame.
        df2: The bitstamp pandas DataFrame.

    Returns:
        The multi-indexed, sorted, and sliced pandas DataFrame.
    """
    df1_indexed = index(df1)
    df2_indexed = index(df2)

    df = pd.concat([df2_indexed, df1_indexed],
                   keys=['bitstamp', 'coinbase'])

    # Swap levels to make Timestamp the leading index dimension
    df = df.swaplevel(0, 1)

    # Sort index chronologically to prepare for label slicing
    df = df.sort_index()

    # Slice the multi-index range inclusively
    return df.loc[1417411980:1417417980]
