from turtle import *
import time

class Figure:

    def __init__(self, x, y, color):
        self._x = x  # _x - координата x
        self._y = y  # _y - координата y
        self._visible = False  # _visible - чи є фіруга видимою на екрані
        self._color = color    # _color - колір фігури

    def _draw(self, color):
        pass

    def show(self):
        if not self._visible:
            self._visible = True
            self._draw(self._color)

    def hide(self):
        if self._visible:
            self._visible = False
            # щоб сховати фігуру, потрібно
            # зобразити її кольором фону.
            self._draw(bgcolor())

    def move(self, dx, dy):
        isVisible = self._visible
        if isVisible:
            self.hide()
        self._x += dx
        self._y += dy
        if isVisible:
            self.show()