def generator(n=-1):
    S = 1
    k = 1
    yield S, k
    while k < n + 1:
        k = k + 1
        S = S + k
        yield S, k

if __name__ == '__main__':
    for S, k in generator():
        if abs(S) < 0.1:
            break

        print(f"n({k}) = {S}")