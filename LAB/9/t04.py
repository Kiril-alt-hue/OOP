def P(k):
    Pn = 2
    yield Pn, 1
    for n in range(2, k+1):
        Pn = Pn * (1 + 1 / n**2)

        yield Pn, n

if __name__ == "__main__":
    k = int(input("k ="))

    for elem, num in P(k):
        print(f"x({num}) = {elem}")