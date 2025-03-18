from turtle import *

from Figure import Figure


class Trapezoid(Figure):
    """ Клас Трапеція

    Використовується для зображення рівнобічної трапеції на екрані
    """

    def __init__(self, x, y, a, b, color):
        """ Конструктор
        Ініціалізує положення лівої нижньої вершини,
        довжини його основ і колір.
        :param x: координата x лівої нижньої вершини
        :param y: координата y лівої нижньої вершини
        :param a: довжина більшох основий трапеції
        :param b: довжина меншої основий трапеції
        :param color: колір трапеції
        """

        super().__init__(x, y, color)  # виклик конструктора базового класу
        self.a = a
        self.b = b

    def _draw(self, color):
        """ Віртуальний метод, що зображує трапецію на екрані заданим кольором
        :param color: колір
        """
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        forward(self.a)
        left(120)
        side_len = ((self.a - self.b) / 2) * (3 ** 0.5)
        forward(side_len)
        left(60)
        forward(self.b)
        left(60)
        forward(side_len)
        left(120)
        up()