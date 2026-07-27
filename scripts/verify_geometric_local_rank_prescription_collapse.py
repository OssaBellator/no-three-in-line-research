#!/usr/bin/env python3
"""Finite audit for GC2eb--GC2ef."""

import math
import random
from collections import defaultdict

SEED = 20260727


def falling(t, r):
    value = 1
    for i in range(r):
        value *= t - i
    return value


def completion_stock(n, r):
    if r == 1:
        return math.comb(n * n, 2)
    if r == 2:
        return n * n
    return 1


def at_least(value, target):
    return value >= target or math.isclose(
        value,
        target,
        rel_tol=1e-12,
        abs_tol=1e-9,
    )


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    for _ in range(100000):
        n = rng.randint(3, 60)
        t = rng.randint(7, 40)
        r = rng.randint(1, 3)
        source = rng.uniform(1.0, 100000.0)
        fixed = rng.uniform(0.0, 0.999 * source)
        prescriptions = falling(t, r)
        threshold = (source - fixed) * prescriptions / 384.0
        total = threshold * (1.0 + 9.0 * rng.random())

        used = min(prescriptions, rng.randint(1, min(prescriptions, 300)))
        raw = [rng.random() for _ in range(used)]
        scale = total / sum(raw)
        weights = [value * scale for value in raw]
        heavy_prescription = max(weights)

        assert at_least(heavy_prescription, total / prescriptions)
        assert at_least(total / prescriptions, (source - fixed) / 384.0)

        stock = completion_stock(n, r)
        used_completions = min(stock, rng.randint(1, min(stock, 300)))
        raw_completion = [rng.random() for _ in range(used_completions)]
        completion_scale = heavy_prescription / sum(raw_completion)
        completion_weights = [value * completion_scale for value in raw_completion]
        exact_weight = max(completion_weights)

        assert at_least(exact_weight, heavy_prescription / stock)
        assert at_least(exact_weight, (source - fixed) / (384.0 * stock))

        theta = (source - fixed) / source
        assert at_least(exact_weight, theta * source / (384.0 * stock))

        counts[f"rank_{r}_systems"] += 1
        counts["prescriptions"] += used
        counts["completions"] += used_completions

    print("GC local rank prescription-collapse audit passed")
    print(f"  rank-one systems: {counts['rank_1_systems']}")
    print(f"  rank-two systems: {counts['rank_2_systems']}")
    print(f"  rank-three systems: {counts['rank_3_systems']}")
    print(f"  sampled prescription classes: {counts['prescriptions']}")
    print(f"  sampled exact completions: {counts['completions']}")


if __name__ == "__main__":
    main()
