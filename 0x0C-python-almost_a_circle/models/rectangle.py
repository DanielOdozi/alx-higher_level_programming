#!/usr/bin/python3
'''class Rectangle'''
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.width

    @property
    def height(self):
        return self.height

    @property
    def x(self):
        return self.x

    @property
    def y(self):
        return self.y

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(value))
        self.width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(value))
        self.height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(value))
        self.x = value

    @y.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(value))
        self.y = value
