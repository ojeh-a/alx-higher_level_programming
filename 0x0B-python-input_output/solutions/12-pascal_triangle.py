#!/usr/bin/python3
"""Defines a pascal_triangle function."""


def pascal_triangle(n):
    """Returns a list of integers represnting
        Pascal Triangle of size n
    """
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) != n:
        t = triangle[-1]
        temp = [1]
        for i in range(len(t) - 1):
            temp.append(t[i] + t[i + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
