#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

# Global target multiplicities are [1,1,3,2,1].  Candidate retained sets are
# nested exactly as source-adaptive multiplicity stripping requires.
options = [
    [(1, {4}), (2, {3, 4}), (3, {2, 3, 4})],
    [(1, {0}), (2, {0, 3}), (3, {0, 2, 3})],
    [(1, {1}), (3, {1, 2})],
]
num_targets = 5

pure_best = None
pure_choice = None
for choice in product(*[range(len(row)) for row in options]):
    loads = [Fraction(0) for _ in range(num_targets)]
    for x, j in enumerate(choice):
        retained = options[x][j][1]
        for y in retained:
            loads[y] += Fraction(1, len(retained))
    value = max(loads)
    if pure_best is None or value < pure_best:
        pure_best = value
        pure_choice = choice
assert pure_best == Fraction(5, 6)

alpha = [
    [Fraction(1, 5), Fraction(4, 5), Fraction(0)],
    [Fraction(2, 5), Fraction(0), Fraction(3, 5)],
    [Fraction(1, 5), Fraction(4, 5)],
]
loads = [Fraction(0) for _ in range(num_targets)]
for x, row in enumerate(options):
    assert sum(alpha[x]) == 1
    for j, (_h, retained) in enumerate(row):
        for y in retained:
            loads[y] += alpha[x][j] / len(retained)
assert loads == [Fraction(3, 5)] * num_targets
mixed_value = max(loads)

# Uniform dual prices: every nonempty uniform retained set has average price 1/5.
z = [Fraction(1, 5)] * num_targets
dual = Fraction(0)
for row in options:
    costs = [sum(z[y] for y in retained) / len(retained) for _h, retained in row]
    dual += min(costs)
assert dual == Fraction(3, 5) == mixed_value
positive = sum(a > 0 for row in alpha for a in row)
assert positive <= len(options) + num_targets - 1
print({
    "deterministic_optimum": str(pure_best),
    "deterministic_choice": pure_choice,
    "mixed_optimum": str(mixed_value),
    "column_loads": [str(x) for x in loads],
    "dual_value": str(dual),
    "positive_threshold_probabilities": positive,
})
