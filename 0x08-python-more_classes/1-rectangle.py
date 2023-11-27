#!/usr/bin/python3
"""Module that defines a rectangle"""


class Rectangle:
    """defines rectangle class"""

    __width = None
    __height = None

    def width(self):
        """getter for width attribute"""
        return self.__width

    def width(self, value):
        """setter for width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def height(self):
        """getter for height attribute"""
        return self.__height

    def height(self, value):
        """setter for height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __init__(self, width=0, height=0):
        """initializes the instance"""
        self.__width = width
        self.__height = height
