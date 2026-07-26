#!/usr/bin/env python3
"""Finite checks for GC2av--GC2az."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import product
from random import Random


def exhaustive_role_fibres(counts: Counter[str]) -> None:
    for n in range(2, 9):
        cells = list(range(n))
        for fixed in cells:
            alternatives = [other for other in cells if other != fixed]
            assert len(alternatives) == n - 1
            for weights in product(range(4), repeat=len(alternatives)):
                total = sum(weights)
                if total:
                    assert max(weights) * (n - 1) >= total
                    counts["weighted target-role fibres"] += 1
                    counts["weighted partner-role fibres"] += 1


def hall_import_checks(counts: Counter[str]) -> None:
    rng = Random(20260726)
    for _ in range(60000):
        n = rng.randint(2, 30)
        rank = rng.randint(1, 5)
        shared_count = rng.randint(1, 12)
        core_size = rng.randint(2, 15)
        deficiency = Fraction(rng.randint(1, 20), rng.randint(1, 8))

        # Build a role fibre at least as heavy as the GC2as lower bound.
        lower = Fraction(core_size, 2 * rank * shared_count) * deficiency
        k = rng.randint(1, n - 1)
        raw = [Fraction(rng.randint(1, 20), rng.randint(1, 8)) for _ in range(k)]
        scale = max(Fraction(1), lower / sum(raw))
        weights = [value * scale for value in raw]
        total = sum(weights)
        heavy = max(weights)

        assert k <= n - 1
        assert total >= lower
        assert heavy >= total / (n - 1)
        assert heavy >= lower / (n - 1)
        counts["Hall-import role fibres"] += 1


def pay_ratio_checks(counts: Counter[str]) -> None:
    rng = Random(911)
    for _ in range(100000):
        value = Fraction(rng.randint(1, 100), rng.randint(1, 20))
        capacity = Fraction(rng.randint(0, 50), rng.randint(1, 20))
        theta = Fraction(rng.randint(1, 20), rng.randint(1, 10))
        if theta < 1:
            theta = Fraction(1)

        if capacity == 0:
            assert value > 0
            counts["zero-capacity incidences"] += 1
        elif value <= theta * capacity:
            payment = value / theta
            assert 0 < payment <= capacity
            counts["normalized heavy-incidence payments"] += 1
        else:
            assert value / capacity > theta
            counts["high-ratio heavy incidences"] += 1


def unified_router_checks(counts: Counter[str]) -> None:
    rng = Random(314159)
    for _ in range(50000):
        total_excess = Fraction(rng.randint(1, 100), rng.randint(1, 10))
        theta = rng.randint(1, 10)
        moderate = Fraction(rng.randint(0, 100), 100) * total_excess
        heavy = total_excess - moderate

        if moderate >= total_excess / 2:
            payment = moderate / theta
            assert payment >= total_excess / (2 * theta)
            counts["direct moderate routes"] += 1
        else:
            assert heavy > total_excess / 2
            counts["direct heavy-ratio routes"] += 1

        # Independently stress the Hall continuation language.
        n = rng.randint(2, 20)
        rank = rng.randint(1, 4)
        shared = rng.randint(1, 10)
        core = rng.randint(2, 12)
        deficiency = Fraction(rng.randint(1, 30), rng.randint(1, 10))
        incidence = Fraction(core, 2 * rank * shared * (n - 1)) * deficiency
        capacity = Fraction(rng.randint(0, 30), rng.randint(1, 10))
        if capacity == 0:
            counts["Hall zero-capacity routes"] += 1
        elif incidence <= theta * capacity:
            assert incidence / theta <= capacity
            counts["Hall payment routes"] += 1
        else:
            assert incidence / capacity > theta
            counts["Hall high-ratio routes"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    exhaustive_role_fibres(counts)
    hall_import_checks(counts)
    pay_ratio_checks(counts)
    unified_router_checks(counts)
    print("GC2av--GC2az heavy Hall incidence audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
