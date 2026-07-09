#!/usr/bin/env python3
"""Module to fill missing values in a pandas DataFrame."""


def fill(df):
    """Clean and fill missing values in the cryptocurrency dataset.

    Args:
        df: The input pandas DataFrame.

    Returns:
        The modified pandas DataFrame with filled values.
    """
    df = df.drop(columns=['Weighted_Price'])

    df['Close'] = df['Close'].ffill()

    df['Open'] = df['Open'].fillna(df['Close'])
    df['High'] = df['High'].fillna(df['Close'])
    df['Low'] = df['Low'].fillna(df['Close'])

    df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
    df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)

    return df
