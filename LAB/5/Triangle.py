from turtle import *

from Figure import Figure


class Triangle(Figure):
    def __init__(self, x, y, a, color):
        super().__init__(x, y, color)  # виклик конструктора базового класу
        self.a = a

    def _draw(self, color):
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        for i in range(3):
            forward(self.a)
            left(120)
        up()