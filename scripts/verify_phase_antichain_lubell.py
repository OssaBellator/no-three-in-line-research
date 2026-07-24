#!/usr/bin/env python3
"""Verify OP2h Lubell weights for canonical partial assignments."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from math import comb

Nogood = tuple[tuple[int, int], ...]


def partial_assignments(domain_sizes: tuple[int, ...]) -> tuple[Nogood, ...]:
    result: list[Nogood] = []
    for arity in range(1, len(domain_sizes) + 1):
        for scope in combinations(range(len(domain_sizes)), arity):
            for labels in product(*(range(domain_sizes[v]) for v in scope)):
                result.append(tuple(zip(scope, labels)))
    return tuple(result)


def comparable(left: Nogood, right: Nogood) -> bool:
    left_items = set(left)
    right_items = set(right)
    return left_items.issubset(right_items) or right_items.issubset(
        left_items
    )


def antichain(family: tuple[Nogood, ...]) -> bool:
    return all(
        not comparable(left, right)
        for left, right in combinations(family, 2)
    )


def lubell_weight(
    family: tuple[Nogood, ...],
    domain_sizes: tuple[int, ...],
) -> Fraction:
    variable_count = len(domain_sizes)
    total = Fraction(0)
    for nogood in family:
        scope_product = 1
        for variable, _ in nogood:
            scope_product *= domain_sizes[variable]
        total += Fraction(
            1,
            comb(variable_count, len(nogood)) * scope_product,
        )
    return total


def verify_families(
    domain_sizes: tuple[int, ...],
    maximum_family_size: int,
) -> None:
    nogoods = partial_assignments(domain_sizes)
    for size in range(maximum_family_size + 1):
        for family in combinations(nogoods, size):
            if antichain(family):
                assert lubell_weight(family, domain_sizes) <= 1


def verify_sharp_layers(domain_sizes: tuple[int, ...]) -> None:
    nogoods = partial_assignments(domain_sizes)
    for arity in range(1, len(domain_sizes) + 1):
        layer = tuple(nogood for nogood in nogoods if len(nogood) == arity)
        assert antichain(layer)
        assert lubell_weight(layer, domain_sizes) == 1


def main() -> None:
    verify_families((2, 2, 2), maximum_family_size=4)
    verify_families((2, 3, 2), maximum_family_size=3)
    verify_sharp_layers((2, 2, 2))
    verify_sharp_layers((2, 3, 2))
    print("phase antichain Lubell bounds: exhaustive regressions passed")


if __name__ == "__main__":
    main()
