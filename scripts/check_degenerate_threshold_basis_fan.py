#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import combinations

columns = [(F(1), F(0)), (F(1), F(1)), (F(0), F(1)), (F(0), F(2))]
cost = [F(1), F(0), F(1), F(2)]


def inv2(matrix):
    (a, b), (c, d) = matrix
    det = a * d - b * c
    if det == 0:
        return None
    return [[d / det, -b / det], [-c / det, a / det]]


def basis_data(basis, t):
    matrix = [[columns[j][i] for j in basis] for i in range(2)]
    inverse = inv2(matrix)
    if inverse is None:
        return None
    rhs = [F(1), F(1, 2) + t]
    x = [sum(inverse[i][r] * rhs[r] for r in range(2)) for i in range(2)]

    transpose = [[matrix[j][i] for j in range(2)] for i in range(2)]
    inverse_transpose = inv2(transpose)
    y = [sum(inverse_transpose[i][r] * cost[basis[r]] for r in range(2)) for i in range(2)]
    reduced = [cost[j] - sum(y[i] * columns[j][i] for i in range(2)) for j in range(4)]
    return x, y, reduced


def optimal_bases(t):
    out = []
    for basis in combinations(range(4), 2):
        data = basis_data(basis, t)
        if data is None:
            continue
        x, y, reduced = data
        if all(value >= 0 for value in x) and all(value >= 0 for value in reduced):
            out.append((basis, x, y, reduced))
    return out

# The pre-wall basis is unique, while the wall has three dual-feasible representations.
assert [b for b, *_ in optimal_bases(F(49, 100))] == [(0, 1)]
wall = optimal_bases(F(1, 2))
assert [b for b, *_ in wall] == [(0, 1), (1, 2), (1, 3)]
assert [b for b, *_ in optimal_bases(F(51, 100))] == [(1, 2), (1, 3)]

# Tangent feasibility at the degenerate wall.
drhs = [F(0), F(1)]
continuations = []
for basis, x, _, _ in wall:
    matrix = [[columns[j][i] for j in basis] for i in range(2)]
    inverse = inv2(matrix)
    derivative = [sum(inverse[i][r] * drhs[r] for r in range(2)) for i in range(2)]
    tangent_feasible = all(value > 0 or derivative[i] >= 0 for i, value in enumerate(x))
    if tangent_feasible:
        continuations.append((basis, derivative))
assert continuations == [((1, 2), [F(0), F(1)]), ((1, 3), [F(0), F(1, 2)])]
assert min(basis for basis, _ in continuations) == (1, 2)

# Audit 101 rational path points and choose Bland's lexicographically first continuation.
path = []
for i in range(101):
    t = F(i, 100)
    bases = optimal_bases(t)
    chosen = min(basis for basis, *_ in bases)
    path.append((t, chosen))
assert path[49][1] == (0, 1)
assert path[50][1] == (0, 1)
assert path[51][1] == (1, 2)

print({
    "path_points": len(path),
    "wall_time": str(F(1, 2)),
    "wall_bases": [list(basis) for basis, *_ in wall],
    "forward_feasible_bases": [list(basis) for basis, _ in continuations],
    "bland_continuation": [1 + j for j in min(basis for basis, _ in continuations)],
})
