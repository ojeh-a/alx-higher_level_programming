#!/usr/bin/python3
'''
    element_at: retrievs an element from a list
    Return: the element at the index given.
'''


def element_at(my_list, idx):
    element = my_list[idx]

    if idx < 0:
        return (None)

    elif idx > (len(my_list) - 1):
        return (None)

    else:
        return (my_list[idx])
