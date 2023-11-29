#!/usr/bin/python3
"""module with a function that add two numbers"""


def add_integer(a, b=98):
    """
    function to return sum of two integers
    a and b must be first casted to integers if they are float

    Raise :
    TypeError : a must be an integer
    TypeError : b must be an integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
