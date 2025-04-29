def taylor_terms(x):
    term = x  # Перший член (k=0)
    k = 0
    yield 2 * term  # Перший член з коефіцієнтом 2

    while True:
        k += 1
        term *= (x ** 2) * (2 * k - 1) / (2 * k + 1)
        yield 2 * term


import math


def taylor_sum_counter(x, n):
    if abs(x) >= 1:
        raise ValueError("|x| має бути менше 1")

    gen = taylor_terms(x)
    total = 0.0
    for _ in range(n):
        total += next(gen)
    return total


def taylor_sum_epsilon(x, epsilon=1e-6, max_iter=1000):
    if abs(x) >= 1:
        raise ValueError("|x| має бути менше 1")

    gen = taylor_terms(x)
    total = 0.0
    for k in range(max_iter):
        term = next(gen)
        total += term
        if abs(term) < epsilon:
            return total, k + 1  # Повертаємо суму та кількість ітерацій
    return total, max_iter


def save_results(x_values, n=10, filename="results_e).txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Обчислення ln((1+x)/(1-x)) за допомогою ряду Тейлора\n")
        f.write("Рекурентне співвідношення: t_k = t_{k-1} * (x²*(2k-1))/(2k+1)\n\n")

        # Цикл з лічильником
        f.write("Цикл з лічильником (n=10):\n")
        f.write("x\tНаближене\tMath\t\tРізниця\n")
        f.write("----------------------------------------\n")
        for x in x_values:
            try:
                approx = taylor_sum_counter(x, n)
                exact = math.log((1 + x) / (1 - x))
                f.write(f"{x:.3f}\t{approx:.8f}\t{exact:.8f}\t{abs(approx - exact):.2e}\n")
            except ValueError:
                continue

        # Цикл з умовою
        f.write("\nЦикл з умовою (ε=1e-6):\n")
        f.write("x\tНаближене\tІтерації\tMath\t\tРізниця\n")
        f.write("------------------------------------------------\n")
        for x in x_values:
            try:
                approx, iterations = taylor_sum_epsilon(x)
                exact = math.log((1 + x) / (1 - x))
                f.write(f"{x:.3f}\t{approx:.8f}\t{iterations}\t\t{exact:.8f}\t{abs(approx - exact):.2e}\n")
            except ValueError:
                continue


if __name__ == "__main__":
    test_values = [0.1, 0.3, 0.5, 0.7, 0.9]
    save_results(test_values)

    # Додатковий вивід для перевірки
    for x in test_values:
        try:
            approx, iter = taylor_sum_epsilon(x)
            exact = math.log((1 + x) / (1 - x))
            print(f"x={x:.1f}: Тейлор={approx:.8f} ({iter} ітер.), Math={exact:.8f}")
        except ValueError as e:
            print(f"Помилка для x={x:.1f}: {e}")

    print("Результати збережено у файл 'results_e).txt'")