#!/usr/bin/env python3
"""Function that returns the shape of a matrix."""


def matrix_shape(matrix):
    """Return matrix dimensions as a list."""
    shape = []

    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]

    return shape
