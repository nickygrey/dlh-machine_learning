#!/usr/bin/env python3
"""Calculate determinant of a matrix"""


def determinant(matrix):
    """Calculate the determinant of a matrix"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
    
    # ... rest of clean, simple code ...
    return det
