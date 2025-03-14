from Figure import Figure
from turtle import *

class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height

    def draw(self):
        super().draw()
        up()
        pencolor(self.color)

        v0 = self.position
        v1 = (self.position[0] + self.__width, self.position[1])
        v2 = (self.position[0] + self.__width, self.position[1] + self.__height)
        v3 = (self.position[0], self.position[1] + self.__height)

        setpos(self._calc_position(v0))
        down()
        setpos(self._calc_position(v1))
        setpos(self._calc_position(v2))
        setpos(self._calc_position(v3))
        setpos(self._calc_position(v0))
        up()