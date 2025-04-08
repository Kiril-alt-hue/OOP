import math


class Rational:
    def __init__(self, numerator=0, denominator=1):

        if isinstance(numerator, str):

            parts = numerator.split('/')
            if len(parts) == 1:
                self.n = int(parts[0])
                self.d = 1  #знаменник = 1, якщо передано лише число
            elif len(parts) == 2:
                self.n = int(parts[0])
                self.d = int(parts[1])
            else:
                raise ValueError("Невірний формат раціонального числа")
        else:
            #якщо передано два числа
            self.n = numerator
            self.d = denominator


        if self.d == 0:
            raise ZeroDivisionError("Знаменник не може бути нулем")

        #скорочення дробу
        self._simplify()

    def _simplify(self):

        gcd_value = math.gcd(abs(self.n), abs(self.d))

        self.n = self.n // gcd_value
        self.d = self.d // gcd_value

        #якщо знаменник від'ємний, переносимо мінус до чисельника
        if self.d < 0:
            self.n *= -1
            self.d *= -1

    # ===============================Арифметичні операції ==============================================

    def __add__(self, other):

        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            raise TypeError("Непідтримуваний тип операнда для +")


        new_n = self.n * other.d + other.n * self.d
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __sub__(self, other):

        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            raise TypeError("Непідтримуваний тип операнда для -")


        new_n = self.n * other.d - other.n * self.d
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __mul__(self, other):

        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            raise TypeError("Непідтримуваний тип операнда для *")


        new_n = self.n * other.n
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __truediv__(self, other):

        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            raise TypeError("Непідтримуваний тип операнда для /")
        if other.n == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе")


        new_n = self.n * other.d
        new_d = self.d * other.n
        return Rational(new_n, new_d)

    # ====================реверсні оператори (для випадків, коли ціле число зліва) ==========

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return Rational(other) - self

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rtruediv__(self, other):
        return Rational(other) / self

    #================================Спеціальні оператори ===============================================

    def __call__(self):
        return self.n / self.d

    def __getitem__(self, key):
        if key == "n":
            return self.n
        elif key == "d":
            return self.d
        else:
            raise KeyError("Невірний ключ. Використовуйте 'n' або 'd'")

    def __setitem__(self, key, value):
        if key == "n":
            self.n = value
        elif key == "d":
            if value == 0:
                raise ZeroDivisionError("Знаменник не може бути нулем")
            self.d = value
        else:
            raise KeyError("Невірний ключ. Використовуйте 'n' або 'd'")
        self._simplify()

    # =================================Представлення об'єкта ==============================================

    def __str__(self):
        if self.d == 1:
            return str(self.n)  #виводимо лише чисельник для цілих чисел
        return f"{self.n}/{self.d}"

    def __repr__(self):
        return f"Rational({self.n}, {self.d})"