import math

x = 1
eps = 0.0000001  # точність

n = 0
a = x
S = a

while abs(a) > eps:
    n += 1
    a *= -1 * x**2 / ((2 * n) * (2 * n + 1))  # рекурентне співвідношення
    S += a

print(f"{n = }sin({x}) ≈ {S}")
print(f"Перевірка через math.sin: {math.sin(x)}")