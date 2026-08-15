#!/usr/bin/env python3
"""Classify the first-host canonical forbidden-cell background class.

Finite conditional theorem only. It proves selector invariance when the local
background is a subset of the diagonal cells plus target 01; it does not prove
that every physical occurrence has this form.
"""
from __future__ import annotations

import argparse
import copy
import json
from itertools import combinations
from pathlib import Path
from typing import Iterable

Point = tuple[int, int]
Perm = tuple[int, ...]

HOST_ID = "s4-75b04c45c1c8eac2"
RESPONSES: dict[str, Perm] = {
    "3012": (3, 0, 1, 2),
    "3210": (3, 2, 1, 0),
    "2031": (2, 0, 3, 1),
    "2310": (2, 3, 1, 0),
    "3201": (3, 2, 0, 1),
}
FORBIDDEN_BACKGROUND_POINTS: tuple[Point, ...] = (
    (0, 0),
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 3),
)
OFFSET_PAIRS: tuple[tuple[Point, Point], ...] = (
    ((0, 0), (0, 1)),
    ((0, 1), (1, 1)),
)


class AuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AuditError(message)


def response_points(permutation: Perm) -> tuple[Point, ...]:
    return tuple((row, permutation[row]) for row in range(4))


def collinear(first: Point, second: Point, third: Point) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def triple_count(points: Iterable[Point]) -> int:
    sequence = tuple(points)
    return sum(
        1
        for first, second, third in combinations(sequence, 3)
        if collinear(first, second, third)
    )


def intrinsic_score(permutation: Perm) -> int:
    return triple_count(response_points(permutation))


def new_triple_score(permutation: Perm, background: tuple[Point, ...]) -> int:
    response = response_points(permutation)
    require(not set(response) & set(background), "background overlaps response")
    return triple_count((*background, *response)) - triple_count(background)


def canonical_offset(background: tuple[Point, ...]) -> int:
    present = set(background)
    return sum(int(first in present and second in present) for first, second in OFFSET_PAIRS)


def all_backgrounds() -> tuple[tuple[Point, ...], ...]:
    return tuple(
        tuple(
            point
            for index, point in enumerate(FORBIDDEN_BACKGROUND_POINTS)
            if mask & (1 << index)
        )
        for mask in range(1 << len(FORBIDDEN_BACKGROUND_POINTS))
    )


def point_code(point: Point) -> str:
    return f"{point[0]}{point[1]}"


def compile_manifest() -> dict[str, object]:
    intrinsic = {name: intrinsic_score(permutation) for name, permutation in RESPONSES.items()}
    require(intrinsic == {"3012": 1, "3210": 4, "2031": 0, "2310": 0, "3201": 0}, "intrinsic scores")

    rows = []
    offset_census = {0: 0, 1: 0, 2: 0}
    for background in all_backgrounds():
        offset = canonical_offset(background)
        scores = {
            name: new_triple_score(permutation, background)
            for name, permutation in RESPONSES.items()
        }
        require(
            scores == {name: value + offset for name, value in intrinsic.items()},
            f"common offset identity for {background}",
        )
        minimum = min(scores.values())
        minimizers = [name for name, value in scores.items() if value == minimum]
        require(minimizers == ["2031", "2310", "3201"], "minimizer face")
        offset_census[offset] += 1
        rows.append(
            {
                "background": [point_code(point) for point in background],
                "offset": offset,
                "scores": scores,
                "minimizer_face": minimizers,
            }
        )

    require(offset_census == {0: 20, 1: 8, 2: 4}, "offset census")
    return {
        "schema": "exact-recurrent-first-host-forbidden-background-invariance/v1",
        "scope": {
            "host_id": HOST_ID,
            "background_universe": [point_code(point) for point in FORBIDDEN_BACKGROUND_POINTS],
            "responses": list(RESPONSES),
            "status": "conditional local background class",
        },
        "common_offset_formula": (
            "1[{00,01} subset B] + 1[{01,11} subset B]"
        ),
        "offset_pairs": [
            [point_code(first), point_code(second)]
            for first, second in OFFSET_PAIRS
        ],
        "intrinsic_scores": intrinsic,
        "rows": rows,
        "aggregate": {
            "forbidden_background_points": 5,
            "background_subsets": 32,
            "offset_zero_subsets": 20,
            "offset_one_subsets": 8,
            "offset_two_subsets": 4,
            "selector_order_preserved_subsets": 32,
            "common_minimizer_face_size": 3,
        },
        "honesty": {
            "forbidden_background_classification_complete": 1,
            "selector_invariance_on_declared_class_proved": 1,
            "all_physical_backgrounds_lie_in_declared_class": 0,
            "deletion_causes_populated": 0,
            "legal_reopening_proved": 0,
            "recurrent_child_rows_populated": 0,
            "strict_lyapunov_certificate_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def validate(manifest: dict[str, object]) -> None:
    require(manifest == compile_manifest(), "manifest differs from exact compiler")
    honesty = manifest.get("honesty")
    require(isinstance(honesty, dict), "honesty object")
    require(
        honesty.get("all_physical_backgrounds_lie_in_declared_class") == 0,
        "physical-class honesty",
    )
    require(honesty.get("all_n_proved_by_checker") == 0, "all-n honesty")


def mutation_audit(manifest: dict[str, object]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(background_subsets=31),
        lambda item: item["aggregate"].update(offset_zero_subsets=19),
        lambda item: item["aggregate"].update(offset_one_subsets=9),
        lambda item: item["aggregate"].update(offset_two_subsets=3),
        lambda item: item["aggregate"].update(selector_order_preserved_subsets=31),
        lambda item: item["rows"].pop(),
        lambda item: item["rows"][0].update(offset=1),
        lambda item: item["rows"][0]["scores"].update({"2031": 1}),
        lambda item: item["rows"][0].update(minimizer_face=["2031"]),
        lambda item: item["honesty"].update(all_physical_backgrounds_lie_in_declared_class=1),
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

    print(
        json.dumps(
            {
                "checker": "exact-recurrent-first-host-forbidden-background-invariance",
                **manifest["aggregate"],
                "mutation_corruptions_rejected": mutation_audit(manifest),
                **manifest["honesty"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
