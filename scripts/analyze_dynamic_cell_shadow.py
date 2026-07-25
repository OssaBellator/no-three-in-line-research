#!/usr/bin/env python3
"""Analyze the PP3kv--PP3kw dynamic excess-shadow potential.

For each stored saturated source and deterministic perfect-matching layer, use the
whole layer as one controller pool.  The program enumerates movement and refill
candidate cells for a requested number of labels, verifies that every candidate
has exactly one controller-containing axis blocker pair, checks that every other
blocker pair is nonaxis and controller-disjoint, and reports the exact excess
potential Xi.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Any

from analyze_random_matching_block_preparation import (
    determinant,
    load_certificates,
    matching_layers,
)

Point = tuple[int, int]


def blocker_pairs(points: tuple[Point, ...], candidate: Point) -> list[tuple[int, int]]:
    return [
        (first, second)
        for first, second in itertools.combinations(range(len(points)), 2)
        if determinant(points[first], points[second], candidate) == 0
    ]


def analyze_candidate(
    points: tuple[Point, ...],
    candidate: Point,
    controller_index: int,
    kind: str,
) -> dict[str, Any]:
    pairs = blocker_pairs(points, candidate)
    axis_pairs: list[tuple[int, int]] = []
    nonaxis_pairs: list[tuple[int, int]] = []

    for first, second in pairs:
        first_point = points[first]
        second_point = points[second]
        if kind == "movement":
            axis = first_point[0] == second_point[0] == candidate[0]
        else:
            axis = first_point[1] == second_point[1] == candidate[1]
        if axis:
            axis_pairs.append((first, second))
        else:
            nonaxis_pairs.append((first, second))

    if len(axis_pairs) != 1:
        raise ValueError(
            f"candidate {candidate}: expected one axis blocker, found {len(axis_pairs)}"
        )
    if controller_index not in axis_pairs[0]:
        raise ValueError(f"candidate {candidate}: axis blocker misses controller")
    if any(controller_index in pair for pair in nonaxis_pairs):
        raise ValueError(f"candidate {candidate}: nonaxis blocker contains controller")
    if len(pairs) - 1 != len(nonaxis_pairs):
        raise ValueError(f"candidate {candidate}: excess/nonaxis mismatch")

    return {
        "candidate": list(candidate),
        "controller_index": controller_index,
        "kind": kind,
        "blocker_pair_count": len(pairs),
        "excess": len(pairs) - 1,
        "axis_pair": list(axis_pairs[0]),
        "nonaxis_pairs": [list(pair) for pair in nonaxis_pairs],
    }


def analyze_layer(
    n: int,
    points: tuple[Point, ...],
    layer_number: int,
    layer_indices: tuple[int, ...],
    label_count: int,
) -> dict[str, Any]:
    by_column = {points[index][0]: index for index in layer_indices}
    by_row = {points[index][1]: index for index in layer_indices}
    details: list[dict[str, Any]] = []

    for offset in range(1, label_count + 1):
        label = n + offset
        for x, controller_index in sorted(by_column.items()):
            details.append(
                analyze_candidate(points, (x, label), controller_index, "movement")
            )
        for y, controller_index in sorted(by_row.items()):
            details.append(
                analyze_candidate(points, (label, y), controller_index, "refill")
            )

    excesses = [item["excess"] for item in details]
    bad_entries = sum(excess > 0 for excess in excesses)
    xi = sum(excesses)
    return {
        "n": n,
        "layer": layer_number,
        "label_count": label_count,
        "candidate_cell_count": len(details),
        "bad_cell_entry_count": bad_entries,
        "bad_cell_entry_density": bad_entries / len(details) if details else 0.0,
        "Xi": xi,
        "Xi_per_candidate": xi / len(details) if details else 0.0,
        "maximum_excess": max(excesses, default=0),
        "PP3kw_bad_count_bound": bad_entries <= xi,
        "details": details,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificates", type=Path)
    parser.add_argument("--labels", type=int, default=12)
    parser.add_argument("--n", type=int, action="append", dest="side_lengths")
    parser.add_argument("--layer", type=int, choices=(0, 1), action="append")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.labels < 1:
        raise SystemExit("--labels must be positive")

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
                        args.labels,
                    )
                )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"analysis failed: {exc}") from exc

    text = json.dumps({"results": rows}, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
