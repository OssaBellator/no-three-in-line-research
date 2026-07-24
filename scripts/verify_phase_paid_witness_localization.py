#!/usr/bin/env python3
"""Verify OP3g--OP3i paid correction-witness localization."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, product


Assignment = tuple[int, ...]
Support = frozenset[int]
Factor = tuple[tuple[int, int], ...]


def ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def support(
    current: Assignment,
    correction: Assignment,
) -> Support:
    return frozenset(
        variable
        for variable in range(len(current))
        if current[variable] != correction[variable]
    )


def factor_scope(factor: Factor) -> Support:
    return frozenset(variable for variable, _ in factor)


def conflict(
    left: int,
    right: int,
    supports: tuple[Support, ...],
    active_factors: tuple[Factor, ...],
) -> bool:
    if supports[left] & supports[right]:
        return True
    return any(
        factor_scope(factor) & supports[left]
        and factor_scope(factor) & supports[right]
        for factor in active_factors
    )


def corrections(sizes: tuple[int, ...]) -> tuple[Assignment, ...]:
    current = tuple(0 for _ in sizes)
    result: list[Assignment] = []
    for rank in (1, 2):
        for variables in combinations(range(len(sizes)), rank):
            domains = tuple(range(1, sizes[v]) for v in variables)
            for values in product(*domains):
                candidate = list(current)
                for variable, value in zip(variables, values):
                    candidate[variable] = value
                result.append(tuple(candidate))
    return tuple(result)


def factors(sizes: tuple[int, ...]) -> tuple[Factor, ...]:
    result: list[Factor] = []
    index = 0
    for rank in (2, 3):
        for variables in combinations(range(len(sizes)), rank):
            result.append(
                tuple(
                    (
                        variable,
                        (index + 2 * variable + rank) % sizes[variable],
                    )
                    for variable in variables
                )
            )
            index += 1
    return tuple(result)


def witness_partition(
    center: int,
    supports: tuple[Support, ...],
    active_factors: tuple[Factor, ...],
) -> tuple[
    dict[int, tuple[int, ...]],
    dict[int, tuple[int, ...]],
]:
    overlap: dict[int, list[int]] = defaultdict(list)
    coupled: dict[int, list[int]] = defaultdict(list)
    center_support = supports[center]

    for neighbor, neighbor_support in enumerate(supports):
        if neighbor == center:
            continue
        intersection = center_support & neighbor_support
        if intersection:
            overlap[min(intersection)].append(neighbor)
            continue

        witnesses = tuple(
            factor_index
            for factor_index, factor in enumerate(active_factors)
            if factor_scope(factor) & center_support
            and factor_scope(factor) & neighbor_support
        )
        if witnesses:
            coupled[min(witnesses)].append(neighbor)

    return (
        {
            variable: tuple(neighbors)
            for variable, neighbors in overlap.items()
        },
        {
            factor_index: tuple(neighbors)
            for factor_index, neighbors in coupled.items()
        },
    )


def degree(
    partition: tuple[
        dict[int, tuple[int, ...]],
        dict[int, tuple[int, ...]],
    ],
) -> int:
    overlap, coupled = partition
    return sum(map(len, overlap.values())) + sum(
        map(len, coupled.values())
    )


def classify(
    center: int,
    sizes: tuple[int, ...],
    current: Assignment,
    candidates: tuple[Assignment, ...],
    supports: tuple[Support, ...],
    active_factors: tuple[Factor, ...],
    partition: tuple[
        dict[int, tuple[int, ...]],
        dict[int, tuple[int, ...]],
    ],
    support_cap: int,
    star_size: int,
    degree_threshold: int,
) -> str:
    center_support = supports[center]
    assert len(center_support) <= support_cap
    assert degree(partition) >= degree_threshold
    assert degree_threshold > support_cap * star_size * (
        star_size - 1
    )

    overlap, coupled = partition
    overlap_stars = tuple(
        (variable, neighbors)
        for variable, neighbors in overlap.items()
        if len(neighbors) >= star_size
    )
    if overlap_stars:
        variable, neighbors = min(overlap_stars)
        labels = Counter(
            candidates[neighbor][variable]
            for neighbor in neighbors
        )
        assert all(
            candidates[neighbor][variable] != current[variable]
            for neighbor in neighbors
        )
        assert max(labels.values()) >= ceil_div(
            star_size,
            sizes[variable] - 1,
        )
        return "variable"

    factor_stars = tuple(
        (factor_index, neighbors)
        for factor_index, neighbors in coupled.items()
        if len(neighbors) >= star_size
    )
    if factor_stars:
        factor_index, neighbors = min(factor_stars)
        factor = active_factors[factor_index]
        scope = factor_scope(factor)
        literals: Counter[tuple[int, int]] = Counter()
        for neighbor in neighbors:
            variable = min(supports[neighbor] & scope)
            literals[(variable, candidates[neighbor][variable])] += 1
        action_count = sum(sizes[v] - 1 for v in scope)
        assert max(literals.values()) >= ceil_div(
            star_size,
            action_count,
        )
        assert all(
            not (center_support & supports[neighbor])
            for neighbor in neighbors
        )
        return "factor"

    rooted: dict[int, list[int]] = defaultdict(list)
    for factor_index in coupled:
        factor = active_factors[factor_index]
        root = min(center_support & factor_scope(factor))
        rooted[root].append(factor_index)

    root, fan = max(
        rooted.items(),
        key=lambda item: (len(item[1]), -item[0]),
    )
    assert len(fan) >= star_size
    forbidden_labels = Counter(
        dict(active_factors[factor_index])[root]
        for factor_index in fan
    )
    assert max(forbidden_labels.values()) >= ceil_div(
        star_size,
        sizes[root],
    )

    chosen_neighbors = tuple(
        coupled[factor_index][0]
        for factor_index in fan
    )
    assert len(set(chosen_neighbors)) == len(chosen_neighbors)
    assert all(
        not (center_support & supports[neighbor])
        for neighbor in chosen_neighbors
    )
    return "fan"


def verify_exhaustive_systems() -> None:
    current = tuple(0 for _ in SIZES)
    candidates = corrections(SIZES)
    supports = tuple(
        support(current, candidate)
        for candidate in candidates
    )
    universe = factors(SIZES)

    for factor_mask in range(1 << len(universe)):
        active_factors = tuple(
            factor
            for index, factor in enumerate(universe)
            if factor_mask & (1 << index)
        )
        partitions = tuple(
            witness_partition(
                center,
                supports,
                active_factors,
            )
            for center in range(len(candidates))
        )
        for center, partition in enumerate(partitions):
            overlap, coupled = partition
            actual = tuple(
                neighbor
                for bucket in (*overlap.values(), *coupled.values())
                for neighbor in bucket
            )
            expected = {
                neighbor
                for neighbor in range(len(candidates))
                if neighbor != center
                and conflict(
                    center,
                    neighbor,
                    supports,
                    active_factors,
                )
            }
            assert len(actual) == len(set(actual))
            assert set(actual) == expected
        degrees = tuple(map(degree, partitions))
        weights = tuple(
            1 + (7 * center + 3 * factor_mask) % 11
            for center in range(len(candidates))
        )
        total_weight = sum(weights)

        for support_cap in (1, 2):
            for star_size in (2, 3):
                lower = support_cap * star_size * (star_size - 1)
                for threshold in range(lower + 1, len(candidates)):
                    high = tuple(
                        center
                        for center, value in enumerate(degrees)
                        if value >= threshold
                    )
                    if not high:
                        continue
                    high_weight = sum(weights[center] for center in high)
                    wide = tuple(
                        center
                        for center in high
                        if len(supports[center]) > support_cap
                    )
                    wide_weight = sum(
                        weights[center]
                        for center in wide
                    )
                    if 2 * wide_weight > high_weight:
                        if 2 * high_weight > total_weight:
                            assert 4 * wide_weight > total_weight
                        continue

                    class_weights = Counter()
                    for center in high:
                        if center in wide:
                            continue
                        kind = classify(
                            center,
                            SIZES,
                            current,
                            candidates,
                            supports,
                            active_factors,
                            partitions[center],
                            support_cap,
                            star_size,
                            threshold,
                        )
                        class_weights[kind] += weights[center]

                    assert class_weights
                    assert 6 * max(class_weights.values()) >= high_weight
                    if 2 * high_weight > total_weight:
                        assert (
                            12 * max(class_weights.values())
                            > total_weight
                        )


def verify_fan_is_necessary() -> None:
    sizes = (2,) * 9
    current = (0,) * 9
    center = (1,) + (0,) * 8
    neighbors = tuple(
        tuple(1 if variable == index else 0 for variable in range(9))
        for index in range(1, 9)
    )
    candidates = (center,) + neighbors
    supports = tuple(
        support(current, candidate)
        for candidate in candidates
    )
    active_factors = tuple(
        ((0, index % 2), (index, 1))
        for index in range(1, 9)
    )
    partition = witness_partition(0, supports, active_factors)
    overlap, coupled = partition

    assert not overlap
    assert max(map(len, coupled.values())) == 1
    assert degree(partition) == 8

    rooted = {
        min(supports[0] & factor_scope(active_factors[index]))
        for index in coupled
    }
    assert rooted == {0}
    assert classify(
        0,
        sizes,
        current,
        candidates,
        supports,
        active_factors,
        partition,
        support_cap=1,
        star_size=3,
        degree_threshold=7,
    ) == "fan"


SIZES = (3, 2, 3, 2)


def main() -> None:
    verify_exhaustive_systems()
    verify_fan_is_necessary()
    print("OP paid witness localization: exhaustive regressions passed")


if __name__ == "__main__":
    main()
