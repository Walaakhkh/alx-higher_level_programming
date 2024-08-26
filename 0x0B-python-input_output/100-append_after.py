#!/usr/bin/python3
""" Function to insert a line of text after each line containing a specific
string.
"""


def append_after(filename="", search_string="", new_string=""):
    """ Inserts a line of text after each line containing a specific string.

    Args:
        filename (str): Name of the file to modify.
        search_string (str): String to search for in the file.
        new_string (str): Line of text to insert after each occurrence
        of search_string.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
