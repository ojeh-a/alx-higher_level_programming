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
        self.height = height
        self.width = width

    @property
    def width(self):
        """Return the value of width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set value for width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the value of height of rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Set value for height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
