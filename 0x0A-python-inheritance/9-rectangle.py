#!/usr/bin/python3
"""Defines a class rectangle that inherites from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle"""

    def __int__(self, width, height):
        """
        initialize a new rectangle
        :param width: The width of the new rectangle.
        :param height: Height of the new rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        compute the area of the rectangle instance
        :return: the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        :return: the print() and str() representation of a rectangle.
        """
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

