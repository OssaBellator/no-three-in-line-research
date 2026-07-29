#!/usr/bin/env python3
from fractions import Fraction

STAR = (Fraction(4, 5), Fraction(3, 10))
C = (Fraction(2), Fraction(1))


def feasible(x, y):
    return (
        x >= 0
        and y >= 0
        and x <= Fraction(4, 5)
        and y <= Fraction(3, 10)
        and x + y <= Fraction(11, 10)
        and 2 * x + y <= Fraction(19, 10)
    )


def objective(point):
    x, y = point
    return C[0] * x + C[1] * y


def floor_grid(value, denominator):
    scaled = value * denominator
    return Fraction(scaled.numerator // scaled.denominator, denominator)

records = []
for denominator in range(1, 101):
    rounded = tuple(floor_grid(value, denominator) for value in STAR)
    assert feasible(*rounded)
    loss = objective(STAR) - objective(rounded)
    assert loss >= 0
    assert loss < sum(C) / denominator

    grid_points = []
    for i in range(denominator + 1):
        for j in range(denominator + 1):
            point = (Fraction(i, denominator), Fraction(j, denominator))
            if feasible(*point):
                grid_points.append((objective(point), point))
    best_value = max(value for value, _ in grid_points)
    assert objective(rounded) == best_value
    records.append((denominator, rounded, loss))

m7 = records[6]
m10 = records[9]
assert m7[1] == (Fraction(5, 7), Fraction(2, 7))
assert m7[2] == Fraction(13, 70)
assert m10[1] == STAR and m10[2] == 0

print({
    "continuous_optimum": tuple(map(str, STAR)),
    "continuous_objective": str(objective(STAR)),
    "M7_design": tuple(map(str, m7[1])),
    "M7_loss": str(m7[2]),
    "exact_denominator": 10,
    "verified_denominators": 100,
})
