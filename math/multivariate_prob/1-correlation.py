#!/usr/bin/env python3
"""Module to calculate a correlation matrix from a covariance matrix."""
import numpy as np


def correlation(C):
    """Calculate the correlation matrix from a covariance matrix.

    Args:
        C (numpy.ndarray): A 2D square matrix of shape (d, d).

    Returns:
        numpy.ndarray: A 2D square matrix containing the correlation matrix.
    """
    if type(C) is not np.ndarray:
        raise TypeError("C must be a numpy.ndarray")
    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    v = np.diag(C)
    stddev = np.sqrt(v)
    outer_std = np.outer(stddev, stddev)
    return C / outer_std
