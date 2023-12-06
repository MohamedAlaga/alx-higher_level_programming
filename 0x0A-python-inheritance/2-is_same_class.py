#!/usr/bin/python3
"""
module to check if objects fro the same class
"""

def is_same_class(obj, a_class):
    """
    if obj and a_class are inctence of the same class return True
    otherwise return False
    """
    return type(obj) == a_class
    

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))