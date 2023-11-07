#!/usr/bin/python3
'''function that returns the JSON representation of an object (string)'''
import json


def from_json_string(my_str):
    """returns the JSON representation of an object (string).

    Args:
        my_str: The object file to read.

    Raises:
        None.

    Return:
        json.loads():  returns an object represented by a JSON string.
    """
    return json.loads(my_str)
