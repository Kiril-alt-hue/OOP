P = 2
for n in range(2, 11):
    P = P * (1 + 1/(n ** 2))
    print(f"P = {P}")