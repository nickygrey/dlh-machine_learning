#!/usr/bin/env python3
"""Function that concatenates two 2D matrices."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Return a new concatenated matrix."""
    result = []

    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None

        for row in mat1:
            result.append(row[:])

        for row in mat2:
            result.append(row[:])

    elif axis == 1:
        if len(mat1) != len(mat2):
            return None

        for i in range(len(mat1)):
            result.append(mat1[i][:] + mat2[i][:])

    else:
        return None

    return result
