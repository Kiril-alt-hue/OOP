def finite_generator(n):
    S = 0  # S_1 = 0
    yield (1, S)

    for k in range(2, n + 1):
        S = S + ((-1)**k * (k - 1)) / k
        yield (k, S)


def infinite_generator():
    S = 0  # S_1 = 0
    yield (1, S)
    k = 2

    while True:
        S = S + ((-1)**k * (k - 1)) / k
        yield (k, S)
        k += 1


# Головна програма
if __name__ == "__main__":
    n = int(input("n = "))

    print("\n1. Генератор до n-го члена:")
    for k, S in finite_generator(n):
        print(f"S_{k} = {S}")

    print("\n2. Нескінченний генератор (перші n елементів):")
    infinite_gen = infinite_generator()
    for _ in range(n):
        k, S = next(infinite_gen)
        print(f"S_{k} = {S}")