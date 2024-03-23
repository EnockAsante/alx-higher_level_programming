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
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
