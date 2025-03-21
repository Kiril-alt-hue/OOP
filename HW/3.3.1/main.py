from Triangle import *
from Rectangle import *
from Trapeze import *
from Parallelogram import *
from Circle import *
from Ball import *
from TriangularPyramid import *
from QuadrangularPyramid import *
from RectangularParallelepiped import *
from Cone import *
from TriangularPrism import *

def process_figures(file_path):
    figures = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            name = parts[0]
            params = list(map(float, parts[1:]))

            try:
                if name == "Triangle":
                    figures.append(Triangle([params[0], params[1], params[2]]))
                elif name == "Rectangle":
                    figures.append(Rectangle([params[0], params[1]]))
                elif name == "Trapeze":
                    figures.append(Trapeze([params[0], params[1]], [params[2], params[3]]))
                elif name == "Parallelogram":
                    figures.append(Parallelogram([params[0], params[1]], params[2]))
                elif name == "Circle":
                    figures.append(Circle(*params))
                elif name == "Ball":
                    figures.append(Ball(*params))
                elif name == "TriangularPyramid":
                    figures.append(TriangularPyramid(*params))
                elif name == "QuadrangularPyramid":
                    figures.append(QuadrangularPyramid([params[0], params[1]], params[2]))
                elif name == "RectangularParallelepiped":
                    figures.append(RectangularParallelepiped([params[0], params[1], params[2]]))
                elif name == "Cone":
                    figures.append(Cone(*params))
                elif name == "TriangularPrism":
                    figures.append(TriangularPrism([params[0], params[1], params[2]], params[3]))
            except ValueError as e:
                print(f"Помилка при створенні фігури {name}: {e}")
                continue

    max_figure = None
    max_volume = -1

    #знаходимо фігуру з найбільшою мірою
    for fig in figures:
        vol = fig.volume()
        if vol > max_volume:
            max_volume = vol
            max_figure = fig

    #використовую точно зазнечено utf-8, бо не читався result.txt
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(f"Фігура з найбільшою мірою: {max_figure.__class__.__name__}, volume = {max_volume}\n")

    return max_figure, max_volume

file_path = "input.txt"
max_fig, max_vol = process_figures(file_path)
print(f"Фігура з найбільшою мірою: {max_fig.__class__.__name__}, volume = {max_vol}")