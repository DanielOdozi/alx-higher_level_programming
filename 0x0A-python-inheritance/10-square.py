#!/usr/bin/python3
'''class Square'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size):
        """Creates new instances of Square.

        Args:
            size (int): size of a square.
        """
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """Calculates the area of square.

        Returns: the current square area.
        """
        return self.__size ** 2
