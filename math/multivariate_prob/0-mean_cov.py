#!/usr/bin/env python3
"""Module to calculate mean and covariance of a dataset."""
import numpy as np


def mean_cov(X):
    """Calculate the mean and covariance matrix of a dataset.

    Args:
        X (numpy.ndarray): A 2D array of shape (n, d) containing the dataset.

    Returns:
        mean (numpy.ndarray): A 2D array of shape (1, d) containing the mean.
        cov (numpy.ndarray): A 2D array of shape (d, d) containing covariance.
    """
    if type(X) is not np.ndarray or len(X.shape) != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    n, d = X.shape

    if n < 2:
        raise ValueError("X must contain multiple data points")

    mean = np.mean(X, axis=0, keepdims=True)
    X_centered = X - mean
    cov = np.dot(X_centered.T, X_centered) / (n - 1)

    return mean, cov
