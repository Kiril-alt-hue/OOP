x = float(input("x = "))
k_max = int(input("k = "))

xk = 1  # Початкове значення x_0 = 1
print(f"x_0 = {xk}")

for k in range(1, k_max + 1):
    denominator = 1
    for i in range(k**2 - k + 1, k**2 + k + 1):
        denominator *= i
    xk = xk * (-x) / denominator
    print(f"x_{k} = {xk}")

print(f"\nРезультат: x_{k_max} = {xk}")