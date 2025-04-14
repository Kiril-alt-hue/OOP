def finite_generator(x, n):
    xk = x  # x0 = x
    yield xk  # повертаємо x0
    for k in range(1, n + 1):
        xk = xk * (x ** 2) / ((2 * k) * (2 * k + 1))
        yield xk

def infinite_generator(x):
    xk = x  # x0 = x
    yield xk
    k = 1
    while True:
        xk = xk * (x ** 2) / ((2 * k) * (2 * k + 1))
        yield xk
        k += 1

# Головна програма
if __name__ == "__main__":
    x = float(input("x = "))
    k_max = int(input("k = "))

    print("\n1. Генератор до k_max-го члена:")
    finite_gen = finite_generator(x, k_max)
    for i, val in enumerate(finite_gen):
        print(f"x_{i} = {val}")

    print("\n2. Нескінченний генератор (перші k_max + 1 елементів):")
    infinite_gen = infinite_generator(x)
    for i in range(k_max + 1):
        print(f"x_{i} = {next(infinite_gen)}")



##########НЕСКІНЧЕННЕ ВИВЕДЕННЯ####################
    # print("\n2. Нескінченний генератор:")
    # infinite_gen = infinite_generator(x)
    # i = 0
    # try:
    #     while True:
    #         val = next(infinite_gen)
    #         print(f"x_{i} = {val}")
    #         i += 1
    # except KeyboardInterrupt:
    #     print("\nЗупинено користувачем.")
