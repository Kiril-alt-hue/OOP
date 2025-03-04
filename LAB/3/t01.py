from turtle import * # Підключаємо модуль turtle
from random import randint, choice


class Triangle:

    def __init__(self, x1, y1, x2, y2):
        self.__position = (0, 0)   # абсолютна позиція першої вершини
        self.__vertex1 = (x1, y1)  # позиція другої відносно першої вершини
        self.__vertex2 = (x2, y2)  # позиція третьої відносно першої вершини

        self._color = "lightblue"     # колір трикутника за промовчанням




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


    def __str__(self):
        return f"Triangle: {self.__position, self.__vertex1, self.__vertex2}"

    def draw(self):
        up() # перестраховка, якщо пензлик був опущений

        goto(self.__position)

        down()

        fillcolor(self._color)
        begin_fill()

        # зміщені координати для vertex1
        x, y = self.__position[0] + self.__vertex1[0], self.__position[1] + self.__vertex1[1]
        setpos(x, y)

        # зміщені координати для vertex1
        x, y = self.__position[0] + self.__vertex2[0], self.__position[1] + self.__vertex2[1]
        setpos(x, y)
        setpos(self.__position)

        end_fill()
        up()


if __name__ == '__main__':
    reset()
    speed(5)
    colors = ["red", "orange", "yellow", "green", "blue", "lightblue", "purple"]

    t = Triangle(100, 0, 100, 100)
    print(t)

    for i in range(100):
        x1 = randint(-400, 400)
        y1 = randint(-400, 400)



        t.position = (x1, y1)
        t.color = choice(colors)
        t.draw()

    mainloop()       # Затримуємо вікно на екрані