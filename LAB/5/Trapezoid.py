from turtle import *

from Figure import Figure


class Trapezoid(Figure):
    def __init__(self, x, y, a, b, color):
        super().__init__(x, y, color)  # виклик конструктора базового класу
        self.a = a
        self.b = b

    def _draw(self, color):
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        forward(self.a)
        left(120)
        side_len = ((self.a - self.b) / 2) * (3 ** 0.5)
        forward(side_len)
        left(60)
        forward(self.b)
        left(60)
        forward(side_len)
        left(120)
        up()