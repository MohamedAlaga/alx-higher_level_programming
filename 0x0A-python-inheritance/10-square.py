#!/usr/bin/python3
"""
square geometry class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    square gemetry class
    """

    def __init__(self, size):
        """
        set square size
        """

        self.integer_validator("size",size)
        self.__size = size
    
    def area(self):
        """
        return square area
        """

        return self.__size*self.__size
