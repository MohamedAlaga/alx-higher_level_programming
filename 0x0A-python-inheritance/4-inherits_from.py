#!/usr/bin/python3
"""
module to check if object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    return
    True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class ;
    otherwise False
    """

    return isinstance(obj, a_class)
