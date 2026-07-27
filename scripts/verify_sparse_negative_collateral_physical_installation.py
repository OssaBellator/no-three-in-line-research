#!/usr/bin/env python3
"""Finite audit for SAS5gb--SAS5gf."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import random

SEED = 20260727

NEGATIVE_TABLES = {
    (0, 1, 0, 0): "sigma",
    (0, 0, 1, 0): "tau",
}


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    for table, orientation in NEGATIVE_TABLES.items():
        chi = table[0] - table[1] - table[2] + table[3]
        assert chi == -1
        assert sum(table[1:3]) == 1
        assert table[0] == table[3] == 0
        counts[f"{orientation} table types"] += 1

    for _ in range(100000):
        square_count = rng.randint(1, 20)
        c_sigma = [rng.randint(0, 200) for _ in range(square_count)]
        c_tau = [rng.randint(0, 200) for _ in range(square_count)]
        if sum(c_sigma) + sum(c_tau) == 0:
            c_sigma[0] = 1

        selected = [max(x, y) for x, y in zip(c_sigma, c_tau)]
        creators = ["sigma" if x >= y else "tau" for x, y in zip(c_sigma, c_tau)]
        c_total = sum(c_sigma) + sum(c_tau)
        r_total = sum(selected)
        assert 2 * r_total >= c_total

        installed = sum(selected)
        assert installed == r_total

        barriers = [rng.randint(0, 400) for _ in range(square_count)]
        kappa_0 = Fraction(rng.randint(1, 20), rng.randint(1, 10))
        low = [i for i in range(square_count) if barriers[i] <= kappa_0 * selected[i]]
        high = [i for i in range(square_count) if i not in low]
        low_weight = sum(selected[i] for i in low)
        high_weight = sum(selected[i] for i in high)

        if 2 * low_weight >= r_total:
            low_cost = sum(barriers[i] for i in low)
            assert low_cost <= kappa_0 * low_weight
            counts["low cost installation branches"] += 1
            counts["installed record weight"] += low_weight
        else:
            high_cost = sum(barriers[i] for i in high)
            assert high_weight * 2 > r_total
            assert high_cost > kappa_0 * high_weight
            assert high_cost > kappa_0 * Fraction(c_total, 4)
            counts["high creator barrier branches"] += 1
            counts["creator barrier units"] += high_cost

        m = rng.randint(1, 5000)
        d_sq = rng.randint(0, 200)
        lam = Fraction(rng.randint(1, 20), rng.randint(1, 10))
        theta = Fraction(rng.randint(1, 9), 10)
        c_bound = (1 - theta) * lam * m / (4 * (d_sq + 1))
        c_exact = c_bound + Fraction(rng.randint(1, 20), 20)
        r_exact = c_exact / 2
        installed_bound = (1 - theta) * lam * m / (16 * (d_sq + 1))
        barrier_bound = kappa_0 * installed_bound
        assert r_exact / 2 > installed_bound
        assert kappa_0 * r_exact / 2 > barrier_bound

        counts["systems"] += 1
        counts["square vertices"] += square_count
        counts["selected sigma creators"] += creators.count("sigma")
        counts["selected tau creators"] += creators.count("tau")
        counts["negative collateral units"] += c_total

    print("SAS negative-collateral physical-installation audit passed")
    for key in sorted(counts):
        print(f"  {key}: {counts[key]}")


if __name__ == "__main__":
    main()
