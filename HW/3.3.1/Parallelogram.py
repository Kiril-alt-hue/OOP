from Figure import *

class Parallelogram(Figure):
    def __init__(self, sides, height):
        self.sides = sides
        self.h = height

    def dimention(self):
        return "2D"

    def perimetr(self):
        return 2 * (self.sides[0] + self.sides[1])

    def square(self):
        return self.sides[0] * self.h

    def volume(self):
        return self.square()