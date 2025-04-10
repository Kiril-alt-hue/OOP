n = int(input("n = "))

# останній знаменник — це 4n + 2
lambda_k = 4 * n + 2

# обчислюємо ланцюговий дріб зсередини назовні
for k in range(2, n + 1):
    # знаменник на поточному рівні: 4*(n-k+1) + 2
    denominator = 4 * (n - k + 1) + 2
    lambda_k = denominator + 1 / lambda_k
    print(f"lambda_{k} (intermediate) = {lambda_k}")


lambda_n = 2 + 1 / lambda_k
print(f"\nРезультат: lambda_{n} = {lambda_n}")