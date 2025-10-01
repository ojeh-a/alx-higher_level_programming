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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
