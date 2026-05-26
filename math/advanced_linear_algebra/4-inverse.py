#!/usr/bin/env python3
"""Function that calculates the inverse matrix."""


def determinant(matrix):
    """Return determinant of a matrix."""
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return ((matrix[0][0] * matrix[1][1]) -
                (matrix[0][1] * matrix[1][0]))

    det = 0

    for i in range(len(matrix)):
        small = []

        for row in matrix[1:]:
            small.append(row[:i] + row[i + 1:])

        det += ((-1) ** i) * matrix[0][i] * determinant(small)

    return det


def cofactor(matrix):
    """Return cofactor matrix."""
    if len(matrix) == 1:
        return [[1]]

    result = []

    for i in range(len(matrix)):
        new_row = []

        for j in range(len(matrix)):
            small = []

            for row in (matrix[:i] + matrix[i + 1:]):
                small.append(row[:j] + row[j + 1:])

            value = determinant(small)
            value = value * ((-1) ** (i + j))

            new_row.append(value)

        result.append(new_row)

    return result


def adjugate(matrix):
    """Return adjugate matrix."""
    cof = cofactor(matrix)

    result = []

    for i in range(len(cof[0])):
        new_row = []

        for j in range(len(cof)):
            new_row.append(cof[j][i])

        result.append(new_row)

    return result


def inverse(matrix):
    """Return inverse matrix."""
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a list of lists")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise ValueError("matrix must be a non-empty square matrix")

    for row in matrix:
        if len(row) != len(matrix):
            raise ValueError("matrix must be a non-empty square matrix")

    det = determinant(matrix)

    if det == 0:
        return None

    if len(matrix) == 1:
        return [[1 / matrix[0][0]]]

    adj = adjugate(matrix)

    result = []

    for row in adj:
        new_row = []

        for value in row:
            new_row.append(value / det)

        result.append(new_row)

    return result
