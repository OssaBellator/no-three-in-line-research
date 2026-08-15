#!/usr/bin/env python3
"""Validate collision and interface dependencies on reoptimized sample responses."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any


class ReoptimizedCollisionInterfaceError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ReoptimizedCollisionInterfaceError(message)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


SCORES_PATH = "data/prime_power_side_four_joint_sample_complete_line_selector_scores.json"
ROUTING_PATH = "data/prime_power_side_four_reoptimized_minimizer_return_routing.json"
ZERO_SAMPLE_PATH = "data/prime_power_side_four_actual_background_sample_batch.json"
BLOCKER_SAMPLE_PATH = "data/prime_power_side_four_blocker_actual_background_sample_batch.json"
DEPENDENCY_PATH = "data/prime_power_side_four_reoptimized_collision_interface_dependency.json"

EXPECTED_SCORES_SHA256 = "c5a7f78ddef889aacdffc152b40945ed4b798f850c9aecbd20d4428f9ea63d0e"
EXPECTED_ROUTING_SHA256 = "de7742146a77134b97d3ccb36c6112bd458cf8920e346c2e9e515777a9c5b2b6"
EXPECTED_ZERO_SAMPLE_SHA256 = "71ba5fcea70f61c5e94e40a635b7eddaa8cb72c8c0cdda9fb78f0f56a84609a0"
EXPECTED_BLOCKER_SAMPLE_SHA256 = "39677a7e68826f9bf9702d3af8f3b4218138fa0bb1d885c6801d220dddcabeaf"
EXPECTED_DEPENDENCY_SHA256 = "e76551e4c6021a3c32f3536bb7891175da419c6354031104800ab58918ca977e"

COLLISION_MISSING = [
    "collision_offspring_enumeration",
    "collision_coefficient_rule",
    "collision_child_key",
    "collision_child_weight",
    "global_transition_occurrence",
]
INTERFACE_MISSING = [
    "child_interface_route",
    "interface_coefficient_rule",
    "interface_multiplicity",
    "interface_child_key",
    "interface_child_weight",
    "factor_tuple_provenance",
    "global_transition_occurrence",
]


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "data").is_dir():
            return candidate
    raise ReoptimizedCollisionInterfaceError("unable to locate repository root")


def response_edges(response: str) -> list[str]:
    require(len(response) == 4 and set(response) == set("0123"), "response permutation")
    return [f"{source}{response[source]}" for source in range(4)]


def deleted_edges(collision_key: str) -> set[str]:
    return set() if collision_key == "-" else set(collision_key.split(","))


def record(
    *,
    scope: str,
    response: str,
    profile: dict[str, Any],
) -> dict[str, Any]:
    edges = response_edges(response)
    collision_key = profile.get("collision_key", "-")
    target = "01"
    return {
        "scope": scope,
        "host_id": profile["host_id"],
        "response": response,
        "response_edges": edges,
        "source_fate": profile.get("selected_fate", "zero-response"),
        "collision_key": collision_key,
        "blockers": profile.get("blockers", []),
        "interface_label": "side4-target01",
        "interface_provenance": profile["interface_provenance"],
        "crt_provenance": profile["crt_provenance"],
        "target_edge": target,
        "response_uses_target_edge": int(target in edges),
        "response_uses_deleted_edge": int(bool(set(edges) & deleted_edges(collision_key))),
        "collision_dependency": {
            "status": "unresolved",
            "known_inputs": ["source_fate", "collision_key", "blockers", "response_edges"],
            "missing_inputs": COLLISION_MISSING,
        },
        "interface_dependency": {
            "status": "unresolved",
            "known_inputs": [
                "interface_label",
                "interface_provenance",
                "crt_provenance",
                "target_edge",
                "response_edges",
            ],
            "missing_inputs": INTERFACE_MISSING,
        },
    }


def validate(
    scores: dict[str, Any],
    routing: dict[str, Any],
    zero_sample: dict[str, Any],
    blocker_sample: dict[str, Any],
    dependency: dict[str, Any],
) -> None:
    require(digest(scores) == EXPECTED_SCORES_SHA256, "selector-score digest")
    require(digest(routing) == EXPECTED_ROUTING_SHA256, "return-routing digest")
    require(digest(zero_sample) == EXPECTED_ZERO_SAMPLE_SHA256, "zero-sample digest")
    require(digest(blocker_sample) == EXPECTED_BLOCKER_SAMPLE_SHA256, "blocker-sample digest")
    require(digest(dependency) == EXPECTED_DEPENDENCY_SHA256, "dependency digest")
    require(
        dependency["inputs"]
        == {
            "selector_score_contract_sha256": EXPECTED_SCORES_SHA256,
            "reoptimized_return_contract_sha256": EXPECTED_ROUTING_SHA256,
            "zero_sample_sha256": EXPECTED_ZERO_SAMPLE_SHA256,
            "blocker_sample_sha256": EXPECTED_BLOCKER_SAMPLE_SHA256,
        },
        "dependency input bindings",
    )

    zero_responses = [
        row["response"] for row in routing["rows"]["zero"]["candidate_responses"]
    ]
    require(zero_responses == ["2301", "2310", "3201"], "zero response face")
    blocker_response = routing["rows"]["blocker"]["candidate_response"]
    require(blocker_response == "3210", "blocker response")

    expected = [
        record(scope="zero", response=response, profile=zero_sample["profile"])
        for response in zero_responses
    ]
    expected.append(
        record(scope="blocker", response=blocker_response, profile=blocker_sample["profile"])
    )
    require(dependency["records"] == expected, "compiled dependency records")
    require(len(expected) == 4, "four candidate response records")
    require(all(item["response_uses_target_edge"] == 0 for item in expected), "target exclusion")
    require(all(item["response_uses_deleted_edge"] == 0 for item in expected), "deleted-edge exclusion")
    require([item["scope"] for item in expected].count("zero") == 3, "zero record count")
    require([item["scope"] for item in expected].count("blocker") == 1, "blocker record count")
    for item in expected:
        require(item["collision_dependency"]["status"] == "unresolved", "collision status")
        require(item["collision_dependency"]["missing_inputs"] == COLLISION_MISSING, "collision missing inputs")
        require(item["interface_dependency"]["status"] == "unresolved", "interface status")
        require(item["interface_dependency"]["missing_inputs"] == INTERFACE_MISSING, "interface missing inputs")

    require(
        dependency["aggregate"]
        == {
            "candidate_responses": 4,
            "zero_candidates": 3,
            "blocker_candidates": 1,
            "collision_dependency_records": 4,
            "interface_dependency_records": 4,
            "collision_coefficients_populated": 0,
            "interface_coefficients_populated": 0,
            "collision_child_bindings_populated": 0,
            "interface_child_bindings_populated": 0,
            "zero_tie_preserved": 1,
        },
        "dependency aggregate",
    )
    require(
        dependency["rules"]
        == {
            "collision_boundary": "a deletion trace or blocker label is not a numerical collision coefficient without exact offspring enumeration and routing",
            "interface_boundary": "a local target/interface label is not a child-interface route or multiplicity",
            "zero_tie_boundary": "all three zero candidates remain active until complete coupled terms break the tie",
            "global_boundary": "coordinate sample labels do not prove global transition occurrence or installed child weights",
        },
        "dependency rules",
    )
    require(
        dependency["honesty"]
        == {
            "joint_sample_reoptimized_collision_interface_dependency_complete": 1,
            "collision_coefficients_complete": 0,
            "interface_coefficients_complete": 0,
            "collision_child_bindings_complete": 0,
            "interface_child_bindings_complete": 0,
            "joint_sample_complete_coupled_selector_terms_complete": 0,
            "joint_sample_full_compulsory_rows_complete": 0,
            "global_binding_constructed": 0,
            "complete_weighted_rows_strict": 0,
            "all_n_proved_by_checker": 0,
        },
        "dependency honesty",
    )


def mutation_audit(
    scores: dict[str, Any],
    routing: dict[str, Any],
    zero_sample: dict[str, Any],
    blocker_sample: dict[str, Any],
    dependency: dict[str, Any],
) -> int:
    mutations = [
        lambda item: item["records"].pop(),
        lambda item: item["records"][0].update(response="2031"),
        lambda item: item["records"][0]["response_edges"].pop(),
        lambda item: item["records"][0].update(response_uses_target_edge=1),
        lambda item: item["records"][3].update(response_uses_deleted_edge=1),
        lambda item: item["records"][3].update(collision_key="-"),
        lambda item: item["records"][3]["blockers"].clear(),
        lambda item: item["records"][0]["collision_dependency"].update(status="known"),
        lambda item: item["records"][0]["collision_dependency"]["missing_inputs"].pop(),
        lambda item: item["records"][0]["interface_dependency"].update(status="known"),
        lambda item: item["records"][0]["interface_dependency"]["missing_inputs"].pop(),
        lambda item: item["aggregate"].update(collision_coefficients_populated=1),
        lambda item: item["aggregate"].update(zero_tie_preserved=0),
        lambda item: item["rules"].update(collision_boundary="collision key is coefficient"),
        lambda item: item["honesty"].update(joint_sample_complete_coupled_selector_terms_complete=1),
        lambda item: item["honesty"].update(complete_weighted_rows_strict=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        bad = copy.deepcopy(dependency)
        mutate(bad)
        try:
            validate(scores, routing, zero_sample, blocker_sample, bad)
        except ReoptimizedCollisionInterfaceError:
            rejected += 1
    require(rejected == len(mutations), "collision/interface corruption accepted")
    return rejected


def main() -> None:
    root = repository_root()
    scores = json.loads((root / SCORES_PATH).read_text(encoding="utf-8"))
    routing = json.loads((root / ROUTING_PATH).read_text(encoding="utf-8"))
    zero_sample = json.loads((root / ZERO_SAMPLE_PATH).read_text(encoding="utf-8"))
    blocker_sample = json.loads((root / BLOCKER_SAMPLE_PATH).read_text(encoding="utf-8"))
    dependency = json.loads((root / DEPENDENCY_PATH).read_text(encoding="utf-8"))
    validate(scores, routing, zero_sample, blocker_sample, dependency)
    print(json.dumps({
        "checker": "prime-power-side-four-reoptimized-collision-interface-dependency",
        "contract_sha256": EXPECTED_DEPENDENCY_SHA256,
        "candidate_response_count": 4,
        "collision_dependency_record_count": 4,
        "interface_dependency_record_count": 4,
        "collision_coefficient_count": 0,
        "interface_coefficient_count": 0,
        "zero_tie_preserved": 1,
        "rejected_corruptions": mutation_audit(
            scores, routing, zero_sample, blocker_sample, dependency
        ),
        "joint_sample_reoptimized_collision_interface_dependency_complete": 1,
        "collision_coefficients_complete": 0,
        "interface_coefficients_complete": 0,
        "collision_child_bindings_complete": 0,
        "interface_child_bindings_complete": 0,
        "joint_sample_complete_coupled_selector_terms_complete": 0,
        "joint_sample_full_compulsory_rows_complete": 0,
        "global_binding_constructed": 0,
        "complete_weighted_rows_strict": 0,
        "all_n_proved_by_checker": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
