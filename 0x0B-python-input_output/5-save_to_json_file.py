#!/usr/bin/python3
"""Defines save_to_JSON_file function."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation."""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
