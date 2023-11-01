#!/usr/bin/python3
"""Defines a class Rectangle."""


class Rectangle:
    """Class that defines properties of a Rectangle.

    Attributes:
        None

    Methods:
        __init__(self)
    """
    def __init__(self, width=0, height=0):
        """Initializes an instance of the Rectangle class.

        Args:
            self: The current instance of the Rectangle class.

        Returns:
            None
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Returns the width of a rectangle
        """
        return self.__width

    @property
    def height(self):
        """Returns the height of a rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Property setter for width.

        Args:
            value (int): width of a rectangle.

        Raises:
            TypeError: width must be an integer.
            ValueError: width must be >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Property setter for height.

        Args:
            value (int): height of a rectangle.

        Raises:
            TypeError: height must be an integer.
            ValueError: height must be >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
