#!/usr/bin/env python3
"""Bind every final quotient state and row to explicit mathematical semantics.

The global quotient currently carries finite state IDs and row arithmetic. This checker
requires one predicate record for every global state and one theorem record for every final
row, binds shared-state equivalence evidence into the predicate records, and reconstructs each
row's target predicate multiset exactly.

Passing proves complete semantic documentation relative to supplied statements. It does not
verify those statements mathematically.
"""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_global_family_skeleton as skeleton
import check_prime_power_state_equivalence_spanning_evidence as equivalence


class QuotientSemanticRefinementError(ValueError):
    """Raised when quotient state/row semantics are incomplete or inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise QuotientSemanticRefinementError(message)


def exact_state_core(record: dict[str, Any], path: str) -> dict[str, Any]:
    state_id = record.get("global_state_id")
    predicate_id = record.get("predicate_id")
    locator = record.get("predicate_locator")
    digest = record.get("predicate_digest")
    statement = record.get("predicate_statement")
    evidence = record.get("evidence")
    for name, value in (("global_state_id", state_id), ("predicate_id", predicate_id),
                        ("predicate_locator", locator), ("predicate_digest", digest),
                        ("predicate_statement", statement), ("evidence", evidence)):
        require(isinstance(value, str) and value, f"{path}.{name}: required")
    return {
        "global_state_id": state_id,
        "predicate_id": predicate_id,
        "predicate_locator": locator,
        "predicate_digest": digest,
        "predicate_statement": statement,
        "evidence": evidence,
    }


def exact_row_core(record: dict[str, Any], path: str) -> dict[str, Any]:
    row_id = record.get("row_id")
    theorem_id = record.get("theorem_id")
    locator = record.get("theorem_locator")
    digest = record.get("theorem_digest")
    statement = record.get("theorem_statement")
    fixed_meaning = record.get("fixed_offset_interpretation")
    evidence = record.get("evidence")
    for name, value in (("row_id", row_id), ("theorem_id", theorem_id),
                        ("theorem_locator", locator), ("theorem_digest", digest),
                        ("theorem_statement", statement),
                        ("fixed_offset_interpretation", fixed_meaning), ("evidence", evidence)):
        require(isinstance(value, str) and value, f"{path}.{name}: required")
    return {
        "row_id": row_id,
        "theorem_id": theorem_id,
        "theorem_locator": locator,
        "theorem_digest": digest,
        "theorem_statement": statement,
        "fixed_offset_interpretation": fixed_meaning,
        "evidence": evidence,
    }


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    skeleton_certificate = certificate.get("global_family_skeleton_certificate")
    equivalence_certificate = certificate.get("state_equivalence_evidence_certificate")
    raw_states = certificate.get("state_semantic_records")
    raw_rows = certificate.get("row_semantic_records")
    require(isinstance(skeleton_certificate, dict), "global_family_skeleton_certificate: expected object")
    require(isinstance(equivalence_certificate, dict), "state_equivalence_evidence_certificate: expected object")
    require(isinstance(raw_states, list) and raw_states, "state_semantic_records: nonempty list required")
    require(isinstance(raw_rows, list) and raw_rows, "row_semantic_records: nonempty list required")
    skeleton.validate_certificate(skeleton_certificate)
    equivalence.validate_certificate(equivalence_certificate)
    skeleton_exact = skeleton.exact_certificate(skeleton_certificate)
    equivalence_exact = equivalence.exact_certificate(equivalence_certificate)

    global_certificate = skeleton_certificate["global_integer_family_certificate"]
    global_exact = __import__("check_prime_power_global_integer_quotient_family").exact_certificate(global_certificate)
    identification = global_certificate["interface_row_certificate"]["weight_synchronization_certificate"][
        "state_identification_certificate"
    ]
    require(equivalence_certificate["state_identification_certificate"]["certificate_sha256"]
            == identification["certificate_sha256"],
            "state equivalence and global family use different identification certificates")
    identification_exact = __import__("check_prime_power_cross_block_state_identification").exact_certificate(
        identification
    )

    state_core_records = [exact_state_core(record, f"state_semantic_records[{index}]")
                          for index, record in enumerate(raw_states)]
    require(state_core_records == sorted(state_core_records, key=lambda item: item["global_state_id"]),
            "state_semantic_records: canonical state order required")
    state_ids = [record["global_state_id"] for record in state_core_records]
    require(len(state_ids) == len(set(state_ids)), "state_semantic_records: duplicate global state")
    expected_state_ids = [record["global_state_id"] for record in identification_exact["global_state_records"]]
    require(state_ids == expected_state_ids, "state_semantic_records: must cover every global state exactly")
    predicate_ids = [record["predicate_id"] for record in state_core_records]
    require(len(predicate_ids) == len(set(predicate_ids)), "state_semantic_records: duplicate predicate_id")

    global_state_by_id = {record["global_state_id"]: record
                          for record in identification_exact["global_state_records"]}
    class_evidence_by_id = {record["global_state_id"]: record
                            for record in equivalence_exact["class_equivalence_records"]}
    state_records = []
    predicate_by_state = {}
    for core in state_core_records:
        state_id = core["global_state_id"]
        global_state = global_state_by_id[state_id]
        class_evidence = class_evidence_by_id[state_id]
        record = dict(core)
        record.update({
            "role": global_state["role"],
            "stratum": global_state["stratum"],
            "owner": copy.deepcopy(global_state["owner"]),
            "member_refs": list(class_evidence["member_refs"]),
            "equivalence_tree_edge_sha256s": list(class_evidence["tree_edge_sha256s"]),
            "class_equivalence_sha256": class_evidence["class_equivalence_sha256"],
        })
        record["state_semantic_record_sha256"] = catalogue.canonical_digest(record)
        state_records.append(record)
        predicate_by_state[state_id] = core["predicate_id"]
    require(raw_states == state_core_records or raw_states == state_records,
            "state_semantic_records: canonical core or enriched records required")

    row_core_records = [exact_row_core(record, f"row_semantic_records[{index}]")
                        for index, record in enumerate(raw_rows)]
    require(row_core_records == sorted(row_core_records, key=lambda item: item["row_id"]),
            "row_semantic_records: canonical row order required")
    row_ids = [record["row_id"] for record in row_core_records]
    require(len(row_ids) == len(set(row_ids)), "row_semantic_records: duplicate row_id")
    global_rows = {record["row_id"]: record for record in global_exact["global_row_records"]}
    require(row_ids == sorted(global_rows), "row_semantic_records: must cover every final global row exactly")

    row_records = []
    theorem_ids = []
    for core in row_core_records:
        row = global_rows[core["row_id"]]
        theorem_ids.append(core["theorem_id"])
        targets = [
            {
                "global_state_id": state_id,
                "predicate_id": predicate_by_state[state_id],
                "multiplicity": multiplicity,
            }
            for state_id, multiplicity in row["target_multiplicities"]
        ]
        record = dict(core)
        record.update({
            "row_kind": row["row_kind"],
            "row_classification": row["classification"],
            "parent_global_state_id": row["parent_global_state_id"],
            "parent_predicate_id": predicate_by_state[row["parent_global_state_id"]],
            "fixed_offset": row["fixed_offset"],
            "target_predicate_multiplicities": targets,
            "margin": row["margin"],
            "global_row_sha256": row["global_row_sha256"],
        })
        record["row_semantic_record_sha256"] = catalogue.canonical_digest(record)
        row_records.append(record)
    require(len(theorem_ids) == len(set(theorem_ids)), "row_semantic_records: duplicate theorem_id")
    require(raw_rows == row_core_records or raw_rows == row_records,
            "row_semantic_records: canonical core or enriched records required")

    claims = {
        "global_states": len(state_records),
        "global_rows": len(row_records),
        "shared_state_classes": sum(len(record["member_refs"]) > 1 for record in state_records),
        "strict_rows": sum(record["row_classification"] == "strict" for record in row_records),
        "critical_descending_rows": sum(record["row_classification"] == "critical-descending" for record in row_records),
        "complete_state_semantic_coverage": 1,
        "complete_row_semantic_coverage": 1,
        "global_family_skeleton_sha256": skeleton_certificate["certificate_sha256"],
        "state_equivalence_evidence_sha256": equivalence_certificate["certificate_sha256"],
        "state_semantic_records_sha256": catalogue.canonical_digest(state_records),
        "row_semantic_records_sha256": catalogue.canonical_digest(row_records),
    }
    return {"state_semantic_records": state_records, "row_semantic_records": row_records, "claims": claims}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("state_semantic_records", "row_semantic_records", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {"states": claims["global_states"], "rows": claims["global_rows"],
            "state_complete": claims["complete_state_semantic_coverage"],
            "row_complete": claims["complete_row_semantic_coverage"]}


def build_certificate(skeleton_certificate: dict[str, Any], equivalence_certificate: dict[str, Any],
                      state_semantics: list[dict[str, Any]], row_semantics: list[dict[str, Any]]) -> dict[str, Any]:
    state_cores = [exact_state_core(record, "state_semantic") for record in state_semantics]
    state_cores.sort(key=lambda item: item["global_state_id"])
    row_cores = [exact_row_core(record, "row_semantic") for record in row_semantics]
    row_cores.sort(key=lambda item: item["row_id"])
    certificate: dict[str, Any] = {
        "version": 1,
        "global_family_skeleton_certificate": skeleton_certificate,
        "state_equivalence_evidence_certificate": equivalence_certificate,
        "state_semantic_records": state_cores,
        "row_semantic_records": row_cores,
    }
    exact = exact_certificate(certificate)
    certificate.update(exact)
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_global_quotient_semantic_refinement.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
