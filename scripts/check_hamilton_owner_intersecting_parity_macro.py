#!/usr/bin/env python3
"""Audit owner-intersecting parity-clean Hamilton rotations through a stored range."""
from __future__ import annotations

import argparse
import json
import math
from collections import Counter, deque
from itertools import combinations
from pathlib import Path
from typing import Any

from check_hamilton_two_owner_parity_csp import hamilton_cycles, two_owner_bad


def pair_predicates(m: int) -> dict[tuple[int, int, int, int], int]:
    """Return -1=no constraint, 0/1=required XOR, 2=both XOR values forbidden."""
    result: dict[tuple[int, int, int, int], int] = {}
    for source_a in range(m):
        for source_b in range(source_a + 1, m):
            for target_a in range(m):
                if target_a == source_a:
                    continue
                for target_b in range(m):
                    if target_b == source_b or target_b == target_a:
                        continue
                    bad_equal = two_owner_bad(
                        m, source_a, target_a, 0, source_b, target_b, 0
                    )
                    bad_unequal = two_owner_bad(
                        m, source_a, target_a, 0, source_b, target_b, 1
                    )
                    value = (
                        2
                        if bad_equal and bad_unequal
                        else 1
                        if bad_equal
                        else 0
                        if bad_unequal
                        else -1
                    )
                    result[(source_a, target_a, source_b, target_b)] = value
    return result


def parity_details(
    m: int,
    rho: tuple[int, ...],
    predicates: dict[tuple[int, int, int, int], int],
) -> tuple[bool, dict[tuple[int, int], int], tuple[tuple[int, int], ...]]:
    constraints: dict[tuple[int, int], int] = {}
    impossible: list[tuple[int, int]] = []
    adjacency: list[list[tuple[int, int]]] = [[] for _ in range(m)]

    for source_a in range(m):
        for source_b in range(source_a + 1, m):
            value = predicates[(source_a, rho[source_a], source_b, rho[source_b])]
            if value == 2:
                impossible.append((source_a, source_b))
            elif value >= 0:
                constraints[(source_a, source_b)] = value
                adjacency[source_a].append((source_b, value))
                adjacency[source_b].append((source_a, value))

    inconsistent = bool(impossible)
    colour: list[int | None] = [None] * m
    if not inconsistent:
        for root in range(m):
            if colour[root] is not None:
                continue
            colour[root] = 0
            queue: deque[int] = deque([root])
            while queue and not inconsistent:
                source = queue.popleft()
                assert colour[source] is not None
                for target, parity in adjacency[source]:
                    wanted = colour[source] ^ parity
                    if colour[target] is None:
                        colour[target] = wanted
                        queue.append(target)
                    elif colour[target] != wanted:
                        inconsistent = True
                        break

    return not inconsistent, constraints, tuple(impossible)


def shortest_inconsistent_cycle(
    m: int, constraints: dict[tuple[int, int], int]
) -> int | None:
    edge_list = list(constraints.items())
    adjacency: list[list[tuple[int, int, int]]] = [[] for _ in range(m)]
    for edge_id, ((source, target), parity) in enumerate(edge_list):
        adjacency[source].append((target, parity, edge_id))
        adjacency[target].append((source, parity, edge_id))

    best: int | None = None
    for edge_id, ((start, finish), label) in enumerate(edge_list):
        queue: deque[tuple[int, int, int]] = deque([(start, 0, 0)])
        seen = {(start, 0)}
        while queue:
            source, parity, distance = queue.popleft()
            if source == finish and distance > 0 and parity != label:
                candidate = distance + 1
                best = candidate if best is None else min(best, candidate)
                break
            for target, edge_parity, other_id in adjacency[source]:
                if other_id == edge_id:
                    continue
                state = (target, parity ^ edge_parity)
                if state not in seen:
                    seen.add(state)
                    queue.append((target, parity ^ edge_parity, distance + 1))
    return best


def switch_rho(
    rho: tuple[int, ...], sources: tuple[int, int, int]
) -> tuple[int, ...]:
    selected = set(sources)
    cyclic: list[int] = []
    current = min(selected)
    for _ in range(len(rho)):
        if current in selected:
            cyclic.append(current)
        current = rho[current]
    if len(cyclic) != 3:
        raise ValueError("source triple not found on Hamilton cycle")
    a, b, c = cyclic
    successor_a, successor_b, successor_c = rho[a], rho[b], rho[c]
    changed = list(rho)
    changed[a], changed[b], changed[c] = successor_b, successor_c, successor_a
    return tuple(changed)


def analyse_case(m: int) -> dict[str, Any]:
    predicates = pair_predicates(m)
    cycles = list(hamilton_cycles(m))
    index = {rho: position for position, rho in enumerate(cycles)}
    details = [parity_details(m, rho, predicates) for rho in cycles]
    satisfiable = [entry[0] for entry in details]
    triples = list(combinations(range(m), 3))
    triple_sets = [set(triple) for triple in triples]

    adjacency: list[list[tuple[int, tuple[int, int, int]]]] = [
        [] for _ in cycles
    ]
    transition_types: Counter[tuple[bool, bool]] = Counter()
    changed_counts: Counter[int] = Counter()
    changes_outside_sources = 0

    for source_index, rho in enumerate(cycles):
        before = details[source_index][1]
        for sources in triples:
            target_index = index[switch_rho(rho, sources)]
            adjacency[source_index].append((target_index, sources))
            transition_types[(satisfiable[source_index], satisfiable[target_index])] += 1
            after = details[target_index][1]
            changed = {
                pair
                for pair in set(before) | set(after)
                if before.get(pair) != after.get(pair)
            }
            changed_counts[len(changed)] += 1
            if any(
                pair[0] not in sources and pair[1] not in sources
                for pair in changed
            ):
                changes_outside_sources += 1

    satisfiable_vertices = {
        position for position, value in enumerate(satisfiable) if value
    }
    component_sizes: list[int] = []
    visited: set[int] = set()
    for root in satisfiable_vertices:
        if root in visited:
            continue
        stack = [root]
        visited.add(root)
        size = 0
        while stack:
            source = stack.pop()
            size += 1
            for target, _ in adjacency[source]:
                if target in satisfiable_vertices and target not in visited:
                    visited.add(target)
                    stack.append(target)
        component_sizes.append(size)

    distance = [-1] * len(cycles)
    queue: deque[int] = deque()
    for root in satisfiable_vertices:
        distance[root] = 0
        queue.append(root)
    while queue:
        source = queue.popleft()
        for target, _ in adjacency[source]:
            if distance[target] < 0:
                distance[target] = distance[source] + 1
                queue.append(target)

    satisfiable_degrees: list[int] = []
    owner_intersection_counts: Counter[int] = Counter()
    minimum_owner_intersections = 10**9
    for source in satisfiable_vertices:
        clean_rotations = [
            set(sources)
            for target, sources in adjacency[source]
            if satisfiable[target]
        ]
        satisfiable_degrees.append(len(clean_rotations))
        for owners in triple_sets:
            count = sum(bool(owners & rotation) for rotation in clean_rotations)
            owner_intersection_counts[count] += 1
            minimum_owner_intersections = min(minimum_owner_intersections, count)

    unsatisfiable_reasons: Counter[str] = Counter()
    impossible_pair_counts: Counter[int] = Counter()
    shortest_cycle_counts: Counter[int] = Counter()
    for is_satisfiable, constraints, impossible in details:
        if is_satisfiable:
            continue
        if impossible:
            unsatisfiable_reasons["owner_pair_forbids_both_xor_values"] += 1
            impossible_pair_counts[len(impossible)] += 1
        else:
            witness_length = shortest_inconsistent_cycle(m, constraints)
            if witness_length is None:
                raise ValueError("inconsistent signed graph has no witness cycle")
            unsatisfiable_reasons["nonzero_xor_signed_cycle"] += 1
            shortest_cycle_counts[witness_length] += 1

    disjoint_bound = math.comb(m - 3, 3) if m >= 6 else 0
    minimum_degree = min(satisfiable_degrees)
    return {
        "m": m,
        "hamilton_cycles": len(cycles),
        "parity_satisfiable_cycles": len(satisfiable_vertices),
        "parity_unsatisfiable_cycles": len(cycles) - len(satisfiable_vertices),
        "parity_unsatisfiable_reason_counts": dict(sorted(unsatisfiable_reasons.items())),
        "impossible_owner_pair_count_distribution": {
            str(key): value for key, value in sorted(impossible_pair_counts.items())
        },
        "shortest_inconsistent_signed_cycle_distribution": {
            str(key): value for key, value in sorted(shortest_cycle_counts.items())
        },
        "directed_successor_rotations": len(cycles) * len(triples),
        "rotation_transition_counts": {
            "satisfiable_to_satisfiable": transition_types[(True, True)],
            "satisfiable_to_unsatisfiable": transition_types[(True, False)],
            "unsatisfiable_to_satisfiable": transition_types[(False, True)],
            "unsatisfiable_to_unsatisfiable": transition_types[(False, False)],
        },
        "satisfiable_induced_components": len(component_sizes),
        "largest_satisfiable_component": max(component_sizes),
        "minimum_satisfiable_neighbours_from_satisfiable_cycle": minimum_degree,
        "maximum_satisfiable_neighbours_from_satisfiable_cycle": max(
            satisfiable_degrees
        ),
        "maximum_distance_to_satisfiable_cycle": max(distance),
        "distance_to_satisfiable_distribution": {
            str(key): value for key, value in sorted(Counter(distance).items())
        },
        "maximum_disjoint_source_triples_from_owner_triple": disjoint_bound,
        "degree_criterion_margin": minimum_degree - disjoint_bound,
        "minimum_satisfiable_rotations_intersecting_any_owner_triple": (
            minimum_owner_intersections
        ),
        "owner_triple_intersecting_rotation_count_distribution": {
            str(key): value
            for key, value in sorted(owner_intersection_counts.items())
        },
        "changed_constraint_count_distribution": {
            str(key): value for key, value in sorted(changed_counts.items())
        },
        "maximum_changed_parity_constraints": max(changed_counts),
        "changed_constraint_outside_rotated_sources": changes_outside_sources,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audit", type=Path)
    args = parser.parse_args()

    try:
        expected = json.loads(args.audit.read_text(encoding="utf-8"))
        minimum = expected["minimum_pair_size"]
        maximum = expected["maximum_pair_size"]
        result = {
            "minimum_pair_size": minimum,
            "maximum_pair_size": maximum,
            "cases": [analyse_case(m) for m in range(minimum, maximum + 1)],
            "all_parity_clean_owner_triples_have_intersecting_clean_rotation": True,
            "asymptotic_seed_theorem_proved": False,
        }
        if result != expected:
            raise ValueError("stored owner-intersecting parity-macro ledger mismatch")
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
