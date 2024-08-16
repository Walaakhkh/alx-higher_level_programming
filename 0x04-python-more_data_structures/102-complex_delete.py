#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    # Create a list of keys to delete
    keys_to_delete = [key for key in a_dictionary if a_dictionary[key] == value]
    
    # Delete the keys from the dictionary
    for key in keys_to_delete:
        del a_dictionary[key]
    
    return a_dictionary
