#!/usr/bin/python3


"""Defines elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The matrix of integers or floats.
        div (int or float): The number to divide all elements by
    """

    if not isinstance(matrix, list)\
            or not all(isinstance(raw, list) for raw in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(n, (int, float)) for row in matrix for n in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for raw in matrix:
        resulted_raw = [round(n/div, 2) for n in raw]
        new_matrix.append(resulted_raw)
    return new_matrix
