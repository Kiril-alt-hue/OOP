def compute_recursive(x, k):
    if k == 0:
        return 1.0
    return compute_recursive(x, k - 1) * (x ** 2) / ((2 * k) * (2 * k - 1))


def sequence_generator(x):
    a = 1.0  # a_0
    yield a
    k = 1
    while True:
        a *= (x ** 2) / ((2 * k) * (2 * k - 1))
        yield a
        k += 1


def compute_with_counter(x, max_k):
    results = []
    a = 1.0
    results.append(a)
    for k in range(1, max_k + 1):
        a *= (x ** 2) / ((2 * k) * (2 * k - 1))
        results.append(a)
    return results


def compute_with_condition(x, epsilon=1e-6):
    results = []
    gen = sequence_generator(x)
    while True:
        a = next(gen)
        results.append(a)
        if abs(a) < epsilon:
            break
    return results


def save_to_file(x, max_k, filename="results_a).txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Обчислення послідовності a_k = x^(2k)/(2k)! для x = {x}\n")
        f.write("Рекурентне співвідношення: a_k = a_(k-1) * x²/(2k(2k-1))\n\n")


        f.write("Цикл з лічильником (k=0..max_k):\n")
        results = compute_with_counter(x, max_k)
        for k, a in enumerate(results):
            f.write(f"a_{k} = {a}\n")


        f.write("\nЦикл з умовою (до |a_k| < 1e-6):\n")
        results = compute_with_condition(x)
        for k, a in enumerate(results):
            f.write(f"a_{k} = {a}\n")


if __name__ == "__main__":
    x = 2.0
    max_k = 10
    save_to_file(x, max_k)
    print(f"Результати збережено у файл 'results_a).txt'")