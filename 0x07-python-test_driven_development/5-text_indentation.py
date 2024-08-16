#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: '.', '?', and ':'.
    
    Parameters:
    text (str): The text to be formatted and printed.
    
    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Initialize variables
    result = ""
    should_indent = False
    
    for char in text:
        if char in '.?:':
            result += char + "\n\n"
            should_indent = True
        else:
            if should_indent and char == ' ':
                continue  # Skip spaces right after '.', '?', or ':'
            result += char
            should_indent = False
    
    # Print the result without leading or trailing spaces
    print(result.strip())
