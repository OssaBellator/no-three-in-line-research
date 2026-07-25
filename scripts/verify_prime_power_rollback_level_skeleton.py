#!/usr/bin/env python3
"""Exhaustive checks for CMR462--CMR466."""

from __future__ import annotations

from collections import defaultdict
from itertools import permutations, product

Edge = tuple[int, int]


def shortest_levels(
    side: int,
    arcs: dict[Edge, int],
) -> list[int]:
    distance = [0] * side
    for _ in range(max(0, side - 1)):
        changed = False
        for (source, target), weight in arcs.items():
            candidate = distance[source] + weight
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
    for edge in host:
        left, right = edge
        if right == base[left]:
            continue
        target = inverse[right]
        arc = (left, target)
        arc_weight[arc] = cost[edge] - cost[(target, base[target])]

    level = shortest_levels(side, arc_weight)
    tight_arcs = {
        arc
        for arc, weight in arc_weight.items()
        if weight + level[arc[0]] - level[arc[1]] == 0
    }

    allowed = {
        (left, state[left])
        for state in optimal
        for left in range(side)
    }

    level_vertices: dict[int, set[int]] = defaultdict(set)
    for vertex, value in enumerate(level):
        level_vertices[value].add(vertex)

    reconstructed: set[tuple[int, ...]] = set()
    skeletons: set[frozenset[Edge]] = set()

    for state in optimal:
        permutation = tuple(inverse[state[left]] for left in range(side))
        up_by_cut: dict[int, int] = defaultdict(int)
        down_by_cut: dict[int, int] = defaultdict(int)
        skeleton: set[Edge] = set()

        for source, target in enumerate(permutation):
            delta = level[target] - level[source]
            assert delta in (-1, 0, 1)
            if delta == 1:
                up_by_cut[level[source]] += 1
                skeleton.add((source, target))
                edge = (source, base[target])
                assert cost[edge] == 1
                assert cost[(target, base[target])] == 0
            elif delta == -1:
                down_by_cut[level[target]] += 1
                skeleton.add((source, target))
                edge = (source, base[target])
                assert cost[edge] == 0
                assert cost[(target, base[target])] == 1

        assert up_by_cut == down_by_cut
        upward = sum(up_by_cut.values())
        downward = sum(down_by_cut.values())
        assert upward == downward <= optimum
        assert len(skeleton) == upward + downward <= 2 * optimum
        skeletons.add(frozenset(skeleton))

        outgoing: dict[int, set[int]] = defaultdict(set)
        incoming: dict[int, set[int]] = defaultdict(set)
        for source, target in skeleton:
            outgoing[level[source]].add(source)
            incoming[level[target]].add(target)

        for value, vertices in level_vertices.items():
            assert len(outgoing[value]) == len(incoming[value])
            residual_sources = vertices - outgoing[value]
            residual_targets = vertices - incoming[value]
            mapped_targets = {
                permutation[source]
                for source in residual_sources
            }
            assert mapped_targets == residual_targets
            assert all(
                level[permutation[source]] == value
                for source in residual_sources
            )

    # Reconstruct every optimum from its skeleton and independent level matchings.
    for skeleton in skeletons:
        outgoing: dict[int, set[int]] = defaultdict(set)
        incoming: dict[int, set[int]] = defaultdict(set)
        fixed_target: dict[int, int] = {}
        used_targets: set[int] = set()
        for source, target in skeleton:
            assert (source, target) in tight_arcs
            fixed_target[source] = target
            used_targets.add(target)
            outgoing[level[source]].add(source)
            incoming[level[target]].add(target)

        assert len(fixed_target) == len(used_targets)
        local_options: list[list[dict[int, int]]] = []
        for value, vertices in sorted(level_vertices.items()):
            sources = sorted(vertices - outgoing[value])
            targets = sorted(vertices - incoming[value])
            assert len(sources) == len(targets)
            options: list[dict[int, int]] = []
            for target_order in permutations(targets):
                candidate = dict(zip(sources, target_order))
                good = True
                for source, target in candidate.items():
                    edge = (source, base[target])
                    if edge not in allowed or level[source] != level[target]:
                        good = False
                        break
                if good:
                    options.append(candidate)
            assert options
            local_options.append(options)

        for choices in product(*local_options):
            permutation_map = dict(fixed_target)
            for choice in choices:
                permutation_map.update(choice)
            assert len(permutation_map) == side
            state = tuple(base[permutation_map[left]] for left in range(side))
            reconstructed.add(state)

    assert reconstructed == optimal
    assert len(skeletons) <= sum(side ** (4 * u) for u in range(optimum + 1))
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
        "verified rollback level skeletons: exact cut balance, at most 2k "
        "cross-level edges, balanced residual levels, exact conditional "
        "factorization, and finite skeleton count"
    )


if __name__ == "__main__":
    main()
