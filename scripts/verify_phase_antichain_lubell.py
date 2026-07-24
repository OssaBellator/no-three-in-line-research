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


def condition_nogood(
    nogood: Nogood,
    assignment: dict[int, int],
    remap: dict[int, int],
) -> Nogood | None:
    residual: list[tuple[int, int]] = []
    for variable, label in nogood:
        if variable in assignment:
            if assignment[variable] != label:
                return None
        else:
            residual.append((remap[variable], label))
    return tuple(residual)


def canonical_residual(family: tuple[Nogood, ...]) -> tuple[Nogood, ...]:
    unique = set(family)
    return tuple(
        sorted(
            nogood
            for nogood in unique
            if not any(
                set(other) < set(nogood) for other in unique
            )
        )
    )


def verify_conditioning_amplification(
    family: tuple[Nogood, ...],
    domain_sizes: tuple[int, ...],
) -> None:
    if not family or len(domain_sizes) < 2:
        return
    variable_count = len(domain_sizes)
    rank = max(len(nogood) for nogood in family)
    variables = tuple(range(variable_count))
    for fixed_size in range(1, variable_count):
        for fixed in combinations(variables, fixed_size):
            fixed_set = set(fixed)
            remaining_variables = tuple(
                variable for variable in variables
                if variable not in fixed_set
            )
            remap = {
                variable: index
                for index, variable in enumerate(remaining_variables)
            }
            residual_domains = tuple(
                domain_sizes[variable]
                for variable in remaining_variables
            )
            pattern_count = sum(
                comb(fixed_size, intersection_size)
                for intersection_size in range(
                    min(fixed_size, rank - 1) + 1
                )
            )
            for labels in product(
                *(range(domain_sizes[variable]) for variable in fixed)
            ):
                assignment = dict(zip(fixed, labels))
                survivors: list[tuple[Nogood, Nogood]] = []
                contradiction = False
                for nogood in family:
                    residual = condition_nogood(
                        nogood,
                        assignment,
                        remap,
                    )
                    if residual is None:
                        continue
                    if not residual:
                        contradiction = True
                        break
                    survivors.append((nogood, residual))
                if contradiction:
                    continue

                canonical = canonical_residual(
                    tuple(residual for _, residual in survivors)
                )
                residual_mass = lubell_weight(
                    canonical,
                    residual_domains,
                )
                residual_loads, _ = lubell_loads(
                    canonical,
                    residual_domains,
                )
                amplified_total = Fraction(0)
                amplified_loads = [
                    Fraction(0) for _ in residual_domains
                ]
                pattern_mass: dict[frozenset[int], Fraction] = {}
                pattern_residuals: dict[
                    frozenset[int],
                    list[Nogood],
                ] = {}
                for original, residual in survivors:
                    intersection = frozenset(
                        variable
                        for variable, _ in original
                        if variable in fixed_set
                    )
                    original_weight = lubell_weight(
                        (original,),
                        domain_sizes,
                    )
                    factor = Fraction(
                        comb(variable_count, len(original)),
                        comb(
                            variable_count - fixed_size,
                            len(residual),
                        ),
                    )
                    for variable in intersection:
                        factor *= domain_sizes[variable]
                    residual_weight = lubell_weight(
                        (residual,),
                        residual_domains,
                    )
                    assert original_weight * factor == residual_weight
                    amplified_total += residual_weight
                    pattern_mass[intersection] = (
                        pattern_mass.get(intersection, Fraction(0))
                        + residual_weight
                    )
                    pattern_residuals.setdefault(
                        intersection,
                        [],
                    ).append(residual)
                    for variable, _ in residual:
                        amplified_loads[variable] += residual_weight

                assert residual_mass <= amplified_total
                assert all(
                    residual_loads[variable]
                    <= amplified_loads[variable]
                    for variable in range(len(residual_domains))
                )
                if residual_mass:
                    assert pattern_mass
                    assert (
                        max(pattern_mass.values()) * pattern_count
                        >= residual_mass
                    )
                for intersection, residuals in pattern_residuals.items():
                    assert len(residuals) == len(set(residuals))
                    assert antichain(tuple(residuals))
                    assert pattern_mass[intersection] == lubell_weight(
                        tuple(residuals),
                        residual_domains,
                    )
                    assert pattern_mass[intersection] <= 1
                assert amplified_total <= pattern_count


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
                verify_conditioning_amplification(
                    family,
                    domain_sizes,
                )


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
