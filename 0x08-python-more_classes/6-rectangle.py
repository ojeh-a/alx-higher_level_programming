#!/usr/bin/python3
"""This module defines a class Rectangle"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0     # Number of instances

    def __init__(self, width=0, height=0):
        """Instantiating a new Rectangle instance"""

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width
        args:
            value: value of the width
        Raises:
            TypeError if value is not int
            ValueError if value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height
        args:
            value: value of the height
        Raises:
            TypeError if value is not int
            ValuError if value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the Recangle"""

        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the Rectangle"""

        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        '''Returns string representation for Rectangle'''

        if self.width == 0 or self.height == 0:
            return ''
        return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        """Returns repr representation of Rectangle"""

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Notification for delete"""

        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1
