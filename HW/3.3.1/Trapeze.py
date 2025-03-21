from Figure import *
import math

class Trapeze(Figure):
    def __init__(self, bases, sides):
        #перевіряю, чи всі сторони та основи додатні
        if any(side <= 0 for side in bases) or any(side <= 0 for side in sides):
            raise ValueError("Усі сторони та основи трапеції повинні бути додатними числами.")
        self.bases = bases
        self.sides = sides

    def dimention(self):
        return "2D"

    def perimetr(self):
        return sum(self.bases) + sum(self.sides)

    def square(self):
        #перевірка на коректність параметрів трапеції
        a, b = self.bases
        c, d = self.sides
        #умова існування трапеції
        if a <= 0 or b <= 0 or c <= 0 or d <= 0:
            return 0
        #перевірка, чи можна обчислити висоту
        discriminant = c**2 - ((a - b) / 2)**2
        if discriminant < 0:
            return 0  #якщо дискримінант від'ємний, повертаємо 0
        h = math.sqrt(discriminant)
        return (a + b) * h / 2

    def volume(self):
        return self.square()