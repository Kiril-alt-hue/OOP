import copy

class QuadraticEquation:

    INF = "Infinite number of solutions"

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"{self.a}x^2 + {self.b}x + {self.c} = 0"

    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def solve(self):
        solve_lst = []
        if self.a == 0:  # вироджене квадратне рівняння
            if self.b == 0:
                if self.c == 0:
                    return QuadraticEquation.INF
                else:
                    return ()  # "Розв'язків не існує"
            else:
                solve_lst.append(-self.c / self.b)
                return solve_lst  # return -self.c / self.b
        else:
            d = self.discriminant()
            if d < 0:  # немає розв'язків
                return ()  # "Дискримінант менше за нуль -> Розв'язків не існує"
            elif d == 0:  # є один розв'язок
                solve_lst.append((-self.b) / (2 * self.a))
            else:  # два корені
                solve_lst.append((-self.b + d ** 0.5) / (2 * self.a))
                solve_lst.append((-self.b - d ** 0.5) / (2 * self.a))

            return sorted(solve_lst)  # список чи кортеж розвʼязків

    def __copy__(self):
        # Створюємо новий об'єкт з тими самими значеннями a, b, c
        return QuadraticEquation(self.a, self.b, self.c)

    #def __deepcopy__(self, memo):
        # Для глибокого копіювання (у цьому випадку не потрібно, оскільки атрибути прості)
        #return QuadraticEquation(copy.deepcopy(self.a, memo),
                                 #copy.deepcopy(self.b, memo),
                                 #copy.deepcopy(self.c, memo))


if __name__ == '__main__':  # блок тестування класу
    eq = QuadraticEquation(1, -3, 2)
    print(eq)
    print(f"Дискримінант рівняння {eq} буде {eq.discriminant()}."
          f" Розв'язки рівняння -> {eq.solve()}")

    # Тестування конструктора копіювання
    eq_copy = copy.copy(eq)
    print("\nКопія рівняння:")
    print(eq_copy)
    print(f"Дискримінант копії рівняння {eq_copy} буде {eq_copy.discriminant()}."
          f" Розв'язки копії рівняння -> {eq_copy.solve()}")