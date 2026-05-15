#!/usr/bin/env python3
"""Function that adds matrices recursively."""


def add_matrices(mat1, mat2):
    """Return a new matrix containing summed values."""
    if type(mat1) != type(mat2):
        return None

    if isinstance(mat1, list):
        if len(mat1) != len(mat2):
            return None

        result = []

        for i in range(len(mat1)):
            value = add_matrices(mat1[i], mat2[i])

            if value is None:
                return None

            result.append(value)

        return result

    return mat1 + mat2
