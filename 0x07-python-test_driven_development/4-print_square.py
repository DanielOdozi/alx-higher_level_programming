#!/usr/bin/python3
'''A function that prints a square with the character #'''


def print_square(size):
    """prints a square with the character #.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: size must be an integer.
        ValueError: size must be >= 0.

    Returns:
        None.
    
    Print:
        My name is <first name> <last name>.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0.")
    elif not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
