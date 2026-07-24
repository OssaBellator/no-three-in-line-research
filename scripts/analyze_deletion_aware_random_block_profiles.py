#!/usr/bin/env python3
"""Analyze the PP3cq deletion-aware random block profile bound.

The script imports the certificate validation, matching-layer decomposition,
candidate construction, and local PP3cl counts from
analyze_random_matching_block_preparation.py.  It stratifies source-anchor
profiles by their rank in the selected matching layer, removes controller-anchor
collisions, applies the exact PP3cp survival factors, and reports PP3cr.
"""
from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

from analyze_random_matching_block_preparation import (
    Candidate,
    build_candidates,
    controller_map_is_possible,
    count_local_signatures,
    determinant,
    falling,
    fraction_object,
    load_certificates,
    matching_layers,
    parse_fraction,
)

Point = tuple[int, int]


def empty_profile_counts() -> dict[str, Any]:
    return {
        "M1_by_layer_anchor_rank": [0, 0, 0],
        "Mh_by_layer_anchor_rank": [0, 0],
        "M2_by_layer_anchor_rank": [0, 0],
        "M11_by_layer_anchor_rank": [0, 0],
        "Mh1": 0,
        "M21": 0,
        "M111": 0,
        "controller_anchor_collisions_removed": 0,
    }


def count_deletion_aware_profiles(
    points: tuple[Point, ...],
    layer: tuple[int, ...],
    all_candidates: tuple[Candidate, ...],
) -> dict[str, Any]:
    layer_set = set(layer)
    counts = empty_profile_counts()

    for candidate in all_candidates:
        controller = candidate[1]
        for first_index, second_index in itertools.combinations(range(len(points)), 2):
            if controller in (first_index, second_index):
                if determinant(
                    points[first_index], points[second_index], candidate[4]
                ) == 0:
                    counts["controller_anchor_collisions_removed"] += 1
                continue
            if determinant(points[first_index], points[second_index], candidate[4]) != 0:
                continue
            rank = int(first_index in layer_set) + int(second_index in layer_set)
            counts["M1_by_layer_anchor_rank"][rank] += 1

    for first, second in itertools.combinations(all_candidates, 2):
        if first[4] == second[4] or not controller_map_is_possible((first, second)):
            continue
        controllers = {first[1], second[1]}
        for anchor_index, anchor in enumerate(points):
            if determinant(anchor, first[4], second[4]) != 0:
                continue
            if anchor_index in controllers:
                counts["controller_anchor_collisions_removed"] += 1
                continue
            rank = int(anchor_index in layer_set)
            if first[0] != second[0]:
                counts["M11_by_layer_anchor_rank"][rank] += 1
            elif first[1] == second[1]:
                counts["Mh_by_layer_anchor_rank"][rank] += 1
            else:
                counts["M2_by_layer_anchor_rank"][rank] += 1

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


def survival_factor(
    n: int, block_count: int, controller_rank: int, anchor_rank: int
) -> Fraction:
    if anchor_rank == 0:
        return Fraction(1)
    remaining = n - 4 * block_count
    if remaining < anchor_rank:
        return Fraction(0)
    return Fraction(
        falling(remaining, anchor_rank),
        falling(n - controller_rank, anchor_rank),
    )


def weighted_sum(
    values: list[int],
    n: int,
    block_count: int,
    controller_rank: int,
) -> Fraction:
    return sum(
        (
            survival_factor(n, block_count, controller_rank, anchor_rank)
            * count
            for anchor_rank, count in enumerate(values)
        ),
        Fraction(0),
    )


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
    local_expectation = (
        Fraction(
            4 * (block_size - 1) * (block_size - 2) * blocker_count,
            falling(n, 3),
        )
        + Fraction(4 * (block_size - 1) * same_edge_count, falling(n, 2))
        + Fraction(12 * (block_size - 2) * ordinary_count, falling(n, 3))
    )

    profiles = count_deletion_aware_profiles(points, layer, all_candidates)
    weighted_m1 = weighted_sum(
        profiles["M1_by_layer_anchor_rank"], n, block_count, 1
    )
    weighted_mh = weighted_sum(
        profiles["Mh_by_layer_anchor_rank"], n, block_count, 1
    )
    weighted_m2 = weighted_sum(
        profiles["M2_by_layer_anchor_rank"], n, block_count, 2
    )
    weighted_m11 = weighted_sum(
        profiles["M11_by_layer_anchor_rank"], n, block_count, 2
    )

    profile_expectation = Fraction(2, delta * n) * weighted_m1
    profile_expectation += Fraction(1, delta * n) * weighted_mh
    profile_expectation += Fraction(
        8 * (block_size - 1), delta * block_size * falling(n, 2)
    ) * weighted_m2
    profile_expectation += Fraction(
        4, delta * delta * falling(n, 2)
    ) * weighted_m11
    profile_expectation += Fraction(
        2 * profiles["Mh1"], delta * delta * falling(n, 2)
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
        "total_deleted_layer_edges": 4 * block_count,
        "unused_layer_edges": n - block_count * block_size,
        "delta": fraction_object(delta),
        "local_signature_counts": {
            "B_star": blocker_count,
            "A1_star": same_edge_count,
            "A2_star": ordinary_count,
        },
        "deletion_aware_profile_counts": profiles,
        "weighted_profile_counts": {
            "M1": fraction_object(weighted_m1),
            "Mh": fraction_object(weighted_mh),
            "M2": fraction_object(weighted_m2),
            "M11": fraction_object(weighted_m11),
        },
        "L_star": fraction_object(local_expectation),
        "G_delta_deletion_aware": fraction_object(profile_expectation),
        "PP3cr_left_side": fraction_object(combined),
        "PP3cr_certifies": combined < 1,
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

    text = json.dumps({"results": rows}, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
