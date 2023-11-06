#!/usr/bin/python3
'''function that returns True if the object is an instance of'''


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance of.

    Args:
        obj (object): object to check if isnistance of the class.
        a_class (class): The class.

    Returns:
        True or False
    """
    return isinstance(obj, a_class)
