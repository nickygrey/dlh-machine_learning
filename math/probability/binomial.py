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

    def pmf(self, k):
        """Calculate the value of the PMF for a given number of successes.

        Args:
            k (int): The number of successes.

        Returns:
            float: The PMF value for k.
        """
        if type(k) is not int:
            k = int(k)
        if k < 0 or k > self.n:
            return 0

        fact_n = 1
        for i in range(1, self.n + 1):
            fact_n *= i

        fact_k = 1
        for i in range(1, k + 1):
            fact_k *= i

        fact_nk = 1
        for i in range(1, self.n - k + 1):
            fact_nk *= i

        combination = fact_n // (fact_k * fact_nk)
        pmf_val = combination * (self.p ** k) * ((1 - self.p) ** (self.n - k))
        return float(pmf_val)
