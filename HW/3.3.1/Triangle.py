from Figure import *
import math

class Triangle(Figure):
    def __init__(self, sides):
        #перевіряю, чи всі сторони додатні
        if any(side <= 0 for side in sides):
            raise ValueError("Усі сторони трикутника повинні бути додатними числами.")
        self.sides = sides

    def dimention(self):
        return "2D"

    def perimetr(self):
        return sum(self.sides)

    def square(self):
        #перевірка на коректність сторін трикутника
        a, b, c = self.sides
        if a + b <= c or a + c <= b or b + c <= a:
            return 0  #якщо сторони не задовольняють умову трикутника, повертаємо 0
        s = self.perimetr() / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def volume(self):
        return self.square()