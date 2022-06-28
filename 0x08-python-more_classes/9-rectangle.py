#!/usr/bin/python3
"""
Module 1-rectangle.py
defines a class rectangle
"""


class Rectangle:
    """
    class implementation of a Rectangle
    Attributes:
        @number_of_instances: number of Rectangle instances,
        increments with every instantitation,
        decrements with every deletion
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a rectangle instance"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                str_ret += str(self.print_symbol)
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
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Finds the biggest rectangle based on the area
        :param rect_1: first rectangle instance
        :param rect_2: second rectangle instance
        :return: the instance of the biggest area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a new rectangle instance with width == height == size
        :param size: size to set the new rectangle
        :return: the new rectangle instance
        """
        return cls(size, size)