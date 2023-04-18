#!/usr/bin/python3
"""
And now, the Square!
inheriting from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square to inherit rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Str representation"""
        return f"[Square] {self.id} {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size of the sqr"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes of Square"""
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return dictionary representation of Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
