#!/usr/bin/python3
"""
Rect mod
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """
    __height = None
    __width = None
    __x = None
    __y = None
    print_symbol = "#"

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if self.validator("width", width):
            self.__width = width
        if self.validator("height", height):
            self.__height = height
        if self.validator("x", x):
            self.__x = x
        if self.validator("y", y):
            self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if self.validator("width", width):
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if self.validator("height", height):
            self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.validator("x", x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.validator("y", y):
            self.__y = y

    def validator(self, name, var):
        """

        :param name:
        :param var:
        :return:
        """
        msg = "{} must be {}".format(name, ">= 0" if name in "xy" else "> 0")
        if isinstance(var, int):
            if name in "width,height" and var <= 0 or name in "xy" and var < 0:
                raise ValueError(msg)
        else:
            raise TypeError("{} must be an integer".format(name))
        return True

    def area(self):
        """

        :return:
        """
        return self.__height * self.__width

    def display(self):
        """
        :display
        """
        rect = ""
        if self.area == 0:
            return ""
        rect += '\n' * self.__y
        for j in range(self.__height):
            rect += " " * self.__x
            rect += str(self.print_symbol) * self.__width
            if j < self.__height - 1:
                rect += '\n'
        for itm in rect:
            print(itm, end="")
        print()
        return rect

    def __str__(self):
        msg = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                      self.__y, self.__width,
                                                      self.__height)
        return msg

    def update(self, *args, **kwargs):
        """

        :param args:
        :return:
        """
        if args and len(args) > 1:
            for i in range(len(args)):
                if i == 0:
                    super().__init__(args[0])
                if i == 1 and self.validator("width", args[1]):
                    self.__width = args[1]
                if i == 2 and self.validator("height", args[2]):
                    self.__height = args[2]
                if i == 3 and self.validator("x", args[3]):
                    self.__x = args[3]
                if i == 4 and self.validator("y", args[4]):
                    self.__y = args[4]
        for k, v in kwargs.items():
            self.validator(k, v)
            setattr(self, k, v)

    def to_dictionary(self):
        """

        :return:
        """
        return vars(self)
