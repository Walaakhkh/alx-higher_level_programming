#!/usr/bin/python3
""" Function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Reads and prints the content of a text file (UTF8)."""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
