#!/usr/bin/env python3
"""Sweep independent sheared parabolic matching-reservoir parameters.

Movement and refill components may use different scale, branch gap, shear, and
offset parameters.  Every tested inserted state is internally no-three by
PP3aq and PP3ad.  The program enumerates every matching reservoir in the source
certificate and counts only the two external certificate classes.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

from analyze_parabolic_matching_reservoir import (
    certificate_counts,
    enumerate_matchings,
    load_cases,
    no_three,
    saturated,
)

Point = tuple[int, int]


def parse_widths(text: str) -> tuple[int, ...]:
    try:
        widths = tuple(
            sorted({int(part) for part in text.split(",") if part.strip()})
        )
    except ValueError as exc:
        raise ValueError("--widths must be comma-separated integers") from exc
    if not widths or any(width < 2 for width in widths):
        raise ValueError("widths must be integers at least two")
    return widths


def component_patterns(
    n: int,
    t: int,
    max_scale: int,
    shear_min: int,
    shear_max: int,
) -> list[dict[str, Any]]:
    patterns: list[dict[str, Any]] = []
    for scale in range(2, max_scale + 1):
        for gap in range(1, scale):
            for shear in range(shear_min, shear_max + 1):
                if scale + shear <= gap:
                    continue
                base = tuple(
                    scale * index * index + shear * index + epsilon * gap
                    for index in range(t)
                    for epsilon in (0, 1)
                )
                minimum = min(base)
                maximum = max(base)
                for offset in range(1 - minimum, n - maximum + 1):
                    ordered = tuple(offset + value for value in base)
                    if len(set(ordered)) != 2 * t:
                        raise AssertionError("component coordinates are not distinct")
                    patterns.append(
                        {
                            "scale": scale,
                            "gap": gap,
                            "shear": shear,
                            "offset": offset,
                            "coordinates": tuple(sorted(ordered)),
                            "ordered_coordinates": ordered,
                        }
                    )
    return patterns


def inserted_patch(
    n: int,
    t: int,
    movement: dict[str, Any],
    refill: dict[str, Any],
) -> tuple[Point, ...]:
    new_values = tuple(range(n + 1, n + t + 1))
    movement_points = tuple(
        (movement["ordered_coordinates"][2 * index + epsilon], new_values[index])
        for index in range(t)
        for epsilon in (0, 1)
    )
    refill_points = tuple(
        (new_values[index], refill["ordered_coordinates"][2 * index + epsilon])
        for index in range(t)
        for epsilon in (0, 1)
    )
    return tuple(sorted(movement_points + refill_points))


def analyze_case(
    n: int,
    core: tuple[Point, ...],
    widths: tuple[int, ...],
    max_scale: int,
    shear_min: int,
    shear_max: int,
    max_pattern_pairs: int,
) -> dict[str, Any]:
    width_results: list[dict[str, Any]] = []
    for t in widths:
        patterns = component_patterns(n, t, max_scale, shear_min, shear_max)
        pair_count = len(patterns) * len(patterns)
        if pair_count > max_pattern_pairs:
            width_results.append(
                {
                    "t": t,
                    "component_pattern_count": len(patterns),
                    "component_pattern_pair_count": pair_count,
                    "status": "cutoff",
                }
            )
            continue

        matching_cache: dict[
            tuple[tuple[int, ...], tuple[int, ...]], list[tuple[Point, ...]]
        ] = {}
        matching_states = 0
        clean_states = 0
        parameter_tuples_with_matchings = 0
        minimum: int | None = None
        histogram: Counter[int] = Counter()
        best: list[dict[str, Any]] = []

        for movement in patterns:
            columns = movement["coordinates"]
            for refill in patterns:
                rows = refill["coordinates"]
                key = (columns, rows)
                if key not in matching_cache:
                    matching_cache[key] = enumerate_matchings(core, columns, rows)
                deletions = matching_cache[key]
                if not deletions:
                    continue
                parameter_tuples_with_matchings += 1
                patch = inserted_patch(n, t, movement, refill)
                if not no_three(patch):
                    raise AssertionError("sheared parabolic patch has an internal triple")

                for deleted in deletions:
                    retained = tuple(point for point in core if point not in set(deleted))
                    final = tuple(sorted(retained + patch))
                    if not saturated(final, n + t):
                        raise AssertionError("patch does not preserve saturation")
                    blocked, anchored, internal = certificate_counts(retained, patch)
                    if internal != 0:
                        raise AssertionError("internal certificate count is nonzero")
                    total = blocked + anchored
                    matching_states += 1
                    clean_states += total == 0
                    histogram[total] += 1
                    if minimum is None or total < minimum:
                        minimum = total
                    best.append(
                        {
                            "total_triples": total,
                            "blocked_cell_triples": blocked,
                            "retained_anchor_triples": anchored,
                            "movement": {
                                key: movement[key]
                                for key in ("scale", "gap", "shear", "offset")
                            },
                            "refill": {
                                key: refill[key]
                                for key in ("scale", "gap", "shear", "offset")
                            },
                            "old_columns": list(columns),
                            "old_rows": list(rows),
                            "deleted": [list(point) for point in deleted],
                            "inserted": [list(point) for point in patch],
                        }
                    )

        best.sort(
            key=lambda item: (
                item["total_triples"],
                item["blocked_cell_triples"],
                item["retained_anchor_triples"],
                tuple(item["movement"].values()),
                tuple(item["refill"].values()),
                item["deleted"],
            )
        )
        width_results.append(
            {
                "t": t,
                "component_pattern_count": len(patterns),
                "component_pattern_pair_count": pair_count,
                "parameter_tuples_with_matchings": parameter_tuples_with_matchings,
                "matching_reservoir_state_count": matching_states,
                "clean_patch_count": clean_states,
                "minimum_total_triples": minimum,
                "triple_histogram": {
                    str(value): histogram[value] for value in sorted(histogram)
                },
                "best_candidates": best[:10],
                "status": "searched",
            }
        )

    return {"source_n": n, "widths": width_results}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int)
    parser.add_argument("--widths", default="2,3")
    parser.add_argument("--max-scale", type=int, default=10)
    parser.add_argument("--shear-min", type=int, default=-5)
    parser.add_argument("--shear-max", type=int, default=10)
    parser.add_argument("--max-pattern-pairs", type=int, default=2_000_000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        if args.max_scale < 2:
            raise ValueError("--max-scale must be at least two")
        if args.shear_min > args.shear_max:
            raise ValueError("--shear-min exceeds --shear-max")
        if args.max_pattern_pairs < 1:
            raise ValueError("--max-pattern-pairs must be positive")
        cases = load_cases(args.certificate, args.n)
        widths = parse_widths(args.widths)
        result = {
            "widths": list(widths),
            "maximum_scale": args.max_scale,
            "shear_range": [args.shear_min, args.shear_max],
            "cases": [
                analyze_case(
                    n,
                    core,
                    widths,
                    args.max_scale,
                    args.shear_min,
                    args.shear_max,
                    args.max_pattern_pairs,
                )
                for n, core in cases
            ],
        }
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
