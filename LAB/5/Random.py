from random import randint, choice
from turtle import *

from Circle import Circle
from Quadrate import Quadrate
from Rectangle import Rectangle
from Trapezoid import Trapezoid
from Triangle import Triangle


def random_color():
    colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "cyan", "magenta", "brown"]
    return choice(colors)

def create_random_figure():
    x = randint(-300, 300)  # Випадкова координата x
    y = randint(-300, 300)  # Випадкова координата y
    color = random_color()  # Випадковий колір

    # Випадково вибираємо тип фігури
    figure_type = choice([Circle, Rectangle, Quadrate, Triangle, Trapezoid])

    if figure_type == Circle:
        radius = randint(10, 100)  # Випадковий радіус
        return Circle(x, y, radius, color)
    elif figure_type == Rectangle:
        a = randint(50, 150)  # Випадкова довжина першої сторони
        b = randint(20, 100)  # Випадкова довжина другої сторони
        return Rectangle(x, y, a, b, color)
    elif figure_type == Quadrate:
        side = randint(50, 150)  # Випадкова довжина сторони
        return Quadrate(x, y, side, color)
    elif figure_type == Triangle:
        side = randint(50, 150)  # Випадкова довжина сторони
        return Triangle(x, y, side, color)
    elif figure_type == Trapezoid:
        a = randint(50, 150)  # Випадкова довжина більшої основи
        b = randint(20, 100)  # Випадкова довжина меншої основи
        return Trapezoid(x, y, a, b, color)

def main():
    bgcolor("white")  # Колір фону
    tracer(0, 0)  # Вимкнення анімації для швидкого малювання
    figures = []

    for _ in range(100):  # Генеруємо 100 фігур
        figure = create_random_figure()
        figure.show()
        figures.append(figure)

    update()  # Оновлюємо екран
    done()  # Затримуємо вікно на екрані

if __name__ == '__main__':
    main()