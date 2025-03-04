from turtle import *
from random import randint, choice
from math import sin, cos, radians


class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self.__position = (0, 0)
        self.__vertex1 = (x1, y1)
        self.__vertex2 = (x2, y2)
        self._color = "lightblue"
        self.rotation = 0  #обертання у градусах
        self.scale = (1, 1)  #масштабування (1,1) означає без змін

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, pos):
        assert isinstance(pos, (tuple, list)) and len(pos) == 2
        self.__position = pos

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def set_rotation(self, rotation):
        self.rotation = rotation

    def set_scale(self, scale_x, scale_y):
        self.scale = (scale_x, scale_y)

    def rotate_point(self, x, y):
        angle = radians(self.rotation)
        new_x = x * cos(angle) - y * sin(angle)
        new_y = x * sin(angle) + y * cos(angle)
        return new_x, new_y

    def scale_point(self, x, y):
        return x * self.scale[0], y * self.scale[1]

    def draw(self):
        up()
        goto(self.__position)
        down()
        fillcolor(self._color)
        begin_fill()

        x1, y1 = self.scale_point(*self.__vertex1)
        x1, y1 = self.rotate_point(x1, y1)
        setpos(self.__position[0] + x1, self.__position[1] + y1)

        x2, y2 = self.scale_point(*self.__vertex2)
        x2, y2 = self.rotate_point(x2, y2)
        setpos(self.__position[0] + x2, self.__position[1] + y2)
        setpos(self.__position)

        end_fill()
        up()


if __name__ == '__main__':
    reset()
    speed(0)
    colors = ["red", "orange", "yellow", "green", "blue", "lightblue", "purple"]

    triangles = []
    for _ in range(100):
        x1, y1 = randint(-50, 50), randint(-50, 50)
        x2, y2 = randint(-50, 50), randint(-50, 50)

        t = Triangle(x1, y1, x2, y2)

        t.position = (randint(-400, 400), randint(-400, 400))

        t.color = choice(colors)

        t.set_rotation(randint(0, 360))
        t.set_scale(randint(1, 3), randint(1, 3))
        triangles.append(t)

        t.draw()

    mainloop()
