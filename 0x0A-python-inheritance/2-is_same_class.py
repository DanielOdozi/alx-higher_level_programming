#!/usr/bn/python3
'''function that checks if the object is an instance of specified class'''


def is_same_class(obj, a_class):
    """function that checks if the object is an instance of specified class.

    Args:
        obj (object): object to check if isnistance of the class.
        a_class (class): The class.

    Returns:
        True or False
    """
    return type(obj) == a_class
