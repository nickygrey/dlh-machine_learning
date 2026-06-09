#!/usr/bin/env python3
"""Module that defines the Poisson distribution class."""


class Poisson:
    """Class that represents a Poisson distribution."""

    def __init__(self, data=None, lambtha=1.):
        """Initialize Poisson distribution instance.

        Args:
            data (list): A list of data points to estimate the distribution.
            lambtha (float): The expected number of occurrences.
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))
