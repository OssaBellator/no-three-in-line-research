#!/usr/bin/env python3

BLOCKS = (
    ("P", 2, 2, (2, 0)),
    ("Q", 2, 2, (0, 2)),
    ("R", 1, 2, (1, 1)),
)
MAX_N = 200

states = [set() for _ in range(MAX_N + 1)]
states[0] = {(0, 0, 0, "")}
for n in range(1, MAX_N + 1):
    candidates = []
    for name, length, work, vec in BLOCKS:
        if n < length:
            continue
        for old_work, x, y, word in states[n - length]:
            candidates.append((old_work + work, x + vec[0], y + vec[1], word + name))
    best_work = min(c[0] for c in candidates)
    same = [c for c in candidates if c[0] == best_work]
    by_vec = {}
    for c in same:
        key = (c[1], c[2])
        if key not in by_vec or c[3] < by_vec[key][3]:
            by_vec[key] = c
    states[n] = set(by_vec.values())

for n in range(1, MAX_N + 1):
    k, r = divmod(n, 2)
    expected_work = n if r == 0 else n + 1
    assert {c[0] for c in states[n]} == {expected_work}
    vecs = {(c[1], c[2]) for c in states[n]}
    if r == 0:
        expected = {(2 * i, 2 * (k - i)) for i in range(k + 1)}
    else:
        expected = {(2 * i + 1, 2 * (k - i) + 1) for i in range(k + 1)}
    assert vecs == expected, (n, vecs, expected)
    assert len(vecs) == k + 1

for n in range(2, MAX_N + 1):
    vecs = sorted((x / n, y / n) for _, x, y, _ in states[n])
    target_sum = 1 if n % 2 == 0 else 1 + 1 / n
    assert all(abs((x + y) - target_sum) < 1e-12 for x, y in vecs)
    if len(vecs) > 1:
        max_mesh = max(abs(vecs[i + 1][0] - vecs[i][0]) for i in range(len(vecs) - 1))
        assert max_mesh <= 2 / n + 1e-12

print({
    "lengths_checked": MAX_N,
    "critical_blocks": 2,
    "minimum_work": "N for even N; N+1 for odd N",
    "frontier_size": "floor(N/2)+1",
    "limiting_polytope": "conv((1,0),(0,1))",
    "status": "passed",
})
