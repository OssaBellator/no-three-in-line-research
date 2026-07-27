#!/usr/bin/env python3
"""Audit local parity-CSP updates under Hamilton successor rotations."""
from __future__ import annotations

import argparse
import json
import math
from collections import Counter, deque
from itertools import combinations
from pathlib import Path
from typing import Any

from check_hamilton_two_owner_parity_csp import hamilton_cycles, two_owner_bad


def parity_constraints(m: int, rho: tuple[int, ...]) -> tuple[bool, dict[tuple[int, int], int]]:
    constraints: dict[tuple[int, int], int] = {}
    adjacency: list[list[tuple[int, int]]] = [[] for _ in range(m)]
    inconsistent = False

    for source_a in range(m):
        for source_b in range(source_a + 1, m):
            bad_equal = two_owner_bad(
                m, source_a, rho[source_a], 0, source_b, rho[source_b], 0
            )
            bad_unequal = two_owner_bad(
                m, source_a, rho[source_a], 0, source_b, rho[source_b], 1
            )
            if bad_equal and bad_unequal:
                inconsistent = True
            elif bad_equal or bad_unequal:
                required = 1 if bad_equal else 0
                constraints[(source_a, source_b)] = required
                adjacency[source_a].append((source_b, required))
                adjacency[source_b].append((source_a, required))

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

    return not inconsistent, constraints


def switch_rho(rho: tuple[int, ...], sources: tuple[int, int, int]) -> tuple[int, ...]:
    selected = set(sources)
    cyclic: list[int] = []
    current = min(selected)
    for _ in range(len(rho)):
        if current in selected:
            cyclic.append(current)
        current = rho[current]
    if len(cyclic) != 3:
        raise ValueError("source triple not found on Hamilton cycle")
    a1, a2, a3 = cyclic
    b1, b2, b3 = rho[a1], rho[a2], rho[a3]
    changed = list(rho)
    changed[a1], changed[a2], changed[a3] = b2, b3, b1
    return tuple(changed)


def analyse_case(m: int) -> dict[str, Any]:
    cycles = list(hamilton_cycles(m))
    index = {rho: position for position, rho in enumerate(cycles)}
    systems = [parity_constraints(m, rho) for rho in cycles]
    satisfiable = [system[0] for system in systems]
    constraints = [system[1] for system in systems]
    adjacency: list[set[int]] = [set() for _ in cycles]
    transition_types: Counter[tuple[bool, bool]] = Counter()
    changed_counts: Counter[int] = Counter()
    changes_outside_rotated_sources = 0

    for source_index, rho in enumerate(cycles):
        for sources in combinations(range(m), 3):
            target_rho = switch_rho(rho, sources)
            target_index = index[target_rho]
            adjacency[source_index].add(target_index)
            transition_types[(satisfiable[source_index], satisfiable[target_index])] += 1

            before = constraints[source_index]
            after = constraints[target_index]
            changed = {
                pair
                for pair in set(before) | set(after)
                if before.get(pair) != after.get(pair)
            }
            changed_counts[len(changed)] += 1
            if any(pair[0] not in sources and pair[1] not in sources for pair in changed):
                changes_outside_rotated_sources += 1

    satisfiable_vertices = [index for index, value in enumerate(satisfiable) if value]
    satisfiable_adjacency = [
        {target for target in neighbours if satisfiable[target]}
        for neighbours in adjacency
    ]

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
            for target in satisfiable_adjacency[source]:
                if target not in visited:
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
        for target in adjacency[source]:
            if distance[target] < 0:
                distance[target] = distance[source] + 1
                queue.append(target)

    return {
        "m": m,
        "hamilton_cycles": len(cycles),
        "parity_satisfiable_cycles": len(satisfiable_vertices),
        "parity_unsatisfiable_cycles": len(cycles) - len(satisfiable_vertices),
        "directed_successor_rotations": len(cycles) * math.comb(m, 3),
        "rotation_transition_counts": {
            "satisfiable_to_satisfiable": transition_types[(True, True)],
            "satisfiable_to_unsatisfiable": transition_types[(True, False)],
            "unsatisfiable_to_satisfiable": transition_types[(False, True)],
            "unsatisfiable_to_unsatisfiable": transition_types[(False, False)],
        },
        "satisfiable_induced_components": len(component_sizes),
        "largest_satisfiable_component": max(component_sizes),
        "minimum_satisfiable_neighbours_from_satisfiable_cycle": min(
            len(satisfiable_adjacency[index]) for index in satisfiable_vertices
        ),
        "maximum_satisfiable_neighbours_from_satisfiable_cycle": max(
            len(satisfiable_adjacency[index]) for index in satisfiable_vertices
        ),
        "maximum_distance_to_satisfiable_cycle": max(distance),
        "distance_to_satisfiable_distribution": {
            str(key): value for key, value in sorted(Counter(distance).items())
        },
        "changed_constraint_count_distribution": {
            str(key): value for key, value in sorted(changed_counts.items())
        },
        "maximum_changed_parity_constraints": max(changed_counts),
        "changed_constraint_outside_rotated_sources": changes_outside_rotated_sources,
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
            "all_changed_constraints_touch_a_rotated_source": True,
            "asymptotic_seed_theorem_proved": False,
        }
        if result != expected:
            raise ValueError("stored parity-rotation ledger mismatch")
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
