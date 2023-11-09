#!/usr/bin/python3
"""Defines an empty class BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle that inherits BaseGeometry property"""

    def __init__(self, width, height):
        """
        Initializes a new Rectangle.

        Args:
            width(int): Width of the Rectangle.
            height(int): Height of the rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the Rectangle area."""
        return self.__width * self.__height

    def __str__(self):
        """Return print() and str() representation of a rectangle."""
        string = '[' + str(self.__class__.__name__) + '] '
        string += str(self.__width) + '/' + str(self.__height)
        return string
