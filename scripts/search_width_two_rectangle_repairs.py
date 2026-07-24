#!/usr/bin/env python3
"""Search one-rectangle repairs of every width-two matching near miss."""
from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path
from typing import Any

from analyze_parabolic_matching_reservoir import (
    enumerate_matchings,
    load_cases,
    no_three,
    saturated,
)
from search_width_two_matching_patches import (
    inserted_state,
    ordered_pair_partitions,
)

Point = tuple[int, int]
Triple = tuple[Point, Point, Point]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def bad_triples(points: frozenset[Point]) -> tuple[Triple, ...]:
    return tuple(
        triple
        for triple in combinations(sorted(points), 3)
        if determinant(*triple) == 0
    )


def repair_switches(
    points: frozenset[Point],
) -> list[tuple[tuple[Point, Point], tuple[Point, Point], frozenset[Point]]]:
    triples = bad_triples(points)
    repairs = []
    for first, second in combinations(sorted(points), 2):
        if first[0] == second[0] or first[1] == second[1]:
            continue
        added_first = (first[0], second[1])
        added_second = (second[0], first[1])
        if added_first in points or added_second in points:
            continue
        if any(first not in triple and second not in triple for triple in triples):
            continue
        switched = frozenset(
            points.difference((first, second)).union((added_first, added_second))
        )
        if no_three(switched):
            repairs.append(
                (
                    tuple(sorted((first, second))),
                    tuple(sorted((added_first, added_second))),
                    switched,
                )
            )
    return repairs


def analyze_case(n: int, core: tuple[Point, ...]) -> dict[str, Any]:
    if n < 4:
        return {
            "source_n": n,
            "unique_internally_clean_initial_states": 0,
            "repairable_initial_states": 0,
            "repairing_switch_count": 0,
            "distinct_repaired_configurations": 0,
            "repairs": [],
        }

    coordinate_sets = tuple(combinations(range(1, n + 1), 4))
    initial_metadata: dict[frozenset[Point], dict[str, Any]] = {}

    for columns in coordinate_sets:
        for rows in coordinate_sets:
            deletions = enumerate_matchings(core, columns, rows)
            if not deletions:
                continue
            for column_partition in ordered_pair_partitions(columns):
                for row_partition in ordered_pair_partitions(rows):
                    inserted = inserted_state(n, column_partition, row_partition)
                    if not no_three(inserted):
                        continue
                    for deleted in deletions:
                        deleted_set = set(deleted)
                        initial = frozenset(
                            point for point in core if point not in deleted_set
                        ).union(inserted)
                        if not saturated(initial, n + 2):
                            raise AssertionError("initial state is not saturated")
                        initial_metadata.setdefault(
                            initial,
                            {
                                "old_columns": list(columns),
                                "old_rows": list(rows),
                                "column_partition": [
                                    list(pair) for pair in column_partition
                                ],
                                "row_partition": [list(pair) for pair in row_partition],
                                "deleted": [list(point) for point in deleted],
                                "inserted": [list(point) for point in inserted],
                            },
                        )

    repairs = []
    repaired_configurations: set[frozenset[Point]] = set()
    repairable_initial_states = 0
    repairing_switch_count = 0

    for initial, metadata in initial_metadata.items():
        switches = repair_switches(initial)
        if not switches:
            continue
        repairable_initial_states += 1
        initial_triples = bad_triples(initial)
        for removed, added, switched in switches:
            repairing_switch_count += 1
            repaired_configurations.add(switched)
            if not saturated(switched, n + 2) or not no_three(switched):
                raise AssertionError("reported repair is invalid")
            repairs.append(
                {
                    "initial_triple_count": len(initial_triples),
                    "initial_triples": [
                        [list(point) for point in triple]
                        for triple in initial_triples
                    ],
                    "removed_corners": [list(point) for point in removed],
                    "added_corners": [list(point) for point in added],
                    "repaired_points": [list(point) for point in sorted(switched)],
                    **metadata,
                }
            )

    repairs.sort(
        key=lambda item: (
            item["initial_triple_count"],
            item["removed_corners"],
            item["added_corners"],
        )
    )
    return {
        "source_n": n,
        "target_n": n + 2,
        "unique_internally_clean_initial_states": len(initial_metadata),
        "repairable_initial_states": repairable_initial_states,
        "repairing_switch_count": repairing_switch_count,
        "distinct_repaired_configurations": len(repaired_configurations),
        "repairs": repairs,
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
