#!/usr/bin/env python3
"""Function that adds two 2D matrices element-wise."""


def add_matrices2D(mat1, mat2):
    """Return a new matrix with added values."""
    if len(mat1) != len(mat2):
        return None

    if len(mat1[0]) != len(mat2[0]):
        return None

    result = []

    for row in range(len(mat1)):
        new_row = []

        for column in range(len(mat1[row])):
            new_row.append(mat1[row][column] + mat2[row][column])

        result.append(new_row)

    return result
