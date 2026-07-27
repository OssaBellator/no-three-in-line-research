#!/usr/bin/env python3
"""Audit combined orientation-flip and three-edge flaw-targeted Hamilton repair."""
from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, product
from pathlib import Path
from typing import Any

Point = tuple[int, int]
State = tuple[tuple[int, ...], tuple[int, ...]]


def hamilton_cycles(m: int):
    for tail in permutations(range(1, m)):
        order = (0,) + tail
        rho = [0] * m
        for index, source in enumerate(order):
            rho[source] = order[(index + 1) % m]
        yield tuple(rho)


def state_points(
    m: int, rho: tuple[int, ...], orientations: tuple[int, ...]
) -> tuple[set[Point], dict[Point, int]]:
    n = 2 * m

    def reversal(x: int) -> int:
        return n - 1 - x

    sigma = [0] * n
    points: set[Point] = set()
    owners: dict[Point, int] = {}
    for source in range(m):
        for bit, column in ((0, source), (1, reversal(source))):
            row = (
                rho[source]
                if (bit ^ orientations[source]) == 0
                else reversal(rho[source])
            )
            sigma[column] = row
            point = (column, row)
            points.add(point)
            owners[point] = source

    for source in range(m):
        for column in (source, reversal(source)):
            row = sigma[column]
            point = (reversal(row), column)
            points.add(point)
            owners[point] = source

    if len(points) != 4 * m:
        raise ValueError("signed Hamilton state is not edge-disjoint")
    return points, owners


def normal_line(a: Point, b: Point) -> tuple[int, int, int]:
    x1, y1 = a
    x2, y2 = b
    A = y2 - y1
    B = x1 - x2
    C = -(A * x1 + B * y1)
    divisor = math.gcd(math.gcd(abs(A), abs(B)), abs(C))
    A //= divisor
    B //= divisor
    C //= divisor
    if A < 0 or (A == 0 and B < 0):
        A, B, C = -A, -B, -C
    return A, B, C


def defects(
    points: set[Point], owners: dict[Point, int]
) -> tuple[int, list[tuple[int, ...]], int]:
    lines: dict[tuple[int, int, int], set[Point]] = defaultdict(set)
    for a, b in combinations(sorted(points), 2):
        lines[normal_line(a, b)].update((a, b))

    triple_count = 0
    owner_sets: list[tuple[int, ...]] = []
    maximum_owner_line_load = 0
    for cells in lines.values():
        if len(cells) < 3:
            continue
        owner_load = Counter(owners[point] for point in cells)
        maximum_owner_line_load = max(maximum_owner_line_load, max(owner_load.values()))
        for triple in combinations(sorted(cells), 3):
            triple_count += 1
            owner_sets.append(tuple(sorted({owners[point] for point in triple})))
    return triple_count, owner_sets, maximum_owner_line_load


def switch_rho(
    rho: tuple[int, ...], sources: tuple[int, int, int]
) -> tuple[int, ...]:
    selected = set(sources)
    start = min(selected)
    cyclic: list[int] = []
    current = start
    for _ in range(len(rho)):
        if current in selected:
            cyclic.append(current)
        current = rho[current]
    if len(cyclic) != 3:
        raise ValueError("source triple not found on cycle")

    a1, a2, a3 = cyclic
    b1, b2, b3 = rho[a1], rho[a2], rho[a3]
    changed = list(rho)
    changed[a1], changed[a2], changed[a3] = b2, b3, b1
    return tuple(changed)


def audit_case(m: int) -> dict[str, Any]:
    states: list[State] = []
    index: dict[State, int] = {}
    triples: list[int] = []
    owner_sets_by_state: list[list[tuple[int, ...]]] = []
    maximum_owner_line_load = 0

    for rho in hamilton_cycles(m):
        for orientations in product((0, 1), repeat=m):
            state = (rho, tuple(orientations))
            index[state] = len(states)
            states.append(state)
            points, owners = state_points(m, rho, tuple(orientations))
            count, owner_sets, owner_line_load = defects(points, owners)
            triples.append(count)
            owner_sets_by_state.append(owner_sets)
            maximum_owner_line_load = max(maximum_owner_line_load, owner_line_load)

    adjacency: list[set[int]] = [set() for _ in states]
    occurrences = Counter()
    defective_states = 0
    only_two_owner_states = 0

    for state_index, ((rho, orientations), count, owner_sets) in enumerate(
        zip(states, triples, owner_sets_by_state)
    ):
        if count:
            defective_states += 1
        if count and all(len(owner_set) == 2 for owner_set in owner_sets):
            only_two_owner_states += 1

        for owner_set in owner_sets:
            occurrences[len(owner_set)] += 1

        for owner_set in set(owner_sets):
            if len(owner_set) == 2:
                for source in owner_set:
                    changed = list(orientations)
                    changed[source] ^= 1
                    adjacency[state_index].add(index[(rho, tuple(changed))])
            elif len(owner_set) == 3:
                changed_rho = switch_rho(rho, owner_set)
                for bits in product((0, 1), repeat=3):
                    changed = list(orientations)
                    for source, bit in zip(owner_set, bits):
                        changed[source] = bit
                    adjacency[state_index].add(index[(changed_rho, tuple(changed))])
            else:
                raise ValueError("bad triple has impossible owner count")

    global_minimum = min(triples)
    targets = [index for index, count in enumerate(triples) if count == global_minimum]
    reverse: list[list[int]] = [[] for _ in states]
    for source, neighbours in enumerate(adjacency):
        for target in neighbours:
            reverse[target].append(source)

    distance: list[int | None] = [None] * len(states)
    queue: deque[int] = deque(targets)
    for target in targets:
        distance[target] = 0
    while queue:
        target = queue.popleft()
        assert distance[target] is not None
        for source in reverse[target]:
            if distance[source] is None:
                distance[source] = distance[target] + 1
                queue.append(source)

    local_minimum_distances: list[int] = []
    local_minima_including_global = 0
    for source, neighbours in enumerate(adjacency):
        if all(triples[target] >= triples[source] for target in neighbours):
            local_minima_including_global += 1
            if triples[source] > global_minimum:
                if distance[source] is None:
                    raise ValueError("nonminimal local minimum cannot reach global minimum")
                local_minimum_distances.append(distance[source])

    if any(distance_value is None for distance_value in distance):
        maximum_distance: int | None = None
    else:
        maximum_distance = max(int(value) for value in distance if value is not None)

    return {
        "m": m,
        "states": len(states),
        "defective_states": defective_states,
        "global_minimum_triples": global_minimum,
        "global_minimum_states": len(targets),
        "bad_triple_occurrences_by_owner_count": {
            "2": occurrences[2],
            "3": occurrences[3],
        },
        "states_with_defects_but_no_three_owner_triple": only_two_owner_states,
        "maximum_points_from_one_owner_on_a_bad_line": maximum_owner_line_load,
        "unique_directed_flaw_targeted_edges": sum(map(len, adjacency)),
        "states_with_no_legal_flaw_targeted_move": sum(
            triples[index] > 0 and not neighbours
            for index, neighbours in enumerate(adjacency)
        ),
        "all_states_reach_global_minimum": all(value is not None for value in distance),
        "maximum_distance_to_global_minimum": maximum_distance,
        "distance_distribution": {
            str(key): value for key, value in sorted(Counter(distance).items())
        },
        "one_step_local_minima_including_global_minima": local_minima_including_global,
        "nonminimal_one_step_local_minima": len(local_minimum_distances),
        "nonminimal_local_minimum_distance_distribution": {
            str(key): value
            for key, value in sorted(Counter(local_minimum_distances).items())
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audit", type=Path)
    args = parser.parse_args()

    try:
        expected = json.loads(args.audit.read_text())
        minimum = expected.get("minimum_pair_size")
        maximum = expected.get("maximum_pair_size")
        if (
            isinstance(minimum, bool)
            or not isinstance(minimum, int)
            or isinstance(maximum, bool)
            or not isinstance(maximum, int)
            or minimum < 4
            or maximum < minimum
        ):
            raise ValueError("invalid pair-size range")

        result = {
            "minimum_pair_size": minimum,
            "maximum_pair_size": maximum,
            "cases": [audit_case(m) for m in range(minimum, maximum + 1)],
            "asymptotic_seed_theorem_proved": False,
        }
        if result != expected:
            raise ValueError("stored combined-repair reachability ledger mismatch")
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
