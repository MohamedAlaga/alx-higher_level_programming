#!/usr/bin/python3
"""
class that inherts from base geometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class to calc the geomtry of rectangle
    """

    def __init__(self, width, height):
        """
        set the values of width and heigth
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
