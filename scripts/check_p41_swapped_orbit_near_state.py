#!/usr/bin/env python3
"""Verify the four-line swapped-quarter-turn p=41 near-state."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import combinations
from pathlib import Path
from typing import Any

Point = tuple[int, int]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def cycle_partition(permutation: list[int]) -> list[int]:
    seen = [False] * len(permutation)
    answer: list[int] = []
    for start in range(len(permutation)):
        if seen[start]:
            continue
        current = start
        length = 0
        while not seen[current]:
            seen[current] = True
            length += 1
            current = permutation[current]
        answer.append(length)
    return sorted(answer, reverse=True)


def orbit(source: int, target: int, orientation: int, n: int) -> set[Point]:
    reverse_source = n - 1 - source
    reverse_target = n - 1 - target
    if orientation == 0:
        return {
            (source, target),
            (reverse_source, reverse_target),
            (target, reverse_source),
            (reverse_target, source),
        }
    return {
        (source, reverse_target),
        (reverse_source, target),
        (target, source),
        (reverse_target, reverse_source),
    }


def verify(raw: Any) -> dict[str, Any]:
    if not isinstance(raw, dict) or raw.get("p") != 41:
        raise ValueError("expected one p=41 object")
    n = 40
    m = 20
    pair_permutation = raw.get("pair_permutation")
    orientations = raw.get("pair_orientations")
    if not isinstance(pair_permutation, list) or not isinstance(orientations, list):
        raise ValueError("pair arrays expected")
    if len(pair_permutation) != m or len(orientations) != m:
        raise ValueError("expected twenty pair assignments")
    rho = [value - 1 for value in pair_permutation]
    if sorted(rho) != list(range(m)):
        raise ValueError("pair_permutation is not a one-based permutation")
    if any(value not in (0, 1) for value in orientations):
        raise ValueError("pair orientations must be bits")

    sigma = [-1] * n
    for source, (target, orientation) in enumerate(zip(rho, orientations)):
        sigma[source] = target if orientation == 0 else n - 1 - target
        sigma[n - 1 - source] = n - 1 - sigma[source]
    inverse = [-1] * n
    for column, row in enumerate(sigma):
        inverse[row] = column
    tau = [inverse[n - 1 - column] for column in range(n)]

    expected_sigma = raw.get("sigma")
    expected_tau = raw.get("tau")
    if [value + 1 for value in sigma] != expected_sigma:
        raise ValueError("stored sigma does not match the signed cover")
    if [value + 1 for value in tau] != expected_tau:
        raise ValueError("stored tau does not match the forced second layer")
    if sorted(sigma) != list(range(n)) or sorted(tau) != list(range(n)):
        raise ValueError("a layer is not a permutation")
    if any(left == right for left, right in zip(sigma, tau)):
        raise ValueError("the layers collide")

    selected = {(column, sigma[column]) for column in range(n)}
    selected |= {(column, tau[column]) for column in range(n)}
    if len(selected) != 2 * n:
        raise ValueError("expected eighty distinct selected cells")
    rows = Counter(row for _, row in selected)
    columns = Counter(column for column, _ in selected)
    if any(rows[index] != 2 or columns[index] != 2 for index in range(n)):
        raise ValueError("the selected set is not saturated")

    owner: dict[Point, int] = {}
    for source, (target, orientation) in enumerate(zip(rho, orientations)):
        for point in orbit(source, target, orientation, n):
            if point in owner:
                raise ValueError("duplicate orbit block")
            owner[point] = source
    if set(owner) != selected:
        raise ValueError("orbit reconstruction changed the selected set")

    bad: list[tuple[Point, Point, Point]] = []
    determinant_checks = 0
    for a, b, c in combinations(sorted(selected), 3):
        determinant_checks += 1
        if determinant(a, b, c) == 0:
            bad.append(tuple(sorted((a, b, c))))
    if determinant_checks != 82160:
        raise ValueError("unexpected determinant count")
    expected_bad_raw = raw.get("bad_triples")
    if not isinstance(expected_bad_raw, list):
        raise ValueError("bad_triples list expected")
    expected_bad = {
        tuple(sorted((column - 1, row - 1) for column, row in triple))
        for triple in expected_bad_raw
    }
    if set(bad) != expected_bad or len(bad) != 4:
        raise ValueError("the four stored bad triples do not match")
    owner_multisets = {
        tuple(sorted(owner[point] + 1 for point in triple)) for triple in bad
    }
    if owner_multisets != {(15, 18, 20)}:
        raise ValueError("bad-line owner set changed")

    pair_cycles: list[tuple[int, int]] = []
    seen = [False] * m
    for start in range(m):
        if seen[start]:
            continue
        cycle: list[int] = []
        current = start
        while not seen[current]:
            seen[current] = True
            cycle.append(current)
            current = rho[current]
        pair_cycles.append((len(cycle), sum(orientations[index] for index in cycle) % 2))
    pair_cycles.sort(reverse=True)
    if [length for length, _ in pair_cycles] != raw.get("pair_cycle_partition"):
        raise ValueError("pair-cycle partition mismatch")
    if [parity for _, parity in pair_cycles] != raw.get("pair_cycle_orientation_parities"):
        raise ValueError("pair-cycle parity mismatch")

    sigma_inverse = [-1] * n
    for column, row in enumerate(sigma):
        sigma_inverse[row] = column
    relative = [sigma_inverse[tau[column]] for column in range(n)]
    relative_cycles = cycle_partition(relative)
    if relative_cycles != raw.get("relative_cycle_partition"):
        raise ValueError("relative-cycle partition mismatch")

    return {
        "outcome": "p41_four_line_near_state_verified",
        "p": 41,
        "selected_points": len(selected),
        "determinant_checks": determinant_checks,
        "zero_determinants": len(bad),
        "bad_orbit_owners": [15, 18, 20],
        "pair_cycle_partition": [length for length, _ in pair_cycles],
        "pair_cycle_orientation_parities": [parity for _, parity in pair_cycles],
        "relative_cycle_partition": relative_cycles,
        "valid_seed": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        raw = json.loads(args.input.read_text(encoding="utf-8"))
        result = verify(raw)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
