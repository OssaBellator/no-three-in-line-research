#!/usr/bin/env python3
"""Compose the atomic all-frontier target manifest with the newest proof registries.

The atomic target checker covers all thirteen genuine frontiers. This wrapper additionally
requires the typed handoff-assertion artifact registry and the exact 252-chamber disposition
registry, checks shared certificate identities, and synchronizes the exceptional and handoff
targets with those authoritative layers.

The result is an execution interface, not a mathematical proof. It permanently reports
``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import check_prime_power_atomic_frontier_execution as atomic
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_exceptional_chamber_disposition_registry as chambers
import check_prime_power_handoff_assertion_artifact_registry as handoff_artifacts


class CurrentFrontierExecutionError(ValueError):
    """Raised when the current-frontier execution stack is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CurrentFrontierExecutionError(message)


ASSERTION_TARGETS: dict[str, str] = {
    "BASE_DOMAIN_ESTABLISHED": "T35_BASE_HANDOFF",
    "NONBASE_RECURRENCE_COVERS_ALL_CASES": "T36_RECURRENCE_HANDOFF",
    "STATE_AND_RESOURCE_INVARIANTS_PRESERVED": "T37_INVARIANT_HANDOFF",
    "EVERY_RECURRENCE_BRANCH_TERMINATES": "T38_TERMINATION_HANDOFF",
    "EXCEPTIONAL_AND_HARD_CORE_CASES_CLOSED": "T39_EXCEPTIONAL_HANDOFF",
    "QUOTIENT_CONCLUSION_TRANSLATES_TO_D_EQ_2N": "T40_TRANSLATION_HANDOFF",
}


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    atomic_certificate = certificate.get("atomic_frontier_execution_certificate")
    handoff_artifact_certificate = certificate.get("handoff_assertion_artifact_registry_certificate")
    chamber_certificate = certificate.get("exceptional_chamber_disposition_certificate")
    require(isinstance(atomic_certificate, dict),
            "atomic_frontier_execution_certificate: expected object")
    require(isinstance(handoff_artifact_certificate, dict),
            "handoff_assertion_artifact_registry_certificate: expected object")
    require(isinstance(chamber_certificate, dict),
            "exceptional_chamber_disposition_certificate: expected object")

    atomic.validate_certificate(atomic_certificate)
    handoff_artifacts.validate_certificate(handoff_artifact_certificate)
    chambers.validate_certificate(chamber_certificate)
    atomic_exact = atomic.exact_certificate(atomic_certificate)
    handoff_exact = handoff_artifacts.exact_certificate(handoff_artifact_certificate)
    chamber_exact = chambers.exact_certificate(chamber_certificate)

    dossier_certificate = atomic_certificate["final_dossier_integrity_certificate"]
    final_handoff_certificate = dossier_certificate["final_induction_handoff_certificate"]
    require(
        handoff_artifact_certificate["final_induction_handoff_certificate"]["certificate_sha256"]
        == final_handoff_certificate["certificate_sha256"],
        "atomic frontier and handoff artifact registry use different final handoffs",
    )
    refinement_certificate = final_handoff_certificate[
        "global_quotient_semantic_refinement_certificate"
    ]
    require(
        chamber_certificate["global_quotient_semantic_refinement_certificate"]["certificate_sha256"]
        == refinement_certificate["certificate_sha256"],
        "atomic frontier and chamber registry use different quotient refinements",
    )

    target_by_id = {
        record["target_id"]: record for record in atomic_exact["target_result_records"]
    }
    handoff_bundle_by_id = {
        record["assertion_id"]: record
        for record in handoff_exact["handoff_assertion_artifact_bundle_records"]
    }

    assertion_sync_records = []
    for assertion_id, target_id in ASSERTION_TARGETS.items():
        target_complete = int(target_by_id[target_id]["effective_target_complete"])
        bundle = handoff_bundle_by_id[assertion_id]
        artifact_complete = int(
            bundle["declared_status"] == "proved"
            and bundle["effective_assertion_closed"]
            and len(bundle["artifact_ids"]) == 1
        )
        require(target_complete == artifact_complete,
                f"assertion {assertion_id}: target and typed handoff artifact disagree")
        record = {
            "assertion_id": assertion_id,
            "target_id": target_id,
            "target_complete": target_complete,
            "typed_handoff_artifact_complete": artifact_complete,
            "handoff_artifact_bundle_sha256": bundle[
                "handoff_assertion_artifact_bundle_sha256"
            ],
        }
        record["assertion_target_sync_sha256"] = catalogue.canonical_digest(record)
        assertion_sync_records.append(record)

    chamber_claims = chamber_exact["claims"]
    exceptional_sync_records = []
    for target_id, chamber_kind, ready_key, closed_key, open_key in (
        (
            "T20_EXCEPTIONAL_ZERO_ROWS",
            "zero-selector",
            "exceptional_zero_rows_ready",
            "closed_zero_selector_chambers",
            "open_zero_selector_chambers",
        ),
        (
            "T21_HARD_CORE_ROWS",
            "hard-core",
            "hard_core_rows_ready",
            "closed_hard_core_chambers",
            "open_hard_core_chambers",
        ),
    ):
        target_complete = int(target_by_id[target_id]["effective_target_complete"])
        registry_ready = int(chamber_claims[ready_key])
        require(target_complete == registry_ready,
                f"target {target_id}: completion disagrees with chamber registry")
        record = {
            "target_id": target_id,
            "chamber_kind": chamber_kind,
            "target_complete": target_complete,
            "registry_ready": registry_ready,
            "closed_chambers": chamber_claims[closed_key],
            "open_chambers": chamber_claims[open_key],
        }
        record["exceptional_target_sync_sha256"] = catalogue.canonical_digest(record)
        exceptional_sync_records.append(record)

    typed_handoff_ready = int(
        handoff_exact["claims"]["exact_typed_handoff_artifact_coverage"]
    )
    chamber_disposition_complete = int(
        chamber_claims["complete_exceptional_chamber_disposition"]
    )
    atomic_ready = int(atomic_exact["claims"]["final_frontier_execution_ready"])
    integrated_ready = int(
        atomic_ready and typed_handoff_ready and chamber_disposition_complete
    )
    gate_record = {
        "atomic_frontier_execution_ready": atomic_ready,
        "typed_handoff_artifact_coverage_ready": typed_handoff_ready,
        "exceptional_chamber_disposition_complete": chamber_disposition_complete,
        "current_frontier_execution_ready": integrated_ready,
    }
    gate_record["current_frontier_gate_sha256"] = catalogue.canonical_digest(gate_record)

    blocker_record = {
        "research_actionable_target_ids": atomic_exact["claims"][
            "research_actionable_target_ids"
        ],
        "proof_actionable_target_ids": atomic_exact["claims"][
            "proof_actionable_target_ids"
        ],
        "open_zero_selector_chambers": chamber_claims["open_zero_selector_chambers"],
        "open_hard_core_chambers": chamber_claims["open_hard_core_chambers"],
        "open_handoff_assertion_bundles": handoff_exact["claims"][
            "open_assertion_bundles"
        ],
        "minimum_parallel_proof_waves_to_root": atomic_exact["claims"][
            "minimum_parallel_proof_waves_to_root"
        ],
    }
    blocker_record["current_frontier_blockers_sha256"] = catalogue.canonical_digest(
        blocker_record
    )

    claims = {
        "frontier_groups": atomic_exact["claims"]["frontier_groups"],
        "atomic_targets": atomic_exact["claims"]["atomic_targets"],
        "handoff_assertion_artifact_bundles": handoff_exact["claims"][
            "handoff_assertions"
        ],
        "exceptional_chambers": chamber_claims["exceptional_chambers"],
        "zero_selector_chambers": chamber_claims["zero_selector_chambers"],
        "hard_core_chambers": chamber_claims["hard_core_selector_chambers"],
        "current_frontier_execution_ready": integrated_ready,
        "all_n_proved_by_checker": 0,
        "atomic_frontier_execution_sha256": atomic_certificate["certificate_sha256"],
        "handoff_artifact_registry_sha256": handoff_artifact_certificate[
            "certificate_sha256"
        ],
        "exceptional_chamber_disposition_sha256": chamber_certificate[
            "certificate_sha256"
        ],
        "assertion_target_sync_sha256": catalogue.canonical_digest(
            assertion_sync_records
        ),
        "exceptional_target_sync_sha256": catalogue.canonical_digest(
            exceptional_sync_records
        ),
        "current_frontier_gate_sha256": gate_record[
            "current_frontier_gate_sha256"
        ],
        "current_frontier_blockers_sha256": blocker_record[
            "current_frontier_blockers_sha256"
        ],
    }
    return {
        "handoff_assertion_target_sync_records": assertion_sync_records,
        "exceptional_target_sync_records": exceptional_sync_records,
        "current_frontier_gate": gate_record,
        "current_frontier_blockers": blocker_record,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in (
        "handoff_assertion_target_sync_records",
        "exceptional_target_sync_records",
        "current_frontier_gate",
        "current_frontier_blockers",
        "claims",
    ):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(
        certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
        "certificate_sha256: incorrect",
    )
    claims = exact["claims"]
    return {
        "frontiers": claims["frontier_groups"],
        "targets": claims["atomic_targets"],
        "chambers": claims["exceptional_chambers"],
        "ready": claims["current_frontier_execution_ready"],
        "proved": claims["all_n_proved_by_checker"],
    }


def build_certificate(
    atomic_certificate: dict[str, Any],
    handoff_artifact_certificate: dict[str, Any],
    chamber_certificate: dict[str, Any],
) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "atomic_frontier_execution_certificate": atomic_certificate,
        "handoff_assertion_artifact_registry_certificate": handoff_artifact_certificate,
        "exceptional_chamber_disposition_certificate": chamber_certificate,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_current_frontier_execution.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
