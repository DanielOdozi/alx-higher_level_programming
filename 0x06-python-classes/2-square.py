#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Class that defines properties of a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size)
    """
    def __init__(self, size=0):
        """Initializes an instance of the Square class.

        Args:
            self (Square): The current instance of the Square class.
            size (int): The size of the square.

        Returns:
            None

        Raises:
            TypeError: If size is less than 0.
            ValueError: If size is not an integer.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer.")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
