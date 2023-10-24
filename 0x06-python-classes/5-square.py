#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Class that defines properties of a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size)
    """
    def __init__(self, size=0) -> None:
        """Initializes an instance of the Square class.

        Args:
            self (Square): The current instance of the Square class.
            size (int): The size of the square.
        """
        self.__size = size

    def area(self):
        """Calculates the area of square.

        Returns: the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #
        """

        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * (self.__size))

    @property
    def size(self):
        """Returns the size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size.

        Args:
            value (int): size of a square (1 side).

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
