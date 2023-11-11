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

    def __str__(self):
        '''Prints a square'''
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.size,))
