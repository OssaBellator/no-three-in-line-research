#!/usr/bin/env python3
"""Assemble a global denominator-cleared integer quotient family.

The certificate composes cross-block state identification, synchronized block weights,
globally scaled interface/return rows and an explicit expected family manifest. Recurrent
block rows are lifted into the final global weight scale, interface rows are appended, and
the checker publishes one canonical integer matrix/vector/rank package.

Completeness is relative to the supplied expected block, interface-row and parent-state
registries. It does not prove that those registries are the genuine exhaustive recurrence.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_interface_return_rows as interface_rows


class GlobalQuotientError(ValueError):
    """Raised when the global integer quotient family is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GlobalQuotientError(message)


def exact_manifest(manifest: dict[str, Any]) -> dict[str, Any]:
    family_id = manifest.get("family_id")
    expected_blocks = manifest.get("expected_block_ids")
    expected_interfaces = manifest.get("expected_interface_row_ids")
    expected_parents = manifest.get("expected_parent_global_state_ids")
    evidence = manifest.get("evidence")
    require(isinstance(family_id, str) and family_id, "family_manifest.family_id: required")
    require(isinstance(expected_blocks, list) and expected_blocks,
            "family_manifest.expected_block_ids: nonempty list required")
    require(isinstance(expected_interfaces, list),
            "family_manifest.expected_interface_row_ids: expected list")
    require(isinstance(expected_parents, list) and expected_parents,
            "family_manifest.expected_parent_global_state_ids: nonempty list required")
    require(isinstance(evidence, str) and evidence, "family_manifest.evidence: required")
    for name, values in (
        ("expected_block_ids", expected_blocks),
        ("expected_interface_row_ids", expected_interfaces),
        ("expected_parent_global_state_ids", expected_parents),
    ):
        require(all(isinstance(value, str) and value for value in values), f"family_manifest.{name}: bad value")
        require(values == sorted(values), f"family_manifest.{name}: sorted order required")
        require(len(values) == len(set(values)), f"family_manifest.{name}: duplicates")
    output = {
        "family_id": family_id,
        "expected_block_ids": list(expected_blocks),
        "expected_interface_row_ids": list(expected_interfaces),
        "expected_parent_global_state_ids": list(expected_parents),
        "evidence": evidence,
    }
    output["family_manifest_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    interface_certificate = certificate.get("interface_row_certificate")
    raw_manifest = certificate.get("family_manifest")
    require(isinstance(interface_certificate, dict), "interface_row_certificate: expected object")
    require(isinstance(raw_manifest, dict), "family_manifest: expected object")
    interface_rows.validate_certificate(interface_certificate)
    interface_exact = interface_rows.exact_certificate(interface_certificate)
    manifest = exact_manifest(raw_manifest)
    require(raw_manifest == manifest, "family_manifest: canonical record or digest required")

    synchronization_certificate = interface_certificate["weight_synchronization_certificate"]
    sync_exact = __import__("check_prime_power_cross_block_weight_synchronization").exact_certificate(
        synchronization_certificate
    )
    identification = synchronization_certificate["state_identification_certificate"]
    identification_exact = __import__("check_prime_power_cross_block_state_identification").exact_certificate(
        identification
    )

    actual_block_ids = sorted(record["block_id"] for record in identification_exact["integer_blocks"])
    actual_interface_ids = sorted(record["row_id"] for record in interface_exact["interface_rows"])
    require(actual_block_ids == manifest["expected_block_ids"],
            "family_manifest: expected block coverage mismatch")
    require(actual_interface_ids == manifest["expected_interface_row_ids"],
            "family_manifest: expected interface-row coverage mismatch")

    final_weight_by_state = {
        record["global_state_id"]: record["global_weight"]
        for record in interface_exact["final_global_weight_records"]
    }
    rank_by_state = {record["global_state_id"]: record["rank"] for record in interface_exact["state_ranks"]}
    role_by_state = {
        record["global_state_id"]: record["role"]
        for record in identification_exact["global_state_records"]
    }
    component_multiplier = {
        record["component_id"]: record["multiplier"]
        for record in interface_exact["component_multipliers"]
    }

    block_complete = {
        record["block_id"]: record["certificate"]["claims"]["complete_integer_recurrent_block"]
        for record in identification_exact["integer_blocks"]
    }
    row_records = []
    for row in sync_exact["scaled_block_rows"]:
        factor = component_multiplier[row["component_id"]]
        targets = [[state_id, multiplicity] for state_id, multiplicity in row["global_target_multiplicities"]]
        parent = row["global_parent_state_id"]
        parent_weight = factor * row["scaled_parent_weight"]
        fixed_offset = factor * row["scaled_fixed_offset"]
        target_weight = sum(multiplicity * final_weight_by_state[state_id] for state_id, multiplicity in targets)
        margin = factor * row["scaled_margin"]
        require(parent_weight == final_weight_by_state[parent],
                f"recurrent row {row['block_id']}:{parent}: final parent weight mismatch")
        require(parent_weight - fixed_offset - target_weight == margin,
                f"recurrent row {row['block_id']}:{parent}: final row identity failed")
        require(margin > 0, f"recurrent row {row['block_id']}:{parent}: nonpositive margin")
        output = {
            "row_id": f"recurrent::{row['block_id']}::{parent}",
            "row_kind": "recurrent",
            "block_id": row["block_id"],
            "parent_global_state_id": parent,
            "parent_weight": parent_weight,
            "parent_rank": rank_by_state[parent],
            "fixed_offset": fixed_offset,
            "target_multiplicities": targets,
            "target_weight": target_weight,
            "margin": margin,
            "classification": "strict",
            "selected_slot_id": row["selected_slot_id"],
            "selected_fibre_id": row["selected_fibre_id"],
            "selected_response": row["selected_response"],
        }
        output["global_row_sha256"] = catalogue.canonical_digest(output)
        row_records.append(output)

    for row in interface_exact["interface_rows"]:
        output = {
            "row_id": row["row_id"],
            "row_kind": row["kind"],
            "block_id": None,
            "parent_global_state_id": row["parent_global_state_id"],
            "parent_weight": row["parent_weight"],
            "parent_rank": row["parent_rank"],
            "fixed_offset": row["fixed_offset"],
            "target_multiplicities": [
                [target["global_state_id"], target["multiplicity"]]
                for target in row["target_multiplicities"]
            ],
            "target_weight": row["target_weight"],
            "margin": row["margin"],
            "classification": row["classification"],
            "selected_slot_id": None,
            "selected_fibre_id": None,
            "selected_response": None,
        }
        output["global_row_sha256"] = catalogue.canonical_digest(output)
        row_records.append(output)

    row_records.sort(key=lambda item: (item["parent_global_state_id"], item["row_kind"], item["row_id"]))
    row_ids = [record["row_id"] for record in row_records]
    require(len(row_ids) == len(set(row_ids)), "global rows: duplicate row_id")
    parents = [record["parent_global_state_id"] for record in row_records]
    require(len(parents) == len(set(parents)), "global rows: duplicate parent state")
    require(sorted(parents) == manifest["expected_parent_global_state_ids"],
            "family_manifest: expected parent-state coverage mismatch")
    require(all(role_by_state[parent] not in {"auxiliary", "sink"} for parent in parents),
            "global rows: invalid parent role")
    require(all(role_by_state[state_id] != "auxiliary"
                for row in row_records for state_id, _ in row["target_multiplicities"]),
            "global rows: auxiliary target survives final assembly")

    columns = sorted(state_id for state_id, role in role_by_state.items() if role != "auxiliary")
    matrix = []
    fixed_offsets = []
    parent_weights = []
    margins = []
    ranks = []
    for row in row_records:
        target_map = {state_id: multiplicity for state_id, multiplicity in row["target_multiplicities"]}
        matrix.append([target_map.get(state_id, 0) for state_id in columns])
        fixed_offsets.append(row["fixed_offset"])
        parent_weights.append(row["parent_weight"])
        margins.append(row["margin"])
        ranks.append(row["parent_rank"])

    global_package = {
        "row_ids": [record["row_id"] for record in row_records],
        "row_parent_global_state_ids": parents,
        "column_global_state_ids": columns,
        "target_matrix": matrix,
        "fixed_offset_vector": fixed_offsets,
        "parent_weight_vector": parent_weights,
        "margin_vector": margins,
        "parent_rank_vector": ranks,
        "global_weight_vector": [final_weight_by_state[state_id] for state_id in columns],
    }
    global_package["global_integer_quotient_sha256"] = catalogue.canonical_digest(global_package)

    all_blocks_complete = int(all(block_complete.values()))
    complete = int(
        identification_exact["claims"]["complete_local_state_coverage"]
        and sync_exact["claims"]["exact_ratio_consistency"]
        and interface_exact["claims"]["all_interface_rows_accepted"]
        and all_blocks_complete
        and actual_block_ids == manifest["expected_block_ids"]
        and actual_interface_ids == manifest["expected_interface_row_ids"]
        and sorted(parents) == manifest["expected_parent_global_state_ids"]
        and all(record["classification"] in {"strict", "critical-descending"} for record in row_records)
    )
    claims = {
        "blocks": len(actual_block_ids),
        "interface_rows": len(actual_interface_ids),
        "global_states": len(final_weight_by_state),
        "global_rows": len(row_records),
        "global_columns": len(columns),
        "recurrent_rows": sum(record["row_kind"] == "recurrent" for record in row_records),
        "strict_rows": sum(record["classification"] == "strict" for record in row_records),
        "critical_descending_rows": sum(record["classification"] == "critical-descending" for record in row_records),
        "nonzero_matrix_entries": sum(value > 0 for row in matrix for value in row),
        "minimum_margin": min(margins),
        "all_blocks_complete": all_blocks_complete,
        "exact_block_coverage": 1,
        "exact_interface_coverage": 1,
        "exact_parent_coverage": 1,
        "complete_global_integer_family": complete,
        "interface_row_sha256": interface_certificate["certificate_sha256"],
        "family_manifest_sha256": manifest["family_manifest_sha256"],
        "global_rows_sha256": catalogue.canonical_digest(row_records),
        "global_integer_quotient_sha256": global_package["global_integer_quotient_sha256"],
    }
    return {
        "family_manifest": manifest,
        "global_row_records": row_records,
        "global_integer_quotient": global_package,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("family_manifest", "global_row_records", "global_integer_quotient", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload), "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {
        "blocks": claims["blocks"],
        "rows": claims["global_rows"],
        "columns": claims["global_columns"],
        "critical": claims["critical_descending_rows"],
        "complete": claims["complete_global_integer_family"],
    }


def build_certificate(interface_row_certificate: dict[str, Any], family_manifest: dict[str, Any]) -> dict[str, Any]:
    manifest = exact_manifest(family_manifest)
    certificate: dict[str, Any] = {
        "version": 1,
        "interface_row_certificate": interface_row_certificate,
        "family_manifest": manifest,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_global_integer_quotient_family.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
