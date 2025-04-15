import math

def seq(n):
    P = 1/2
    a = 2
    for i in range(2,n+1):
        a *= (i + 1)
        P *= 1/a
    return P

if __name__ == "__main__":
    n = int(input("n = "))
    print(seq(n))
    print(f"\nРезультат: P_{n} = {P}")