#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product

cycles = {
    "C01": (1, 1, 0),
    "C12": (0, 1, 1),
    "C02": (1, 0, 1),
}

grid = [F(i, 2) for i in range(5)]
def solve(names):
    feasible = []
    for x in product(grid, repeat=3):
        if all(sum(cycles[name][e] * x[e] for e in range(3)) >= 1 for name in names):
            feasible.append((sum(x), x))
    return min(feasible)

cost2, x2 = solve(("C01", "C12"))
assert (cost2, x2) == (F(1), (F(0), F(1), F(0)))
assert sum(cycles["C02"][e] * x2[e] for e in range(3)) == 0

cost3, x3 = solve(tuple(cycles))
assert (cost3, x3) == (F(3, 2), (F(1, 2), F(1, 2), F(1, 2)))

y = {name: F(1, 2) for name in cycles}
for e in range(3):
    assert sum(y[name] * cycles[name][e] for name in cycles) == 1
assert sum(y.values()) == cost3

print({
    "initial_active_cycles": 2,
    "initial_solution": [str(v) for v in x2],
    "violated_cycle": "C02",
    "final_attenuation": [str(v) for v in x3],
    "minimum_cost": str(cost3),
    "dual_cycle_prices": {k: str(v) for k, v in y.items()},
})
