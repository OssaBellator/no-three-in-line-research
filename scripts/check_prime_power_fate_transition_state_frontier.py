#!/usr/bin/env python3
"""Validate and synchronize the exact T07 fate/transition/state semantic proof bank.

T03 supplies literal owner/fate witnesses, labelled vectors and transitions. T04 identifies every
block/interface assembly unit using each slot. This checker gives each literal semantic subject one
canonical proof claim, checks exact coverage and acyclic claim support, seals one slot proof artifact
with exact T03/T04 ancestry, and binds the aggregate banks to FATE_TRANSITION_STATE_SEMANTICS and
T07_FATE_TRANSITION_STATE.

The checker validates documentary identity, coverage and support only. It does not decide whether a
semantic statement is mathematically true and permanently reports ``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import copy
import heapq
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_all_n_implication_closure as closure
import check_prime_power_atomic_frontier_execution as atomic
import check_prime_power_atomic_target_artifact_registry as target_artifacts
import check_prime_power_block_interface_population_frontier as t04_frontier
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_obligation_artifact_registry as obligation_artifacts


class FateTransitionStateFrontierError(ValueError):
    """Raised when the exact T07 semantic proof bank is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise FateTransitionStateFrontierError(message)


REQUIRED_SLOT_ARTIFACT_KIND = "slot-fate-transition-state-proof"
STATE_OBLIGATION_LOCATOR = (
    "fate-transition-state-frontier://"
    "FATE_TRANSITION_STATE_SEMANTICS/state-semantics-proof"
)
TRANSITION_OBLIGATION_LOCATOR = (
    "fate-transition-state-frontier://"
    "FATE_TRANSITION_STATE_SEMANTICS/transition-proof"
)
T07_TARGET_LOCATOR = "fate-transition-state-frontier://T07_FATE_TRANSITION_STATE"


def canonical_json_value(value: Any, path: str) -> Any:
    require(
        value is None or isinstance(value, (bool, int, str, list, dict)),
        f"{path}: non-JSON value",
    )
    if isinstance(value, list):
        return [canonical_json_value(item, f"{path}[]") for item in value]
    if isinstance(value, dict):
        require(all(isinstance(key, str) for key in value), f"{path}: non-string key")
        return {key: canonical_json_value(value[key], f"{path}.{key}") for key in value}
    return value


def subject_records(
    *,
    slot_id: str,
    claim_kind: str,
    values: list[Any],
) -> list[dict[str, Any]]:
    output = []
    for index, value in enumerate(values):
        record = {
            "slot_id": slot_id,
            "claim_kind": claim_kind,
            "subject_index": index,
            "subject_value": canonical_json_value(
                value, f"{claim_kind}_subjects[{index}]"
            ),
        }
        record["subject_sha256"] = catalogue.canonical_digest(record)
        output.append(record)
    return output


def expected_subjects(slot: dict[str, Any], payload: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    data = payload["population_data"]
    parent_subject = {
        "state_role": "parent-slot-state",
        "parent_state_id": slot["parent_state_id"],
        "host_id": payload["host_id"],
        "fibre_id": payload["fibre_id"],
        "state_labels": copy.deepcopy(slot["state_labels"]),
    }
    state_values = [parent_subject] + copy.deepcopy(data["labelled_vectors"])
    return {
        "fate": subject_records(
            slot_id=slot["slot_id"],
            claim_kind="fate",
            values=copy.deepcopy(data["owner_fate_witnesses"]),
        ),
        "state": subject_records(
            slot_id=slot["slot_id"],
            claim_kind="state",
            values=state_values,
        ),
        "transition": subject_records(
            slot_id=slot["slot_id"],
            claim_kind="transition",
            values=copy.deepcopy(data["transitions"]),
        ),
    }


def claim_id(subject: dict[str, Any]) -> str:
    return (
        f"{subject['claim_kind']}::{subject['slot_id']}::"
        f"{subject['subject_index']:05d}::{subject['subject_sha256'][:16]}"
    )


def exact_claim(
    raw: dict[str, Any],
    *,
    subject: dict[str, Any],
    path: str,
) -> dict[str, Any]:
    expected_id = claim_id(subject)
    require(raw.get("claim_id") == expected_id, f"{path}.claim_id: mismatch")
    require(raw.get("claim_kind") == subject["claim_kind"], f"{path}.claim_kind: mismatch")
    require(
        raw.get("subject_sha256") == subject["subject_sha256"],
        f"{path}.subject_sha256: mismatch",
    )
    statement = raw.get("statement")
    evidence = raw.get("evidence")
    support = raw.get("support_claim_ids")
    require(isinstance(statement, str) and statement, f"{path}.statement: required")
    require(isinstance(evidence, str) and evidence, f"{path}.evidence: required")
    require(isinstance(support, list), f"{path}.support_claim_ids: expected list")
    require(all(isinstance(value, str) and value for value in support),
            f"{path}.support_claim_ids: bad value")
    require(support == sorted(support), f"{path}.support_claim_ids: sorted order required")
    require(len(support) == len(set(support)), f"{path}.support_claim_ids: duplicates")
    require(expected_id not in support, f"{path}: claim cannot support itself")
    output = {
        "claim_id": expected_id,
        "claim_kind": subject["claim_kind"],
        "subject_sha256": subject["subject_sha256"],
        "statement": statement,
        "support_claim_ids": list(support),
        "evidence": evidence,
    }
    output["semantic_claim_sha256"] = catalogue.canonical_digest(output)
    return output


def topological_claim_order(claims: list[dict[str, Any]], path: str) -> tuple[list[str], list[list[str]]]:
    claim_by_id = {claim["claim_id"]: claim for claim in claims}
    require(len(claim_by_id) == len(claims), f"{path}: duplicate claim_id")
    indegree = {claim_id: 0 for claim_id in claim_by_id}
    dependents: dict[str, list[str]] = {claim_id: [] for claim_id in claim_by_id}
    edges: list[list[str]] = []
    for claim in claims:
        claim_id_value = claim["claim_id"]
        for support_id in claim["support_claim_ids"]:
            require(support_id in claim_by_id, f"{path}: unknown support claim {support_id}")
            indegree[claim_id_value] += 1
            dependents[support_id].append(claim_id_value)
            edges.append([support_id, claim_id_value])
    queue = [claim_id_value for claim_id_value, degree in indegree.items() if degree == 0]
    heapq.heapify(queue)
    order: list[str] = []
    while queue:
        claim_id_value = heapq.heappop(queue)
        order.append(claim_id_value)
        for dependent in sorted(dependents[claim_id_value]):
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                heapq.heappush(queue, dependent)
    require(len(order) == len(claims), f"{path}: semantic claim support cycle")
    return order, sorted(edges)


def exact_semantic_certificate(
    raw: dict[str, Any],
    *,
    slot: dict[str, Any],
    payload: dict[str, Any],
    path: str,
) -> dict[str, Any]:
    slot_id = slot["slot_id"]
    require(raw.get("slot_id") == slot_id, f"{path}.slot_id: mismatch")
    require(
        raw.get("slot_population_payload_sha256")
        == payload["slot_population_payload_sha256"],
        f"{path}.slot_population_payload_sha256: mismatch",
    )
    subjects = expected_subjects(slot, payload)
    claims_by_kind: dict[str, list[dict[str, Any]]] = {}
    all_claims: list[dict[str, Any]] = []
    for kind, field in (
        ("fate", "fate_claims"),
        ("state", "state_claims"),
        ("transition", "transition_claims"),
    ):
        raw_claims = raw.get(field)
        require(isinstance(raw_claims, list), f"{path}.{field}: expected list")
        require(
            len(raw_claims) == len(subjects[kind]),
            f"{path}.{field}: exact subject cardinality required",
        )
        claims = [
            exact_claim(
                claim,
                subject=subject,
                path=f"{path}.{field}[{index}]",
            )
            for index, (claim, subject) in enumerate(zip(raw_claims, subjects[kind]))
        ]
        require(raw_claims == claims, f"{path}.{field}: canonical claims/digests required")
        claims_by_kind[kind] = claims
        all_claims.extend(claims)

    order, edges = topological_claim_order(all_claims, path)
    require(raw.get("claim_topological_order") == order,
            f"{path}.claim_topological_order: incorrect")
    require(raw.get("claim_support_edges") == edges,
            f"{path}.claim_support_edges: incorrect")
    output = {
        "slot_id": slot_id,
        "slot_population_payload_sha256": payload["slot_population_payload_sha256"],
        "fate_subjects": subjects["fate"],
        "state_subjects": subjects["state"],
        "transition_subjects": subjects["transition"],
        "fate_claims": claims_by_kind["fate"],
        "state_claims": claims_by_kind["state"],
        "transition_claims": claims_by_kind["transition"],
        "claim_topological_order": order,
        "claim_support_edges": edges,
    }
    output["slot_fate_transition_state_semantics_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_status_record(
    record: dict[str, Any],
    *,
    slot_id: str,
    payload_sha256: str | None,
    path: str,
) -> dict[str, Any]:
    record_id = f"semantics::{slot_id}"
    require(record.get("record_id") == record_id, f"{path}.record_id: mismatch")
    require(record.get("slot_id") == slot_id, f"{path}.slot_id: mismatch")
    require(
        record.get("slot_population_payload_sha256") == payload_sha256,
        f"{path}.slot_population_payload_sha256: mismatch",
    )
    status = record.get("status")
    locator = record.get("verification_locator")
    digest = record.get("verification_digest")
    note = record.get("note")
    require(status in {"open", "proved"}, f"{path}.status: expected open/proved")
    require(isinstance(note, str) and note, f"{path}.note: required")
    if status == "open":
        require(locator is None, f"{path}.verification_locator: open requires null")
        require(digest is None, f"{path}.verification_digest: open requires null")
    else:
        require(
            locator == f"fate-transition-state-slot-registry://{slot_id}",
            f"{path}.verification_locator: canonical slot URI required",
        )
        require(isinstance(digest, str) and digest, f"{path}.verification_digest: required")
        require(payload_sha256 is not None, f"{path}: proved semantics requires T03 payload")
    output = {
        "record_id": record_id,
        "slot_id": slot_id,
        "slot_population_payload_sha256": payload_sha256,
        "status": status,
        "verification_locator": locator,
        "verification_digest": digest,
        "note": note,
    }
    output["fate_transition_state_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_slot_artifact(
    raw: dict[str, Any],
    *,
    slot_id: str,
    payload_sha256: str,
    semantics_sha256: str,
    expected_t03_support: list[str],
    expected_t04_support: list[str],
    path: str,
) -> dict[str, Any]:
    values = {
        key: raw.get(key)
        for key in (
            "artifact_id",
            "artifact_kind",
            "proof_locator",
            "proof_digest",
            "proof_statement",
            "evidence",
        )
    }
    for name, value in values.items():
        require(isinstance(value, str) and value, f"{path}.{name}: required")
    require(raw.get("slot_id") == slot_id, f"{path}.slot_id: mismatch")
    require(
        values["artifact_kind"] == REQUIRED_SLOT_ARTIFACT_KIND,
        f"{path}.artifact_kind: wrong kind",
    )
    require(
        raw.get("slot_population_payload_sha256") == payload_sha256,
        f"{path}.slot_population_payload_sha256: mismatch",
    )
    require(
        raw.get("slot_fate_transition_state_semantics_sha256") == semantics_sha256,
        f"{path}.slot_fate_transition_state_semantics_sha256: mismatch",
    )
    t03_support = raw.get("support_t03_population_artifact_ids")
    t04_support = raw.get("support_t04_population_artifact_ids")
    require(t03_support == expected_t03_support,
            f"{path}.support_t03_population_artifact_ids: exact support required")
    require(t04_support == expected_t04_support,
            f"{path}.support_t04_population_artifact_ids: exact support required")
    for name, support in (
        ("support_t03_population_artifact_ids", t03_support),
        ("support_t04_population_artifact_ids", t04_support),
    ):
        require(isinstance(support, list), f"{path}.{name}: list required")
        require(support == sorted(support), f"{path}.{name}: sorted")
        require(len(support) == len(set(support)), f"{path}.{name}: duplicates")
        require(values["artifact_id"] not in support, f"{path}: self support")
    output = {
        "slot_id": slot_id,
        "artifact_id": values["artifact_id"],
        "artifact_kind": values["artifact_kind"],
        "slot_population_payload_sha256": payload_sha256,
        "slot_fate_transition_state_semantics_sha256": semantics_sha256,
        "proof_locator": values["proof_locator"],
        "proof_digest": values["proof_digest"],
        "proof_statement": values["proof_statement"],
        "support_t03_population_artifact_ids": list(t03_support),
        "support_t04_population_artifact_ids": list(t04_support),
        "evidence": values["evidence"],
    }
    output["fate_transition_state_artifact_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    t04_certificate = certificate.get("block_interface_population_frontier_certificate")
    raw_records = certificate.get("slot_fate_transition_state_records")
    raw_semantics = certificate.get("slot_fate_transition_state_semantic_certificates")
    raw_artifacts = certificate.get("slot_fate_transition_state_artifacts")
    require(isinstance(t04_certificate, dict),
            "block_interface_population_frontier_certificate: expected object")
    require(isinstance(raw_records, list),
            "slot_fate_transition_state_records: expected list")
    require(isinstance(raw_semantics, list),
            "slot_fate_transition_state_semantic_certificates: expected list")
    require(isinstance(raw_artifacts, list),
            "slot_fate_transition_state_artifacts: expected list")

    t04_frontier.validate_certificate(t04_certificate)
    t04_exact = t04_frontier.exact_certificate(t04_certificate)
    t03_certificate = t04_certificate["slot_candidate_population_frontier_certificate"]
    t03_module = __import__("check_prime_power_slot_candidate_population_frontier")
    t03_module.validate_certificate(t03_certificate)
    t03_exact = t03_module.exact_certificate(t03_certificate)
    rule_certificate = t03_certificate["rule_exhaustiveness_frontier_certificate"]
    source_frontier = rule_certificate["source_truth_frontier_execution_certificate"]
    source_registry = source_frontier["source_statement_truth_registry_certificate"]
    obligation_certificate = source_registry["obligation_artifact_registry_certificate"]
    obligation_artifacts.validate_certificate(obligation_certificate)
    obligation_exact = obligation_artifacts.exact_certificate(obligation_certificate)
    closure_certificate = obligation_certificate["all_n_implication_closure_certificate"]
    closure_exact = closure.exact_certificate(closure_certificate)

    target_registry = t04_certificate["atomic_target_artifact_registry_certificate"]
    target_artifacts.validate_certificate(target_registry)
    target_exact = target_artifacts.exact_certificate(target_registry)
    current = target_registry["current_frontier_execution_certificate"]
    atomic_certificate = current["atomic_frontier_execution_certificate"]
    atomic.validate_certificate(atomic_certificate)
    atomic_exact = atomic.exact_certificate(atomic_certificate)

    slots = rule_certificate["source_truth_frontier_execution_certificate"][
        "source_statement_truth_registry_certificate"
    ]["rule_source_provenance_certificate"]["clause_manifest"][
        "expected_slot_registry"
    ]["slots"]
    payload_by_slot = {
        payload["slot_id"]: payload for payload in t03_exact["slot_population_payloads"]
    }
    t03_artifact_by_slot = {
        artifact["slot_id"]: artifact["artifact_id"]
        for artifact in t03_exact["slot_population_artifacts"]
    }
    t04_artifact_by_unit = {
        artifact["unit_id"]: artifact["artifact_id"]
        for artifact in t04_exact["block_interface_population_artifacts"]
    }
    units_by_slot: dict[str, list[str]] = {slot["slot_id"]: [] for slot in slots}
    for unit in t04_exact["expected_block_interface_population_units"]:
        for binding in unit["parent_bindings"]:
            slot_id = binding["operation_slot_id"]
            require(slot_id in units_by_slot, f"T04 unit uses unknown slot {slot_id}")
            units_by_slot[slot_id].append(unit["unit_id"])
    for slot_id in units_by_slot:
        units_by_slot[slot_id] = sorted(set(units_by_slot[slot_id]))

    require(len(raw_records) == len(slots),
            "slot_fate_transition_state_records: exact slot cardinality required")
    require(
        [record.get("slot_id") for record in raw_records]
        == [slot["slot_id"] for slot in slots],
        "slot_fate_transition_state_records: canonical slot order required",
    )
    records = []
    for index, (raw, slot) in enumerate(zip(raw_records, slots)):
        payload = payload_by_slot.get(slot["slot_id"])
        records.append(
            exact_status_record(
                raw,
                slot_id=slot["slot_id"],
                payload_sha256=(
                    None if payload is None else payload["slot_population_payload_sha256"]
                ),
                path=f"slot_fate_transition_state_records[{index}]",
            )
        )
    require(raw_records == records,
            "slot_fate_transition_state_records: canonical records/digests required")
    record_by_slot = {record["slot_id"]: record for record in records}

    semantics_groups: dict[str, list[dict[str, Any]]] = {
        slot["slot_id"]: [] for slot in slots
    }
    for item in raw_semantics:
        require(isinstance(item, dict),
                "slot_fate_transition_state_semantic_certificates: expected objects")
        slot_id = item.get("slot_id")
        require(slot_id in semantics_groups, f"semantic certificate: unknown slot {slot_id}")
        semantics_groups[slot_id].append(item)
    artifact_groups: dict[str, list[dict[str, Any]]] = {
        slot["slot_id"]: [] for slot in slots
    }
    for item in raw_artifacts:
        require(isinstance(item, dict),
                "slot_fate_transition_state_artifacts: expected objects")
        slot_id = item.get("slot_id")
        require(slot_id in artifact_groups, f"semantic artifact: unknown slot {slot_id}")
        artifact_groups[slot_id].append(item)

    semantic_certificates: list[dict[str, Any]] = []
    artifacts: list[dict[str, Any]] = []
    bundle_records: list[dict[str, Any]] = []
    fate_claims: list[dict[str, Any]] = []
    state_claims: list[dict[str, Any]] = []
    transition_claims: list[dict[str, Any]] = []

    for slot in slots:
        slot_id = slot["slot_id"]
        record = record_by_slot[slot_id]
        semantic_group = semantics_groups[slot_id]
        artifact_group = artifact_groups[slot_id]
        semantic_list: list[dict[str, Any]] = []
        artifact_list: list[dict[str, Any]] = []
        if record["status"] == "open":
            require(not semantic_group,
                    f"slot {slot_id}: open record cannot contain semantic certificate")
            require(not artifact_group,
                    f"slot {slot_id}: open record cannot contain semantic artifact")
        else:
            require(len(semantic_group) == 1,
                    f"slot {slot_id}: exactly one semantic certificate required")
            require(len(artifact_group) == 1,
                    f"slot {slot_id}: exactly one semantic artifact required")
            require(slot_id in payload_by_slot,
                    f"slot {slot_id}: proved semantics requires T03 payload")
            require(slot_id in t03_artifact_by_slot,
                    f"slot {slot_id}: proved semantics requires proved T03 slot")
            payload = payload_by_slot[slot_id]
            semantic = exact_semantic_certificate(
                semantic_group[0],
                slot=slot,
                payload=payload,
                path=f"slot_fate_transition_state_semantic_certificate[{slot_id}]",
            )
            semantic_certificates.append(semantic)
            semantic_list = [semantic]
            fate_claims.extend(semantic["fate_claims"])
            state_claims.extend(semantic["state_claims"])
            transition_claims.extend(semantic["transition_claims"])

            expected_t03_support = [t03_artifact_by_slot[slot_id]]
            expected_t04_support = sorted(
                t04_artifact_by_unit[unit_id]
                for unit_id in units_by_slot[slot_id]
                if unit_id in t04_artifact_by_unit
            )
            require(
                len(expected_t04_support) == len(units_by_slot[slot_id]),
                f"slot {slot_id}: every using T04 unit must be proved",
            )
            artifact = exact_slot_artifact(
                artifact_group[0],
                slot_id=slot_id,
                payload_sha256=payload["slot_population_payload_sha256"],
                semantics_sha256=semantic[
                    "slot_fate_transition_state_semantics_sha256"
                ],
                expected_t03_support=expected_t03_support,
                expected_t04_support=expected_t04_support,
                path=f"slot_fate_transition_state_artifact[{slot_id}]",
            )
            artifacts.append(artifact)
            artifact_list = [artifact]
            proof_bundle = {
                "slot_id": slot_id,
                "slot_population_payload_sha256": payload[
                    "slot_population_payload_sha256"
                ],
                "slot_fate_transition_state_semantics_sha256": semantic[
                    "slot_fate_transition_state_semantics_sha256"
                ],
                "fate_transition_state_artifact_sha256": artifact[
                    "fate_transition_state_artifact_sha256"
                ],
                "support_t03_population_artifact_ids": expected_t03_support,
                "support_t04_population_artifact_ids": expected_t04_support,
            }
            proof_bundle[
                "slot_fate_transition_state_proof_bundle_sha256"
            ] = catalogue.canonical_digest(proof_bundle)
            require(
                record["verification_digest"]
                == proof_bundle["slot_fate_transition_state_proof_bundle_sha256"],
                f"slot {slot_id}: verification digest does not bind proof bundle",
            )

        bundle = {
            "slot_id": slot_id,
            "status": record["status"],
            "semantic_certificates_sha256": catalogue.canonical_digest(semantic_list),
            "artifacts_sha256": catalogue.canonical_digest(artifact_list),
        }
        bundle["slot_fate_transition_state_bundle_sha256"] = catalogue.canonical_digest(bundle)
        bundle_records.append(bundle)

    require(raw_semantics == semantic_certificates,
            "slot_fate_transition_state_semantic_certificates: canonical order/content required")
    require(raw_artifacts == artifacts,
            "slot_fate_transition_state_artifacts: canonical order/content required")
    artifact_ids = [artifact["artifact_id"] for artifact in artifacts]
    require(len(artifact_ids) == len(set(artifact_ids)),
            "slot_fate_transition_state_artifacts: duplicate artifact_id")

    status_counts = Counter(record["status"] for record in records)
    t03_ready = int(t03_exact["claims"]["slot_candidate_population_ready"])
    t04_ready = int(t04_exact["claims"]["t04_block_interface_population_ready"])
    all_slots_proved = int(status_counts["proved"] == len(slots))
    semantics_ready = int(
        t03_ready and t04_ready and all_slots_proved and len(artifacts) == len(slots)
    )

    state_bank = {
        "expected_slot_registry_sha256": t03_exact["claims"]["expected_slot_registry_sha256"],
        "t03_slot_population_payloads_sha256": t03_exact["claims"]["slot_population_payloads_sha256"],
        "t03_slot_population_artifacts_sha256": t03_exact["claims"]["slot_population_artifacts_sha256"],
        "t04_population_payloads_sha256": t04_exact["claims"][
            "block_interface_population_payloads_sha256"
        ],
        "t04_population_artifacts_sha256": t04_exact["claims"][
            "block_interface_population_artifacts_sha256"
        ],
        "slot_semantic_records_sha256": catalogue.canonical_digest(records),
        "slot_semantic_certificates_sha256": catalogue.canonical_digest(semantic_certificates),
        "fate_claims_sha256": catalogue.canonical_digest(fate_claims),
        "state_claims_sha256": catalogue.canonical_digest(state_claims),
        "slot_semantic_artifacts_sha256": catalogue.canonical_digest(artifacts),
        "slot_semantic_bundles_sha256": catalogue.canonical_digest(bundle_records),
    }
    state_bank["state_semantics_proof_bank_sha256"] = catalogue.canonical_digest(state_bank)
    transition_bank = {
        "expected_slot_registry_sha256": t03_exact["claims"]["expected_slot_registry_sha256"],
        "slot_semantic_records_sha256": catalogue.canonical_digest(records),
        "slot_semantic_certificates_sha256": catalogue.canonical_digest(semantic_certificates),
        "transition_claims_sha256": catalogue.canonical_digest(transition_claims),
        "slot_semantic_artifacts_sha256": catalogue.canonical_digest(artifacts),
        "slot_semantic_bundles_sha256": catalogue.canonical_digest(bundle_records),
    }
    transition_bank["transition_proof_bank_sha256"] = catalogue.canonical_digest(
        transition_bank
    )
    combined_bank = {
        "state_semantics_proof_bank_sha256": state_bank[
            "state_semantics_proof_bank_sha256"
        ],
        "transition_proof_bank_sha256": transition_bank[
            "transition_proof_bank_sha256"
        ],
        "slot_semantic_records_sha256": catalogue.canonical_digest(records),
        "slot_semantic_artifacts_sha256": catalogue.canonical_digest(artifacts),
    }
    combined_bank["fate_transition_state_frontier_proof_bank_sha256"] = (
        catalogue.canonical_digest(combined_bank)
    )

    closure_by_id = {
        record["obligation_id"]: record
        for record in closure_exact["obligation_closure_records"]
    }
    fate_closure = closure_by_id["FATE_TRANSITION_STATE_SEMANTICS"]
    require(
        int(fate_closure["closed"]) == semantics_ready,
        "FATE_TRANSITION_STATE_SEMANTICS closure disagrees with exact T07 bank",
    )

    obligation_by_kind = {
        artifact["artifact_kind"]: artifact
        for artifact in obligation_exact["proof_artifacts"]
        if artifact["obligation_id"] == "FATE_TRANSITION_STATE_SEMANTICS"
    }
    population_artifact_ids = sorted(
        artifact["artifact_id"]
        for artifact in obligation_exact["proof_artifacts"]
        if artifact["obligation_id"] == "SLOT_AND_CANDIDATE_POPULATION"
    )
    require(
        len(obligation_by_kind) == (2 if semantics_ready else 0),
        "FATE_TRANSITION_STATE_SEMANTICS artifact presence disagrees with readiness",
    )
    if semantics_ready:
        state_obligation = obligation_by_kind.get("state-semantics-proof")
        transition_obligation = obligation_by_kind.get("transition-proof")
        require(
            state_obligation is not None and transition_obligation is not None,
            "FATE_TRANSITION_STATE_SEMANTICS requires both fixed artifacts",
        )
        require(state_obligation["locator"] == STATE_OBLIGATION_LOCATOR,
                "state-semantics-proof locator does not bind T07 bank")
        require(
            state_obligation["digest"]
            == state_bank["state_semantics_proof_bank_sha256"],
            "state-semantics-proof digest does not bind exact state bank",
        )
        require(transition_obligation["locator"] == TRANSITION_OBLIGATION_LOCATOR,
                "transition-proof locator does not bind T07 bank")
        require(
            transition_obligation["digest"]
            == transition_bank["transition_proof_bank_sha256"],
            "transition-proof digest does not bind exact transition bank",
        )
        require(
            state_obligation["support_artifact_ids"] == population_artifact_ids,
            "state-semantics-proof requires exact population support",
        )
        require(
            transition_obligation["support_artifact_ids"] == population_artifact_ids,
            "transition-proof requires exact population support",
        )

    target_results = {
        record["target_id"]: record for record in atomic_exact["target_result_records"]
    }
    t07_complete = int(
        target_results["T07_FATE_TRANSITION_STATE"]["effective_target_complete"]
    )
    require(
        t07_complete == semantics_ready,
        "T07_FATE_TRANSITION_STATE completion disagrees with exact semantic bank",
    )
    target_artifact_by_id = {
        artifact["target_id"]: artifact
        for artifact in target_exact["atomic_target_artifacts"]
    }
    t07_artifact = target_artifact_by_id.get("T07_FATE_TRANSITION_STATE")
    if semantics_ready:
        require(t07_artifact is not None,
                "completed T07 target missing transition-state-proof artifact")
        require(t07_artifact["artifact_kind"] == "transition-state-proof",
                "T07 target requires transition-state-proof")
        require(t07_artifact["proof_locator"] == T07_TARGET_LOCATOR,
                "T07 target proof locator does not bind T07 frontier")
        require(
            t07_artifact["proof_digest"]
            == combined_bank["fate_transition_state_frontier_proof_bank_sha256"],
            "T07 target proof digest does not bind noncircular T07 bank",
        )
    else:
        require(t07_artifact is None, "open T07 target cannot contain target artifact")

    claims = {
        "expected_slots": len(slots),
        "open_semantic_slots": status_counts["open"],
        "proved_semantic_slots": status_counts["proved"],
        "fate_claims": len(fate_claims),
        "state_claims": len(state_claims),
        "transition_claims": len(transition_claims),
        "semantic_artifacts": len(artifacts),
        "t03_slot_candidate_population_ready": t03_ready,
        "t04_block_interface_population_ready": t04_ready,
        "fate_transition_state_semantics_ready": semantics_ready,
        "exact_literal_semantic_subject_coverage": 1,
        "acyclic_semantic_claim_support": 1,
        "exact_t03_t04_semantic_artifact_support": 1,
        "noncircular_fate_transition_state_bank_binding": 1,
        "state_obligation_synchronized": 1,
        "transition_obligation_synchronized": 1,
        "t07_atomic_target_synchronized": 1,
        "all_n_proved_by_checker": 0,
        "open_slot_ids": [
            record["slot_id"] for record in records if record["status"] == "open"
        ],
        "slot_semantic_records_sha256": catalogue.canonical_digest(records),
        "slot_semantic_certificates_sha256": catalogue.canonical_digest(semantic_certificates),
        "slot_semantic_artifacts_sha256": catalogue.canonical_digest(artifacts),
        "slot_semantic_bundles_sha256": catalogue.canonical_digest(bundle_records),
        "state_semantics_proof_bank_sha256": state_bank[
            "state_semantics_proof_bank_sha256"
        ],
        "transition_proof_bank_sha256": transition_bank[
            "transition_proof_bank_sha256"
        ],
        "fate_transition_state_frontier_proof_bank_sha256": combined_bank[
            "fate_transition_state_frontier_proof_bank_sha256"
        ],
        "obligation_artifact_registry_sha256": obligation_certificate[
            "certificate_sha256"
        ],
        "atomic_target_artifact_registry_sha256": target_registry[
            "certificate_sha256"
        ],
    }
    return {
        "slot_fate_transition_state_records": records,
        "slot_fate_transition_state_semantic_certificates": semantic_certificates,
        "slot_fate_transition_state_artifacts": artifacts,
        "slot_fate_transition_state_bundle_records": bundle_records,
        "state_semantics_proof_bank": state_bank,
        "transition_proof_bank": transition_bank,
        "fate_transition_state_frontier_proof_bank": combined_bank,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in (
        "slot_fate_transition_state_records",
        "slot_fate_transition_state_semantic_certificates",
        "slot_fate_transition_state_artifacts",
        "slot_fate_transition_state_bundle_records",
        "state_semantics_proof_bank",
        "transition_proof_bank",
        "fate_transition_state_frontier_proof_bank",
        "claims",
    ):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {
        key: value for key, value in certificate.items() if key != "certificate_sha256"
    }
    require(
        certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
        "certificate_sha256: incorrect",
    )
    claims = exact["claims"]
    return {
        "slots": claims["expected_slots"],
        "open": claims["open_semantic_slots"],
        "proved": claims["proved_semantic_slots"],
        "claims": (
            claims["fate_claims"]
            + claims["state_claims"]
            + claims["transition_claims"]
        ),
        "ready": claims["fate_transition_state_semantics_ready"],
        "all_n": claims["all_n_proved_by_checker"],
    }


def build_certificate(
    t04_certificate: dict[str, Any],
    records: list[dict[str, Any]],
    semantic_certificates: list[dict[str, Any]],
    artifacts: list[dict[str, Any]],
) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "block_interface_population_frontier_certificate": t04_certificate,
        "slot_fate_transition_state_records": records,
        "slot_fate_transition_state_semantic_certificates": semantic_certificates,
        "slot_fate_transition_state_artifacts": artifacts,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: check_prime_power_fate_transition_state_frontier.py certificate.json"
        )
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
