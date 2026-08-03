#!/usr/bin/env python3
"""Audit exact first-host symmetries on the safe signature quotient."""
from __future__ import annotations

import argparse
import copy
import itertools
import json
from pathlib import Path
from typing import Iterable

Point = tuple[int, int]
Permutation = tuple[int, ...]
Transform = tuple[Permutation, Permutation, bool]

SIDE = 4
HOST_ID = "s4-75b04c45c1c8eac2"
TARGET: Point = (0, 1)
DELETIONS = frozenset({(0, 2), (2, 0)})
LINEAGE_HOST = frozenset({
    (0, 1), (0, 3),
    (1, 0), (1, 2), (1, 3),
    (2, 1), (2, 3),
    (3, 0), (3, 1), (3, 2),
})
RESPONSES = {
    "3012": frozenset({(0, 3), (1, 0), (2, 1), (3, 2)}),
    "3210": frozenset({(0, 3), (1, 2), (2, 1), (3, 0)}),
    "2031": frozenset({(0, 2), (1, 0), (2, 3), (3, 1)}),
    "2310": frozenset({(0, 2), (1, 3), (2, 1), (3, 0)}),
    "3201": frozenset({(0, 3), (1, 2), (2, 0), (3, 1)}),
}
PAIR_LEFT = frozenset({(0, 0), (0, 1)})
PAIR_RIGHT = frozenset({(0, 1), (1, 1)})


class AuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AuditError(message)


def transform_point(point: Point, transform: Transform) -> Point:
    row_permutation, column_permutation, swap_axes = transform
    row, column = point
    if swap_axes:
        return row_permutation[column], column_permutation[row]
    return row_permutation[row], column_permutation[column]


def transform_set(points: Iterable[Point], transform: Transform) -> frozenset[Point]:
    return frozenset(transform_point(point, transform) for point in points)


def collinear(first: Point, second: Point, third: Point) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def all_transforms() -> tuple[Transform, ...]:
    permutations = tuple(itertools.permutations(range(SIDE)))
    return tuple(
        (row_permutation, column_permutation, swap_axes)
        for row_permutation in permutations
        for column_permutation in permutations
        for swap_axes in (False, True)
    )


def ambient_collinearity_automorphisms(transforms: tuple[Transform, ...]) -> tuple[Transform, ...]:
    grid = tuple((row, column) for row in range(SIDE) for column in range(SIDE))
    triples = frozenset(
        frozenset(triple)
        for triple in itertools.combinations(grid, 3)
        if collinear(*triple)
    )
    return tuple(
        transform
        for transform in transforms
        if all(transform_set(triple, transform) in triples for triple in triples)
    )


def response_menu_image(transform: Transform) -> frozenset[frozenset[Point]]:
    return frozenset(transform_set(response, transform) for response in RESPONSES.values())


def preserves_lineage(transform: Transform) -> bool:
    return transform_set(LINEAGE_HOST, transform) == LINEAGE_HOST


def preserves_deletions(transform: Transform) -> bool:
    return transform_set(DELETIONS, transform) == DELETIONS


def preserves_menu(transform: Transform) -> bool:
    return response_menu_image(transform) == frozenset(RESPONSES.values())


def preserves_target(transform: Transform) -> bool:
    return transform_point(TARGET, transform) == TARGET


def transform_code(transform: Transform) -> dict[str, object]:
    row_permutation, column_permutation, swap_axes = transform
    return {
        "row_permutation": list(row_permutation),
        "column_permutation": list(column_permutation),
        "swap_axes": int(swap_axes),
        "target_image": list(transform_point(TARGET, transform)),
    }


def compile_manifest() -> dict[str, object]:
    transforms = all_transforms()
    geometry = ambient_collinearity_automorphisms(transforms)
    lineage = tuple(transform for transform in geometry if preserves_lineage(transform))
    lineage_deletions = tuple(
        transform for transform in lineage if preserves_deletions(transform)
    )
    lineage_deletions_menu = tuple(
        transform for transform in lineage_deletions if preserves_menu(transform)
    )
    exact_geometry = tuple(
        transform for transform in lineage_deletions_menu if preserves_target(transform)
    )
    exact_structure = tuple(
        transform
        for transform in transforms
        if preserves_lineage(transform)
        and preserves_deletions(transform)
        and preserves_menu(transform)
        and preserves_target(transform)
    )

    require(len(transforms) == 1152, "row-column/swap transform census")
    require(len(geometry) == 8, "ambient grid collinearity group")
    require(len(lineage) == 2, "lineage stabilizer")
    require(len(lineage_deletions) == 2, "lineage/deletion stabilizer")
    require(len(lineage_deletions_menu) == 1, "menu stabilizer")
    require(len(exact_geometry) == 1, "exact geometric stabilizer")
    require(len(exact_structure) == 1, "exact structural stabilizer")

    identity = ((0, 1, 2, 3), (0, 1, 2, 3), False)
    transpose = ((0, 1, 2, 3), (0, 1, 2, 3), True)
    require(exact_geometry == (identity,), "exact geometry is identity")
    require(exact_structure == (identity,), "exact structure is identity")
    require(lineage_deletions == (identity, transpose), "relaxed stabilizer census")

    transpose_response_images = {
        name: [list(point) for point in sorted(transform_set(response, transpose))]
        for name, response in RESPONSES.items()
    }
    require(transform_point(TARGET, transpose) == (1, 0), "transpose target image")
    require(not preserves_menu(transpose), "transpose breaks response menu")
    require(
        transform_set(PAIR_LEFT, transpose) == frozenset({(0, 0), (1, 0)}),
        "left pair transpose",
    )
    require(
        transform_set(PAIR_LEFT, transpose) != PAIR_RIGHT,
        "relaxed symmetry does not exchange bits",
    )

    exact_left_orbit = frozenset(
        transform_set(PAIR_LEFT, transform) for transform in exact_geometry
    )
    relaxed_left_orbit = frozenset(
        transform_set(PAIR_LEFT, transform) for transform in lineage_deletions
    )
    require(PAIR_RIGHT not in exact_left_orbit, "exact orbit separation")
    require(PAIR_RIGHT not in relaxed_left_orbit, "relaxed orbit separation")

    return {
        "schema": "exact-recurrent-first-host-safe-signature-symmetry/v1",
        "scope": {
            "host_id": HOST_ID,
            "side": SIDE,
            "target": list(TARGET),
            "deletions": [list(point) for point in sorted(DELETIONS)],
            "ordered_activation_bits": {
                "left": [list(point) for point in sorted(PAIR_LEFT)],
                "right": [list(point) for point in sorted(PAIR_RIGHT)],
            },
        },
        "groups": {
            "all_row_column_axis_relabelings": len(transforms),
            "ambient_collinearity_automorphisms": [
                transform_code(item) for item in geometry
            ],
            "lineage_host_stabilizer": [transform_code(item) for item in lineage],
            "lineage_deletion_stabilizer": [
                transform_code(item) for item in lineage_deletions
            ],
            "lineage_deletion_menu_stabilizer": [
                transform_code(item) for item in lineage_deletions_menu
            ],
            "exact_geometric_stabilizer": [
                transform_code(item) for item in exact_geometry
            ],
            "exact_structural_relabeling_stabilizer": [
                transform_code(item) for item in exact_structure
            ],
        },
        "transpose_obstruction": {
            "target_image": list(transform_point(TARGET, transpose)),
            "left_activation_pair_image": [
                list(point) for point in sorted(transform_set(PAIR_LEFT, transpose))
            ],
            "right_activation_pair": [list(point) for point in sorted(PAIR_RIGHT)],
            "response_images": transpose_response_images,
            "preserves_five_response_menu": 0,
        },
        "aggregate": {
            "all_row_column_axis_relabelings": len(transforms),
            "ambient_collinearity_automorphisms": len(geometry),
            "lineage_host_stabilizer": len(lineage),
            "lineage_deletion_stabilizer": len(lineage_deletions),
            "lineage_deletion_menu_stabilizer": len(lineage_deletions_menu),
            "exact_geometric_stabilizer": len(exact_geometry),
            "exact_structural_relabeling_stabilizer": len(exact_structure),
            "offset_one_classes_same_exact_orbit": int(PAIR_RIGHT in exact_left_orbit),
            "offset_one_classes_same_relaxed_lineage_deletion_orbit": int(
                PAIR_RIGHT in relaxed_left_orbit
            ),
        },
        "conclusion": {
            "ordered_activation_bits_symmetry_exchange_available": 0,
            "score_offset_one_collision_resolved_by_host_symmetry": 0,
            "four_signature_classes_reduce_to_three_by_exact_symmetry": 0,
            "exact_first_host_automorphism_group_trivial": 1,
        },
        "honesty": {
            "physical_chart_confinement_proved": 0,
            "physical_occurrence_coverage_proved": 0,
            "transition_congruence_proved": 0,
            "payment_congruence_proved": 0,
            "strict_lyapunov_certificate_proved": 0,
            "global_termination_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def validate(manifest: dict[str, object]) -> None:
    require(manifest == compile_manifest(), "manifest differs from exact compiler")


def mutation_audit(manifest: dict[str, object]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(ambient_collinearity_automorphisms=7),
        lambda item: item["aggregate"].update(lineage_host_stabilizer=1),
        lambda item: item["aggregate"].update(lineage_deletion_menu_stabilizer=2),
        lambda item: item["aggregate"].update(exact_geometric_stabilizer=2),
        lambda item: item["aggregate"].update(exact_structural_relabeling_stabilizer=2),
        lambda item: item["aggregate"].update(offset_one_classes_same_exact_orbit=1),
        lambda item: item["conclusion"].update(
            ordered_activation_bits_symmetry_exchange_available=1
        ),
        lambda item: item["conclusion"].update(
            four_signature_classes_reduce_to_three_by_exact_symmetry=1
        ),
        lambda item: item["transpose_obstruction"].update(
            preserves_five_response_menu=1
        ),
        lambda item: item["honesty"].update(transition_congruence_proved=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(manifest)
        mutate(candidate)
        try:
            validate(candidate)
        except (AuditError, KeyError, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "mutation audit")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path)
    parser.add_argument("--check", type=Path)
    arguments = parser.parse_args()
    manifest = compile_manifest()

    if arguments.write:
        arguments.write.parent.mkdir(parents=True, exist_ok=True)
        arguments.write.write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    if arguments.check:
        observed = json.loads(arguments.check.read_text(encoding="utf-8"))
        validate(observed)

    print(json.dumps({
        "checker": "exact-recurrent-first-host-safe-signature-symmetry",
        **manifest["aggregate"],
        "mutation_corruptions_rejected": mutation_audit(manifest),
        **manifest["conclusion"],
        **manifest["honesty"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
