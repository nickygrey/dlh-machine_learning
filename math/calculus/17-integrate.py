#!/usr/bin/env python3
"""Module to calculate the integral of a polynomial."""


def poly_integral(poly, C=0):
    """Calculate the integral of a polynomial."""
    if type(poly) is not list or type(C) is not int:
        return None
    if len(poly) == 0:
        return None

    integral = [C]
    for i, coef in enumerate(poly):
        if type(coef) is not int and type(coef) is not float:
            return None
        val = coef / (i + 1)
        if val == int(val):
            val = int(val)
        integral.append(val)

    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
