#!/usr/bin/env python3
"""Validate the final documentary handoff from quotient certificates to an induction proof.

Six fixed handoff assertions summarize the ordinary proof that must be reviewed: base domain,
nonbase recurrence coverage, invariant preservation, termination, exceptional closure, and
translation of the quotient conclusion to D(n)=2n. Each assertion is effective only when its
fixed premise dependencies are effective and it carries a proof artifact.

The checker can mark a handoff dossier ready but always states that it has not proved the
mathematics itself.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import check_prime_power_artifact_support_dag as artifact_dag
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_final_implication_premise_contract as contract
import check_prime_power_global_quotient_semantic_refinement as refinement
import check_prime_power_premise_artifact_registry as premise_registry


class FinalInductionHandoffError(ValueError):
    """Raised when the final induction handoff dossier is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise FinalInductionHandoffError(message)


HANDOFF_DEPENDENCIES: dict[str, tuple[str, ...]] = {
    "BASE_DOMAIN_ESTABLISHED": ("BASE_CASES_COMPLETE",),
    "NONBASE_RECURRENCE_COVERS_ALL_CASES": ("RECURRENCE_EXHAUSTIVE", "OPERATION_SELECTION_SOUND"),
    "STATE_AND_RESOURCE_INVARIANTS_PRESERVED": (
        "STATE_INVARIANTS_PRESERVED", "RESOURCE_AND_CREDIT_SOUND"
    ),
    "EVERY_RECURRENCE_BRANCH_TERMINATES": (
        "BLOCK_AND_AUXILIARY_CONTRACTION", "CROSS_BLOCK_ASSEMBLY_SOUND", "TERMINATION_ARGUMENT"
    ),
    "EXCEPTIONAL_AND_HARD_CORE_CASES_CLOSED": ("EXCEPTIONAL_CASES_CLOSED",),
    "QUOTIENT_CONCLUSION_TRANSLATES_TO_D_EQ_2N": ("OBJECTIVE_TRANSLATION_TO_D_EQ_2N",),
}


def exact_assertion(record: dict[str, Any], assertion_id: str) -> dict[str, Any]:
    require(record.get("assertion_id") == assertion_id, f"assertion {assertion_id}: ID mismatch")
    status = record.get("status")
    dependencies = record.get("dependency_premise_ids")
    locator = record.get("artifact_locator")
    digest = record.get("artifact_digest")
    statement = record.get("statement")
    note = record.get("note")
    require(status in {"proved", "open"}, f"assertion {assertion_id}: bad status")
    require(dependencies == list(HANDOFF_DEPENDENCIES[assertion_id]),
            f"assertion {assertion_id}: exact dependency list required")
    require(isinstance(statement, str) and statement, f"assertion {assertion_id}: statement required")
    require(isinstance(note, str) and note, f"assertion {assertion_id}: note required")
    if status == "proved":
        require(isinstance(locator, str) and locator, f"assertion {assertion_id}: artifact locator required")
        require(isinstance(digest, str) and digest, f"assertion {assertion_id}: artifact digest required")
    else:
        require(locator is None and digest is None,
                f"assertion {assertion_id}: open assertion requires null artifact fields")
    output = {
        "assertion_id": assertion_id,
        "status": status,
        "dependency_premise_ids": list(HANDOFF_DEPENDENCIES[assertion_id]),
        "artifact_locator": locator,
        "artifact_digest": digest,
        "statement": statement,
        "note": note,
    }
    output["handoff_assertion_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    premise_registry_certificate = certificate.get("premise_artifact_registry_certificate")
    artifact_dag_certificate = certificate.get("artifact_support_dag_certificate")
    refinement_certificate = certificate.get("global_quotient_semantic_refinement_certificate")
    raw_assertions = certificate.get("handoff_assertions")
    require(isinstance(premise_registry_certificate, dict),
            "premise_artifact_registry_certificate: expected object")
    require(isinstance(artifact_dag_certificate, dict), "artifact_support_dag_certificate: expected object")
    require(isinstance(refinement_certificate, dict),
            "global_quotient_semantic_refinement_certificate: expected object")
    require(isinstance(raw_assertions, list), "handoff_assertions: expected list")
    premise_registry.validate_certificate(premise_registry_certificate)
    artifact_dag.validate_certificate(artifact_dag_certificate)
    refinement.validate_certificate(refinement_certificate)

    contract_certificate = premise_registry_certificate["final_implication_premise_contract_certificate"]
    contract.validate_certificate(contract_certificate)
    contract_exact = contract.exact_certificate(contract_certificate)
    require(artifact_dag_certificate["obligation_artifact_registry_certificate"]["certificate_sha256"]
            == contract_certificate["obligation_artifact_registry_certificate"]["certificate_sha256"],
            "artifact DAG and premise registry use different obligation artifact registries")
    closure_certificate = contract_certificate["obligation_artifact_registry_certificate"][
        "all_n_implication_closure_certificate"
    ]
    closure_skeleton_sha = closure_certificate["global_family_skeleton_certificate"]["certificate_sha256"]
    require(refinement_certificate["global_family_skeleton_certificate"]["certificate_sha256"]
            == closure_skeleton_sha,
            "semantic refinement and final contract use different global-family skeletons")
    require(refinement_certificate["state_equivalence_evidence_certificate"]["certificate_sha256"]
            == closure_certificate["state_equivalence_evidence_certificate"]["certificate_sha256"],
            "semantic refinement and final contract use different equivalence evidence")

    assertion_ids = list(HANDOFF_DEPENDENCIES)
    require([record.get("assertion_id") for record in raw_assertions] == assertion_ids,
            "handoff_assertions: exact canonical assertion order required")
    assertions = [exact_assertion(record, assertion_id)
                  for record, assertion_id in zip(raw_assertions, assertion_ids)]
    require(raw_assertions == assertions, "handoff_assertions: canonical records or digests required")

    premise_results = {record["premise_id"]: record
                       for record in contract_exact["premise_result_records"]}
    result_records = []
    for assertion in assertions:
        dependencies_effective = all(
            premise_results[premise_id]["effective_premise_closed"]
            for premise_id in assertion["dependency_premise_ids"]
        )
        effective = int(assertion["status"] == "proved" and dependencies_effective)
        record = {
            "assertion_id": assertion["assertion_id"],
            "declared_proved": int(assertion["status"] == "proved"),
            "dependencies_effective": int(dependencies_effective),
            "effective_assertion_closed": effective,
            "open_dependency_premise_ids": [
                premise_id for premise_id in assertion["dependency_premise_ids"]
                if not premise_results[premise_id]["effective_premise_closed"]
            ],
            "handoff_assertion_sha256": assertion["handoff_assertion_sha256"],
        }
        record["handoff_assertion_result_sha256"] = catalogue.canonical_digest(record)
        result_records.append(record)

    all_effective = int(all(record["effective_assertion_closed"] for record in result_records))
    refinement_exact = refinement.exact_certificate(refinement_certificate)
    premise_registry_exact = premise_registry.exact_certificate(premise_registry_certificate)
    artifact_dag_exact = artifact_dag.exact_certificate(artifact_dag_certificate)
    ready = int(
        contract_exact["claims"]["final_implication_contract_ready"]
        and premise_registry_exact["claims"]["exact_typed_premise_artifact_coverage"]
        and artifact_dag_exact["claims"]["acyclic_artifact_support"]
        and artifact_dag_exact["claims"]["immediate_dependency_artifact_coverage"]
        and refinement_exact["claims"]["complete_state_semantic_coverage"]
        and refinement_exact["claims"]["complete_row_semantic_coverage"]
        and all_effective
    )
    open_assertions = [record["assertion_id"] for record in result_records
                       if not record["effective_assertion_closed"]]
    claims = {
        "handoff_assertions": len(assertions),
        "effective_closed_assertions": sum(record["effective_assertion_closed"] for record in result_records),
        "open_assertions": len(open_assertions),
        "all_assertions_effective": all_effective,
        "final_induction_handoff_ready": ready,
        "all_n_proved_by_checker": 0,
        "open_assertion_ids": open_assertions,
        "premise_artifact_registry_sha256": premise_registry_certificate["certificate_sha256"],
        "artifact_support_dag_sha256": artifact_dag_certificate["certificate_sha256"],
        "semantic_refinement_sha256": refinement_certificate["certificate_sha256"],
        "assertions_sha256": catalogue.canonical_digest(assertions),
        "assertion_results_sha256": catalogue.canonical_digest(result_records),
    }
    return {"handoff_assertions": assertions, "handoff_assertion_result_records": result_records, "claims": claims}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("handoff_assertions", "handoff_assertion_result_records", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {"assertions": claims["handoff_assertions"], "closed": claims["effective_closed_assertions"],
            "open": claims["open_assertions"], "ready": claims["final_induction_handoff_ready"]}


def build_certificate(premise_registry_certificate: dict[str, Any], artifact_dag_certificate: dict[str, Any],
                      refinement_certificate: dict[str, Any], assertions: list[dict[str, Any]]) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "premise_artifact_registry_certificate": premise_registry_certificate,
        "artifact_support_dag_certificate": artifact_dag_certificate,
        "global_quotient_semantic_refinement_certificate": refinement_certificate,
        "handoff_assertions": assertions,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_final_induction_handoff.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
