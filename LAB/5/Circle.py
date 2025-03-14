import math
from Figure import Figure
from turtle import *

class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, r):
        assert r > 0
        self.__radius = r

    def draw(self):
        super().draw()
        up()
        pencolor(self.color)
        x, y = self._calc_position((self.position[0], self.position[1] - self.__radius))
        goto(x, y)
        down()
        circle(self.__radius * self.scale[0])
        up()