#!/usr/bin/python3
"""
module to add attributes
"""


def add_attribute(obj, attr, value):
    """
    check if there is slot for more
    attribute then add if possible
    """
    x = "__dict__"
    y = "__slots__"
    if hasattr(obj, x) or (hasattr(obj, y) and attr in obj.__slots__):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
