from t01 import QuadraticEquation

equations = []  # буде містити список всіх рівнянь прочитаних з файлу
none_solut = []  # немає розв'язків
one_solut = []  # один розв'язок
two_solut = []  # два розв'язки
inf_solut = []  # нескінченна кількість розв'язків

with open("input01.txt") as f:
    for line in f:
        print(line)
        try:
            a, b, c = [int(elem) for elem in line.split()]
            equations.append(QuadraticEquation(a, b, c))
        except ValueError:
            pass

maxim_solut = [None, None]
minim_solut = [None, None]

for eq in equations:
    solution = eq.solve()

    if solution == QuadraticEquation.INF:
        inf_solut.append(eq)
    elif len(solution) == 0:
        none_solut.append(eq)
    elif len(solution) == 1:
        one_solut.append(eq)
        if maxim_solut[0] is None or solution[0] > maxim_solut[0]:
            maxim_solut = [solution[0], eq]
        if minim_solut[0] is None or solution[0] < minim_solut[0]:
            minim_solut = [solution[0], eq]
    elif len(solution) == 2:
        two_solut.append(eq)

print(f"Рівняння, що мають 0 розв'язків - {none_solut}")
print(f"Рівняння, що мають 1 розв'язок - {one_solut}")
print(f"Найбільший розв'язок для рівнянь, що мають 1 корінь - {maxim_solut}")
print(f"Найменший розв'язок для рівнянь, що мають 1 корінь - {minim_solut}")
print(f"Рівняння, що мають 2 розв'язки - {two_solut}")
print(f"Рівняння, що мають безліч розв'язків - {inf_solut}")