import math
from turtle import *
from Figure import Figure
from Rectangle import Rectangle
from Circle import Circle
from Trapezoid import Trapezoid
import time

class Car(Figure):
    def __init__(self, x, y, body_width, body_height, wheel_radius, color):
        super().__init__(x, y, color)


        self.body = Rectangle(x, y, body_width, body_height, color)

        self.wheel1 = Circle(x + body_width * 0.2, y - wheel_radius, wheel_radius, color)
        self.wheel2 = Circle(x + body_width * 0.8, y - wheel_radius, wheel_radius, color)

        roof_base_large = body_width * 0.8
        roof_base_small = body_width * 0.4
        roof_x = x + (body_width - roof_base_large) / 2
        roof_y = y + body_height
        self.roof = Trapezoid(roof_x, roof_y, roof_base_large, roof_base_small, color)

        window_width = body_width * 0.25
        window_height = body_height * 0.4
        window_y = y + body_height * 0.3
        self.window1 = Rectangle(x + body_width * 0.15, window_y, window_width, window_height, "blue")
        self.window2 = Rectangle(x + body_width * 0.6, window_y, window_width, window_height, "blue")

    def _draw(self, color):
        self.body._draw(color)
        self.wheel1._draw(color)
        self.wheel2._draw(color)
        self.roof._draw(color)
        window_color = "blue" if color != bgcolor() else bgcolor()
        self.window1._draw(window_color)
        self.window2._draw(window_color)

    def show(self):
        if not self._visible:
            self._visible = True
            self._draw(self._color)

    def hide(self):
        if self._visible:
            self._visible = False
            self._draw(bgcolor())

    def move(self, dx, dy):
        isVisible = self._visible
        if isVisible:
            self.hide()
        self._x += dx
        self._y += dy
        self.body.move(dx, dy)
        self.wheel1.move(dx, dy)
        self.wheel2.move(dx, dy)
        self.roof.move(dx, dy)
        self.window1.move(dx, dy)
        self.window2.move(dx, dy)
        if isVisible:
            self.show()


# Перевірка для "машини"
if __name__ == "__main__":
    bgcolor("white")
    tracer(0, 0)

    car = Car(-200, 0, 200, 70, 30, "red")
    car.show()

    for i in range(100):
        car.move(1, 0)
        update()
        time.sleep(0.02)
    done()