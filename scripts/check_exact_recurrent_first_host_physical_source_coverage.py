#!/usr/bin/env python3
"""Audit source-backed coverage of the first-host physical fibre worklist."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

HOST_ID = "s4-75b04c45c1c8eac2"
RAW_PATH = "data/prime_power_side_four_raw_fibre_lineage_manifest.json"
SELECTED_PATH = "data/prime_power_side_four_selected_response_provenance_manifest.json"
BRIDGE_PATH = "data/exact_recurrent_first_host_dual_edge_bridge.json"
LINE_PATH = "data/exact_recurrent_side_four_selected_line_geometry.json"
KERNEL_PATH = "data/exact_recurrent_side_four_kernel.json"
MOMENT_PATH = "data/exact_recurrent_first_host_occupancy_moments.json"
REGISTRY_PATH = "scripts/extend_prime_power_installed_operation_registry_1166.py"
EXPECTED_RAW_DIGEST = "84ad1c92a9e0bcfb4d1f613e05edec20c4300022d96269ed561b45d32bf7432f"
EXPECTED_SELECTED_DIGEST = "0eb284dd945b3022b529551c5d5f0407884f8ed1958de02b58e3cff024f5a4e6"
REQUIRED_FIELDS = (
    "coordinate_domain.physical_embedding_ref",
    "physical_source_ref",
    "deletion_causes.02",
    "deletion_causes.20",
    "provenance.owner",
    "provenance.fate",
    "provenance.collision",
    "provenance.line",
    "provenance.interface",
    "provenance.crt",
    "legal_operations",
    "intermediate_states",
    "child_row",
    "positive_weights",
    "parent_budget",
    "realization_status",
)


class AuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AuditError(message)


def canonical_digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def repository_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__).resolve()).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "STATUS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise AuditError("unable to locate repository root")


def load_json(root: Path, relative: str) -> dict[str, Any]:
    path = root / relative
    require(path.is_file(), f"missing source artifact: {relative}")
    value = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(value, dict), f"source object required: {relative}")
    return value


def coverage_rows() -> list[dict[str, Any]]:
    return [
        {"field": "coordinate_domain.physical_embedding_ref", "physical_populated": 0, "nearest_evidence_class": "schema-only", "source_paths": [BRIDGE_PATH], "evidence": "relative-affine-integer is declared but physical_embedding_ref is null"},
        {"field": "physical_source_ref", "physical_populated": 0, "nearest_evidence_class": "none", "source_paths": [BRIDGE_PATH], "evidence": "schema completions carry no construction trace reference"},
        {"field": "deletion_causes.02", "physical_populated": 0, "nearest_evidence_class": "deletion-presence-only", "source_paths": [RAW_PATH, BRIDGE_PATH], "evidence": "cell 02 is deleted but no physical cause or owner is attached"},
        {"field": "deletion_causes.20", "physical_populated": 0, "nearest_evidence_class": "deletion-presence-only", "source_paths": [RAW_PATH, BRIDGE_PATH], "evidence": "cell 20 is deleted but no physical cause or owner is attached"},
        {"field": "provenance.owner", "physical_populated": 0, "nearest_evidence_class": "normalized-only", "source_paths": [SELECTED_PATH], "evidence": "owner_scope is side-four-raw-host, not a physical owner identity"},
        {"field": "provenance.fate", "physical_populated": 0, "nearest_evidence_class": "normalized-only", "source_paths": [SELECTED_PATH], "evidence": "selected host fate B is normalized and has no physical ancestry"},
        {"field": "provenance.collision", "physical_populated": 0, "nearest_evidence_class": "normalized-only", "source_paths": [SELECTED_PATH], "evidence": "collision key is the deletion trace 02,20 rather than a physical collision record"},
        {"field": "provenance.line", "physical_populated": 0, "nearest_evidence_class": "intrinsic-geometry-only", "source_paths": [SELECTED_PATH, LINE_PATH], "evidence": "selected response lies on x-y-1=0, but physical line ownership is absent"},
        {"field": "provenance.interface", "physical_populated": 0, "nearest_evidence_class": "normalized-only", "source_paths": [SELECTED_PATH], "evidence": "interface target-01 is normalized and not linked to a physical occurrence"},
        {"field": "provenance.crt", "physical_populated": 0, "nearest_evidence_class": "normalized-only", "source_paths": [SELECTED_PATH], "evidence": "crt_scope not-applied is normalized and not a physical CRT ancestry record"},
        {"field": "legal_operations", "physical_populated": 0, "nearest_evidence_class": "catalog-only", "source_paths": [REGISTRY_PATH], "evidence": "operation kinds are registered globally but none is selected for this occurrence"},
        {"field": "intermediate_states", "physical_populated": 0, "nearest_evidence_class": "local-candidate-only", "source_paths": [KERNEL_PATH], "evidence": "local restorations 02 and 20 expose responses, but no installed physical trace is populated"},
        {"field": "child_row", "physical_populated": 0, "nearest_evidence_class": "none", "source_paths": [BRIDGE_PATH], "evidence": "no labelled child coefficients or multiplicities are present"},
        {"field": "positive_weights", "physical_populated": 0, "nearest_evidence_class": "none", "source_paths": [BRIDGE_PATH], "evidence": "no positive child or parent Lyapunov weights are present"},
        {"field": "parent_budget", "physical_populated": 0, "nearest_evidence_class": "upper-bound-only", "source_paths": [MOMENT_PATH], "evidence": "E2=69 is a background upper certificate; destroyed load or parent budget is explicitly unpopulated"},
        {"field": "realization_status", "physical_populated": 0, "nearest_evidence_class": "schema-only", "source_paths": [BRIDGE_PATH], "evidence": "records are marked schema-completion-only rather than realized or source-excluded"},
    ]


def expected_manifest() -> dict[str, Any]:
    rows = coverage_rows()
    census = Counter(row["nearest_evidence_class"] for row in rows)
    return {
        "schema": "exact-recurrent-first-host-physical-source-coverage/v1",
        "scope": {"host_id": HOST_ID, "deletions": ["02", "20"], "required_physical_fields": list(REQUIRED_FIELDS)},
        "source_artifacts": [
            {"path": RAW_PATH, "role": "host-response projection"},
            {"path": SELECTED_PATH, "role": "normalized selector provenance"},
            {"path": BRIDGE_PATH, "role": "dual-edge schema and missing-field worklist"},
            {"path": LINE_PATH, "role": "intrinsic selected-line geometry"},
            {"path": KERNEL_PATH, "role": "local reopening candidates"},
            {"path": MOMENT_PATH, "role": "coarse background upper certificate"},
            {"path": REGISTRY_PATH, "role": "global installed operation catalogue"},
        ],
        "field_coverage": rows,
        "aggregate": {
            "required_physical_fields": len(rows),
            "source_backed_physical_fields": sum(row["physical_populated"] for row in rows),
            "unpopulated_physical_fields": sum(not row["physical_populated"] for row in rows),
            "nearest_evidence_class_census": dict(sorted(census.items())),
            "physical_occurrence_records_found": 0,
        },
        "conclusion": {"normalized_or_structural_surrogate_counts_as_physical": 0, "first_host_physical_source_coverage_complete": 0, "promotion_to_recurrent_row_allowed": 0},
        "honesty": {"physical_background_realizability_proved": 0, "physical_background_exclusion_proved": 0, "legal_operations_populated": 0, "recurrent_child_rows_populated": 0, "strict_lyapunov_certificate_proved": 0, "all_n_proved_by_checker": 0},
    }


def audit_sources(root: Path) -> None:
    raw = load_json(root, RAW_PATH)
    selected = load_json(root, SELECTED_PATH)
    bridge = load_json(root, BRIDGE_PATH)
    line = load_json(root, LINE_PATH)
    kernel = load_json(root, KERNEL_PATH)
    moment = load_json(root, MOMENT_PATH)
    registry_path = root / REGISTRY_PATH
    require(registry_path.is_file(), "operation registry source missing")
    registry = registry_path.read_text(encoding="utf-8")

    require(canonical_digest(raw) == EXPECTED_RAW_DIGEST, "raw projection digest")
    require(canonical_digest(selected) == EXPECTED_SELECTED_DIGEST, "selected provenance digest")

    raw_host = next((row for row in raw.get("hosts", []) if row[0] == HOST_ID), None)
    require(raw_host is not None, "raw first host missing")
    require(raw_host[1] == "02,20", "raw deletion trace")
    require(raw_host[2] == ["3012:1", "3210:4"], "raw response family")

    selected_host = next((row for row in selected.get("hosts", []) if row[0] == HOST_ID), None)
    require(selected_host is not None, "selected first host missing")
    require(selected_host[1:6] == ["3012", "3012", 1, 3, "B"], "selected first-host fields")
    require(selected_host[7] == "02,20", "selected collision key")
    normalized = selected.get("normalized_provenance", {})
    require(normalized.get("owner_scope") == "side-four-raw-host", "normalized owner")
    require(normalized.get("local_line_class") == "minimum-response-energy", "normalized line")
    require(normalized.get("interface") == "target-01", "normalized interface")
    require(normalized.get("crt_scope") == "not-applied", "normalized crt")

    completions = bridge.get("schema_completions", [])
    require(len(completions) == 2, "bridge completion census")
    for completion in completions:
        require(tuple(completion.get("missing_physical_fields", [])) == REQUIRED_FIELDS, "bridge worklist")
        require(completion.get("complete") is False, "bridge completion honesty")
    require(bridge.get("aggregate", {}).get("missing_physical_fields_per_record") == 16, "bridge field census")

    first_line = next((row for row in line.get("hosts", []) if row.get("upstream_id") == HOST_ID), None)
    require(first_line == {"class_id": "selected-line-3012", "selector": "3012", "upstream_id": HOST_ID}, "line host join")
    line_class = next((row for row in line.get("classes", []) if row.get("id") == "selected-line-3012"), None)
    require(line_class is not None and line_class.get("line_equation") == "x-y-1=0", "selected line equation")
    require(line.get("honesty", {}).get("physical_line_owner_complete") == 0, "line owner honesty")

    residual = next((row for row in kernel.get("residual_hosts", []) if row.get("deletions") == ["02", "20"]), None)
    require(residual is not None, "kernel first host missing")
    require(residual.get("minimum_reopenings") == [{"available_good_responses": ["2031", "2310"], "restore": ["02"]}, {"available_good_responses": ["3201"], "restore": ["20"]}], "local reopening candidates")
    require(kernel.get("honesty", {}).get("legal_global_reopening_proved") == 0, "reopening honesty")

    require(moment.get("aggregate", {}).get("E2") == 69, "moment certificate")
    require(moment.get("honesty", {}).get("destroyed_load_or_parent_budget_populated") == 0, "parent budget honesty")

    require("rank-three-zero-response-strict-dispatch|CMR1963" in registry, "registered strict dispatch")
    require(HOST_ID not in registry, "registry unexpectedly selects a first-host occurrence")


def compile_manifest(root: Path) -> dict[str, Any]:
    audit_sources(root)
    return expected_manifest()


def validate(manifest: dict[str, Any], root: Path) -> None:
    require(manifest == compile_manifest(root), "manifest differs from exact source audit")
    rows = manifest.get("field_coverage")
    require(isinstance(rows, list) and len(rows) == 16, "field coverage rows")
    require([row.get("field") for row in rows] == list(REQUIRED_FIELDS), "required field ordering")
    require(all(row.get("physical_populated") == 0 for row in rows), "unsupported physical field promoted")
    require(manifest.get("honesty", {}).get("all_n_proved_by_checker") == 0, "all-n honesty")


def mutation_audit(manifest: dict[str, Any], root: Path) -> int:
    mutations = [
        lambda item: item["aggregate"].update(required_physical_fields=15),
        lambda item: item["aggregate"].update(source_backed_physical_fields=1),
        lambda item: item["aggregate"].update(physical_occurrence_records_found=1),
        lambda item: item["field_coverage"][0].update(physical_populated=1),
        lambda item: item["field_coverage"][4].update(nearest_evidence_class="physical"),
        lambda item: item["field_coverage"].pop(),
        lambda item: item["scope"].update(host_id="corrupt"),
        lambda item: item["source_artifacts"].pop(),
        lambda item: item["conclusion"].update(first_host_physical_source_coverage_complete=1),
        lambda item: item["conclusion"].update(promotion_to_recurrent_row_allowed=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(manifest)
        mutate(candidate)
        try:
            validate(candidate, root)
        except (AuditError, KeyError, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "mutation audit")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path)
    parser.add_argument("--check", type=Path)
    arguments = parser.parse_args()
    root = repository_root()
    manifest = compile_manifest(root)
    if arguments.write:
        arguments.write.parent.mkdir(parents=True, exist_ok=True)
        arguments.write.write_text(json.dumps(manifest, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    if arguments.check:
        observed = json.loads(arguments.check.read_text(encoding="utf-8"))
        validate(observed, root)
    print(json.dumps({"checker": "exact-recurrent-first-host-physical-source-coverage", **manifest["aggregate"], "mutation_corruptions_rejected": mutation_audit(manifest, root), **manifest["honesty"]}, sort_keys=True))


if __name__ == "__main__":
    main()
