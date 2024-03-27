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
    def size(self):
        return self.width

    @size.setter
    def size(self, width):
        if self.validator("width", width):
            self.width = width
            self.height = width

    def update(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        if args and len(args) > 1:
            for i in range(len(args)):
                if i == 0:
                    Rectangle.id = args[0]
                if i == 1 and self.validator("width", args[1]):
                    self.__width = args[1]
                if i == 3 and self.validator("x", args[3]):
                    self.__x = args[3]
                if i == 4 and self.validator("y", args[4]):
                    self.__y = args[4]
        for k, v in kwargs.items():
            self.validator(k, v)
            setattr(self, k, v)
