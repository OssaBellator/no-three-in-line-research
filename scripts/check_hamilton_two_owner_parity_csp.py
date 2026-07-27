#!/usr/bin/env python3
"""Audit the two-owner orientation subsystem as a signed-graph parity CSP."""
from __future__ import annotations

import argparse
import json
from collections import Counter, deque
from itertools import combinations, permutations
from pathlib import Path
from typing import Any

Point = tuple[int, int]


def hamilton_cycles(m: int):
    for tail in permutations(range(1, m)):
        order = (0,) + tail
        rho = [0] * m
        for index, source in enumerate(order):
            rho[source] = order[(index + 1) % m]
        yield tuple(rho)


def orbit_block(m: int, source: int, target: int, orientation: int) -> set[Point]:
    n = 2 * m

    def reversal(x: int) -> int:
        return n - 1 - x

    sigma = [
        (source, reversal(target) if orientation else target),
        (reversal(source), target if orientation else reversal(target)),
    ]
    return set(sigma + [(reversal(row), column) for column, row in sigma])


def collinear(a: Point, b: Point, c: Point) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (
        b[1] - a[1]
    ) * (c[0] - a[0])


def two_owner_bad(
    m: int,
    source_a: int,
    target_a: int,
    orientation_a: int,
    source_b: int,
    target_b: int,
    orientation_b: int,
) -> bool:
    points = list(orbit_block(m, source_a, target_a, orientation_a))
    points += list(orbit_block(m, source_b, target_b, orientation_b))
    return any(collinear(*triple) for triple in combinations(points, 3))


def analyse_case(m: int) -> dict[str, Any]:
    cycle_count = 0
    required_zero = 0
    required_one = 0
    pairs_forbidding_both = 0
    satisfiable_cycles = 0
    unsatisfiable_cycles = 0
    total_clean_orientations = 0
    clean_distribution: Counter[int] = Counter()
    minimum_constraints = 10**9
    maximum_constraints = 0

    for rho in hamilton_cycles(m):
        cycle_count += 1
        adjacency: list[list[tuple[int, int]]] = [[] for _ in range(m)]
        inconsistent = False
        constraint_count = 0

        for source_a in range(m):
            for source_b in range(source_a + 1, m):
                bad: dict[tuple[int, int], bool] = {}
                for orientation_a in (0, 1):
                    for orientation_b in (0, 1):
                        bad[(orientation_a, orientation_b)] = two_owner_bad(
                            m,
                            source_a,
                            rho[source_a],
                            orientation_a,
                            source_b,
                            rho[source_b],
                            orientation_b,
                        )

                if bad[(0, 0)] != bad[(1, 1)] or bad[(0, 1)] != bad[(1, 0)]:
                    raise ValueError("simultaneous-complement invariance failed")

                forbidden_xor = {value for value in (0, 1) if bad[(0, value)]}
                if len(forbidden_xor) == 2:
                    pairs_forbidding_both += 1
                    inconsistent = True
                elif len(forbidden_xor) == 1:
                    required = 1 - next(iter(forbidden_xor))
                    constraint_count += 1
                    if required == 0:
                        required_zero += 1
                    else:
                        required_one += 1
                    adjacency[source_a].append((source_b, required))
                    adjacency[source_b].append((source_a, required))

        minimum_constraints = min(minimum_constraints, constraint_count)
        maximum_constraints = max(maximum_constraints, constraint_count)

        colour: list[int | None] = [None] * m
        components = 0
        if not inconsistent:
            for root in range(m):
                if colour[root] is not None:
                    continue
                components += 1
                colour[root] = 0
                queue: deque[int] = deque([root])
                while queue and not inconsistent:
                    source = queue.popleft()
                    assert colour[source] is not None
                    for target, parity in adjacency[source]:
                        required_colour = colour[source] ^ parity
                        if colour[target] is None:
                            colour[target] = required_colour
                            queue.append(target)
                        elif colour[target] != required_colour:
                            inconsistent = True
                            break

        clean = 0 if inconsistent else 1 << components
        if clean:
            satisfiable_cycles += 1
        else:
            unsatisfiable_cycles += 1
        total_clean_orientations += clean
        clean_distribution[clean] += 1

    return {
        "m": m,
        "hamilton_cycles": cycle_count,
        "pair_constraints_total": required_zero + required_one,
        "required_xor_zero_constraints": required_zero,
        "required_xor_one_constraints": required_one,
        "owner_pairs_forbidding_both_xor_values": pairs_forbidding_both,
        "cycles_with_satisfiable_two_owner_system": satisfiable_cycles,
        "cycles_with_unsatisfiable_two_owner_system": unsatisfiable_cycles,
        "two_owner_clean_orientation_vectors_total": total_clean_orientations,
        "clean_orientation_count_distribution": {
            str(key): value for key, value in sorted(clean_distribution.items())
        },
        "minimum_constraints_on_one_cycle": minimum_constraints,
        "maximum_constraints_on_one_cycle": maximum_constraints,
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
            "simultaneous_orientation_complement_preserves_two_owner_flaws": True,
            "asymptotic_seed_theorem_proved": False,
        }
        if result != expected:
            raise ValueError("stored parity-CSP ledger mismatch")
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
