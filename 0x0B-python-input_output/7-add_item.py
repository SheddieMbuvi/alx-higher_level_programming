#!/usr/bin/python3
"""
writes an Object to a text file, using a JSON representation
"""
import json
import sys


def save_to_json_file(my_obj, filename):
    """The function"""
    with open(filename, 'w') as a_file:
        new = json.dumps(my_obj)
        a_file.write(new)

def load_from_json_file(filename):
    """The function to create"""
    with open(filename, 'r') as a_file:
        data = a_file.read()
        newdata = json.loads(data)
        return newdata

try:
    obj = load_from_json_file("add_item.json")
except:
    save_to_json_file([], "add_item.json")
obj = load_from_json_file("add_item.json")
l = []
for i in range(1, len(sys.argv)):
    l.append(sys.argv[i])
obj = obj + l
save_to_json_file(obj, "add_item.json")
