#!/usr/bin/env python3
"""Audit promotion of the first side-four projection into the raw-lineage schema."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from itertools import combinations, permutations
from pathlib import Path
from typing import Any

Point = tuple[int, int]
Permutation = tuple[int, ...]

HOST_ID = "s4-75b04c45c1c8eac2"
BLOCKER_ID = "b4-8a44614df456"
SIDE = 4
TARGET: Point = (0, 1)
DELETIONS = ((0, 2), (2, 0))
STRICT_BACKGROUNDS = (
    ((-3, 5), (5, -3)),
    ((-1, 3), (5, -3)),
    ((-2, 6), (4, 0)),
    ((-2, 6), (6, -2)),
)
LABELS = {
    "owner": "unpopulated",
    "fate": "unpopulated",
    "collision": "unpopulated",
    "line": "unpopulated",
    "interface": "unpopulated",
    "crt": "unpopulated",
}


class AuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AuditError(message)


def collinear(a: Point, b: Point, c: Point) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def triple_count(permutation: Permutation) -> int:
    points = tuple((row, permutation[row]) for row in range(len(permutation)))
    return sum(collinear(*triple) for triple in combinations(points, 3))


def response_code(permutation: Permutation) -> str:
    return "".join(map(str, permutation))


def projected_host_edges() -> tuple[Point, ...]:
    identity = {(index, index) for index in range(SIDE)}
    return tuple(
        sorted(
            (row, column)
            for row in range(SIDE)
            for column in range(SIDE)
            if (row, column) not in identity
            and (row, column) != TARGET
            and (row, column) not in DELETIONS
        )
    )


def allowed_responses(edges: tuple[Point, ...]) -> tuple[Permutation, ...]:
    allowed = set(edges)
    return tuple(
        permutation
        for permutation in permutations(range(SIDE))
        if all((row, permutation[row]) in allowed for row in range(SIDE))
    )


def installed_validate(record: dict[str, Any]) -> tuple[Permutation, ...]:
    side = record["side"]
    require(side >= 2, "side")
    edges = [tuple(edge) for edge in record["host_edges"]]
    require(
        all(0 <= row < side and 0 <= column < side for row, column in edges),
        "edge coordinates",
    )
    require(tuple(record["target"]) in edges, "target in host")
    require(
        len({tuple(point) for point in record["background"]})
        == len(record["background"]),
        "background unique",
    )
    responses = allowed_responses(tuple(edges))
    require(responses, "nonempty response family")
    require(record["response_count"] == len(responses), "response linkage")
    require(
        all(
            name in record["labels"]
            for name in ("owner", "fate", "collision", "line", "interface", "crt")
        ),
        "provenance",
    )
    return responses


def identifier(record: dict[str, Any]) -> str:
    payload = {
        key: record[key]
        for key in ("side", "host_edges", "deletions", "target", "background", "labels")
    }
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def record(edges: tuple[Point, ...], background: tuple[Point, ...], count: int) -> dict[str, Any]:
    return {
        "side": SIDE,
        "host_edges": [list(edge) for edge in edges],
        "deletions": [list(edge) for edge in DELETIONS],
        "target": list(TARGET),
        "background": [list(point) for point in background],
        "labels": copy.deepcopy(LABELS),
        "response_count": count,
    }


def response_table(responses: tuple[Permutation, ...]) -> list[dict[str, Any]]:
    return [
        {"response": response_code(permutation), "intrinsic_triples": triple_count(permutation)}
        for permutation in responses
    ]


def compile_manifest() -> dict[str, Any]:
    projected_edges = projected_host_edges()
    require(len(projected_edges) == 9, "projected edge count")
    require(TARGET not in projected_edges, "projection excludes target")
    projected_responses = allowed_responses(projected_edges)
    require(
        tuple(response_code(item) for item in projected_responses) == ("3012", "3210"),
        "projected response family",
    )
    require(tuple(triple_count(item) for item in projected_responses) == (1, 4), "projected energies")

    direct = record(projected_edges, tuple(), len(projected_responses))
    direct_rejection = None
    try:
        installed_validate(direct)
    except AuditError as error:
        direct_rejection = str(error)
    require(direct_rejection == "target in host", "direct promotion rejection")

    augmented_edges = tuple(sorted((*projected_edges, TARGET)))
    augmented_responses = allowed_responses(augmented_edges)
    require(
        tuple(response_code(item) for item in augmented_responses)
        == ("1032", "1230", "3012", "3210"),
        "augmented response family",
    )
    require(
        tuple(triple_count(item) for item in augmented_responses) == (0, 1, 1, 4),
        "augmented energies",
    )

    stale_count = record(augmented_edges, tuple(), len(projected_responses))
    stale_rejection = None
    try:
        installed_validate(stale_count)
    except AuditError as error:
        stale_rejection = str(error)
    require(stale_rejection == "response linkage", "stale count rejection")

    accepted = []
    identifiers = set()
    for background in (tuple(), *STRICT_BACKGROUNDS):
        candidate = record(augmented_edges, background, len(augmented_responses))
        observed = installed_validate(candidate)
        require(observed == augmented_responses, "accepted response family")
        candidate_id = identifier(candidate)
        require(candidate_id not in identifiers, "lineage identifier collision")
        identifiers.add(candidate_id)
        accepted.append(
            {
                "background": [list(point) for point in background],
                "identifier": candidate_id,
                "outside_side_four_chart": any(
                    not (0 <= x < SIDE and 0 <= y < SIDE) for x, y in background
                ),
            }
        )

    require(sum(item["outside_side_four_chart"] for item in accepted) == 4, "exterior acceptance census")

    return {
        "schema": "exact-recurrent-first-host-raw-lineage-promotion-gap/v1",
        "scope": {
            "host_id": HOST_ID,
            "blocker_id": BLOCKER_ID,
            "side": SIDE,
            "target": list(TARGET),
            "deletions": [list(edge) for edge in DELETIONS],
        },
        "projected_record": {
            "host_edges": [list(edge) for edge in projected_edges],
            "target_is_host_edge": False,
            "response_table": response_table(projected_responses),
            "direct_installed_validator_result": {
                "accepted": False,
                "reason": direct_rejection,
            },
        },
        "target_augmented_record": {
            "host_edges": [list(edge) for edge in augmented_edges],
            "target_is_host_edge": True,
            "response_table": response_table(augmented_responses),
            "new_responses_relative_to_projection": ["1032", "1230"],
            "projected_response_count_reuse_result": {
                "accepted": False,
                "reason": stale_rejection,
            },
        },
        "background_domain_audit": {
            "installed_checks": ["background points are unique"],
            "not_installed": [
                "integer coordinate type",
                "coordinate bounds by side",
                "disjointness from host edges",
                "disjointness from response points",
                "physical owner or deletion-cause realization",
                "declared batch completeness",
            ],
            "accepted_records": accepted,
            "accepted_exterior_strict_backgrounds": 4,
        },
        "aggregate": {
            "projected_host_edges": 9,
            "projected_responses": 2,
            "target_augmented_host_edges": 10,
            "target_augmented_responses": 4,
            "new_target_using_responses": 2,
            "accepted_distinct_background_records": 5,
            "accepted_exterior_strict_background_records": 4,
        },
        "conclusion": {
            "direct_field_copy_promotion_valid": 0,
            "target_convention_reconciled": 0,
            "background_coordinate_domain_proved": 0,
            "physical_first_host_batch_populated": 0,
        },
        "honesty": {
            "physical_background_realizability_proved": 0,
            "physical_background_exclusion_proved": 0,
            "deletion_causes_populated": 0,
            "legal_operations_populated": 0,
            "recurrent_child_rows_populated": 0,
            "strict_lyapunov_certificate_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def validate(manifest: dict[str, Any]) -> None:
    require(manifest == compile_manifest(), "manifest differs from exact compiler")
    require(manifest["conclusion"]["direct_field_copy_promotion_valid"] == 0, "promotion honesty")
    require(manifest["honesty"]["all_n_proved_by_checker"] == 0, "all-n honesty")


def mutation_audit(manifest: dict[str, Any]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(projected_host_edges=10),
        lambda item: item["aggregate"].update(projected_responses=3),
        lambda item: item["aggregate"].update(target_augmented_responses=3),
        lambda item: item["projected_record"].update(target_is_host_edge=True),
        lambda item: item["projected_record"]["direct_installed_validator_result"].update(accepted=True),
        lambda item: item["target_augmented_record"]["new_responses_relative_to_projection"].pop(),
        lambda item: item["target_augmented_record"]["projected_response_count_reuse_result"].update(accepted=True),
        lambda item: item["background_domain_audit"].update(accepted_exterior_strict_backgrounds=3),
        lambda item: item["background_domain_audit"]["accepted_records"].pop(),
        lambda item: item["conclusion"].update(direct_field_copy_promotion_valid=1),
        lambda item: item["honesty"].update(physical_background_exclusion_proved=1),
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
        arguments.write.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if arguments.check:
        validate(json.loads(arguments.check.read_text(encoding="utf-8")))
    print(json.dumps({
        "checker": "exact-recurrent-first-host-raw-lineage-promotion-gap",
        **manifest["aggregate"],
        "mutation_corruptions_rejected": mutation_audit(manifest),
        **manifest["conclusion"],
        **manifest["honesty"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
