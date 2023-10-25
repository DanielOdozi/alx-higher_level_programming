#!?usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines a square.

    Attributes:
        size: The size of the square.
        position: The position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Creates new instances of node.

        Args:
            __size : size field of square.
            __postion: position field of square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size field instance.

        Returns: the size field of a square.
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """Propery setter for size.

        Args:
            value (int): size field of a square.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @property
    def position(self):
        """Retrieves the position field instance.

        Returns: the position field of a square.
        """
        return self.__position
    
    @position.setter
    def position(self, value):
        """Propery setter for size.

        Args:
            value (int): size field of a square.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        for i in value:
            if i < 0:
                raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value
    
    def my_print(self):
        """prints in stdout the square with the character #
        """

        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))

    def __str__(self):
        """Prints square offsetting it by position with symbol #

        Returns: The square.
        """
        if self.__size == 0:
            return ''
        new_lines = '\n' * self.position[1]
        spaces = ' ' * self.position[0]
        hashes = '#' * self.size
        return new_lines + '\n'.join(spaces + hashes for e in range(self.size))