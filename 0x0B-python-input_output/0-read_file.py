#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The path to the file to be read. Defaults to an empty
        string.

    This function uses the `with` statement to open and read the file
    to ensure proper resource management.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print(file.read(), end='')
    except FileNotFoundError:
        pass
