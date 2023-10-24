#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Class that defines properties of a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self)
    """
    def __init__(self, size: int) -> None:
        """Initializes an instance of the Square class.

        Args:
            self (Square): The current instance of the Square class.
            size (int): The size of the square.

        Returns:
            None
        """
        self.__size = size
