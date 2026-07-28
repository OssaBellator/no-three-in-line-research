#!/usr/bin/env python3
"""Finite audit for GC2hd--GC2hh: global shortage potential and adverse bank."""

import random

rng = random.Random(20260728)
epochs = steps = closed_cycles = adverse_units = progress_units = 0

for _ in range(12000):
    epochs += 1
    t0 = rng.randint(1, 30)
    a0 = rng.randint(0, 25)
    t, a = t0, a0
    adverse_bank = rng.randint(0, 80)
    spent_adverse = 0
    gained_progress = 0

    for _j in range(rng.randint(5, 60)):
        old_t, old_a = t, a
        if rng.random() < 0.58:
            remove = rng.randint(0, min(3, t))
            add = rng.randint(0, 3)
            t -= remove
            a += add
            gained_progress += remove + add
            progress_units += remove + add
        else:
            recreate = rng.randint(0, 3)
            destroy = rng.randint(0, min(3, a))
            cost = recreate + destroy
            if spent_adverse + cost <= adverse_bank:
                t += recreate
                a -= destroy
                spent_adverse += cost
                adverse_units += cost
        steps += 1

        signed_before = old_t - old_a
        signed_after = t - a
        actual_progress = (old_t - t) + (a - old_a)
        assert signed_after == signed_before - actual_progress

    assert spent_adverse <= adverse_bank
    if (t, a) == (t0, a0):
        closed_cycles += 1
        assert gained_progress == spent_adverse

print(f"{epochs=}")
print(f"{steps=}")
print(f"{closed_cycles=}")
print(f"{adverse_units=}")
print(f"{progress_units=}")
