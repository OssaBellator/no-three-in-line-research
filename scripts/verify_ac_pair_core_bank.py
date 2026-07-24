#!/usr/bin/env python3
"""Verify AC3m--AC3o high-pair endpoint rematching."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial


Point = tuple[int, int]


def collinear(left: Point, middle: Point, right: Point) -> bool:
    return (
        (middle[0] - left[0]) * (right[1] - left[1])
        == (middle[1] - left[1]) * (right[0] - left[0])
    )


def triple_potential(points: set[Point]) -> int:
    return sum(
        collinear(left, middle, right)
        for left, middle, right in combinations(points, 3)
    )


def is_compatible(cells: tuple[Point, ...]) -> bool:
    return (
        len({column for column, _ in cells}) == len(cells)
        and len({row for _, row in cells}) == len(cells)
    )


def verify_pair_core_bank() -> None:
    order = 9
    red = {(index, index) for index in range(order)}
    blue = {
        (index, (index + 1) % order)
        for index in range(order)
    }
    assert red.isdisjoint(blue)

    first_anchor = (0, 0)
    second_anchor = (1, 1)
    selected = {(index, index) for index in range(2, order)}
    columns = tuple(range(2, order))
    rows = tuple(range(2, order))
    size = len(selected)
    assert size == 7

    forbidden = {
        (columns[index], rows[index])
        for index in range(size)
    }
    forbidden.update(
        point
        for point in blue
        if point[0] in columns and point[1] in rows
    )

    row_degrees = Counter(row for _, row in forbidden)
    column_degrees = Counter(column for column, _ in forbidden)
    assert max(row_degrees.values()) <= 2
    assert max(column_degrees.values()) <= 2

    allowed_matchings: list[frozenset[Point]] = []
    for permutation in permutations(range(size)):
        matching = frozenset(
            (columns[index], rows[permutation[index]])
            for index in range(size)
        )
        if matching.isdisjoint(forbidden):
            allowed_matchings.append(matching)
    assert allowed_matchings
    assert len(allowed_matchings) * 128 >= factorial(size)

    base_state = red | blue
    fixed = base_state - selected
    fixed_potential = triple_potential(fixed)
    destroyed = triple_potential(base_state) - fixed_potential
    assert destroyed >= size

    cylinder_counts: dict[int, defaultdict[tuple[Point, ...], int]] = {
        rank: defaultdict(int)
        for rank in range(1, 4)
    }
    state_collateral = 0
    all_state_potentials: list[int] = []

    for matching in allowed_matchings:
        new_red = (red - selected) | set(matching)
        assert len(new_red) == order
        assert new_red.isdisjoint(blue)

        state = new_red | blue
        assert len(state) == 2 * order
        assert all(
            sum(point[0] == coordinate for point in state) == 2
            for coordinate in range(order)
        )
        assert all(
            sum(point[1] == coordinate for point in state) == 2
            for coordinate in range(order)
        )
        assert set(matching).isdisjoint(selected)
        for endpoint in selected:
            assert not {
                first_anchor,
                second_anchor,
                endpoint,
            }.issubset(state)

        state_potential = triple_potential(state)
        all_state_potentials.append(state_potential)
        state_collateral += state_potential - fixed_potential

        ordered_matching = tuple(sorted(matching))
        for rank in range(1, 4):
            for cylinder in combinations(ordered_matching, rank):
                cylinder_counts[rank][cylinder] += 1

    state_count = len(allowed_matchings)
    for rank in range(1, 4):
        falling_factorial = factorial(size) // factorial(size - rank)
        for count in cylinder_counts[rank].values():
            assert count <= factorial(size - rank)
            assert (
                Fraction(count, state_count)
                <= Fraction(128, falling_factorial)
            )

    block = {
        (column, row)
        for column in columns
        for row in rows
        if (column, row) not in forbidden
    }
    certificate_counts = [0, 0, 0, 0]
    certificate_occurrences = 0
    for rank in range(1, 4):
        for block_cells in combinations(block, rank):
            if not is_compatible(block_cells):
                continue
            for fixed_cells in combinations(fixed, 3 - rank):
                triple = block_cells + fixed_cells
                if collinear(triple[0], triple[1], triple[2]):
                    certificate_counts[rank] += 1
                    certificate_occurrences += cylinder_counts[rank][
                        tuple(sorted(block_cells))
                    ]

    assert certificate_occurrences == state_collateral

    normalized_bound = 128 * sum(
        Fraction(
            certificate_counts[rank],
            factorial(size) // factorial(size - rank),
        )
        for rank in range(1, 4)
    )
    assert Fraction(state_collateral, state_count) <= normalized_bound

    if min(all_state_potentials) >= triple_potential(base_state):
        assert max(
            Fraction(
                certificate_counts[rank],
                factorial(size) // factorial(size - rank),
            )
            for rank in range(1, 4)
        ) >= Fraction(destroyed, 384)


def verify_constant_threshold_router() -> None:
    for codegree in range(13, 41):
        for red_count in range(codegree + 1):
            blue_count = codegree - red_count
            assert max(red_count, blue_count) >= 7

    codegree = 13
    for red_count in range(codegree + 1):
        for weights in product(range(2), repeat=codegree):
            total_weight = sum(weights)
            if total_weight == 0:
                continue
            red_weights = weights[:red_count]
            blue_weights = weights[red_count:]
            parts = (
                (len(red_weights), sum(red_weights), red_weights),
                (len(blue_weights), sum(blue_weights), blue_weights),
            )
            size, weight, part_weights = max(
                parts,
                key=lambda part: part[1],
            )
            assert 2 * weight >= total_weight
            if size >= 7:
                continue
            assert part_weights
            assert 12 * max(part_weights) >= total_weight


def hyperbola(prime: int, channel: int) -> set[Point]:
    return {
        (column, channel * pow(column, -1, prime) % prime)
        for column in range(1, prime)
    }


def verify_channel_pair_cap() -> None:
    for prime in (5, 7, 11):
        channels = {
            channel: hyperbola(prime, channel)
            for channel in range(1, prime)
        }
        maximum_channels = min(3, prime - 1)
        for channel_count in range(1, maximum_channels + 1):
            for chosen in combinations(range(1, prime), channel_count):
                state = set().union(*(channels[channel] for channel in chosen))
                for left, right in combinations(state, 2):
                    third_count = sum(
                        point not in (left, right)
                        and collinear(left, right, point)
                        for point in state
                    )
                    assert third_count <= 2 * channel_count - 2

        chosen = (1, 2)
        algebraic = set().union(*(channels[channel] for channel in chosen))
        exceptions = set()
        for point in product(range(1, prime), repeat=2):
            if point not in algebraic:
                exceptions.add(point)
            if len(exceptions) == 3:
                break
        state = algebraic | exceptions
        for left, right in combinations(state, 2):
            pair = {left, right}
            third_points = {
                point
                for point in state - pair
                if collinear(left, right, point)
            }
            algebraic_pair_count = sum(
                point in algebraic
                for point in pair
            )
            lower_bound = max(
                0,
                len(third_points) - (4 - algebraic_pair_count),
            )
            assert len(third_points & exceptions) >= lower_bound


def main() -> None:
    verify_pair_core_bank()
    verify_constant_threshold_router()
    verify_channel_pair_cap()
    print("AC high-pair endpoint rematching: verified")


if __name__ == "__main__":
    main()
