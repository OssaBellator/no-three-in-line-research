#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product

# Two marker states, each mixing two actions.  Let x,y be probabilities of the
# expensive action.  Robust contraction requires x>=1/3 and y>=1/2, while a
# shared resource budget requires x+y<=5/6.  Hence the unique feasible policy
# is (1/3,1/2).  The rows below realize those exact inequalities.

candidates = [F(i, 60) for i in range(61)]
feasible = []
for x, y in product(candidates, repeat=2):
    gaps = {
        "state0_scenario0": x - F(1, 3),
        "state0_scenario1": x - F(1, 4),
        "state1_scenario0": y - F(1, 2),
        "state1_scenario1": y - F(2, 5),
        "shared_budget": F(5, 6) - x - y,
    }
    if all(v >= 0 for v in gaps.values()):
        feasible.append((x, y))

assert feasible == [(F(1, 3), F(1, 2))]

dual_margin = F(1, 3) + F(1, 2) - F(4, 5)
assert dual_margin == F(1, 30)

x, y = feasible[0]
Q = [
    [F(1, 5) + x * F(1, 10), F(1, 10) - x * F(1, 20)],
    [F(1, 8) - y * F(1, 20), F(1, 4) + y * F(1, 20)],
]
w = [F(1), F(1)]
row_loads = [sum(row[j] * w[j] for j in range(2)) for row in Q]
assert row_loads == [F(19, 60), F(3, 8)]
assert max(row_loads) < F(2, 5)

print({
    "unique_policy": [str(x), str(y)],
    "shared_budget": str(F(5, 6)),
    "closed_loop_row_loads": [str(v) for v in row_loads],
    "impossible_budget": str(F(4, 5)),
    "dual_separator_margin": str(dual_margin),
})
