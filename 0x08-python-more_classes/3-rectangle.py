#!/usr/bin/python3
class Rectangle:
    """
    class Rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialization of rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting the wwidth"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """The area calculator"""
        return self.__width * self.__height

    def perimeter(self):
        """find the perimeter"""
        if self.__width == 0:
            perimeter = 0
            return perimeter
        elif self.__height == 0:
            perimeter = 0
            return perimeter
        perimeter = (2 * self.__width) + (2 * self.__height)
        return perimeter

    def __str__(self):
        """prints a character"""
        c = ""
        if self.__width == 0 or self.__height == 0:
            return c
        for i in range(self.__height):
            for j in range(self.__width):
                c += "#"
            c += '\n'
        return c[:-1]
