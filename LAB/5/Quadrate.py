from turtle import *

from Figure import Figure


class Quadrate(Figure):


    def __init__(self, x, y, a, color):
        super().__init__(x, y, color)
        self.a = a #сторона квадрату

    def _draw(self, color):
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        for i in range(4):
            forward(self.a)
            left(90)
        up()