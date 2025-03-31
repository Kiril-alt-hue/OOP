import math


class Rational:
    def __init__(self, numerator=0, denominator=1):
        """
        Конструктор класу Rational.

        Параметри:
            numerator - чисельник (ціле число або рядок у форматі 'n/d')
            denominator - знаменник (ціле число, за замовчуванням 1)

        Якщо передано рядок, він має бути у форматі 'n/d' або просто 'n' (знаменник = 1)
        """
        if isinstance(numerator, str):
            # Обробка рядкового вводу у форматі 'n/d'
            parts = numerator.split('/')
            if len(parts) == 1:
                self.n = int(parts[0])  # Чисельник
                self.d = 1  # Знаменник = 1, якщо передано лише число
            elif len(parts) == 2:
                self.n = int(parts[0])  # Чисельник з першої частини
                self.d = int(parts[1])  # Знаменник з другої частини
            else:
                raise ValueError("Невірний формат раціонального числа")
        else:
            # Якщо передано два числа
            self.n = numerator  # Чисельник
            self.d = denominator  # Знаменник

        # Перевірка на нульовий знаменник
        if self.d == 0:
            raise ZeroDivisionError("Знаменник не може бути нулем")

        # Скорочення дробу
        self._simplify()

    def _simplify(self):
        """
        Приватний метод для скорочення дробу.
        Знаходить НСД чисельника і знаменника та ділить їх на нього.
        Також виправляє знак (знаменник завжди додатній).
        """
        # Знаходимо найбільший спільний дільник
        gcd_value = math.gcd(abs(self.n), abs(self.d))
        # Скорочуємо дріб
        self.n = self.n // gcd_value
        self.d = self.d // gcd_value

        # Якщо знаменник від'ємний, переносимо мінус до чисельника
        if self.d < 0:
            self.n *= -1
            self.d *= -1

    # Арифметичні операції ==============================================

    def __add__(self, other):
        """
        Перевантаження оператора додавання (+).
        Підтримує додавання Rational + Rational або Rational + int.
        """
        if isinstance(other, int):
            other = Rational(other)  # Конвертуємо ціле число в Rational
        if not isinstance(other, Rational):
            raise TypeError("Непідтримуваний тип операнда для +")

        # Формула додавання дробів: a/b + c/d = (ad + bc)/bd
        new_n = self.n * other.d + other.n * self.d
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __sub__(self, other):
        """
        Перевантаження оператора віднімання (-).
        Підтримує віднімання Rational - Rational або Rational - int.
        """
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            raise TypeError("Непідтримуваний тип операнда для -")

        # Формула віднімання дробів: a/b - c/d = (ad - bc)/bd
        new_n = self.n * other.d - other.n * self.d
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __mul__(self, other):
        """
        Перевантаження оператора множення (*).
        Підтримує множення Rational * Rational або Rational * int.
        """
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            raise TypeError("Непідтримуваний тип операнда для *")

        # Формула множення дробів: a/b * c/d = ac/bd
        new_n = self.n * other.n
        new_d = self.d * other.d
        return Rational(new_n, new_d)

    def __truediv__(self, other):
        """
        Перевантаження оператора ділення (/).
        Підтримує ділення Rational / Rational або Rational / int.
        """
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            raise TypeError("Непідтримуваний тип операнда для /")
        if other.n == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе")

        # Формула ділення дробів: a/b / c/d = ad/bc
        new_n = self.n * other.d
        new_d = self.d * other.n
        return Rational(new_n, new_d)

    # Реверсні оператори (для випадків, коли ціле число зліва) ==========

    def __radd__(self, other):
        """Додавання, коли ціле число зліва: int + Rational"""
        return self.__add__(other)

    def __rsub__(self, other):
        """Віднімання, коли ціле число зліва: int - Rational"""
        return Rational(other) - self

    def __rmul__(self, other):
        """Множення, коли ціле число зліва: int * Rational"""
        return self.__mul__(other)

    def __rtruediv__(self, other):
        """Ділення, коли ціле число зліва: int / Rational"""
        return Rational(other) / self

    # Спеціальні оператори ===============================================

    def __call__(self):
        """
        Оператор круглих дужок - конвертує дріб у десяткове число.
        Наприклад: x = Rational(1,2); x() поверне 0.5
        """
        return self.n / self.d

    def __getitem__(self, key):
        """
        Оператор квадратних дужок - доступ до чисельника або знаменника.
        Наприклад: x["n"] - чисельник, x["d"] - знаменник
        """
        if key == "n":
            return self.n
        elif key == "d":
            return self.d
        else:
            raise KeyError("Невірний ключ. Використовуйте 'n' або 'd'")

    def __setitem__(self, key, value):
        """
        Оператор квадратних дужок - зміна чисельника або знаменника.
        Автоматично скорочує дріб після зміни.
        """
        if key == "n":
            self.n = value
        elif key == "d":
            if value == 0:
                raise ZeroDivisionError("Знаменник не може бути нулем")
            self.d = value
        else:
            raise KeyError("Невірний ключ. Використовуйте 'n' або 'd'")
        self._simplify()  # Скорочуємо дріб після зміни

    # Представлення об'єкта ==============================================

    def __str__(self):
        """Рядкове представлення дробу (наприклад '3/4' або '2')"""
        if self.d == 1:
            return str(self.n)  # Виводимо лише чисельник для цілих чисел
        return f"{self.n}/{self.d}"

    def __repr__(self):
        """Формальне представлення об'єкта для відладки"""
        return f"Rational({self.n}, {self.d})"


# Функції для обчислення виразів ========================================

def evaluate_expression(expr):
    """
    Обчислює арифметичний вираз з рядка, використовуючи Rational.

    Параметри:
        expr - рядок з арифметичним виразом (наприклад "1/2 + 3/4 * 2")

    Повертає:
        Об'єкт Rational з результатом обчислення
    """
    # Розбиваємо вираз на токени, додаючи пробіли навколо операторів
    tokens = expr.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').split()

    # Конвертуємо всі числа в об'єкти Rational
    for i in range(len(tokens)):
        if tokens[i] not in ('+', '-', '*', '/'):
            try:
                tokens[i] = Rational(tokens[i])
            except ValueError as e:
                raise ValueError(f"Невірний формат числа: {tokens[i]}") from e

    # Обробляємо множення та ділення (вищий пріоритет)
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in ('*', '/'):
            # Беремо лівий і правий операнди
            left = tokens[i - 1]
            right = tokens[i + 1]

            # Виконуємо операцію
            if token == '*':
                result = left * right
            else:
                result = left / right

            # Замінюємо три елементи (лівий, оператор, правий) на результат
            tokens[i - 1:i + 2] = [result]
            i -= 1  # Зменшуємо лічильник, оскільки масив скоротився
        else:
            i += 1

    # Обробляємо додавання та віднімання
    if len(tokens) == 0:
        return Rational(0)  # Порожній вираз

    result = tokens[0]  # Початковий результат - перший елемент
    i = 1
    while i < len(tokens):
        token = tokens[i]
        if token in ('+', '-'):
            right = tokens[i + 1]  # Правий операнд

            # Виконуємо операцію
            if token == '+':
                result += right
            else:
                result -= right
            i += 2  # Переходимо через оператор і операнд
        else:
            i += 1

    return result


def process_file(filename):
    """
    Обробляє файл з арифметичними виразами, обчислює кожен вираз
    і виводить результати.

    Параметри:
        filename - ім'я файлу з виразами (по одному на рядок)
    """
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # Видаляємо зайві пробіли
            if line:  # Якщо рядок не порожній
                try:
                    result = evaluate_expression(line)
                    # Виводимо вираз, результат у вигляді дробу та десяткового числа
                    print(f"{line} = {result} (десятковий: {result():.6f})")
                except Exception as e:
                    print(f"Помилка при обчисленні виразу '{line}': {e}")


# Головна частина програми ==============================================

if __name__ == "__main__":
    # Обробка файлу input01.txt
    print("Початок обчислення виразів з файлу input.txt")
    process_file("input.txt")
    print("Обчислення завершено")