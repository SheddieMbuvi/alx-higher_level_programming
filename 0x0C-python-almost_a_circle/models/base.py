#!/usr/bin/python3
"""
First class base
"""
import json


class Base:
    """The class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that return Json string"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method"""
        fname = cls.__name__ + ".json"
        new_list = []
        if list_objs is not None:
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))
        with open(fname, 'w') as a_file:
            a_file.write(cls.to_json_string(new_list))

    def from_json_string(json_string):
        """method"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes"""
        if cls.__name__ == "Square":
            m = cls(5)
        elif cls.__name__ == "Rectangle":
            m = cls(5, 5)
        m.update(**dictionary)
        return m

    @classmethod
    def load_from_file(cls):
        """Reads a file and returns the list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                ls = cls.from_json_string(f.read())
                li = []
                for i in ls:
                    li.append(cls.create(**i))
                return li
        except (FileNotFoundError, PermissionError, IOError):
            return []
