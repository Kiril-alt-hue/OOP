from Rectangle import *

class RectangularParallelepiped(Rectangle):
    def __init__(self, sides):
        super().__init__(sides[:2])
        self.h = sides[2]

    def dimention(self):
        return "3D"

    def squareSurface(self):
        return 2 * (self.sides[0] * self.sides[1] + self.sides[0] * self.h + self.sides[1] * self.h)

    def squareBase(self):
        return self.sides[0] * self.sides[1]

    def height(self):
        return self.h

    def volume(self):
        return self.sides[0] * self.sides[1] * self.h