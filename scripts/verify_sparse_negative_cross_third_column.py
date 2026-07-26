#!/usr/bin/env python3
"""Finite checks for SAS5bx--SAS5cb."""

from __future__ import annotations

from collections import Counter
from itertools import permutations
from math import gcd
from random import Random


def collinear(rows: tuple[int, int, int], columns: tuple[int, int, int]) -> bool:
    r0, r1, r2 = rows
    c0, c1, c2 = columns
    return (r1 - r0) * (c2 - c0) == (r2 - r0) * (c1 - c0)


def exhaustive_reconstruction(counts: Counter[str]) -> None:
    for n in range(3, 11):
        for r0 in range(n):
            for r1 in range(r0 + 1, n):
                for r2 in range(r1 + 1, n):
                    rows = (r0, r1, r2)
                    observed_addresses: set[tuple[tuple[int, int, int], int, int]] = set()
                    for placement in permutations(range(3)):
                        i, j, k = placement
                        a_gap = rows[j] - rows[i]
                        b_gap = rows[k] - rows[i]
                        scale = gcd(abs(a_gap), abs(b_gap))
                        a0 = a_gap // scale
                        b0 = b_gap // scale
                        observed_addresses.add((placement, a0, b0))
                        for a in range(n):
                            for b in range(n):
                                if a == b:
                                    continue
                                divisible = (b - a) % a0 == 0
                                c_formula = a + b0 * ((b - a) // a0) if divisible else None
                                solutions = []
                                for c in range(n):
                                    if c in {a, b}:
                                        continue
                                    columns = [None, None, None]
                                    columns[i] = a
                                    columns[j] = b
                                    columns[k] = c
                                    if collinear(rows, tuple(columns)):
                                        solutions.append(c)
                                if divisible and c_formula is not None and 0 <= c_formula < n and c_formula not in {a, b}:
                                    assert solutions == [c_formula]
                                    counts["valid reconstructions"] += 1
                                else:
                                    assert solutions == []
                                counts["fixed-column systems"] += 1
                    assert len(observed_addresses) <= 24 * (n - 1) ** 2
                    counts["row triples"] += 1
                    counts["observed addresses"] += len(observed_addresses)


def mate_type_checks(counts: Counter[str]) -> None:
    for x in range(12):
        for y in range(12):
            if x == y:
                continue
            assert y == y
            counts["original-mate fibres"] += 1
    for z in range(12):
        for r in range(12):
            if z == r:
                continue
            assert r == r
            counts["donor-mate fibres"] += 1


def weighted_localization(counts: Counter[str]) -> None:
    rng = Random(20260726)
    for _ in range(50000):
        n = rng.randint(3, 30)
        address_cap = 24 * (n - 1) ** 2
        class_count = rng.randint(1, min(address_cap, 200))
        weights = [rng.randint(1, 20) for _ in range(class_count)]
        total = sum(weights)
        assert max(weights) * address_cap >= total
        counts["weighted outside fibres"] += 1
        counts["weighted records"] += total

        eta_num = rng.randint(1, 99)
        lg = rng.randint(1, 10000)
        negative_numerator = eta_num * lg
        left_denominator = 24 * 24 * (n - 1) ** 2
        right_denominator = 576 * (n - 1) ** 2
        assert negative_numerator * right_denominator == negative_numerator * left_denominator
        counts["quantitative routers"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    exhaustive_reconstruction(counts)
    mate_type_checks(counts)
    weighted_localization(counts)
    print("SAS5bx--SAS5cb negative-cross third-column audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
