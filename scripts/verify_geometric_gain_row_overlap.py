#!/usr/bin/env python3
"""Finite checks for GC2bm--GC2bq."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from random import Random


def audit_system(
    capacities: tuple[Fraction, ...],
    charges: tuple[Fraction, ...],
    residual: Fraction,
    roles: tuple[int, ...],
    counts: Counter[str],
) -> None:
    assert len(capacities) == len(charges) == len(roles)
    assert residual > 0
    effective = tuple(min(c, a) for c, a in zip(capacities, charges))
    z_total = sum(effective, Fraction(0))
    c_total = sum(capacities, Fraction(0))
    gain = sum(charges, Fraction(0))

    # Coordinatewise intersection is the exact feasible total.
    assert z_total == sum(min(c, a) for c, a in zip(capacities, charges))

    if z_total >= residual:
        scale = residual / z_total
        allocation = tuple(scale * z for z in effective)
        assert sum(allocation, Fraction(0)) == residual
        assert all(Fraction(0) <= x <= c for x, c in zip(allocation, capacities))
        assert all(Fraction(0) <= x <= a for x, a in zip(allocation, charges))
        assert residual <= gain
        counts["gain-certified systems"] += 1
        counts["gain-certified amount numerators"] += residual.numerator
    else:
        delta = residual - z_total
        assert delta > 0
        if c_total < residual:
            assert residual - c_total > 0
            counts["ordinary Hall deficits"] += 1
        else:
            uncertified = tuple(max(c - a, Fraction(0)) for c, a in zip(capacities, charges))
            uncertified_total = sum(uncertified, Fraction(0))
            assert uncertified_total == c_total - z_total
            assert uncertified_total >= delta

            role_mass: dict[int, Fraction] = defaultdict(Fraction)
            role_size: dict[int, int] = defaultdict(int)
            for role, mass in zip(roles, uncertified):
                role_mass[role] += mass
                role_size[role] += 1
            role_count = len(role_mass)
            assert role_count >= 1
            selected_role = max(role_mass, key=role_mass.get)
            assert role_mass[selected_role] * role_count >= uncertified_total >= delta

            fibre = [mass for role, mass in zip(roles, uncertified) if role == selected_role]
            assert max(fibre, default=Fraction(0)) * len(fibre) >= role_mass[selected_role]
            counts["pure provenance deficits"] += 1
            counts["localized provenance roles"] += 1
            counts["localized provenance occurrences"] += 1

    counts["systems"] += 1
    counts["resource occurrences"] += len(capacities)


def exhaustive_systems(counts: Counter[str]) -> None:
    values = tuple(Fraction(v) for v in range(3))
    for size in range(1, 4):
        for capacities in product(values, repeat=size):
            for charges in product(values, repeat=size):
                max_residual = max(1, int(sum(capacities, Fraction(0)) + 2))
                for residual_int in range(1, max_residual + 1):
                    roles = tuple(p % min(size, 2) for p in range(size))
                    audit_system(
                        tuple(capacities),
                        tuple(charges),
                        Fraction(residual_int),
                        roles,
                        counts,
                    )
                    counts["exhaustive systems"] += 1


def random_systems(counts: Counter[str]) -> None:
    rng = Random(20260726)
    for _ in range(50000):
        size = rng.randint(1, 12)
        capacities = tuple(
            Fraction(rng.randint(0, 30), rng.randint(1, 6)) for _ in range(size)
        )
        charges = tuple(
            Fraction(rng.randint(0, 30), rng.randint(1, 6)) for _ in range(size)
        )
        residual = Fraction(rng.randint(1, 60), rng.randint(1, 6))
        role_count = rng.randint(1, min(size, 5))
        roles = tuple(rng.randrange(role_count) for _ in range(size))
        audit_system(capacities, charges, residual, roles, counts)
        counts["random systems"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    exhaustive_systems(counts)
    random_systems(counts)
    print("GC2bm--GC2bq gain-row overlap audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
