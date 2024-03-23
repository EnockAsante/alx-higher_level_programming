#!/usr/bin/python3
"""
mod Base
"""
BaseG = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseG):
    """
    Rectangle
    """

    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
