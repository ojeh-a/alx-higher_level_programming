#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary)
    [print(f"{key}: {a_dictionary[key]}") for key in sorted_keys]
