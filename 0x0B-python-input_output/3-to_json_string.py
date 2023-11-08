#!/usr/bin/python3
"""Defines to_json_string function."""
import json


def to_json_string(my_obj):
    """
    Returns JSON representation of ann object
    """
    return json.dumps(my_obj)
