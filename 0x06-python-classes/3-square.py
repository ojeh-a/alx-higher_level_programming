#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """class Square"""
    def __init__(self, size=0):
        """Instantiates a Square with size
        Args: size(int)
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the square a a square Instant"""
        return self.__size ** 2
