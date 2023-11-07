#!/usr/bin/python3
'''function that returns the JSON representation of an object (string)'''
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string).

    Args:
        my_obj: The object file to read.

    Raises:
        None.

    Return:
        json.dumps(): return the string reresentation of an object.
    """
    return json.dumps(my_obj)
