#!/usr/bin/python3
""" A class that defines a square """


class Square:
    """ Class square """

    def __init__(self, size=0):
        """
        Init a new square

        Args:
            size of the square(int)
        """

        self.size = size

    @property
    def size(self):
        """ Setter and Getter for size of square """

        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Return area of the square """

        return (self.__size ** 2)
