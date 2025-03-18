from turtle import *
from Figure import Figure


class Rectangle(Figure):
    """ Клас Прямокутник

    Використовується для зображення прямокутника на екрані
    """

    def __init__(self, x, y, a, b, color):
        """ Конструктор
        Ініціалізує положення лівої нижньої вершини,
        довжини його основ і колір.
        :param x: координата x лівої нижньої вершини
        :param y: координата y лівої нижньої вершини
        :param a: перша сторона прямокутника
        :param b: друга сторона прямокутника
        :param color: колір прямокутника
        """
        super().__init__(x, y, color)  # виклик конструктора базового класу
        self.a = a
        self.b = b

    def _draw(self, color):
        """ Віртуальний метод, що зображує прямокутник на екрані заданим кольором
        :param color: колір
        """
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        for i in range(2):
            forward(self.a)
            left(90)
            forward(self.b)
            left(90)
        up()
