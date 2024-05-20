#!/usr/bin/python3
""" a class Rectangle that defines a rectangle """


class Rectangle:
    """ Represents a rectangle """

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Return the value of width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set value for width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the value of height of rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """setting value for height of the rectangle"""

        if not isinstance(value, int):
            raise ValueError("height must be an integer")
        if value < 0:
            raise isinstance("height must >= 0")
        self.__height = value
