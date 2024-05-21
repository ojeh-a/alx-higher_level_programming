#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """class Rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantiation of Rectangle"""

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets width with a value
        args:
            value: value of width
        Raises:
            TypeError if width is not an integer
            ValueError if width is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for hieght"""

        return self.__height

    @height.setter
    def height(self, value):
        """"Setter for height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the Rectangle"""

        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the Rectangle instance"""

        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width * self.height)

    def __str__(self):
        """Reutrns string representation of symblo"""
        if self.width == 0 or self.height == 0:
            return ""
        if hasattr(self, 'print_symbol'):
            symbol = self.print_symbol
        else:
            symbol = Rectangle.print_symbol
        return "\n".join([str(symbol) * self.width] * self.height)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare Rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
