#!/usr/bin/python3

def no_c(my_string):
    # Create a new string with characters that are not 'c' or 'C'
    new_string = ''.join(char for char in my_string if char not in ('c', 'C'))
    return new_string
