#!/usr/bin/env python3
"""Module that defines the likelihood function for a binomial distribution."""
import numpy as np


def likelihood(x, n, P):
    """Calculate the likelihood of obtaining the data for each probability in P.

    Args:
        x (int): The number of patients that develop severe side effects.
        n (int): The total number of patients observed.
        P (numpy.ndarray): A 1D array containing various hypothetical
            probabilities of developing severe side effects.

    Returns:
        numpy.ndarray: A 1D array containing the likelihood for each
            probability in P, respectively.
    """
    if type(n) is not int or n <= 0:
        raise ValueError("n must be a positive integer")
    if type(x) is not int or x < 0:
        msg = "x must be an integer that is greater than or equal to 0"
        raise ValueError(msg)
    if x > n:
        raise ValueError("x cannot be greater than n")
    if type(P) is not np.ndarray or len(P.shape) != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")

    num = 1
    den = 1
    for i in range(1, x + 1):
        num *= (n - x + i)
        den *= i
    comb = num // den

    return comb * (P ** x) * ((1 - P) ** (n - x))
