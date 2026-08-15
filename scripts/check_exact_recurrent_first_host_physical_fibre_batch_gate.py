#!/usr/bin/env python3
"""Reject incomplete first-host physical fibre batches by default."""
from __future__ import annotations

import argparse
import copy
import json
from fractions import Fraction
from itertools import permutations
from pathlib import Path
from typing import Any

HOST_ID = "s4-75b04c45c1c8eac2"
BRIDGE_PATH = "data/exact_recurrent_first_host_dual_edge_bridge.json"
COVERAGE_PATH = "data/exact_recurrent_first_host_physical_source_coverage.json"
EXPECTED_RESPONSES = ("3012", "3210")
PROVENANCE_FIELDS = ("owner", "fate", "collision", "line", "interface", "crt")
FORBIDDEN_SOURCE_VALUES = {"", "unknown", "todo", "none", "null", "schema-completion-only", "normalized-only", "catalog-only", "local-candidate-only", "upper-bound-only"}


class AuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AuditError(message)


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


def source_ref(value: Any, field: str) -> str:
    require(isinstance(value, str), f"{field}: source reference string")
    normalized = value.strip()
    require(normalized.lower() not in FORBIDDEN_SOURCE_VALUES, f"{field}: placeholder source reference")
    require(len(normalized) >= 3, f"{field}: source reference too short")
    return normalized


def rational(value: Any, field: str, *, positive: bool = False) -> Fraction:
    require(isinstance(value, (int, str)) and not isinstance(value, bool), f"{field}: rational value")
    try:
        result = Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise AuditError(f"{field}: invalid rational") from error
    require(result > 0 if positive else result >= 0, f"{field}: sign")
    return result


def response_codes(edges: list[list[int]]) -> tuple[str, ...]:
    allowed = {tuple(edge) for edge in edges}
    return tuple("".join(str(permutation[row]) for row in range(4)) for permutation in permutations(range(4)) if all((row, permutation[row]) in allowed for row in range(4)))


def validate_sourced_value(value: Any, field: str) -> None:
    require(isinstance(value, dict), f"{field}: sourced object")
    require(value.get("value") not in (None, ""), f"{field}: value")
    source_ref(value.get("source_ref"), f"{field}.source_ref")


def validate_complete_enumeration(value: Any, field: str) -> None:
    require(isinstance(value, dict), f"{field}: enumeration object")
    require(value.get("scope_complete") is True, f"{field}: scope completeness")
    source_ref(value.get("source_ref"), f"{field}.source_ref")
    require(isinstance(value.get("items"), list), f"{field}: items")
    for index, item in enumerate(value["items"]):
        require(isinstance(item, dict), f"{field}[{index}]: object")
        source_ref(item.get("source_ref"), f"{field}[{index}].source_ref")


def validate_physical_record(record: dict[str, Any], bridge_record: dict[str, Any]) -> None:
    require(isinstance(record.get("occurrence_id"), str) and record["occurrence_id"], "occurrence id")
    require(record.get("host_id") == HOST_ID, "host id")
    require(record.get("side") == 4, "side")
    require(record.get("target") == [0, 1], "target")
    require(record.get("deletions") == [[0, 2], [2, 0]], "deletions")
    require(record.get("lineage_host_edges") == bridge_record.get("lineage_host_edges"), "lineage edges")
    require(record.get("response_edges") == bridge_record.get("response_edges"), "response edges")
    require(response_codes(record["response_edges"]) == EXPECTED_RESPONSES, "response family")

    background = record.get("background")
    require(isinstance(background, list), "background list")
    points = []
    for index, point in enumerate(background):
        require(isinstance(point, list) and len(point) == 2, f"background[{index}]")
        require(all(isinstance(coordinate, int) and not isinstance(coordinate, bool) for coordinate in point), f"background[{index}]: integer coordinates")
        points.append(tuple(point))
    require(len(points) == len(set(points)), "background uniqueness")

    domain = record.get("coordinate_domain")
    require(isinstance(domain, dict), "coordinate domain")
    require(isinstance(domain.get("kind"), str) and domain["kind"], "coordinate domain kind")
    source_ref(domain.get("physical_embedding_ref"), "coordinate_domain.physical_embedding_ref")
    source_ref(record.get("physical_source_ref"), "physical_source_ref")

    causes = record.get("deletion_causes")
    require(isinstance(causes, dict), "deletion causes")
    for cell in ("02", "20"):
        cause = causes.get(cell)
        require(isinstance(cause, dict), f"deletion_causes.{cell}")
        require(isinstance(cause.get("cause"), str) and cause["cause"], f"deletion_causes.{cell}.cause")
        require(isinstance(cause.get("owner"), str) and cause["owner"], f"deletion_causes.{cell}.owner")
        source_ref(cause.get("source_ref"), f"deletion_causes.{cell}.source_ref")

    provenance = record.get("provenance")
    require(isinstance(provenance, dict), "provenance")
    for field in PROVENANCE_FIELDS:
        validate_sourced_value(provenance.get(field), f"provenance.{field}")

    validate_complete_enumeration(record.get("legal_operations"), "legal_operations")
    for index, item in enumerate(record["legal_operations"]["items"]):
        require(isinstance(item.get("operation_kind"), str) and item["operation_kind"], f"legal_operations[{index}].operation_kind")

    validate_complete_enumeration(record.get("intermediate_states"), "intermediate_states")
    for index, item in enumerate(record["intermediate_states"]["items"]):
        require(isinstance(item.get("state_id"), str) and item["state_id"], f"intermediate_states[{index}].state_id")

    child_row = record.get("child_row")
    require(isinstance(child_row, dict), "child row")
    require(child_row.get("complete") is True, "child row completeness")
    source_ref(child_row.get("source_ref"), "child_row.source_ref")
    coefficients = child_row.get("coefficients")
    require(isinstance(coefficients, list), "child row coefficients")
    for index, coefficient in enumerate(coefficients):
        require(isinstance(coefficient, dict), f"child_row[{index}]")
        require(isinstance(coefficient.get("child_label"), str) and coefficient["child_label"], f"child_row[{index}].child_label")
        rational(coefficient.get("multiplicity"), f"child_row[{index}].multiplicity", positive=True)
        source_ref(coefficient.get("source_ref"), f"child_row[{index}].source_ref")

    weights = record.get("positive_weights")
    require(isinstance(weights, dict), "positive weights")
    require(weights.get("complete") is True, "positive weights completeness")
    source_ref(weights.get("source_ref"), "positive_weights.source_ref")
    rational(weights.get("parent"), "positive_weights.parent", positive=True)
    children = weights.get("children")
    require(isinstance(children, dict), "positive_weights.children")
    require(set(children) == {item["child_label"] for item in coefficients}, "child weight labels")
    for label, value in children.items():
        rational(value, f"positive_weights.children.{label}", positive=True)

    budget = record.get("parent_budget")
    require(isinstance(budget, dict), "parent budget")
    rational(budget.get("value"), "parent_budget.value")
    source_ref(budget.get("source_ref"), "parent_budget.source_ref")

    realization = record.get("realization_status")
    require(isinstance(realization, dict), "realization status")
    require(realization.get("value") == "realized", "realization status value")
    source_ref(realization.get("source_ref"), "realization_status.source_ref")


def expected_manifest() -> dict[str, Any]:
    return {
        "schema": "exact-recurrent-first-host-physical-fibre-batch-gate/v1",
        "scope": {"host_id": HOST_ID, "bridge_path": BRIDGE_PATH, "coverage_path": COVERAGE_PATH, "response_family": list(EXPECTED_RESPONSES)},
        "source_scope": {"occurrence_domain_ref": None, "expected_occurrence_count": None, "completeness_proof_ref": None},
        "records": [],
        "declaration": {"batch_complete": False, "physical_coverage_proved": False, "promotion_to_recurrent_row_allowed": False},
        "aggregate": {"records": 0, "accepted_physical_records": 0, "required_source_backed_fields_per_record": 16, "expected_occurrence_count_known": 0, "schema_completion_candidates_rejected": 2},
        "honesty": {"physical_background_realizability_proved": 0, "physical_background_exclusion_proved": 0, "recurrent_child_rows_populated": 0, "strict_lyapunov_certificate_proved": 0, "global_termination_proved": 0, "all_n_proved_by_checker": 0},
    }


def validate_batch_declaration(manifest: dict[str, Any], bridge_record: dict[str, Any]) -> int:
    source_scope = manifest.get("source_scope")
    require(isinstance(source_scope, dict), "source scope")
    records = manifest.get("records")
    require(isinstance(records, list), "records")
    accepted = 0
    occurrence_ids = set()
    for index, record in enumerate(records):
        require(isinstance(record, dict), f"record[{index}]")
        validate_physical_record(record, bridge_record)
        require(record["occurrence_id"] not in occurrence_ids, "duplicate occurrence id")
        occurrence_ids.add(record["occurrence_id"])
        accepted += 1

    declaration = manifest.get("declaration")
    require(isinstance(declaration, dict), "declaration")
    complete = declaration.get("batch_complete")
    require(isinstance(complete, bool), "batch complete boolean")
    if complete:
        source_ref(source_scope.get("occurrence_domain_ref"), "source_scope.occurrence_domain_ref")
        source_ref(source_scope.get("completeness_proof_ref"), "source_scope.completeness_proof_ref")
        expected = source_scope.get("expected_occurrence_count")
        require(isinstance(expected, int) and not isinstance(expected, bool) and expected >= 0, "expected occurrence count")
        require(expected == accepted, "batch occurrence count")
        require(declaration.get("physical_coverage_proved") is True, "physical coverage declaration")
        require(declaration.get("promotion_to_recurrent_row_allowed") is True, "promotion declaration")
    else:
        require(declaration.get("physical_coverage_proved") is False, "incomplete physical coverage")
        require(declaration.get("promotion_to_recurrent_row_allowed") is False, "incomplete promotion")
    return accepted


def compile_manifest(root: Path) -> dict[str, Any]:
    bridge = load_json(root, BRIDGE_PATH)
    coverage = load_json(root, COVERAGE_PATH)
    require(coverage.get("aggregate", {}).get("source_backed_physical_fields") == 0, "coverage source-backed field count")
    require(coverage.get("conclusion", {}).get("promotion_to_recurrent_row_allowed") == 0, "coverage promotion honesty")
    completions = bridge.get("schema_completions", [])
    require(len(completions) == 2, "bridge completion census")
    bridge_record = completions[0].get("record")
    require(isinstance(bridge_record, dict), "bridge record")
    rejected = 0
    for completion in completions:
        candidate = copy.deepcopy(completion.get("record"))
        require(isinstance(candidate, dict), "bridge candidate")
        candidate["occurrence_id"] = completion.get("name", "candidate")
        try:
            validate_physical_record(candidate, bridge_record)
        except AuditError:
            rejected += 1
    require(rejected == 2, "schema completions must fail physical gate")
    return expected_manifest()


def validate(manifest: dict[str, Any], root: Path) -> None:
    bridge = load_json(root, BRIDGE_PATH)
    bridge_record = bridge["schema_completions"][0]["record"]
    accepted = validate_batch_declaration(manifest, bridge_record)
    require(accepted == manifest.get("aggregate", {}).get("accepted_physical_records"), "accepted record aggregate")
    require(manifest == compile_manifest(root), "manifest differs from exact batch gate")
    require(manifest.get("honesty", {}).get("all_n_proved_by_checker") == 0, "all-n honesty")


def mutation_audit(manifest: dict[str, Any], root: Path) -> int:
    bridge = load_json(root, BRIDGE_PATH)
    schema_candidate = copy.deepcopy(bridge["schema_completions"][0]["record"])
    schema_candidate["occurrence_id"] = "fake-schema-completion"
    mutations = [
        lambda item: item["declaration"].update(batch_complete=True),
        lambda item: item["declaration"].update(physical_coverage_proved=True),
        lambda item: item["declaration"].update(promotion_to_recurrent_row_allowed=True),
        lambda item: item["source_scope"].update(expected_occurrence_count=0),
        lambda item: item["source_scope"].update(occurrence_domain_ref="fake"),
        lambda item: item["records"].append(copy.deepcopy(schema_candidate)),
        lambda item: item["aggregate"].update(accepted_physical_records=1),
        lambda item: item["aggregate"].update(schema_completion_candidates_rejected=1),
        lambda item: item["scope"].update(response_family=["3012"]),
        lambda item: item["honesty"].update(recurrent_child_rows_populated=1),
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
    print(json.dumps({"checker": "exact-recurrent-first-host-physical-fibre-batch-gate", **manifest["aggregate"], "mutation_corruptions_rejected": mutation_audit(manifest, root), **manifest["honesty"]}, sort_keys=True))


if __name__ == "__main__":
    main()
