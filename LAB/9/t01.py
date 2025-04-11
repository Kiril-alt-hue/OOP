def generator(x):
    xk = 1
    yield xk, 0
    k = 0
    #for k in range(1, n + 1):
    while True:
        k = k + 1
        xk = - xk * x**2 / ((2*k - 1) * 2 * k)

        yield xk, k

if __name__ == '__main__':
    x = float(input("x = "))
    #print(generator(x, n))
    for elem, num in generator(x):
        if abs(elem) < 0.1:
            break

        print(f"x({num}) = {elem}")