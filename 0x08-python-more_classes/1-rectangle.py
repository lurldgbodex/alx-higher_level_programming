#!/usr/bin/python3
"""
Module 1-rectangle.py
defines a class rectangle
"""


class Rectangle:
    """
    class implementation of a Rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the value of the width property
        :param value: parameter that takes the width argument
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        gets the value of height
        :return: the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the value of height
        :param value: the value to set
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
