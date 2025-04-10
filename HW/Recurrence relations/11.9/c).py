n = int(input("n = "))

P = 2/3  # Початкове значення P_1 = 2/3
print(f"P_1 = {P}")

for i in range(2, n + 1):
    P = P * (i + 1) / (i + 2)
    print(f"P_{i} = {P}")

print(f"\nРезультат: P_{n} = {P}")