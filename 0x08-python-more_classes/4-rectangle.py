#!/usr/bin/python3
"""This module defines a class `Rectangle`"""


class Rectangle:
    """Rectangle with height and width
    """
    def __init__(self, width, height):
        """Instantiate a Rectangle with width and height

        Args:
            width - Rectangle with
            height = Rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width"""
        return self.__width

    @property
    def height(self):
        """Get height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets values for width
        Args:
            value - width's value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Sets value for height
        Args:
            value - height value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Rectangle Area"""
        return self.height * self.width

    def perimeter(self):
        """Rectangle perimeter"""
        if self.width ==  0 or self.height == 0:
            return 0
        return (2 * (self.height + self.width))
    
    def __str__(self):
        for i in range(self.height):
            if self.height == 0 or self.width == 0:
                return ""
            return "\n".join(["#" * self.width] * self.height)
        
    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)