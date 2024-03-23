#!/usr/bin/python3
"""
mod Base
"""


class BaseGeometry:
    """
    BaseGeometry
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is int:
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
        else:
            raise TypeError("{} must be an integer".format(name))
        return True


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().__init__()
        if (self.integer_validator("width", width) and
                self.integer_validator("height", height)):
            self.__width = width
            self.__height = height
