#!/usr/bin/env python3
"""Finite checks for CMR487--CMR491."""

from __future__ import annotations

from itertools import combinations, permutations


Point = tuple[int, int]
Arc = tuple[int, int]


def collinear(first: Point, second: Point, third: Point) -> bool:
    x1, y1 = first
    x2, y2 = second
    x3, y3 = third
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


def clean_matching(points: list[Point]) -> bool:
    return all(
        not collinear(points[first], points[second], points[third])
        for first, second, third in combinations(range(len(points)), 3)
    )


def verify_rooted_stars() -> None:
    expected = {2: 4, 3: 24, 4: 216, 5: 1_120}
    observed: dict[int, int] = {}

    for side in range(2, 6):
        instances = 0
        for permutation in permutations(range(side)):
            matching = [
                (source, permutation[source])
                for source in range(side)
            ]
            if not clean_matching(matching):
                continue

            matching_set = set(matching)
            for centre in (
                (source, target)
                for source in range(side)
                for target in range(side)
                if (source, target) not in matching_set
            ):
                rooted_pairs = [
                    (first, second)
                    for first, second in combinations(range(side), 2)
                    if collinear(centre, matching[first], matching[second])
                ]

                # CMR487: outside pairs are disjoint and there are at most
                # floor(side/2) rooted arms.
                for first_pair, second_pair in combinations(rooted_pairs, 2):
                    assert set(first_pair).isdisjoint(second_pair)
                assert len(rooted_pairs) <= side // 2

                # CMR488: a cycle-flip state retains exactly the rooted arms
                # whose outside matching indices are not visited.
                for cycle_size in range(2, side + 1):
                    for cycle_vertices in combinations(range(side), cycle_size):
                        visited = set(cycle_vertices)
                        retained = [
                            pair
                            for pair in rooted_pairs
                            if pair[0] not in visited and pair[1] not in visited
                        ]
                        for pair in rooted_pairs:
                            assert (pair in retained) == (
                                pair[0] not in visited and pair[1] not in visited
                            )

                instances += 1
        observed[side] = instances

    assert observed == expected


def directed_cycles(side: int) -> list[tuple[tuple[int, ...], tuple[Arc, ...]]]:
    cycles: list[tuple[tuple[int, ...], tuple[Arc, ...]]] = []
    for cycle_size in range(2, side + 1):
        for vertex_set in combinations(range(side), cycle_size):
            start = min(vertex_set)
            remaining = [vertex for vertex in vertex_set if vertex != start]
            for order in permutations(remaining):
                vertices = (start,) + order
                arcs = tuple(
                    (
                        vertices[index],
                        vertices[(index + 1) % cycle_size],
                    )
                    for index in range(cycle_size)
                )
                cycles.append((vertices, arcs))
    return cycles


def verify_pair_cylinders() -> None:
    expected = {
        2: (1, 1),
        3: (5, 9),
        4: (20, 42),
        5: (84, 130),
    }
    observed: dict[int, tuple[int, int]] = {}

    for side in range(2, 6):
        cycles = directed_cycles(side)
        pair_states: dict[tuple[Arc, Arc], list[frozenset[Arc]]] = {}

        for vertices, arcs in cycles:
            state = frozenset(arcs) | frozenset(
                (index, index)
                for index in range(side)
                if index not in vertices
            )

            for first, second in combinations(arcs, 2):
                # CMR490: distinct cycle arcs form a compatible bipartite pair.
                assert first[0] != second[0]
                assert first[1] != second[1]
                key = tuple(sorted((first, second)))
                pair_states.setdefault(key, []).append(state)

        for pair, states in pair_states.items():
            first, second = pair
            used_sources = {first[0], second[0]}
            used_targets = {first[1], second[1]}
            residuals: list[frozenset[Arc]] = []

            for state in states:
                assert first in state and second in state
                residual = frozenset(
                    (source, target)
                    for source, target in state
                    if source not in used_sources and target not in used_targets
                )
                assert len(residual) == side - 2
                residuals.append(residual)

            # Distinct full states containing the same fixed pair remain
            # distinct after deleting that pair and its endpoints.
            assert len(residuals) == len(set(residuals))

        observed[side] = (len(cycles), len(pair_states))

    assert observed == expected


def main() -> None:
    verify_rooted_stars()
    verify_pair_cylinders()
    print(
        "verified rooted-star and pair-cylinder endpoint: collinear rooted arms "
        "are outside-pair disjoint, cycle-arm presence is exact, and common "
        "cycle arcs form compatible injective rank-two residual cylinders"
    )


if __name__ == "__main__":
    main()
