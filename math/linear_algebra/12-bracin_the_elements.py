#!/usr/bin/env python3
"""Function that performs element-wise add, subt, mul, and div"""


def np_elementwise(mat1, mat2):
    """Return element-wise add, sub, mult, and div of two matrices"""
    return (mat1 + mat2,
            mat1 - mat2,
            mat1 * mat2,
            mat1 / mat2)
