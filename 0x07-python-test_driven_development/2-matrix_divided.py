#!/usr/bin/python3

"""
matrix division
"""


def matrix_divided(matrix, div):
    """
    matrix_division with div
    :param matrix:
    :param div:
    :return:new matrix with result
    """
    new_mat = []
    if matrix and type(matrix) is list:
        for row in matrix:
            if type(row) is not list:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row = []
            for i in row:
                if not isinstance(i, (int, float)):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                len_ = len(matrix[0])
                if len_ != len(row):
                    raise TypeError(
                        "Each row of the matrix must have the same size")
                if not isinstance(div, (int, float)):
                    raise TypeError("div must be a number")
                if div == 0:
                    raise ZeroDivisionError("division by zero")
                else:
                    new_row.append(round(i / div, 2))
            new_mat.append(new_row)
    return new_mat
