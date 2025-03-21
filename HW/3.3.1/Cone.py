from Circle import *

class Cone(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.h = height

    def dimention(self):
        return "3D"

    def squareSurface(self):
        base_area = self.squareBase()
        lateral_area = math.pi * self.radius * math.sqrt(self.radius**2 + self.h**2)
        return base_area + lateral_area

    def squareBase(self):
        return math.pi * self.radius**2

    def height(self):
        return self.h

    def volume(self):
        return (1/3) * math.pi * self.radius**2 * self.h