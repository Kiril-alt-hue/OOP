from Figure import Figure
from turtle import *

class Triangle(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def draw(self):
        super().draw()
        up()
        pencolor(self.color)

        v0 = self.position
        v1 = (self.position[0] + self.__side_length, self.position[1])
        v2 = (self.position[0] + self.__side_length / 2, self.position[1] + (self.__side_length * (3 ** 0.5) / 2))

        setpos(self._calc_position(v0))
        down()
        setpos(self._calc_position(v1))
        setpos(self._calc_position(v2))
        setpos(self._calc_position(v0))
        up()