#!/usr/bin/python3
"""Define a class"""

class Square:
    """Class representation of a square.
    private instance of attribute size
        - property def size(self)
        - property setter def size(self, value)
    private instance attribute position
        - property def position(self)
        - property setter def position(self, value)
    instantiation with optional size and position
    public instance method: def area(self):
    public instance method: def my_print(self):
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialisation of size
        and checks if size is of type int and is greater than zero"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieves and return the value of size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the of value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position attribute"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the private position attributes"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with character #
        at the position given by position attribute"""
        if self.__size == 0:
            print('')
        for i in range(0, self.__position[1]):
            print('')
        for x in range(0, self.__size):
            for y in range(0, self.__position):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
        print('')
