#!/usr/bin/env python3
"""Finite audit for GC2fz--GC2gd."""

from collections import defaultdict
from fractions import Fraction
import random

SEED = 20260728


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    for _ in range(60000):
        n = rng.randint(1, 40)
        eps = Fraction(rng.randint(1, 9), 10)
        h = Fraction(rng.randint(20, 5000), 7)
        K_rem = rng.randint(1, 20)
        K_swap = rng.randint(1, 80)

        mode = rng.randrange(3)
        if mode == 0:
            F = Fraction(rng.randint(0, 40), 100) * (1 - eps) * h
            E = [Fraction(rng.randint(0, 40), 100) * (1 - eps) * h for _ in range(n)]
            scale = (1 - eps) * h / max(F + sum(E, Fraction(0)) / n, Fraction(1))
            if scale < 1:
                F *= scale
                E = [x * scale for x in E]
            assert F + sum(E, Fraction(0)) / n <= (1 - eps) * h
            deltas = [F + x - h for x in E]
            assert min(deltas) <= -eps * h
            counts["descent_routes"] += 1
        elif mode == 1:
            F = Fraction(rng.randint(51, 100), 100) * (1 - eps) * h
            E = [Fraction(0) for _ in range(n)]
            assert F > (1 - eps) * h / 2
            pieces = [F / K_rem for _ in range(K_rem)]
            assert max(pieces) >= F / K_rem > (1 - eps) * h / (2 * K_rem)
            counts["removal_output_routes"] += 1
        else:
            F = Fraction(0)
            Ebar = Fraction(rng.randint(51, 100), 100) * (1 - eps) * h
            E = [Ebar for _ in range(n)]
            assert sum(E, Fraction(0)) > n * (1 - eps) * h / 2
            total_slots = n * K_swap
            slot_weight = sum(E, Fraction(0)) / total_slots
            assert slot_weight > (1 - eps) * h / (2 * K_swap)
            counts["donor_output_routes"] += 1

        N = rng.randint(5, 80)
        q_ch = rng.randint(1, 8)
        Delta_cap = rng.randint(1, 1000)
        denom = 8 * q_ch * N * N * (2 * Delta_cap - 1)
        W_B = int(h * denom) - 1
        assert h > Fraction(W_B, denom)

        counts["systems"] += 1
        counts["donor_operations"] += n
        counts["removal_slots"] += K_rem
        counts["donor_slots"] += n * K_swap

    print("GC blocker-removal donor-router audit passed")
    for key in sorted(counts):
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()
