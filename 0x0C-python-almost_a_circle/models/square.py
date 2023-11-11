#!/usr/bin/python3
'''class Square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that defines properties of Square.

     Attributes:
        width (int): Width of the Rectangle.
        height (int): Height of the Rectangle.
        x (int): value.
        y (int): value.
        id (int): Identity of each instance.
    """
    def __init__(self, size, x=0, y=0, id=None):