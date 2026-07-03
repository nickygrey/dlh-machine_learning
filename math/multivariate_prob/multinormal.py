#!/usr/bin/env python3
"""Module that defines a Multivariate Normal distribution class."""
import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution."""

    def __init__(self, data):
        """Initialize the distribution with a dataset.

        Args:
            data (numpy.ndarray): A 2D array of shape (d, n) containing
                the dataset.
        """
        if type(data) is not np.ndarray or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)
        data_centered = data - self.mean
        self.cov = np.dot(data_centered, data_centered.T) / (n - 1)
