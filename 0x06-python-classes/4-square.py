#!/usr/bin/python3
"""Define a class"""


class Square:
    """Class representation of a square."""

    def __init__(self, size=0):
        """Initialisation of size
        Args:
            size (int): The size of the square
        """
        self.size = size
        
    @property
    def size(self):
        """Retrieves and return the value of size"""
        return self.__size
        
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square are"""
        return self.__size ** 2
