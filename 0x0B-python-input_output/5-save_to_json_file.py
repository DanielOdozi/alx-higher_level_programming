#!/usr/bin/python3
'''function that writes an Object to a text file'''
import json


def save_to_json_file(my_obj, filename):
    """returns the JSON representation.

    Args:
        my_obj: The object file to read.
        filename: The txt file to write to.

    Raises:
        None.

    Return:
        json.loads(): returns an Object to a text file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
