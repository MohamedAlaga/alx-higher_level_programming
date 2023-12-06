#!/usr/bin/python3
"""
rectangle geometry class
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
        __width = width
        self.integer_validator("height", height)
        __height = height

    def area(self):
        """
        return the area of a rectangle
        """
        return self.__width * self.__height
    
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width,self.__height)