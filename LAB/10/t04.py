def sum(n):
    a_2 = 0
    a_1 = 1
    S = 2**1 * a_2 + 2**2 * a_1

    for i in range(3, n+1):
        a_current = a_2 + i * a_2
        S = 2**1 * i * a_current
        print(S, i)
        a_2, a_1 = a_1, a_current

    return S

print(sum(2))