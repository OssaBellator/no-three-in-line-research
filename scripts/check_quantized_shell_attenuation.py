#!/usr/bin/env python3
from fractions import Fraction

A = Fraction(1, 2)
B = Fraction(2, 3)
C = Fraction(5, 6)
STAR = (Fraction(1, 3), Fraction(1, 6), Fraction(1, 2))


def feasible(x, y, z):
    return x >= 0 and y >= 0 and z >= 0 and x + y >= A and y + z >= B and z + x >= C


def ceil_grid(value, denominator):
    scaled = value * denominator
    quotient, remainder = divmod(scaled.numerator, scaled.denominator)
    return Fraction(quotient + bool(remainder), denominator)


def grid_optimum(denominator):
    best = None
    limit = 2 * denominator
    for i in range(limit + 1):
        for j in range(limit + 1):
            for k in range(limit + 1):
                point = (Fraction(i, denominator), Fraction(j, denominator), Fraction(k, denominator))
                if feasible(*point):
                    record = (sum(point), point)
                    if best is None or record < best:
                        best = record
    return best

assert feasible(*STAR)
assert sum(STAR) == 1

records = {}
for denominator in range(1, 21):
    rounded = tuple(ceil_grid(value, denominator) for value in STAR)
    assert feasible(*rounded)
    overhead = sum(rounded) - sum(STAR)
    assert 0 <= overhead < Fraction(3, denominator)
    optimum = grid_optimum(denominator)
    records[denominator] = (rounded, overhead, optimum)
    assert optimum[0] <= sum(rounded)

assert records[4][0] == (Fraction(1, 2), Fraction(1, 4), Fraction(1, 2))
assert records[4][1] == Fraction(1, 4)
assert records[4][2][0] == Fraction(5, 4)
assert records[6][2] == (Fraction(1), STAR)

print({
    "continuous_optimum": tuple(map(str, STAR)),
    "continuous_cost": str(sum(STAR)),
    "M4_ceiling_schedule": tuple(map(str, records[4][0])),
    "M4_grid_optimum": str(records[4][2][0]),
    "exact_denominator": 6,
    "verified_denominators": 20,
})
