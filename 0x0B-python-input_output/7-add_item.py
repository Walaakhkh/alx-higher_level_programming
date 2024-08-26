#!/usr/bin/python3
""" Script that adds all arguments to a Python list, and then save them
to a file"""


import sys
import importlib.util

# Function to dynamically load a module from a given filename
def load_module_from_file(module_name, filename):
    spec = importlib.util.spec_from_file_location(module_name, filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    filename = 'add_item.json'
    
    # Load the save_to_json_file and load_from_json_file functions
    save_to_json_file_module = load_module_from_file('save_to_json_file', '5-save_to_json_file.py')
    load_from_json_file_module = load_module_from_file('load_from_json_file', '6-load_from_json_file.py')
    
    save_to_json_file = save_to_json_file_module.save_to_json_file
    load_from_json_file = load_from_json_file_module.load_from_json_file

    # Try to load the existing list from the file
    try:
        items_list = load_from_json_file(filename)
    except FileNotFoundError:
        items_list = []
    
    # Add command line arguments to the list (excluding the script name)
    items_list.extend(sys.argv[1:])
    
    # Save the updated list to the file
    save_to_json_file(items_list, filename)

if __name__ == "__main__":
    main()
