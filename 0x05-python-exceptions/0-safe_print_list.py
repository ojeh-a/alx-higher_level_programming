#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            elements = my_list[i]
            print(elements, end='')
    except IndexError:
        pass
    print()
    return elements
