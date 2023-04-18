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
