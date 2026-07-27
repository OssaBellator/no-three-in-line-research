#!/usr/bin/env python3
"""Finite audit for SAS5dr--SAS5dv.

Checks arithmetic localization of batched original and donor repair words,
extension of the cross third-column reconstruction to positive curvature, and
all combined constants from the multi-peel output router.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import comb, gcd
import random


def primitive_third_column(a: int, b: int, A: int, B: int) -> int | None:
    g = gcd(abs(A), abs(B))
    A0, B0 = A // g, B // g
    if (b - a) % A0:
        return None
    return a + B0 * ((b - a) // A0)


def max_bucket(weights: list[int], stock: int) -> int:
    buckets = [0] * stock
    for i, w in enumerate(weights):
        buckets[i % stock] += w
    return max(buckets, default=0)


def main() -> None:
    rng = random.Random(20260727)
    stats: Counter[str] = Counter()

    for N in range(5, 15):
        for a in range(N):
            for b in range(N):
                if a == b:
                    continue
                for r1 in range(N):
                    for r2 in range(N):
                        for r3 in range(N):
                            if len({r1, r2, r3}) < 3:
                                continue
                            A = r2 - r1
                            B = r3 - r1
                            c = primitive_third_column(a, b, A, B)
                            if c is not None:
                                assert A * (c - a) == B * (b - a)
                            stats["third_column_systems"] += 1

    for _ in range(50_000):
        N = rng.randint(5, 30)
        K0 = 24 * comb(N, 3) * (N - 2) ** 2
        omega_peel = rng.randint(1, 10**7)

        W_orig = Fraction(omega_peel, 192 * K0)
        double_orig = W_orig / (N * (N - 1))
        singleton_orig = W_orig / (4 * N * (N - 1) ** 3)
        assert double_orig == Fraction(
            omega_peel, 192 * K0 * N * (N - 1)
        )
        assert singleton_orig == Fraction(
            omega_peel, 768 * K0 * N * (N - 1) ** 3
        )

        M = max(1, (N - 2) // 2)
        W_donor = Fraction(omega_peel, 6912)
        selected_donor = W_donor / M
        donor_double = selected_donor / (N * (N - 1))
        donor_singleton = selected_donor / (4 * N * (N - 1) ** 3)
        assert donor_double >= Fraction(
            omega_peel, 3456 * (N - 2) * N * (N - 1)
        )
        assert donor_singleton >= Fraction(
            omega_peel, 13824 * (N - 2) * N * (N - 1) ** 3
        )

        W_pos = Fraction(omega_peel, 18432)
        fixed_pair = W_pos / (N - 2)
        positive_mate = fixed_pair
        positive_outside = fixed_pair / (24 * (N - 1) ** 2)
        assert positive_mate == Fraction(
            omega_peel, 18432 * (N - 2)
        )
        assert positive_outside == Fraction(
            omega_peel, 442368 * (N - 2) * (N - 1) ** 2
        )

        designated = Fraction(omega_peel, 16)
        assert designated > 0
        stats["constant_systems"] += 1

    for _ in range(30_000):
        N = rng.randint(5, 20)
        M = max(1, (N - 2) // 2)
        donors = rng.randint(1, M)
        donor_masses = [rng.randint(1, 500) for _ in range(donors)]
        total = sum(donor_masses)
        best = max(donor_masses)
        assert best * M >= total

        double_stock = N * (N - 1)
        singleton_stock = 4 * N * (N - 1) ** 3
        double_parts = [rng.randint(0, 20) for _ in range(rng.randint(1, 100))]
        if sum(double_parts):
            assert max_bucket(double_parts, double_stock) * double_stock >= sum(
                double_parts
            )
        singleton_parts = [
            rng.randint(0, 20) for _ in range(rng.randint(1, 100))
        ]
        if sum(singleton_parts):
            assert (
                max_bucket(singleton_parts, singleton_stock) * singleton_stock
                >= sum(singleton_parts)
            )

        partner_count = rng.randint(1, N - 2)
        partner_masses = [rng.randint(1, 500) for _ in range(partner_count)]
        pos_total = sum(partner_masses)
        pos_best = max(partner_masses)
        assert pos_best * (N - 2) >= pos_total

        stats["weighted_localizations"] += 1
        stats["donor_pairs"] += donors
        stats["positive_partner_pairs"] += partner_count

    print("SAS batched arithmetic output audit passed")
    for key in sorted(stats):
        print(f"{key}: {stats[key]}")


if __name__ == "__main__":
    main()
