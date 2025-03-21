from Figure import *

class Rectangle(Figure):
    def __init__(self, sides):
        self.sides = sides

    def dimention(self):
        return "2D"

    def perimetr(self):
        return 2 * (self.sides[0] + self.sides[1])

    def square(self):
        return self.sides[0] * self.sides[1]

    def volume(self):
        return self.square()