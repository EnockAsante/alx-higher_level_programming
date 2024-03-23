#!/usr/bin/python3
"""
mod Base
"""
Rect = __import__('9-rectangle').Rectangle


class Square(Rect):
    """
    Square
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2
