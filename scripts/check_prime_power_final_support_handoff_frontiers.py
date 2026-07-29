#!/usr/bin/env python3
"""Exact documentary T32--T43 support, handoff, dossier and root frontiers.

This checker composes the canonical T22--T31 premise-frontier certificate with the older typed
obligation, support-DAG, premise, handoff and dossier layers.  It reconstructs exact immediate
atomic-target support for T32--T43, publishes one reviewed completion statement for every proved
target, and binds a noncircular proof-bundle digest into the corresponding atomic target artifact.

The T43 bundle additionally binds the same digest into the three root-obligation artifacts.  Stable
cores exclude those outward locator/digest fields and exclude ancestor certificate digests that
would contain them.  Passing establishes documentary identity and support only and permanently
reports ``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_all_n_implication_closure as closure
import check_prime_power_atomic_frontier_execution as atomic
import check_prime_power_atomic_target_artifact_registry as target_artifacts
import check_prime_power_canonical_raw_host_catalogue as cat
import check_prime_power_final_dossier_integrity as dossier
import check_prime_power_final_induction_handoff as handoff
import check_prime_power_final_premise_frontiers as t31
import check_prime_power_handoff_assertion_artifact_registry as handoff_artifacts
import check_prime_power_obligation_artifact_registry as obligation_artifacts
import check_prime_power_obligation_artifact_support_dag as support_dag
import check_prime_power_premise_artifact_registry as premise_artifacts


class FinalSupportHandoffFrontierError(ValueError):
    """Raised when one of the exact T32--T43 frontiers is inconsistent."""


def req(value: bool, message: str) -> None:
    if not value:
        raise FinalSupportHandoffFrontierError(message)


def text(value: Any, path: str) -> str:
    req(isinstance(value, str) and bool(value), f"{path}: nonempty string required")
    return value


TARGET_IDS = tuple(target_id for target_id in atomic.TARGETS if target_id >= "T32")
req(TARGET_IDS == tuple(f"T{index:02d}_{name}" for index, name in (
    (32, "OBLIGATION_ARTIFACTS"),
    (33, "OBLIGATION_SUPPORT_DAG"),
    (34, "PREMISE_ARTIFACTS"),
    (35, "BASE_HANDOFF"),
    (36, "RECURRENCE_HANDOFF"),
    (37, "INVARIANT_HANDOFF"),
    (38, "TERMINATION_HANDOFF"),
    (39, "EXCEPTIONAL_HANDOFF"),
    (40, "TRANSLATION_HANDOFF"),
    (41, "FINAL_HANDOFF_REVIEW"),
    (42, "FINAL_DOSSIER_AUDIT"),
    (43, "ROOT_IMPLICATION"),
)), "canonical T32--T43 target order changed")

ASSERTION_TARGETS: dict[str, str] = {
    "BASE_DOMAIN_ESTABLISHED": "T35_BASE_HANDOFF",
    "NONBASE_RECURRENCE_COVERS_ALL_CASES": "T36_RECURRENCE_HANDOFF",
    "STATE_AND_RESOURCE_INVARIANTS_PRESERVED": "T37_INVARIANT_HANDOFF",
    "EVERY_RECURRENCE_BRANCH_TERMINATES": "T38_TERMINATION_HANDOFF",
    "EXCEPTIONAL_AND_HARD_CORE_CASES_CLOSED": "T39_EXCEPTIONAL_HANDOFF",
    "QUOTIENT_CONCLUSION_TRANSLATES_TO_D_EQ_2N": "T40_TRANSLATION_HANDOFF",
}
TARGET_ASSERTIONS = {target_id: assertion_id for assertion_id, target_id in ASSERTION_TARGETS.items()}
ROOT_ID = "GLOBAL_QUOTIENT_IMPLIES_ALL_N"
ROOT_TARGET = "T43_ROOT_IMPLICATION"
FRONTIER_PREFIX = "final-support-handoff-frontier://"


def target_artifact_core(record: dict[str, Any]) -> dict[str, Any]:
    """Stable atomic-target fields, excluding the outward proof locator and digest."""
    return {
        "target_id": record["target_id"],
        "artifact_id": record["artifact_id"],
        "artifact_kind": record["artifact_kind"],
        "statement": record["statement"],
        "evidence": record["evidence"],
        "support_target_artifact_ids": list(record["support_target_artifact_ids"]),
        "support_external_artifact_refs": list(record["support_external_artifact_refs"]),
        "support_certificate_refs": list(record["support_certificate_refs"]),
    }


def root_obligation_artifact_core(record: dict[str, Any]) -> dict[str, Any]:
    """Stable T43 obligation-artifact fields, excluding the new outward locator and digest."""
    return {
        "artifact_id": record["artifact_id"],
        "obligation_id": record["obligation_id"],
        "artifact_kind": record["artifact_kind"],
        "statement": record["statement"],
        "support_artifact_ids": list(record["support_artifact_ids"]),
        "evidence": record["evidence"],
    }


def root_obligation_core(record: dict[str, Any]) -> dict[str, Any]:
    """Stable root-obligation fields, excluding its registry locator and bundle digest."""
    return {
        "obligation_id": record["obligation_id"],
        "status": record["status"],
        "dependency_ids": list(record["dependency_ids"]),
        "note": record["note"],
    }


def root_closure_core(record: dict[str, Any]) -> dict[str, Any]:
    """Stable root closure fields, excluding the obligation-record digest that contains outward seals."""
    return {
        "obligation_id": record["obligation_id"],
        "declared_proved": record["declared_proved"],
        "dependencies_closed": record["dependencies_closed"],
        "closed": record["closed"],
        "open_dependency_ids": list(record["open_dependency_ids"]),
    }


def exact_record(raw: dict[str, Any], target_id: str, dependency_support: list[dict[str, Any]],
                 external_support: list[dict[str, Any]], atomic_completion: dict[str, Any],
                 atomic_result: dict[str, Any], path: str) -> dict[str, Any]:
    req(raw.get("target_id") == target_id, f"{path}.target_id: mismatch")
    status = raw.get("status")
    req(status in {"open", "proved"}, f"{path}.status: open/proved required")
    expected_status = atomic_completion["status"]
    req(status == expected_status, f"{path}.status: atomic completion mismatch")
    req(int(status == "proved") == int(atomic_result["effective_target_complete"]),
        f"{path}.status: effective atomic result mismatch")
    dependencies = list(atomic.TARGETS[target_id]["proof_dependency_target_ids"])
    req(raw.get("dependency_target_ids") == dependencies,
        f"{path}.dependency_target_ids: exact list required")
    dependency_sha = cat.canonical_digest(dependency_support)
    external_sha = cat.canonical_digest(external_support)
    req(raw.get("dependency_target_support_records_sha256") == dependency_sha,
        f"{path}: dependency support digest mismatch")
    req(raw.get("external_frontier_support_records_sha256") == external_sha,
        f"{path}: external support digest mismatch")
    locator = raw.get("verification_locator")
    digest = raw.get("verification_digest")
    if status == "open":
        req(locator is None and digest is None, f"{path}: open verification fields must be null")
    else:
        req(locator == f"{FRONTIER_PREFIX}{target_id}", f"{path}: canonical locator required")
        req(isinstance(digest, str) and digest, f"{path}: proved verification digest required")
    core = {
        "target_id": target_id,
        "status": status,
        "dependency_target_ids": dependencies,
        "dependency_target_support_records_sha256": dependency_sha,
        "external_frontier_support_records_sha256": external_sha,
        "verification_locator": locator,
        "note": text(raw.get("note"), f"{path}.note"),
    }
    output = {
        **core,
        "verification_digest": digest,
        "final_support_handoff_frontier_record_core_sha256": cat.canonical_digest(core),
    }
    output["final_support_handoff_frontier_record_sha256"] = cat.canonical_digest(output)
    return output


def exact_semantic(raw: dict[str, Any], target_id: str, path: str) -> dict[str, Any]:
    req(raw.get("target_id") == target_id, f"{path}.target_id: mismatch")
    output = {
        "target_id": target_id,
        "artifact_kind": atomic.TARGETS[target_id]["required_artifact_kind"],
        "completion_statement": text(raw.get("completion_statement"), f"{path}.completion_statement"),
        "support_implication_statement": text(
            raw.get("support_implication_statement"), f"{path}.support_implication_statement"
        ),
        "arbitrary_n_scope_statement": text(
            raw.get("arbitrary_n_scope_statement"), f"{path}.arbitrary_n_scope_statement"
        ),
        "review_boundary": text(raw.get("review_boundary"), f"{path}.review_boundary"),
        "evidence": text(raw.get("evidence"), f"{path}.evidence"),
    }
    output["final_support_handoff_semantic_sha256"] = cat.canonical_digest(output)
    return output


def dependency_support_records(target_id: str, result_by_target: dict[str, dict[str, Any]],
                               completion_by_target: dict[str, dict[str, Any]],
                               artifact_by_target: dict[str, dict[str, Any]],
                               bundle_by_target: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    records = []
    for dependency_id in atomic.TARGETS[target_id]["proof_dependency_target_ids"]:
        result = result_by_target[dependency_id]
        completion = completion_by_target[dependency_id]
        artifact = artifact_by_target.get(dependency_id)
        bundle = bundle_by_target[dependency_id]
        effective = int(result["effective_target_complete"])
        if effective:
            req(artifact is not None, f"dependency {dependency_id}: target artifact missing")
            req(bundle["artifact_ids"] == [artifact["artifact_id"]],
                f"dependency {dependency_id}: target bundle mismatch")
        else:
            req(artifact is None and bundle["artifact_ids"] == [],
                f"dependency {dependency_id}: open target contains artifact")
        record = {
            "target_id": target_id,
            "dependency_target_id": dependency_id,
            "dependency_effective_target_complete": effective,
            "dependency_target_result_sha256": result["target_result_sha256"],
            "dependency_target_completion_sha256": completion["target_completion_sha256"],
            "dependency_target_artifact_id": None if artifact is None else artifact["artifact_id"],
            "dependency_target_artifact_sha256": (
                None if artifact is None else artifact["atomic_target_artifact_sha256"]
            ),
            "dependency_target_artifact_bundle_sha256": bundle[
                "atomic_target_artifact_bundle_sha256"
            ],
            "dependency_proof_locator": None if artifact is None else artifact["proof_locator"],
            "dependency_proof_digest": None if artifact is None else artifact["proof_digest"],
        }
        record["final_support_handoff_dependency_sha256"] = cat.canonical_digest(record)
        records.append(record)
    return records


def t32_support(closurex: dict[str, Any], obligationx: dict[str, Any],
                result_by_target: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    obligation_by_id = {record["obligation_id"]: record for record in closurex["proof_obligations"]}
    closure_by_id = {
        record["obligation_id"]: record for record in closurex["obligation_closure_records"]
    }
    artifact_by_id = {record["artifact_id"]: record for record in obligationx["proof_artifacts"]}
    bundle_by_id = {
        record["obligation_id"]: record for record in obligationx["artifact_bundle_records"]
    }
    records = []
    for dependency_target_id in atomic.TARGETS["T32_OBLIGATION_ARTIFACTS"][
        "proof_dependency_target_ids"
    ]:
        obligation_ids = list(atomic.TARGETS[dependency_target_id]["obligation_ids"])
        req(len(obligation_ids) == 1, f"{dependency_target_id}: exactly one obligation required")
        obligation_id = obligation_ids[0]
        obligation = obligation_by_id[obligation_id]
        closure_record = closure_by_id[obligation_id]
        bundle = bundle_by_id[obligation_id]
        artifacts = [artifact_by_id[artifact_id] for artifact_id in bundle["artifact_ids"]]
        target_complete = int(result_by_target[dependency_target_id]["effective_target_complete"])
        req(target_complete == int(closure_record["closed"]),
            f"{dependency_target_id}: target/obligation closure mismatch")
        record = {
            "target_id": "T32_OBLIGATION_ARTIFACTS",
            "source_target_id": dependency_target_id,
            "obligation_id": obligation_id,
            "obligation_status": obligation["status"],
            "obligation_closed": int(closure_record["closed"]),
            "obligation_record_sha256": obligation["obligation_record_sha256"],
            "obligation_closure_sha256": closure_record["obligation_closure_sha256"],
            "required_artifact_kinds": list(bundle["required_artifact_kinds"]),
            "artifact_ids": list(bundle["artifact_ids"]),
            "artifact_record_sha256s": [artifact["artifact_record_sha256"] for artifact in artifacts],
            "artifact_bundle_sha256": bundle["artifact_bundle_sha256"],
        }
        record["typed_obligation_frontier_support_sha256"] = cat.canonical_digest(record)
        records.append(record)
    return records


def t33_support(supportx: dict[str, Any]) -> list[dict[str, Any]]:
    claims = supportx["claims"]
    record = {
        "target_id": "T33_OBLIGATION_SUPPORT_DAG",
        "proof_artifacts": claims["proof_artifacts"],
        "artifact_support_edges": claims["artifact_support_edges"],
        "artifact_support_roots": claims["artifact_support_roots"],
        "maximum_artifact_support_depth": claims["maximum_artifact_support_depth"],
        "artifact_support_acyclic": claims["artifact_support_acyclic"],
        "artifact_support_dependency_aligned": claims["artifact_support_dependency_aligned"],
        "exact_dependency_artifact_support_coverage": claims[
            "exact_dependency_artifact_support_coverage"
        ],
        "artifact_support_edges_sha256": claims["artifact_support_edges_sha256"],
        "artifact_support_records_sha256": claims["artifact_support_records_sha256"],
        "obligation_support_records_sha256": claims["obligation_support_records_sha256"],
    }
    record["obligation_support_dag_frontier_sha256"] = cat.canonical_digest(record)
    return [record]


def t34_support(t31x: dict[str, Any], premisex: dict[str, Any]) -> list[dict[str, Any]]:
    frontier_by_id = {
        record["premise_id"]: record for record in t31x["final_premise_frontier_records"]
    }
    semantic_by_id = {
        record["premise_id"]: record for record in t31x["final_premise_semantic_certificates"]
    }
    bundle_by_id = {
        record["premise_id"]: record for record in t31x["final_premise_proof_bundles"]
    }
    artifact_by_id = {
        record["premise_id"]: record for record in premisex["premise_artifacts"]
    }
    registry_bundle_by_id = {
        record["premise_id"]: record for record in premisex["premise_artifact_bundle_records"]
    }
    records = []
    for premise_id in t31.PREMISE_TARGETS:
        frontier = frontier_by_id[premise_id]
        artifact = artifact_by_id.get(premise_id)
        proof_bundle = bundle_by_id.get(premise_id)
        semantic = semantic_by_id.get(premise_id)
        registry_bundle = registry_bundle_by_id[premise_id]
        ready = int(frontier["status"] == "proved")
        req(ready == int(artifact is not None) == int(proof_bundle is not None) == int(semantic is not None),
            f"premise {premise_id}: T31 typed bank mismatch")
        record = {
            "target_id": "T34_PREMISE_ARTIFACTS",
            "premise_id": premise_id,
            "premise_target_id": t31.PREMISE_TARGETS[premise_id],
            "status": frontier["status"],
            "final_premise_frontier_record_sha256": frontier[
                "final_premise_frontier_record_sha256"
            ],
            "final_premise_semantic_sha256": (
                None if semantic is None else semantic["final_premise_semantic_sha256"]
            ),
            "final_premise_frontier_proof_bundle_sha256": (
                None if proof_bundle is None else proof_bundle[
                    "final_premise_frontier_proof_bundle_sha256"
                ]
            ),
            "premise_artifact_id": None if artifact is None else artifact["artifact_id"],
            "premise_artifact_record_sha256": (
                None if artifact is None else artifact["premise_artifact_record_sha256"]
            ),
            "premise_artifact_bundle_sha256": registry_bundle[
                "premise_artifact_bundle_sha256"
            ],
        }
        record["typed_premise_frontier_support_sha256"] = cat.canonical_digest(record)
        records.append(record)
    return records


def assertion_support(target_id: str, handoffx: dict[str, Any], handoff_artifactx: dict[str, Any],
                      t31x: dict[str, Any]) -> list[dict[str, Any]]:
    assertion_id = TARGET_ASSERTIONS[target_id]
    assertion = next(record for record in handoffx["handoff_assertions"]
                     if record["assertion_id"] == assertion_id)
    result = next(record for record in handoffx["handoff_assertion_result_records"]
                  if record["assertion_id"] == assertion_id)
    artifact = next((record for record in handoff_artifactx["handoff_assertion_artifacts"]
                     if record["assertion_id"] == assertion_id), None)
    artifact_bundle = next(record for record in handoff_artifactx[
        "handoff_assertion_artifact_bundle_records"
    ] if record["assertion_id"] == assertion_id)
    premise_bundle_by_id = {
        record["premise_id"]: record for record in t31x["final_premise_proof_bundles"]
    }
    premise_support = []
    for premise_id in assertion["dependency_premise_ids"]:
        bundle = premise_bundle_by_id.get(premise_id)
        premise_support.append({
            "premise_id": premise_id,
            "premise_target_id": t31.PREMISE_TARGETS[premise_id],
            "final_premise_frontier_proof_bundle_sha256": (
                None if bundle is None else bundle["final_premise_frontier_proof_bundle_sha256"]
            ),
        })
    record = {
        "target_id": target_id,
        "assertion_id": assertion_id,
        "assertion_status": assertion["status"],
        "handoff_assertion_sha256": assertion["handoff_assertion_sha256"],
        "handoff_assertion_result_sha256": result["handoff_assertion_result_sha256"],
        "effective_assertion_closed": result["effective_assertion_closed"],
        "handoff_artifact_id": None if artifact is None else artifact["artifact_id"],
        "handoff_assertion_artifact_sha256": (
            None if artifact is None else artifact["handoff_assertion_artifact_sha256"]
        ),
        "handoff_assertion_artifact_bundle_sha256": artifact_bundle[
            "handoff_assertion_artifact_bundle_sha256"
        ],
        "dependency_premise_frontier_support": premise_support,
    }
    record["handoff_assertion_frontier_support_sha256"] = cat.canonical_digest(record)
    return [record]


def t41_support(handoffx: dict[str, Any], handoff_artifactx: dict[str, Any],
                completed_bundles: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    result_by_id = {
        record["assertion_id"]: record for record in handoffx["handoff_assertion_result_records"]
    }
    artifact_bundle_by_id = {
        record["assertion_id"]: record
        for record in handoff_artifactx["handoff_assertion_artifact_bundle_records"]
    }
    records = []
    for assertion_id, target_id in ASSERTION_TARGETS.items():
        frontier_bundle = completed_bundles.get(target_id)
        record = {
            "target_id": "T41_FINAL_HANDOFF_REVIEW",
            "assertion_id": assertion_id,
            "assertion_target_id": target_id,
            "effective_assertion_closed": result_by_id[assertion_id]["effective_assertion_closed"],
            "handoff_assertion_result_sha256": result_by_id[assertion_id][
                "handoff_assertion_result_sha256"
            ],
            "handoff_assertion_artifact_bundle_sha256": artifact_bundle_by_id[assertion_id][
                "handoff_assertion_artifact_bundle_sha256"
            ],
            "assertion_frontier_proof_bundle_sha256": (
                None if frontier_bundle is None else frontier_bundle[
                    "final_support_handoff_frontier_proof_bundle_sha256"
                ]
            ),
        }
        record["final_handoff_review_support_sha256"] = cat.canonical_digest(record)
        records.append(record)
    return records


def t42_support(dossierx: dict[str, Any], completed_bundles: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    t41_bundle = completed_bundles.get("T41_FINAL_HANDOFF_REVIEW")
    gate = dossierx["final_dossier_gate"]
    blockers = dossierx["final_dossier_blockers"]
    record = {
        "target_id": "T42_FINAL_DOSSIER_AUDIT",
        "integrity_gates": dossierx["claims"]["integrity_gates"],
        "satisfied_integrity_gates": dossierx["claims"]["satisfied_integrity_gates"],
        "final_dossier_integrity_ready": dossierx["claims"]["final_dossier_integrity_ready"],
        "final_dossier_gate_sha256": gate["final_dossier_gate_sha256"],
        "final_dossier_blockers_sha256": blockers["final_dossier_blockers_sha256"],
        "t41_frontier_proof_bundle_sha256": (
            None if t41_bundle is None else t41_bundle[
                "final_support_handoff_frontier_proof_bundle_sha256"
            ]
        ),
    }
    record["final_dossier_audit_frontier_support_sha256"] = cat.canonical_digest(record)
    return [record]


def t43_support(closurex: dict[str, Any], obligationx: dict[str, Any],
                completed_bundles: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    obligation = next(record for record in closurex["proof_obligations"]
                      if record["obligation_id"] == ROOT_ID)
    closure_record = next(record for record in closurex["obligation_closure_records"]
                          if record["obligation_id"] == ROOT_ID)
    artifacts = [record for record in obligationx["proof_artifacts"]
                 if record["obligation_id"] == ROOT_ID]
    t42_bundle = completed_bundles.get("T42_FINAL_DOSSIER_AUDIT")
    record = {
        "target_id": ROOT_TARGET,
        "root_obligation_core_sha256": cat.canonical_digest(root_obligation_core(obligation)),
        "root_closure_core_sha256": cat.canonical_digest(root_closure_core(closure_record)),
        "root_obligation_artifact_core_sha256s": [
            cat.canonical_digest(root_obligation_artifact_core(artifact)) for artifact in artifacts
        ],
        "root_obligation_artifact_ids": [artifact["artifact_id"] for artifact in artifacts],
        "root_obligation_artifact_kinds": [artifact["artifact_kind"] for artifact in artifacts],
        "t42_frontier_proof_bundle_sha256": (
            None if t42_bundle is None else t42_bundle[
                "final_support_handoff_frontier_proof_bundle_sha256"
            ]
        ),
    }
    record["root_implication_frontier_support_sha256"] = cat.canonical_digest(record)
    return [record]


def _exact(certificate: dict[str, Any]) -> dict[str, Any]:
    t31c = certificate.get("final_premise_frontier_certificate")
    raw_records = certificate.get("final_support_handoff_frontier_records")
    raw_semantics = certificate.get("final_support_handoff_semantic_certificates")
    raw_bundles = certificate.get("final_support_handoff_proof_bundles")
    req(isinstance(t31c, dict), "final_premise_frontier_certificate: expected object")
    req(isinstance(raw_records, list), "final_support_handoff_frontier_records: expected list")
    req(isinstance(raw_semantics, list), "final_support_handoff_semantic_certificates: expected list")
    req(isinstance(raw_bundles, list), "final_support_handoff_proof_bundles: expected list")

    t31.validate_certificate(t31c)
    t31x = t31.exact_certificate(t31c)
    t21c = t31c["exceptional_chamber_frontier_certificate"]
    t19c = t21c["global_family_exhaustiveness_frontier_certificate"]
    t18c = t19c["row_theorem_frontier_certificate"]
    t17c = t18c["state_predicate_frontier_certificate"]
    t16c = t17c["global_rank_frontier_certificate"]
    t15c = t16c["interface_exhaustiveness_frontier_certificate"]
    t14c = t15c["component_scale_frontier_certificate"]
    t13c = t14c["state_equivalence_frontier_certificate"]
    t07c = t13c["fate_transition_state_frontier_certificate"]
    t04c = t07c["block_interface_population_frontier_certificate"]
    targetc = t04c["atomic_target_artifact_registry_certificate"]

    with t31.corrected_upstream_roots():
        target_artifacts.validate_certificate(targetc)
        targetx = target_artifacts.exact_certificate(targetc)
        atomc = targetc["current_frontier_execution_certificate"][
            "atomic_frontier_execution_certificate"
        ]
        atomic.validate_certificate(atomc)
        atomx = atomic.exact_certificate(atomc)

    currentc = targetc["current_frontier_execution_certificate"]
    dossierc = atomc["final_dossier_integrity_certificate"]
    handoffc = dossierc["final_induction_handoff_certificate"]
    premisec = handoffc["premise_artifact_registry_certificate"]
    contractc = premisec["final_implication_premise_contract_certificate"]
    obligationc = contractc["obligation_artifact_registry_certificate"]
    closurec = obligationc["all_n_implication_closure_certificate"]
    supportc = handoffc["artifact_support_dag_certificate"]
    handoff_artifactc = currentc["handoff_assertion_artifact_registry_certificate"]

    dossier.validate_certificate(dossierc)
    handoff.validate_certificate(handoffc)
    premise_artifacts.validate_certificate(premisec)
    obligation_artifacts.validate_certificate(obligationc)
    closure.validate_certificate(closurec)
    support_dag.validate_certificate(supportc)
    handoff_artifacts.validate_certificate(handoff_artifactc)

    dossierx = dossier.exact_certificate(dossierc)
    handoffx = handoff.exact_certificate(handoffc)
    premisex = premise_artifacts.exact_certificate(premisec)
    obligationx = obligation_artifacts.exact_certificate(obligationc)
    closurex = closure.exact_certificate(closurec)
    supportx = support_dag.exact_certificate(supportc)
    handoff_artifactx = handoff_artifacts.exact_certificate(handoff_artifactc)

    req([raw.get("target_id") for raw in raw_records] == list(TARGET_IDS),
        "final_support_handoff_frontier_records: exact canonical target order required")
    result_by_target = {record["target_id"]: record for record in atomx["target_result_records"]}
    completion_by_target = {
        record["target_id"]: record for record in atomx["target_completion_records"]
    }
    artifact_by_target = {
        record["target_id"]: record for record in targetx["atomic_target_artifacts"]
    }
    bundle_by_target = {
        record["target_id"]: record
        for record in targetx["atomic_target_artifact_bundle_records"]
    }

    dependency_support_by_target: dict[str, list[dict[str, Any]]] = {}
    external_support_by_target: dict[str, list[dict[str, Any]]] = {}
    records = []
    completed_bundles: dict[str, dict[str, Any]] = {}

    # External support for T41--T43 references earlier frontier bundles, so records and bundles are
    # built in canonical target order.
    semantic_groups = {target_id: [] for target_id in TARGET_IDS}
    for raw in raw_semantics:
        target_id = raw.get("target_id")
        req(target_id in semantic_groups,
            "final_support_handoff_semantic_certificates: unknown target")
        semantic_groups[target_id].append(raw)
    semantics = []
    semantic_by_target: dict[str, dict[str, Any]] = {}

    for index, target_id in enumerate(TARGET_IDS):
        dependency_support = dependency_support_records(
            target_id, result_by_target, completion_by_target, artifact_by_target, bundle_by_target
        )
        if target_id == "T32_OBLIGATION_ARTIFACTS":
            external_support = t32_support(closurex, obligationx, result_by_target)
        elif target_id == "T33_OBLIGATION_SUPPORT_DAG":
            external_support = t33_support(supportx)
        elif target_id == "T34_PREMISE_ARTIFACTS":
            external_support = t34_support(t31x, premisex)
        elif target_id in TARGET_ASSERTIONS:
            external_support = assertion_support(
                target_id, handoffx, handoff_artifactx, t31x
            )
        elif target_id == "T41_FINAL_HANDOFF_REVIEW":
            external_support = t41_support(handoffx, handoff_artifactx, completed_bundles)
        elif target_id == "T42_FINAL_DOSSIER_AUDIT":
            external_support = t42_support(dossierx, completed_bundles)
        else:
            req(target_id == ROOT_TARGET, f"unsupported target {target_id}")
            external_support = t43_support(closurex, obligationx, completed_bundles)
        dependency_support_by_target[target_id] = dependency_support
        external_support_by_target[target_id] = external_support
        record = exact_record(
            raw_records[index], target_id, dependency_support, external_support,
            completion_by_target[target_id], result_by_target[target_id],
            f"final_support_handoff_frontier_records[{index}]",
        )
        if target_id == "T41_FINAL_HANDOFF_REVIEW":
            req(
                int(record["status"] == "proved")
                == int(handoffx["claims"]["final_induction_handoff_ready"]),
                "T41: frontier status disagrees with final induction handoff gate",
            )
        if target_id == "T42_FINAL_DOSSIER_AUDIT":
            req(
                int(record["status"] == "proved")
                == int(dossierx["claims"]["final_dossier_integrity_ready"]),
                "T42: frontier status disagrees with final dossier gate",
            )
        records.append(record)

        group = semantic_groups[target_id]
        if record["status"] == "open":
            req(not group, f"target {target_id}: open target cannot contain semantic certificate")
            continue
        req(len(group) == 1, f"target {target_id}: exactly one semantic certificate required")
        req(all(item["dependency_effective_target_complete"] for item in dependency_support),
            f"target {target_id}: proved before every dependency completed")
        semantic = exact_semantic(group[0], target_id,
                                  f"final_support_handoff_semantic[{target_id}]")
        semantics.append(semantic)
        semantic_by_target[target_id] = semantic

        target_artifact = artifact_by_target.get(target_id)
        req(target_artifact is not None, f"target {target_id}: completed target artifact missing")
        bundle = {
            "target_id": target_id,
            "final_support_handoff_frontier_record_core_sha256": record[
                "final_support_handoff_frontier_record_core_sha256"
            ],
            "final_support_handoff_semantic_sha256": semantic[
                "final_support_handoff_semantic_sha256"
            ],
            "dependency_target_support_records_sha256": cat.canonical_digest(dependency_support),
            "external_frontier_support_records_sha256": cat.canonical_digest(external_support),
            "atomic_target_artifact_core_sha256": cat.canonical_digest(
                target_artifact_core(target_artifact)
            ),
        }
        bundle["final_support_handoff_frontier_proof_bundle_sha256"] = cat.canonical_digest(bundle)
        digest = bundle["final_support_handoff_frontier_proof_bundle_sha256"]
        req(record["verification_digest"] == digest,
            f"target {target_id}: frontier verification digest mismatch")
        req(target_artifact["proof_locator"] == f"{FRONTIER_PREFIX}{target_id}"
            and target_artifact["proof_digest"] == digest,
            f"target {target_id}: atomic target artifact does not bind frontier bundle")

        if target_id == ROOT_TARGET:
            root_artifacts = [artifact for artifact in obligationx["proof_artifacts"]
                              if artifact["obligation_id"] == ROOT_ID]
            required_kinds = list(obligation_artifacts.REQUIRED_ARTIFACT_KINDS[ROOT_ID])
            req([artifact["artifact_kind"] for artifact in root_artifacts] == required_kinds,
                "T43: exact root obligation artifact kinds required")
            for artifact in root_artifacts:
                req(
                    artifact["locator"] == f"{FRONTIER_PREFIX}{ROOT_TARGET}/{artifact['artifact_id']}"
                    and artifact["digest"] == digest,
                    f"T43 root artifact {artifact['artifact_id']}: frontier binding mismatch",
                )
        completed_bundles[target_id] = bundle

    req(raw_records == records, "final_support_handoff_frontier_records: noncanonical records")
    req(raw_semantics == semantics,
        "final_support_handoff_semantic_certificates: noncanonical records")
    bundles = [completed_bundles[target_id] for target_id in TARGET_IDS
               if target_id in completed_bundles]
    req(raw_bundles == [] or raw_bundles == bundles,
        "final_support_handoff_proof_bundles: noncanonical records")

    root_obligation = next(record for record in closurex["proof_obligations"]
                           if record["obligation_id"] == ROOT_ID)
    root_closure = next(record for record in closurex["obligation_closure_records"]
                        if record["obligation_id"] == ROOT_ID)
    root_artifacts = [record for record in obligationx["proof_artifacts"]
                      if record["obligation_id"] == ROOT_ID]
    root_ready = int(
        root_obligation["status"] == "proved"
        and root_closure["closed"]
        and len(root_artifacts) == len(obligation_artifacts.REQUIRED_ARTIFACT_KINDS[ROOT_ID])
    )
    req(root_ready == int(result_by_target[ROOT_TARGET]["effective_target_complete"]),
        "T43: root obligation and target completion mismatch")

    counts = Counter(record["status"] for record in records)
    all_ready = int(counts["proved"] == len(TARGET_IDS))
    proof_bank = {
        "t22_t31_final_premise_frontiers_proof_bank_sha256": t31x[
            "claims"
        ]["final_premise_frontiers_proof_bank_sha256"],
        "final_support_handoff_dependency_records_sha256": cat.canonical_digest([
            item for target_id in TARGET_IDS for item in dependency_support_by_target[target_id]
        ]),
        "final_support_handoff_external_records_sha256": cat.canonical_digest([
            item for target_id in TARGET_IDS for item in external_support_by_target[target_id]
        ]),
        "final_support_handoff_frontier_records_sha256": cat.canonical_digest(records),
        "final_support_handoff_semantic_certificates_sha256": cat.canonical_digest(semantics),
        "final_support_handoff_proof_bundles_sha256": cat.canonical_digest(bundles),
    }
    proof_bank["final_support_handoff_frontiers_proof_bank_sha256"] = cat.canonical_digest(
        proof_bank
    )

    claims = {
        "final_support_handoff_targets": len(TARGET_IDS),
        "open_final_support_handoff_targets": counts["open"],
        "proved_final_support_handoff_targets": counts["proved"],
        "t32_t43_final_support_handoff_frontiers_ready": all_ready,
        "exact_immediate_target_dependency_census": 1,
        "exact_t32_obligation_artifact_bank": 1,
        "exact_t33_obligation_support_dag_binding": 1,
        "exact_t34_final_premise_artifact_binding": 1,
        "exact_t35_t40_handoff_assertion_binding": 1,
        "exact_t41_final_handoff_review_binding": 1,
        "exact_t42_final_dossier_audit_binding": 1,
        "exact_t43_root_obligation_binding": 1,
        "noncircular_t32_t43_frontier_bundle_binding": 1,
        "all_n_proved_by_checker": 0,
        "open_target_ids": [record["target_id"] for record in records if record["status"] == "open"],
        "final_premise_frontier_sha256": t31c["certificate_sha256"],
        "atomic_target_artifact_registry_sha256": targetc["certificate_sha256"],
        "obligation_artifact_registry_sha256": obligationc["certificate_sha256"],
        "obligation_artifact_support_dag_sha256": supportc["certificate_sha256"],
        "premise_artifact_registry_sha256": premisec["certificate_sha256"],
        "handoff_assertion_artifact_registry_sha256": handoff_artifactc["certificate_sha256"],
        "final_induction_handoff_sha256": handoffc["certificate_sha256"],
        "final_dossier_integrity_sha256": dossierc["certificate_sha256"],
        "final_support_handoff_frontiers_proof_bank_sha256": proof_bank[
            "final_support_handoff_frontiers_proof_bank_sha256"
        ],
    }
    return {
        "final_support_handoff_dependency_records": [
            item for target_id in TARGET_IDS for item in dependency_support_by_target[target_id]
        ],
        "final_support_handoff_external_records": [
            item for target_id in TARGET_IDS for item in external_support_by_target[target_id]
        ],
        "final_support_handoff_frontier_records": records,
        "final_support_handoff_semantic_certificates": semantics,
        "final_support_handoff_proof_bundles": bundles,
        "final_support_handoff_frontiers_proof_bank": proof_bank,
        "claims": claims,
    }


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    return _exact(certificate)


def validate_certificate(certificate: Any) -> dict[str, Any]:
    req(isinstance(certificate, dict) and certificate.get("version") == 1,
        "version 1 certificate required")
    exact = exact_certificate(certificate)
    for key, value in exact.items():
        req(certificate.get(key) == value, f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    req(certificate.get("certificate_sha256") == cat.canonical_digest(payload),
        "certificate digest incorrect")
    claims = exact["claims"]
    return {
        "targets": claims["final_support_handoff_targets"],
        "proved": claims["proved_final_support_handoff_targets"],
        "open": claims["open_final_support_handoff_targets"],
        "ready": claims["t32_t43_final_support_handoff_frontiers_ready"],
        "all_n": 0,
    }


def build_certificate(t31_certificate: dict[str, Any], records: list[dict[str, Any]],
                      semantics: list[dict[str, Any]]) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "final_premise_frontier_certificate": t31_certificate,
        "final_support_handoff_frontier_records": records,
        "final_support_handoff_semantic_certificates": semantics,
        "final_support_handoff_proof_bundles": [],
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = cat.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: check_prime_power_final_support_handoff_frontiers.py certificate.json"
        )
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
