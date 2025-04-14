def finite_generator(n):
    P = 2/3  # P_1 = 2/3
    yield (1, P)

    for i in range(2, n + 1):
        P = P * (i + 1) / (i + 2)
        yield (i, P)


def infinite_generator():
    P = 2/3  # P_1 = 2/3
    yield (1, P)
    i = 2

    while True:
        P = P * (i + 1) / (i + 2)
        yield (i, P)
        i += 1


# Головна програма
if __name__ == "__main__":
    n = int(input("n = "))

    print("\n1. Генератор до n-го члена:")
    for i, P in finite_generator(n):
        print(f"P_{i} = {P}")

    print("\n2. Нескінченний генератор (перші n елементів):")
    infinite_gen = infinite_generator()
    for _ in range(n):
        i, P = next(infinite_gen)
        print(f"P_{i} = {P}")