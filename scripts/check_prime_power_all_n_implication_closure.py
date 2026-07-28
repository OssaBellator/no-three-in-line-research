#!/usr/bin/env python3
"""Publish the exact semantic proof-obligation closure needed beyond the finite quotient.

The checker composes the independently derived global-family skeleton, spanning state-
equivalence evidence and global support-condensation certificate. It then validates a fixed
proof-obligation DAG. An obligation closes only when its own supplied artifact is marked
proved and every dependency is closed. The all-n readiness flag cannot turn on while any
named semantic obligation remains open.

This is a documentary closure interface. It does not verify the mathematical truth of the
supplied proof artifacts and therefore never labels the conjecture proved by itself.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_global_family_skeleton as skeleton
import check_prime_power_global_support_condensation as support
import check_prime_power_state_equivalence_spanning_evidence as equivalence


class AllNClosureError(ValueError):
    """Raised when the semantic proof-obligation closure dossier is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AllNClosureError(message)


OBLIGATION_DEPENDENCIES: dict[str, tuple[str, ...]] = {
    "SOURCE_STATEMENTS_TRUE": (),
    "RULE_EXHAUSTIVE": ("SOURCE_STATEMENTS_TRUE",),
    "SLOT_AND_CANDIDATE_POPULATION": ("RULE_EXHAUSTIVE",),
    "GEOMETRY_SELECTOR_CORRECT": ("SLOT_AND_CANDIDATE_POPULATION",),
    "FATE_TRANSITION_STATE_SEMANTICS": ("SLOT_AND_CANDIDATE_POPULATION",),
    "CANDIDATE_POLICY_CORRECT": ("GEOMETRY_SELECTOR_CORRECT", "FATE_TRANSITION_STATE_SEMANTICS"),
    "ACTIVE_ROW_FAMILY_EXHAUSTIVE": ("CANDIDATE_POLICY_CORRECT",),
    "DESTROYED_RESOURCE_MODEL_EXHAUSTIVE": ("ACTIVE_ROW_FAMILY_EXHAUSTIVE", "GEOMETRY_SELECTOR_CORRECT"),
    "CREDIT_ROUTING_SEMANTIC": ("DESTROYED_RESOURCE_MODEL_EXHAUSTIVE", "FATE_TRANSITION_STATE_SEMANTICS"),
    "CLOSED_STRICT_RECURRENT_BLOCKS": ("CANDIDATE_POLICY_CORRECT", "CREDIT_ROUTING_SEMANTIC"),
    "AUXILIARY_EXPANSIONS_SEMANTIC": (
        "FATE_TRANSITION_STATE_SEMANTICS", "CLOSED_STRICT_RECURRENT_BLOCKS"
    ),
    "CROSS_BLOCK_STATE_IDENTITY_SEMANTIC": ("FATE_TRANSITION_STATE_SEMANTICS",),
    "COMPONENT_SCALE_SEMANTIC": ("CROSS_BLOCK_STATE_IDENTITY_SEMANTIC", "CLOSED_STRICT_RECURRENT_BLOCKS"),
    "INTERFACE_RETURN_ROWS_EXHAUSTIVE": ("COMPONENT_SCALE_SEMANTIC", "FATE_TRANSITION_STATE_SEMANTICS"),
    "GLOBAL_RANK_WELL_FOUNDED": ("INTERFACE_RETURN_ROWS_EXHAUSTIVE",),
    "EXPECTED_GLOBAL_FAMILY_EXHAUSTIVE": (
        "RULE_EXHAUSTIVE", "INTERFACE_RETURN_ROWS_EXHAUSTIVE", "CLOSED_STRICT_RECURRENT_BLOCKS"
    ),
    "EXCEPTIONAL_ZERO_ROWS_CLOSED": (
        "GEOMETRY_SELECTOR_CORRECT", "CREDIT_ROUTING_SEMANTIC", "INTERFACE_RETURN_ROWS_EXHAUSTIVE"
    ),
    "HARD_CORE_ROWS_CLOSED": (
        "GEOMETRY_SELECTOR_CORRECT", "CREDIT_ROUTING_SEMANTIC", "INTERFACE_RETURN_ROWS_EXHAUSTIVE"
    ),
    "GLOBAL_QUOTIENT_IMPLIES_ALL_N": (
        "EXPECTED_GLOBAL_FAMILY_EXHAUSTIVE", "GLOBAL_RANK_WELL_FOUNDED",
        "EXCEPTIONAL_ZERO_ROWS_CLOSED", "HARD_CORE_ROWS_CLOSED", "AUXILIARY_EXPANSIONS_SEMANTIC"
    ),
}


def exact_obligation(record: dict[str, Any], obligation_id: str) -> dict[str, Any]:
    require(record.get("obligation_id") == obligation_id, f"obligation {obligation_id}: ID mismatch")
    status = record.get("status")
    dependencies = record.get("dependency_ids")
    artifact_locator = record.get("artifact_locator")
    artifact_digest = record.get("artifact_digest")
    note = record.get("note")
    require(status in {"proved", "open"}, f"obligation {obligation_id}: bad status")
    require(dependencies == list(OBLIGATION_DEPENDENCIES[obligation_id]),
            f"obligation {obligation_id}: exact dependency list required")
    require(isinstance(note, str) and note, f"obligation {obligation_id}: note required")
    if status == "proved":
        require(isinstance(artifact_locator, str) and artifact_locator,
                f"obligation {obligation_id}: proved status requires artifact locator")
        require(isinstance(artifact_digest, str) and artifact_digest,
                f"obligation {obligation_id}: proved status requires artifact digest")
    else:
        require(artifact_locator is None, f"obligation {obligation_id}: open status requires null artifact locator")
        require(artifact_digest is None, f"obligation {obligation_id}: open status requires null artifact digest")
    output = {
        "obligation_id": obligation_id,
        "status": status,
        "dependency_ids": list(OBLIGATION_DEPENDENCIES[obligation_id]),
        "artifact_locator": artifact_locator,
        "artifact_digest": artifact_digest,
        "note": note,
    }
    output["obligation_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    skeleton_certificate = certificate.get("global_family_skeleton_certificate")
    equivalence_certificate = certificate.get("state_equivalence_evidence_certificate")
    support_certificate = certificate.get("global_support_condensation_certificate")
    raw_obligations = certificate.get("proof_obligations")
    require(isinstance(skeleton_certificate, dict), "global_family_skeleton_certificate: expected object")
    require(isinstance(equivalence_certificate, dict), "state_equivalence_evidence_certificate: expected object")
    require(isinstance(support_certificate, dict), "global_support_condensation_certificate: expected object")
    require(isinstance(raw_obligations, list), "proof_obligations: expected list")
    skeleton.validate_certificate(skeleton_certificate)
    equivalence.validate_certificate(equivalence_certificate)
    support.validate_certificate(support_certificate)
    skeleton_exact = skeleton.exact_certificate(skeleton_certificate)
    equivalence_exact = equivalence.exact_certificate(equivalence_certificate)
    support_exact = support.exact_certificate(support_certificate)

    global_sha = skeleton_certificate["global_integer_family_certificate"]["certificate_sha256"]
    require(support_certificate["global_integer_family_certificate"]["certificate_sha256"] == global_sha,
            "support and skeleton certificates use different global families")
    id_sha = skeleton_certificate["global_integer_family_certificate"]["interface_row_certificate"][
        "weight_synchronization_certificate"
    ]["state_identification_certificate"]["certificate_sha256"]
    require(equivalence_certificate["state_identification_certificate"]["certificate_sha256"] == id_sha,
            "equivalence evidence uses different state-identification certificate")

    expected_ids = list(OBLIGATION_DEPENDENCIES)
    require(len(raw_obligations) == len(expected_ids), "proof_obligations: exact fixed obligation count required")
    require([record.get("obligation_id") for record in raw_obligations] == expected_ids,
            "proof_obligations: exact canonical obligation order required")
    obligations = [exact_obligation(record, obligation_id) for record, obligation_id in zip(raw_obligations, expected_ids)]
    require(raw_obligations == obligations, "proof_obligations: canonical records or digests required")

    closure: dict[str, int] = {}
    closure_records = []
    for record in obligations:
        obligation_id = record["obligation_id"]
        dependencies_closed = all(closure[dependency] for dependency in record["dependency_ids"])
        closed = int(record["status"] == "proved" and dependencies_closed)
        closure[obligation_id] = closed
        closure_record = {
            "obligation_id": obligation_id,
            "declared_proved": int(record["status"] == "proved"),
            "dependencies_closed": int(dependencies_closed),
            "closed": closed,
            "open_dependency_ids": [dependency for dependency in record["dependency_ids"] if not closure[dependency]],
            "obligation_record_sha256": record["obligation_record_sha256"],
        }
        closure_record["obligation_closure_sha256"] = catalogue.canonical_digest(closure_record)
        closure_records.append(closure_record)

    interface_ready = int(
        skeleton_exact["claims"]["skeleton_manifest_exact"]
        and skeleton_exact["claims"]["skeleton_row_binding_exact"]
        and equivalence_exact["claims"]["complete_spanning_equivalence_evidence"]
        and support_exact["claims"]["critical_edge_graph_acyclic"]
        and support_exact["claims"]["every_support_cycle_contains_strict_edge"]
        and skeleton_exact["claims"]["global_family_complete"]
    )
    root_closed = closure["GLOBAL_QUOTIENT_IMPLIES_ALL_N"]
    all_n_readiness = int(interface_ready and root_closed)
    status_counts = Counter(record["status"] for record in obligations)
    open_ids = [record["obligation_id"] for record in obligations if not closure[record["obligation_id"]]]
    frontier_ids = [
        record["obligation_id"] for record in obligations
        if not closure[record["obligation_id"]]
        and all(closure[dependency] for dependency in record["dependency_ids"])
    ]
    claims = {
        "proof_obligations": len(obligations),
        "declared_proved_obligations": status_counts["proved"],
        "declared_open_obligations": status_counts["open"],
        "closed_obligations": sum(closure.values()),
        "unclosed_obligations": len(obligations) - sum(closure.values()),
        "current_frontier_obligations": len(frontier_ids),
        "finite_interface_ready": interface_ready,
        "root_implication_obligation_closed": root_closed,
        "all_n_implication_dossier_ready": all_n_readiness,
        "all_n_proved_by_checker": 0,
        "open_obligation_ids": open_ids,
        "current_frontier_obligation_ids": frontier_ids,
        "global_family_skeleton_sha256": skeleton_certificate["certificate_sha256"],
        "state_equivalence_evidence_sha256": equivalence_certificate["certificate_sha256"],
        "global_support_condensation_sha256": support_certificate["certificate_sha256"],
        "global_family_sha256": global_sha,
        "obligations_sha256": catalogue.canonical_digest(obligations),
        "closure_records_sha256": catalogue.canonical_digest(closure_records),
    }
    return {"proof_obligations": obligations, "obligation_closure_records": closure_records, "claims": claims}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("proof_obligations", "obligation_closure_records", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload), "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {"obligations": claims["proof_obligations"], "closed": claims["closed_obligations"],
            "frontier": claims["current_frontier_obligations"], "ready": claims["all_n_implication_dossier_ready"]}


def build_certificate(skeleton_certificate: dict[str, Any], equivalence_certificate: dict[str, Any],
                      support_certificate: dict[str, Any], proof_obligations: list[dict[str, Any]]) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "global_family_skeleton_certificate": skeleton_certificate,
        "state_equivalence_evidence_certificate": equivalence_certificate,
        "global_support_condensation_certificate": support_certificate,
        "proof_obligations": proof_obligations,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_all_n_implication_closure.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
