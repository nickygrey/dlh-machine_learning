#!/usr/bin/env python3
"""Function that performs matrix multiplication."""


def mat_mul(mat1, mat2):
    """Return a new multiplied matrix."""
    if len(mat1[0]) != len(mat2):
        return None

    result = []

    for row in range(len(mat1)):
        new_row = []

        for column in range(len(mat2[0])):
            value = 0

            for k in range(len(mat2)):
                value += mat1[row][k] * mat2[k][column]

            new_row.append(value)

        result.append(new_row)

    return result
