def generator(max_n):
    S = 1
    a = 1
    n = 0
    yield S, n
    while n < max_n:
        a = -a
        n = n + 1
        S += a / n
        yield S, n

if __name__ == '__main__':
    for S, n in generator(10):
        print(S, n)