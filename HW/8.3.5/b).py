def product_generator(n):
    P = 1.0
    yield P  # P_0 = 1 (опціонально)
    for k in range(1, n + 1):
        P *= (1 + 1 / (k ** 2))
        yield P

def compute_product(n):
    P = 1.0
    for k in range(1, n + 1):
        P *= (1 + 1 / (k ** 2))
    return P

def compute_product_epsilon(epsilon=1e-6):
    P = 1.0
    k = 1
    while True:
        term = (1 + 1 / (k ** 2))
        P *= term
        if abs(term - 1) < epsilon:
            break
        k += 1
    return P, k


def save_results(n, filename="results_b).txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Обчислення добутку P_n = ∏(1 + 1/k²) для n = {n}\n")
        f.write("Рекурентне співвідношення: P_k = P_{k-1} * (1 + 1/k²)\n\n")

        # Результати через цикл з лічильником
        f.write("Цикл з лічильником:\n")
        P = 1.0
        for k in range(1, n + 1):
            P *= (1 + 1 / (k ** 2))
            f.write(f"P_{k} = {P}\n")

        # Результати через генератор
        f.write("\nГенератор-функція:\n")
        gen = product_generator(n)
        next(gen)  # Пропускаємо P_0
        for k in range(1, n + 1):
            f.write(f"P_{k} = {next(gen)}\n")

        # Результат з умовою точності
        P_final, iterations = compute_product_epsilon()
        f.write(f"\nЦикл з умовою (до |1/k²| < 1e-6):\n")
        f.write(f"Остаточний P = {P_final} (досягнуто за {iterations} ітерацій)\n")


if __name__ == "__main__":
    n = 5
    save_results(n)
    print(f"Результати збережено у файл 'results_b).txt'")