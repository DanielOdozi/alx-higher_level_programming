#!/usr/bin/python3
'''function that appends a string to a text file (UTF8)'''


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text into a file after each line containing.

    Args:
        filename: The .txt file to read and update.
        search_string: The specific string to search for in each line.
        new_string: The line of text to insert after lines.

    Raises:
        None.

    Prints:
        Updated file content.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        with open(filename, 'w', encoding='utf-8') as g:
            for line in lines:
                g.write(line)
                if search_string in line:
                    g.write(new_string)

    except Exception as e:
        print(f"An error occurred: {e}")
