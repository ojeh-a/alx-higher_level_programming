#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        return int(sorted(my_list)[-1])
