#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """
    class of Square
    """

    def __init__(self, size = 0):
        """constructor for initialising the instance variable
        :@size = size(private) to use"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        area of a square
        :returns square
        """
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        i = 0
        if self.__size == 0:
            print()
        else:
            str = "#" * self.area()
            for j in (str):
                if i == self.__size:
                    print()
                    i = 0
                print("{}".format(j), end="")
                i += 1
            print()
