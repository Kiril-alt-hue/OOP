from turtle import *
from Circle import Circle
from Square import Square
from Rectangle import Rectangle
from Triangle import Triangle
from Trapezoid import Trapezoid

if __name__ == '__main__':
    reset()
    speed(1)

    c = Circle(50)
    c.color = "blue"
    c.draw()

    r = Rectangle(120, 80)
    r.color = "purple"
    r.draw()

    s = Square(100)
    s.color = "green"
    s.draw()

    t = Triangle(100)
    t.color = "orange"
    t.draw()

    trap = Trapezoid(150, 100, 80)
    trap.color = "red"
    trap.draw()

    # Переміщення фігури
    t.move((100, 100))

    # Стирання фігури
    trap.erase()

    mainloop()