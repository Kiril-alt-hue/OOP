from Rectangle import *
import math

class QuadrangularPyramid(Rectangle):
    def __init__(self, base_sides, height):
        super().__init__(base_sides)
        self.h = height

    def dimention(self):
        return "3D"

    def squareSurface(self):
        base_area = self.squareBase()
        lateral_area = 2 * (self.sides[0] * math.sqrt(self.h**2 + (self.sides[1]/2)**2)) / 2 + \
                       2 * (self.sides[1] * math.sqrt(self.h**2 + (self.sides[0]/2)**2)) / 2
        return base_area + lateral_area

    def squareBase(self):
        return self.sides[0] * self.sides[1]

    def height(self):
        return self.h

    def volume(self):
        return (1/3) * self.squareBase() * self.h