#!/usr/bin/python3
"""
Rectangle module
"""


class Rectangle:
    """
    class Rectangle
    """
    __width = 0
    __height = 0

    def __init__(self, width = 0, height = 0):
        if self.test_passed(width, "width"):
            self.__width = width
        if self.test_passed(height, "height"):
            self.__height = height

    def width(self, value):
        if self.test_passed(value, "width"):
            self.__width = value

    def height(self, value):
        if self.test_passed(value, "height"):
            self.__width = value

    def test_passed(self, value, name):
        if type(value) is not int:
            raise (TypeError, "{} must be an integer".format(name))
        elif value < 0:
            raise (ValueError, "{} must be >= 0".format(name))
        else:
            return 1

    def width(self):
        return self.__width

    def height(self):
        return self.__height


