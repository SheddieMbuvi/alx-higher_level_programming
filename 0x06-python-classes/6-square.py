#!/usr/bin/python3
"""
No import modules allowed for this
"""


class Square:
    """Class that defines the size"""
    def __init__(self, size=0, position=(0, 0)):
        """Method for initialization"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif ((type(position) is not tuple) or (len(position) != 2)
                or (type(position[0]) is not int)
                or (type(position[1]) is not int)
                or ((position[0]) < 0) or (position[1]) < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

    @property
    def size(self):
        """ gets the value of __size """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the value of __size """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """method that returns the current square area"""
        return self.__size * self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if ((type(value) is not tuple) or (len(value) != 2)) \
            or (type(value[0]) is not int) \
            or (type(value[1]) is not int) \
                or ((value[0] < 0) or (value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__position[1]):
                print()
            for n in range(0, self.__size):
                for x in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
