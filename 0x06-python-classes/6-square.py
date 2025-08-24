#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Instantiates a Square with size
        Args: size(int)
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) == 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Returns the square a a square Instant"""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.size == 0:
            print()

        else:
            [print("") for i in range(self.position[1])]
            for i in range(self.size):
                [print(" ", end="") for space in range(self.position[0])]
                [print("#", end='') for unit in range(self.size)]
                print()
