#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, product

OPTIONS = [
    [(Fraction(1, 3), 0, Fraction(1, 3), Fraction(1, 3), 0), (0, 0, 0, Fraction(1, 2), Fraction(1, 2))],
    [(Fraction(1, 2), 0, 0, Fraction(1, 2), 0), (0, Fraction(1, 2), 0, 0, Fraction(1, 2))],
    [(0, Fraction(1, 3), Fraction(1, 3), 0, Fraction(1, 3)), (0, Fraction(1, 2), 0, 0, Fraction(1, 2))],
]
OPTIONS = [[tuple(Fraction(v) for v in option) for option in row] for row in OPTIONS]
VARIABLES = [(x, h) for x in range(3) for h in range(2)]

def solve_square(A, b):
    n = len(A)
    matrix = [list(map(Fraction, A[i])) + [Fraction(b[i])] for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if matrix[r][col]), None)
        if pivot is None:
            return None
        matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
        scale = matrix[col][col]
        matrix[col] = [v / scale for v in matrix[col]]
        for r in range(n):
            if r == col or not matrix[r][col]:
                continue
            factor = matrix[r][col]
            matrix[r] = [matrix[r][j] - factor * matrix[col][j] for j in range(n + 1)]
    return [matrix[i][-1] for i in range(n)]

deterministic = Fraction(99)
for choice in product((0, 1), repeat=3):
    loads = [Fraction(0) for _ in range(5)]
    for x, h in enumerate(choice):
        loads = [a + b for a, b in zip(loads, OPTIONS[x][h])]
    deterministic = min(deterministic, max(loads))
assert deterministic == Fraction(5, 6)

certificates = []
for support_size in range(3, 7):
    for support in combinations(VARIABLES, support_size):
        if {x for x, _ in support} != {0, 1, 2}:
            continue
        active_size = support_size + 1 - 3
        if not 1 <= active_size <= 5:
            continue
        for active in combinations(range(5), active_size):
            A, b = [], []
            for x in range(3):
                A.append([Fraction(1 if sx == x else 0) for sx, _ in support] + [Fraction(0)])
                b.append(Fraction(1))
            for y in active:
                A.append([OPTIONS[x][h][y] for x, h in support] + [Fraction(-1)])
                b.append(Fraction(0))
            solution = solve_square(A, b)
            if solution is None:
                continue
            alpha, lam = solution[:-1], solution[-1]
            if any(a <= 0 for a in alpha) or lam < 0:
                continue
            loads = [Fraction(0) for _ in range(5)]
            for a, (x, h) in zip(alpha, support):
                for y in range(5):
                    loads[y] += a * OPTIONS[x][h][y]
            if max(loads) <= lam and lam == Fraction(3, 5):
                certificates.append((support, active, alpha, loads))

assert len(certificates) == 4
support, active, alpha, loads = certificates[0]
assert loads == [Fraction(3, 5)] * 5
assert alpha == [Fraction(1), Fraction(8, 15), Fraction(7, 15), Fraction(4, 5), Fraction(1, 5)]

print({
    "deterministic_optimum": str(deterministic),
    "basis_optimum": "3/5",
    "optimal_bases_found": len(certificates),
    "positive_variables": len(support),
    "active_columns_in_basis": len(active),
})
