#!/usr/bin/env python3
"""Publish a transparent integrity audit of the complete final induction handoff dossier.

The handoff checker already composes the pre-root premise contract, typed premise artifacts,
noncircular obligation-artifact support, quotient semantic refinement and six final induction
assertions. This checker reconstructs every nested readiness gate and shared certificate identity
from that one handoff certificate and publishes the exact remaining blocker sets.

The audit is documentary. It never closes the root implication obligation, verifies ordinary
mathematical reasoning or declares the no-three-in-line conjecture proved.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import check_prime_power_all_n_implication_closure as closure
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_final_implication_premise_contract as contract
import check_prime_power_final_induction_handoff as handoff
import check_prime_power_global_quotient_semantic_refinement as refinement
import check_prime_power_obligation_artifact_support_dag as support_dag
import check_prime_power_premise_artifact_registry as premise_artifacts


class FinalDossierIntegrityError(ValueError):
    """Raised when the final handoff integrity audit is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise FinalDossierIntegrityError(message)


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    handoff_certificate = certificate.get("final_induction_handoff_certificate")
    require(isinstance(handoff_certificate, dict),
            "final_induction_handoff_certificate: expected object")
    handoff.validate_certificate(handoff_certificate)
    handoff_exact = handoff.exact_certificate(handoff_certificate)

    premise_certificate = handoff_certificate["premise_artifact_registry_certificate"]
    support_certificate = handoff_certificate["artifact_support_dag_certificate"]
    refinement_certificate = handoff_certificate["global_quotient_semantic_refinement_certificate"]
    premise_artifacts.validate_certificate(premise_certificate)
    support_dag.validate_certificate(support_certificate)
    refinement.validate_certificate(refinement_certificate)
    premise_exact = premise_artifacts.exact_certificate(premise_certificate)
    support_exact = support_dag.exact_certificate(support_certificate)
    refinement_exact = refinement.exact_certificate(refinement_certificate)

    contract_certificate = premise_certificate["final_implication_premise_contract_certificate"]
    contract.validate_certificate(contract_certificate)
    contract_exact = contract.exact_certificate(contract_certificate)
    obligation_registry = contract_certificate["obligation_artifact_registry_certificate"]
    closure_certificate = obligation_registry["all_n_implication_closure_certificate"]
    closure.validate_certificate(closure_certificate)
    closure_exact = closure.exact_certificate(closure_certificate)

    require(
        support_certificate["obligation_artifact_registry_certificate"]["certificate_sha256"]
        == obligation_registry["certificate_sha256"],
        "handoff support DAG and premise contract use different obligation registries",
    )
    require(
        refinement_certificate["global_family_skeleton_certificate"]["certificate_sha256"]
        == closure_certificate["global_family_skeleton_certificate"]["certificate_sha256"],
        "handoff refinement and closure use different global-family skeletons",
    )
    require(
        refinement_certificate["state_equivalence_evidence_certificate"]["certificate_sha256"]
        == closure_certificate["state_equivalence_evidence_certificate"]["certificate_sha256"],
        "handoff refinement and closure use different equivalence evidence",
    )

    support_claims = support_exact["claims"]
    support_ready = int(
        support_claims["artifact_support_acyclic"]
        and support_claims["artifact_support_dependency_aligned"]
        and support_claims["exact_dependency_artifact_support_coverage"]
    )
    semantic_ready = int(
        refinement_exact["claims"]["complete_state_semantic_coverage"]
        and refinement_exact["claims"]["complete_row_semantic_coverage"]
    )
    gate_record = {
        "finite_interface_ready": int(closure_exact["claims"]["finite_interface_ready"]),
        "root_implication_dependencies_closed": int(
            contract_exact["claims"]["root_implication_dependencies_closed"]
        ),
        "final_implication_contract_ready": int(
            contract_exact["claims"]["final_implication_contract_ready"]
        ),
        "typed_premise_artifact_coverage_ready": int(
            premise_exact["claims"]["exact_typed_premise_artifact_coverage"]
        ),
        "obligation_artifact_support_integrity_ready": support_ready,
        "global_quotient_semantic_refinement_ready": semantic_ready,
        "final_induction_handoff_ready": int(
            handoff_exact["claims"]["final_induction_handoff_ready"]
        ),
    }
    final_ready = int(all(gate_record.values()))
    gate_record["final_dossier_integrity_ready"] = final_ready
    gate_record["final_dossier_gate_sha256"] = catalogue.canonical_digest(gate_record)

    blocker_record = {
        "open_semantic_obligation_ids": closure_exact["claims"]["open_obligation_ids"],
        "current_frontier_obligation_ids": closure_exact["claims"]["current_frontier_obligation_ids"],
        "open_premise_ids": contract_exact["claims"]["open_premise_ids"],
        "open_handoff_assertion_ids": handoff_exact["claims"]["open_assertion_ids"],
        "root_implication_obligation_closed": closure_exact["claims"][
            "root_implication_obligation_closed"
        ],
        "root_implication_open_and_actionable": contract_exact["claims"][
            "root_implication_open_and_actionable"
        ],
    }
    blocker_record["final_dossier_blockers_sha256"] = catalogue.canonical_digest(blocker_record)

    claims = {
        "integrity_gates": 7,
        "satisfied_integrity_gates": sum(
            gate_record[key]
            for key in (
                "finite_interface_ready",
                "root_implication_dependencies_closed",
                "final_implication_contract_ready",
                "typed_premise_artifact_coverage_ready",
                "obligation_artifact_support_integrity_ready",
                "global_quotient_semantic_refinement_ready",
                "final_induction_handoff_ready",
            )
        ),
        "final_dossier_integrity_ready": final_ready,
        "all_n_proved_by_checker": 0,
        "maximum_artifact_support_depth": support_claims["maximum_artifact_support_depth"],
        "final_induction_handoff_sha256": handoff_certificate["certificate_sha256"],
        "final_contract_sha256": contract_certificate["certificate_sha256"],
        "premise_artifact_registry_sha256": premise_certificate["certificate_sha256"],
        "obligation_artifact_support_dag_sha256": support_certificate["certificate_sha256"],
        "semantic_refinement_sha256": refinement_certificate["certificate_sha256"],
        "obligation_artifact_registry_sha256": obligation_registry["certificate_sha256"],
        "closure_sha256": closure_certificate["certificate_sha256"],
        "final_dossier_gate_sha256": gate_record["final_dossier_gate_sha256"],
        "final_dossier_blockers_sha256": blocker_record["final_dossier_blockers_sha256"],
    }
    return {
        "final_dossier_gate": gate_record,
        "final_dossier_blockers": blocker_record,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("final_dossier_gate", "final_dossier_blockers", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {
        "gates": claims["integrity_gates"],
        "satisfied": claims["satisfied_integrity_gates"],
        "ready": claims["final_dossier_integrity_ready"],
        "proved": claims["all_n_proved_by_checker"],
    }


def build_certificate(handoff_certificate: dict[str, Any]) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "final_induction_handoff_certificate": handoff_certificate,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_final_dossier_integrity.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
