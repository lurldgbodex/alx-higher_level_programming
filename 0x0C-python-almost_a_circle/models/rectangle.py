#!/usr/bin/python3
"""Defines a class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """A rectangle class that inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """returns the width attributes"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrieves the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of a rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the rectangle instance with the character #"""
        for y in range(0, self.__y):
            print()
        for h in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for w in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns a string rep. of a rectangle instance"""
        str_rep = "[Rectangle] () {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
        return str_rep

    def update(self, *args, **kwargs):
        """
        updates the Rectangle.
        :param args: contains new attributes values to represent
        -id attribute
        -width attribute
        -height attribute
        -x attribute
        -y attribute
        :param kwargs: new key/value pairs of attribute
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height == value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a rectangle"""
        dict_rep = {'id': self.id, 'width': self.__width, 'height': self.__height,'x': self.__x, 'y': self.__y}
        return dict_rep
