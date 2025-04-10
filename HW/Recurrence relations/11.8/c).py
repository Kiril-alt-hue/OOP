n = int(input("n = "))

S = 0  # Початкове значення S_1 = 0
print(f"S_1 = {S}")

for k in range(2, n + 1):
    S = S + ((-1)**k * (k-1)) / k
    print(f"S_{k} = {S}")

print(f"\nРезультат: S_{n} = {S}")