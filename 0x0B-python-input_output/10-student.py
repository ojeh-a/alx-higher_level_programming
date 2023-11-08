#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name: The student's first name.
            last_name: The student's last name.
            age: The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the student.
        If attrs is a list of strings, represents only
        those attributed included in the list.

        Args:
            attrs (list): The attributes to represent
        """
        if (type(attrs) == list and all(type(element)
            == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs
                    if hasattr(self, k)}
        return self.__dict__
