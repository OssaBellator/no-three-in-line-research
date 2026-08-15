#!/usr/bin/env python3
"""Classify the exact 31-coordinate signatures of chart-safe backgrounds."""

from __future__ import annotations

import argparse
import copy
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from check_exact_recurrent_first_host_background_signature import (
    background_signature,
    union_coordinates,
)


class SafeSignatureQuotientError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SafeSignatureQuotientError(message)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


POINTS = {
    "00": (0, 0),
    "01": (0, 1),
    "11": (1, 1),
    "22": (2, 2),
    "33": (3, 3),
}


def class_id(background: set[str]) -> str:
    left = {"00", "01"} <= background
    right = {"01", "11"} <= background
    if left and right:
        return "both-pairs"
    if left:
        return "pair-00-01"
    if right:
        return "pair-01-11"
    return "no-active-pair"


def point_code(point: tuple[int, int]) -> str:
    return f"{point[0]},{point[1]}"


def build_manifest(root: Path) -> dict[str, Any]:
    safe = load_json(
        root / "data/exact_recurrent_first_host_forbidden_background_invariance.json"
    )
    lines, response_points = union_coordinates()
    require(len(lines) == 20, "line coordinate count")
    require(len(response_points) == 11, "point coordinate count")

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    signature_to_classes: dict[tuple[int, ...], set[str]] = defaultdict(set)
    score_to_signatures: dict[tuple[int, ...], set[tuple[int, ...]]] = defaultdict(set)

    response_order = ["3012", "3210", "2031", "2310", "3201"]
    for row in safe["rows"]:
        background_codes = set(row["background"])
        background = tuple(POINTS[code] for code in sorted(background_codes))
        signature = background_signature(background, lines, response_points)
        identifier = class_id(background_codes)
        grouped[identifier].append(
            {
                "background": sorted(background_codes),
                "signature": signature,
                "offset": int(row["offset"]),
                "score_vector": tuple(row["scores"][name] for name in response_order),
            }
        )
        signature_to_classes[signature].add(identifier)
        score_to_signatures[
            tuple(row["scores"][name] for name in response_order)
        ].add(signature)

    expected_counts = {
        "no-active-pair": 20,
        "pair-00-01": 4,
        "pair-01-11": 4,
        "both-pairs": 4,
    }
    require({key: len(value) for key, value in grouped.items()} == expected_counts, "class census")
    require(len(signature_to_classes) == 4, "exact signature count")
    require(len(score_to_signatures) == 3, "score class count")
    require(sorted(len(value) for value in score_to_signatures.values()) == [1, 1, 2], "score collision pattern")

    class_order = ["no-active-pair", "pair-00-01", "pair-01-11", "both-pairs"]
    class_rows = []
    for identifier in class_order:
        records = grouped[identifier]
        signatures = {record["signature"] for record in records}
        offsets = {record["offset"] for record in records}
        scores = {record["score_vector"] for record in records}
        require(len(signatures) == 1, f"{identifier}: signature consistency")
        require(len(offsets) == 1, f"{identifier}: offset consistency")
        require(len(scores) == 1, f"{identifier}: score consistency")
        signature = next(iter(signatures))
        line_part = signature[: len(lines)]
        pair_part = signature[len(lines) :]
        require(not any(line_part), f"{identifier}: safe line loads vanish")
        class_rows.append(
            {
                "id": identifier,
                "background_count": len(records),
                "score_offset": next(iter(offsets)),
                "score_vector": list(next(iter(scores))),
                "nonzero_line_loads": {},
                "nonzero_pair_through_points": {
                    point_code(point): value
                    for point, value in zip(response_points, pair_part)
                    if value
                },
                "optional_invisible_points": ["22", "33"],
            }
        )

    return {
        "schema": "exact-recurrent-first-host-safe-signature-quotient/v1",
        "scope": {
            "host_id": "s4-75b04c45c1c8eac2",
            "background_universe": ["00", "01", "11", "22", "33"],
            "signature": "20 secant line loads plus 11 pair-through-response-point counts",
            "response_order": response_order,
        },
        "aggregate": {
            "safe_backgrounds": 32,
            "complete_score_classes": 3,
            "exact_31_coordinate_signature_classes": 4,
            "signature_class_census": expected_counts,
            "score_classes_with_multiple_signatures": 1,
            "maximum_signatures_per_score_class": 2,
            "safe_line_load_coordinates_nonzero": 0,
            "safe_pair_through_coordinates_ever_nonzero": 4,
        },
        "signature_classes": class_rows,
        "quotient_gate": {
            "four_class_31_coordinate_signature_quotient_exact": 1,
            "three_class_score_quotient_injective_on_31_signatures": 0,
            "offset_one_score_class_splits_geometrically": 1,
            "points_22_and_33_invisible_to_current_31_signature": 1,
            "four_class_signature_transition_congruence_proved": 0,
            "four_class_signature_payment_complete": 0,
            "promotion_to_alternating_core_physical_signature_allowed": 0,
        },
        "conclusion": {
            "present_score_equality_does_not_imply_signature_equality": 1,
            "score_only_recurrence_quotient_refuted_on_safe_class": 1,
            "exact_four_signature_candidate_available": 1,
            "physical_transition_quotient_complete": 0,
        },
        "honesty": {
            "physical_chart_confinement_proved": 0,
            "physical_occurrence_coverage_proved": 0,
            "legal_operations_populated": 0,
            "recurrent_child_rows_populated": 0,
            "strict_lyapunov_certificate_proved": 0,
            "global_termination_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def validate_manifest(manifest: dict[str, Any]) -> None:
    require(manifest.get("schema") == "exact-recurrent-first-host-safe-signature-quotient/v1", "schema")
    aggregate = manifest.get("aggregate", {})
    require(aggregate.get("safe_backgrounds") == 32, "safe backgrounds")
    require(aggregate.get("complete_score_classes") == 3, "score classes")
    require(aggregate.get("exact_31_coordinate_signature_classes") == 4, "signature classes")
    require(
        aggregate.get("signature_class_census")
        == {
            "no-active-pair": 20,
            "pair-00-01": 4,
            "pair-01-11": 4,
            "both-pairs": 4,
        },
        "signature census",
    )
    require(aggregate.get("score_classes_with_multiple_signatures") == 1, "score collision count")
    require(aggregate.get("maximum_signatures_per_score_class") == 2, "max signatures per score")
    require(aggregate.get("safe_line_load_coordinates_nonzero") == 0, "line loads")
    require(aggregate.get("safe_pair_through_coordinates_ever_nonzero") == 4, "pair coordinate support")

    expected = {
        "no-active-pair": (20, 0, [1, 4, 0, 0, 0], {}),
        "pair-00-01": (4, 1, [2, 5, 1, 1, 1], {"0,2": 1, "0,3": 1}),
        "pair-01-11": (4, 1, [2, 5, 1, 1, 1], {"2,1": 1, "3,1": 1}),
        "both-pairs": (
            4,
            2,
            [3, 6, 2, 2, 2],
            {"0,2": 1, "0,3": 1, "2,1": 1, "3,1": 1},
        ),
    }
    rows = manifest.get("signature_classes", [])
    require([row.get("id") for row in rows] == list(expected), "class order")
    for row in rows:
        count, offset, scores, pair_points = expected[row["id"]]
        require(row.get("background_count") == count, "class count")
        require(row.get("score_offset") == offset, "class offset")
        require(row.get("score_vector") == scores, "class score")
        require(row.get("nonzero_line_loads") == {}, "class line loads")
        require(row.get("nonzero_pair_through_points") == pair_points, "class pair points")
        require(row.get("optional_invisible_points") == ["22", "33"], "invisible points")

    gate = manifest.get("quotient_gate", {})
    for key in (
        "four_class_31_coordinate_signature_quotient_exact",
        "offset_one_score_class_splits_geometrically",
        "points_22_and_33_invisible_to_current_31_signature",
    ):
        require(gate.get(key) == 1, f"gate {key}")
    for key in (
        "three_class_score_quotient_injective_on_31_signatures",
        "four_class_signature_transition_congruence_proved",
        "four_class_signature_payment_complete",
        "promotion_to_alternating_core_physical_signature_allowed",
    ):
        require(gate.get(key) == 0, f"gate {key}")

    conclusion = manifest.get("conclusion", {})
    for key in (
        "present_score_equality_does_not_imply_signature_equality",
        "score_only_recurrence_quotient_refuted_on_safe_class",
        "exact_four_signature_candidate_available",
    ):
        require(conclusion.get(key) == 1, f"conclusion {key}")
    require(conclusion.get("physical_transition_quotient_complete") == 0, "physical quotient")

    for key, value in manifest.get("honesty", {}).items():
        require(value == 0, f"honesty {key}")


def mutation_audit(manifest: dict[str, Any]) -> int:
    mutations = [
        lambda x: x["aggregate"].update(exact_31_coordinate_signature_classes=3),
        lambda x: x["aggregate"].update(score_classes_with_multiple_signatures=0),
        lambda x: x["aggregate"].update(safe_pair_through_coordinates_ever_nonzero=2),
        lambda x: x["signature_classes"][1].update(background_count=8),
        lambda x: x["signature_classes"][1].update(nonzero_pair_through_points={"0,2": 1}),
        lambda x: x["signature_classes"][2].update(score_offset=2),
        lambda x: x["quotient_gate"].update(three_class_score_quotient_injective_on_31_signatures=1),
        lambda x: x["quotient_gate"].update(four_class_signature_transition_congruence_proved=1),
        lambda x: x["quotient_gate"].update(promotion_to_alternating_core_physical_signature_allowed=1),
        lambda x: x["conclusion"].update(score_only_recurrence_quotient_refuted_on_safe_class=0),
        lambda x: x["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(manifest)
        mutate(candidate)
        try:
            validate_manifest(candidate)
        except SafeSignatureQuotientError:
            rejected += 1
    require(rejected == len(mutations), "mutation accepted")
    return rejected


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise SafeSignatureQuotientError("unable to locate repository root")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()

    root = repository_root()
    manifest = build_manifest(root)
    validate_manifest(manifest)
    if args.check:
        require(load_json(args.check) == manifest, "manifest mismatch")

    rejected = mutation_audit(manifest)
    print(
        "verified safe first-host signature quotient: "
        f"{manifest['aggregate']['safe_backgrounds']} backgrounds, "
        f"{manifest['aggregate']['complete_score_classes']} score classes, "
        f"{manifest['aggregate']['exact_31_coordinate_signature_classes']} exact signatures and "
        f"{rejected} rejected corruptions"
    )


if __name__ == "__main__":
    main()
