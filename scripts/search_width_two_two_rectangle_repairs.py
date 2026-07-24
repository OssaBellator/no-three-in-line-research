#!/usr/bin/env python3
"""Exhaust two sequential rectangle repairs of width-two matching patches.

The search starts from every distinct internally no-three cross-only width-two
matching-patch state.  A first rectangle switch is retained only when the
original triples that it does not hit have a transversal of size at most two;
this is necessary because the second switch removes only two selected points.
Every retained first switch is followed by every exact one-switch repair of the
intermediate state.  The transversal filter is therefore lossless.
"""
from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path
from typing import Any, Iterable

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
Switch = tuple[Point, Point, Point, Point, frozenset[Point]]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def bad_triples(points: Iterable[Point]) -> tuple[Triple, ...]:
    return tuple(
        triple
        for triple in combinations(sorted(points), 3)
        if determinant(*triple) == 0
    )


def legal_switches(points: frozenset[Point]) -> Iterable[Switch]:
    point_set = set(points)
    for first, second in combinations(sorted(points), 2):
        if first[0] == second[0] or first[1] == second[1]:
            continue
        added_first = (first[0], second[1])
        added_second = (second[0], first[1])
        if added_first in point_set or added_second in point_set:
            continue
        switched = frozenset(
            point_set.difference((first, second)).union((added_first, added_second))
        )
        yield first, second, added_first, added_second, switched


def point_masks(
    points: tuple[Point, ...], triples: tuple[Triple, ...]
) -> tuple[dict[Point, int], tuple[int, ...]]:
    index = {point: ordinal for ordinal, point in enumerate(points)}
    masks = [0] * len(points)
    for triple_index, triple in enumerate(triples):
        bit = 1 << triple_index
        for point in triple:
            masks[index[point]] |= bit
    return index, tuple(masks)


def has_two_point_transversal(
    uncovered: int,
    masks: tuple[int, ...],
    excluded_indices: frozenset[int],
) -> bool:
    """Return whether at most two available original points hit every bit."""
    if uncovered == 0:
        return True
    available = [
        mask for index, mask in enumerate(masks) if index not in excluded_indices
    ]
    for mask in available:
        if mask & uncovered == uncovered:
            return True
    for first_index, first_mask in enumerate(available):
        remaining = uncovered & ~first_mask
        for second_mask in available[first_index + 1 :]:
            if second_mask & remaining == remaining:
                return True
    return False


def exact_one_switch_repairs(points: frozenset[Point]) -> Iterable[Switch]:
    """Enumerate every one-switch repair, using an exact triple transversal."""
    triples = bad_triples(points)
    ordered_points = tuple(sorted(points))
    index, masks = point_masks(ordered_points, triples)
    all_triples = (1 << len(triples)) - 1
    point_set = set(points)

    for first, second in combinations(ordered_points, 2):
        if first[0] == second[0] or first[1] == second[1]:
            continue
        if triples and masks[index[first]] | masks[index[second]] != all_triples:
            continue
        added_first = (first[0], second[1])
        added_second = (second[0], first[1])
        if added_first in point_set or added_second in point_set:
            continue
        switched = frozenset(
            point_set.difference((first, second)).union((added_first, added_second))
        )
        if no_three(switched):
            yield first, second, added_first, added_second, switched


def initial_states(
    n: int, core: tuple[Point, ...]
) -> dict[frozenset[Point], dict[str, Any]]:
    coordinate_sets = tuple(combinations(range(1, n + 1), 4))
    states: dict[frozenset[Point], dict[str, Any]] = {}

    for columns in coordinate_sets:
        column_partitions = ordered_pair_partitions(columns)
        for rows in coordinate_sets:
            deletions = enumerate_matchings(core, columns, rows)
            if not deletions:
                continue
            row_partitions = ordered_pair_partitions(rows)
            for column_partition in column_partitions:
                for row_partition in row_partitions:
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
                        states.setdefault(
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
    return states


def analyze_case(
    n: int, core: tuple[Point, ...], max_examples: int
) -> dict[str, Any]:
    if n < 4:
        return {
            "source_n": n,
            "target_n": n + 2,
            "unique_internally_clean_initial_states": 0,
            "promising_first_switches": 0,
            "two_switch_repair_sequences": 0,
            "distinct_two_switch_final_configurations": 0,
            "additional_final_configurations_beyond_one_switch": 0,
            "examples": [],
        }

    states = initial_states(n, core)
    one_switch_finals: set[frozenset[Point]] = set()
    two_switch_finals: set[frozenset[Point]] = set()
    promising_first_switches = 0
    sequence_count = 0
    examples: list[dict[str, Any]] = []

    for initial, metadata in states.items():
        initial_triples = bad_triples(initial)
        ordered_points = tuple(sorted(initial))
        index, masks = point_masks(ordered_points, initial_triples)
        all_triples = (1 << len(initial_triples)) - 1

        for *_, one_switch_final in exact_one_switch_repairs(initial):
            one_switch_finals.add(one_switch_final)

        for first, second, added_first, added_second, intermediate in legal_switches(
            initial
        ):
            uncovered = all_triples & ~(
                masks[index[first]] | masks[index[second]]
            )
            if not has_two_point_transversal(
                uncovered,
                masks,
                frozenset((index[first], index[second])),
            ):
                continue
            promising_first_switches += 1

            intermediate_triples = bad_triples(intermediate)
            for (
                next_first,
                next_second,
                next_added_first,
                next_added_second,
                final,
            ) in exact_one_switch_repairs(intermediate):
                if final == initial:
                    continue
                if not saturated(final, n + 2) or not no_three(final):
                    raise AssertionError("reported two-switch repair is invalid")
                sequence_count += 1
                two_switch_finals.add(final)
                if len(examples) < max_examples:
                    examples.append(
                        {
                            "initial_triple_count": len(initial_triples),
                            "intermediate_triple_count": len(intermediate_triples),
                            "first_removed": [list(first), list(second)],
                            "first_added": [list(added_first), list(added_second)],
                            "second_removed": [list(next_first), list(next_second)],
                            "second_added": [
                                list(next_added_first),
                                list(next_added_second),
                            ],
                            "final_points": [list(point) for point in sorted(final)],
                            **metadata,
                        }
                    )

    additional = two_switch_finals.difference(one_switch_finals)
    return {
        "source_n": n,
        "target_n": n + 2,
        "unique_internally_clean_initial_states": len(states),
        "promising_first_switches": promising_first_switches,
        "two_switch_repair_sequences": sequence_count,
        "distinct_two_switch_final_configurations": len(two_switch_finals),
        "one_switch_final_configurations": len(one_switch_finals),
        "additional_final_configurations_beyond_one_switch": len(additional),
        "examples": examples,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int)
    parser.add_argument("--max-examples", type=int, default=10)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_examples < 0:
        raise SystemExit("--max-examples must be nonnegative")

    try:
        cases = load_cases(args.certificate, args.n)
        result = {
            "cases": [
                analyze_case(n, core, args.max_examples) for n, core in cases
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
