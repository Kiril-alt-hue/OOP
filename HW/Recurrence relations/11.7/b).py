x = float(input("x = "))
k_max = int(input("k = "))

xk = -x

print(f"\nx_1 = {xk}")

for k in range(2, k_max + 1):
    xk = -xk * x * (k-1) / k
    print(f"x_{k} = {xk}")