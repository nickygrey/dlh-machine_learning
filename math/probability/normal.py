#!/usr/bin/env python3
"""Module that defines the Normal distribution class."""


class Normal:
    """Class that represents a normal distribution."""

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initialize Normal distribution instance.

        Args:
            data (list): A list of data points to estimate the distribution.
            mean (float): The mean of the distribution.
            stddev (float): The standard deviation of the distribution.
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.mean = float(sum(data) / len(data))
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)
            self.stddev = float(variance ** 0.5)

    def z_score(self, x):
        """Calculate the z-score of a given x-value.

        Args:
            x (float): The x-value.

        Returns:
            float: The z-score of x.
        """
        return float((x - self.mean) / self.stddev)

    def x_value(self, z):
        """Calculate the x-value of a given z-score.

        Args:
            z (float): The z-score.

        Returns:
            float: The x-value of z.
        """
        return float(self.mean + (z * self.stddev))
