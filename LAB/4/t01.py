import math

class Equation:
    INF = "Infinite number of solutions"

    def __init__(self, b, c):
        self.b = b
        self.c = c

    def solve(self):
        if self.b == 0:
            if self.c == 0:
                return Equation.INF
            else:
                return ()  # No solution
        else:
            return (-self.c / self.b,)

    def show(self):
        print(f"{self.b}x + {self.c} = 0")


class QuadraticEquation(Equation):
    def __init__(self, a, b, c):
        self.a = a
        super().__init__(b, c)

    def solve(self):
        if self.a == 0:
            return super().solve()

        d = self.b**2 - 4 * self.a * self.c

        if d < 0:
            return ()  # No real solutions
        elif d == 0:
            return (-self.b / (2 * self.a),)
        else:
            return (-self.b + math.sqrt(d)) / (2 * self.a), (-self.b - math.sqrt(d)) / (2 * self.a)

    def show(self):
        print(f"{self.a}x^2 + {self.b}x + {self.c} = 0")


class BiQuadraticEquation(QuadraticEquation):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def solve(self):
        quadratic_solutions = super().solve()
        solutions = []

        for y in quadratic_solutions:
            if y < 0:
                continue
            if y == 0:
                solutions.append(0)
            else:
                solutions.append(math.sqrt(y))
                solutions.append(-math.sqrt(y))

        return tuple(solutions)

    def show(self):
        print(f"{self.a}x^4 + {self.b}x^2 + {self.c} = 0")

if __name__ == "__main__":

    linear_eq = Equation(2, 3)
    print("Лінійне рівняння:")
    linear_eq.show()
    print("Розв'язок:", linear_eq.solve())


    quadratic_eq = QuadraticEquation(1, -5, 6)
    print("\nКвадратне рівняння:")
    quadratic_eq.show()
    print("Розв'язок:", quadratic_eq.solve())


    biquadratic_eq = BiQuadraticEquation(1, -5, 4)
    print("\nБіквадратне рівняння:")
    biquadratic_eq.show()
    print("Розв'язок:", biquadratic_eq.solve())
