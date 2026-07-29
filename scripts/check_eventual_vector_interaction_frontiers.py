#!/usr/bin/env python3
from collections import defaultdict

# Macro blocks: (name, length, work, secondary vector).
BLOCKS = (
    ("A", 1, 3, (0, 4)),
    ("B", 1, 3, (4, 0)),
    ("D", 2, 5, (1, 5)),
    ("E", 2, 5, (5, 1)),
    ("P", 3, 6, (3, 3)),
)
MAX_N = 180

# Keep only minimum-work plans, then Pareto-prune their secondary vectors.
frontiers = [set() for _ in range(MAX_N + 1)]
frontiers[0] = {(0, 0, 0, "")}
for n in range(1, MAX_N + 1):
    candidates = []
    for name, length, work, vec in BLOCKS:
        if n < length:
            continue
        for prev_work, x, y, word in frontiers[n - length]:
            candidates.append((prev_work + work, x + vec[0], y + vec[1], word + name))
    min_work = min(c[0] for c in candidates)
    same = [c for c in candidates if c[0] == min_work]
    keep = []
    for c in same:
        if any(d[1] <= c[1] and d[2] <= c[2] and (d[1], d[2]) != (c[1], c[2]) for d in same):
            continue
        keep.append(c)
    # Remove duplicate vectors, retaining a lexicographically least witness.
    by_vec = {}
    for c in keep:
        key = (c[1], c[2])
        if key not in by_vec or c[3] < by_vec[key][3]:
            by_vec[key] = c
    frontiers[n] = set(by_vec.values())

for n in range(1, MAX_N + 1):
    q, r = divmod(n, 3)
    expected_work = 6 * q + (0 if r == 0 else 3 if r == 1 else 5)
    assert {c[0] for c in frontiers[n]} == {expected_work}
    base = (3 * q, 3 * q)
    vecs = {(c[1], c[2]) for c in frontiers[n]}
    if r == 0:
        expected = {base}
    elif r == 1:
        expected = {(base[0], base[1] + 4), (base[0] + 4, base[1])}
    else:
        expected = {(base[0] + 1, base[1] + 5), (base[0] + 5, base[1] + 1)}
    assert vecs == expected, (n, vecs, expected)

print({
    "lengths_checked": MAX_N,
    "period": 3,
    "residue_frontier_sizes": {0: 1, 1: 2, 2: 2},
    "minimum_work_formula": "6*floor(N/3)+{0,3,5}[N mod 3]",
    "status": "passed",
})
