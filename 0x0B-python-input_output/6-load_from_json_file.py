#!/usr/bin/python3
"""
Creates object from a JSON file
"""
import json


def load_from_json_file(filename):
    """The function to create"""
    with open(filename, 'r') as a_file:
        data = a_file.read()
        newdata = json.loads(data)
        return newdata
