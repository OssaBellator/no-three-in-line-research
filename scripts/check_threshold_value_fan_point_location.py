#!/usr/bin/env python3
from fractions import Fraction as F
from collections import Counter

pieces = [
    ("x", (F(1), F(0))),
    ("y", (F(0), F(1))),
    ("-x+y", (F(-1), F(1))),
    ("-x", (F(-1), F(0))),
    ("-y", (F(0), F(-1))),
    ("x-y", (F(1), F(-1))),
]

def active_set(theta):
    x, y = theta
    values = [a * x + b * y for _, (a, b) in pieces]
    best = max(values)
    return tuple(i for i, value in enumerate(values) if value == best), best

histogram = Counter()
tie_points = 0
for ix in range(-20, 21):
    for iy in range(-20, 21):
        active, _ = active_set((F(ix, 10), F(iy, 10)))
        histogram[active] += 1
        tie_points += len(active) > 1
assert sum(histogram.values()) == 1681
assert tie_points == 121

theta0 = (F(-2), F(-1))
direction = (F(4), F(5, 2))
line_data = []
for name, (a, b) in pieces:
    intercept = a * theta0[0] + b * theta0[1]
    slope = a * direction[0] + b * direction[1]
    line_data.append((name, intercept, slope))

crossings = {F(0), F(1)}
for i in range(len(line_data)):
    for j in range(i + 1, len(line_data)):
        _, ai, bi = line_data[i]
        _, aj, bj = line_data[j]
        if bi != bj:
            t = (aj - ai) / (bi - bj)
            if 0 <= t <= 1:
                crossings.add(t)

segments = []
ordered = sorted(crossings)
for left, right in zip(ordered, ordered[1:]):
    mid = (left + right) / 2
    values = [a + b * mid for _, a, b in line_data]
    best = max(values)
    active = tuple(i for i, value in enumerate(values) if value == best)
    if not active:
        continue
    names = tuple(pieces[i][0] for i in active)
    if segments and segments[-1][2] == names and segments[-1][1] == left:
        segments[-1] = (segments[-1][0], right, names)
    else:
        segments.append((left, right, names))

assert segments == [
    (F(0), F(2, 5), ("-x",)),
    (F(2, 5), F(1, 2), ("-x+y",)),
    (F(1, 2), F(2, 3), ("y",)),
    (F(2, 3), F(1), ("x",)),
]

origin_active, origin_value = active_set((F(0), F(0)))
assert len(origin_active) == 6 and origin_value == 0
h = (F(2), F(-1))
directional = max(
    pieces[i][1][0] * h[0] + pieces[i][1][1] * h[1]
    for i in origin_active
)
assert directional == 3
lipschitz_linf = max(abs(a) + abs(b) for _, (a, b) in pieces)
assert lipschitz_linf == 2

print({
    "grid_points": 1681,
    "distinct_active_sets": len(histogram),
    "wall_or_vertex_points": tie_points,
    "segment_breakpoints": ["2/5", "1/2", "2/3"],
    "segment_cells": [segment[2][0] for segment in segments],
    "origin_directional_derivative": str(directional),
    "global_linf_lipschitz_constant": str(lipschitz_linf),
})
