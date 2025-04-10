n = int(input("n = "))

P = 1  # Початкове значення P_1 = 1
print(f"P_1 = {P}")

for i in range(2, n + 1):
    P = P * (1 - 1 / (i**2))
    print(f"P_{i} = {P}")

print(f"\nРезультат: P_{n} = {P}")