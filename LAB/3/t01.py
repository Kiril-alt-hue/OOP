from turtle import *
from random import randint, choice
from math import sin, cos, radians


class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self.__position = (0, 0)
        self.__vertex1 = (x1, y1)
        self.__vertex2 = (x2, y2)
        self._color = "lightblue"
        self.rotation = 0  # Обертання у градусах
        self.scale = (1, 1)  # Масштабування (1,1) означає без змін
        self.pivot = (0, 0)  # Опорна точка

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

    def set_pivot(self, pivot_x, pivot_y):
        #Задає точку обертання та масштабування.
        self.pivot = (pivot_x, pivot_y)

    def rotate_point(self, x, y):
        #Обертання точки навколо pivot
        angle = radians(self.rotation)
        px, py = self.pivot


        x -= px
        y -= py


        new_x = x * cos(angle) - y * sin(angle)
        new_y = x * sin(angle) + y * cos(angle)


        return new_x + px, new_y + py

    def scale_point(self, x, y):
        #Масштабування точки відносно pivot
        px, py = self.pivot
        x = px + (x - px) * self.scale[0]
        y = py + (y - py) * self.scale[1]
        return x, y

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


#функція для обчислення точки перетину бісектрис (наближено як центр трикутника)
def bisector_intersection(v1, v2, v3):
    return ((v1[0] + v2[0] + v3[0]) / 3, (v1[1] + v2[1] + v3[1]) / 3)


#функція для обчислення точки перетину медіан (центр мас трикутника)
def median_intersection(v1, v2, v3):
    return ((v1[0] + v2[0] + v3[0]) / 3, (v1[1] + v2[1] + v3[1]) / 3)


if __name__ == '__main__':
    reset()
    speed(0)
    colors = ["red", "orange", "yellow", "green", "blue", "lightblue", "purple"]

    triangles = []
    for _ in range(50):
        x1, y1 = randint(-50, 50), randint(-50, 50)
        x2, y2 = randint(-50, 50), randint(-50, 50)
        x3, y3 = randint(-50, 50), randint(-50, 50)

        t = Triangle(x1, y1, x2, y2)
        t.position = (randint(-200, 200), randint(-200, 200))
        t.color = choice(colors)

        #обчислення точки перетину бісектрис для обертання
        pivot_bisector = bisector_intersection((x1, y1), (x2, y2), (x3, y3))
        t.set_pivot(*pivot_bisector)

        #обчислення точки перетину медіан для масштабування
        pivot_median = median_intersection((x1, y1), (x2, y2), (x3, y3))

        triangles.append((t, pivot_bisector, pivot_median))

    #анімація обертання навколо точки перетину бісектрис
    for angle in range(0, 360, 5):
        clear()
        for t, pivot_bisector, _ in triangles:
            t.set_rotation(angle)
            t.draw()
        update()

    #анімація масштабування відносно точки перетину медіан
    for scale_factor in range(1, 4):
        clear()
        for t, _, pivot_median in triangles:
            t.set_pivot(*pivot_median)
            t.set_scale(scale_factor, scale_factor)
            t.draw()
        update()

    mainloop()
