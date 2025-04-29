def det_generator(a, b):
    D_prev, D_curr = 1, a + b
    yield D_prev
    yield D_curr
    while True:
        D_next = (a + b) * D_curr - a * b * D_prev
        yield D_next
        D_prev, D_curr = D_curr, D_next


def det_by_counter(n, a, b):
    if n == 0:
        return 1
    if n == 1:
        return a + b

    d_prev, d_curr = 1, a + b
    for _ in range(2, n + 1):
        d_next = (a + b) * d_curr - a * b * d_prev
        d_prev, d_curr = d_curr, d_next
    return d_curr


def det_by_epsilon(a, b, eps=1e-6, max_iter=1000):
    gen = det_generator(a, b)
    prev = next(gen)
    curr = next(gen)

    for n in range(1, max_iter + 1):
        next_val = next(gen)
        if abs(next_val - curr) < eps:
            return next_val, n
        prev, curr = curr, next_val
    return curr, max_iter


def save_det_results(a, b, max_n, filename="results_c).txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Обчислення визначників для a={a}, b={b}\n")
        f.write("Рекурентна формула: D_n = (a+b)*D_{n-1} - ab*D_{n-2}\n\n")

        # Цикл з лічильником
        f.write("Цикл з лічильником:\n")
        f.write("n\tD_n\n")
        f.write("--------\n")
        for n in range(max_n + 1):
            f.write(f"{n}\t{det_by_counter(n, a, b)}\n")

        # Генератор-функція
        f.write("\nГенератор-функція:\n")
        f.write("n\tD_n\n")
        f.write("--------\n")
        gen = det_generator(a, b)
        for n in range(max_n + 1):
            f.write(f"{n}\t{next(gen)}\n")

        # Цикл з умовою
        final_val, iterations = det_by_epsilon(a, b)
        f.write(f"\nЦикл з умовою (ε=1e-6):\n")
        f.write(f"Остаточне значення: {final_val}\n")
        f.write(f"Досягнуто за {iterations} ітерацій\n")


if __name__ == "__main__":
    try:
        a, b = 2, 3
        max_n = 10
        save_det_results(a, b, max_n)
        print("Результати успішно збережено у файл 'results_c).txt'")
    except Exception as e:
        print(f"Сталася помилка: {e}")