#!/usr/bin/python3
'''A function to divide matrix'''


def matrix_divided(matrix, div):
    """Divids a matrix by the div input.

    Args:
        matrix (int): The matrix data to be divided.
        div (int): The div is the data the matrix will be dvided with.

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats.
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number.
        ZeroDivisionError: division by zero

    Returns:
        A new matrix.
    """
    new_matrix = []
    first_row_length = len(matrix[0])
    if not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
    for row in matrix:
        if len(row) != first_row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats.")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)
    return new_matrix
