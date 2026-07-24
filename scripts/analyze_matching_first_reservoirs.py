#!/usr/bin/env python3
"""Decompose saturated certificates and report matching-first reservoir spread."""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

Point = tuple[int, int]
Vertex = tuple[str, int]


def parse_point(raw: Any, label: str) -> Point:
    if not isinstance(raw, list) or len(raw) != 2:
        raise ValueError(f"{label}: malformed point")
    x, y = raw
    if (
        isinstance(x, bool)
        or isinstance(y, bool)
        or not isinstance(x, int)
        or not isinstance(y, int)
    ):
        raise ValueError(f"{label}: nonintegral point")
    return x, y


def load_cases(path: Path, requested_n: int | None) -> list[tuple[int, tuple[Point, ...]]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("certificate file must contain a list")
    cases: list[tuple[int, tuple[Point, ...]]] = []
    for index, raw_case in enumerate(payload):
        if not isinstance(raw_case, dict):
            raise ValueError(f"case {index}: expected an object")
        n = raw_case.get("n")
        raw_points = raw_case.get("points")
        if isinstance(n, bool) or not isinstance(n, int) or n < 2:
            raise ValueError(f"case {index}: invalid side length")
        if requested_n is not None and n != requested_n:
            continue
        if not isinstance(raw_points, list):
            raise ValueError(f"case {index}: points must be a list")
        points = tuple(
            sorted(
                parse_point(raw, f"case {index} point {ordinal}")
                for ordinal, raw in enumerate(raw_points)
            )
        )
        validate_saturated(n, points)
        cases.append((n, points))
    if requested_n is not None and not cases:
        raise ValueError(f"no certificate with n={requested_n}")
    return cases


def validate_saturated(n: int, points: tuple[Point, ...]) -> None:
    if len(points) != 2 * n or len(set(points)) != len(points):
        raise ValueError(f"n={n}: wrong point count or duplicate point")
    if any(not (1 <= x <= n and 1 <= y <= n) for x, y in points):
        raise ValueError(f"n={n}: point outside grid")
    for coordinate in range(1, n + 1):
        if sum(x == coordinate for x, _ in points) != 2:
            raise ValueError(f"n={n}: column {coordinate} does not have degree two")
        if sum(y == coordinate for _, y in points) != 2:
            raise ValueError(f"n={n}: row {coordinate} does not have degree two")


def other_endpoint(point: Point, vertex: Vertex) -> Vertex:
    x, y = point
    if vertex == ("c", x):
        return "r", y
    if vertex == ("r", y):
        return "c", x
    raise AssertionError("edge is not incident with traversal vertex")


def alternating_decomposition(
    n: int, points: tuple[Point, ...]
) -> tuple[tuple[Point, ...], tuple[Point, ...], tuple[int, ...]]:
    adjacency: dict[Vertex, list[int]] = {}
    for edge_index, (x, y) in enumerate(points):
        adjacency.setdefault(("c", x), []).append(edge_index)
        adjacency.setdefault(("r", y), []).append(edge_index)
    if any(len(edges) != 2 for edges in adjacency.values()):
        raise AssertionError("saturated graph is not two-regular")

    seen_edges: set[int] = set()
    layers: list[list[Point]] = [[], []]
    cycle_lengths: list[int] = []

    for start_vertex in sorted(adjacency):
        if all(edge in seen_edges for edge in adjacency[start_vertex]):
            continue
        current = start_vertex
        previous_edge: int | None = None
        cycle: list[int] = []
        while True:
            choices = [edge for edge in adjacency[current] if edge != previous_edge]
            edge = choices[0]
            if edge in seen_edges:
                if current != start_vertex:
                    raise AssertionError("cycle traversal closed at the wrong vertex")
                break
            cycle.append(edge)
            seen_edges.add(edge)
            next_vertex = other_endpoint(points[edge], current)
            previous_edge = edge
            current = next_vertex
            if current == start_vertex:
                break
        if len(cycle) % 2 != 0:
            raise AssertionError("bipartite cycle has odd length")
        cycle_lengths.append(len(cycle))
        for ordinal, edge in enumerate(cycle):
            layers[ordinal % 2].append(points[edge])

    if len(seen_edges) != len(points):
        raise AssertionError("not every edge was decomposed")
    for layer in layers:
        if len(layer) != n:
            raise AssertionError("layer is not a perfect matching")
        if len({x for x, _ in layer}) != n or len({y for _, y in layer}) != n:
            raise AssertionError("layer is not a perfect matching")
    return (
        tuple(sorted(layers[0])),
        tuple(sorted(layers[1])),
        tuple(sorted(cycle_lengths)),
    )


def falling_ratio(k: int, n: int, rank: int) -> Fraction:
    if rank < 0 or rank > k:
        return Fraction(0, 1)
    numerator = math.prod(range(k - rank + 1, k + 1)) if rank else 1
    denominator = math.prod(range(n - rank + 1, n + 1)) if rank else 1
    return Fraction(numerator, denominator)


def parse_widths(raw: str | None, n: int) -> tuple[int, ...]:
    if raw is None:
        return tuple(range(1, n // 2 + 1))
    widths = []
    for token in raw.split(","):
        token = token.strip()
        if not token:
            continue
        value = int(token)
        if value < 1:
            raise ValueError("widths must be positive")
        if 2 * value <= n:
            widths.append(value)
    return tuple(sorted(set(widths)))


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def analyze_case(n: int, points: tuple[Point, ...], raw_widths: str | None) -> dict[str, Any]:
    layer_zero, layer_one, cycle_lengths = alternating_decomposition(n, points)
    width_records = []
    for t in parse_widths(raw_widths, n):
        k = 2 * t
        width_records.append(
            {
                "t": t,
                "deleted_edges": k,
                "layer_labelled_reservoir_count": 2 * math.comb(n, k),
                "source_point_deletion_probability": fraction_text(Fraction(t, n)),
                "coordinate_inclusion_probability": fraction_text(Fraction(k, n)),
                "rank_2_coordinate_inclusion_probability": fraction_text(
                    falling_ratio(k, n, 2)
                ),
                "rank_3_coordinate_inclusion_probability": fraction_text(
                    falling_ratio(k, n, 3)
                ),
                "rank_2_same_layer_edge_deletion_probability": fraction_text(
                    Fraction(1, 2) * falling_ratio(k, n, 2)
                ),
                "rank_3_same_layer_edge_deletion_probability": fraction_text(
                    Fraction(1, 2) * falling_ratio(k, n, 3)
                ),
            }
        )
    return {
        "n": n,
        "cycle_edge_lengths": list(cycle_lengths),
        "layer_0": [list(point) for point in layer_zero],
        "layer_1": [list(point) for point in layer_one],
        "widths": width_records,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int)
    parser.add_argument("--widths", help="comma-separated patch widths; default all feasible")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        cases = load_cases(args.certificate, args.n)
        result = {
            "cases": [
                analyze_case(n, points, args.widths) for n, points in cases
            ]
        }
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
