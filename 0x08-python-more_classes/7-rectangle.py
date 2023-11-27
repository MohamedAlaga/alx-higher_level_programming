#!/usr/bin/python3
"""Module that defines a rectangle"""


class Rectangle:
    """defines rectangle class

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    @property
    def width(self):
        """Width retriver.

        Returns:
            int: the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter for width of rectangle.

        Args:
            value (int): width of the rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Height retriver.

        Returns:
            int: the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for height of recyangle.

        Args:
            value (int): height of the rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __init__(self, width=0, height=0):
        """Creates new instances of Rectangle.

        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """Calculates the area of a rectangle.

        Returns:
            int: the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of a rectangle.

        Returns:
            int: the perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        """Returns a string representation of the rectangle with the
        character
        #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            text = [str(self.print_symbol) * self.__width]
            return "\n".join( text * self.__height)

    def __repr__(self):
        """Returns a string representation of the rectangle that can be
        evaluated by the eval() function.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
