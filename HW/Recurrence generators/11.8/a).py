def finite_generator(n):
    S = 1  # S_1 = 1
    yield (1, S)

    for i in range(2, n + 1):
        S = S + (-1)**(i + 1) * i
        yield (i, S)


def infinite_generator():
    S = 1  # S_1 = 1
    yield (1, S)
    i = 2

    while True:
        S = S + (-1)**(i + 1) * i
        yield (i, S)
        i += 1


# Головна програма
if __name__ == "__main__":
    n = int(input("n = "))

    print("\n1. Генератор до n-го члена:")
    for i, S in finite_generator(n):
        print(f"S_{i} = {S}")

    print("\n2. Нескінченний генератор (перші n елементів):")
    infinite_gen = infinite_generator()
    for _ in range(n):
        i, S = next(infinite_gen)
        print(f"S_{i} = {S}")