#!/usr/bin/env python3
from fractions import Fraction

BLOCKS = (
    ("P", 2, 2, (2, 0)),
    ("Q", 3, 3, (0, 3)),
    ("R", 1, 2, (1, 0)),
)
MAX_N = 500

states = [dict() for _ in range(MAX_N + 1)]
states[0][(0, 0)] = (0, "")
for n in range(1, MAX_N + 1):
    best = None
    candidates = {}
    for name, length, cost, vec in BLOCKS:
        if n < length:
            continue
        for old_vec, (old_cost, word) in states[n - length].items():
            new_cost = old_cost + cost
            new_vec = (old_vec[0] + vec[0], old_vec[1] + vec[1])
            if best is None or new_cost < best:
                best = new_cost
                candidates = {new_vec: word + name}
            elif new_cost == best:
                if new_vec not in candidates or word + name < candidates[new_vec]:
                    candidates[new_vec] = word + name
    assert best is not None
    states[n] = {vec: (best, word) for vec, word in candidates.items()}

assert {cost for cost, _ in states[1].values()} == {2}
for n in range(2, MAX_N + 1):
    assert {cost for cost, _ in states[n].values()} == {n}
    expected = set()
    for b in range(n // 3 + 1):
        remainder = n - 3 * b
        if remainder >= 0 and remainder % 2 == 0:
            a = remainder // 2
            expected.add((2 * a, 3 * b))
    assert set(states[n]) == expected, (n, set(states[n]), expected)
    assert all(x + y == n for x, y in expected)

    xs = sorted(Fraction(x, n) for x, _ in expected)
    cover = max(2 * xs[0], 2 * (1 - xs[-1]))
    for left, right in zip(xs, xs[1:]):
        cover = max(cover, right - left)
    assert cover <= Fraction(8, n)

print({
    "lengths_checked": MAX_N,
    "critical_lengths": (2, 3),
    "conductor": 2,
    "minimum_cost": "2 at N=1; N for N>=2",
    "rate_polytope": "conv((1,0),(0,1))",
    "l1_mesh_bound": "8/N",
    "status": "passed",
})
