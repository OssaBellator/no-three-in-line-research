#!/usr/bin/env python3
"""Validate and synchronize the exact T06 candidate-minimization policy bank.

T05 proves finite geometry/selector records and T07 supplies fate/transition/state semantic claims.
This checker gives every expected slot one externally proved minimum labelled-row score, reconstructs
the complete candidate set for every local parent from the independent operation-slot registry,
selects the deterministic winner by ``(minimum score, slot ID)``, and requires every T02 global-parent
application to use that winner.

The older common-weight candidate-policy checker depends on recurrent-block common weights and is
therefore downstream of T06 in the fixed proof DAG. It is not used here. This checker validates exact
documentary identity, minimization arithmetic, support and digest binding only; it does not prove the
external score statements true and permanently reports ``all_n_proved_by_checker = 0``.
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
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_fate_transition_state_frontier as t07_frontier
import check_prime_power_geometry_selector_frontier_v2 as t05_frontier
import check_prime_power_obligation_artifact_registry as obligation_artifacts
import check_prime_power_rule_exhaustiveness_frontier as rule_frontier


class CandidatePolicyFrontierError(ValueError):
    """Raised when the exact T06 candidate-policy bank is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CandidatePolicyFrontierError(message)


SCORE_ARTIFACT_KIND = "candidate-score-proof"
PARENT_ARTIFACT_KIND = "parent-candidate-policy-proof"
APPLICATION_ARTIFACT_KIND = "candidate-policy-application-proof"
OBLIGATION_LOCATOR = "candidate-policy-frontier://CANDIDATE_POLICY_CORRECT"
T06_TARGET_LOCATOR = "candidate-policy-frontier://T06_CANDIDATE_POLICY"


def exact_score_record(
    raw: dict[str, Any],
    *,
    slot: dict[str, Any],
    payload: dict[str, Any] | None,
    selector_summary: dict[str, Any] | None,
    semantic_certificate: dict[str, Any] | None,
    path: str,
) -> dict[str, Any]:
    slot_id = slot["slot_id"]
    record_id = f"score::{slot_id}"
    require(raw.get("record_id") == record_id, f"{path}.record_id: mismatch")
    require(raw.get("slot_id") == slot_id, f"{path}.slot_id: mismatch")
    require(
        raw.get("parent_state_id") == slot["parent_state_id"],
        f"{path}.parent_state_id: mismatch",
    )
    payload_sha = None if payload is None else payload["slot_population_payload_sha256"]
    selector_sha = (
        None if selector_summary is None
        else selector_summary["slot_selector_bank_record_sha256"]
    )
    semantic_sha = (
        None if semantic_certificate is None
        else semantic_certificate["slot_fate_transition_state_semantics_sha256"]
    )
    require(raw.get("slot_population_payload_sha256") == payload_sha,
            f"{path}.slot_population_payload_sha256: mismatch")
    require(raw.get("slot_selector_summary_sha256") == selector_sha,
            f"{path}.slot_selector_summary_sha256: mismatch")
    require(raw.get("slot_semantic_certificate_sha256") == semantic_sha,
            f"{path}.slot_semantic_certificate_sha256: mismatch")
    status = raw.get("status")
    score = raw.get("minimum_labelled_row_load")
    locator = raw.get("verification_locator")
    digest = raw.get("verification_digest")
    score_statement = raw.get("score_statement")
    evidence = raw.get("evidence")
    require(status in {"open", "proved"}, f"{path}.status: expected open/proved")
    if status == "open":
        require(score is None, f"{path}.minimum_labelled_row_load: open requires null")
        require(locator is None, f"{path}.verification_locator: open requires null")
        require(digest is None, f"{path}.verification_digest: open requires null")
        require(score_statement is None, f"{path}.score_statement: open requires null")
        require(evidence is None, f"{path}.evidence: open requires null")
    else:
        require(type(score) is int, f"{path}.minimum_labelled_row_load: integer required")
        require(
            locator == f"candidate-policy-score-registry://{slot_id}",
            f"{path}.verification_locator: canonical score URI required",
        )
        require(isinstance(digest, str) and digest, f"{path}.verification_digest: required")
        require(isinstance(score_statement, str) and score_statement,
                f"{path}.score_statement: required")
        require(isinstance(evidence, str) and evidence, f"{path}.evidence: required")
        require(payload_sha is not None and selector_sha is not None and semantic_sha is not None,
                f"{path}: proved score requires T03, T05 and T07 data")
    row_loads_sha = (
        None if payload is None
        else catalogue.canonical_digest(payload["population_data"]["row_loads"])
    )
    require(raw.get("row_loads_sha256") == row_loads_sha,
            f"{path}.row_loads_sha256: mismatch")
    output = {
        "record_id": record_id,
        "slot_id": slot_id,
        "parent_state_id": slot["parent_state_id"],
        "slot_population_payload_sha256": payload_sha,
        "row_loads_sha256": row_loads_sha,
        "slot_selector_summary_sha256": selector_sha,
        "slot_semantic_certificate_sha256": semantic_sha,
        "status": status,
        "minimum_labelled_row_load": score,
        "verification_locator": locator,
        "verification_digest": digest,
        "score_statement": score_statement,
        "evidence": evidence,
    }
    output["candidate_score_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_score_artifact(
    raw: dict[str, Any],
    *,
    score_record: dict[str, Any],
    expected_t05_support: list[str],
    expected_t07_support: list[str],
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
    require(raw.get("slot_id") == score_record["slot_id"], f"{path}.slot_id: mismatch")
    require(values["artifact_kind"] == SCORE_ARTIFACT_KIND,
            f"{path}.artifact_kind: wrong kind")
    require(
        raw.get("candidate_score_record_sha256")
        == score_record["candidate_score_record_sha256"],
        f"{path}.candidate_score_record_sha256: mismatch",
    )
    t05_support = raw.get("support_t05_geometry_artifact_ids")
    t07_support = raw.get("support_t07_semantic_artifact_ids")
    require(t05_support == expected_t05_support,
            f"{path}.support_t05_geometry_artifact_ids: exact support required")
    require(t07_support == expected_t07_support,
            f"{path}.support_t07_semantic_artifact_ids: exact support required")
    for name, support in (
        ("support_t05_geometry_artifact_ids", t05_support),
        ("support_t07_semantic_artifact_ids", t07_support),
    ):
        require(isinstance(support, list), f"{path}.{name}: list required")
        require(support == sorted(support), f"{path}.{name}: sorted")
        require(len(support) == len(set(support)), f"{path}.{name}: duplicates")
        require(values["artifact_id"] not in support, f"{path}: self support")
    output = {
        "slot_id": score_record["slot_id"],
        "artifact_id": values["artifact_id"],
        "artifact_kind": values["artifact_kind"],
        "candidate_score_record_sha256": score_record[
            "candidate_score_record_sha256"
        ],
        "proof_locator": values["proof_locator"],
        "proof_digest": values["proof_digest"],
        "proof_statement": values["proof_statement"],
        "support_t05_geometry_artifact_ids": list(t05_support),
        "support_t07_semantic_artifact_ids": list(t07_support),
        "evidence": values["evidence"],
    }
    output["candidate_score_artifact_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_parent_record(
    raw: dict[str, Any],
    *,
    parent_state_id: str,
    candidate_slot_ids: list[str],
    score_by_slot: dict[str, dict[str, Any]],
    path: str,
) -> dict[str, Any]:
    record_id = f"parent-policy::{parent_state_id}"
    require(raw.get("record_id") == record_id, f"{path}.record_id: mismatch")
    require(raw.get("parent_state_id") == parent_state_id,
            f"{path}.parent_state_id: mismatch")
    require(raw.get("candidate_slot_ids") == candidate_slot_ids,
            f"{path}.candidate_slot_ids: exact candidate set required")
    status = raw.get("status")
    selected = raw.get("selected_slot_id")
    minimum_score = raw.get("minimum_labelled_row_load")
    minimizer_count = raw.get("minimizer_count")
    locator = raw.get("verification_locator")
    digest = raw.get("verification_digest")
    note = raw.get("note")
    require(status in {"open", "proved"}, f"{path}.status: expected open/proved")
    require(isinstance(note, str) and note, f"{path}.note: required")
    proved_scores = [
        score_by_slot[slot_id]
        for slot_id in candidate_slot_ids
        if slot_id in score_by_slot and score_by_slot[slot_id]["status"] == "proved"
    ]
    if status == "open":
        require(selected is None, f"{path}.selected_slot_id: open requires null")
        require(minimum_score is None,
                f"{path}.minimum_labelled_row_load: open requires null")
        require(minimizer_count is None, f"{path}.minimizer_count: open requires null")
        require(locator is None, f"{path}.verification_locator: open requires null")
        require(digest is None, f"{path}.verification_digest: open requires null")
    else:
        require(len(proved_scores) == len(candidate_slot_ids),
                f"{path}: proved parent policy requires every candidate score")
        winner = min(
            proved_scores,
            key=lambda record: (
                record["minimum_labelled_row_load"],
                record["slot_id"],
            ),
        )
        exact_minimum = winner["minimum_labelled_row_load"]
        exact_minimizers = sum(
            record["minimum_labelled_row_load"] == exact_minimum
            for record in proved_scores
        )
        require(selected == winner["slot_id"], f"{path}.selected_slot_id: wrong winner")
        require(minimum_score == exact_minimum,
                f"{path}.minimum_labelled_row_load: wrong minimum")
        require(minimizer_count == exact_minimizers,
                f"{path}.minimizer_count: incorrect")
        require(
            locator == f"candidate-policy-parent-registry://{parent_state_id}",
            f"{path}.verification_locator: canonical parent URI required",
        )
        require(isinstance(digest, str) and digest, f"{path}.verification_digest: required")
    entries = []
    if len(proved_scores) == len(candidate_slot_ids):
        minimum = min(record["minimum_labelled_row_load"] for record in proved_scores)
        for slot_id in candidate_slot_ids:
            score = score_by_slot[slot_id]["minimum_labelled_row_load"]
            entries.append({
                "slot_id": slot_id,
                "minimum_labelled_row_load": score,
                "load_gap": score - minimum,
                "is_minimizer": int(score == minimum),
                "is_selected": int(slot_id == selected),
            })
    output = {
        "record_id": record_id,
        "parent_state_id": parent_state_id,
        "candidate_slot_ids": list(candidate_slot_ids),
        "status": status,
        "selected_slot_id": selected,
        "minimum_labelled_row_load": minimum_score,
        "minimizer_count": minimizer_count,
        "candidate_entries": entries,
        "verification_locator": locator,
        "verification_digest": digest,
        "note": note,
    }
    output["parent_candidate_policy_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_parent_artifact(
    raw: dict[str, Any],
    *,
    parent_record: dict[str, Any],
    expected_score_support: list[str],
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
    require(raw.get("parent_state_id") == parent_record["parent_state_id"],
            f"{path}.parent_state_id: mismatch")
    require(values["artifact_kind"] == PARENT_ARTIFACT_KIND,
            f"{path}.artifact_kind: wrong kind")
    require(
        raw.get("parent_candidate_policy_record_sha256")
        == parent_record["parent_candidate_policy_record_sha256"],
        f"{path}.parent_candidate_policy_record_sha256: mismatch",
    )
    support = raw.get("support_candidate_score_artifact_ids")
    require(support == expected_score_support,
            f"{path}.support_candidate_score_artifact_ids: exact support required")
    require(isinstance(support, list), f"{path}.support_candidate_score_artifact_ids: list required")
    require(support == sorted(support), f"{path}.support_candidate_score_artifact_ids: sorted")
    require(len(support) == len(set(support)), f"{path}.support_candidate_score_artifact_ids: duplicates")
    require(values["artifact_id"] not in support, f"{path}: self support")
    output = {
        "parent_state_id": parent_record["parent_state_id"],
        "artifact_id": values["artifact_id"],
        "artifact_kind": values["artifact_kind"],
        "parent_candidate_policy_record_sha256": parent_record[
            "parent_candidate_policy_record_sha256"
        ],
        "proof_locator": values["proof_locator"],
        "proof_digest": values["proof_digest"],
        "proof_statement": values["proof_statement"],
        "support_candidate_score_artifact_ids": list(support),
        "evidence": values["evidence"],
    }
    output["parent_candidate_policy_artifact_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_application_record(
    raw: dict[str, Any],
    *,
    application: dict[str, Any],
    local_parent_state_id: str,
    parent_record: dict[str, Any],
    path: str,
) -> dict[str, Any]:
    identity = application["identity"]
    global_parent = identity["parent_global_state_id"]
    record_id = f"application-policy::{global_parent}"
    require(raw.get("record_id") == record_id, f"{path}.record_id: mismatch")
    require(raw.get("parent_global_state_id") == global_parent,
            f"{path}.parent_global_state_id: mismatch")
    require(raw.get("local_parent_state_id") == local_parent_state_id,
            f"{path}.local_parent_state_id: mismatch")
    require(raw.get("t02_application_record_id") == application["record_id"],
            f"{path}.t02_application_record_id: mismatch")
    require(raw.get("applied_slot_id") == identity["operation_slot_id"],
            f"{path}.applied_slot_id: mismatch")
    require(raw.get("policy_selected_slot_id") == parent_record["selected_slot_id"],
            f"{path}.policy_selected_slot_id: mismatch")
    status = raw.get("status")
    locator = raw.get("verification_locator")
    digest = raw.get("verification_digest")
    note = raw.get("note")
    require(status in {"open", "proved"}, f"{path}.status: expected open/proved")
    require(isinstance(note, str) and note, f"{path}.note: required")
    if status == "open":
        require(locator is None, f"{path}.verification_locator: open requires null")
        require(digest is None, f"{path}.verification_digest: open requires null")
    else:
        require(parent_record["status"] == "proved",
                f"{path}: proved application requires proved parent policy")
        require(
            identity["operation_slot_id"] == parent_record["selected_slot_id"],
            f"{path}: T02 application does not use policy winner",
        )
        require(
            locator == f"candidate-policy-application-registry://{global_parent}",
            f"{path}.verification_locator: canonical application URI required",
        )
        require(isinstance(digest, str) and digest, f"{path}.verification_digest: required")
    output = {
        "record_id": record_id,
        "parent_global_state_id": global_parent,
        "local_parent_state_id": local_parent_state_id,
        "t02_application_record_id": application["record_id"],
        "applied_slot_id": identity["operation_slot_id"],
        "policy_selected_slot_id": parent_record["selected_slot_id"],
        "status": status,
        "verification_locator": locator,
        "verification_digest": digest,
        "note": note,
    }
    output["candidate_policy_application_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_application_artifact(
    raw: dict[str, Any],
    *,
    application_record: dict[str, Any],
    expected_parent_support: list[str],
    expected_t02_support: list[str],
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
    require(
        raw.get("parent_global_state_id")
        == application_record["parent_global_state_id"],
        f"{path}.parent_global_state_id: mismatch",
    )
    require(values["artifact_kind"] == APPLICATION_ARTIFACT_KIND,
            f"{path}.artifact_kind: wrong kind")
    require(
        raw.get("candidate_policy_application_record_sha256")
        == application_record["candidate_policy_application_record_sha256"],
        f"{path}.candidate_policy_application_record_sha256: mismatch",
    )
    parent_support = raw.get("support_parent_policy_artifact_ids")
    t02_support = raw.get("support_t02_application_artifact_ids")
    require(parent_support == expected_parent_support,
            f"{path}.support_parent_policy_artifact_ids: exact support required")
    require(t02_support == expected_t02_support,
            f"{path}.support_t02_application_artifact_ids: exact support required")
    for name, support in (
        ("support_parent_policy_artifact_ids", parent_support),
        ("support_t02_application_artifact_ids", t02_support),
    ):
        require(isinstance(support, list), f"{path}.{name}: list required")
        require(support == sorted(support), f"{path}.{name}: sorted")
        require(len(support) == len(set(support)), f"{path}.{name}: duplicates")
        require(values["artifact_id"] not in support, f"{path}: self support")
    output = {
        "parent_global_state_id": application_record["parent_global_state_id"],
        "artifact_id": values["artifact_id"],
        "artifact_kind": values["artifact_kind"],
        "candidate_policy_application_record_sha256": application_record[
            "candidate_policy_application_record_sha256"
        ],
        "proof_locator": values["proof_locator"],
        "proof_digest": values["proof_digest"],
        "proof_statement": values["proof_statement"],
        "support_parent_policy_artifact_ids": list(parent_support),
        "support_t02_application_artifact_ids": list(t02_support),
        "evidence": values["evidence"],
    }
    output["candidate_policy_application_artifact_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    t05_certificate = certificate.get("geometry_selector_frontier_certificate")
    t07_certificate = certificate.get("fate_transition_state_frontier_certificate")
    raw_scores = certificate.get("candidate_score_records")
    raw_score_artifacts = certificate.get("candidate_score_artifacts")
    raw_parents = certificate.get("parent_candidate_policy_records")
    raw_parent_artifacts = certificate.get("parent_candidate_policy_artifacts")
    raw_applications = certificate.get("candidate_policy_application_records")
    raw_application_artifacts = certificate.get("candidate_policy_application_artifacts")
    require(isinstance(t05_certificate, dict),
            "geometry_selector_frontier_certificate: expected object")
    require(isinstance(t07_certificate, dict),
            "fate_transition_state_frontier_certificate: expected object")
    for name, value in (
        ("candidate_score_records", raw_scores),
        ("candidate_score_artifacts", raw_score_artifacts),
        ("parent_candidate_policy_records", raw_parents),
        ("parent_candidate_policy_artifacts", raw_parent_artifacts),
        ("candidate_policy_application_records", raw_applications),
        ("candidate_policy_application_artifacts", raw_application_artifacts),
    ):
        require(isinstance(value, list), f"{name}: expected list")

    t05_frontier.validate_certificate(t05_certificate)
    t05_exact = t05_frontier.exact_certificate(t05_certificate)
    t07_frontier.validate_certificate(t07_certificate)
    t07_exact = t07_frontier.exact_certificate(t07_certificate)
    t04_from_t05 = t05_certificate["block_interface_population_frontier_certificate"]
    t04_from_t07 = t07_certificate["block_interface_population_frontier_certificate"]
    require(
        t04_from_t05["certificate_sha256"] == t04_from_t07["certificate_sha256"],
        "T05 and T07 use different T04 population certificates",
    )
    t04_certificate = t04_from_t05
    t03_certificate = t04_certificate["slot_candidate_population_frontier_certificate"]
    t03_module = __import__("check_prime_power_slot_candidate_population_frontier")
    t03_exact = t03_module.exact_certificate(t03_certificate)
    rule_certificate = t03_certificate["rule_exhaustiveness_frontier_certificate"]
    rule_frontier.validate_certificate(rule_certificate)
    rule_exact = rule_frontier.exact_certificate(rule_certificate)
    source_frontier = rule_certificate["source_truth_frontier_execution_certificate"]
    source_registry = source_frontier["source_statement_truth_registry_certificate"]
    obligation_certificate = source_registry["obligation_artifact_registry_certificate"]
    obligation_artifacts.validate_certificate(obligation_certificate)
    obligation_exact = obligation_artifacts.exact_certificate(obligation_certificate)
    closure_certificate = obligation_certificate["all_n_implication_closure_certificate"]
    closure_exact = closure.exact_certificate(closure_certificate)

    target_registry_t05 = t04_certificate["atomic_target_artifact_registry_certificate"]
    target_registry_t07 = t04_from_t07["atomic_target_artifact_registry_certificate"]
    require(
        target_registry_t05["certificate_sha256"]
        == target_registry_t07["certificate_sha256"],
        "T05 and T07 use different target-artifact registries",
    )
    target_registry = target_registry_t05
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
    slot_by_id = {slot["slot_id"]: slot for slot in slots}
    payload_by_slot = {
        payload["slot_id"]: payload for payload in t03_exact["slot_population_payloads"]
    }
    selector_by_slot = {
        summary["slot_id"]: summary for summary in t05_exact["slot_selector_summaries"]
    }
    semantic_by_slot = {
        semantic["slot_id"]: semantic
        for semantic in t07_exact["slot_fate_transition_state_semantic_certificates"]
    }
    t05_artifact_by_slot = {
        artifact["slot_id"]: artifact["artifact_id"]
        for artifact in t05_exact["slot_geometry_selector_artifacts"]
    }
    t07_artifact_by_slot = {
        artifact["slot_id"]: artifact["artifact_id"]
        for artifact in t07_exact["slot_fate_transition_state_artifacts"]
    }
    t02_artifact_by_record = {
        artifact["record_id"]: artifact["artifact_id"]
        for artifact in rule_exact["rule_exhaustiveness_artifacts"]
    }

    require(len(raw_scores) == len(slots),
            "candidate_score_records: exact slot cardinality required")
    require(
        [record.get("slot_id") for record in raw_scores]
        == [slot["slot_id"] for slot in slots],
        "candidate_score_records: canonical slot order required",
    )
    score_records = [
        exact_score_record(
            raw,
            slot=slot,
            payload=payload_by_slot.get(slot["slot_id"]),
            selector_summary=selector_by_slot.get(slot["slot_id"]),
            semantic_certificate=semantic_by_slot.get(slot["slot_id"]),
            path=f"candidate_score_records[{index}]",
        )
        for index, (raw, slot) in enumerate(zip(raw_scores, slots))
    ]
    require(raw_scores == score_records,
            "candidate_score_records: canonical records/digests required")
    score_by_slot = {record["slot_id"]: record for record in score_records}

    score_artifact_groups: dict[str, list[dict[str, Any]]] = {
        slot["slot_id"]: [] for slot in slots
    }
    for artifact in raw_score_artifacts:
        require(isinstance(artifact, dict), "candidate_score_artifacts: expected objects")
        slot_id = artifact.get("slot_id")
        require(slot_id in score_artifact_groups,
                f"candidate score artifact: unknown slot {slot_id}")
        score_artifact_groups[slot_id].append(artifact)
    score_artifacts: list[dict[str, Any]] = []
    score_artifact_by_slot: dict[str, str] = {}
    score_bundle_records: list[dict[str, Any]] = []
    for record in score_records:
        slot_id = record["slot_id"]
        group = score_artifact_groups[slot_id]
        artifact_list: list[dict[str, Any]] = []
        if record["status"] == "open":
            require(not group, f"slot {slot_id}: open score cannot contain artifact")
        else:
            require(len(group) == 1, f"slot {slot_id}: exactly one score artifact required")
            require(slot_id in t05_artifact_by_slot,
                    f"slot {slot_id}: proved score requires T05 artifact")
            require(slot_id in t07_artifact_by_slot,
                    f"slot {slot_id}: proved score requires T07 artifact")
            artifact = exact_score_artifact(
                group[0],
                score_record=record,
                expected_t05_support=[t05_artifact_by_slot[slot_id]],
                expected_t07_support=[t07_artifact_by_slot[slot_id]],
                path=f"candidate_score_artifact[{slot_id}]",
            )
            score_artifacts.append(artifact)
            artifact_list = [artifact]
            score_artifact_by_slot[slot_id] = artifact["artifact_id"]
            bundle = {
                "slot_id": slot_id,
                "candidate_score_record_sha256": record["candidate_score_record_sha256"],
                "candidate_score_artifact_sha256": artifact[
                    "candidate_score_artifact_sha256"
                ],
                "support_t05_geometry_artifact_ids": [t05_artifact_by_slot[slot_id]],
                "support_t07_semantic_artifact_ids": [t07_artifact_by_slot[slot_id]],
            }
            bundle["candidate_score_proof_bundle_sha256"] = catalogue.canonical_digest(bundle)
            require(
                record["verification_digest"]
                == bundle["candidate_score_proof_bundle_sha256"],
                f"slot {slot_id}: score digest does not bind proof bundle",
            )
        score_bundle = {
            "slot_id": slot_id,
            "status": record["status"],
            "artifacts_sha256": catalogue.canonical_digest(artifact_list),
        }
        score_bundle["candidate_score_bundle_sha256"] = catalogue.canonical_digest(
            score_bundle
        )
        score_bundle_records.append(score_bundle)
    require(raw_score_artifacts == score_artifacts,
            "candidate_score_artifacts: canonical order/content required")

    slots_by_parent: dict[str, list[str]] = {}
    for slot in slots:
        slots_by_parent.setdefault(slot["parent_state_id"], []).append(slot["slot_id"])
    for parent in slots_by_parent:
        slots_by_parent[parent].sort()
    parent_ids = sorted(slots_by_parent)
    require(len(raw_parents) == len(parent_ids),
            "parent_candidate_policy_records: exact parent cardinality required")
    require(
        [record.get("parent_state_id") for record in raw_parents] == parent_ids,
        "parent_candidate_policy_records: canonical parent order required",
    )
    parent_records = [
        exact_parent_record(
            raw,
            parent_state_id=parent,
            candidate_slot_ids=slots_by_parent[parent],
            score_by_slot=score_by_slot,
            path=f"parent_candidate_policy_records[{index}]",
        )
        for index, (raw, parent) in enumerate(zip(raw_parents, parent_ids))
    ]
    require(raw_parents == parent_records,
            "parent_candidate_policy_records: canonical records/digests required")
    parent_by_id = {record["parent_state_id"]: record for record in parent_records}

    parent_artifact_groups: dict[str, list[dict[str, Any]]] = {
        parent: [] for parent in parent_ids
    }
    for artifact in raw_parent_artifacts:
        require(isinstance(artifact, dict),
                "parent_candidate_policy_artifacts: expected objects")
        parent = artifact.get("parent_state_id")
        require(parent in parent_artifact_groups,
                f"parent policy artifact: unknown parent {parent}")
        parent_artifact_groups[parent].append(artifact)
    parent_artifacts: list[dict[str, Any]] = []
    parent_artifact_by_id: dict[str, str] = {}
    parent_bundle_records: list[dict[str, Any]] = []
    for record in parent_records:
        parent = record["parent_state_id"]
        group = parent_artifact_groups[parent]
        artifact_list: list[dict[str, Any]] = []
        if record["status"] == "open":
            require(not group, f"parent {parent}: open policy cannot contain artifact")
        else:
            require(len(group) == 1,
                    f"parent {parent}: exactly one policy artifact required")
            expected_support = sorted(
                score_artifact_by_slot[slot_id]
                for slot_id in record["candidate_slot_ids"]
                if slot_id in score_artifact_by_slot
            )
            require(len(expected_support) == len(record["candidate_slot_ids"]),
                    f"parent {parent}: every candidate score must be proved")
            artifact = exact_parent_artifact(
                group[0],
                parent_record=record,
                expected_score_support=expected_support,
                path=f"parent_candidate_policy_artifact[{parent}]",
            )
            parent_artifacts.append(artifact)
            artifact_list = [artifact]
            parent_artifact_by_id[parent] = artifact["artifact_id"]
            bundle = {
                "parent_state_id": parent,
                "parent_candidate_policy_record_sha256": record[
                    "parent_candidate_policy_record_sha256"
                ],
                "parent_candidate_policy_artifact_sha256": artifact[
                    "parent_candidate_policy_artifact_sha256"
                ],
                "support_candidate_score_artifact_ids": expected_support,
            }
            bundle["parent_candidate_policy_proof_bundle_sha256"] = catalogue.canonical_digest(bundle)
            require(
                record["verification_digest"]
                == bundle["parent_candidate_policy_proof_bundle_sha256"],
                f"parent {parent}: policy digest does not bind proof bundle",
            )
        parent_bundle = {
            "parent_state_id": parent,
            "status": record["status"],
            "artifacts_sha256": catalogue.canonical_digest(artifact_list),
        }
        parent_bundle["parent_candidate_policy_bundle_sha256"] = catalogue.canonical_digest(
            parent_bundle
        )
        parent_bundle_records.append(parent_bundle)
    require(raw_parent_artifacts == parent_artifacts,
            "parent_candidate_policy_artifacts: canonical order/content required")

    applications = sorted(
        [
            record for record in rule_exact["rule_exhaustiveness_records"]
            if record["record_kind"] == "global-parent-application"
        ],
        key=lambda record: record["identity"]["parent_global_state_id"],
    )
    require(len(raw_applications) == len(applications),
            "candidate_policy_application_records: exact application cardinality required")
    require(
        [record.get("parent_global_state_id") for record in raw_applications]
        == [record["identity"]["parent_global_state_id"] for record in applications],
        "candidate_policy_application_records: canonical global-parent order required",
    )
    application_records = []
    for index, (raw, application) in enumerate(zip(raw_applications, applications)):
        slot_id = application["identity"]["operation_slot_id"]
        require(slot_id in slot_by_id, f"T02 application uses unknown slot {slot_id}")
        local_parent = slot_by_id[slot_id]["parent_state_id"]
        require(local_parent in parent_by_id,
                f"T02 application has unknown local parent {local_parent}")
        application_records.append(
            exact_application_record(
                raw,
                application=application,
                local_parent_state_id=local_parent,
                parent_record=parent_by_id[local_parent],
                path=f"candidate_policy_application_records[{index}]",
            )
        )
    require(raw_applications == application_records,
            "candidate_policy_application_records: canonical records/digests required")

    application_artifact_groups: dict[str, list[dict[str, Any]]] = {
        record["parent_global_state_id"]: [] for record in application_records
    }
    for artifact in raw_application_artifacts:
        require(isinstance(artifact, dict),
                "candidate_policy_application_artifacts: expected objects")
        parent = artifact.get("parent_global_state_id")
        require(parent in application_artifact_groups,
                f"application policy artifact: unknown global parent {parent}")
        application_artifact_groups[parent].append(artifact)
    application_artifacts: list[dict[str, Any]] = []
    application_bundle_records: list[dict[str, Any]] = []
    application_by_global = {
        record["identity"]["parent_global_state_id"]: record for record in applications
    }
    for record in application_records:
        global_parent = record["parent_global_state_id"]
        group = application_artifact_groups[global_parent]
        artifact_list: list[dict[str, Any]] = []
        if record["status"] == "open":
            require(not group,
                    f"application {global_parent}: open policy cannot contain artifact")
        else:
            require(len(group) == 1,
                    f"application {global_parent}: exactly one policy artifact required")
            local_parent = record["local_parent_state_id"]
            require(local_parent in parent_artifact_by_id,
                    f"application {global_parent}: parent policy artifact missing")
            t02_record_id = application_by_global[global_parent]["record_id"]
            require(t02_record_id in t02_artifact_by_record,
                    f"application {global_parent}: T02 application artifact missing")
            expected_parent_support = [parent_artifact_by_id[local_parent]]
            expected_t02_support = [t02_artifact_by_record[t02_record_id]]
            artifact = exact_application_artifact(
                group[0],
                application_record=record,
                expected_parent_support=expected_parent_support,
                expected_t02_support=expected_t02_support,
                path=f"candidate_policy_application_artifact[{global_parent}]",
            )
            application_artifacts.append(artifact)
            artifact_list = [artifact]
            bundle = {
                "parent_global_state_id": global_parent,
                "candidate_policy_application_record_sha256": record[
                    "candidate_policy_application_record_sha256"
                ],
                "candidate_policy_application_artifact_sha256": artifact[
                    "candidate_policy_application_artifact_sha256"
                ],
                "support_parent_policy_artifact_ids": expected_parent_support,
                "support_t02_application_artifact_ids": expected_t02_support,
            }
            bundle["candidate_policy_application_proof_bundle_sha256"] = (
                catalogue.canonical_digest(bundle)
            )
            require(
                record["verification_digest"]
                == bundle["candidate_policy_application_proof_bundle_sha256"],
                f"application {global_parent}: digest does not bind proof bundle",
            )
        application_bundle = {
            "parent_global_state_id": global_parent,
            "status": record["status"],
            "artifacts_sha256": catalogue.canonical_digest(artifact_list),
        }
        application_bundle["candidate_policy_application_bundle_sha256"] = (
            catalogue.canonical_digest(application_bundle)
        )
        application_bundle_records.append(application_bundle)
    require(raw_application_artifacts == application_artifacts,
            "candidate_policy_application_artifacts: canonical order/content required")

    all_artifact_ids = [
        artifact["artifact_id"]
        for artifact in (
            score_artifacts + parent_artifacts + application_artifacts
        )
    ]
    require(len(all_artifact_ids) == len(set(all_artifact_ids)),
            "candidate policy artifacts: duplicate artifact_id")

    score_counts = Counter(record["status"] for record in score_records)
    parent_counts = Counter(record["status"] for record in parent_records)
    application_counts = Counter(record["status"] for record in application_records)
    t05_ready = int(t05_exact["claims"]["geometry_selector_correct_ready"])
    t07_ready = int(t07_exact["claims"]["fate_transition_state_semantics_ready"])
    policy_ready = int(
        t05_ready
        and t07_ready
        and score_counts["proved"] == len(score_records)
        and parent_counts["proved"] == len(parent_records)
        and application_counts["proved"] == len(application_records)
    )

    policy_bank = {
        "expected_slot_registry_sha256": t03_exact["claims"]["expected_slot_registry_sha256"],
        "t02_application_records_sha256": catalogue.canonical_digest(applications),
        "t05_selector_summaries_sha256": t05_exact["claims"][
            "slot_selector_summaries_sha256"
        ],
        "t05_geometry_artifacts_sha256": t05_exact["claims"][
            "slot_geometry_selector_artifacts_sha256"
        ],
        "t07_semantic_certificates_sha256": t07_exact["claims"][
            "slot_semantic_certificates_sha256"
        ],
        "t07_semantic_artifacts_sha256": t07_exact["claims"][
            "slot_semantic_artifacts_sha256"
        ],
        "candidate_score_records_sha256": catalogue.canonical_digest(score_records),
        "candidate_score_artifacts_sha256": catalogue.canonical_digest(score_artifacts),
        "candidate_score_bundles_sha256": catalogue.canonical_digest(score_bundle_records),
        "parent_policy_records_sha256": catalogue.canonical_digest(parent_records),
        "parent_policy_artifacts_sha256": catalogue.canonical_digest(parent_artifacts),
        "parent_policy_bundles_sha256": catalogue.canonical_digest(parent_bundle_records),
        "application_policy_records_sha256": catalogue.canonical_digest(application_records),
        "application_policy_artifacts_sha256": catalogue.canonical_digest(application_artifacts),
        "application_policy_bundles_sha256": catalogue.canonical_digest(
            application_bundle_records
        ),
    }
    policy_bank["candidate_policy_proof_bank_sha256"] = catalogue.canonical_digest(
        policy_bank
    )

    closure_by_id = {
        record["obligation_id"]: record
        for record in closure_exact["obligation_closure_records"]
    }
    policy_closure = closure_by_id["CANDIDATE_POLICY_CORRECT"]
    require(
        int(policy_closure["closed"]) == policy_ready,
        "CANDIDATE_POLICY_CORRECT closure disagrees with exact T06 bank",
    )

    policy_obligation_artifacts = [
        artifact
        for artifact in obligation_exact["proof_artifacts"]
        if artifact["obligation_id"] == "CANDIDATE_POLICY_CORRECT"
    ]
    dependency_artifact_ids = sorted(
        artifact["artifact_id"]
        for artifact in obligation_exact["proof_artifacts"]
        if artifact["obligation_id"] in {
            "GEOMETRY_SELECTOR_CORRECT",
            "FATE_TRANSITION_STATE_SEMANTICS",
        }
    )
    require(
        len(policy_obligation_artifacts) == (1 if policy_ready else 0),
        "CANDIDATE_POLICY_CORRECT artifact presence disagrees with readiness",
    )
    if policy_ready:
        obligation_artifact = policy_obligation_artifacts[0]
        require(obligation_artifact["artifact_kind"] == "candidate-policy-proof",
                "CANDIDATE_POLICY_CORRECT requires candidate-policy-proof")
        require(obligation_artifact["locator"] == OBLIGATION_LOCATOR,
                "candidate-policy-proof locator does not bind T06 bank")
        require(
            obligation_artifact["digest"]
            == policy_bank["candidate_policy_proof_bank_sha256"],
            "candidate-policy-proof digest does not bind exact T06 bank",
        )
        require(
            obligation_artifact["support_artifact_ids"] == dependency_artifact_ids,
            "candidate-policy-proof requires exact geometry and semantic support",
        )

    target_results = {
        record["target_id"]: record for record in atomic_exact["target_result_records"]
    }
    t06_complete = int(
        target_results["T06_CANDIDATE_POLICY"]["effective_target_complete"]
    )
    require(t06_complete == policy_ready,
            "T06_CANDIDATE_POLICY completion disagrees with exact policy bank")
    target_artifact_by_id = {
        artifact["target_id"]: artifact
        for artifact in target_exact["atomic_target_artifacts"]
    }
    t06_artifact = target_artifact_by_id.get("T06_CANDIDATE_POLICY")
    if policy_ready:
        require(t06_artifact is not None,
                "completed T06 target missing candidate-policy-proof artifact")
        require(t06_artifact["artifact_kind"] == "candidate-policy-proof",
                "T06 target requires candidate-policy-proof")
        require(t06_artifact["proof_locator"] == T06_TARGET_LOCATOR,
                "T06 target proof locator does not bind T06 frontier")
        require(
            t06_artifact["proof_digest"]
            == policy_bank["candidate_policy_proof_bank_sha256"],
            "T06 target proof digest does not bind noncircular policy bank",
        )
    else:
        require(t06_artifact is None, "open T06 target cannot contain target artifact")

    claims = {
        "expected_slots": len(slots),
        "candidate_parents": len(parent_records),
        "global_parent_applications": len(application_records),
        "open_candidate_scores": score_counts["open"],
        "proved_candidate_scores": score_counts["proved"],
        "open_parent_policies": parent_counts["open"],
        "proved_parent_policies": parent_counts["proved"],
        "open_application_policies": application_counts["open"],
        "proved_application_policies": application_counts["proved"],
        "t05_geometry_selector_ready": t05_ready,
        "t07_fate_transition_state_ready": t07_ready,
        "candidate_policy_correct_ready": policy_ready,
        "exact_complete_candidate_sets": 1,
        "exact_lexicographic_candidate_minimization": 1,
        "exact_t02_application_to_policy_winner_binding": 1,
        "exact_t05_t07_score_artifact_support": 1,
        "noncircular_candidate_policy_bank_binding": 1,
        "candidate_policy_obligation_synchronized": 1,
        "t06_atomic_target_synchronized": 1,
        "all_n_proved_by_checker": 0,
        "open_slot_ids": [
            record["slot_id"] for record in score_records if record["status"] == "open"
        ],
        "open_parent_state_ids": [
            record["parent_state_id"]
            for record in parent_records
            if record["status"] == "open"
        ],
        "open_parent_global_state_ids": [
            record["parent_global_state_id"]
            for record in application_records
            if record["status"] == "open"
        ],
        "candidate_score_records_sha256": catalogue.canonical_digest(score_records),
        "candidate_score_artifacts_sha256": catalogue.canonical_digest(score_artifacts),
        "parent_policy_records_sha256": catalogue.canonical_digest(parent_records),
        "parent_policy_artifacts_sha256": catalogue.canonical_digest(parent_artifacts),
        "application_policy_records_sha256": catalogue.canonical_digest(application_records),
        "application_policy_artifacts_sha256": catalogue.canonical_digest(application_artifacts),
        "candidate_policy_proof_bank_sha256": policy_bank[
            "candidate_policy_proof_bank_sha256"
        ],
        "obligation_artifact_registry_sha256": obligation_certificate[
            "certificate_sha256"
        ],
        "atomic_target_artifact_registry_sha256": target_registry[
            "certificate_sha256"
        ],
    }
    return {
        "candidate_score_records": score_records,
        "candidate_score_artifacts": score_artifacts,
        "candidate_score_bundle_records": score_bundle_records,
        "parent_candidate_policy_records": parent_records,
        "parent_candidate_policy_artifacts": parent_artifacts,
        "parent_candidate_policy_bundle_records": parent_bundle_records,
        "candidate_policy_application_records": application_records,
        "candidate_policy_application_artifacts": application_artifacts,
        "candidate_policy_application_bundle_records": application_bundle_records,
        "candidate_policy_proof_bank": policy_bank,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in (
        "candidate_score_records",
        "candidate_score_artifacts",
        "candidate_score_bundle_records",
        "parent_candidate_policy_records",
        "parent_candidate_policy_artifacts",
        "parent_candidate_policy_bundle_records",
        "candidate_policy_application_records",
        "candidate_policy_application_artifacts",
        "candidate_policy_application_bundle_records",
        "candidate_policy_proof_bank",
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
        "parents": claims["candidate_parents"],
        "applications": claims["global_parent_applications"],
        "proved_scores": claims["proved_candidate_scores"],
        "proved_parents": claims["proved_parent_policies"],
        "proved_applications": claims["proved_application_policies"],
        "ready": claims["candidate_policy_correct_ready"],
        "all_n": claims["all_n_proved_by_checker"],
    }


def build_certificate(
    t05_certificate: dict[str, Any],
    t07_certificate: dict[str, Any],
    score_records: list[dict[str, Any]],
    score_artifacts: list[dict[str, Any]],
    parent_records: list[dict[str, Any]],
    parent_artifacts: list[dict[str, Any]],
    application_records: list[dict[str, Any]],
    application_artifacts: list[dict[str, Any]],
) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "geometry_selector_frontier_certificate": t05_certificate,
        "fate_transition_state_frontier_certificate": t07_certificate,
        "candidate_score_records": score_records,
        "candidate_score_artifacts": score_artifacts,
        "parent_candidate_policy_records": parent_records,
        "parent_candidate_policy_artifacts": parent_artifacts,
        "candidate_policy_application_records": application_records,
        "candidate_policy_application_artifacts": application_artifacts,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: check_prime_power_candidate_policy_frontier.py certificate.json"
        )
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
