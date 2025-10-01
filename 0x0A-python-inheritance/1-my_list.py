#!/usr/bin/python3
"""Module defines a class MyList"""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
