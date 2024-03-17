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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if self.test_passed(width, "width"):
            self.__width = width
        if self.test_passed(height, "height"):
            self.__height = height
        Rectangle.number_of_instances += 1

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
            rec += str(self.print_symbol) * self.__width
            if j < self.__height - 1:
                rec += '\n'
        return rec

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        return rect_1 if rect_1.area() > rect_2.area() else rect_2

    @classmethod
    def test_passed_cls(cls, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            return 1

    @classmethod
    def square(cls, size=0):
        if Rectangle.test_passed_cls(size):
            return Rectangle(size, size)
