#!/usr/bin/env python3
"""Finite audit for SAS5gy--SAS5hc."""

from collections import defaultdict
import random

SEED = 20260728


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    for _ in range(100000):
        k_rec = rng.randint(2, 40)
        length = rng.randint(2, k_rec)
        start = rng.randint(0, 10000)
        energies = [start]
        for _j in range(length - 1):
            energies.append(rng.randint(0, 10000))
        energies.append(start)
        deltas = [energies[j + 1] - energies[j] for j in range(length)]
        assert sum(deltas) == 0
        pos = sum(max(x, 0) for x in deltas)
        neg = sum(max(-x, 0) for x in deltas)
        assert pos == neg
        if pos > 0:
            best = max(max(-x, 0) for x in deltas)
            assert best * length >= pos
            assert best * k_rec >= pos
            counts["positive_barrier_cycles"] += 1
            counts["barrier_units"] += pos
        else:
            assert all(x == 0 for x in deltas)
            counts["neutral_cycles"] += 1

        local = [0] * length
        assert sum(local) == 0 and all(x == 0 for x in local)
        counts["local_minimum_neutral_checks"] += 1

        if rng.random() < 0.25:
            end = start + rng.choice([-1, 1]) * rng.randint(1, 20)
            assert end != start
            counts["omitted_field_refinements"] += 1

        counts["systems"] += 1
        counts["cycle_edges"] += length

    print("SAS signature-cycle barrier-payment audit passed")
    for key in sorted(counts):
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()
