from turtle import *
from Figure import Figure


class Rectangle(Figure):
    def __init__(self, x, y, a, b, color):
        super().__init__(x, y, color)
        self.a = a
        self.b = b

    def _draw(self, color):
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        for i in range(2):
            forward(self.a)
            left(90)
            forward(self.b)
            left(90)
        up()