def finite_generator(n):
    lambda_k = 4 * n + 2
    yield (n, lambda_k)


    for k in range(n - 1, 0, -1):
        denominator = 4 * (n - k + 1) + 2
        lambda_k = denominator + 1 / lambda_k
        yield (k, lambda_k)


def infinite_generator(n_start):
    k = n_start
    lambda_k = 4 * k + 2
    yield (k, lambda_k)
    k -= 1

    while k > 0:
        denominator = 4 * (n_start - k + 1) + 2
        lambda_k = denominator + 1 / lambda_k
        yield (k, lambda_k)
        k -= 1


# Головна програма
if __name__ == "__main__":
    n = int(input("n = "))

    print("\n1. Генератор до n-го члена (зсередини назовні):")
    for k, lambda_k in finite_generator(n):
        print(f"lambda_{k} = {lambda_k}")

    print("\n2. Нескінченний генератор (перші n елементів, починаючи з lambda_n):")
    infinite_gen = infinite_generator(n)
    for _ in range(n):
        k, lambda_k = next(infinite_gen)
        print(f"lambda_{k} = {lambda_k}")