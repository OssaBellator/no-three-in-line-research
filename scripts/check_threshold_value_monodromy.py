#!/usr/bin/env python3
from fractions import Fraction as F

forms = {
    "E": (F(1), F(0)),
    "W": (F(-1), F(0)),
    "N": (F(0), F(1)),
    "S": (F(0), F(-1)),
}

def value(p):
    x, y = p
    return max(a * x + b * y for a, b in forms.values())

def active(p):
    v = value(p)
    return tuple(k for k, (a, b) in forms.items() if a * p[0] + b * p[1] == v)

path = [
    (F(2), F(1)),
    (F(1), F(2)),
    (F(-1), F(2)),
    (F(-2), F(1)),
    (F(-2), F(-1)),
    (F(-1), F(-2)),
    (F(1), F(-2)),
    (F(2), F(-1)),
    (F(2), F(1)),
]

assert sum((value(q) - value(p) for p, q in zip(path, path[1:])), F(0)) == 0

def segment_integral(p, q):
    cuts = {F(0), F(1)}
    dx, dy = q[0] - p[0], q[1] - p[1]
    keys = list(forms)
    for i, k in enumerate(keys):
        a, b = forms[k]
        for l in keys[i + 1:]:
            c, d = forms[l]
            den = (a - c) * dx + (b - d) * dy
            num = -((a - c) * p[0] + (b - d) * p[1])
            if den and F(0) <= num / den <= F(1):
                cuts.add(num / den)
    cuts = sorted(cuts)
    total = F(0)
    cells = []
    for s, t in zip(cuts, cuts[1:]):
        mid = (s + t) / 2
        r = (p[0] + mid * dx, p[1] + mid * dy)
        act = active(r)
        assert len(act) == 1
        k = act[0]
        a, b = forms[k]
        total += (t - s) * (a * dx + b * dy)
        cells.append(k)
    return total, tuple(cells)

atlas_integral = F(0)
visited = []
for p, q in zip(path, path[1:]):
    val, cells = segment_integral(p, q)
    atlas_integral += val
    visited.extend(cells)
assert atlas_integral == 0
assert set(visited) == set(forms)

a = (F(2), F(1))
b = (F(-1), F(-2))
route1 = [a, (F(1), F(2)), (F(-1), F(2)), (F(-2), F(-1)), b]
route2 = [a, (F(2), F(-1)), (F(1), F(-2)), b]
for route in (route1, route2):
    total = sum((segment_integral(p, q)[0] for p, q in zip(route, route[1:])), F(0))
    assert total == value(b) - value(a) == F(0)

print({
    "basis_cells": len(forms),
    "closed_path_segments": len(path) - 1,
    "visited_cells": sorted(set(visited)),
    "closed_integral": str(atlas_integral),
    "endpoint_value_difference": str(value(b) - value(a)),
})
