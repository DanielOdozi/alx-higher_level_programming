#!/usr/bin/python3
'''A function to add two numbers'''


def add_integer(a, b=98):
    """Adds two integer and/or float values.

    Args:
        a (int): First value
        b (int, optional): Second value. Defaults to 98.

    Raises:
        TypeError: If a and b are not integers or floats.

    Returns:
        int: Sum of a and b.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    elif isinstance(b, float):
        b = int(b)

    return a + b
