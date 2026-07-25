#!/usr/bin/env python3
"""Exhaustive binary-cost checks for CMR453--CMR461."""

from __future__ import annotations

from collections import defaultdict
from itertools import permutations, product

Edge = tuple[int, int]


def strongly_connected_components(
    side: int, arcs: set[Edge]
) -> tuple[list[int], list[list[int]]]:
    adjacency = [[] for _ in range(side)]
    reverse = [[] for _ in range(side)]
    for source, target in arcs:
        adjacency[source].append(target)
        reverse[target].append(source)

    seen = [False] * side
    order: list[int] = []

    def visit(vertex: int) -> None:
        seen[vertex] = True
        for next_vertex in adjacency[vertex]:
            if not seen[next_vertex]:
                visit(next_vertex)
        order.append(vertex)

    for vertex in range(side):
        if not seen[vertex]:
            visit(vertex)

    component = [-1] * side

    def assign(vertex: int, label: int) -> None:
        component[vertex] = label
        for next_vertex in reverse[vertex]:
            if component[next_vertex] < 0:
                assign(next_vertex, label)

    label = 0
    for vertex in reversed(order):
        if component[vertex] < 0:
            assign(vertex, label)
            label += 1

    groups = [[] for _ in range(label)]
    for vertex, group in enumerate(component):
        groups[group].append(vertex)
    return component, groups


def shortest_levels(
    vertices: list[int],
    arcs: set[Edge],
    weights: dict[Edge, int],
) -> dict[int, int]:
    distance = {vertex: 0 for vertex in vertices}
    vertex_set = set(vertices)
    for _ in range(max(0, len(vertices) - 1)):
        changed = False
        for source, target in arcs:
            if source not in vertex_set or target not in vertex_set:
                continue
            candidate = distance[source] + weights[(source, target)]
            if candidate < distance[target]:
                distance[target] = candidate
                changed = True
        if not changed:
            break
    return distance


def verify_instance(side: int, edge_states: tuple[int, ...]) -> bool:
    universe = [
        (left, right)
        for left in range(side)
        for right in range(side)
    ]
    host = {
        universe[index]
        for index, state in enumerate(edge_states)
        if state != 0
    }
    cost = {
        universe[index]: state - 1
        for index, state in enumerate(edge_states)
        if state != 0
    }

    all_states = list(permutations(range(side)))
    feasible = [
        state
        for state in all_states
        if all((left, state[left]) in host for left in range(side))
    ]
    if not feasible:
        return False

    state_cost = {
        state: sum(cost[(left, state[left])] for left in range(side))
        for state in feasible
    }
    optimum = min(state_cost.values())
    optimal = {
        state for state, value in state_cost.items() if value == optimum
    }
    base = min(optimal)
    inverse = {right: left for left, right in enumerate(base)}

    arc_weight: dict[Edge, int] = {}
    for left, right in host:
        if right == base[left]:
            continue
        target = inverse[right]
        arc_weight[(left, target)] = (
            cost[(left, right)] - cost[(target, base[target])]
        )

    all_arcs = set(arc_weight)
    distance = shortest_levels(list(range(side)), all_arcs, arc_weight)

    assert all(-optimum <= value <= 0 for value in distance.values())
    level_sizes: dict[int, int] = defaultdict(int)
    for value in distance.values():
        level_sizes[value] += 1
    assert max(level_sizes.values()) >= (
        side + optimum
    ) // (optimum + 1)

    tight = {
        (source, target)
        for (source, target), weight in arc_weight.items()
        if weight + distance[source] - distance[target] == 0
    }
    component, groups = strongly_connected_components(side, tight)

    allowed = {
        (left, state[left])
        for state in optimal
        for left in range(side)
    }

    for left, right in host:
        if right == base[left]:
            continue
        target = inverse[right]
        predicted_allowed = (
            (left, target) in tight
            and component[left] == component[target]
        )
        assert ((left, right) in allowed) == predicted_allowed

    for vertex in range(side):
        forced = all(state[vertex] == base[vertex] for state in optimal)
        assert forced == (len(groups[component[vertex]]) == 1)

    allowed_states = {
        state
        for state in all_states
        if all((left, state[left]) in allowed for left in range(side))
    }
    assert allowed_states == optimal

    product_count = 1
    active_components: list[tuple[list[int], int, dict[int, int]]] = []
    active_vertices = 0
    local_cost_sum = 0
    local_level_count = 0

    for group in groups:
        local_cost = sum(cost[(vertex, base[vertex])] for vertex in group)
        local_cost_sum += local_cost
        local_states: list[tuple[int, ...]] = []

        for target_order in permutations(group):
            if all(
                (left, base[target_order[position]]) in allowed
                for position, left in enumerate(group)
            ):
                local_states.append(target_order)

        assert local_states
        product_count *= len(local_states)

        for target_order in local_states:
            candidate_cost = sum(
                cost[(left, base[target_order[position]])]
                for position, left in enumerate(group)
            )
            assert candidate_cost == local_cost

        if local_cost == 0:
            assert all(
                cost[edge] == 0
                for edge in allowed
                if edge[0] in group
            )
            continue

        active_vertices += len(group)
        local_distance = shortest_levels(group, tight, arc_weight)
        assert all(
            -local_cost <= value <= 0
            for value in local_distance.values()
        )
        local_level_count += len(set(local_distance.values()))
        active_components.append((group, local_cost, local_distance))

    assert product_count == len(optimal)
    assert local_cost_sum == optimum
    assert len(active_components) <= optimum

    if optimum == 0:
        assert not active_components
    else:
        assert local_level_count <= 2 * optimum
        if active_vertices:
            maximum_active_level = 0
            for group, _local_cost, local_distance in active_components:
                counts: dict[int, int] = defaultdict(int)
                for vertex in group:
                    counts[local_distance[vertex]] += 1
                maximum_active_level = max(
                    maximum_active_level,
                    max(counts.values()),
                )
            assert maximum_active_level >= (
                active_vertices + 2 * optimum - 1
            ) // (2 * optimum)

    for threshold in range(2, side + 1):
        free_large = any(
            sum(cost[(vertex, base[vertex])] for vertex in group) == 0
            and len(group) >= threshold
            for group in groups
        )
        if free_large:
            continue

        if active_vertices < threshold:
            assert all(len(group) < threshold for group in groups)
            continue

        assert optimum > 0
        maximum_active_level = 0
        for group, _local_cost, local_distance in active_components:
            counts: dict[int, int] = defaultdict(int)
            for vertex in group:
                counts[local_distance[vertex]] += 1
            maximum_active_level = max(
                maximum_active_level,
                max(counts.values()),
            )
        assert maximum_active_level >= (
            threshold + 2 * optimum - 1
        ) // (2 * optimum)

    return True


def main() -> None:
    checked: dict[int, int] = {}
    for side in (1, 2, 3):
        count = 0
        for edge_states in product(range(3), repeat=side * side):
            if verify_instance(side, edge_states):
                count += 1
        checked[side] = count

    assert checked == {1: 2, 2: 56, 3: 15632}
    print(
        "verified tight rollback SCC structure: optimum-sensitive levels, "
        "optimal-allowed cycle edges, exact component products, additive "
        "local rollback cost, active-level concentration, and arbitrary "
        "binary marked costs"
    )


if __name__ == "__main__":
    main()
