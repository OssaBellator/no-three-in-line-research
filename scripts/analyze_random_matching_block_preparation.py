#!/usr/bin/env python3
"""Analyze the PP3cn random matching-block preparation bound.

For each requested saturated certificate and perfect-matching layer, construct
all labeled width-two support cells for K=floor(m/r) reserved block intervals.
The program counts the local PP3cl signatures and the deletion-blind global
PP3cm certificate profiles, then reports the exact rational values L_*, G_delta,
and L_*/(1-36 delta)+G_delta.
"""
from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

Point = tuple[int, int]
Candidate = tuple[int, int, str, int, Point]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def falling(value: int, rank: int) -> int:
    result = 1
    for offset in range(rank):
        result *= value - offset
    return result


def parse_fraction(text: str) -> Fraction:
    try:
        value = Fraction(text)
    except (ValueError, ZeroDivisionError) as exc:
        raise argparse.ArgumentTypeError(f"invalid fraction: {text}") from exc
    if value <= 0 or value >= Fraction(1, 36):
        raise argparse.ArgumentTypeError("delta must satisfy 0 < delta < 1/36")
    return value


def fraction_object(value: Fraction) -> dict[str, Any]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "text": str(value),
        "decimal": float(value),
    }


def load_certificates(path: Path) -> list[tuple[int, tuple[Point, ...]]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("certificate file must contain a list")

    result: list[tuple[int, tuple[Point, ...]]] = []
    for ordinal, raw in enumerate(payload):
        if not isinstance(raw, dict):
            raise ValueError(f"certificate {ordinal}: expected an object")
        n = raw.get("n")
        points_raw = raw.get("points")
        if isinstance(n, bool) or not isinstance(n, int) or n < 2:
            raise ValueError(f"certificate {ordinal}: invalid n")
        if not isinstance(points_raw, list):
            raise ValueError(f"certificate {ordinal}: points must be a list")
        points: list[Point] = []
        for point_ordinal, point in enumerate(points_raw):
            if (
                not isinstance(point, list)
                or len(point) != 2
                or isinstance(point[0], bool)
                or isinstance(point[1], bool)
                or not isinstance(point[0], int)
                or not isinstance(point[1], int)
            ):
                raise ValueError(
                    f"certificate {ordinal}, point {point_ordinal}: malformed point"
                )
            points.append((point[0], point[1]))
        if len(points) != 2 * n or len(set(points)) != len(points):
            raise ValueError(f"certificate n={n}: invalid point count or duplicates")
        if any(not (1 <= x <= n and 1 <= y <= n) for x, y in points):
            raise ValueError(f"certificate n={n}: point outside grid")
        for coordinate in range(1, n + 1):
            if sum(x == coordinate for x, _ in points) != 2:
                raise ValueError(f"certificate n={n}: column {coordinate} not saturated")
            if sum(y == coordinate for _, y in points) != 2:
                raise ValueError(f"certificate n={n}: row {coordinate} not saturated")
        result.append((n, tuple(points)))
    return result


def matching_layers(points: tuple[Point, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    by_column: dict[int, list[int]] = {}
    by_row: dict[int, list[int]] = {}
    for edge, (x, y) in enumerate(points):
        by_column.setdefault(x, []).append(edge)
        by_row.setdefault(y, []).append(edge)

    adjacency: list[set[int]] = [set() for _ in points]
    for pair in list(by_column.values()) + list(by_row.values()):
        if len(pair) != 2:
            raise ValueError("source is not two-regular")
        first, second = pair
        adjacency[first].add(second)
        adjacency[second].add(first)

    layers: list[list[int]] = [[], []]
    seen: set[int] = set()
    for start in range(len(points)):
        if start in seen:
            continue
        order: list[int] = []
        previous: int | None = None
        current = start
        while True:
            order.append(current)
            seen.add(current)
            choices = [edge for edge in adjacency[current] if edge != previous]
            following = min(choices) if previous is None else choices[0]
            previous, current = current, following
            if current == start:
                break
        if len(order) % 2:
            raise ValueError("incidence component has odd edge length")
        for index, edge in enumerate(order):
            layers[index % 2].append(edge)

    return tuple(sorted(layers[0])), tuple(sorted(layers[1]))


def build_candidates(
    n: int, layer: tuple[int, ...], points: tuple[Point, ...], block_count: int
) -> tuple[dict[tuple[int, int], tuple[Candidate, ...]], tuple[Candidate, ...]]:
    by_owner: dict[tuple[int, int], tuple[Candidate, ...]] = {}
    all_candidates: list[Candidate] = []
    for block in range(block_count):
        first_new = n + 2 * block + 1
        for edge in layer:
            x, y = points[edge]
            entries = (
                (block, edge, "M", 0, (x, first_new)),
                (block, edge, "M", 1, (x, first_new + 1)),
                (block, edge, "F", 0, (first_new, y)),
                (block, edge, "F", 1, (first_new + 1, y)),
            )
            by_owner[block, edge] = entries
            all_candidates.extend(entries)
    return by_owner, tuple(all_candidates)


def count_local_signatures(
    layer: tuple[int, ...],
    points: tuple[Point, ...],
    candidates: dict[tuple[int, int], tuple[Candidate, ...]],
    block_count: int,
) -> tuple[int, int, int]:
    blocker_count = 0
    same_edge_anchor_count = 0
    ordinary_anchor_count = 0

    for block in range(block_count):
        for first, second in itertools.combinations(layer, 2):
            for controller in layer:
                if controller in (first, second):
                    continue
                for candidate in candidates[block, controller]:
                    if determinant(points[first], points[second], candidate[4]) == 0:
                        blocker_count += 1

        for controller in layer:
            movement = [
                candidate
                for candidate in candidates[block, controller]
                if candidate[2] == "M"
            ]
            refill = [
                candidate
                for candidate in candidates[block, controller]
                if candidate[2] == "F"
            ]
            for anchor in layer:
                if anchor == controller:
                    continue
                for first in movement:
                    for second in refill:
                        if determinant(points[anchor], first[4], second[4]) == 0:
                            same_edge_anchor_count += 1

        for first_controller, second_controller in itertools.combinations(layer, 2):
            for anchor in layer:
                if anchor in (first_controller, second_controller):
                    continue
                for first in candidates[block, first_controller]:
                    for second in candidates[block, second_controller]:
                        if determinant(points[anchor], first[4], second[4]) == 0:
                            ordinary_anchor_count += 1

    return blocker_count, same_edge_anchor_count, ordinary_anchor_count


def controller_map_is_possible(candidates: Iterable[Candidate]) -> bool:
    assigned: dict[int, int] = {}
    for block, edge, _, _, _ in candidates:
        previous = assigned.get(edge)
        if previous is not None and previous != block:
            return False
        assigned[edge] = block
    return True


def count_global_profiles(
    points: tuple[Point, ...], all_candidates: tuple[Candidate, ...]
) -> dict[str, int]:
    counts = {
        "M1": 0,
        "Mh": 0,
        "M2": 0,
        "M11": 0,
        "Mh1": 0,
        "M21": 0,
        "M111": 0,
    }

    for candidate in all_candidates:
        for first, second in itertools.combinations(points, 2):
            if determinant(first, second, candidate[4]) == 0:
                counts["M1"] += 1

    for first, second in itertools.combinations(all_candidates, 2):
        if first[4] == second[4] or not controller_map_is_possible((first, second)):
            continue
        for anchor in points:
            if determinant(anchor, first[4], second[4]) != 0:
                continue
            if first[0] != second[0]:
                counts["M11"] += 1
            elif first[1] == second[1]:
                counts["Mh"] += 1
            else:
                counts["M2"] += 1

    for triple in itertools.combinations(all_candidates, 3):
        coordinates = tuple(candidate[4] for candidate in triple)
        if len(set(coordinates)) < 3 or determinant(*coordinates) != 0:
            continue
        if not controller_map_is_possible(triple):
            continue
        by_block: dict[int, list[Candidate]] = {}
        for candidate in triple:
            by_block.setdefault(candidate[0], []).append(candidate)
        if len(by_block) == 1:
            continue
        if len(by_block) == 3:
            counts["M111"] += 1
            continue
        repeated = next(group for group in by_block.values() if len(group) == 2)
        if repeated[0][1] == repeated[1][1]:
            counts["Mh1"] += 1
        else:
            counts["M21"] += 1

    return counts


def analyze_layer(
    n: int,
    points: tuple[Point, ...],
    layer_number: int,
    layer: tuple[int, ...],
    block_size: int,
    delta: Fraction,
) -> dict[str, Any]:
    block_count = n // block_size
    if block_count == 0:
        raise ValueError(f"n={n}: block size exceeds matching layer size")

    candidates, all_candidates = build_candidates(n, layer, points, block_count)
    blocker_count, same_edge_count, ordinary_count = count_local_signatures(
        layer, points, candidates, block_count
    )
    profiles = count_global_profiles(points, all_candidates)

    local_expectation = (
        Fraction(4 * (block_size - 1) * (block_size - 2) * blocker_count, falling(n, 3))
        + Fraction(4 * (block_size - 1) * same_edge_count, falling(n, 2))
        + Fraction(12 * (block_size - 2) * ordinary_count, falling(n, 3))
    )

    profile_expectation = Fraction(2 * profiles["M1"] + profiles["Mh"], delta * n)
    profile_expectation += Fraction(
        8 * (block_size - 1) * profiles["M2"],
        delta * block_size * falling(n, 2),
    )
    profile_expectation += Fraction(
        4 * profiles["M11"] + 2 * profiles["Mh1"],
        delta * delta * falling(n, 2),
    )
    profile_expectation += Fraction(
        16 * (block_size - 1) * profiles["M21"],
        delta * delta * block_size * falling(n, 3),
    )
    profile_expectation += Fraction(
        8 * profiles["M111"], delta * delta * delta * falling(n, 3)
    )

    combined = local_expectation / (1 - 36 * delta) + profile_expectation
    return {
        "n": n,
        "layer": layer_number,
        "block_size": block_size,
        "block_count": block_count,
        "unused_layer_edges": n - block_count * block_size,
        "delta": fraction_object(delta),
        "local_signature_counts": {
            "B_star": blocker_count,
            "A1_star": same_edge_count,
            "A2_star": ordinary_count,
        },
        "global_profile_counts": profiles,
        "L_star": fraction_object(local_expectation),
        "G_delta": fraction_object(profile_expectation),
        "PP3cn_left_side": fraction_object(combined),
        "PP3cn_certifies": combined < 1,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificates", type=Path)
    parser.add_argument("--n", type=int, action="append", dest="side_lengths")
    parser.add_argument("--layer", type=int, choices=(0, 1), action="append")
    parser.add_argument("--block-size", type=int, default=4)
    parser.add_argument("--delta", type=parse_fraction, default=Fraction(1, 72))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.block_size < 4:
        raise SystemExit("block size must be at least four")

    requested_sides = set(args.side_lengths or [])
    requested_layers = set(args.layer or (0, 1))
    rows: list[dict[str, Any]] = []
    try:
        for n, points in load_certificates(args.certificates):
            if requested_sides and n not in requested_sides:
                continue
            layers = matching_layers(points)
            for layer_number in sorted(requested_layers):
                rows.append(
                    analyze_layer(
                        n,
                        points,
                        layer_number,
                        layers[layer_number],
                        args.block_size,
                        args.delta,
                    )
                )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"analysis failed: {exc}") from exc

    payload = {"results": rows}
    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
