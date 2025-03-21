from Figure import *
import math

class Ball(Figure):
    def __init__(self, radius):
        self.radius = radius

    def dimention(self):
        return "3D"

    def squareSurface(self):
        return 4 * math.pi * self.radius**2

    def volume(self):
        return (4/3) * math.pi * self.radius**3