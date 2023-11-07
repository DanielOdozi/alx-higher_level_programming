#!/usr/bin/python3
'''function that writes an Object to a text file'''
import json


def load_from_json_file(filename):
    """returns the JSON representation.

    Args:
        filename: The txt file to read from.

    Raises:
        None.

    Return:
        json.load(): returns an Object to a text file.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
