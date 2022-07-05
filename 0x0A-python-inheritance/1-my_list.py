#!/usr/bin/python3
"""Creates a class that inherits from the list class"""


class MyList(list):
    """A subclass of list"""

    def __init__(self):
        """initializes the obj"""
        super().__init__()

    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))

