from Triangle import *
import math

class TriangularPyramid(Triangle):
    def __init__(self, base_side, height):
        super().__init__([base_side, base_side, base_side])
        self.h = height

    def dimention(self):
        return "3D"

    def squareSurface(self):
        base_area = self.squareBase()
        lateral_area = 3 * (self.sides[0] * math.sqrt(self.h**2 + (self.sides[0] / (2 * math.sqrt(3)))**2)) / 2
        return base_area + lateral_area

    def squareBase(self):
        return (math.sqrt(3) / 4) * self.sides[0]**2

    def height(self):
        return self.h

    def volume(self):
        return (1/3) * self.squareBase() * self.h