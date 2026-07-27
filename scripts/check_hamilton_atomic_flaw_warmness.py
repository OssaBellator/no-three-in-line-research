#!/usr/bin/env python3
"""Audit atomic Hamilton flaw probabilities and deletion-image warmness."""
from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from pathlib import Path
from typing import Any

Point = tuple[int, int]
State = tuple[tuple[int, ...], tuple[int, ...]]
FlawKey = tuple[tuple[Point, ...], tuple[tuple[int, int, int], ...]]


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


def atomic_flaws(
    m: int, rho: tuple[int, ...], orientations: tuple[int, ...]
) -> list[tuple[FlawKey, tuple[int, ...]]]:
    points, owners = state_points(m, rho, orientations)
    lines: dict[tuple[int, int, int], set[Point]] = defaultdict(set)
    for a, b in combinations(sorted(points), 2):
        lines[normal_line(a, b)].update((a, b))

    flaws: list[tuple[FlawKey, tuple[int, ...]]] = []
    for cells in lines.values():
        if len(cells) < 3:
            continue
        for triple in combinations(sorted(cells), 3):
            owner_set = tuple(sorted({owners[point] for point in triple}))
            descriptors = tuple(
                (source, rho[source], orientations[source]) for source in owner_set
            )
            key: FlawKey = (tuple(sorted(triple)), descriptors)
            flaws.append((key, owner_set))
    return flaws


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
        raise ValueError("selected sources not found")
    a1, a2, a3 = cyclic
    b1, b2, b3 = rho[a1], rho[a2], rho[a3]
    changed = list(rho)
    changed[a1], changed[a2], changed[a3] = b2, b3, b1
    return tuple(changed)


def audit_case(m: int) -> dict[str, Any]:
    states: list[State] = []
    flaws: dict[tuple[int, FlawKey, tuple[int, ...]], list[State]] = defaultdict(list)
    state_flaw_keys: dict[State, set[FlawKey]] = {}

    for rho in hamilton_cycles(m):
        for orientations in product((0, 1), repeat=m):
            state = (rho, tuple(orientations))
            states.append(state)
            state_flaws = atomic_flaws(m, rho, tuple(orientations))
            state_flaw_keys[state] = {key for key, _ in state_flaws}
            for key, owner_set in state_flaws:
                flaws[(len(owner_set), key, owner_set)].append(state)

    flaw_counts = Counter()
    event_sizes: dict[int, set[int]] = defaultdict(set)
    output_sizes: dict[int, set[int]] = defaultdict(set)
    maximum_multiplicity = Counter()
    all_outputs_outside = True
    all_injective = True

    for (owner_count, key, owner_set), input_states in flaws.items():
        flaw_counts[owner_count] += 1
        event_sizes[owner_count].add(len(input_states))
        outputs: list[State] = []

        if owner_count == 2:
            for rho, orientations in input_states:
                for source in owner_set:
                    changed = list(orientations)
                    changed[source] ^= 1
                    output = (rho, tuple(changed))
                    outputs.append(output)
                    if key in state_flaw_keys[output]:
                        all_outputs_outside = False
        elif owner_count == 3:
            for rho, orientations in input_states:
                changed_rho = switch_rho(rho, owner_set)
                for bits in product((0, 1), repeat=3):
                    changed = list(orientations)
                    for source, bit in zip(owner_set, bits):
                        changed[source] = bit
                    output = (changed_rho, tuple(changed))
                    outputs.append(output)
                    if key in state_flaw_keys[output]:
                        all_outputs_outside = False
        else:
            raise ValueError("atomic flaw has impossible owner count")

        multiplicities = Counter(outputs)
        maximum_multiplicity[owner_count] = max(
            maximum_multiplicity[owner_count], max(multiplicities.values())
        )
        if max(multiplicities.values()) != 1:
            all_injective = False
        output_sizes[owner_count].add(len(multiplicities))

    for owner_count in (2, 3):
        if len(event_sizes[owner_count]) != 1 or len(output_sizes[owner_count]) != 1:
            raise ValueError("nonuniform atomic flaw size or deletion image")

    event_size_2 = next(iter(event_sizes[2]))
    event_size_3 = next(iter(event_sizes[3]))
    expected_event_size_2 = len(states) // (4 * (m - 1) * (m - 2))
    expected_event_size_3 = len(states) // (
        8 * (m - 1) * (m - 2) * (m - 3)
    )
    if event_size_2 != expected_event_size_2:
        raise ValueError("two-owner cylinder size mismatch")
    if event_size_3 != expected_event_size_3:
        raise ValueError("three-owner cylinder size mismatch")

    return {
        "m": m,
        "states": len(states),
        "atomic_flaws": len(flaws),
        "atomic_flaws_by_owner_count": {
            "2": flaw_counts[2],
            "3": flaw_counts[3],
        },
        "event_state_count_by_owner_count": {
            "2": event_size_2,
            "3": event_size_3,
        },
        "deletion_output_count_by_owner_count": {
            "2": next(iter(output_sizes[2])),
            "3": next(iter(output_sizes[3])),
        },
        "maximum_deletion_output_multiplicity": {
            "2": maximum_multiplicity[2],
            "3": maximum_multiplicity[3],
        },
        "all_deletion_outputs_outside_target_flaw": all_outputs_outside,
        "all_labelled_deletion_maps_injective": all_injective,
        "warmness_by_owner_count": {
            "2": 2 * (m - 1) * (m - 2),
            "3": (m - 1) * (m - 2) * (m - 3),
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
            raise ValueError("stored atomic-flaw warmness ledger mismatch")
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
