#!/usr/bin/env python3
"""Validate a fixed final implication-premise contract above the all-n closure dossier.

The contract separates ten ordinary mathematical premises: base cases, recurrence coverage,
invariants, operation selection, resource/credit soundness, block contraction, cross-block
assembly, exceptional closure, termination, and translation to D(n)=2n. Each proved premise
must have all required semantic obligations closed and one proof artifact.

The checker can mark a final implication dossier ready, but it never declares the theorem
proved or verifies the mathematical truth of the supplied premise artifacts.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import check_prime_power_all_n_implication_closure as closure
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_edgewise_lexicographic_support as edgewise
import check_prime_power_obligation_artifact_registry as artifacts
import check_prime_power_obligation_blocker_schedule as schedule


class FinalImplicationContractError(ValueError):
    """Raised when the final implication-premise contract is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise FinalImplicationContractError(message)


PREMISE_DEPENDENCIES: dict[str, tuple[str, ...]] = {
    "BASE_CASES_COMPLETE": ("SOURCE_STATEMENTS_TRUE",),
    "RECURRENCE_EXHAUSTIVE": ("RULE_EXHAUSTIVE", "EXPECTED_GLOBAL_FAMILY_EXHAUSTIVE"),
    "STATE_INVARIANTS_PRESERVED": ("GEOMETRY_SELECTOR_CORRECT", "FATE_TRANSITION_STATE_SEMANTICS"),
    "OPERATION_SELECTION_SOUND": ("SLOT_AND_CANDIDATE_POPULATION", "CANDIDATE_POLICY_CORRECT"),
    "RESOURCE_AND_CREDIT_SOUND": (
        "ACTIVE_ROW_FAMILY_EXHAUSTIVE", "DESTROYED_RESOURCE_MODEL_EXHAUSTIVE", "CREDIT_ROUTING_SEMANTIC"
    ),
    "BLOCK_AND_AUXILIARY_CONTRACTION": ("CLOSED_STRICT_RECURRENT_BLOCKS", "AUXILIARY_EXPANSIONS_SEMANTIC"),
    "CROSS_BLOCK_ASSEMBLY_SOUND": (
        "CROSS_BLOCK_STATE_IDENTITY_SEMANTIC", "COMPONENT_SCALE_SEMANTIC",
        "INTERFACE_RETURN_ROWS_EXHAUSTIVE", "GLOBAL_RANK_WELL_FOUNDED"
    ),
    "EXCEPTIONAL_CASES_CLOSED": ("EXCEPTIONAL_ZERO_ROWS_CLOSED", "HARD_CORE_ROWS_CLOSED"),
    "TERMINATION_ARGUMENT": ("CLOSED_STRICT_RECURRENT_BLOCKS", "GLOBAL_RANK_WELL_FOUNDED"),
    "OBJECTIVE_TRANSLATION_TO_D_EQ_2N": (
        "EXPECTED_GLOBAL_FAMILY_EXHAUSTIVE", "GLOBAL_RANK_WELL_FOUNDED",
        "EXCEPTIONAL_ZERO_ROWS_CLOSED", "HARD_CORE_ROWS_CLOSED",
        "AUXILIARY_EXPANSIONS_SEMANTIC",
    ),
}


def exact_premise(record: dict[str, Any], premise_id: str) -> dict[str, Any]:
    require(record.get("premise_id") == premise_id, f"premise {premise_id}: ID mismatch")
    status = record.get("status")
    dependencies = record.get("dependency_obligation_ids")
    proof_mode = record.get("proof_mode")
    locator = record.get("artifact_locator")
    digest = record.get("artifact_digest")
    note = record.get("note")
    require(status in {"proved", "open"}, f"premise {premise_id}: bad status")
    require(dependencies == list(PREMISE_DEPENDENCIES[premise_id]),
            f"premise {premise_id}: exact dependency list required")
    if premise_id == "TERMINATION_ARGUMENT":
        require(proof_mode in {"edgewise-lex", "semantic-multiset", "semantic-well-founded"},
                "TERMINATION_ARGUMENT: bad proof mode")
    else:
        require(proof_mode == "direct", f"premise {premise_id}: proof_mode must be direct")
    require(isinstance(note, str) and note, f"premise {premise_id}: note required")
    if status == "proved":
        require(isinstance(locator, str) and locator, f"premise {premise_id}: artifact locator required")
        require(isinstance(digest, str) and digest, f"premise {premise_id}: artifact digest required")
    else:
        require(locator is None and digest is None,
                f"premise {premise_id}: open premise requires null artifact fields")
    output = {
        "premise_id": premise_id,
        "status": status,
        "dependency_obligation_ids": list(PREMISE_DEPENDENCIES[premise_id]),
        "proof_mode": proof_mode,
        "artifact_locator": locator,
        "artifact_digest": digest,
        "note": note,
    }
    output["premise_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    registry_certificate = certificate.get("obligation_artifact_registry_certificate")
    schedule_certificate = certificate.get("obligation_blocker_schedule_certificate")
    edgewise_certificate = certificate.get("edgewise_lexicographic_support_certificate")
    raw_premises = certificate.get("implication_premises")
    require(isinstance(registry_certificate, dict),
            "obligation_artifact_registry_certificate: expected object")
    require(isinstance(schedule_certificate, dict),
            "obligation_blocker_schedule_certificate: expected object")
    require(isinstance(edgewise_certificate, dict),
            "edgewise_lexicographic_support_certificate: expected object")
    require(isinstance(raw_premises, list), "implication_premises: expected list")
    artifacts.validate_certificate(registry_certificate)
    schedule.validate_certificate(schedule_certificate)
    edgewise.validate_certificate(edgewise_certificate)
    require(schedule_certificate["obligation_artifact_registry_certificate"]["certificate_sha256"]
            == registry_certificate["certificate_sha256"],
            "schedule and premise contract use different artifact registries")

    closure_certificate = registry_certificate["all_n_implication_closure_certificate"]
    closure.validate_certificate(closure_certificate)
    closure_exact = closure.exact_certificate(closure_certificate)
    closure_by_id = {record["obligation_id"]: record
                     for record in closure_exact["obligation_closure_records"]}
    closure_support_sha = closure_certificate["global_support_condensation_certificate"]["certificate_sha256"]
    require(edgewise_certificate["global_support_condensation_certificate"]["certificate_sha256"]
            == closure_support_sha,
            "edgewise audit and closure dossier use different support certificates")

    premise_ids = list(PREMISE_DEPENDENCIES)
    require([record.get("premise_id") for record in raw_premises] == premise_ids,
            "implication_premises: exact canonical premise order required")
    premises = [exact_premise(record, premise_id)
                for record, premise_id in zip(raw_premises, premise_ids)]
    require(raw_premises == premises, "implication_premises: canonical records or digests required")

    edgewise_exact = edgewise.exact_certificate(edgewise_certificate)
    result_records = []
    for premise in premises:
        dependencies_closed = all(closure_by_id[obligation_id]["closed"]
                                  for obligation_id in premise["dependency_obligation_ids"])
        mode_ready = True
        if premise["premise_id"] == "TERMINATION_ARGUMENT" and premise["proof_mode"] == "edgewise-lex":
            mode_ready = bool(edgewise_exact["claims"]["complete_edgewise_lex_termination"])
        effective = int(premise["status"] == "proved" and dependencies_closed and mode_ready)
        result = {
            "premise_id": premise["premise_id"],
            "declared_proved": int(premise["status"] == "proved"),
            "dependencies_closed": int(dependencies_closed),
            "proof_mode_ready": int(mode_ready),
            "effective_premise_closed": effective,
            "open_dependency_obligation_ids": [
                obligation_id for obligation_id in premise["dependency_obligation_ids"]
                if not closure_by_id[obligation_id]["closed"]
            ],
            "premise_record_sha256": premise["premise_record_sha256"],
        }
        result["premise_result_sha256"] = catalogue.canonical_digest(result)
        result_records.append(result)

    all_effective = int(all(record["effective_premise_closed"] for record in result_records))
    root_id = "GLOBAL_QUOTIENT_IMPLIES_ALL_N"
    root_dependencies_closed = int(all(
        closure_by_id[obligation_id]["closed"]
        for obligation_id in closure.OBLIGATION_DEPENDENCIES[root_id]
    ))
    root_open_and_actionable = int(
        not closure_by_id[root_id]["closed"] and root_dependencies_closed
    )
    ready = int(
        closure_exact["claims"]["finite_interface_ready"]
        and artifacts.exact_certificate(registry_certificate)["claims"]["exact_typed_artifact_coverage"]
        and root_dependencies_closed
        and all_effective
    )
    open_premises = [record["premise_id"] for record in result_records
                     if not record["effective_premise_closed"]]
    claims = {
        "implication_premises": len(premises),
        "effective_closed_premises": sum(record["effective_premise_closed"] for record in result_records),
        "open_premises": len(open_premises),
        "all_premises_effective": all_effective,
        "edgewise_lex_termination_available": edgewise_exact["claims"]["complete_edgewise_lex_termination"],
        "root_implication_dependencies_closed": root_dependencies_closed,
        "root_implication_open_and_actionable": root_open_and_actionable,
        "final_implication_contract_ready": ready,
        "all_n_proved_by_checker": 0,
        "open_premise_ids": open_premises,
        "closure_sha256": closure_certificate["certificate_sha256"],
        "artifact_registry_sha256": registry_certificate["certificate_sha256"],
        "blocker_schedule_sha256": schedule_certificate["certificate_sha256"],
        "edgewise_support_sha256": edgewise_certificate["certificate_sha256"],
        "premises_sha256": catalogue.canonical_digest(premises),
        "premise_results_sha256": catalogue.canonical_digest(result_records),
    }
    return {"implication_premises": premises, "premise_result_records": result_records, "claims": claims}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("implication_premises", "premise_result_records", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {"premises": claims["implication_premises"], "closed": claims["effective_closed_premises"],
            "open": claims["open_premises"], "ready": claims["final_implication_contract_ready"]}


def build_certificate(registry_certificate: dict[str, Any], schedule_certificate: dict[str, Any],
                      edgewise_certificate: dict[str, Any], premises: list[dict[str, Any]]) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "obligation_artifact_registry_certificate": registry_certificate,
        "obligation_blocker_schedule_certificate": schedule_certificate,
        "edgewise_lexicographic_support_certificate": edgewise_certificate,
        "implication_premises": premises,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_final_implication_premise_contract.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
