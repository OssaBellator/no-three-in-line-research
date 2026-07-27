#!/usr/bin/env python3
"""Audit immediate atomic-flaw causality under the combined Hamilton deletion rule."""
from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction
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
            flaws.append(((tuple(sorted(triple)), descriptors), owner_set))
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


def fraction_text(numerator: int, denominator: int) -> str:
    value = Fraction(numerator, denominator)
    return (
        str(value.numerator)
        if value.denominator == 1
        else f"{value.numerator}/{value.denominator}"
    )


def audit_case(m: int) -> dict[str, Any]:
    states: list[State] = []
    index: dict[State, int] = {}
    state_flaw_keys: list[set[tuple[FlawKey, tuple[int, ...]]]] = []
    flaw_inputs: dict[tuple[FlawKey, tuple[int, ...]], list[State]] = defaultdict(list)

    for rho in hamilton_cycles(m):
        for orientations in product((0, 1), repeat=m):
            state = (rho, tuple(orientations))
            index[state] = len(states)
            states.append(state)
            flaws = {
                (key, owner_set)
                for key, owner_set in atomic_flaws(m, rho, tuple(orientations))
            }
            state_flaw_keys.append(flaws)
            for flaw in flaws:
                flaw_inputs[flaw].append(state)

    flaw_list = list(flaw_inputs)
    flaw_id = {flaw: index for index, flaw in enumerate(flaw_list)}
    state_flaw_ids = [
        {flaw_id[flaw] for flaw in flaws} for flaws in state_flaw_keys
    ]
    causal: list[set[int]] = [set() for _ in flaw_list]
    transition_counts = Counter()
    new_flaw_sums = Counter()
    maximum_new_flaws = Counter()

    for flaw, input_states in flaw_inputs.items():
        key, owner_set = flaw
        owner_count = len(owner_set)
        source_flaw_id = flaw_id[flaw]
        for rho, orientations in input_states:
            old_flaws = state_flaw_ids[index[(rho, orientations)]]
            outputs: list[State] = []
            if owner_count == 2:
                for source in owner_set:
                    changed = list(orientations)
                    changed[source] ^= 1
                    outputs.append((rho, tuple(changed)))
            elif owner_count == 3:
                changed_rho = switch_rho(rho, owner_set)
                for bits in product((0, 1), repeat=3):
                    changed = list(orientations)
                    for source, bit in zip(owner_set, bits):
                        changed[source] = bit
                    outputs.append((changed_rho, tuple(changed)))
            else:
                raise ValueError("atomic flaw has impossible owner count")

            for output in outputs:
                new_flaws = state_flaw_ids[index[output]] - old_flaws
                causal[source_flaw_id].update(new_flaws)
                transition_counts[owner_count] += 1
                new_flaw_sums[owner_count] += len(new_flaws)
                maximum_new_flaws[owner_count] = max(
                    maximum_new_flaws[owner_count], len(new_flaws)
                )

    outdegrees: dict[int, list[int]] = {2: [], 3: []}
    for flaw, neighbours in zip(flaw_list, causal):
        outdegrees[len(flaw[1])].append(len(neighbours))

    return {
        "m": m,
        "states": len(states),
        "atomic_flaws": len(flaw_list),
        "deletion_transitions_by_owner_count": {
            "2": transition_counts[2],
            "3": transition_counts[3],
        },
        "maximum_new_flaws_in_one_transition": {
            "2": maximum_new_flaws[2],
            "3": maximum_new_flaws[3],
        },
        "mean_new_flaws_per_transition": {
            "2": fraction_text(new_flaw_sums[2], transition_counts[2]),
            "3": fraction_text(new_flaw_sums[3], transition_counts[3]),
        },
        "maximum_immediate_causal_outdegree": {
            "2": max(outdegrees[2]),
            "3": max(outdegrees[3]),
        },
        "mean_immediate_causal_outdegree": {
            "2": fraction_text(sum(outdegrees[2]), len(outdegrees[2])),
            "3": fraction_text(sum(outdegrees[3]), len(outdegrees[3])),
        },
        "total_directed_causal_edges": sum(map(len, causal)),
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
            raise ValueError("stored immediate-causality ledger mismatch")
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
