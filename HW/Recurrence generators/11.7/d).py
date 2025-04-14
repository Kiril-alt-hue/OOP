def finite_generator(x, n):
    xk = 1.0  # x₀ = 1
    yield (0, xk)

    for k in range(1, n + 1):
        xk = xk * (k + 1) * x / (k * k)
        yield (k, xk)


def infinite_generator(x):
    xk = 1.0  # x₀ = 1
    yield (0, xk)
    k = 1

    while True:
        xk = xk * (k + 1) * x / (k * k)
        yield (k, xk)
        k += 1


# Головна програма
if __name__ == "__main__":
    x = float(input("x = "))
    k_max = int(input("k = "))

    print("\n1. Генератор до k_max-го члена:")
    for k, xk in finite_generator(x, k_max):
        print(f"x_{k} = {xk}")

    print("\n2. Нескінченний генератор (перші k_max+1 елементів):")
    infinite_gen = infinite_generator(x)
    for _ in range(k_max + 1):
        k, xk = next(infinite_gen)
        print(f"x_{k} = {xk}")