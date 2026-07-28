#!/usr/bin/env python3
"""Certify common-weight operation selection across every populated candidate slot.

For each recurrent parent, the recurrent-population certificate publishes the complete
clause-generated candidate slot set. This checker requires one witness-bound row
certificate for every candidate slot, binds it to the populated fibre assignment, checks
that all rows use the same global state weights, and selects the least exact minimum row
load with slot ID as deterministic tie-break.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_common_recurrent_block_weights as common
import check_prime_power_recurrent_population_coverage as population
import check_prime_power_witness_bound_destroyed_credit_routing as routing


class CandidatePolicyError(ValueError):
    """Raised when common-weight candidate-operation selection is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CandidatePolicyError(message)


def exact_candidate(record: dict[str, Any], path: str, weights: dict[str, int]) -> dict[str, Any]:
    parent = record.get("parent_state_id")
    slot_id = record.get("slot_id")
    route_certificate = record.get("routing_certificate")
    require(isinstance(parent, str) and parent, f"{path}.parent_state_id: required")
    require(isinstance(slot_id, str) and slot_id, f"{path}.slot_id: required")
    require(isinstance(route_certificate, dict), f"{path}.routing_certificate: expected object")
    routing.validate_certificate(route_certificate)
    row_certificate = route_certificate["row_margin_certificate"]
    source = row_certificate["linked_operation_certificate"]["linkage_certificate"]["source_manifest"]
    require(source["parent"] == parent, f"{path}: route parent mismatch")
    require(parent in weights, f"{path}: parent missing common weight")
    require(row_certificate["parent_budget"] == weights[parent],
            f"{path}: parent budget differs from common weight")
    children = row_certificate["weight_exposure_certificate"]["children"]
    require(set(children) <= set(weights), f"{path}: child missing common weight")
    require(row_certificate["child_weights"] == {child: weights[child] for child in children},
            f"{path}: child weights differ from common restriction")
    claims = row_certificate["claims"]
    output = {
        "parent_state_id": parent,
        "slot_id": slot_id,
        "fibre_id": claims["fibre_id"],
        "host_id": claims["host_id"],
        "minimum_row_load": claims["minimum_row_load"],
        "maximum_margin": claims["maximum_margin"],
        "selected_response": claims["selected_response"],
        "minimizer_count": claims["minimizer_count"],
        "strict_row": claims["strict_row"],
        "routing_certificate": route_certificate,
        "routing_certificate_sha256": route_certificate["certificate_sha256"],
    }
    output["candidate_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    population_certificate = certificate.get("recurrent_population_certificate")
    raw_candidates = certificate.get("candidate_row_certificates")
    require(isinstance(population_certificate, dict),
            "recurrent_population_certificate: expected object")
    require(isinstance(raw_candidates, list) and raw_candidates,
            "candidate_row_certificates: nonempty list required")
    population.validate_certificate(population_certificate)
    population_exact = population.exact_certificate(population_certificate)
    block = population_certificate["common_weight_certificate"]
    common.validate_certificate(block)
    weights = {record["state_id"]: record["weight"] for record in block["state_weights"]}

    candidates = [
        exact_candidate(record, f"candidate_row_certificates[{index}]", weights)
        for index, record in enumerate(raw_candidates)
    ]
    require(raw_candidates == candidates,
            "candidate_row_certificates: canonical records or digests required")
    require(candidates == sorted(candidates, key=lambda record: (record["parent_state_id"], record["slot_id"])),
            "candidate_row_certificates: canonical parent/slot order required")
    candidate_keys = [(record["parent_state_id"], record["slot_id"]) for record in candidates]
    require(len(candidate_keys) == len(set(candidate_keys)),
            "candidate_row_certificates: duplicate parent/slot")

    coverage = population_certificate["slot_batch_conformance_certificate"]
    coverage_exact = __import__("check_prime_power_slot_fibre_batch_conformance").exact_certificate(coverage)
    assignment_by_slot = {record["slot_id"]: record for record in coverage_exact["slot_assignments"]}
    slot_by_id = {
        record["slot_id"]: record
        for record in population_certificate["clause_manifest"]["expected_slot_registry"]["slots"]
    }
    selection_by_parent = {
        record["parent_state_id"]: record for record in population_exact["row_selections"]
    }

    by_parent: dict[str, list[dict[str, Any]]] = {}
    for record in candidates:
        parent = record["parent_state_id"]
        slot_id = record["slot_id"]
        require(slot_id in slot_by_id, f"candidate {slot_id}: unknown slot")
        require(slot_by_id[slot_id]["parent_state_id"] == parent,
                f"candidate {slot_id}: slot parent mismatch")
        require(slot_id in assignment_by_slot, f"candidate {slot_id}: slot not populated")
        require(assignment_by_slot[slot_id]["fibre_id"] == record["fibre_id"],
                f"candidate {slot_id}: fibre differs from population assignment")
        by_parent.setdefault(parent, []).append(record)

    policy_records = []
    load_gap_distribution: Counter[int] = Counter()
    tied_parents = 0
    for parent, selection in sorted(selection_by_parent.items()):
        records = by_parent.get(parent, [])
        expected_slots = selection["candidate_slot_ids"]
        require([record["slot_id"] for record in records] == expected_slots,
                f"parent {parent}: candidate rows do not cover complete slot set")
        winner = min(records, key=lambda record: (record["minimum_row_load"], record["slot_id"]))
        require(winner["slot_id"] == selection["selected_slot_id"],
                f"parent {parent}: supplied selected slot is not the common-weight policy winner")
        minimum_load = winner["minimum_row_load"]
        minimizers = [record for record in records if record["minimum_row_load"] == minimum_load]
        tied_parents += int(len(minimizers) > 1)
        entries = []
        for record in records:
            gap = record["minimum_row_load"] - minimum_load
            require(gap >= 0, f"parent {parent}: negative candidate gap")
            load_gap_distribution[gap] += 1
            entries.append({
                "slot_id": record["slot_id"],
                "fibre_id": record["fibre_id"],
                "minimum_row_load": record["minimum_row_load"],
                "maximum_margin": record["maximum_margin"],
                "load_gap": gap,
                "is_minimizer": int(gap == 0),
                "is_selected": int(record["slot_id"] == winner["slot_id"]),
                "routing_certificate_sha256": record["routing_certificate_sha256"],
            })
        policy = {
            "parent_state_id": parent,
            "candidate_slots": len(records),
            "minimum_candidate_load": minimum_load,
            "maximum_selected_margin": winner["maximum_margin"],
            "minimizer_count": len(minimizers),
            "selected_slot_id": winner["slot_id"],
            "selected_fibre_id": winner["fibre_id"],
            "candidate_entries": entries,
        }
        policy["policy_record_sha256"] = catalogue.canonical_digest(policy)
        policy_records.append(policy)

    require(set(by_parent) == set(selection_by_parent),
            "candidate rows contain parent outside recurrent population")
    claims = {
        "parents": len(policy_records),
        "candidate_rows": len(candidates),
        "selected_rows": len(policy_records),
        "unselected_rows": len(candidates) - len(policy_records),
        "tied_parents": tied_parents,
        "strict_selected_rows": sum(record["maximum_selected_margin"] > 0 for record in policy_records),
        "total_candidate_load_gap": sum(gap * count for gap, count in load_gap_distribution.items()),
        "maximum_candidate_load_gap": max(load_gap_distribution),
        "load_gap_distribution": [[gap, load_gap_distribution[gap]] for gap in sorted(load_gap_distribution)],
        "common_weight_sha256": block["certificate_sha256"],
        "recurrent_population_sha256": population_certificate["certificate_sha256"],
        "candidate_rows_sha256": catalogue.canonical_digest(candidates),
        "policy_records_sha256": catalogue.canonical_digest(policy_records),
        "common_weight_policy_exact": 1,
    }
    return {
        "candidate_row_certificates": candidates,
        "parent_policy_records": policy_records,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("candidate_row_certificates", "parent_policy_records", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {
        "parents": claims["parents"],
        "candidates": claims["candidate_rows"],
        "tied": claims["tied_parents"],
        "strict": claims["strict_selected_rows"],
        "exact": claims["common_weight_policy_exact"],
    }


def build_certificate(population_certificate: dict[str, Any],
                      candidate_rows: list[dict[str, Any]]) -> dict[str, Any]:
    block = population_certificate["common_weight_certificate"]
    weights = {record["state_id"]: record["weight"] for record in block["state_weights"]}
    canonical = [exact_candidate(record, "candidate_row", weights) for record in candidate_rows]
    canonical.sort(key=lambda record: (record["parent_state_id"], record["slot_id"]))
    certificate: dict[str, Any] = {
        "version": 1,
        "recurrent_population_certificate": population_certificate,
        "candidate_row_certificates": canonical,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_common_weight_candidate_policy.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
