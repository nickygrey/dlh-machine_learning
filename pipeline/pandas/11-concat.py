#!/usr/bin/env python3
"""Module to concatenate two dataframes with hierarchical indexing."""
import pandas as pd

index = __import__('10-index').index


def concat(df1, df2):
    """Index, filter, and concatenate two cryptocurrency dataframes.

    Args:
        df1: The coinbase pandas DataFrame.
        df2: The bitstamp pandas DataFrame.

    Returns:
        The concatenated pandas DataFrame with keys 'bitstamp' and 'coinbase'.
    """
    df1_indexed = index(df1)
    df2_indexed = index(df2)

    df2_filtered = df2_indexed.loc[:1417411920]

    result = pd.concat([df2_filtered, df1_indexed],
                       keys=['bitstamp', 'coinbase'])

    return result
