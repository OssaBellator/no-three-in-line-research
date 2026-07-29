#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import combinations

# V(x,y)=max of these affine pieces.
PIECES = {
    "x": (F(1), F(0), F(0)),
    "y": (F(0), F(1), F(0)),
    "tilted": (F(2), F(1), F(-9, 10)),
    "floor": (F(-1), F(-1), F(0)),
}
TAU = F(1, 2)
OBJECTIVE = (F(100), F(101))  # lexicographically favors y after x+y


def value(piece, point):
    a, b, c = PIECES[piece]
    x, y = point
    return a * x + b * y + c


def solve_two(rows, rhs):
    (a, b), (c, d) = rows
    det = a * d - b * c
    if det == 0:
        return None
    u, v = rhs
    return ((u * d - b * v) / det, (a * v - u * c) / det)


def restricted_optimum(active):
    constraints = [
        ("x>=0", (F(-1), F(0)), F(0)),
        ("y>=0", (F(0), F(-1)), F(0)),
        ("x<=1", (F(1), F(0)), F(1)),
        ("y<=1", (F(0), F(1)), F(1)),
    ]
    for name in active:
        a, b, c = PIECES[name]
        constraints.append((name, (a, b), TAU - c))

    candidates = []
    for left, right in combinations(constraints, 2):
        point = solve_two((left[1], right[1]), (left[2], right[2]))
        if point is None:
            continue
        if all(row[0] * point[0] + row[1] * point[1] <= bound for _, row, bound in constraints):
            score = OBJECTIVE[0] * point[0] + OBJECTIVE[1] * point[1]
            candidates.append((score, point, (left[0], right[0])))
    assert candidates
    return max(candidates, key=lambda item: (item[0], item[1][1], item[1][0]))


active = ["x"]
trace = []
while True:
    score, point, tight = restricted_optimum(active)
    violations = [(value(name, point) - TAU, name) for name in PIECES if value(name, point) > TAU]
    if not violations:
        trace.append(("done", point, score, tuple(active), tight))
        break
    violation, name = max(violations)
    trace.append(("cut", name, point, violation))
    active.append(name)

assert [step[0] for step in trace] == ["cut", "cut", "done"]
assert trace[0][1:] == ("tilted", (F(1, 2), F(1)), F(3, 5))
assert trace[1][1:] == ("y", (F(1, 5), F(1)), F(1, 2))
point = trace[-1][1]
score = trace[-1][2]
assert point == (F(9, 20), F(1, 2))
assert score == F(191, 2)
assert max(value(name, point) for name in PIECES) == TAU

# 50*(2x+y <= 7/5) + 51*(y <= 1/2) gives 100x+101y <= 191/2.
assert F(50) * F(7, 5) + F(51) * F(1, 2) == score
assert (F(50) * F(2), F(50) + F(51)) == OBJECTIVE

ray_limit = min(F(1, 2), F(1, 2), F(7, 15))
assert ray_limit == F(7, 15)
ray_point = (ray_limit, ray_limit)
assert max(value(name, ray_point) for name in PIECES) == TAU

print({
    "generated_value_cuts": [step[1] for step in trace[:-1]],
    "inverse_design_optimum": [str(x) for x in point],
    "objective_value": str(score),
    "active_dual_prices": {"tilted": "50", "y": "51"},
    "exact_ray_limit": str(ray_limit),
})
