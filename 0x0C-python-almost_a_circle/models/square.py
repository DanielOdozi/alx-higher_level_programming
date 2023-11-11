#!/usr/bin/python3
'''class Square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that defines properties of Square.

     Attributes:
        width (int): Width of the square.
        height (int): height of the square.
        size (int): size of the Square.
        x (int): value.
        y (int): value.
        id (int): Identity of each instance.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Creates new instances of Square.

        Args:
            width (int): Width of the square.
            height (int): height of the square.
            size (int): size of the Square.
            x (int): value.
            y (int): value.
            id (int, optional): Identity of each instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size retriever.

        Returns:
            int: size of square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Property setter for size of square.

        Args:
            value (int): width of square.
            value (int): height of square.
        """
        self.width = value
        self.height = value

    def __str__(self):
        '''Prints a square'''
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.size,))

    def update(self, *args, **kwargs):
        '''Updates the attributes using *args and **kwargs'''
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
