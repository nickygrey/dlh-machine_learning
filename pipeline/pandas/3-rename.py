#!/usr/bin/env python3
"""Module to rename and convert columns in a pandas DataFrame."""
import pandas as pd


def rename(df):
    """Rename Timestamp column to Datetime and convert to datetime values.

    Args:
        df (pandas.DataFrame): The input DataFrame containing a Timestamp
            column.

    Returns:
        pandas.DataFrame: The modified DataFrame with only Datetime and
            Close columns.
    """
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')
    df = df.rename(columns={'Timestamp': 'Datetime'})
    return df[['Datetime', 'Close']]
