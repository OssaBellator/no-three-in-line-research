#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import combinations

x0, y0 = F(4, 5), F(3, 4)
tau = F(9, 10)
sum_cap = tau + F(1, 5)

def value(x, y):
    return max(x, y, x + y - F(1, 5))

def objective(x, y):
    return 2 * abs(x - x0) + abs(y - y0)

def feasible(x, y, cap=tau):
    return F(0) <= x <= 1 and F(0) <= y <= 1 and value(x, y) <= cap

lines = [
    (F(1), F(0), F(0)), (F(1), F(0), F(1)),
    (F(0), F(1), F(0)), (F(0), F(1), F(1)),
    (F(1), F(0), tau), (F(0), F(1), tau),
    (F(1), F(1), sum_cap),
    (F(1), F(0), x0), (F(0), F(1), y0),
]

def intersect(l1, l2):
    a, b, c = l1
    d, e, f = l2
    det = a * e - b * d
    if det == 0:
        return None
    return ((c * e - b * f) / det, (a * f - c * d) / det)

candidates = set()
for l1, l2 in combinations(lines, 2):
    z = intersect(l1, l2)
    if z and feasible(*z):
        candidates.add(z)

best_value = min(objective(*z) for z in candidates)
best = sorted(z for z in candidates if objective(*z) == best_value)
assert best == [(F(4, 5), F(3, 10))]
x_star, y_star = best[0]
assert value(x_star, y_star) == tau
assert best_value == F(9, 20)

subgradient = (F(-1), F(-1))
dual_sum_price = F(1)
assert subgradient[0] + dual_sum_price == 0
assert subgradient[1] + dual_sum_price == 0
assert x_star + y_star == sum_cap

for x, y in candidates:
    lower = best_value + subgradient[0] * (x - x_star) + subgradient[1] * (y - y_star)
    assert objective(x, y) >= lower >= best_value

samples = []
for k in range(80, 136):
    cap = F(k, 100)
    if cap <= F(27, 20):
        x = x0
        y = cap - F(3, 5)
        assert feasible(x, y, cap)
        assert F(0) <= y <= y0
        assert objective(x, y) == F(27, 20) - cap
        samples.append((cap, x, y))

ray_boundary = F(11, 20)
assert value(ray_boundary, ray_boundary) == tau
assert value(ray_boundary + F(1, 100), ray_boundary + F(1, 100)) > tau

print({
    "nominal_design": [str(x0), str(y0)],
    "load_cap": str(tau),
    "nearest_design": [str(x_star), str(y_star)],
    "weighted_l1_distance": str(best_value),
    "active_value_piece": "x+y-1/5",
    "dual_sum_price": str(dual_sum_price),
    "parametric_cap_samples": len(samples),
    "diagonal_ray_boundary": str(ray_boundary),
})
