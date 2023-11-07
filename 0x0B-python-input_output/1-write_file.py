#!/usr/bin/python3
'''function that writes a string to a text file (UTF8)'''


def write_file(filename="", text=""):
    """writes to a file and prints it to stdout.

    Args:
        filename: The .txt file to read.
        text: The text to put in a file.

    Raises:
        None.

    Prints:
        f.read(): prints the file to stdout.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
