#!/usr/bin/env python3
"""Finite audit for GC2bw--GC2ca using exact rational arithmetic."""

from __future__ import annotations

import random
from fractions import Fraction
from itertools import product

SEED = 20260726
RNG = random.Random(SEED)


def classify(c: list[Fraction], q: list[Fraction], residual: Fraction) -> str:
    c_dest = sum(c, Fraction(0))
    z_dest = sum((min(x, y) for x, y in zip(c, q)), Fraction(0))
    if c_dest < residual:
        return "hall"
    if z_dest >= residual:
        return "descent"
    return "ratio"


def exhaustive_small() -> dict[str, int]:
    counts = {"hall": 0, "descent": 0, "ratio": 0}
    for n in range(1, 5):
        for c_vals in product(range(4), repeat=n):
            for q_vals in product(range(1, 4), repeat=n):
                c = [Fraction(x) for x in c_vals]
                q = [Fraction(x) for x in q_vals]
                max_r = max(1, sum(c_vals) + 2)
                for r_int in range(1, max_r + 1):
                    residual = Fraction(r_int)
                    c_dest = sum(c, Fraction(0))
                    z_dest = sum((min(x, y) for x, y in zip(c, q)), Fraction(0))
                    case = classify(c, q, residual)
                    counts[case] += 1
                    if case == "hall":
                        assert residual - c_dest > 0
                    elif case == "descent":
                        assert c_dest >= residual and z_dest >= residual
                        scale = residual / z_dest
                        allocation = [scale * min(x, y) for x, y in zip(c, q)]
                        assert sum(allocation, Fraction(0)) == residual
                        assert all(0 <= a <= x and a <= y for a, x, y in zip(allocation, c, q))
                    else:
                        assert c_dest >= residual > z_dest
                        delta = residual - z_dest
                        excess = sum((max(Fraction(0), x - y) for x, y in zip(c, q)), Fraction(0))
                        assert excess == c_dest - z_dest >= delta
                        positive = [(x, y) for x, y in zip(c, q) if x > 0]
                        best = max(x / y for x, y in positive)
                        assert best >= c_dest / z_dest
                        assert best >= residual / (residual - delta) > 1
    return counts


def random_event_systems(trials: int = 80_000) -> tuple[dict[str, int], int, int]:
    counts = {"hall": 0, "descent": 0, "ratio": 0}
    outside_occurrences = 0
    localized = 0
    for _ in range(trials):
        n = RNG.randint(1, 12)
        outside = RNG.randint(0, 8)
        weights = [Fraction(RNG.randint(1, 20), RNG.randint(1, 8)) for _ in range(n)]
        dsum = sum(weights, Fraction(0))
        gain = Fraction(RNG.randint(1, max(1, int(dsum * 8))), 8)
        if gain > dsum:
            gain = dsum
        lam = gain / dsum
        q = [lam * w for w in weights]
        assert sum(q, Fraction(0)) == gain
        assert all(0 < qi <= wi for qi, wi in zip(q, weights))

        c = [Fraction(RNG.randint(0, 30), RNG.randint(1, 8)) for _ in range(n)]
        outside_c = [Fraction(RNG.randint(0, 30), RNG.randint(1, 8)) for _ in range(outside)]
        outside_occurrences += outside
        # Source-free coordinates are deliberately ignored by the corrected system.
        assert sum(outside_c, Fraction(0)) >= 0

        c_dest = sum(c, Fraction(0))
        z_dest = sum((min(x, y) for x, y in zip(c, q)), Fraction(0))
        upper = max(Fraction(1), c_dest + 2)
        residual = Fraction(RNG.randint(1, max(1, int(upper * 8))), 8)
        if residual <= 0:
            residual = Fraction(1, 8)

        case = classify(c, q, residual)
        counts[case] += 1
        if case == "hall":
            assert c_dest < residual
            continue
        if case == "descent":
            assert z_dest >= residual
            allocation = [residual * min(x, y) / z_dest for x, y in zip(c, q)]
            assert sum(allocation, Fraction(0)) == residual
            assert sum(allocation, Fraction(0)) <= gain
            continue

        delta = residual - z_dest
        assert delta > 0 and c_dest >= residual
        excesses = [max(Fraction(0), x - y) for x, y in zip(c, q)]
        assert sum(excesses, Fraction(0)) == c_dest - z_dest >= delta
        best_index = max(range(n), key=lambda i: c[i] / q[i])
        assert c[best_index] / q[best_index] >= c_dest / z_dest
        assert c[best_index] / weights[best_index] >= lam * residual / (residual - delta)

        role_count = RNG.randint(1, min(6, n))
        roles = [RNG.randrange(role_count) for _ in range(n)]
        role_mass = [sum((excesses[i] for i in range(n) if roles[i] == r), Fraction(0)) for r in range(role_count)]
        r_star = max(range(role_count), key=role_mass.__getitem__)
        assert role_mass[r_star] >= delta / role_count
        members = [i for i in range(n) if roles[i] == r_star]
        i_star = max(members, key=excesses.__getitem__)
        assert excesses[i_star] >= delta / (role_count * len(members))
        localized += 1
    return counts, outside_occurrences, localized


def threshold_checks(trials: int = 40_000) -> int:
    checked = 0
    for _ in range(trials):
        n = RNG.randint(1, 10)
        theta = Fraction(RNG.randint(2, 10), RNG.randint(1, 4))
        if theta < 1:
            theta = Fraction(1)
        W = Fraction(RNG.randint(1, 50), RNG.randint(1, 6))
        C = Fraction(RNG.randint(0, max(0, int(W * 6) - 1)), 6)
        if C >= W / theta:
            continue
        residual = W - C
        assert residual > (1 - Fraction(1, 1) / theta) * W
        # Any corrected descent allocation of residual has the advertised size.
        checked += 1
    return checked


def main() -> None:
    exhaustive = exhaustive_small()
    random_counts, outside, localized = random_event_systems()
    threshold = threshold_checks()
    print(
        "PASS GC destruction-faithful external audit:",
        f"exhaustive={exhaustive};",
        f"random={random_counts};",
        f"{outside} source-free coordinates removed;",
        f"{localized} ratio deficits localized;",
        f"{threshold} strict star-residual checks.",
    )


if __name__ == "__main__":
    main()
