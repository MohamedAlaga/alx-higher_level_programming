#!/usr/bin/python3
"""
module for BaseGeometry class
"""


class BaseGeometry ():
    """
    class to calc aria
    """

    def area(self):
        """
        raise exeption only
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Raise
        value is not an integer: raise a TypeError exception,
        with the message <name> must be an integer
        value is less or equal to 0: raise a ValueError exception
        with the message <name> must be greater than 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
