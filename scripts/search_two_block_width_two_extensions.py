#!/usr/bin/env python3
"""Exhaust two disjoint four-edge width-two blocks on stored certificates."""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Any, Iterable

from analyze_full_width_two_block_bank import determinant, no_three, ordered_pair_partitions
from analyze_matching_first_reservoirs import alternating_decomposition, load_cases

Point = tuple[int, int]


def patch_states_at(
    deleted: tuple[Point, ...], n: int, block_index: int
) -> Iterable[tuple[Point, ...]]:
    columns = tuple(sorted(x for x, _ in deleted))
    rows = tuple(sorted(y for _, y in deleted))
    first_new = n + 2 * block_index + 1
    new_values = (first_new, first_new + 1)
    for column_partition in ordered_pair_partitions(columns):
        movement = tuple(
            (column, new_values[index])
            for index, pair in enumerate(column_partition)
            for column in pair
        )
        for row_partition in ordered_pair_partitions(rows):
            refill = tuple(
                (new_values[index], row)
                for index, pair in enumerate(row_partition)
                for row in pair
            )
            yield tuple(sorted(movement + refill))


def source_clean(retained: tuple[Point, ...], patch: tuple[Point, ...]) -> bool:
    if not no_three(patch):
        return False
    for candidate in patch:
        for first, second in itertools.combinations(retained, 2):
            if determinant(first, second, candidate) == 0:
                return False
    for anchor in retained:
        for first, second in itertools.combinations(patch, 2):
            if determinant(anchor, first, second) == 0:
                return False
    return True


def patches_compatible(
    retained: tuple[Point, ...],
    first_patch: tuple[Point, ...],
    second_patch: tuple[Point, ...],
) -> bool:
    for anchor in retained:
        for first in first_patch:
            for second in second_patch:
                if determinant(anchor, first, second) == 0:
                    return False
    for candidate in first_patch:
        for first, second in itertools.combinations(second_patch, 2):
            if determinant(candidate, first, second) == 0:
                return False
    for candidate in second_patch:
        for first, second in itertools.combinations(first_patch, 2):
            if determinant(candidate, first, second) == 0:
                return False
    return True


def block_partitions(edge_count: int) -> Iterable[tuple[tuple[int, ...], tuple[int, ...]]]:
    indices = tuple(range(edge_count))
    for first in itertools.combinations(indices, 4):
        first_set = set(first)
        remaining = tuple(index for index in indices if index not in first_set)
        for second in itertools.combinations(remaining, 4):
            if min(first) > min(second):
                continue
            yield first, second


def analyze_layer(
    n: int,
    core: tuple[Point, ...],
    layer_index: int,
    layer: tuple[Point, ...],
) -> dict[str, Any]:
    partition_count = 0
    both_domains_nonempty = 0
    maximum_first_domain = 0
    maximum_second_domain = 0
    solution: dict[str, Any] | None = None

    for first_indices, second_indices in block_partitions(n):
        partition_count += 1
        first_deleted = tuple(layer[index] for index in first_indices)
        second_deleted = tuple(layer[index] for index in second_indices)
        deleted_set = set(first_deleted + second_deleted)
        retained = tuple(point for point in core if point not in deleted_set)

        first_domain = tuple(
            patch
            for patch in patch_states_at(first_deleted, n, 0)
            if source_clean(retained, patch)
        )
        second_domain = tuple(
            patch
            for patch in patch_states_at(second_deleted, n, 1)
            if source_clean(retained, patch)
        )
        maximum_first_domain = max(maximum_first_domain, len(first_domain))
        maximum_second_domain = max(maximum_second_domain, len(second_domain))
        if not first_domain or not second_domain:
            continue
        both_domains_nonempty += 1

        for first_patch in first_domain:
            for second_patch in second_domain:
                if not patches_compatible(retained, first_patch, second_patch):
                    continue
                final = tuple(sorted(retained + first_patch + second_patch))
                if len(final) != 2 * (n + 4) or not no_three(final):
                    raise AssertionError("candidate solution failed independent verification")
                solution = {
                    "first_block_indices": list(first_indices),
                    "second_block_indices": list(second_indices),
                    "first_patch": [list(point) for point in first_patch],
                    "second_patch": [list(point) for point in second_patch],
                    "final_points": [list(point) for point in final],
                }
                break
            if solution is not None:
                break
        if solution is not None:
            break

    return {
        "layer": layer_index,
        "partition_count": partition_count,
        "partitions_with_both_source_clean_domains_nonempty": both_domains_nonempty,
        "maximum_first_domain_size": maximum_first_domain,
        "maximum_second_domain_size": maximum_second_domain,
        "found": solution is not None,
        "solution": solution,
    }


def analyze_case(n: int, core: tuple[Point, ...]) -> dict[str, Any]:
    if n < 8:
        return {"source_n": n, "layers": [], "status": "fewer-than-eight-layer-edges"}
    layer_zero, layer_one, cycle_lengths = alternating_decomposition(n, core)
    return {
        "source_n": n,
        "target_n": n + 4,
        "cycle_edge_lengths": list(cycle_lengths),
        "layers": [
            analyze_layer(n, core, layer_index, layer)
            for layer_index, layer in enumerate((layer_zero, layer_one))
        ],
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
