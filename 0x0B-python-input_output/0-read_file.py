#!/usr/bin/python3
'''function that reads a text file (UTF8) and prints it to stdout'''


def read_file(filename=""):
    """Reads a file and prints it to stdout.

    Args:
        filename: The .txt file to read.

    Raises:
        None.

    Prints:
        f.read(): prints the file to stdout.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end='')
