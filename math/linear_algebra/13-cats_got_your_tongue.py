#!/usr/bin/env python3
"""Function that concatenates numpy arrays"""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Return concatenated matrices."""
    return np.concatenate((mat1, mat2), axis=axis)
