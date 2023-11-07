#!/usr/bin/python3
'''class MyInt that inherits from int'''


class MyInt(int):
    """Class MyInt"""
    def __init__(self, value):
        """Creates new instances of class MyInt.

        Args:
            value (int): integer.
        """
        self.__value = value

    def __eq__(self, other):
        """The method equal

        Args:
            other (int): integer.

        Returns:
            boolean: True or False.
        """
        return self.__value != other

    def __ne__(self, other):
        """The method not equal

        Args:
            other (int): integer.

        Returns:
            boolean: True or False
        """
        return self.__value == other
