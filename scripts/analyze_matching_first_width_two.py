#!/usr/bin/env python3
"""Analyze canonical adjacent width-two patches from matching-first reservoirs."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import combinations
from pathlib import Path
from typing import Any

from analyze_matching_first_reservoirs import alternating_decomposition, load_cases

Point = tuple[int, int]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def canonical_state(deleted: tuple[Point, ...], n: int) -> tuple[Point, ...]:
    columns = sorted(x for x, _ in deleted)
    rows = sorted(y for _, y in deleted)
    a, b = n + 1, n + 2
    return (
        (columns[0], a),
        (columns[1], a),
        (columns[2], b),
        (columns[3], b),
        (a, rows[0]),
        (a, rows[1]),
        (b, rows[2]),
        (b, rows[3]),
    )


def certificate_counts(
    retained: tuple[Point, ...], inserted: tuple[Point, ...]
) -> tuple[int, int, int]:
    retained_set = set(retained)
    inserted_set = set(inserted)
    blocked = anchored = internal = 0
    for triple in combinations(tuple(sorted(retained_set.union(inserted_set))), 3):
        if determinant(*triple) != 0:
            continue
        inserted_count = sum(point in inserted_set for point in triple)
        if inserted_count == 1:
            blocked += 1
        elif inserted_count == 2:
            anchored += 1
        elif inserted_count == 3:
            internal += 1
    return blocked, anchored, internal


def saturated(points: tuple[Point, ...], n: int) -> bool:
    return (
        len(points) == 2 * n
        and len(set(points)) == len(points)
        and all(
            sum(x == coordinate for x, _ in points) == 2
            for coordinate in range(1, n + 1)
        )
        and all(
            sum(y == coordinate for _, y in points) == 2
            for coordinate in range(1, n + 1)
        )
    )


def analyze_case(n: int, core: tuple[Point, ...]) -> dict[str, Any]:
    if n < 4:
        return {
            "source_n": n,
            "state_count": 0,
            "clean_state_count": 0,
            "minimum_total_defects": None,
            "status": "fewer-than-four-layer-edges",
        }

    layer_zero, layer_one, cycle_lengths = alternating_decomposition(n, core)
    hist: Counter[tuple[int, int]] = Counter()
    best_total: int | None = None
    best_states: list[dict[str, Any]] = []
    clean = 0

    for layer_index, layer in enumerate((layer_zero, layer_one)):
        for deleted in combinations(layer, 4):
            inserted = canonical_state(deleted, n)
            deleted_set = set(deleted)
            retained = tuple(point for point in core if point not in deleted_set)
            final = tuple(sorted(retained + inserted))
            if not saturated(final, n + 2):
                raise AssertionError("canonical state does not preserve saturation")
            blocked, anchored, internal = certificate_counts(retained, inserted)
            if internal != 0:
                raise AssertionError("canonical adjacent state has an internal triple")
            total = blocked + anchored
            hist[(blocked, anchored)] += 1
            clean += total == 0
            record = {
                "layer": layer_index,
                "deleted": [list(point) for point in deleted],
                "inserted": [list(point) for point in inserted],
                "blocked_cell_triples": blocked,
                "retained_anchor_triples": anchored,
                "total_external_triples": total,
            }
            if best_total is None or total < best_total:
                best_total = total
                best_states = [record]
            elif total == best_total:
                best_states.append(record)

    return {
        "source_n": n,
        "target_n": n + 2,
        "cycle_edge_lengths": list(cycle_lengths),
        "state_count": sum(hist.values()),
        "clean_state_count": clean,
        "minimum_total_defects": best_total,
        "minimum_blocker_count_over_all_states": min(key[0] for key in hist),
        "minimum_anchor_count_over_all_states": min(key[1] for key in hist),
        "maximum_anchor_count_over_all_states": max(key[1] for key in hist),
        "defect_histogram": {
            f"{blocked},{anchored}": count
            for (blocked, anchored), count in sorted(hist.items())
        },
        "best_states": best_states[:10],
        "status": "searched",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        cases = load_cases(args.certificate, args.n)
        result = {"cases": [analyze_case(n, core) for n, core in cases]}
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
