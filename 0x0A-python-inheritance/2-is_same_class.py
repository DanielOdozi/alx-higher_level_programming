#!/usr/bn/python3
'''function that returns True if the object is exactly an instance of the specified class'''


def is_same_class(obj, a_class):
    """function that returns True if the object is exactly an instance of the specified class.

    Args:
        obj (object): object to check if isnistance of the class.
        a_class (class): The class.
    
    Returns:
        True or False
    """
    return type(obj) == a_class
