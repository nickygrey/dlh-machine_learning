#!/usr/bin/env python3
"""Function that slices numpy matrices."""


def np_slice(matrix, axes={}):
    """Return a sliced matrix."""
    slices = [slice(None)] * len(matrix.shape)

    for axis, values in axes.items():
        slices[axis] = slice(*values)

    return matrix[tuple(slices)]
