#!/usr/bin/python3
"""Contains definition of matrix_divided function"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number

    Args:
        matrix (list): A list of lists containing integers or floats
        div (int or float): Divisor of division operation.
            Must be either an integer or a float

    Returns:
        list: A list of lists containing integers or floats
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
    elif len(matrix) is 0:
        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
    else:
        for m in matrix:
            if not isinstance(m, list):
                raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
            if len(m) is 0:
                raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
            else:
                for n in m:
                    if not isinstance(n, (int, float)):
                        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
    if len(set([len(x) for x in matrix])) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    res = []
    for mm in matrix:
        res.append([round(float(m) / div, 2) for m in mm])
    return res
