from turtle import *

from Figure import Figure


class Triangle(Figure):
    """ Клас Трикутник

    Використовується для зображення правильного трикутника на екрані
    """

    def __init__(self, x, y, a, color):
        """ Конструктор
        Ініціалізує положення лівого нижньої вершини трикутника,
        довжину його сторони і колір.
        :param x: координата x лівої нижньої вершини трикутника
        :param y: координата y лівої нижньої вершини трикутника
        :param a: довжина сторони трикутника
        :param color: колір трикутника
        """

        super().__init__(x, y, color)  # виклик конструктора базового класу
        self.a = a

    def _draw(self, color):
        """ Допоміжний віртуальний метод, що зображує трикутник заданим кольором
        :param color: колір
        """
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        for i in range(3):
            forward(self.a)
            left(120)
        up()