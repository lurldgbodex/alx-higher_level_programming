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
