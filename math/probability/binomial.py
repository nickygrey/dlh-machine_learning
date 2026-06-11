#!/usr/bin/env python3
"""Module that defines the Binomial distribution class."""


class Binomial:
    """Class that represents a binomial distribution."""

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize Binomial distribution instance.

        Args:
            data (list): A list of data points to estimate the distribution.
            n (int): The number of Bernoulli trials.
            p (float): The probability of a success.
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)

            p_initial = 1.0 - (variance / mean)
            n_estimated = mean / p_initial

            self.n = int(round(n_estimated))
            self.p = float(mean / self.n)
