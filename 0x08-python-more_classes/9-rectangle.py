#!/usr/bin/python3
"""This module defines a class `Rectangle`"""


class Rectangle:
    """Rectangle with height and width
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width, height):
        """Instantiate a Rectangle with width and height

        Args:
            width - Rectangle with
            height = Rectangle height
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.height + self.width))

    def __str__(self):
        """String representation of Rectangle"""

        if self.height == 0 or self.width == 0:
            return ""
        if hasattr(self, "print_symbol"):
            symbol = self.print_symbol
        else:
            symbol = Rectangle.print_symbol
        return "\n".join([str(symbol) * self.width] * self.height)

    def __repr__(self):
        """compatible with eval() representation of Rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Delete rectangle instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on area
        Args:
            rect_1 - First Rectangle
            rect_2 - Second Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new square instance"""
        return cls(size, size)
