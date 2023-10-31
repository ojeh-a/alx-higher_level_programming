#!/usr/bin/python3
"""Define class Rectangle"""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): The width of the newly created rectangle.
            height (int): The height of the newly created rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """set width for the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
            self.__width = value

    @property
    def height(self):
        """set height for the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """Return area of the rectangle"""

        return (self.__height * self.__width)

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ''
        return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)
