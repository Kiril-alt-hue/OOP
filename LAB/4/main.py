import t01

def process_equations(file_name):
    with open(file_name, 'r') as file:
        equations = []
        for line in file:
            coefficients = list(map(float, line.split()))
            if len(coefficients) == 2:
                eq = t01.Equation(*coefficients)
            elif len(coefficients) == 3:
                if coefficients[0] == 0:
                    eq = t01.Equation(coefficients[1], coefficients[2])
                else:
                    eq = t01.QudraticEquation(*coefficients)
            elif len(coefficients) == 4:
                eq = t01.BiOudraticEquation(coefficients[1], coefficients[2], coefficients[3])
            else:
                continue
            equations.append(eq)

    categorized = {"Немає розв'язків": [], "Один розв'язок": [], "Два розв'язки": [], "Три розв'язки": [], "Чотири розв'язки": [], "Безліч": []}
    one_solutions_values = []

    for eq in equations:
        solutions = eq.solve()
        if solutions == t01.Equation.INF:
            categorized["Безліч"].append(eq)
        elif len(solutions) == 0:
            categorized["Немає розв'язків"].append(eq)
        elif len(solutions) == 1:
            categorized["Один розв'язок"].append(eq)
            one_solutions_values.append(solutions[0])
        elif len(solutions) == 2:
            categorized["Два розв'язки"].append(eq)
        elif len(solutions) == 3:
            categorized["Три розв'язки"].append(eq)
        elif len(solutions) == 4:
            categorized["Чотири розв'язки"].append(eq)

    print("Рівняння без розв'язків:")
    for eq in categorized["Немає розв'язків"]:
        eq.show()

    print("\nРівняння з одним розв'язком:")
    for eq in categorized["Один розв'язок"]:
        eq.show()

    print("\nРівняння з двома розв'язками:")
    for eq in categorized["Два розв'язки"]:
        eq.show()

    print("\nРівняння з трьома розв'язками:")
    for eq in categorized["Три розв'язки"]:
        eq.show()

    print("\nРівняння з чотирма розв'язками:")
    for eq in categorized["Чотири розв'язки"]:
        eq.show()

    print("\nРівняння з безліч розв'язками:")
    for eq in categorized["Безліч"]:
        eq.show()

    if one_solutions_values:
        min_solution = min(one_solutions_values)
        max_solution = max(one_solutions_values)
        print(f"\nРівняння з найменшим розв'язком ({min_solution}):")
        for eq in categorized["Один розв'язок"]:
            if eq.solve()[0] == min_solution:
                eq.show()
                break

        print(f"\nРівняння з найбільшим розв'язком ({max_solution}):")
        for eq in categorized["Один розв'язок"]:
            if eq.solve()[0] == max_solution:
                eq.show()
                break


if __name__ == "__main__":
    process_equations("input01.txt")
