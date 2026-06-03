#!/usr/bin/env python3
"""This module calculates the sum of squares up to a given number."""


def summation_i_squared(n):
    """Returns the sum of squares from 1 to n using an algebraic formula."""
    if type(n) is not int or n < 1:
        return None

    # Using the math formula for sum of squares since loops are banned
    result = (n * (n + 1) * (2 * n + 1)) // 6
    return result
