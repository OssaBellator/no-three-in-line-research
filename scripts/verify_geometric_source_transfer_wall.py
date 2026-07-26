#!/usr/bin/env python3
"""Finite checks for GC2k--GC2n."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, product

Point = tuple[int, int]


def collinear(a: Point, b: Point, c: Point) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1])


def verify_cross_cell_exclusion(counts: Counter[str]) -> None:
    for rb, ru, cb, cu in product(range(5), repeat=4):
        if rb == ru or cb == cu:
            continue
        b = (rb, cb)
        u = (ru, cu)
        for rho in ((rb, cu), (ru, cb)):
            for a, c in combinations(
                [p for p in product(range(5), repeat=2) if p not in {b, u, rho}], 2
            ):
                if a[0] == c[0] or a[1] == c[1] or not collinear(a, c, rho):
                    continue
                assert not collinear(a, c, b)
                assert not collinear(a, c, u)
                counts["nonaxis witnesses"] += 1


def verify_explicit_wall(counts: Counter[str]) -> None:
    b = (0, 0)
    u = (1, 1)
    x = (0, 1)
    a = (2, 5)
    c = (3, 7)
    current = (b, u, a, c)
    assert all(not collinear(*triple) for triple in combinations(current, 3))
    assert collinear(x, a, c)
    counts["source-free examples"] += 1


def verify_congestion_scaling(counts: Counter[str]) -> None:
    for factor_count in range(1, 5):
        for witness_count in range(1, 7):
            for source_map in product(range(factor_count), repeat=witness_count):
                for weights in product((0, 1, 2), repeat=witness_count):
                    if sum(weights) == 0:
                        continue
                    for capacities in product((1, 2, 3), repeat=factor_count):
                        loads = [
                            sum(weights[w] for w in range(witness_count) if source_map[w] == q)
                            for q in range(factor_count)
                        ]
                        for congestion in range(1, 5):
                            if any(loads[q] > congestion * capacities[q] for q in range(factor_count)):
                                continue
                            payments = [Fraction(weight, congestion) for weight in weights]
                            for q in range(factor_count):
                                paid = sum(
                                    payments[w]
                                    for w in range(witness_count)
                                    if source_map[w] == q
                                )
                                assert paid <= capacities[q]
                            assert sum(payments) == Fraction(sum(weights), congestion)
                            counts["transfer systems"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_cross_cell_exclusion(counts)
    verify_explicit_wall(counts)
    verify_congestion_scaling(counts)
    print("GC2k--GC2n source-transfer audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
