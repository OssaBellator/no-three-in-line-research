#!/usr/bin/env python3
"""Exhaustive finite checks for CMR448--CMR452."""

from __future__ import annotations

from itertools import permutations


Edge = tuple[int, int]


def matching(vector: tuple[int, ...]) -> frozenset[Edge]:
    return frozenset((left, right) for left, right in enumerate(vector))


def mask_of(edges: frozenset[Edge], positions: dict[Edge, int]) -> int:
    mask = 0
    for edge in edges:
        mask |= 1 << positions[edge]
    return mask


def perfect_matching_masks(side: int, positions: dict[Edge, int]) -> list[int]:
    return [
        mask_of(matching(vector), positions)
        for vector in permutations(range(side))
    ]


def essential_mask(host: int, matchings: list[int]) -> int:
    states = [state for state in matchings if state & ~host == 0]
    if not states:
        return 0
    common = states[0]
    for state in states[1:]:
        common &= state
    return common


def vector_from_mask(side: int, mask: int, universe: list[Edge]) -> tuple[int, ...]:
    vector = [-1] * side
    for index, (left, right) in enumerate(universe):
        if mask & (1 << index):
            vector[left] = right
    assert all(value >= 0 for value in vector)
    return tuple(vector)


def cycle_costs(
    side: int,
    base_vector: tuple[int, ...],
    other_vector: tuple[int, ...],
    arc_weight: dict[tuple[int, int], int],
) -> list[int]:
    inverse = {right: left for left, right in enumerate(base_vector)}
    successor = [inverse[other_vector[left]] for left in range(side)]
    seen: set[int] = set()
    costs: list[int] = []

    for start in range(side):
        if start in seen or successor[start] == start:
            seen.add(start)
            continue
        current = start
        total = 0
        while current not in seen:
            seen.add(current)
            next_vertex = successor[current]
            total += arc_weight[(current, next_vertex)]
            current = next_vertex
        costs.append(total)
    return costs


def verify_pair(
    side: int,
    final_host: int,
    initial_host: int,
    universe: list[Edge],
    positions: dict[Edge, int],
    matchings: list[int],
) -> None:
    initial_states = [state for state in matchings if state & ~initial_host == 0]
    final_states = [state for state in matchings if state & ~final_host == 0]
    if not initial_states or not final_states:
        return
    if essential_mask(initial_host, matchings):
        return

    final_essential = essential_mask(final_host, matchings)
    if not final_essential:
        return

    deleted = initial_host & ~final_host

    for edge_index, edge in enumerate(universe):
        edge_bit = 1 << edge_index
        if not final_essential & edge_bit:
            continue

        avoiding = [
            state
            for state in initial_states
            if not state & edge_bit
        ]
        assert avoiding

        costs = {state: (state & deleted).bit_count() for state in avoiding}
        minimum = min(costs.values())
        optimal = {state for state, value in costs.items() if value == minimum}
        base = min(optimal)
        base_vector = vector_from_mask(side, base, universe)
        inverse = {right: left for left, right in enumerate(base_vector)}

        arcs: list[tuple[int, int, int, int]] = []
        arc_weight: dict[tuple[int, int], int] = {}
        for nonmatching_index, nonmatching_edge in enumerate(universe):
            nonmatching_bit = 1 << nonmatching_index
            if not initial_host & nonmatching_bit:
                continue
            if nonmatching_bit == edge_bit or base & nonmatching_bit:
                continue
            left, right = nonmatching_edge
            target = inverse[right]
            matching_edge = (target, base_vector[target])
            weight = int(bool(deleted & nonmatching_bit)) - int(
                bool(deleted & (1 << positions[matching_edge]))
            )
            arcs.append((left, target, weight, nonmatching_bit))
            arc_weight[(left, target)] = weight

        # Super-source zero arcs mean every initial distance is zero.
        distance = [0] * side
        for _ in range(side - 1):
            changed = False
            for source, target, weight, _bit in arcs:
                candidate = distance[source] + weight
                if candidate < distance[target]:
                    distance[target] = candidate
                    changed = True
            if not changed:
                break

        for source, target, weight, _bit in arcs:
            assert distance[target] <= distance[source] + weight
            reduced = weight + distance[source] - distance[target]
            assert reduced >= 0
        assert all(-(side - 1) <= value <= 0 for value in distance)

        tight_host = base
        for source, target, weight, bit in arcs:
            reduced = weight + distance[source] - distance[target]
            if reduced == 0:
                tight_host |= bit
                assert distance[target] - distance[source] == weight
                assert weight in (-1, 0, 1)

        tight_states = {
            state
            for state in matchings
            if state & edge_bit == 0 and state & ~tight_host == 0
        }
        assert tight_states == optimal

        for state in optimal:
            other_vector = vector_from_mask(side, state, universe)
            component_costs = cycle_costs(
                side,
                base_vector,
                other_vector,
                arc_weight,
            )
            assert all(value == 0 for value in component_costs)
            assert costs[state] == minimum

        for state in avoiding:
            other_vector = vector_from_mask(side, state, universe)
            component_costs = cycle_costs(
                side,
                base_vector,
                other_vector,
                arc_weight,
            )
            assert all(value >= 0 for value in component_costs)
            assert sum(component_costs) == costs[state] - minimum


def verify_exhaustive() -> None:
    for side in (2, 3):
        universe = [
            (left, right)
            for left in range(side)
            for right in range(side)
        ]
        positions = {edge: index for index, edge in enumerate(universe)}
        matchings = perfect_matching_masks(side, positions)

        # Ternary edge states enumerate every nested pair G <= G0.
        for code in range(3 ** len(universe)):
            value = code
            final_host = 0
            initial_host = 0
            for bit in range(len(universe)):
                state = value % 3
                value //= 3
                if state >= 1:
                    initial_host |= 1 << bit
                if state == 2:
                    final_host |= 1 << bit
            verify_pair(
                side,
                final_host,
                initial_host,
                universe,
                positions,
                matchings,
            )


def main() -> None:
    verify_exhaustive()
    print(
        "verified rollback optimal face: minimum assignment cost, no-negative-"
        "cycle optimality, zero-cycle decomposition, exact tight matching host, "
        "and integral rollback-level potentials"
    )


if __name__ == "__main__":
    main()
