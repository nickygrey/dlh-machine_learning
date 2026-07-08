#!/usr/bin/env python3
"""Module to load data from a file into a pandas DataFrame."""
import pandas as pd


def from_file(filename, delimiter):
    """Load data from a file as a pandas DataFrame.

    Args:
        filename (str): The path to the file to load.
        delimiter (str): The column separator character.

    Returns:
        pandas.DataFrame: The loaded DataFrame.
    """
    return pd.read_csv(filename, sep=delimiter)
