#!/usr/bin/python3
'''function that returns True if the object is an instance of'''


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance of.

    Args:
        obj (object): object to check if isnistance of the class.
        a_class (class): The class.

    Returns:
        True or False
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
