#!/usr/bin/python3
"""Defines a class Square that inherites from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """
        Initialize a new square
        :param size: the size of the new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """computes the area of square instance."""
        return self.__size ** 2

    def __str__(self):
        """
        :return: The square description
        """
        return str("[square] {}/{]".format(self.__size, self.__size))
