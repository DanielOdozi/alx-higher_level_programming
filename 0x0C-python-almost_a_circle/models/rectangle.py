#!/usr/bin/python3
'''class Rectangle'''
from models.base import Base


class Rectangle(Base):
    """Class that defines properties of Rectangle.

     Attributes:
        width (int): Width of the Rectangle.
        height (int): Height of the Rectangle.
        x (int): value.
        y (int): value.
        id (int): Identity of each instance.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Creates new instances of Rectangle.

        Args:
            width (int): Width of the Rectangle.
            height (int): Height of the Rectangle.
            x (int): value.
            y (int): value.
            id (int, optional): Identity of each instance. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width retriever.

        Returns:
            int: width of rectangle.
        """
        return self.__width

    @property
    def height(self):
        """Height retriever.

        Returns:
            int: height of rectangle.
        """
        return self.__height

    @property
    def x(self):
        """x retriever.

        Returns:
            int: x of rectangle.
        """
        return self.__x

    @property
    def y(self):
        """y retriever.

        Returns:
            int: y of rectangle.
        """
        return self.__y

    @width.setter
    def width(self, value):
        """Property setter for width of rectangle.

        Args:
            value (int): width of rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0.")
        self.__width = value

    @height.setter
    def height(self, value):
        """Property setter for height of rectangle.

        Args:
            value (int): height of rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0.")
        self.__height = value

    @x.setter
    def x(self, value):
        """Property setter for x of rectangle.

        Args:
            value (int): x of rectangle.

        Raises:
            TypeError: if x is not an integer.
            ValueError: if x is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Property setter for y of rectangle.

        Args:
            value (int): y of rectangle.

        Raises:
            TypeError: if y is not an integer.
            ValueError: if y is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of a Rectangle.

        Args:
            None

        Return:
            Returns the area of rectangle
        """
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #."""
        for i in range(self.__y):
            print()

        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        '''Prints a rectangle'''
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".
                format(self.id, self.__x, self.__y, self.__width,
                       self.__height))

    def update(self, *args):
        '''updates the args'''
        self.width = args[0]
        self.height = args[1]
        self.x = args[2]
        self.y = args[3]
