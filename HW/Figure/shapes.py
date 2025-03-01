import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        # Периметр завжди можна обчислити
        return self.a + self.b + self.c

    def area(self):
        # Перевіряємо, чи існує трикутник
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            s = self.perimeter() / 2
            return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        else:
            # Якщо трикутник не існує, повертаємо 0
            return 0

    def __str__(self):
        return (f"Трикутник зі сторонами: a = {self.a}, b = {self.b}, c = {self.c}. "
                f"Площа: {self.area():.2f}, Периметр: {self.perimeter():.2f}")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __str__(self):
        return (f"Прямокутник зі сторонами: width = {self.width}, height = {self.height}. "
                f"Площа: {self.area():.2f}, Периметр: {self.perimeter():.2f}")

class Trapeze:
    def __init__(self, base1, base2, side1, side2):
        self.base1 = base1
        self.base2 = base2
        self.side1 = side1
        self.side2 = side2

    def perimeter(self):
        # Периметр завжди можна обчислити
        return self.base1 + self.base2 + self.side1 + self.side2

    def area(self):
        # Перевіряємо, чи існує трапеція
        sides = [self.base1, self.base2, self.side1, self.side2]
        if sum(sides) - max(sides) > max(sides):
            # Якщо трапеція існує, обчислюємо площу
            if self.side1 == self.side2:
                # Для рівнобічної трапеції
                h = math.sqrt(self.side1**2 - ((self.base2 - self.base1) / 2)**2)
                return (self.base1 + self.base2) * h / 2
            else:
                # Для нерівнобічної трапеції повертаємо 0
                return 0
        else:
            # Якщо трапеція не існує, повертаємо 0
            return 0

    def __str__(self):
        return (f"Трапеція з основами: base1 = {self.base1}, base2 = {self.base2}, "
                f"бічними сторонами: side1 = {self.side1}, side2 = {self.side2}. "
                f"Площа: {self.area():.2f}, Периметр: {self.perimeter():.2f}")

class Parallelogram:
    def __init__(self, base, side, height):
        self.base = base
        self.side = side
        self.height = height

    def perimeter(self):
        return 2 * (self.base + self.side)

    def area(self):
        return self.base * self.height

    def __str__(self):
        return (f"Паралелограм зі сторонами: base = {self.base}, side = {self.side}, "
                f"висотою: height = {self.height}. "
                f"Площа: {self.area():.2f}, Периметр: {self.perimeter():.2f}")

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius**2

    def __str__(self):
        return (f"Коло з радіусом: radius = {self.radius}. "
                f"Площа: {self.area():.2f}, Довжина кола: {self.perimeter():.2f}")