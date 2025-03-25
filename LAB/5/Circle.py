from turtle import *
from Figure import Figure


class Circle(Figure):
    def __init__(self, x, y, r, color):
        super().__init__(x, y, color)
        self._r = r  # _r - радіус кола

    def _draw(self, color):
        pencolor(color)
        up()
        # малює починаючи знизу кола
        setpos(self._x, self._y - self._r)
        down()
        circle(self._r)
        up()