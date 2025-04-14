def finite_generator(x, n):
    xk = -x  # x1 = -x
    yield xk  # повертаємо x1
    for k in range(2, n + 1):
        xk = -xk * x * (k - 1) / k
        yield xk

def infinite_generator(x):
    xk = -x  # x1 = -x
    yield xk
    k = 2
    while True:
        xk = -xk * x * (k - 1) / k
        yield xk
        k += 1

# Головна програма
if __name__ == "__main__":
    x = float(input("x = "))
    k_max = int(input("k = "))

    print("\n1. Генератор до k_max-го члена:")
    finite_gen = finite_generator(x, k_max)
    for i, val in enumerate(finite_gen, start=1):  # індексація з 1
        print(f"x_{i} = {val}")

    print("\n2. Нескінченний генератор (перші k_max елементів):")
    infinite_gen = infinite_generator(x)
    for i in range(1, k_max + 1):
        print(f"x_{i} = {next(infinite_gen)}")