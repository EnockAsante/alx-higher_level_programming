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
    num_of_inst = 0

    def __init__(self, width=0, height=0):
        if self.test_passed(width, "width"):
            self.__width = width
        if self.test_passed(height, "height"):
            self.__height = height
        Rectangle.num_of_inst += 1


    def test_passed(self, value, name):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
        else:
            return 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if self.test_passed(value, "width"):
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if self.test_passed(value, "height"):
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height * self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        rec = ""

        if self.__height * self.__width == 0:
            return ""
        for j in range(self.__height):
            rec += '#' * self.__width
            if j < self.__height - 1:
                rec += '\n'
        return rec

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        if Rectangle.num_of_inst > 0:
            Rectangle.num_of_inst -= 1
        print("Bye rectangle...")

