from Triangle import *

class TriangularPrism(Triangle):
    def __init__(self, sides, height):
        super().__init__(sides)
        self.h = height

    def dimention(self):
        return "3D"

    def squareSurface(self):
        base_area = 2 * self.squareBase()
        lateral_area = self.perimetr() * self.h
        return base_area + lateral_area

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def volume(self):
        return self.squareBase() * self.h