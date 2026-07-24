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


def lubell_loads(
    family: tuple[Nogood, ...],
    domain_sizes: tuple[int, ...],
) -> tuple[list[Fraction], dict[tuple[int, int], Fraction]]:
    variable_count = len(domain_sizes)
    variable_loads = [Fraction(0) for _ in domain_sizes]
    literal_loads = {
        (variable, label): Fraction(0)
        for variable, size in enumerate(domain_sizes)
        for label in range(size)
    }
    for nogood in family:
        scope_product = 1
        for variable, _ in nogood:
            scope_product *= domain_sizes[variable]
        weight = Fraction(
            1,
            comb(variable_count, len(nogood)) * scope_product,
        )
        for variable, label in nogood:
            variable_loads[variable] += weight
            literal_loads[variable, label] += weight
    return variable_loads, literal_loads


def verify_load_localization(
    family: tuple[Nogood, ...],
    domain_sizes: tuple[int, ...],
) -> None:
    variable_loads, literal_loads = lubell_loads(family, domain_sizes)
    rank = max((len(nogood) for nogood in family), default=0)
    weighted_rank = sum(
        (
            len(nogood) * lubell_weight((nogood,), domain_sizes)
            for nogood in family
        ),
        Fraction(0),
    )
    assert sum(variable_loads, Fraction(0)) == weighted_rank
    assert weighted_rank <= rank

    for variable, size in enumerate(domain_sizes):
        assert sum(
            (
                literal_loads[variable, label]
                for label in range(size)
            ),
            Fraction(0),
        ) == variable_loads[variable]
        assert min(
            literal_loads[variable, label] for label in range(size)
        ) <= variable_loads[variable] / size

    for numerator in range(1, 4 * max(1, rank) + 1):
        threshold = Fraction(numerator, 12)
        heavy_variables = sum(
            load >= threshold for load in variable_loads
        )
        heavy_literals = sum(
            load >= threshold for load in literal_loads.values()
        )
        assert heavy_variables * threshold <= rank
        assert heavy_literals * threshold <= rank

    if domain_sizes:
        lightest = min(
            range(len(domain_sizes)),
            key=variable_loads.__getitem__,
        )
        assert variable_loads[lightest] <= Fraction(
            rank,
            len(domain_sizes),
        )
        assert min(
            literal_loads[lightest, label]
            for label in range(domain_sizes[lightest])
        ) <= Fraction(
            rank,
            len(domain_sizes) * domain_sizes[lightest],
        )


def verify_families(
    domain_sizes: tuple[int, ...],
    maximum_family_size: int,
) -> None:
    nogoods = partial_assignments(domain_sizes)
    for size in range(maximum_family_size + 1):
        for family in combinations(nogoods, size):
            if antichain(family):
                assert lubell_weight(family, domain_sizes) <= 1
                verify_load_localization(family, domain_sizes)


def verify_sharp_layers(domain_sizes: tuple[int, ...]) -> None:
    nogoods = partial_assignments(domain_sizes)
    for arity in range(1, len(domain_sizes) + 1):
        layer = tuple(nogood for nogood in nogoods if len(nogood) == arity)
        assert antichain(layer)
        assert lubell_weight(layer, domain_sizes) == 1
        variable_loads, literal_loads = lubell_loads(
            layer,
            domain_sizes,
        )
        for variable, size in enumerate(domain_sizes):
            assert variable_loads[variable] == Fraction(
                arity,
                len(domain_sizes),
            )
            for label in range(size):
                assert literal_loads[variable, label] == Fraction(
                    arity,
                    len(domain_sizes) * size,
                )


def main() -> None:
    verify_families((2, 2, 2), maximum_family_size=4)
    verify_families((2, 3, 2), maximum_family_size=3)
    verify_sharp_layers((2, 2, 2))
    verify_sharp_layers((2, 3, 2))
    print("phase antichain Lubell bounds: exhaustive regressions passed")


if __name__ == "__main__":
    main()
