#!/usr/bin/env python3
"""Assemble one denominator-cleared integer recurrent quotient block.

This checker composes exact candidate-operation selection, resource-overlap-derived scopes,
a common recurrent block and acyclic auxiliary elimination. When full elimination preserves
the row-selected responses, every parent row becomes one exact integer inequality

    w_parent - net_fixed_offset - sum(target_multiplicity * w_target) = margin > 0.

The resulting matrix/vector package is a finite recurrent block certificate, not the final
global CRT quotient across every block and interface.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import check_prime_power_acyclic_auxiliary_elimination as auxiliary
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_common_recurrent_block_weights as common
import check_prime_power_common_weight_candidate_policy as policy
import check_prime_power_resource_overlap_scope_partition as scopes


class IntegerQuotientError(ValueError):
    """Raised when integer block quotient components do not compose exactly."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise IntegerQuotientError(message)


def state_registry(block: dict[str, Any]) -> dict[str, dict[str, Any]]:
    states: dict[str, dict[str, Any]] = {}
    for routed in block["routed_row_certificates"]:
        source = routed["row_margin_certificate"]["linked_operation_certificate"]["linkage_certificate"]["source_manifest"]
        for raw in source["states"]:
            core = {key: raw[key] for key in ("id", "role", "stratum", "owner")}
            if core["id"] in states:
                require(states[core["id"]] == core, f"state {core['id']}: definition drift")
            else:
                states[core["id"]] = core
    return states


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    policy_certificate = certificate.get("candidate_policy_certificate")
    scope_certificate = certificate.get("resource_scope_partition_certificate")
    auxiliary_certificate = certificate.get("acyclic_auxiliary_elimination_certificate")
    require(isinstance(policy_certificate, dict), "candidate_policy_certificate: expected object")
    require(isinstance(scope_certificate, dict), "resource_scope_partition_certificate: expected object")
    require(isinstance(auxiliary_certificate, dict),
            "acyclic_auxiliary_elimination_certificate: expected object")

    policy.validate_certificate(policy_certificate)
    scopes.validate_certificate(scope_certificate)
    auxiliary.validate_certificate(auxiliary_certificate)
    policy_exact = policy.exact_certificate(policy_certificate)
    scope_exact = scopes.exact_certificate(scope_certificate)
    auxiliary_exact = auxiliary.exact_certificate(auxiliary_certificate)

    population_certificate = policy_certificate["recurrent_population_certificate"]
    block = population_certificate["common_weight_certificate"]
    require(auxiliary_certificate["common_weight_certificate"] == block,
            "auxiliary elimination common block differs from candidate policy block")
    common.validate_certificate(block)
    block_exact = common.exact_certificate(block)
    weights = {record["state_id"]: record["weight"] for record in block["state_weights"]}
    states = state_registry(block)

    simultaneous_certificate = scope_certificate["simultaneous_credit_certificate"]
    simultaneous_rows = simultaneous_certificate["selected_rows"]
    scope_route_shas = sorted(row["routing_certificate_sha256"] for row in simultaneous_rows)
    block_route_shas = sorted(route["certificate_sha256"] for route in block["routed_row_certificates"])
    require(scope_route_shas == block_route_shas,
            "derived scope partition does not cover exactly the common-block rows")

    policy_by_parent = {record["parent_state_id"]: record
                        for record in policy_exact["parent_policy_records"]}
    eliminated_by_parent = {record["parent_state_id"]: record
                            for record in auxiliary_exact["eliminated_row_records"]}
    block_row_by_parent = {record["parent_state_id"]: record
                           for record in block_exact["row_records"]}
    selected_response_by_parent = {}
    for routed in block["routed_row_certificates"]:
        row_certificate = routed["row_margin_certificate"]
        parent = row_certificate["linked_operation_certificate"]["linkage_certificate"]["source_manifest"]["parent"]
        selected_response_by_parent[parent] = row_certificate["claims"]["selected_response"]
    require(set(policy_by_parent) == set(eliminated_by_parent) == set(block_row_by_parent),
            "parent sets differ across policy, block and elimination certificates")

    columns = sorted(state_id for state_id, state in states.items()
                     if state["role"] != "auxiliary")
    row_records = []
    matrix = []
    fixed_offsets = []
    parent_weights = []
    margins = []
    selection_preserved = 1
    for parent in sorted(policy_by_parent):
        policy_record = policy_by_parent[parent]
        eliminated = eliminated_by_parent[parent]
        original = block_row_by_parent[parent]
        require(policy_record["selected_fibre_id"] == eliminated["fibre_id"] == original["fibre_id"],
                f"parent {parent}: selected fibre mismatch")
        original_selected_response = selected_response_by_parent[parent]
        if eliminated["selected_response"] != original_selected_response:
            selection_preserved = 0
        require(eliminated["selected_response"] == original_selected_response,
                f"parent {parent}: auxiliary elimination changes selected response; reroute required")

        target_map = {state_id: multiplicity
                      for state_id, multiplicity in eliminated["selected_child_vector"]}
        require(set(target_map) <= set(columns),
                f"parent {parent}: eliminated vector contains auxiliary or unknown target")
        vector = [target_map.get(state_id, 0) for state_id in columns]
        require(all(type(value) is int and value >= 0 for value in vector),
                f"parent {parent}: target vector must be nonnegative integer")
        target_weight = sum(value * weights[state_id] for state_id, value in zip(columns, vector))
        fixed = eliminated["selected_net_fixed_offset"]
        row_load = fixed + target_weight
        parent_weight = weights[parent]
        margin = parent_weight - row_load
        require(row_load == eliminated["selected_row_load"],
                f"parent {parent}: quotient row load mismatch")
        require(margin == eliminated["selected_margin"],
                f"parent {parent}: quotient margin mismatch")
        require(margin > 0, f"parent {parent}: integer quotient row is not strict")
        record = {
            "parent_state_id": parent,
            "selected_slot_id": policy_record["selected_slot_id"],
            "selected_fibre_id": policy_record["selected_fibre_id"],
            "selected_response": eliminated["selected_response"],
            "parent_weight": parent_weight,
            "net_fixed_offset": fixed,
            "target_vector": vector,
            "target_weighted_load": target_weight,
            "row_load": row_load,
            "margin": margin,
        }
        record["quotient_row_sha256"] = catalogue.canonical_digest(record)
        row_records.append(record)
        matrix.append(vector)
        fixed_offsets.append(fixed)
        parent_weights.append(parent_weight)
        margins.append(margin)

    require([record["parent_state_id"] for record in row_records] == sorted(block["scc_state_ids"]),
            "quotient rows do not cover exact SCC parent order")
    matrix_record = {
        "row_state_ids": [record["parent_state_id"] for record in row_records],
        "column_state_ids": columns,
        "target_matrix": matrix,
        "fixed_offset_vector": fixed_offsets,
        "parent_weight_vector": parent_weights,
        "margin_vector": margins,
    }
    matrix_record["integer_block_sha256"] = catalogue.canonical_digest(matrix_record)

    complete = int(
        policy_exact["claims"]["common_weight_policy_exact"]
        and scope_exact["claims"]["scope_partition_exact"]
        and block_exact["claims"]["complete_strict_scc"]
        and auxiliary_exact["claims"]["strict_scc_preserved_after_elimination"]
        and selection_preserved
        and all(margin > 0 for margin in margins)
    )
    claims = {
        "states": len(states),
        "rows": len(row_records),
        "columns": len(columns),
        "nonzero_matrix_entries": sum(value > 0 for row in matrix for value in row),
        "signed_fixed_offsets": sum(value < 0 for value in fixed_offsets),
        "minimum_margin": min(margins),
        "total_margin": sum(margins),
        "maximum_parent_weight": max(parent_weights),
        "selected_response_preserved": selection_preserved,
        "candidate_policy_exact": policy_exact["claims"]["common_weight_policy_exact"],
        "resource_scope_partition_exact": scope_exact["claims"]["scope_partition_exact"],
        "source_complete_strict_scc": block_exact["claims"]["complete_strict_scc"],
        "auxiliary_strictness_preserved": auxiliary_exact["claims"]["strict_scc_preserved_after_elimination"],
        "complete_integer_recurrent_block": complete,
        "candidate_policy_sha256": policy_certificate["certificate_sha256"],
        "resource_scope_sha256": scope_certificate["certificate_sha256"],
        "auxiliary_elimination_sha256": auxiliary_certificate["certificate_sha256"],
        "common_weight_sha256": block["certificate_sha256"],
        "quotient_rows_sha256": catalogue.canonical_digest(row_records),
        "integer_block_sha256": matrix_record["integer_block_sha256"],
    }
    return {
        "quotient_row_records": row_records,
        "integer_block": matrix_record,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("quotient_row_records", "integer_block", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {
        "rows": claims["rows"],
        "columns": claims["columns"],
        "nonzero": claims["nonzero_matrix_entries"],
        "minimum_margin": claims["minimum_margin"],
        "complete": claims["complete_integer_recurrent_block"],
    }


def build_certificate(policy_certificate: dict[str, Any], scope_certificate: dict[str, Any],
                      auxiliary_certificate: dict[str, Any]) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "candidate_policy_certificate": policy_certificate,
        "resource_scope_partition_certificate": scope_certificate,
        "acyclic_auxiliary_elimination_certificate": auxiliary_certificate,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_integer_recurrent_quotient_block.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
