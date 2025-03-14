from Figure import Figure
from turtle import *

class Trapezoid(Figure):
    def __init__(self, base1, base2, height):
        super().__init__()
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def draw(self):
        super().draw()
        up()
        pencolor(self.color)

        x0, y0 = self.position
        x1, y1 = x0 + self.base1, y0
        x2, y2 = x0 + (self.base1 - self.base2) / 2, y0 + self.height
        x3, y3 = x2 + self.base2, y2

        setpos(self._calc_position((x0, y0)))
        down()
        setpos(self._calc_position((x1, y1)))
        setpos(self._calc_position((x3, y3)))
        setpos(self._calc_position((x2, y2)))
        setpos(self._calc_position((x0, y0)))
        up()