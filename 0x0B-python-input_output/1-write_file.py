#!/usr/bin/python3
"""
No module imported
should append text to a file
"""


def write_file(filename="", text=""):
    """Function to append the text"""
    with open(filename, 'w') as a_file:
        new_file = a_file.write(text)
    return new_file
