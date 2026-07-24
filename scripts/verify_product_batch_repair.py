#!/usr/bin/env python3
"""Exact one- and two-cycle batch-repair censuses for side 6 and side 9."""
from __future__ import annotations

from collections import Counter

from verify_product_hybrid_repair import (
    FactorPair,
    Point,
    enumerate_degree_two_states,
    product_host,
    triple_potential,
)


def state_mask(
    state: tuple[Point, ...],
    edge_index: dict[Point, int],
) -> int:
    return sum(1 << edge_index[edge] for edge in state)


def alternating_neighbour_masks(
    host: tuple[Point, ...],
    state: tuple[Point, ...],
) -> tuple[int, ...]:
    """Enumerate every state obtained by toggling one simple alternating cycle."""
    side = len(host) // 4
    edge_index = {edge: index for index, edge in enumerate(host)}
    selected = state_mask(state, edge_index)

    adjacency: list[list[tuple[int, int]]] = [
        [] for _ in range(2 * side)
    ]
    for index, (x, y) in enumerate(host):
        row = x
        column = side + y
        adjacency[row].append((index, column))
        adjacency[column].append((index, row))

    cycles: set[int] = set()
    for start in range(side):
        for first_edge, first_vertex in adjacency[start]:
            if not (selected & (1 << first_edge)):
                continue

            def search(
                vertex: int,
                need_selected: bool,
                visited: frozenset[int],
                edge_mask: int,
                depth: int,
            ) -> None:
                for edge, neighbour in adjacency[vertex]:
                    edge_is_selected = bool(selected & (1 << edge))
                    if edge_is_selected != need_selected:
                        continue
                    if neighbour == start:
                        if depth >= 3:
                            cycles.add(edge_mask | (1 << edge))
                        continue
                    if neighbour < side and neighbour < start:
                        continue
                    if neighbour in visited:
                        continue
                    search(
                        neighbour,
                        not need_selected,
                        visited | {neighbour},
                        edge_mask | (1 << edge),
                        depth + 1,
                    )

            search(
                first_vertex,
                False,
                frozenset((start, first_vertex)),
                1 << first_edge,
                1,
            )

    return tuple(selected ^ cycle for cycle in cycles)


def census(
    outer: FactorPair,
    inner: FactorPair,
    orientation: str,
    expected_states: int,
    expected_edges: int,
    expected_solutions: int,
    expected_one_step: int,
    expected_profiles: Counter[tuple[int, int, int]],
) -> None:
    host = product_host(outer, inner, orientation)
    states = enumerate_degree_two_states(host)
    assert len(states) == expected_states

    edge_index = {edge: index for index, edge in enumerate(host)}
    mask_to_state = {
        state_mask(state, edge_index): index
        for index, state in enumerate(states)
    }
    potentials = tuple(triple_potential(state) for state in states)
    assert sum(value == 0 for value in potentials) == expected_solutions

    neighbours: list[tuple[int, ...]] = []
    directed_edges = 0
    for state in states:
        ids = tuple(
            mask_to_state[mask]
            for mask in alternating_neighbour_masks(host, state)
        )
        neighbours.append(ids)
        directed_edges += len(ids)
    assert directed_edges // 2 == expected_edges

    one_step = 0
    profiles: Counter[tuple[int, int, int]] = Counter()
    for index, value in enumerate(potentials):
        if value == 0:
            continue
        if any(potentials[neighbour] < value for neighbour in neighbours[index]):
            one_step += 1
            continue

        candidates = [
            (potentials[middle], potentials[endpoint])
            for middle in neighbours[index]
            for endpoint in neighbours[middle]
            if potentials[endpoint] < value
        ]
        assert candidates, (index, value)
        middle_value, endpoint_value = min(candidates)
        profiles[(value, middle_value, endpoint_value)] += 1

    assert one_step == expected_one_step
    assert profiles == expected_profiles
    bad_states = len(states) - expected_solutions
    print(
        f"side={len(host) // 4}, orientation={orientation}: "
        f"states={len(states)}, edges={expected_edges}, solutions={expected_solutions}, "
        f"one_step={one_step}/{bad_states}, two_step_profiles={dict(profiles)}"
    )


def main() -> None:
    census(
        outer=((0, 1), (1, 0)),
        inner=((0, 2, 1), (1, 0, 2)),
        orientation="cf",
        expected_states=546,
        expected_edges=20944,
        expected_solutions=2,
        expected_one_step=534,
        expected_profiles=Counter({(1, 2, 0): 10}),
    )
    census(
        outer=((0, 2, 1), (1, 0, 2)),
        inner=((1, 2, 0), (2, 0, 1)),
        orientation="cf",
        expected_states=6840,
        expected_edges=1359432,
        expected_solutions=2,
        expected_one_step=6814,
        expected_profiles=Counter({(3, 3, 0): 20, (3, 4, 0): 4}),
    )


if __name__ == "__main__":
    main()
