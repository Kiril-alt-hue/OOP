x = float(input("x = "))
k_max = int(input("k = "))

xk = x  # початкове значення x0 = x

for k in range(1, k_max + 1):
    xk = xk * x**2 / ((2*k) * (2*k + 1))
    print(f"x_{k} = {xk}")

print(f"\nРезультат: x_{k_max} = {xk}")