#!/usr/bin/python3
'''A function that prints a text with 2 new lines after each of these characters: ., ? and :'''


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The argument.

    Raises:
        TypeError: text must be a string.

    Returns:
        None.
    
    Print:
         a text with 2 new lines after each of these characters.
    """
    result = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for i in text:
        if i == '?':
            result += '?\n'
            result += '\n'
        elif i == '.':
            result += '.\n'
            result += '\n'
        elif i == ':':
            result += ':\n'
            result += '\n'
        else:
            result += i
    print(result)