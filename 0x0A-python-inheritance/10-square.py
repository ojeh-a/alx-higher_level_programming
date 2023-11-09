#!/usr/bin/python3
"""Defines a a subclass Square."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represents a Square."""

    def __init__(self, size):
        """Initializes a new square.

        Args:
            size: Size of the new sqaure.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
