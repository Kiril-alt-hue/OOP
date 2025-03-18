from Figure import Figure
import time
from Circle import Circle
from Quadrate import Quadrate
from Triangle import Triangle
from Trapezoid import Trapezoid
from Rectangle import Rectangle
from turtle import *



if __name__ == '__main__':
    # Ініціалізація turtle
    home()
    delay(30)

    ###### Перевірка кола ############
    c = Circle(120, 120, 50, "blue")
    c.show()
    c.move(-30, -140)
    c.hide()

    ###### Перевірка квадрата ############
    q = Quadrate(0, 0, 150, "red")
    q.show()
    q.move(0, 140)
    q.hide()

    ###### Перевірка трикутника ############
    t = Triangle(120, 120, 50, "blue")
    t.show()
    t.move(-30, -140)
    t.hide()

    ###### Перевірка трапеції ############
    t = Trapezoid(120, 120, 50, 30, "red")
    t.show()
    t.move(-30, -140)
    t.hide()

    ###### Перевірка прямокутника ############
    t = Rectangle(120, 120, 50, 30, "red")
    t.show()
    t.move(-30, -140)
    t.hide()

    mainloop()