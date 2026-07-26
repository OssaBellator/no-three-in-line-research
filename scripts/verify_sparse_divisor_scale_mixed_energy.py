#!/usr/bin/env python3
"""Finite checks for SAS5bn--SAS5br."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import product
from random import Random


IndicatorPattern = tuple[int, int, int, int]


def mixed_curvature(pattern: IndicatorPattern) -> int:
    base, omega, tau, combined = pattern
    return combined - omega - tau + base


def exhaustive_indicator_checks(counts: Counter[str]) -> None:
    for pattern in product((0, 1), repeat=4):
        delta_omega = pattern[1] - pattern[0]
        delta_tau = pattern[2] - pattern[0]
        delta_comb = pattern[3] - pattern[0]
        curvature = mixed_curvature(pattern)
        assert delta_comb == delta_omega + delta_tau + curvature
        assert -2 <= curvature <= 2
        counts["four-state indicator patterns"] += 1

    selected = (0, 0, 0, 1)
    assert mixed_curvature(selected) == 1
    counts["selected scale patterns"] += 1


def random_weighted_systems(counts: Counter[str]) -> None:
    rng = Random(20260726)
    etas = (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4))
    accepted = 0
    attempts = 0
    while accepted < 80000 and attempts < 800000:
        attempts += 1
        selected_weights = [rng.randint(1, 12) for _ in range(rng.randint(1, 8))]
        scale_weight = sum(selected_weights)

        other: list[tuple[int, IndicatorPattern, int | None]] = []
        for _ in range(rng.randint(0, 20)):
            weight = rng.randint(1, 12)
            pattern = tuple(rng.randint(0, 1) for _ in range(4))
            curvature = mixed_curvature(pattern)
            role = rng.randrange(4) if curvature < 0 else None
            other.append((weight, pattern, role))

        delta_omega = sum(weight * (pattern[1] - pattern[0]) for weight, pattern, _ in other)
        delta_tau = sum(weight * (pattern[2] - pattern[0]) for weight, pattern, _ in other)
        # Selected scale records contribute zero to both individual swaps.
        if delta_omega < 0 or delta_tau < 0:
            continue

        c_minus = sum(
            weight * max(0, -mixed_curvature(pattern))
            for weight, pattern, _ in other
        )
        c_plus = sum(
            weight * max(0, mixed_curvature(pattern))
            for weight, pattern, _ in other
        )
        delta_comb = delta_omega + delta_tau + scale_weight + c_plus - c_minus

        direct_delta_comb = sum(
            weight * (pattern[3] - pattern[0]) for weight, pattern, _ in other
        ) + scale_weight
        assert delta_comb == direct_delta_comb

        for eta in etas:
            assert c_minus >= eta * scale_weight or delta_comb > (1 - eta) * scale_weight

        if delta_comb < 0:
            assert c_minus > scale_weight + delta_omega + delta_tau + c_plus
            assert c_minus > scale_weight
            counts["improving composed systems"] += 1

        role_weight = [0, 0, 0, 0]
        for weight, pattern, role in other:
            curvature = mixed_curvature(pattern)
            if curvature < 0:
                assert role is not None
                role_weight[role] += weight * (-curvature)
        assert sum(role_weight) == c_minus
        if c_minus:
            assert max(role_weight) * 4 >= c_minus
            counts["negative-curvature endpoint fibres"] += 1

        counts["local-minimum weighted systems"] += 1
        accepted += 1

    assert accepted == 80000


def support_localization_checks(counts: Counter[str]) -> None:
    rng = Random(911)
    omega = {0, 1}
    tau = {2, 3}
    for _ in range(50000):
        scope = set(rng.sample(range(8), rng.randint(1, 3)))
        pattern = tuple(rng.randint(0, 1) for _ in range(4))
        curvature = mixed_curvature(pattern)
        if not (scope & omega) or not (scope & tau):
            # A real constraint missing one swap has zero curvature; enforce that model.
            pattern = (pattern[0], pattern[0], pattern[2], pattern[2]) if not (scope & omega) else (
                pattern[0], pattern[1], pattern[0], pattern[1]
            )
            curvature = mixed_curvature(pattern)
            assert curvature == 0
        else:
            pair_count = len(scope & omega) * len(scope & tau)
            assert 1 <= pair_count <= 4
        counts["scope-support systems"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    exhaustive_indicator_checks(counts)
    random_weighted_systems(counts)
    support_localization_checks(counts)
    print("SAS5bn--SAS5br mixed divisor-scale energy audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
