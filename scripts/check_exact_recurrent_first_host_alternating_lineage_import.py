#!/usr/bin/env python3
"""Audit the alternating-core lineage quotient at the first residual host."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any


class AlternatingLineageImportError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AlternatingLineageImportError(message)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_background(background: list[str]) -> tuple[str, ...]:
    return tuple(sorted(background))


def build_manifest(root: Path) -> dict[str, Any]:
    safe = load_json(
        root / "data/exact_recurrent_first_host_forbidden_background_invariance.json"
    )
    coverage = load_json(
        root / "data/exact_recurrent_first_host_physical_source_coverage.json"
    )

    rows = safe["rows"]
    require(len(rows) == 32, "safe background count")

    expected_face = ["2031", "2310", "3201"]
    classes: dict[int, list[tuple[str, ...]]] = {}
    score_vectors: dict[int, dict[str, int]] = {}
    for row in rows:
        offset = int(row["offset"])
        classes.setdefault(offset, []).append(canonical_background(row["background"]))
        require(row["minimizer_face"] == expected_face, "safe minimizer face")
        score_vectors.setdefault(offset, row["scores"])
        require(score_vectors[offset] == row["scores"], "score class consistency")

    require(sorted(classes) == [0, 1, 2], "exact score class offsets")
    require({key: len(value) for key, value in classes.items()} == {0: 20, 1: 8, 2: 4}, "score class census")

    required_fields = coverage["aggregate"]["required_physical_fields"]
    populated_fields = coverage["aggregate"]["source_backed_physical_fields"]
    require(required_fields == 16, "physical field count")
    require(populated_fields == 0, "physical fields remain unpopulated")

    score_classes = []
    for offset in sorted(classes):
        score_classes.append(
            {
                "offset": offset,
                "background_count": len(classes[offset]),
                "score_vector": score_vectors[offset],
                "minimizer_face": expected_face,
                "original_response_in_minimizer_face": 0,
            }
        )

    return {
        "schema": "exact-recurrent-first-host-alternating-lineage-import/v1",
        "scope": {
            "host_id": "s4-75b04c45c1c8eac2",
            "deletions": ["02", "20"],
            "background_class": "chart-confined response-disjoint safe class",
            "alternating_core_branch": "research/alternating-core-chain",
        },
        "alternating_core_contracts": [
            {
                "path": "docs/alternating-core-occurrence-lineage-gates.md",
                "blob_sha": "9fef497dd4b3a7689b92c0a6c5fe0d1208b8922d",
                "required_interface": "registered occurrence continuation edges and canonical false-to-true gates",
            },
            {
                "path": "docs/alternating-core-physical-signature-lineage-quotient.md",
                "blob_sha": "51df0c27bd8d079768837d1a8bf9a295939f7835",
                "required_interface": "finite payment-complete physical signatures with shared quotient capacities",
            },
            {
                "path": "docs/alternating-core-physical-arithmetic-profile-bound.md",
                "blob_sha": "04047aece5045f81190b36ab6135241e026bc09f",
                "required_interface": "physically determinant-realized arithmetic labels",
            },
            {
                "path": "docs/alternating-core-cross-branch-event-interfaces.md",
                "blob_sha": "5e81effba9c48a268f4e165d685e62dd4d2d54b5",
                "required_interface": "declared physical hypotheses for imported event-cost terms",
            },
        ],
        "aggregate": {
            "safe_backgrounds": 32,
            "exact_complete_score_classes": 3,
            "score_class_census": {str(key): len(value) for key, value in sorted(classes.items())},
            "required_physical_fields": required_fields,
            "source_backed_physical_fields": populated_fields,
            "registered_occurrence_continuation_edges": 0,
            "shared_gate_capacities_populated": 0,
        },
        "score_classes": score_classes,
        "import_gate": {
            "finite_selector_score_signature_alphabet": 1,
            "original_response_currentness_factors_through_score_class": 1,
            "payment_complete_physical_signature_proved": 0,
            "all_legal_operations_factor_through_score_class": 0,
            "all_child_rows_factor_through_score_class": 0,
            "occurrence_identity_continuation_graph_populated": 0,
            "shared_capacity_accounting_populated": 0,
            "alternating_core_recurrence_closure_import_allowed": 0,
        },
        "conclusion": {
            "three_class_score_quotient_exact_on_safe_backgrounds": 1,
            "three_class_quotient_is_payment_complete": 0,
            "alternating_core_contract_supplies_first_host_occurrence_data": 0,
            "promotion_to_recurrent_row_allowed": 0,
        },
        "honesty": {
            "physical_chart_confinement_proved": 0,
            "physical_occurrence_coverage_proved": 0,
            "recurrent_child_rows_populated": 0,
            "strict_lyapunov_certificate_proved": 0,
            "global_termination_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def validate_manifest(manifest: dict[str, Any]) -> None:
    require(manifest.get("schema") == "exact-recurrent-first-host-alternating-lineage-import/v1", "schema")
    aggregate = manifest.get("aggregate", {})
    require(aggregate.get("safe_backgrounds") == 32, "safe backgrounds")
    require(aggregate.get("exact_complete_score_classes") == 3, "score class count")
    require(aggregate.get("score_class_census") == {"0": 20, "1": 8, "2": 4}, "score class census")
    require(aggregate.get("required_physical_fields") == 16, "required fields")
    require(aggregate.get("source_backed_physical_fields") == 0, "populated fields")
    require(aggregate.get("registered_occurrence_continuation_edges") == 0, "continuation edges")
    require(aggregate.get("shared_gate_capacities_populated") == 0, "shared capacities")

    score_classes = manifest.get("score_classes", [])
    require([row.get("offset") for row in score_classes] == [0, 1, 2], "score offsets")
    require([row.get("background_count") for row in score_classes] == [20, 8, 4], "class sizes")
    for row in score_classes:
        offset = row["offset"]
        require(
            row.get("score_vector")
            == {
                "2031": offset,
                "2310": offset,
                "3012": offset + 1,
                "3201": offset,
                "3210": offset + 4,
            },
            "score vector",
        )
        require(row.get("minimizer_face") == ["2031", "2310", "3201"], "minimizer face")
        require(row.get("original_response_in_minimizer_face") == 0, "original response currentness")

    contracts = manifest.get("alternating_core_contracts", [])
    require(len(contracts) == 4, "alternating contract count")
    for contract in contracts:
        require(contract.get("path", "").startswith("docs/alternating-core-"), "contract path")
        require(len(contract.get("blob_sha", "")) == 40, "contract blob sha")
        require(bool(contract.get("required_interface")), "contract interface")

    gate = manifest.get("import_gate", {})
    require(gate.get("finite_selector_score_signature_alphabet") == 1, "finite score alphabet")
    require(gate.get("original_response_currentness_factors_through_score_class") == 1, "currentness factorization")
    for key in (
        "payment_complete_physical_signature_proved",
        "all_legal_operations_factor_through_score_class",
        "all_child_rows_factor_through_score_class",
        "occurrence_identity_continuation_graph_populated",
        "shared_capacity_accounting_populated",
        "alternating_core_recurrence_closure_import_allowed",
    ):
        require(gate.get(key) == 0, f"gate {key}")

    conclusion = manifest.get("conclusion", {})
    require(conclusion.get("three_class_score_quotient_exact_on_safe_backgrounds") == 1, "score quotient")
    for key in (
        "three_class_quotient_is_payment_complete",
        "alternating_core_contract_supplies_first_host_occurrence_data",
        "promotion_to_recurrent_row_allowed",
    ):
        require(conclusion.get(key) == 0, f"conclusion {key}")

    honesty = manifest.get("honesty", {})
    for key in honesty:
        require(honesty[key] == 0, f"honesty {key}")


def mutation_audit(manifest: dict[str, Any]) -> int:
    mutations = [
        lambda x: x["aggregate"].update(safe_backgrounds=31),
        lambda x: x["aggregate"].update(exact_complete_score_classes=2),
        lambda x: x["aggregate"].update(score_class_census={"0": 32}),
        lambda x: x["aggregate"].update(source_backed_physical_fields=1),
        lambda x: x["aggregate"].update(registered_occurrence_continuation_edges=1),
        lambda x: x["score_classes"][0].update(background_count=19),
        lambda x: x["score_classes"][1]["score_vector"].update({"3012": 1}),
        lambda x: x["import_gate"].update(payment_complete_physical_signature_proved=1),
        lambda x: x["import_gate"].update(alternating_core_recurrence_closure_import_allowed=1),
        lambda x: x["conclusion"].update(promotion_to_recurrent_row_allowed=1),
        lambda x: x["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(manifest)
        mutate(candidate)
        try:
            validate_manifest(candidate)
        except AlternatingLineageImportError:
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
    raise AlternatingLineageImportError("unable to locate repository root")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()

    root = repository_root()
    manifest = build_manifest(root)
    validate_manifest(manifest)

    if args.check:
        expected = load_json(args.check)
        require(expected == manifest, "manifest mismatch")

    rejected = mutation_audit(manifest)
    print(
        "verified alternating-core first-host import gate: "
        f"{manifest['aggregate']['safe_backgrounds']} safe backgrounds, "
        f"{manifest['aggregate']['exact_complete_score_classes']} score classes, "
        f"{rejected} rejected corruptions and recurrence import disabled"
    )


if __name__ == "__main__":
    main()
