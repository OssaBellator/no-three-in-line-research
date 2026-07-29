#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

# Project nominal (t,t) in weighted l1 distance |x-t|+2|y-t|
# onto P={x>=0,y>=0,x+y<=1,y<=3/5}.


def objective(t, x, y):
    return abs(x - t) + 2 * abs(y - t)


def candidates(t):
    # Intersections of x=0,y=0,x=t,y=t,x+y=1,y=3/5.
    lines = [
        (1, 0, Fraction(0)),
        (0, 1, Fraction(0)),
        (1, 0, t),
        (0, 1, t),
        (1, 1, Fraction(1)),
        (0, 1, Fraction(3, 5)),
    ]
    pts = set()
    for (a, b, c), (d, e, f) in combinations(lines, 2):
        det = a * e - b * d
        if det == 0:
            continue
        x = Fraction(c * e - b * f, det)
        y = Fraction(a * f - c * d, det)
        if x >= 0 and y >= 0 and x + y <= 1 and y <= Fraction(3, 5):
            pts.add((x, y))
    return pts


def projected_formula(t):
    if t <= Fraction(1, 2):
        return (t, t)
    if t <= Fraction(3, 5):
        return (1 - t, t)
    return (Fraction(2, 5), Fraction(3, 5))

breaks = []
last = None
for k in range(101):
    t = Fraction(k, 100)
    pts = candidates(t)
    vals = [(objective(t, x, y), x, y) for x, y in pts]
    best = min(vals)
    winners = [(x, y) for v, x, y in vals if v == best[0]]
    formula = projected_formula(t)
    assert formula in winners
    assert best[0] == objective(t, *formula)
    region = 0 if t <= Fraction(1, 2) else (1 if t <= Fraction(3, 5) else 2)
    if region != last:
        breaks.append((t, region))
        last = region

# KKT-style objective slopes on the three open regions.
# Value: 0, 2t-1, 3t-8/5.
for t in [Fraction(1, 4), Fraction(11, 20), Fraction(4, 5)]:
    x, y = projected_formula(t)
    val = objective(t, x, y)
    expected = Fraction(0) if t < Fraction(1, 2) else (2 * t - 1 if t < Fraction(3, 5) else 3 * t - Fraction(8, 5))
    assert val == expected

print({
    "samples": 101,
    "sampled_region_entries": breaks,
    "exact_breakpoints": (Fraction(1, 2), Fraction(3, 5)),
    "projection_at_4_5": projected_formula(Fraction(4, 5)),
    "distance_at_4_5": objective(Fraction(4, 5), *projected_formula(Fraction(4, 5))),
    "value_slopes": (0, 2, 3),
})
