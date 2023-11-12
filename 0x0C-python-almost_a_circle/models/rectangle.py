#!/usr/bin/python3
"""Defines a class Rectangle."""
from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new rectangle

        Args:
            width: Width of the new Rectangle.
            height: Height of the new Rectangle.
            x: The x coordinate of the new Rectangle.
            y: The y coordinate of the new Rectangle.
            id: The identity of the new Rectangle.
        Raises:
            TypeError: If width or height is not an int
            ValueError: If width or height <= 0
            TypeError: If x or y is not an int
            ValueError: If x or y <= 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set/get the width of the Rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set/get the height of the Rectangle."""
        return self.__height
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set/get the x coordinate of the Rectangle."""
        return self.__x
    
    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must > 0")
        self.__x = value

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height
