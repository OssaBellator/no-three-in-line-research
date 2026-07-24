#!/usr/bin/env python3
"""Exhaust every cross-only width-two matching-reservoir patch.

For four old columns and four old rows, enumerate every perfect matching
deletion and all 36 ordered pair partitions that refill the two new rows and
two new columns.  Exact integer determinants classify internal and external
triple certificates.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import combinations
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


def ordered_pair_partitions(values: tuple[int, ...]) -> tuple[tuple[tuple[int, int], tuple[int, int]], ...]:
    if len(values) != 4:
        raise ValueError("an ordered pair partition requires four values")
    out = []
    for first_indices in combinations(range(4), 2):
        first_index_set = set(first_indices)
        first = tuple(values[index] for index in first_indices)
        second = tuple(
            values[index] for index in range(4) if index not in first_index_set
        )
        out.append((tuple(sorted(first)), tuple(sorted(second))))
    return tuple(out)


def inserted_state(
    n: int,
    column_partition: tuple[tuple[int, int], tuple[int, int]],
    row_partition: tuple[tuple[int, int], tuple[int, int]],
) -> tuple[Point, ...]:
    new_first = n + 1
    new_second = n + 2
    new_values = (new_first, new_second)
    movement = tuple(
        (column, new_values[index])
        for index, pair in enumerate(column_partition)
        for column in pair
    )
    refill = tuple(
        (new_values[index], row)
        for index, pair in enumerate(row_partition)
        for row in pair
    )
    return tuple(sorted(movement + refill))


def analyze_case(n: int, core: tuple[Point, ...]) -> dict[str, Any]:
    if n < 4:
        return {
            "source_n": n,
            "matching_reservoir_count": 0,
            "degree_state_count": 0,
            "internally_clean_state_count": 0,
            "clean_patch_count": 0,
            "minimum_external_triples": None,
            "status": "fewer-than-four-old-coordinates",
        }

    coordinate_sets = tuple(combinations(range(1, n + 1), 4))
    matching_reservoir_count = 0
    degree_state_count = 0
    internally_clean_state_count = 0
    clean_patch_count = 0
    minimum_external: int | None = None
    internal_histogram: Counter[int] = Counter()
    external_histogram: Counter[int] = Counter()
    best: list[dict[str, Any]] = []

    for columns in coordinate_sets:
        column_partitions = ordered_pair_partitions(columns)
        for rows in coordinate_sets:
            deletions = enumerate_matchings(core, columns, rows)
            if not deletions:
                continue
            matching_reservoir_count += len(deletions)
            row_partitions = ordered_pair_partitions(rows)

            for column_partition in column_partitions:
                for row_partition in row_partitions:
                    inserted = inserted_state(n, column_partition, row_partition)
                    internal_clean = no_three(inserted)
                    for deleted in deletions:
                        degree_state_count += 1
                        deleted_set = set(deleted)
                        retained = tuple(
                            point for point in core if point not in deleted_set
                        )
                        final = tuple(sorted(retained + inserted))
                        if not saturated(final, n + 2):
                            raise AssertionError("degree state does not preserve saturation")

                        blocked, anchored, internal = certificate_counts(
                            retained, inserted
                        )
                        internal_histogram[internal] += 1
                        if not internal_clean:
                            if internal == 0:
                                raise AssertionError(
                                    "internal no-three test and certificate count disagree"
                                )
                            continue
                        if internal != 0:
                            raise AssertionError("internally clean state has a triple")

                        internally_clean_state_count += 1
                        external = blocked + anchored
                        external_histogram[external] += 1
                        clean_patch_count += external == 0
                        if minimum_external is None or external < minimum_external:
                            minimum_external = external
                        best.append(
                            {
                                "external_triples": external,
                                "blocked_cell_triples": blocked,
                                "retained_anchor_triples": anchored,
                                "old_columns": list(columns),
                                "old_rows": list(rows),
                                "column_partition": [
                                    list(pair) for pair in column_partition
                                ],
                                "row_partition": [list(pair) for pair in row_partition],
                                "deleted": [list(point) for point in deleted],
                                "inserted": [list(point) for point in inserted],
                            }
                        )

    best.sort(
        key=lambda item: (
            item["external_triples"],
            item["blocked_cell_triples"],
            item["retained_anchor_triples"],
            item["old_columns"],
            item["old_rows"],
            item["column_partition"],
            item["row_partition"],
            item["deleted"],
        )
    )
    return {
        "source_n": n,
        "matching_reservoir_count": matching_reservoir_count,
        "degree_state_count": degree_state_count,
        "internally_clean_state_count": internally_clean_state_count,
        "clean_patch_count": clean_patch_count,
        "minimum_external_triples": minimum_external,
        "internal_triple_histogram": {
            str(value): internal_histogram[value]
            for value in sorted(internal_histogram)
        },
        "external_triple_histogram_on_clean_states": {
            str(value): external_histogram[value]
            for value in sorted(external_histogram)
        },
        "best_candidates": best[:10],
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
