import json


class Figure:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


class rectangle(Figure):

    def __init__(self, width, height, color):
        super().__init__(color)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError

    @height.setter
    def height(self, h):
        if h > 0:
            self.__height = h
        else:
            raise ValueError

    def area(self):
        return self.__width * self.__height

class TestClass:
    def __init__(self, line):
        self.line = line

    @property
    def line_to_reverse(self):
        return self.line

    @line_to_reverse.setter
    def line_to_reverse(self, l):
        self.line = l

    def rev_line(self):
        return ''.join([i for i in reversed(self.line)])

class MyCls:

    def __init__(self, num: int):
        self.num = num

    def my_method(self, num1: int) -> int:
        return self.num * num1

x = MyCls(27)

print(x.my_method(3))