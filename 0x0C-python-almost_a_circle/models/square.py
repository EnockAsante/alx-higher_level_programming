#!/usr/bin/python3
"""
Square mod
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    square
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        msg = "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                self.y, self.height)
        return msg

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, width):
        if self.validator("width", width):
            self.width(width)

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, height):
        if self.validator("height", height):
            self.height(height)
