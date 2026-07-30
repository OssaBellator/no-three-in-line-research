#!/usr/bin/env python3
from math import inf
from fractions import Fraction

BLOCKS = (
    ("P", 4, 4, (4, 0)),
    ("Q", 7, 7, (0, 7)),
    ("R", 1, 2, (1, 0)),
)
CRITICAL_LENGTHS = (4, 7)
MODULUS = 4
MAX_N = 500

# Critical semigroup and Apéry set with respect to 4.
reachable = [False] * (MAX_N + 1)
reachable[0] = True
for n in range(MAX_N + 1):
    if not reachable[n]:
        continue
    for ell in CRITICAL_LENGTHS:
        if n + ell <= MAX_N:
            reachable[n + ell] = True

apery = []
for r in range(MODULUS):
    apery.append(next(n for n in range(MAX_N + 1) if n % MODULUS == r and reachable[n]))
assert apery == [0, 21, 14, 7]
conductor = max(apery) - MODULUS + 1
assert conductor == 18
assert all(reachable[n] for n in range(conductor, MAX_N + 1))
assert not reachable[17]

# Exact minimum-cost dynamic program with one noncritical unit corrector.
best = [inf] * (MAX_N + 1)
witness = [None] * (MAX_N + 1)
best[0] = 0
witness[0] = ()
for n in range(1, MAX_N + 1):
    for name, ell, cost, _ in BLOCKS:
        if n >= ell and best[n - ell] + cost < best[n]:
            best[n] = best[n - ell] + cost
            witness[n] = witness[n - ell] + (name,)

assert best[1] == 2
for n in range(conductor, MAX_N + 1):
    assert best[n] == n
    assert "R" not in witness[n]

# Critical representations and deterministic rate-mesh certificate.
max_scaled_gap = 0
for n in range(conductor, MAX_N + 1):
    reps = []
    for b in range(n // 7 + 1):
        rem = n - 7 * b
        if rem % 4 == 0:
            a = rem // 4
            reps.append((Fraction(4 * a, n), Fraction(7 * b, n)))
    assert reps
    reps.sort()
    # Endpoints may have bounded residue offsets; adjacent l1 mesh is at most 56/n.
    if len(reps) > 1:
        gap = max(abs(reps[i + 1][0] - reps[i][0]) + abs(reps[i + 1][1] - reps[i][1])
                  for i in range(len(reps) - 1))
        max_scaled_gap = max(max_scaled_gap, n * gap)
        assert n * gap <= 56

print({
    "apery_mod_4": apery,
    "conductor": conductor,
    "lengths_checked": MAX_N,
    "eventual_cost": "F(N)=N for N>=18",
    "max_scaled_adjacent_rate_gap": max_scaled_gap,
    "status": "passed",
})
