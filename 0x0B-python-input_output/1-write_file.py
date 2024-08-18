#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of
    characters written.

    Args:
        filename (str): The path to the file where the text will be written.
        Defaults to an empty string.
        text (str): The string to be written to the file. Defaults to an
        empty string.

    Returns:
        int: The number of characters written to the file.

    This function uses the `with` statement to open and write to the file
    to ensure proper resource management. The file is created if it does
    not exist, and its content is overwritten if it does.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_characters = file.write(text)
    return num_characters
