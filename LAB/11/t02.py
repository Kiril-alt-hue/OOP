import math


eps = 0.0000000001
x = 1

n = 1
a = 1
S = a

while abs(a) > eps:
    a *= x * x/(2 * n * (2 * n - 1))
    S += a
    n += 1

print(f"{n = }: ch({x}) ≈ {S}")
print(f"Перевірка через math.sin: {math.cosh(x)}")