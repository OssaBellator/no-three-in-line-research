#!/usr/bin/env python3
from fractions import Fraction

BLOCKS = (
    ("P", 1, 1, (1, 0)),
    ("Q", 2, 2, (0, 2)),
    ("R", 1, 2, (0, 1)),
)
MAX_N = 300

states = [dict() for _ in range(MAX_N + 1)]
states[0][(0, 0)] = (0, "")
for n in range(1, MAX_N + 1):
    best = None
    candidates = {}
    for name, length, work, vec in BLOCKS:
        if n < length:
            continue
        for old_vec, (old_work, word) in states[n - length].items():
            new_work = old_work + work
            new_vec = (old_vec[0] + vec[0], old_vec[1] + vec[1])
            if best is None or new_work < best:
                best = new_work
                candidates = {new_vec: word + name}
            elif new_work == best:
                if new_vec not in candidates or word + name < candidates[new_vec]:
                    candidates[new_vec] = word + name
    states[n] = {vec: (best, word) for vec, word in candidates.items()}

for n in range(1, MAX_N + 1):
    assert {work for work, _ in states[n].values()} == {n}
    expected = {(n - 2 * b, 2 * b) for b in range(n // 2 + 1)}
    assert set(states[n]) == expected
    assert len(expected) == n // 2 + 1
    assert all(x + y == n for x, y in expected)
    for x in range(n + 1):
        y = n - x
        if y % 2 == 0:
            assert (x, y) in expected
    xs = sorted(Fraction(x, n) for x, _ in expected)
    cover = max(2 * xs[0], 2 * (1 - xs[-1]))
    for left, right in zip(xs, xs[1:]):
        cover = max(cover, right - left)
    assert cover <= Fraction(2, n)

print({
    "lengths_checked": MAX_N,
    "critical_lengths": (1, 2),
    "hilbert_basis": ((1, 1, 0), (2, 0, 2)),
    "minimum_work": "N",
    "frontier_count": "floor(N/2)+1",
    "frontier_generating_function": "1/((1-z)(1-z^2))",
    "normalized_mesh_bound": "2/N",
    "status": "passed",
})
