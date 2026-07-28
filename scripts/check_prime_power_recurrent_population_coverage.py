#!/usr/bin/env python3
"""Bind a declared recurrent block to selected populated operation slots.

The clause enumerator may generate several candidate operations for one parent state. This
checker composes the clause-generated slot registry, slot-covered fibre batch and common-
weight recurrent block. For every declared SCC parent it publishes the complete candidate
slot set and binds the unique supplied row to one populated selected slot.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_common_recurrent_block_weights as common
import check_prime_power_parent_rule_clause_enumerator as clauses
import check_prime_power_slot_fibre_batch_conformance as slot_batch


class RecurrentPopulationError(ValueError):
    """Raised when recurrent rows do not match the selected populated slots."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RecurrentPopulationError(message)


def exact_selection(record: dict[str, Any], path: str) -> dict[str, Any]:
    parent = record.get("parent_state_id")
    candidates = record.get("candidate_slot_ids")
    selected_slot = record.get("selected_slot_id")
    fibre_id = record.get("selected_fibre_id")
    routing_sha = record.get("routing_certificate_sha256")
    reason = record.get("selection_reason")
    require(isinstance(parent, str) and parent, f"{path}.parent_state_id: required")
    require(isinstance(candidates, list) and candidates, f"{path}.candidate_slot_ids: nonempty list required")
    require(candidates == sorted(candidates), f"{path}.candidate_slot_ids: sorted order required")
    require(len(candidates) == len(set(candidates)), f"{path}.candidate_slot_ids: duplicates")
    require(isinstance(selected_slot, str) and selected_slot in candidates, f"{path}.selected_slot_id: not a candidate")
    require(isinstance(fibre_id, str) and fibre_id, f"{path}.selected_fibre_id: required")
    require(isinstance(routing_sha, str) and len(routing_sha) == 64, f"{path}.routing_certificate_sha256: required")
    require(isinstance(reason, str) and reason, f"{path}.selection_reason: required")
    output = {
        "parent_state_id": parent,
        "candidate_slot_ids": list(candidates),
        "selected_slot_id": selected_slot,
        "selected_fibre_id": fibre_id,
        "routing_certificate_sha256": routing_sha,
        "selection_reason": reason,
    }
    output["selection_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    clause_manifest = certificate.get("clause_manifest")
    coverage = certificate.get("slot_batch_conformance_certificate")
    block = certificate.get("common_weight_certificate")
    raw_selections = certificate.get("row_selections")
    require(isinstance(clause_manifest, dict), "clause_manifest: expected object")
    require(isinstance(coverage, dict), "slot_batch_conformance_certificate: expected object")
    require(isinstance(block, dict), "common_weight_certificate: expected object")
    require(isinstance(raw_selections, list) and raw_selections, "row_selections: nonempty list required")

    clauses.validate_manifest(clause_manifest)
    slot_batch.validate_certificate(coverage)
    common.validate_certificate(block)
    clause_exact = clauses.exact_enumerator(clause_manifest)
    coverage_exact = slot_batch.exact_certificate(coverage)
    block_exact = common.exact_certificate(block)
    registry = clause_exact["expected_slot_registry"]
    require(coverage["expected_slot_registry"] == registry,
            "slot batch registry differs from clause-generated registry")

    selections = [exact_selection(record, f"row_selections[{index}]") for index, record in enumerate(raw_selections)]
    require(raw_selections == selections, "row_selections: canonical records or digests required")
    require(selections == sorted(selections, key=lambda record: record["parent_state_id"]),
            "row_selections: canonical parent order required")
    require(len({record["parent_state_id"] for record in selections}) == len(selections),
            "row_selections: duplicate parent")

    slots_by_parent: dict[str, list[str]] = {}
    slot_by_id = {record["slot_id"]: record for record in registry["slots"]}
    for slot in registry["slots"]:
        slots_by_parent.setdefault(slot["parent_state_id"], []).append(slot["slot_id"])
    for values in slots_by_parent.values():
        values.sort()
    assignment_by_slot = {record["slot_id"]: record for record in coverage_exact["slot_assignments"]}
    common_rows = {}
    routed_by_sha = {record["certificate_sha256"]: record for record in block["routed_row_certificates"]}
    for row in block_exact["row_records"]:
        require(row["routing_certificate_sha256"] in routed_by_sha, "common row routing digest missing")
        common_rows[row["parent_state_id"]] = row

    scc_states = set(block["scc_state_ids"])
    require({record["parent_state_id"] for record in selections} == scc_states,
            "row_selections: must cover every declared SCC parent exactly")
    for index, selection in enumerate(selections):
        parent = selection["parent_state_id"]
        expected_candidates = slots_by_parent.get(parent, [])
        require(selection["candidate_slot_ids"] == expected_candidates,
                f"row_selections[{index}]: candidate set differs from complete parent slot set")
        require(selection["selected_slot_id"] in assignment_by_slot,
                f"row_selections[{index}]: selected slot is not populated")
        assignment = assignment_by_slot[selection["selected_slot_id"]]
        require(assignment["fibre_id"] == selection["selected_fibre_id"],
                f"row_selections[{index}]: selected fibre differs from slot assignment")
        require(slot_by_id[selection["selected_slot_id"]]["parent_state_id"] == parent,
                f"row_selections[{index}]: slot parent mismatch")
        require(parent in common_rows, f"row_selections[{index}]: parent missing common row")
        row = common_rows[parent]
        require(row["fibre_id"] == selection["selected_fibre_id"],
                f"row_selections[{index}]: common row fibre mismatch")
        require(row["routing_certificate_sha256"] == selection["routing_certificate_sha256"],
                f"row_selections[{index}]: routing certificate mismatch")

    candidate_counts = Counter(len(record["candidate_slot_ids"]) for record in selections)
    coverage_complete = coverage_exact["claims"]["complete"]
    block_complete = block_exact["claims"]["complete_strict_scc"]
    complete = int(coverage_complete and block_complete)
    claims = {
        "parent_cases": clause_exact["claims"]["parent_cases"],
        "generated_slots": clause_exact["claims"]["generated_slots"],
        "scc_states": len(scc_states),
        "row_selections": len(selections),
        "selected_populated_slots": len(selections),
        "candidate_slots": sum(len(record["candidate_slot_ids"]) for record in selections),
        "unselected_candidate_slots": sum(len(record["candidate_slot_ids"]) - 1 for record in selections),
        "slot_batch_complete": coverage_complete,
        "common_block_complete_strict_scc": block_complete,
        "complete_strict_recurrent_population": complete,
        "candidate_count_distribution": [[key, candidate_counts[key]] for key in sorted(candidate_counts)],
        "clause_manifest_sha256": clause_manifest["manifest_sha256"],
        "slot_batch_conformance_sha256": coverage["certificate_sha256"],
        "common_weight_sha256": block["certificate_sha256"],
        "row_selections_sha256": catalogue.canonical_digest(selections),
    }
    return {"row_selections": selections, "claims": claims}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("row_selections", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload), "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {
        "states": claims["scc_states"],
        "selections": claims["row_selections"],
        "candidates": claims["candidate_slots"],
        "unselected": claims["unselected_candidate_slots"],
        "batch_complete": claims["slot_batch_complete"],
        "block_complete": claims["common_block_complete_strict_scc"],
        "complete": claims["complete_strict_recurrent_population"],
    }


def build_certificate(clause_manifest: dict[str, Any], coverage: dict[str, Any], block: dict[str, Any],
                      selections: list[dict[str, Any]]) -> dict[str, Any]:
    canonical = [exact_selection(record, "row_selection") for record in selections]
    canonical.sort(key=lambda record: record["parent_state_id"])
    certificate: dict[str, Any] = {
        "version": 1,
        "clause_manifest": clause_manifest,
        "slot_batch_conformance_certificate": coverage,
        "common_weight_certificate": block,
        "row_selections": canonical,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_recurrent_population_coverage.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
