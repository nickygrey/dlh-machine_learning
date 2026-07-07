#!/usr/bin/env python3
"""Module to convert a numpy ndarray to a pandas DataFrame."""
import pandas as pd


def from_numpy(array):
    """Create a pd.DataFrame from a np.ndarray with alphabetical columns.

    Args:
        array (numpy.ndarray): The array from which to create the DataFrame.

    Returns:
        pandas.DataFrame: The newly created DataFrame.
    """
    cols = array.shape[1]
    col_names = [chr(i) for i in range(65, 65 + cols)]
    return pd.DataFrame(array, columns=col_names)
