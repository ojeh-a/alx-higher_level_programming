#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """class Square"""
    def __init__(self, size=0):
        """Instantiates a Square with size
        Args: size(int)
        """
        self.size = size

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the square a a square Instant"""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.size == 0:
            print()

        else:
            for i in range(self.size):
                for i in range(self.size):
                    print("#", end='')
                print()
