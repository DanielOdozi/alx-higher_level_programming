#!/usr/bin/python3
'''A function that prints My name is <first name> <last name>'''


def say_my_name(first_name, last_name=""):
    """Divids a matrix by the div input.

    Args:
        first_name (str): The first name.
        last_name (str): The last name.

    Raises:
        TypeError: first_name must be a string.
        TypeError: last_name must be a string.

    Returns:
        None.
    
    Print:
        My name is <first name> <last name>.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))
