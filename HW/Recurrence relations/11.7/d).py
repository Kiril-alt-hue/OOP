x = float(input("x = "))
k_max = int(input("k = "))

xk = 1  # Початкове значення x_0 = 1
print(f"x_0 = {xk}")

for k in range(1, k_max + 1):
    xk = xk * (k + 1) * x / (k * k)
    print(f"x_{k} = {xk}")

print(f"\nРезультат: x_{k_max} = {xk}")