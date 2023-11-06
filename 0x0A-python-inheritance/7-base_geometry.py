#!/usr/bin/python3
'''class BaseGeometry'''


class BaseGeometry:
    """class BaseGeometry.

    Args:
        None

    Returns:
        None
    """
    def area(self):
        """function that raises an Exception.

        Args:
            None.

        Returns:
            None.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value.

        Args:
            name (str): name of the object.
            value (int): value of the property.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
