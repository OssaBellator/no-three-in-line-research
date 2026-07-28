#!/usr/bin/env python3
"""Finite audit for RI5bw--RI5ca: symmetric/antisymmetric two-lift ledgers."""

import random

rng = random.Random(20260728)
fibres = swaps = cancellation_checks = reset_checks = 0

for _ in range(120000):
    fibres += 1
    wu = rng.randint(-100, 100)
    wv = rng.randint(-100, 100)
    sym2 = wu + wv
    anti = wu - wv

    wu2, wv2 = wv, wu
    assert wu2 + wv2 == sym2
    assert wu2 - wv2 == -anti
    swaps += 1

    assert anti + (wu2 - wv2) == 0
    cancellation_checks += 1

    owner_u = rng.randrange(6)
    owner_v = rng.randrange(6)
    coh = rng.randrange(5)
    owner_u2, owner_v2 = owner_v, owner_u
    coh2 = coh
    immutable = (owner_u2, owner_v2, coh2) == (owner_v, owner_u, coh)
    assert immutable
    if rng.random() < 0.2:
        coh2 = (coh + 1) % 5
        assert coh2 != coh
        reset_checks += 1

print(f"{fibres=}")
print(f"{swaps=}")
print(f"{cancellation_checks=}")
print(f"{reset_checks=}")
