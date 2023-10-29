#!/usr/bin/python3
""" A square that defines a square """

class Square:
    """ Defining the square. """

    def __init__(self, size=0):
        """ Initializing a square.
        Args:
            size: Size of the square(int).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
