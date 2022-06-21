#!/usr/bin/python3
class Square:
    """Class representation of a square.
    private instance of attribute size
    instantiation with optional size
    public instance method def area(self)
    public instance method def my_print(self)
    """

    def __init__(self, size=0):
        """Initialisation of size
        and checks if size is of type int and is greater than zero"""
        self.__size = size

    @property
    def size(self):
        """Retrieves and return the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the of value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square are"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with character #"""
        if self.__size > 0:
            print('')
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
            print()
