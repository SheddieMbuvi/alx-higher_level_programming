#!/usr/bin/python3
"""
No import module
file reading function
"""
def read_file(filename=""):
    """The function"""
    with open(filename, encoding='utf-8') as a_file:
        for line in a_file:
            print(line, end="")
