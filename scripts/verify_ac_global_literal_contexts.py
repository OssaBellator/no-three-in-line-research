#!/usr/bin/env python3
"""Verify AC3ag--AC3ai global literal-context extraction."""

from __future__ import annotations

from itertools import combinations, product


Literal = tuple[int, int]
Context = tuple[Literal, ...]
Scope = frozenset[int]


def contexts(sizes: tuple[int, ...]) -> tuple[Context, ...]:
    result = [()]
    for rank in (1, 2):
        for scope in combinations(range(len(sizes)), rank):
            for labels in product(*(range(sizes[x]) for x in scope)):
                result.append(tuple(zip(scope, labels)))
    return tuple(result)


def effective_scope(
    context: Context,
    sizes: tuple[int, ...],
) -> Scope:
    return frozenset(
        variable for variable, _ in context if sizes[variable] >= 2
    )


def disjoint(family: tuple[Scope, ...]) -> bool:
    return all(
        not (left & right)
        for left, right in combinations(family, 2)
    )


def maximal_matching(scopes: tuple[Scope, ...]) -> tuple[int, ...]:
    chosen: list[int] = []
    occupied: set[int] = set()
    for index in sorted(
        range(len(scopes)),
        key=lambda item: (len(scopes[item]), tuple(scopes[item]), item),
    ):
        if scopes[index] and occupied.isdisjoint(scopes[index]):
            chosen.append(index)
            occupied.update(scopes[index])
    return tuple(chosen)


def realizes(
    family: tuple[Context, ...],
    sizes: tuple[int, ...],
) -> bool:
    assignment: dict[int, int] = {}
    for context in family:
        for variable, label in context:
            if variable in assignment and assignment[variable] != label:
                return False
            assignment[variable] = label
    return all(
        0 <= label < sizes[variable]
        for variable, label in assignment.items()
    )


def dyadic_stratum(
    indices: tuple[int, ...],
    weights: tuple[int, ...],
) -> tuple[tuple[int, ...], int, int]:
    minimum = min(weights[index] for index in indices)
    bins: dict[int, list[int]] = {}
    for index in indices:
        scale = minimum
        level = 0
        while weights[index] >= 2 * scale:
            scale *= 2
            level += 1
        bins.setdefault(level, []).append(index)
    level, members = max(
        bins.items(),
        key=lambda item: (
            sum(weights[index] for index in item[1]),
            -item[0],
        ),
    )
    maximum = max(weights[index] for index in indices)
    scale = minimum * (2 ** level)
    levels = 1
    ceiling = minimum * 2
    while maximum >= ceiling:
        levels += 1
        ceiling *= 2
    return tuple(members), scale, levels


def greedy_coloring(
    indices: tuple[int, ...],
    scopes: tuple[Scope, ...],
) -> tuple[tuple[int, ...], ...]:
    colors: list[list[int]] = []
    for index in indices:
        for color in colors:
            if all(not (scopes[index] & scopes[other]) for other in color):
                color.append(index)
                break
        else:
            colors.append([index])
    return tuple(tuple(color) for color in colors)


def verify_family(
    family: tuple[Context, ...],
    sizes: tuple[int, ...],
    family_id: int,
) -> tuple[int, int]:
    scopes = tuple(effective_scope(context, sizes) for context in family)
    positive = tuple(index for index, scope in enumerate(scopes) if scope)
    units = tuple(index for index, scope in enumerate(scopes) if not scope)
    matching_local = maximal_matching(tuple(scopes[index] for index in positive))
    matching = tuple(positive[index] for index in matching_local)
    matching_scopes = tuple(scopes[index] for index in matching)
    assert disjoint(matching_scopes)
    transversal = (
        set().union(*matching_scopes) if matching_scopes else set()
    )
    assert all(transversal & scopes[index] for index in positive)
    assert len(transversal) <= 2 * len(matching)
    assert realizes(tuple(family[index] for index in matching + units), sizes)

    weights = tuple(
        1 + (11 * index + 5 * family_id + len(context)) % 31
        for index, context in enumerate(family)
    )
    if not positive:
        return 0, 0

    stratum, eta, levels = dyadic_stratum(positive, weights)
    positive_weight = sum(weights[index] for index in positive)
    stratum_weight = sum(weights[index] for index in stratum)
    assert levels * stratum_weight >= positive_weight
    assert all(
        eta <= weights[index] < 2 * eta for index in stratum
    )

    degrees = {
        variable: sum(
            variable in scopes[index] for index in stratum
        )
        for variable in range(len(sizes))
        if sizes[variable] >= 2
    }
    maximum_degree = max(degrees.values(), default=0)
    low_degree_checks = 0
    high_degree_checks = 0
    for degree_cap in range(1, max(2, maximum_degree + 1)):
        if maximum_degree <= degree_cap:
            colors = greedy_coloring(stratum, scopes)
            assert len(colors) <= 2 * degree_cap - 1
            assert all(
                disjoint(tuple(scopes[index] for index in color))
                for color in colors
            )
            heaviest = max(
                sum(weights[index] for index in color)
                for color in colors
            )
            assert heaviest * (2 * degree_cap - 1) >= stratum_weight
            low_degree_checks += 1
            continue

        variable = max(degrees, key=degrees.__getitem__)
        assert degrees[variable] > degree_cap
        phase_counts = {
            label: sum(
                variable in scopes[index]
                and dict(family[index])[variable] == label
                for index in stratum
            )
            for label in range(sizes[variable])
        }
        block_weight = sum(
            weights[index]
            for index in stratum
            if variable in scopes[index]
        )
        assert block_weight > degree_cap * eta
        for phase_cap in range(1, degree_cap + 2):
            maximum_phase = max(phase_counts.values())
            if maximum_phase > phase_cap:
                heavy_phase = max(
                    phase_counts, key=phase_counts.__getitem__
                )
                phase_weight = sum(
                    weights[index]
                    for index in stratum
                    if variable in scopes[index]
                    and dict(family[index])[variable] == heavy_phase
                )
                assert phase_weight > phase_cap * eta
            else:
                used = sum(count > 0 for count in phase_counts.values())
                assert used >= degree_cap // phase_cap + 1
            high_degree_checks += 1

    return low_degree_checks, high_degree_checks


def main() -> None:
    sizes = (2, 2, 1)
    universe = contexts(sizes)
    low_degree = 0
    high_degree = 0
    family_count = 1 << len(universe)
    for mask in range(family_count):
        family = tuple(
            context
            for index, context in enumerate(universe)
            if mask & (1 << index)
        )
        low, high = verify_family(family, sizes, mask)
        low_degree += low
        high_degree += high
    print(
        "AC global literal contexts verified:",
        f"{family_count} context families,",
        f"{low_degree} paid matchings,",
        f"{high_degree} high-degree refinements",
    )


if __name__ == "__main__":
    main()
