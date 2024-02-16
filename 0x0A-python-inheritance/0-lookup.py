#!/usr/bin/python3
'''Defines a function to lookupattributes and methods of an object
'''


def lookup(obj):
    '''Return: The list of available attributes and methods of an obj.
    '''

    return (dir(obj))
