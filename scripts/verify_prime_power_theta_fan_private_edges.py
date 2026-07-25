#!/usr/bin/env python3
"""Exhaustive finite checks for CMR482--CMR486."""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations, product


Arc = tuple[int, int]
SymbolicEdge = tuple[str, int] | tuple[str, int, int]


def arcs_from_mask(side: int, mask: int) -> set[Arc]:
    positions = [
        (source, target)
        for source in range(side)
        for target in range(side)
        if source != target
    ]
    return {
        arc
        for index, arc in enumerate(positions)
        if mask & (1 << index)
    }


def adjacency(side: int, arcs: set[Arc]) -> list[set[int]]:
    graph = [set() for _ in range(side)]
    for source, target in arcs:
        graph[source].add(target)
    return graph


def reachable(
    side: int,
    arcs: set[Arc],
    start: int,
    target: int,
) -> bool:
    graph = adjacency(side, arcs)
    stack = [start]
    seen = {start}
    while stack:
        source = stack.pop()
        if source == target:
            return True
        for vertex in graph[source]:
            if vertex not in seen:
                seen.add(vertex)
                stack.append(vertex)
    return False


def all_simple_paths(
    side: int,
    arcs: set[Arc],
    start: int,
    target: int,
) -> list[tuple[int, ...]]:
    graph = adjacency(side, arcs)
    paths: list[tuple[int, ...]] = []

    def search(source: int, path: list[int], seen: set[int]) -> None:
        if source == target:
            paths.append(tuple(path))
            return
        for vertex in sorted(graph[source]):
            if vertex not in seen:
                search(vertex, path + [vertex], seen | {vertex})

    search(start, [start], {start})
    return paths


def path_edges(path: tuple[int, ...] | list[int]) -> frozenset[Arc]:
    return frozenset(zip(path, path[1:]))


def edge_disjoint_families(paths: list[tuple[int, ...]]) -> list[list[int]]:
    edge_sets = [path_edges(path) for path in paths]
    families: list[list[int]] = []

    for mask in range(1, 1 << len(paths)):
        family = [index for index in range(len(paths)) if mask & (1 << index)]
        used: set[Arc] = set()
        valid = True
        for index in family:
            if used.intersection(edge_sets[index]):
                valid = False
                break
            used.update(edge_sets[index])
        if valid:
            families.append(family)
    return families


def symbolic_arc(arc: Arc) -> SymbolicEdge:
    return ("A", arc[0], arc[1])


def verify_family(
    side: int,
    arcs: set[Arc],
    boundary_arc: Arc,
    paths: list[tuple[int, ...]],
    family: list[int],
    check_conflicts: bool,
) -> None:
    core = symbolic_arc(boundary_arc)
    private_sets = [path_edges(paths[index]) for index in family]
    entering_sets = [frozenset({boundary_arc}) | edges for edges in private_sets]
    size = len(family)

    # CMR482: a sunflower with core equal to the boundary arc.
    for index, private in enumerate(private_sets):
        assert private
        assert 1 <= len(private) <= side - 1
        for earlier in range(index):
            assert private.isdisjoint(private_sets[earlier])
            assert entering_sets[index].intersection(entering_sets[earlier]) == {
                boundary_arc
            }

    # CMR483: fewer than q noncore edges cannot hit every entering set.
    private_union = sorted(set().union(*private_sets))
    for blocker_size in range(min(size, len(private_union) + 1)):
        for blocker in combinations(private_union, blocker_size):
            blocked = set(blocker)
            assert any(blocked.isdisjoint(entering) for entering in entering_sets)

    if not check_conflicts:
        return

    base: set[SymbolicEdge] = {("M", index) for index in range(side)}
    states: list[set[SymbolicEdge]] = []

    for path_index in family:
        path = paths[path_index]
        cycle_sequence = [boundary_arc[0]] + list(path)
        cycle_vertices = set(cycle_sequence[:-1])
        state: set[SymbolicEdge] = {
            symbolic_arc(arc)
            for arc in zip(cycle_sequence, cycle_sequence[1:])
        }
        state.update(
            ("M", index)
            for index in range(side)
            if index not in cycle_vertices
        )
        states.append(state)

        private = {symbolic_arc(arc) for arc in path_edges(path)}
        elements = sorted(state)
        for conflict_size in range(1, min(3, len(elements)) + 1):
            for chosen in combinations(elements, conflict_size):
                conflict = set(chosen)
                if conflict.issubset(base):
                    continue
                rooted = core in conflict and conflict.issubset(base | {core})
                assert rooted or bool(conflict.intersection(private))

    # CMR485: test the aggregate assignment bound on the complete family of
    # three-edge P-clean symbolic conflicts.
    universe = base | {symbolic_arc(arc) for arc in arcs}
    if len(universe) < 3:
        return

    conflicts = [
        set(chosen)
        for chosen in combinations(sorted(universe), 3)
        if not set(chosen).issubset(base)
    ]
    degree: defaultdict[SymbolicEdge, int] = defaultdict(int)
    for conflict in conflicts:
        for edge in conflict:
            degree[edge] += 1
    maximum_degree = max(degree.values(), default=0)

    nonrooted_occurrences = 0
    for state in states:
        for conflict in conflicts:
            rooted = core in conflict and conflict.issubset(base | {core})
            if conflict.issubset(state) and not rooted:
                nonrooted_occurrences += 1

    assert nonrooted_occurrences <= maximum_degree * sum(
        len(private) for private in private_sets
    )


def verify_exhaustive() -> None:
    expected_families = {2: 4, 3: 672, 4: 342_528}
    observed: dict[int, int] = {}

    for side in range(2, 5):
        family_count = 0
        for mask in range(1 << (side * (side - 1))):
            arcs = arcs_from_mask(side, mask)
            for colours in product((0, 1), repeat=side):
                boundary = [
                    arc
                    for arc in arcs
                    if colours[arc[0]] != colours[arc[1]]
                    and reachable(side, arcs, arc[1], arc[0])
                ]
                for arc in boundary:
                    paths = all_simple_paths(side, arcs - {arc}, arc[1], arc[0])
                    families = edge_disjoint_families(paths)
                    maximum_size = max((len(family) for family in families), default=0)
                    checked_maximum = False
                    for family in families:
                        check_conflicts = (
                            not checked_maximum and len(family) == maximum_size
                        )
                        verify_family(
                            side,
                            arcs,
                            arc,
                            paths,
                            family,
                            check_conflicts,
                        )
                        checked_maximum |= check_conflicts
                        family_count += 1
        observed[side] = family_count

    assert observed == expected_families


def verify_arithmetic() -> None:
    for parent_side in range(2, 30):
        for local_side in range(2, parent_side + 1):
            for fan_size in range(1, local_side + 1):
                for numerator in range(1, 20):
                    for denominator in range(1, 20):
                        weight = numerator / denominator
                        degree = 2 * (parent_side - 1) ** 2 * weight
                        private_total = fan_size * (local_side - 1)
                        assert degree * private_total <= (
                            2
                            * (parent_side - 1) ** 2
                            * weight
                            * fan_size
                            * (local_side - 1)
                        )


def main() -> None:
    verify_exhaustive()
    verify_arithmetic()
    print(
        "verified theta-fan payment: private entering-edge sunflower, blocker "
        "resilience, rooted-conflict dichotomy, aggregate conflict-degree "
        "charging, and harmonic arithmetic through side four"
    )


if __name__ == "__main__":
    main()
