#!/usr/bin/env python3
"""Function that returns the transpose of a matrix."""


def matrix_transpose(matrix):
    """Return transposed matrix."""
    new_matrix = []

    for column in range(len(matrix[0])):
        new_row = []

        for row in range(len(matrix)):
            new_row.append(matrix[row][column])

        new_matrix.append(new_row)

    return new_matrix