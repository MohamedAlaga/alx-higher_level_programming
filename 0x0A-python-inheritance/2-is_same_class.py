#!/usr/bin/python3
"""
module to check if objects fro the same class
"""


def is_same_class(obj, a_class):
    """
    if obj and a_class are inctence of the same class return True
    otherwise return False
    """
    return type(obj) is a_class
