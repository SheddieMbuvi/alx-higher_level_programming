#!/usr/bin/python3
"""
class to inherit from
"""


class MyList(list):
    """Class inheriting from list"""
    def print_sorted(self):
        """Method to print list sorted ascending"""
        newlist = self.copy()
        newlist.sort()
        print(newlist)
