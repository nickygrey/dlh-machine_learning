#!/usr/bin/env python3
"""This module calculates the derivative of a polynomial."""


def poly_derivative(poly):
    """Returns a list of coefficients representing the polynomial derivative."""
    if type(poly) is not list or len(poly) == 0:
        return None

    for coef in poly:
        if type(coef) is not int and type(coef) is not float:
            return None

    # Compute derivative coefficients: coefficient * power
    derivative = [poly[i] * i for i in range(1, len(poly))]

    # If the list is empty or evaluates to 0, ensure it returns [0]
    if len(derivative) == 0:
        return [0]

    # Clean up any trailing zeros from the derivative list
    while len(derivative) > 1 and derivative[-1] == 0:
        derivative.pop()

    return derivative
