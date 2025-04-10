import math

n = int(input("n = "))

P = 3  # Початкове значення P_1 = 3
print(f"P_1 = {P}")

for i in range(2, n + 1):
    P = P * (2 + 1 / math.factorial(i))
    print(f"P_{i} = {P}")

print(f"\nРезультат: P_{n} = {P}")