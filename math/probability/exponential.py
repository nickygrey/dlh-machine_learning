#!/usr/bin/env python3
"""Module that defines the Exponential distribution class."""


class Exponential:
    """Class that represents an exponential distribution."""

    def __init__(self, data=None, lambtha=1.):
        """Initialize Exponential distribution instance.

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
            self.lambtha = float(len(data) / sum(data))

    def pdf(self, x):
        """Calculate the value of the PDF for a given time period.

        Args:
            x (float): The time period.

        Returns:
            float: The PDF value for x.
        """
        if x < 0:
            return 0

        e = 2.7182818285
        return self.lambtha * (e ** (-self.lambtha * x))

    def cdf(self, x):
        """Calculate the value of the CDF for a given time period.

        Args:
            x (float): The time period.

        Returns:
            float: The CDF value for x.
        """
        if x < 0:
            return 0

        e = 2.7182818285
        return 1 - (e ** (-self.lambtha * x))
