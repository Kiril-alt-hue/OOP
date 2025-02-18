class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


        # self.d = self.b ** 2 - 4 * self.a * self.c # дискримінант - не можна,
        # # бо може порушитися цілісність даних, отже робимо метод

    def __str__(self):
        return f"{self.a}x^2 + {self.b}x + {self.c} = 0"

    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    #def show(self):
        #print(self)

    #def solutions_number(self):
        # залежить від дискримінанту
        #return 0

    def solve(self):
        solve_lst = []
        if self.a == 0:
            if self.b == 0:
                if self.c == 0:
                    return "Безліч розв'язків"
                else:
                    return "Розв'язків не існує"
            else:
                  solve_lst.append(-self.c/self.b)
                  return solve_lst                                  #return -self.c / self.b
        else:
            d = self.discriminant()
            if d < 0:
                return "Дискримінант менше за нуль -> розв'язків не існує"
            elif d == 0:
                solve_lst.append(-self.b / 2 * self.a)
            else:
                solve_lst.append((-self.b + d**0.5)/2 * self.a)
                solve_lst.append((-self.b - d ** 0.5)/ 2 * self.a)

            return solve_lst  # список чи кортеж розвʼязків



if __name__ == '__main__':  # блок тестування класу
    eq = QuadraticEquation( -25, 0, 48)
    # eq.show()
    print(eq)
    print(f"Дискримінант рівняння {eq} буде {eq.discriminant()}."
          f" Розв'язки рівняння -> {eq.solve()}")
          #f"Розв'язки рівняння - {}")
    # eq.discriminant() = 100500
    #eq.a = 100560
    #print(f"дискримінант рівняння {eq} буде {eq.discriminant()}")
    # r = str(eq)
    # print(r)
