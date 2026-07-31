#!/usr/bin/env python3
from fractions import Fraction
from math import gcd

BASE_LOSS = Fraction(7, 30)
TARGET = Fraction(1, 5)
REQUIRED_REDUCTION = BASE_LOSS - TARGET

ROWS = [
    ("hall", Fraction(1, 40), Fraction(1, 1)),
    ("boundary", Fraction(1, 60), Fraction(2, 1)),
    ("threshold", Fraction(1, 80), Fraction(3, 1)),
    ("prefix", Fraction(1, 96), Fraction(4, 1)),
    ("shell", Fraction(1, 120), Fraction(5, 1)),
    ("interaction", Fraction(1, 120), Fraction(6, 1)),
]

assert REQUIRED_REDUCTION == Fraction(1, 30)

remaining = REQUIRED_REDUCTION
allocation = {}
for name, cap, price in sorted(ROWS, key=lambda row: row[2]):
    take = min(cap, remaining)
    allocation[name] = take
    remaining -= take
assert remaining == 0

expected = {
    "hall": Fraction(1, 40),
    "boundary": Fraction(1, 120),
    "threshold": Fraction(0),
    "prefix": Fraction(0),
    "shell": Fraction(0),
    "interaction": Fraction(0),
}
assert allocation == expected
optimum_cost = sum(allocation[name] * price for name, _, price in ROWS)
assert optimum_cost == Fraction(1, 24)
assert BASE_LOSS - sum(allocation.values()) == TARGET

step_denominator = 1
for _, cap, _ in ROWS:
    step_denominator = step_denominator * cap.denominator // gcd(step_denominator, cap.denominator)
step_denominator = step_denominator * REQUIRED_REDUCTION.denominator // gcd(step_denominator, REQUIRED_REDUCTION.denominator)
assert step_denominator == 480
caps = [int(cap * step_denominator) for _, cap, _ in ROWS]
need = int(REQUIRED_REDUCTION * step_denominator)
prices = [price for _, _, price in ROWS]

best = None
best_vectors = []


def visit(i, remaining_units, vector):
    global best, best_vectors
    if i == len(ROWS):
        if remaining_units != 0:
            return
        cost = sum(Fraction(vector[j], step_denominator) * prices[j] for j in range(len(ROWS)))
        if best is None or cost < best:
            best = cost
            best_vectors = [tuple(vector)]
        elif cost == best:
            best_vectors.append(tuple(vector))
        return
    for units in range(min(caps[i], remaining_units) + 1):
        visit(i + 1, remaining_units - units, vector + [units])


visit(0, need, [])
assert best == optimum_cost
assert len(best_vectors) == 1
assert best_vectors[0] == tuple(int(expected[name] * step_denominator) for name, _, _ in ROWS)

lambda_price = Fraction(2)
for name, cap, price in ROWS:
    x = allocation[name]
    if price < lambda_price:
        assert x == cap
    elif price > lambda_price:
        assert x == 0
    else:
        assert 0 < x < cap

print({
    "required_reduction": str(REQUIRED_REDUCTION),
    "allocation": {name: str(value) for name, value in allocation.items()},
    "optimum_cost": str(optimum_cost),
    "dual_price": str(lambda_price),
    "grid_denominator": step_denominator,
    "optimal_vectors": len(best_vectors),
    "status": "passed",
})
