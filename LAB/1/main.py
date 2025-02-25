from t01 import QuadraticEquation

equations = [] # буде містити список всіх рівнянь прочитаних з файлу
none_solut = [] # немає розв'язків
one_solut = [] # один розв'язок
two_solut = [] # два розв'язки
inf_solut = [] # нескінченна кількість розв'язків
with open("input01.txt") as f:
    for line in f:
        print(line)
        try:
            a, b, c = [int(elem) for elem in line.split()]
            equations.append(QuadraticEquation(a, b, c))
        except ValueError:
            pass

for eq in equations:
    maxim_solut = [None, None]
    minim_solut = [None, None]
    solution = eq.solve()
    #if len(solution) == 1 and solution[0] == None:
    if solution == QuadraticEquation.INF:
        inf_solut.append(eq)
    elif len(solution) == 0:
        none_solut.append(eq)
    elif len(solution) == 1:
        one_solut.append(eq)
        if maxim_solut[0] is None:
            maxim_solut = [solution[0], eq]
            minim_solut = [solution[0], eq]
        else:
            if solution[0] > maxim_solut[0]:
                maxim_solut = [solution[0], eq]
            if solution[0] < minim_solut[0]:
                minim_solut = [solution[0], eq]

    elif len(solution) == 2:
        two_solut.append(eq)

print(f"Рівняння, що мають 0 розв'язків - {}")



