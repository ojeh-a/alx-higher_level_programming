#!/usr/bin/python3
"""Defines an empty class BaseGeometry"""


class BaseGeometry:
    """Represent Base Geometry."""

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This function validates value.

        Args:
            name: Always a string.
            value: Value to be validated.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Represents a rectangle that inherits BaseGeometry property"""

    def __init__(self, width, height):
        """
        Initializes a new Rectangle.

        Args:
            width(int): Width of the Rectangle.
            height(int): Height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
