#!/usr/bin/env python3
from fractions import Fraction as F

a1 = (F(1, 2), F(1, 2), F(0))
a2 = (F(0), F(1, 2), F(1, 2))


def dot(a, d):
    return sum(x * y for x, y in zip(a, d))


best = None
best_directions = []
checked = 0
for i in range(-8, 9):
    for j in range(-8, 9):
        k = -i - j
        if not -8 <= k <= 8:
            continue
        d = (F(i, 8), F(j, 8), F(k, 8))
        checked += 1
        tau = max(dot(a1, d), dot(a2, d))
        if best is None or tau < best:
            best = tau
            best_directions = [d]
        elif tau == best:
            best_directions.append(d)

assert best == F(-1, 4)
assert (F(1, 2), F(-1), F(1, 2)) in best_directions

certificate_weights = (F(1, 2), F(1, 2))
opt = (F(1, 2), F(-1), F(1, 2))
average_slope = certificate_weights[0] * dot(a1, opt) + certificate_weights[1] * dot(a2, opt)
assert dot(a1, opt) == dot(a2, opt) == average_slope == best

print({
    "grid_directions_checked": checked,
    "optimal_worst_log_slope": str(best),
    "optimal_direction": [str(x) for x in opt],
    "active_cycle_slopes": [str(dot(a1, opt)), str(dot(a2, opt))],
    "dual_cycle_weights": [str(x) for x in certificate_weights],
    "optimal_grid_directions": len(best_directions),
})
