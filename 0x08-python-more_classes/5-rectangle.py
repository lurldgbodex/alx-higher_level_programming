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

    def __str__(self):
        """
        returns an informal and nicely printable string representation
        filled with the '#' character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        str_ret = ''
        for i in range(self.__height):
            for j in range(self.__width):
                str_ret += '#'
            str_ret += '\n'
        return str_ret[:-1]

    def __repr__(self):
        """
        :returns a string representation of a rectangle instance
        that is able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Deletes a rectangle instance.
        """
        print("Bye rectangle...")

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

    def area(self):
        """
        calculates area of rectangle
        :return: The area of the rectangle calculate
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        calculates the perimeter of a rectangle
        :return: the calculated perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
