#!/usr/bin/env python3
"""Derive the expected global quotient family from a source-independent recurrence skeleton.

The skeleton contains one canonical parent clause for every expected global parent. Recurrent
clauses name an expected integer block; return/interface/off-diagonal clauses name an expected
interface row. The expected family manifest is reconstructed from those clauses and must match
the manifest consumed by the global integer quotient certificate exactly.

Passing this checker proves noncircular family derivation relative to the supplied skeleton.
It does not prove that the skeleton is the genuine exhaustive recurrence.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_global_integer_quotient_family as global_family


class GlobalFamilySkeletonError(ValueError):
    """Raised when the expected-family skeleton is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GlobalFamilySkeletonError(message)


def exact_clause(record: dict[str, Any], path: str) -> dict[str, Any]:
    parent = record.get("parent_global_state_id")
    kind = record.get("row_kind")
    rule_id = record.get("source_rule_id")
    case_id = record.get("source_case_id")
    block_id = record.get("expected_block_id")
    interface_id = record.get("expected_interface_row_id")
    evidence = record.get("evidence")
    require(isinstance(parent, str) and parent, f"{path}.parent_global_state_id: required")
    require(kind in {"recurrent", "return", "interface", "offdiagonal"}, f"{path}.row_kind: bad value")
    require(isinstance(rule_id, str) and rule_id, f"{path}.source_rule_id: required")
    require(isinstance(case_id, str) and case_id, f"{path}.source_case_id: required")
    require(isinstance(evidence, str) and evidence, f"{path}.evidence: required")
    if kind == "recurrent":
        require(isinstance(block_id, str) and block_id, f"{path}.expected_block_id: required")
        require(interface_id is None, f"{path}.expected_interface_row_id: must be null for recurrent row")
    else:
        require(block_id is None, f"{path}.expected_block_id: must be null for interface row")
        require(isinstance(interface_id, str) and interface_id, f"{path}.expected_interface_row_id: required")
    output = {
        "parent_global_state_id": parent,
        "row_kind": kind,
        "source_rule_id": rule_id,
        "source_case_id": case_id,
        "expected_block_id": block_id,
        "expected_interface_row_id": interface_id,
        "evidence": evidence,
    }
    output["skeleton_clause_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_skeleton(skeleton: dict[str, Any]) -> dict[str, Any]:
    family_id = skeleton.get("family_id")
    skeleton_id = skeleton.get("skeleton_id")
    evidence = skeleton.get("evidence")
    raw_clauses = skeleton.get("parent_clauses")
    require(isinstance(family_id, str) and family_id, "recurrence_skeleton.family_id: required")
    require(isinstance(skeleton_id, str) and skeleton_id, "recurrence_skeleton.skeleton_id: required")
    require(isinstance(evidence, str) and evidence, "recurrence_skeleton.evidence: required")
    require(isinstance(raw_clauses, list) and raw_clauses, "recurrence_skeleton.parent_clauses: nonempty list required")
    clauses = [exact_clause(record, f"parent_clauses[{index}]") for index, record in enumerate(raw_clauses)]
    require(raw_clauses == clauses, "recurrence_skeleton.parent_clauses: canonical records or digests required")
    require(clauses == sorted(clauses, key=lambda item: item["parent_global_state_id"]),
            "recurrence_skeleton.parent_clauses: canonical parent order required")
    parents = [record["parent_global_state_id"] for record in clauses]
    require(len(parents) == len(set(parents)), "recurrence_skeleton.parent_clauses: duplicate parent")
    interface_ids = [record["expected_interface_row_id"] for record in clauses if record["row_kind"] != "recurrent"]
    require(len(interface_ids) == len(set(interface_ids)), "recurrence_skeleton.parent_clauses: duplicate interface row ID")
    blocks = sorted({record["expected_block_id"] for record in clauses if record["row_kind"] == "recurrent"})
    interfaces = sorted(interface_ids)
    manifest = {
        "family_id": family_id,
        "expected_block_ids": blocks,
        "expected_interface_row_ids": interfaces,
        "expected_parent_global_state_ids": parents,
        "evidence": f"derived from recurrence skeleton {skeleton_id}: {evidence}",
    }
    manifest = global_family.exact_manifest(manifest)
    kind_counts = Counter(record["row_kind"] for record in clauses)
    block_parent_counts = Counter(record["expected_block_id"] for record in clauses if record["row_kind"] == "recurrent")
    output = {
        "family_id": family_id,
        "skeleton_id": skeleton_id,
        "evidence": evidence,
        "parent_clauses": clauses,
        "derived_family_manifest": manifest,
        "row_kind_distribution": [[kind, kind_counts[kind]] for kind in sorted(kind_counts)],
        "block_parent_distribution": [[block, block_parent_counts[block]] for block in sorted(block_parent_counts)],
    }
    output["recurrence_skeleton_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    global_certificate = certificate.get("global_integer_family_certificate")
    raw_skeleton = certificate.get("recurrence_skeleton")
    require(isinstance(global_certificate, dict), "global_integer_family_certificate: expected object")
    require(isinstance(raw_skeleton, dict), "recurrence_skeleton: expected object")
    global_family.validate_certificate(global_certificate)
    global_exact = global_family.exact_certificate(global_certificate)
    skeleton = exact_skeleton(raw_skeleton)
    require(raw_skeleton == skeleton, "recurrence_skeleton: canonical record or digest required")
    require(global_certificate["family_manifest"] == skeleton["derived_family_manifest"],
            "global family manifest differs from skeleton-derived manifest")

    clause_by_parent = {record["parent_global_state_id"]: record for record in skeleton["parent_clauses"]}
    row_bindings = []
    for row in global_exact["global_row_records"]:
        parent = row["parent_global_state_id"]
        require(parent in clause_by_parent, f"global row parent {parent}: absent from recurrence skeleton")
        clause = clause_by_parent[parent]
        require(row["row_kind"] == clause["row_kind"], f"global row parent {parent}: row kind mismatch")
        if row["row_kind"] == "recurrent":
            require(row["block_id"] == clause["expected_block_id"], f"global row parent {parent}: block mismatch")
            expected_row_id = f"recurrent::{row['block_id']}::{parent}"
            require(row["row_id"] == expected_row_id, f"global row parent {parent}: recurrent row ID mismatch")
        else:
            require(row["row_id"] == clause["expected_interface_row_id"],
                    f"global row parent {parent}: interface row ID mismatch")
        binding = {
            "parent_global_state_id": parent,
            "row_id": row["row_id"],
            "row_kind": row["row_kind"],
            "block_id": row["block_id"],
            "source_rule_id": clause["source_rule_id"],
            "source_case_id": clause["source_case_id"],
            "skeleton_clause_sha256": clause["skeleton_clause_sha256"],
            "global_row_sha256": row["global_row_sha256"],
        }
        binding["row_binding_sha256"] = catalogue.canonical_digest(binding)
        row_bindings.append(binding)
    row_bindings.sort(key=lambda item: item["parent_global_state_id"])
    require(len(row_bindings) == len(skeleton["parent_clauses"]), "recurrence skeleton/global row cardinality mismatch")

    claims = {
        "parents": len(row_bindings),
        "blocks": len(skeleton["derived_family_manifest"]["expected_block_ids"]),
        "interface_rows": len(skeleton["derived_family_manifest"]["expected_interface_row_ids"]),
        "recurrent_parents": sum(record["row_kind"] == "recurrent" for record in row_bindings),
        "interface_parents": sum(record["row_kind"] != "recurrent" for record in row_bindings),
        "global_family_complete": global_exact["claims"]["complete_global_integer_family"],
        "skeleton_manifest_exact": 1,
        "skeleton_row_binding_exact": 1,
        "global_family_sha256": global_certificate["certificate_sha256"],
        "recurrence_skeleton_sha256": skeleton["recurrence_skeleton_sha256"],
        "row_bindings_sha256": catalogue.canonical_digest(row_bindings),
    }
    return {"recurrence_skeleton": skeleton, "row_bindings": row_bindings, "claims": claims}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("recurrence_skeleton", "row_bindings", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload), "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {"parents": claims["parents"], "blocks": claims["blocks"],
            "interfaces": claims["interface_rows"], "exact": claims["skeleton_manifest_exact"]}


def build_certificate(global_certificate: dict[str, Any], recurrence_skeleton: dict[str, Any]) -> dict[str, Any]:
    skeleton = exact_skeleton(recurrence_skeleton)
    certificate: dict[str, Any] = {
        "version": 1,
        "global_integer_family_certificate": global_certificate,
        "recurrence_skeleton": skeleton,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_global_family_skeleton.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
