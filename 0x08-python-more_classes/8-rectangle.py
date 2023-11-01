#!/usr/bin/python3
"""Defines a class Rectangle."""


class Rectangle:
    """Class that defines properties of a Rectangle.

    Attributes:
        number_of_instances

    Methods:
        __init__(self)
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes an instance of the Rectangle class.

        Args:
            self: The current instance of the Rectangle class.

        Returns:
            None
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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

    def area(self):
        """Returns the area of a rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """Returns the perimeter of a rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.height + self.width)

    def __str__(self):
        """Prints the rectangle with the character # .

        Returns:
            str: the rectangle
        """
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append(str(self.print_symbol))
            rectangle.append("\n")

        # remove blank line
        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """return a string representation of the rectangle.

        Returns:
            repr: the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance of a class
        """
        print("{:s}".format("Bye rectangle..."))
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Computes the area of two rectangles and compares them.

        Args:
            rect_1 (Rectangle): first rectangle.
            rect_2 (Rectangle): second rectangle.

        Returns:
            Rectangle: the rectangle with the biggest area else rect_1 if
            areas are equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        
        if area_1 < area_2:
            return rect_2
        elif area_2 < area_1:
            return rect_1
        else:
            return rect_1
