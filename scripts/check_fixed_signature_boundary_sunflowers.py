#!/usr/bin/env python3
"""Exact small audits for PP3bxd--PP3bxf."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
from math import ceil, factorial


def is_sunflower(sets: tuple[frozenset[int], ...]) -> bool:
    if len(sets) <= 2:
        return True
    core = sets[0] & sets[1]
    return all((a & b) == core for a, b in combinations(sets, 2))


def has_sunflower(family: tuple[frozenset[int], ...], size: int) -> bool:
    return any(is_sunflower(choice) for choice in combinations(family, size))


def exhaustive_uniform_audit(n: int, r: int, max_s: int) -> int:
    universe = tuple(range(n))
    all_sets = tuple(frozenset(c) for c in combinations(universe, r))
    checked = 0
    for mask in range(1 << len(all_sets)):
        family = tuple(all_sets[i] for i in range(len(all_sets)) if mask & (1 << i))
        for s in range(2, max_s + 1):
            threshold = factorial(r) * (s - 1) ** r
            if len(family) > threshold:
                assert has_sunflower(family, s), (n, r, s, family)
        if family:
            # Verify the equivalent strict integer threshold directly.
            guaranteed = max(
                s for s in range(1, len(family) + 1)
                if s == 1 or factorial(r) * (s - 1) ** r < len(family)
            )
            assert has_sunflower(family, guaranteed)
        checked += 1
    return checked


def weighted_role_audit() -> dict[str, str | int]:
    r = 3
    L = Fraction(5, 2)
    boundary_sets = [
        (0, 1, 2),
        (0, 3, 4),
        (0, 5, 6),
        (7, 8, 9),
    ]
    ordered_paths: list[tuple[tuple[int, ...], Fraction]] = []
    weights = [Fraction(1, 2), Fraction(3, 2), Fraction(5, 2)]
    for index, boundary_set in enumerate(boundary_sets):
        for j, role_tuple in enumerate(permutations(boundary_set)):
            ordered_paths.append((role_tuple, weights[(index + j) % len(weights)]))

    per_set: dict[frozenset[int], Fraction] = {}
    multiplicity: dict[frozenset[int], int] = {}
    for role_tuple, weight in ordered_paths:
        key = frozenset(role_tuple)
        per_set[key] = per_set.get(key, Fraction(0)) + weight
        multiplicity[key] = multiplicity.get(key, 0) + 1
        assert weight <= L

    assert max(multiplicity.values()) == factorial(r)
    assert all(value <= factorial(r) * L for value in per_set.values())
    total = sum((weight for _, weight in ordered_paths), Fraction(0))
    distinct = len(per_set)
    assert Fraction(distinct, 1) >= total / (factorial(r) * L)

    sunflower = tuple(frozenset(x) for x in boundary_sets[:3])
    assert is_sunflower(sunflower)
    return {
        "r": r,
        "distinct_boundary_sets": distinct,
        "ordered_paths": len(ordered_paths),
        "total_weight": str(total),
        "maximum_set_multiplicity": max(multiplicity.values()),
    }


def main() -> None:
    families_checked = 0
    families_checked += exhaustive_uniform_audit(n=6, r=2, max_s=3)
    families_checked += exhaustive_uniform_audit(n=5, r=3, max_s=2)
    report = weighted_role_audit()
    print({
        "all_checks_passed": True,
        "uniform_families_checked": families_checked,
        "weighted_role_audit": report,
    })


if __name__ == "__main__":
    main()
