from Rational_copy import *

class RationalList:
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = []
            for item in data:
                if isinstance(item, (Rational, int)):
                    self.data.append(Rational(item) if isinstance(item, int) else item)
                else:
                    raise TypeError("Елементи списку повинні бути типу Rational або int")

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        if isinstance(value, (Rational, int)):
            self.data[index] = Rational(value) if isinstance(value, int) else value
        else:
            raise TypeError("Елементи списку повинні бути типу Rational або int")

    def __len__(self):
        return len(self.data)

    def __add__(self, other):
        if isinstance(other, RationalList):
            new_data = self.data + other.data
            return RationalList(new_data)
        elif isinstance(other, (Rational, int)):
            new_data = self.data + [Rational(other) if isinstance(other, int) else other]
            return RationalList(new_data)
        else:
            raise TypeError("Непідтримуваний тип операнда для +")

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self.data += other.data
        elif isinstance(other, (Rational, int)):
            self.data.append(Rational(other) if isinstance(other, int) else other)
        else:
            raise TypeError("Непідтримуваний тип операнда для +=")
        return self

    def __str__(self):
        return str([str(item) for item in self.data])

    def __repr__(self):
        return f"RationalList({self.data})"


def evaluate_expression(expr):
    tokens = expr.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').split()
    for i in range(len(tokens)):
        if tokens[i] not in ('+', '-', '*', '/'):
            try:
                tokens[i] = Rational(tokens[i])
            except ValueError as e:
                raise ValueError(f"Невірний формат числа: {tokens[i]}") from e

    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in ('*', '/'):
            left = tokens[i - 1]
            right = tokens[i + 1]
            if token == '*':
                result = left * right
            else:
                result = left / right
            tokens[i - 1:i + 2] = [result]
            i -= 1
        else:
            i += 1

    if len(tokens) == 0:
        return Rational(0)

    result = tokens[0]
    i = 1
    while i < len(tokens):
        token = tokens[i]
        if token in ('+', '-'):
            right = tokens[i + 1]
            if token == '+':
                result += right
            else:
                result -= right
            i += 2
        else:
            i += 1

    return result


def process_file(input_filename, output_filename):
    rational_list = RationalList()
    with open(input_filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                numbers = line.split()
                for num in numbers:
                    try:
                        rational = Rational(num)
                        rational_list += rational
                    except Exception as e:
                        print(f"Помилка при обробці числа '{num}': {e}")

    sum_result = Rational(0)
    for num in rational_list:
        sum_result += num


    with open(output_filename, 'w', encoding="utf-8") as file:
        file.write(f"Сума всіх чисел: {sum_result} (десятковий: {sum_result():.6f})\n")
        file.write("Елементи списку:\n")
        for num in rational_list:
            file.write(f"{num}\n")

    print(f"Результати записано у файл {output_filename}")


if __name__ == "__main__":
    input_filename = "input.txt"
    output_filename = "output_5.3.2.txt"
    print(f"Початок обчислення суми чисел з файлу {input_filename}")
    process_file(input_filename, output_filename)
    print("Обчислення завершено")