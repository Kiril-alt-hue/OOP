# from sympy import Matrix
#
#
# n = int(input("Введи розмір матриці n: "))
# matrix = []
#
# print("Введи матрицю построково:")
# for _ in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)
#
# A = Matrix(matrix)
# print(f"Визначник: {A.det()}")
#
#
def det(n):
    yield 2
    yield 1

    i = 3
    d_prev_1 = 1
    d_prev_2 = 2
    for i in range(3, n+1):
        d = 2*d_prev_1 + 3*d_prev_2
        d_prev_1, d_prev_2 = d_prev_2, d
        yield d

if __name__ == "__main__":
    for

