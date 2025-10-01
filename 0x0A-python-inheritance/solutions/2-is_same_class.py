#!/usr/bin/python3
'''Defines a function that checks class instance.'''


def is_same_class(obj, a_class):
    '''Checks if an object is an exact instance of a given class.

    Args:
        obj: The object to check.
        a_class: The class to check.
    Return:
        True or False
    '''
    if type(obj) is a_class:
        return True
    return False
