#!/usr/bin/python3
'''function that appends a string to a text file (UTF8)'''


def append_write(filename="", text=""):
    """appends to the end of a file and prints it to stdout.

    Args:
        filename: The .txt file to read.
        text: The text to put in a file.

    Raises:
        None.

    Prints:
        f.write(): appends to the end of the file.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
