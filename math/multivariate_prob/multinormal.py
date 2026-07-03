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

    def pdf(self, x):
        """Calculate the Probability Density Function (PDF) at a data point.

        Args:
            x (numpy.ndarray): A 2D array of shape (d, 1) containing
                the data point.

        Returns:
            float: The value of the PDF at data point x.
        """
        if type(x) is not np.ndarray:
            raise TypeError("x must be a numpy.ndarray")

        d = self.mean.shape[0]

        if len(x.shape) != 2 or x.shape[0] != d or x.shape[1] != 1:
            raise ValueError("x must have the shape ({}, 1)".format(d))

        det = np.linalg.det(self.cov)
        inv = np.linalg.inv(self.cov)

        diff = x - self.mean
        exponent = -0.5 * np.dot(np.dot(diff.T, inv), diff)
        norm_coeff = 1.0 / np.sqrt(((2 * np.pi) ** d) * det)
        pdf_val = norm_coeff * np.exp(exponent)

        return float(pdf_val[0][0])
