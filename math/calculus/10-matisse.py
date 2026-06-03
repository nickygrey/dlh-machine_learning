#!/usr/bin/env python3
"""Module to calculate the derivative of a polynomial."""


def poly_derivative(poly):
    """Calculate the derivative of a polynomial."""
    if type(poly) is not list or len(poly) == 0:
        return None

    for coef in poly:
        if type(coef) is not int and type(coef) is not float:
            return None

    derivative = [poly[i] * i for i in range(1, len(poly))]

    if len(derivative) == 0:
        return [0]

    while len(derivative) > 1 and derivative[-1] == 0:
        derivative.pop()

    return derivative
