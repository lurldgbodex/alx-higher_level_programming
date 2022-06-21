#!/usr/bin/python3
"""Define a class"""

class Square:
    """Class representation of a square.
    private instance of attribute size
    instantiation with optional size
    """

    def __init__(self, size=0):
        """Initialisation of size
        and checks if size is of type int and is greater than zero"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
