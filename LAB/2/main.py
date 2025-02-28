from Matrix2D import Matrix2D
from Vector2D import Vector2D
from Solver import Solver
import sys

def solve(matrix_file, rhs_file, out_file = None):
    lst = []
    with open (matrix_file, "r") as f:
        for line in f:
            if len(line.split()) == 4:
                lst.append(Matrix2D([int (l) for l in line.split()]))

    lst_rhs = []
    with open(rhs_file, "r") as f:
        for line in f:
            if len(line.split()) == 2:
                lst_rhs.append(Vector2D([int (l) for l in line.split()]))

    if out_file is not None:
        out = open(out_file, 'w')
    else:
        out = sys.stdout

    for i in range(len(lst)):
        s = Solver(lst[i], lst_rhs[i])
        x = s.solve()
        print(x, file=out)

    if out_file is not None:
        out.close()

if __name__ == "__main__":
    solve("matrix_file", "rhs_file", "out")