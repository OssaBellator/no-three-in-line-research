#!/usr/bin/env python3
"""Exhaustively audit targeted Hamilton three-edge switching drift."""
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


def potentials(
    points: set[Point], owners: dict[Point, int]
) -> tuple[int, int, int, int, list[tuple[int, int, int]]]:
    lines: dict[tuple[int, int, int], set[Point]] = defaultdict(set)
    ordered = sorted(points)
    for a, b in combinations(ordered, 2):
        lines[normal_line(a, b)].update((a, b))

    bad_lines = [cells for cells in lines.values() if len(cells) >= 3]
    triple_count = sum(math.comb(len(cells), 3) for cells in bad_lines)
    excess = sum(len(cells) - 2 for cells in bad_lines)
    target_sets: list[tuple[int, int, int]] = []
    for cells in bad_lines:
        for triple in combinations(sorted(cells), 3):
            source_set = tuple(sorted({owners[point] for point in triple}))
            if len(source_set) == 3:
                target_sets.append(source_set)
    return triple_count, len(bad_lines), excess, len(target_sets), target_sets


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


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def census(m: int) -> dict[str, Any]:
    metrics: dict[
        tuple[tuple[int, ...], tuple[int, ...]],
        tuple[int, int, int, int, list[tuple[int, int, int]]],
    ] = {}
    for rho in hamilton_cycles(m):
        for orientations in product((0, 1), repeat=m):
            points, owners = state_points(m, rho, orientations)
            metrics[(rho, tuple(orientations))] = potentials(points, owners)

    names = ("triples", "bad_lines", "excess", "targetable")
    totals = [0] * 4
    drift_sums = [Fraction(0) for _ in range(4)]
    random_signs = [Counter() for _ in range(4)]
    best_sums = [0] * 4
    best_nonnegative = [0] * 4
    best_max = [-10**9] * 4
    best_witness: list[dict[str, Any] | None] = [None] * 4
    state_classes = [Counter() for _ in range(4)]
    local_witness: list[dict[str, Any] | None] = [None] * 4
    targeted_occurrences = 0
    valid_states = 0

    for (rho, orientations), values in metrics.items():
        for index in range(4):
            totals[index] += values[index]
        if values[0] == 0:
            valid_states += 1

        unique_sources = sorted(set(values[4]))
        for index in range(4):
            old = values[index]
            if old == 0:
                continue
            if not unique_sources:
                state_classes[index]["stuck_no_target"] += 1
                if local_witness[index] is None:
                    local_witness[index] = {
                        "kind": "stuck_no_target",
                        "rho": list(rho),
                        "orientations": list(orientations),
                        "potentials": list(values[:4]),
                    }
                continue

            improving = False
            for sources in unique_sources:
                changed_rho = switch_rho(rho, sources)
                for bits in product((0, 1), repeat=3):
                    changed_orientations = list(orientations)
                    for source, bit in zip(sources, bits):
                        changed_orientations[source] = bit
                    if metrics[(changed_rho, tuple(changed_orientations))][index] < old:
                        improving = True
                        break
                if improving:
                    break

            if improving:
                state_classes[index]["improvable"] += 1
            else:
                state_classes[index]["local_min"] += 1
                if local_witness[index] is None:
                    local_witness[index] = {
                        "kind": "local_min",
                        "rho": list(rho),
                        "orientations": list(orientations),
                        "potentials": list(values[:4]),
                        "source_sets": [list(sources) for sources in unique_sources],
                    }

        for sources in values[4]:
            targeted_occurrences += 1
            changed_rho = switch_rho(rho, sources)
            outputs = [[] for _ in range(4)]
            for bits in product((0, 1), repeat=3):
                changed_orientations = list(orientations)
                for source, bit in zip(sources, bits):
                    changed_orientations[source] = bit
                changed = metrics[(changed_rho, tuple(changed_orientations))]
                for index in range(4):
                    outputs[index].append(changed[index])

            for index in range(4):
                old = values[index]
                random_drift = Fraction(sum(outputs[index]), 8) - old
                drift_sums[index] += random_drift
                if random_drift < 0:
                    random_signs[index]["negative"] += 1
                elif random_drift > 0:
                    random_signs[index]["positive"] += 1
                else:
                    random_signs[index]["zero"] += 1

                best_drift = min(outputs[index]) - old
                best_sums[index] += best_drift
                if best_drift >= 0:
                    best_nonnegative[index] += 1
                if best_drift > best_max[index]:
                    best_max[index] = best_drift
                    best_witness[index] = {
                        "rho": list(rho),
                        "orientations": list(orientations),
                        "sources": list(sources),
                        "old": old,
                        "after": outputs[index],
                        "best_drift": best_drift,
                    }

    result: dict[str, Any] = {
        "m": m,
        "states": len(metrics),
        "valid_states": valid_states,
        "targeted_occurrences": targeted_occurrences,
        "potentials": {},
    }
    for index, name in enumerate(names):
        result["potentials"][name] = {
            "state_mean": fraction_text(Fraction(totals[index], len(metrics))),
            "random_targeted_mean_drift": fraction_text(drift_sums[index] / targeted_occurrences),
            "random_negative": random_signs[index]["negative"],
            "random_zero": random_signs[index]["zero"],
            "random_positive": random_signs[index]["positive"],
            "best_sign_mean_drift": fraction_text(Fraction(best_sums[index], targeted_occurrences)),
            "best_sign_nonnegative": best_nonnegative[index],
            "best_sign_max_drift": best_max[index],
            "state_classification": dict(state_classes[index]),
        }

    result["triple_increase_witness"] = best_witness[0]
    result["triple_local_minimum_witness"] = local_witness[0]
    return result


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
            "cases": [census(m) for m in range(minimum, maximum + 1)],
            "asymptotic_seed_theorem_proved": False,
        }
        if result != expected:
            raise ValueError("stored targeted-switching drift ledger mismatch")
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
