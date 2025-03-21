from Figure import *
import math

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def dimention(self):
        return "2D"

    def perimetr(self):
        return 2 * math.pi * self.radius

    def square(self):
        return math.pi * self.radius**2

    def volume(self):
        return self.square()