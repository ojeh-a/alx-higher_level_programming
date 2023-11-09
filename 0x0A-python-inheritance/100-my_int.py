#!/usr/bin/python3
"""Defines int operators == and !="""


class MyInt(int):
    """Invert operators '==' and '!="""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real ==value
