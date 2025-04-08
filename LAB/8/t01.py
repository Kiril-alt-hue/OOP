xk = 1
x = float(input("x = "))
n = int(input("n = "))

for k in range(1, n + 1):
    xk = - xk * x**2 / ((2*k - 1) * 2 * k)

print(f"xk = {xk}")