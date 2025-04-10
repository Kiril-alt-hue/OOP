n = int(input("n = "))

S = 1  # Початкове значення S_1 = 1
print(f"S_1 = {S}")

for i in range(2, n + 1):
    S = S + (-1)**(i + 1) * i
    print(f"S_{i} = {S}")

print(f"\nРезультат: S_{n} = {S}")