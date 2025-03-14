import math
from turtle import *

class Figure:
    def __init__(self):
        self.__position = (0, 0)   # абсолютна позиція першої вершини
        self.__rotation = 0        # кут повороту в радіанах
        self.__scale = (1, 1)      # масштаб фігури
        self.__pivot = (0, 0)      # опорна точка
        self.__color = "black"     # колір фігури за промовчанням
        self.__is_drawn = False    # чи зображена фігура на екрані

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation):
        assert isinstance(rotation, (float, int))
        self.__rotation = rotation

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale):
        assert isinstance(scale, (tuple, list)) and len(scale) == 2
        self.__scale = scale

    @property
    def pivot(self):
        return self.__pivot

    @pivot.setter
    def pivot(self, pivot):
        assert isinstance(pivot, (tuple, list)) and len(pivot) == 2
        self.__pivot = pivot

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, pos):
        assert isinstance(pos, (tuple, list)) and len(pos) == 2
        self.__position = pos

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def is_drawn(self):
        return self.__is_drawn

    def _calc_position(self, vertex):
        x, y = vertex[0], vertex[1]

        # Зміщуємо вершини, щоб точка pivot збіглася з початком координат
        x, y = x - self.__pivot[0], y - self.__pivot[1]

        # Масштабуємо
        x, y = self.scale[0] * x, self.scale[1] * y

        # Обертання
        cos_phi = math.cos(self.__rotation)
        sin_phi = math.sin(self.__rotation)
        x, y = cos_phi * x - sin_phi * y, sin_phi * x + cos_phi * y

        # Перенос в позицію self.__position
        x, y = self.__position[0] + x, self.__position[1] + y

        # Повертаємо назад
        x, y = x + self.__pivot[0], y + self.__pivot[1]

        return x, y

    def draw(self):
        if not self.__is_drawn:
            self.__is_drawn = True
        else:
            print("Фігура вже зображена на екрані.")

    def erase(self):
        if self.__is_drawn:
            original_color = self.color
            self.color = "white"  # Стираємо фігуру, малюючи її кольором фону
            self.draw()
            self.color = original_color
            self.__is_drawn = False
        else:
            print("Фігура не зображена на екрані.")

    def move(self, new_position):
        if self.__is_drawn:
            self.erase()
            self.position = new_position
            self.draw()
        else:
            print("Фігура не зображена на екрані.")

    def __str__(self):
        return f"Figure(position={self.position}, rotation={self.rotation}, scale={self.scale}, color={self.color})"