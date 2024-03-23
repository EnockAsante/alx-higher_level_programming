#!/usr/bin/python3
"""
mod Base
"""
Rect = __import__('8-base_geometry').Rectangle


class Square(Rect):
    """
    Square
    """

    def __init__(self, size):
        super().__init__()
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

