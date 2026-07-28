#!/usr/bin/env python3
"""Validate the exact T08/T09/T10 transition-resource proof banks.

T06 fixes one selected operation slot for every T02 global-parent application.  This checker derives
one active row from every such application, reconstructs every row's literal destroyed-triple
universe from the linked T05 geometry certificate, derives overlap scopes, and gives every literal
T03 routed-credit entry one exact semantic route into T07 fate/state/transition claims.

The three proof banks remain separate and noncircular:

    T06 -> T08 active rows
    T05 + T08 -> T09 destroyed resources
    T07 + T09 -> T10 routed-credit semantics

This checker validates documentary identity, coverage, support, injectivity and digest binding.  It
does not prove the external mathematical statements true and permanently reports
``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter, deque
from pathlib import Path
from typing import Any

import check_prime_power_all_n_implication_closure as closure
import check_prime_power_atomic_frontier_execution as atomic
import check_prime_power_atomic_target_artifact_registry as target_artifacts
import check_prime_power_block_interface_population_frontier as t04_frontier
import check_prime_power_candidate_policy_frontier as t06_frontier
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_fate_transition_state_frontier as t07_frontier
import check_prime_power_geometry_selector_frontier_v2 as t05_frontier
import check_prime_power_obligation_artifact_registry as obligation_artifacts
import check_prime_power_slot_candidate_population_frontier as t03_frontier
import check_prime_power_witness_bound_destroyed_credit_routing as witness_routing


class TransitionResourceFrontierError(ValueError):
    """Raised when an exact T08/T09/T10 proof bank is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise TransitionResourceFrontierError(message)


ACTIVE_ROW_ARTIFACT_KIND = "active-row-member-proof"
RESOURCE_ROW_ARTIFACT_KIND = "row-destroyed-resource-model-proof"
CREDIT_ROW_ARTIFACT_KIND = "row-routed-credit-semantics-proof"

T08_OBLIGATION_LOCATOR = "active-row-family-frontier://ACTIVE_ROW_FAMILY_EXHAUSTIVE"
T09_OBLIGATION_LOCATOR = (
    "destroyed-resource-model-frontier://DESTROYED_RESOURCE_MODEL_EXHAUSTIVE"
)
T10_OBLIGATION_LOCATOR = "routed-credit-semantics-frontier://CREDIT_ROUTING_SEMANTIC"

T08_TARGET_LOCATOR = "active-row-family-frontier://T08_ACTIVE_ROW_FAMILY"
T09_TARGET_LOCATOR = "destroyed-resource-model-frontier://T09_RESOURCE_MODEL"
T10_TARGET_LOCATOR = "routed-credit-semantics-frontier://T10_CREDIT_ROUTING"


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


def connected_components(nodes: list[str], edges: set[tuple[str, str]]) -> list[list[str]]:
    adjacency = {node: set() for node in nodes}
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    remaining = set(nodes)
    components: list[list[str]] = []
    while remaining:
        start = min(remaining)
        queue = deque([start])
        seen = {start}
        while queue:
            current = queue.popleft()
            for nxt in sorted(adjacency[current]):
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        remaining -= seen
        components.append(sorted(seen))
    components.sort()
    return components


def fixed_artifact(
    raw: dict[str, Any],
    *,
    identity: dict[str, Any],
    required_kind: str,
    bound_digest_name: str,
    bound_digest: str,
    expected_support_fields: dict[str, list[str]],
    output_digest_name: str,
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
    for name, value in identity.items():
        require(raw.get(name) == value, f"{path}.{name}: mismatch")
    require(values["artifact_kind"] == required_kind, f"{path}.artifact_kind: wrong kind")
    require(raw.get(bound_digest_name) == bound_digest, f"{path}.{bound_digest_name}: mismatch")
    output = {
        **identity,
        "artifact_id": values["artifact_id"],
        "artifact_kind": values["artifact_kind"],
        bound_digest_name: bound_digest,
        "proof_locator": values["proof_locator"],
        "proof_digest": values["proof_digest"],
        "proof_statement": values["proof_statement"],
    }
    for support_name, expected in expected_support_fields.items():
        support = raw.get(support_name)
        require(support == expected, f"{path}.{support_name}: exact support required")
        require(isinstance(support, list), f"{path}.{support_name}: list required")
        require(support == sorted(support), f"{path}.{support_name}: sorted")
        require(len(support) == len(set(support)), f"{path}.{support_name}: duplicates")
        require(values["artifact_id"] not in support, f"{path}: self support")
        output[support_name] = list(support)
    output["evidence"] = values["evidence"]
    output[output_digest_name] = catalogue.canonical_digest(output)
    return output


def exact_active_row_record(
    raw: dict[str, Any],
    *,
    application: dict[str, Any],
    payload: dict[str, Any] | None,
    semantic: dict[str, Any] | None,
    using_unit_ids: list[str],
    path: str,
) -> dict[str, Any]:
    global_parent = application["parent_global_state_id"]
    local_parent = application["local_parent_state_id"]
    slot_id = application["applied_slot_id"]
    row_id = f"active::{global_parent}"
    require(raw.get("row_id") == row_id, f"{path}.row_id: mismatch")
    require(raw.get("parent_global_state_id") == global_parent,
            f"{path}.parent_global_state_id: mismatch")
    require(raw.get("local_parent_state_id") == local_parent,
            f"{path}.local_parent_state_id: mismatch")
    require(raw.get("selected_slot_id") == slot_id, f"{path}.selected_slot_id: mismatch")
    require(raw.get("candidate_policy_application_record_sha256")
            == application["candidate_policy_application_record_sha256"],
            f"{path}.candidate_policy_application_record_sha256: mismatch")

    payload_sha = None if payload is None else payload["slot_population_payload_sha256"]
    row_loads_sha = None if payload is None else catalogue.canonical_digest(
        payload["population_data"]["row_loads"]
    )
    response_sha = None if payload is None else catalogue.canonical_digest(
        payload["population_data"]["response_family"]
    )
    credits_sha = None if payload is None else catalogue.canonical_digest(
        payload["population_data"]["routed_credits"]
    )
    transitions_sha = None if payload is None else catalogue.canonical_digest(
        payload["population_data"]["transitions"]
    )
    semantic_sha = None if semantic is None else semantic[
        "slot_fate_transition_state_semantics_sha256"
    ]
    exact_fields = {
        "slot_population_payload_sha256": payload_sha,
        "row_loads_sha256": row_loads_sha,
        "response_family_sha256": response_sha,
        "routed_credits_sha256": credits_sha,
        "transitions_sha256": transitions_sha,
        "slot_semantic_certificate_sha256": semantic_sha,
        "using_t04_unit_ids": using_unit_ids,
    }
    for name, value in exact_fields.items():
        require(raw.get(name) == value, f"{path}.{name}: mismatch")

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
        require(application["status"] == "proved",
                f"{path}: proved active row requires proved T06 application")
        require(payload is not None and semantic is not None,
                f"{path}: proved active row requires T03 and T07 data")
        require(locator == f"active-row-family-registry://{row_id}",
                f"{path}.verification_locator: canonical row URI required")
        require(isinstance(digest, str) and digest, f"{path}.verification_digest: required")
    output = {
        "row_id": row_id,
        "parent_global_state_id": global_parent,
        "local_parent_state_id": local_parent,
        "selected_slot_id": slot_id,
        "candidate_policy_application_record_sha256": application[
            "candidate_policy_application_record_sha256"
        ],
        **exact_fields,
        "status": status,
        "verification_locator": locator,
        "verification_digest": digest,
        "note": note,
    }
    output["active_row_record_sha256"] = catalogue.canonical_digest(output)
    return output


def resource_key(points: list[list[int]]) -> str:
    canonical_points = sorted(tuple(point) for point in points)
    return f"resource-{catalogue.canonical_digest(canonical_points)[:24]}"


def exact_literal_resources(
    *,
    row: dict[str, Any],
    geometry_wrapper: dict[str, Any] | None,
) -> list[dict[str, Any]]:
    if geometry_wrapper is None:
        return []
    nested = geometry_wrapper["linked_operation_selector_certificate"]
    destroyed = witness_routing.exact_destroyed_records(nested)
    records = []
    for item in destroyed:
        record = {
            "row_id": row["row_id"],
            "selected_slot_id": row["selected_slot_id"],
            "resource_key": resource_key(item["points"]),
            "points": sorted(copy.deepcopy(item["points"])),
            "source_destroyed_id": item["destroyed_id"],
            "source_destroyed_record_sha256": item["destroyed_record_sha256"],
        }
        record["literal_resource_record_sha256"] = catalogue.canonical_digest(record)
        records.append(record)
    records.sort(key=lambda record: record["resource_key"])
    require(len({record["resource_key"] for record in records}) == len(records),
            f"row {row['row_id']}: duplicate canonical destroyed resource")
    return records


def exact_resource_model_record(
    raw: dict[str, Any],
    *,
    row: dict[str, Any],
    resources: list[dict[str, Any]],
    path: str,
) -> dict[str, Any]:
    row_id = row["row_id"]
    require(raw.get("row_id") == row_id, f"{path}.row_id: mismatch")
    require(raw.get("parent_global_state_id") == row["parent_global_state_id"],
            f"{path}.parent_global_state_id: mismatch")
    require(raw.get("selected_slot_id") == row["selected_slot_id"],
            f"{path}.selected_slot_id: mismatch")
    require(raw.get("active_row_record_sha256") == row["active_row_record_sha256"],
            f"{path}.active_row_record_sha256: mismatch")
    resource_keys = [record["resource_key"] for record in resources]
    resource_records_sha = catalogue.canonical_digest(resources)
    require(raw.get("literal_resource_keys") == resource_keys,
            f"{path}.literal_resource_keys: exact resource universe required")
    require(raw.get("literal_resource_records_sha256") == resource_records_sha,
            f"{path}.literal_resource_records_sha256: mismatch")
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
        require(row["status"] == "proved", f"{path}: proved resource model requires proved active row")
        require(locator == f"destroyed-resource-model-registry://{row_id}",
                f"{path}.verification_locator: canonical row URI required")
        require(isinstance(digest, str) and digest, f"{path}.verification_digest: required")
    output = {
        "row_id": row_id,
        "parent_global_state_id": row["parent_global_state_id"],
        "selected_slot_id": row["selected_slot_id"],
        "active_row_record_sha256": row["active_row_record_sha256"],
        "literal_resource_keys": resource_keys,
        "literal_resource_records_sha256": resource_records_sha,
        "status": status,
        "verification_locator": locator,
        "verification_digest": digest,
        "note": note,
    }
    output["resource_model_record_sha256"] = catalogue.canonical_digest(output)
    return output


def credit_subjects(row: dict[str, Any], payload: dict[str, Any] | None) -> list[dict[str, Any]]:
    if payload is None:
        return []
    output = []
    for index, value in enumerate(payload["population_data"]["routed_credits"]):
        subject = {
            "row_id": row["row_id"],
            "selected_slot_id": row["selected_slot_id"],
            "credit_index": index,
            "credit_value": canonical_json_value(value, f"routed_credits[{index}]"),
        }
        subject["credit_subject_sha256"] = catalogue.canonical_digest(subject)
        output.append(subject)
    return output


def exact_route_assignment(
    raw: dict[str, Any],
    *,
    subject: dict[str, Any],
    resource_keys: set[str],
    fate_claim_ids: set[str],
    state_claim_ids: set[str],
    transition_claim_ids: set[str],
    path: str,
) -> dict[str, Any]:
    require(raw.get("credit_subject_sha256") == subject["credit_subject_sha256"],
            f"{path}.credit_subject_sha256: mismatch")
    destroyed_key = raw.get("destroyed_resource_key")
    fate_claim = raw.get("fate_claim_id")
    state_claim = raw.get("state_claim_id")
    transition_claims = raw.get("transition_claim_ids")
    child = raw.get("child_state_id")
    statement = raw.get("route_statement")
    evidence = raw.get("evidence")
    require(isinstance(destroyed_key, str) and destroyed_key in resource_keys,
            f"{path}.destroyed_resource_key: unknown row resource")
    require(isinstance(fate_claim, str) and fate_claim in fate_claim_ids,
            f"{path}.fate_claim_id: unknown slot fate claim")
    require(isinstance(state_claim, str) and state_claim in state_claim_ids,
            f"{path}.state_claim_id: unknown slot state claim")
    require(isinstance(transition_claims, list) and transition_claims,
            f"{path}.transition_claim_ids: nonempty list required")
    require(transition_claims == sorted(transition_claims),
            f"{path}.transition_claim_ids: sorted")
    require(len(transition_claims) == len(set(transition_claims)),
            f"{path}.transition_claim_ids: duplicates")
    require(set(transition_claims) <= transition_claim_ids,
            f"{path}.transition_claim_ids: unknown slot transition claim")
    require(isinstance(child, str) and child, f"{path}.child_state_id: required")
    require(isinstance(statement, str) and statement, f"{path}.route_statement: required")
    require(isinstance(evidence, str) and evidence, f"{path}.evidence: required")
    output = {
        "credit_subject_sha256": subject["credit_subject_sha256"],
        "destroyed_resource_key": destroyed_key,
        "fate_claim_id": fate_claim,
        "state_claim_id": state_claim,
        "transition_claim_ids": list(transition_claims),
        "child_state_id": child,
        "route_statement": statement,
        "evidence": evidence,
    }
    output["routed_credit_assignment_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_credit_semantic_record(
    raw: dict[str, Any],
    *,
    row: dict[str, Any],
    resource_record: dict[str, Any],
    subjects: list[dict[str, Any]],
    semantic: dict[str, Any] | None,
    path: str,
) -> dict[str, Any]:
    row_id = row["row_id"]
    require(raw.get("row_id") == row_id, f"{path}.row_id: mismatch")
    require(raw.get("parent_global_state_id") == row["parent_global_state_id"],
            f"{path}.parent_global_state_id: mismatch")
    require(raw.get("selected_slot_id") == row["selected_slot_id"],
            f"{path}.selected_slot_id: mismatch")
    require(raw.get("active_row_record_sha256") == row["active_row_record_sha256"],
            f"{path}.active_row_record_sha256: mismatch")
    require(raw.get("resource_model_record_sha256")
            == resource_record["resource_model_record_sha256"],
            f"{path}.resource_model_record_sha256: mismatch")
    require(raw.get("credit_subjects") == subjects,
            f"{path}.credit_subjects: exact routed-credit subject bank required")
    require(raw.get("credit_subjects_sha256") == catalogue.canonical_digest(subjects),
            f"{path}.credit_subjects_sha256: mismatch")
    status = raw.get("status")
    locator = raw.get("verification_locator")
    digest = raw.get("verification_digest")
    note = raw.get("note")
    assignments_raw = raw.get("route_assignments")
    require(status in {"open", "proved"}, f"{path}.status: expected open/proved")
    require(isinstance(note, str) and note, f"{path}.note: required")
    require(isinstance(assignments_raw, list), f"{path}.route_assignments: expected list")
    assignments: list[dict[str, Any]] = []
    if status == "open":
        require(not assignments_raw, f"{path}.route_assignments: open record requires empty list")
        require(locator is None, f"{path}.verification_locator: open requires null")
        require(digest is None, f"{path}.verification_digest: open requires null")
    else:
        require(row["status"] == "proved" and resource_record["status"] == "proved",
                f"{path}: proved credit semantics requires proved T08 and T09 rows")
        require(semantic is not None, f"{path}: proved credit semantics requires T07 certificate")
        require(len(assignments_raw) == len(subjects),
                f"{path}.route_assignments: exact credit cardinality required")
        fate_ids = {claim["claim_id"] for claim in semantic["fate_claims"]}
        state_ids = {claim["claim_id"] for claim in semantic["state_claims"]}
        transition_ids = {claim["claim_id"] for claim in semantic["transition_claims"]}
        require(not subjects or (fate_ids and state_ids and transition_ids),
                f"{path}: nonempty routed credits require fate/state/transition claims")
        resource_keys = set(resource_record["literal_resource_keys"])
        assignments = [
            exact_route_assignment(
                assignment,
                subject=subject,
                resource_keys=resource_keys,
                fate_claim_ids=fate_ids,
                state_claim_ids=state_ids,
                transition_claim_ids=transition_ids,
                path=f"{path}.route_assignments[{index}]",
            )
            for index, (assignment, subject) in enumerate(zip(assignments_raw, subjects))
        ]
        require(assignments_raw == assignments,
                f"{path}.route_assignments: canonical order/digests required")
        destroyed = [assignment["destroyed_resource_key"] for assignment in assignments]
        witnesses = [assignment["fate_claim_id"] for assignment in assignments]
        require(len(destroyed) == len(set(destroyed)),
                f"{path}: destroyed resource reused within row")
        require(len(witnesses) == len(set(witnesses)),
                f"{path}: fate witness reused within row")
        require(locator == f"routed-credit-semantics-registry://{row_id}",
                f"{path}.verification_locator: canonical row URI required")
        require(isinstance(digest, str) and digest, f"{path}.verification_digest: required")
    output = {
        "row_id": row_id,
        "parent_global_state_id": row["parent_global_state_id"],
        "selected_slot_id": row["selected_slot_id"],
        "active_row_record_sha256": row["active_row_record_sha256"],
        "resource_model_record_sha256": resource_record["resource_model_record_sha256"],
        "credit_subjects": subjects,
        "credit_subjects_sha256": catalogue.canonical_digest(subjects),
        "status": status,
        "route_assignments": assignments,
        "verification_locator": locator,
        "verification_digest": digest,
        "note": note,
    }
    output["routed_credit_semantic_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    t06_certificate = certificate.get("candidate_policy_frontier_certificate")
    raw_active_rows = certificate.get("active_row_records")
    raw_active_artifacts = certificate.get("active_row_artifacts")
    raw_resource_records = certificate.get("destroyed_resource_model_records")
    raw_resource_artifacts = certificate.get("destroyed_resource_model_artifacts")
    raw_credit_records = certificate.get("routed_credit_semantic_records")
    raw_credit_artifacts = certificate.get("routed_credit_semantic_artifacts")
    require(isinstance(t06_certificate, dict),
            "candidate_policy_frontier_certificate: expected object")
    for name, value in (
        ("active_row_records", raw_active_rows),
        ("active_row_artifacts", raw_active_artifacts),
        ("destroyed_resource_model_records", raw_resource_records),
        ("destroyed_resource_model_artifacts", raw_resource_artifacts),
        ("routed_credit_semantic_records", raw_credit_records),
        ("routed_credit_semantic_artifacts", raw_credit_artifacts),
    ):
        require(isinstance(value, list), f"{name}: expected list")

    t06_frontier.validate_certificate(t06_certificate)
    t06_exact = t06_frontier.exact_certificate(t06_certificate)
    t05_certificate = t06_certificate["geometry_selector_frontier_certificate"]
    t07_certificate = t06_certificate["fate_transition_state_frontier_certificate"]
    t05_frontier.validate_certificate(t05_certificate)
    t07_frontier.validate_certificate(t07_certificate)
    t05_exact = t05_frontier.exact_certificate(t05_certificate)
    t07_exact = t07_frontier.exact_certificate(t07_certificate)
    t04_certificate = t05_certificate["block_interface_population_frontier_certificate"]
    require(
        t04_certificate["certificate_sha256"]
        == t07_certificate["block_interface_population_frontier_certificate"]["certificate_sha256"],
        "T05 and T07 use different T04 certificates",
    )
    t04_frontier.validate_certificate(t04_certificate)
    t04_exact = t04_frontier.exact_certificate(t04_certificate)
    t03_certificate = t04_certificate["slot_candidate_population_frontier_certificate"]
    t03_frontier.validate_certificate(t03_certificate)
    t03_exact = t03_frontier.exact_certificate(t03_certificate)

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

    payload_by_slot = {
        payload["slot_id"]: payload for payload in t03_exact["slot_population_payloads"]
    }
    semantic_by_slot = {
        item["slot_id"]: item
        for item in t07_exact["slot_fate_transition_state_semantic_certificates"]
    }
    t07_artifact_by_slot = {
        item["slot_id"]: item["artifact_id"]
        for item in t07_exact["slot_fate_transition_state_artifacts"]
    }
    geometry_wrapper_by_slot = {
        item["slot_id"]: item
        for item in t05_exact["slot_linked_operation_selector_certificates"]
    }
    t05_artifact_by_slot = {
        item["slot_id"]: item["artifact_id"]
        for item in t05_exact["slot_geometry_selector_artifacts"]
    }
    t04_artifact_by_unit = {
        item["unit_id"]: item["artifact_id"]
        for item in t04_exact["block_interface_population_artifacts"]
    }
    units_by_global_parent: dict[str, list[str]] = {}
    for unit in t04_exact["expected_block_interface_population_units"]:
        for binding in unit["parent_bindings"]:
            units_by_global_parent.setdefault(
                binding["parent_global_state_id"], []
            ).append(unit["unit_id"])
    for parent in units_by_global_parent:
        units_by_global_parent[parent] = sorted(set(units_by_global_parent[parent]))

    applications = t06_exact["candidate_policy_application_records"]
    application_artifact_by_parent = {
        item["parent_global_state_id"]: item["artifact_id"]
        for item in t06_exact["candidate_policy_application_artifacts"]
    }
    require(len(raw_active_rows) == len(applications),
            "active_row_records: exact T06 application cardinality required")
    require(
        [record.get("parent_global_state_id") for record in raw_active_rows]
        == [record["parent_global_state_id"] for record in applications],
        "active_row_records: canonical global-parent order required",
    )
    active_rows = []
    for index, (raw, application) in enumerate(zip(raw_active_rows, applications)):
        slot_id = application["applied_slot_id"]
        active_rows.append(
            exact_active_row_record(
                raw,
                application=application,
                payload=payload_by_slot.get(slot_id),
                semantic=semantic_by_slot.get(slot_id),
                using_unit_ids=units_by_global_parent.get(
                    application["parent_global_state_id"], []
                ),
                path=f"active_row_records[{index}]",
            )
        )
    require(raw_active_rows == active_rows,
            "active_row_records: canonical records/digests required")

    active_artifact_groups = {row["row_id"]: [] for row in active_rows}
    for item in raw_active_artifacts:
        require(isinstance(item, dict), "active_row_artifacts: expected objects")
        row_id = item.get("row_id")
        require(row_id in active_artifact_groups,
                f"active row artifact: unknown row {row_id}")
        active_artifact_groups[row_id].append(item)
    active_artifacts: list[dict[str, Any]] = []
    active_artifact_by_row: dict[str, str] = {}
    active_bundles = []
    for row in active_rows:
        group = active_artifact_groups[row["row_id"]]
        artifact_list: list[dict[str, Any]] = []
        if row["status"] == "open":
            require(not group, f"row {row['row_id']}: open active row cannot contain artifact")
        else:
            require(len(group) == 1,
                    f"row {row['row_id']}: exactly one active-row artifact required")
            parent = row["parent_global_state_id"]
            slot_id = row["selected_slot_id"]
            require(parent in application_artifact_by_parent,
                    f"row {row['row_id']}: T06 application artifact missing")
            require(slot_id in t07_artifact_by_slot,
                    f"row {row['row_id']}: T07 semantic artifact missing")
            expected_t04_support = sorted(
                t04_artifact_by_unit[unit_id]
                for unit_id in row["using_t04_unit_ids"]
                if unit_id in t04_artifact_by_unit
            )
            require(len(expected_t04_support) == len(row["using_t04_unit_ids"]),
                    f"row {row['row_id']}: every using T04 unit must be proved")
            artifact = fixed_artifact(
                group[0],
                identity={"row_id": row["row_id"]},
                required_kind=ACTIVE_ROW_ARTIFACT_KIND,
                bound_digest_name="active_row_record_sha256",
                bound_digest=row["active_row_record_sha256"],
                expected_support_fields={
                    "support_t06_application_artifact_ids": [
                        application_artifact_by_parent[parent]
                    ],
                    "support_t04_population_artifact_ids": expected_t04_support,
                    "support_t07_semantic_artifact_ids": [t07_artifact_by_slot[slot_id]],
                },
                output_digest_name="active_row_artifact_sha256",
                path=f"active_row_artifact[{row['row_id']}]",
            )
            active_artifacts.append(artifact)
            active_artifact_by_row[row["row_id"]] = artifact["artifact_id"]
            artifact_list = [artifact]
            proof_bundle = {
                "row_id": row["row_id"],
                "active_row_record_sha256": row["active_row_record_sha256"],
                "active_row_artifact_sha256": artifact["active_row_artifact_sha256"],
                "support_t06_application_artifact_ids": artifact[
                    "support_t06_application_artifact_ids"
                ],
                "support_t04_population_artifact_ids": artifact[
                    "support_t04_population_artifact_ids"
                ],
                "support_t07_semantic_artifact_ids": artifact[
                    "support_t07_semantic_artifact_ids"
                ],
            }
            proof_bundle["active_row_proof_bundle_sha256"] = catalogue.canonical_digest(
                proof_bundle
            )
            require(
                row["verification_digest"] == proof_bundle["active_row_proof_bundle_sha256"],
                f"row {row['row_id']}: verification digest does not bind active-row proof bundle",
            )
        bundle = {
            "row_id": row["row_id"],
            "status": row["status"],
            "artifacts_sha256": catalogue.canonical_digest(artifact_list),
        }
        bundle["active_row_bundle_sha256"] = catalogue.canonical_digest(bundle)
        active_bundles.append(bundle)
    require(raw_active_artifacts == active_artifacts,
            "active_row_artifacts: canonical order/content required")

    active_counts = Counter(row["status"] for row in active_rows)
    t06_ready = int(t06_exact["claims"]["candidate_policy_correct_ready"])
    t08_ready = int(
        t06_ready
        and active_counts["proved"] == len(active_rows)
        and len(active_artifacts) == len(active_rows)
    )
    t08_bank = {
        "candidate_policy_proof_bank_sha256": t06_exact["claims"][
            "candidate_policy_proof_bank_sha256"
        ],
        "t06_application_records_sha256": t06_exact["claims"][
            "application_policy_records_sha256"
        ],
        "t06_application_artifacts_sha256": t06_exact["claims"][
            "application_policy_artifacts_sha256"
        ],
        "t04_expected_units_sha256": t04_exact["claims"][
            "expected_population_units_sha256"
        ],
        "t04_population_artifacts_sha256": t04_exact["claims"][
            "block_interface_population_artifacts_sha256"
        ],
        "t07_semantic_certificates_sha256": t07_exact["claims"][
            "slot_semantic_certificates_sha256"
        ],
        "t07_semantic_artifacts_sha256": t07_exact["claims"][
            "slot_semantic_artifacts_sha256"
        ],
        "active_row_records_sha256": catalogue.canonical_digest(active_rows),
        "active_row_artifacts_sha256": catalogue.canonical_digest(active_artifacts),
        "active_row_bundles_sha256": catalogue.canonical_digest(active_bundles),
    }
    t08_bank["active_row_family_proof_bank_sha256"] = catalogue.canonical_digest(t08_bank)

    require(len(raw_resource_records) == len(active_rows),
            "destroyed_resource_model_records: exact active-row cardinality required")
    require(
        [record.get("row_id") for record in raw_resource_records]
        == [row["row_id"] for row in active_rows],
        "destroyed_resource_model_records: canonical row order required",
    )
    literal_resources_by_row: dict[str, list[dict[str, Any]]] = {}
    resource_records = []
    for index, (raw, row) in enumerate(zip(raw_resource_records, active_rows)):
        resources = exact_literal_resources(
            row=row,
            geometry_wrapper=geometry_wrapper_by_slot.get(row["selected_slot_id"]),
        )
        literal_resources_by_row[row["row_id"]] = resources
        resource_records.append(
            exact_resource_model_record(
                raw,
                row=row,
                resources=resources,
                path=f"destroyed_resource_model_records[{index}]",
            )
        )
    require(raw_resource_records == resource_records,
            "destroyed_resource_model_records: canonical records/digests required")

    resource_artifact_groups = {row["row_id"]: [] for row in active_rows}
    for item in raw_resource_artifacts:
        require(isinstance(item, dict),
                "destroyed_resource_model_artifacts: expected objects")
        row_id = item.get("row_id")
        require(row_id in resource_artifact_groups,
                f"resource-model artifact: unknown row {row_id}")
        resource_artifact_groups[row_id].append(item)
    resource_artifacts: list[dict[str, Any]] = []
    resource_artifact_by_row: dict[str, str] = {}
    resource_bundles = []
    for row, record in zip(active_rows, resource_records):
        group = resource_artifact_groups[row["row_id"]]
        artifact_list: list[dict[str, Any]] = []
        if record["status"] == "open":
            require(not group,
                    f"row {row['row_id']}: open resource model cannot contain artifact")
        else:
            require(len(group) == 1,
                    f"row {row['row_id']}: exactly one resource-model artifact required")
            require(row["row_id"] in active_artifact_by_row,
                    f"row {row['row_id']}: active-row artifact missing")
            slot_id = row["selected_slot_id"]
            require(slot_id in t05_artifact_by_slot,
                    f"row {row['row_id']}: T05 geometry artifact missing")
            artifact = fixed_artifact(
                group[0],
                identity={"row_id": row["row_id"]},
                required_kind=RESOURCE_ROW_ARTIFACT_KIND,
                bound_digest_name="resource_model_record_sha256",
                bound_digest=record["resource_model_record_sha256"],
                expected_support_fields={
                    "support_t08_active_row_artifact_ids": [active_artifact_by_row[row["row_id"]]],
                    "support_t05_geometry_artifact_ids": [t05_artifact_by_slot[slot_id]],
                },
                output_digest_name="destroyed_resource_model_artifact_sha256",
                path=f"destroyed_resource_model_artifact[{row['row_id']}]",
            )
            resource_artifacts.append(artifact)
            resource_artifact_by_row[row["row_id"]] = artifact["artifact_id"]
            artifact_list = [artifact]
            proof_bundle = {
                "row_id": row["row_id"],
                "resource_model_record_sha256": record["resource_model_record_sha256"],
                "destroyed_resource_model_artifact_sha256": artifact[
                    "destroyed_resource_model_artifact_sha256"
                ],
                "support_t08_active_row_artifact_ids": artifact[
                    "support_t08_active_row_artifact_ids"
                ],
                "support_t05_geometry_artifact_ids": artifact[
                    "support_t05_geometry_artifact_ids"
                ],
            }
            proof_bundle["destroyed_resource_model_proof_bundle_sha256"] = (
                catalogue.canonical_digest(proof_bundle)
            )
            require(
                record["verification_digest"]
                == proof_bundle["destroyed_resource_model_proof_bundle_sha256"],
                f"row {row['row_id']}: digest does not bind resource-model proof bundle",
            )
        bundle = {
            "row_id": row["row_id"],
            "status": record["status"],
            "artifacts_sha256": catalogue.canonical_digest(artifact_list),
        }
        bundle["destroyed_resource_model_bundle_sha256"] = catalogue.canonical_digest(bundle)
        resource_bundles.append(bundle)
    require(raw_resource_artifacts == resource_artifacts,
            "destroyed_resource_model_artifacts: canonical order/content required")

    row_ids = [row["row_id"] for row in active_rows]
    resource_sets = {
        row_id: {record["resource_key"] for record in literal_resources_by_row[row_id]}
        for row_id in row_ids
    }
    overlap_edges: set[tuple[str, str]] = set()
    for index, left in enumerate(row_ids):
        for right in row_ids[index + 1:]:
            if resource_sets[left] & resource_sets[right]:
                overlap_edges.add((left, right))
    components = connected_components(row_ids, overlap_edges)
    scope_records = []
    for component in components:
        keys = sorted(set().union(*(resource_sets[row_id] for row_id in component)))
        core = {"row_ids": component, "literal_resource_keys": keys}
        scope_id = f"scope-{catalogue.canonical_digest(core)[:24]}"
        record = {
            "derived_scope_id": scope_id,
            "row_ids": component,
            "literal_resource_keys": keys,
            "rows": len(component),
            "literal_resources": len(keys),
        }
        record["derived_resource_scope_sha256"] = catalogue.canonical_digest(record)
        scope_records.append(record)
    scope_records.sort(key=lambda record: record["derived_scope_id"])

    resource_counts = Counter(record["status"] for record in resource_records)
    t05_ready = int(t05_exact["claims"]["geometry_selector_correct_ready"])
    t09_ready = int(
        t08_ready
        and t05_ready
        and resource_counts["proved"] == len(resource_records)
        and len(resource_artifacts) == len(resource_records)
    )
    literal_resource_records = [
        resource
        for row_id in row_ids
        for resource in literal_resources_by_row[row_id]
    ]
    t09_bank = {
        "active_row_family_proof_bank_sha256": t08_bank[
            "active_row_family_proof_bank_sha256"
        ],
        "geometry_proof_bank_sha256": t05_exact["claims"]["geometry_proof_bank_sha256"],
        "active_row_records_sha256": catalogue.canonical_digest(active_rows),
        "destroyed_resource_model_records_sha256": catalogue.canonical_digest(resource_records),
        "literal_resource_records_sha256": catalogue.canonical_digest(literal_resource_records),
        "resource_overlap_edges_sha256": catalogue.canonical_digest(
            [list(edge) for edge in sorted(overlap_edges)]
        ),
        "derived_resource_scopes_sha256": catalogue.canonical_digest(scope_records),
        "destroyed_resource_model_artifacts_sha256": catalogue.canonical_digest(
            resource_artifacts
        ),
        "destroyed_resource_model_bundles_sha256": catalogue.canonical_digest(
            resource_bundles
        ),
    }
    t09_bank["destroyed_resource_model_proof_bank_sha256"] = catalogue.canonical_digest(t09_bank)

    resource_record_by_row = {record["row_id"]: record for record in resource_records}
    require(len(raw_credit_records) == len(active_rows),
            "routed_credit_semantic_records: exact active-row cardinality required")
    require(
        [record.get("row_id") for record in raw_credit_records]
        == [row["row_id"] for row in active_rows],
        "routed_credit_semantic_records: canonical row order required",
    )
    credit_records = []
    for index, (raw, row) in enumerate(zip(raw_credit_records, active_rows)):
        credit_records.append(
            exact_credit_semantic_record(
                raw,
                row=row,
                resource_record=resource_record_by_row[row["row_id"]],
                subjects=credit_subjects(row, payload_by_slot.get(row["selected_slot_id"])),
                semantic=semantic_by_slot.get(row["selected_slot_id"]),
                path=f"routed_credit_semantic_records[{index}]",
            )
        )
    require(raw_credit_records == credit_records,
            "routed_credit_semantic_records: canonical records/digests required")

    credit_artifact_groups = {row["row_id"]: [] for row in active_rows}
    for item in raw_credit_artifacts:
        require(isinstance(item, dict),
                "routed_credit_semantic_artifacts: expected objects")
        row_id = item.get("row_id")
        require(row_id in credit_artifact_groups,
                f"routed-credit artifact: unknown row {row_id}")
        credit_artifact_groups[row_id].append(item)
    credit_artifacts: list[dict[str, Any]] = []
    credit_bundles = []
    all_assignments = []
    for row, record in zip(active_rows, credit_records):
        group = credit_artifact_groups[row["row_id"]]
        artifact_list: list[dict[str, Any]] = []
        if record["status"] == "open":
            require(not group,
                    f"row {row['row_id']}: open credit semantics cannot contain artifact")
        else:
            require(len(group) == 1,
                    f"row {row['row_id']}: exactly one routed-credit artifact required")
            require(row["row_id"] in active_artifact_by_row,
                    f"row {row['row_id']}: active-row artifact missing")
            require(row["row_id"] in resource_artifact_by_row,
                    f"row {row['row_id']}: resource-model artifact missing")
            slot_id = row["selected_slot_id"]
            require(slot_id in t07_artifact_by_slot,
                    f"row {row['row_id']}: T07 semantic artifact missing")
            artifact = fixed_artifact(
                group[0],
                identity={"row_id": row["row_id"]},
                required_kind=CREDIT_ROW_ARTIFACT_KIND,
                bound_digest_name="routed_credit_semantic_record_sha256",
                bound_digest=record["routed_credit_semantic_record_sha256"],
                expected_support_fields={
                    "support_t08_active_row_artifact_ids": [active_artifact_by_row[row["row_id"]]],
                    "support_t09_resource_model_artifact_ids": [resource_artifact_by_row[row["row_id"]]],
                    "support_t07_semantic_artifact_ids": [t07_artifact_by_slot[slot_id]],
                },
                output_digest_name="routed_credit_semantic_artifact_sha256",
                path=f"routed_credit_semantic_artifact[{row['row_id']}]",
            )
            credit_artifacts.append(artifact)
            artifact_list = [artifact]
            proof_bundle = {
                "row_id": row["row_id"],
                "routed_credit_semantic_record_sha256": record[
                    "routed_credit_semantic_record_sha256"
                ],
                "routed_credit_semantic_artifact_sha256": artifact[
                    "routed_credit_semantic_artifact_sha256"
                ],
                "support_t08_active_row_artifact_ids": artifact[
                    "support_t08_active_row_artifact_ids"
                ],
                "support_t09_resource_model_artifact_ids": artifact[
                    "support_t09_resource_model_artifact_ids"
                ],
                "support_t07_semantic_artifact_ids": artifact[
                    "support_t07_semantic_artifact_ids"
                ],
            }
            proof_bundle["routed_credit_semantic_proof_bundle_sha256"] = (
                catalogue.canonical_digest(proof_bundle)
            )
            require(
                record["verification_digest"]
                == proof_bundle["routed_credit_semantic_proof_bundle_sha256"],
                f"row {row['row_id']}: digest does not bind routed-credit proof bundle",
            )
            all_assignments.extend(record["route_assignments"])
        bundle = {
            "row_id": row["row_id"],
            "status": record["status"],
            "artifacts_sha256": catalogue.canonical_digest(artifact_list),
        }
        bundle["routed_credit_semantic_bundle_sha256"] = catalogue.canonical_digest(bundle)
        credit_bundles.append(bundle)
    require(raw_credit_artifacts == credit_artifacts,
            "routed_credit_semantic_artifacts: canonical order/content required")

    destroyed_global = [assignment["destroyed_resource_key"] for assignment in all_assignments]
    obligation_global = [
        catalogue.canonical_digest({
            "fate_claim_id": assignment["fate_claim_id"],
            "state_claim_id": assignment["state_claim_id"],
            "child_state_id": assignment["child_state_id"],
        })
        for assignment in all_assignments
    ]
    require(len(destroyed_global) == len(set(destroyed_global)),
            "routed credits: destroyed resource reused across active rows")
    require(len(obligation_global) == len(set(obligation_global)),
            "routed credits: child-bearing witness obligation reused across active rows")

    credit_counts = Counter(record["status"] for record in credit_records)
    t07_ready = int(t07_exact["claims"]["fate_transition_state_semantics_ready"])
    t10_ready = int(
        t09_ready
        and t07_ready
        and credit_counts["proved"] == len(credit_records)
        and len(credit_artifacts) == len(credit_records)
    )
    t10_bank = {
        "destroyed_resource_model_proof_bank_sha256": t09_bank[
            "destroyed_resource_model_proof_bank_sha256"
        ],
        "state_semantics_proof_bank_sha256": t07_exact["claims"][
            "state_semantics_proof_bank_sha256"
        ],
        "transition_proof_bank_sha256": t07_exact["claims"][
            "transition_proof_bank_sha256"
        ],
        "routed_credit_semantic_records_sha256": catalogue.canonical_digest(credit_records),
        "routed_credit_assignments_sha256": catalogue.canonical_digest(all_assignments),
        "routed_credit_semantic_artifacts_sha256": catalogue.canonical_digest(credit_artifacts),
        "routed_credit_semantic_bundles_sha256": catalogue.canonical_digest(credit_bundles),
        "global_destroyed_resource_keys_sha256": catalogue.canonical_digest(sorted(destroyed_global)),
        "global_obligation_keys_sha256": catalogue.canonical_digest(sorted(obligation_global)),
    }
    t10_bank["routed_credit_semantics_proof_bank_sha256"] = catalogue.canonical_digest(t10_bank)

    closure_by_id = {
        record["obligation_id"]: record
        for record in closure_exact["obligation_closure_records"]
    }
    readiness_by_obligation = {
        "ACTIVE_ROW_FAMILY_EXHAUSTIVE": t08_ready,
        "DESTROYED_RESOURCE_MODEL_EXHAUSTIVE": t09_ready,
        "CREDIT_ROUTING_SEMANTIC": t10_ready,
    }
    for obligation_id, readiness in readiness_by_obligation.items():
        require(
            int(closure_by_id[obligation_id]["closed"]) == readiness,
            f"{obligation_id} closure disagrees with exact transition-resource bank",
        )

    obligation_artifact_by_obligation = {
        obligation_id: [
            artifact
            for artifact in obligation_exact["proof_artifacts"]
            if artifact["obligation_id"] == obligation_id
        ]
        for obligation_id in readiness_by_obligation
    }
    dependency_ids = {
        "ACTIVE_ROW_FAMILY_EXHAUSTIVE": {"CANDIDATE_POLICY_CORRECT"},
        "DESTROYED_RESOURCE_MODEL_EXHAUSTIVE": {
            "ACTIVE_ROW_FAMILY_EXHAUSTIVE",
            "GEOMETRY_SELECTOR_CORRECT",
        },
        "CREDIT_ROUTING_SEMANTIC": {
            "DESTROYED_RESOURCE_MODEL_EXHAUSTIVE",
            "FATE_TRANSITION_STATE_SEMANTICS",
        },
    }
    expected_obligation_kind_locator_digest = {
        "ACTIVE_ROW_FAMILY_EXHAUSTIVE": (
            "active-family-exhaustiveness-proof",
            T08_OBLIGATION_LOCATOR,
            t08_bank["active_row_family_proof_bank_sha256"],
        ),
        "DESTROYED_RESOURCE_MODEL_EXHAUSTIVE": (
            "resource-model-proof",
            T09_OBLIGATION_LOCATOR,
            t09_bank["destroyed_resource_model_proof_bank_sha256"],
        ),
        "CREDIT_ROUTING_SEMANTIC": (
            "credit-routing-proof",
            T10_OBLIGATION_LOCATOR,
            t10_bank["routed_credit_semantics_proof_bank_sha256"],
        ),
    }
    all_obligation_artifacts = obligation_exact["proof_artifacts"]
    for obligation_id, readiness in readiness_by_obligation.items():
        records = obligation_artifact_by_obligation[obligation_id]
        require(len(records) == (1 if readiness else 0),
                f"{obligation_id} artifact presence disagrees with readiness")
        if readiness:
            artifact = records[0]
            kind, locator, digest = expected_obligation_kind_locator_digest[obligation_id]
            require(artifact["artifact_kind"] == kind,
                    f"{obligation_id}: wrong obligation artifact kind")
            require(artifact["locator"] == locator,
                    f"{obligation_id}: obligation locator mismatch")
            require(artifact["digest"] == digest,
                    f"{obligation_id}: obligation digest mismatch")
            expected_support = sorted(
                item["artifact_id"]
                for item in all_obligation_artifacts
                if item["obligation_id"] in dependency_ids[obligation_id]
            )
            require(artifact["support_artifact_ids"] == expected_support,
                    f"{obligation_id}: exact immediate obligation support required")

    target_results = {
        record["target_id"]: record for record in atomic_exact["target_result_records"]
    }
    target_readiness = {
        "T08_ACTIVE_ROW_FAMILY": t08_ready,
        "T09_RESOURCE_MODEL": t09_ready,
        "T10_CREDIT_ROUTING": t10_ready,
    }
    for target_id, readiness in target_readiness.items():
        require(
            int(target_results[target_id]["effective_target_complete"]) == readiness,
            f"{target_id} completion disagrees with exact transition-resource bank",
        )
    target_artifact_by_id = {
        artifact["target_id"]: artifact
        for artifact in target_exact["atomic_target_artifacts"]
    }
    target_specs = {
        "T08_ACTIVE_ROW_FAMILY": (
            "active-family-proof",
            T08_TARGET_LOCATOR,
            t08_bank["active_row_family_proof_bank_sha256"],
        ),
        "T09_RESOURCE_MODEL": (
            "resource-model-proof",
            T09_TARGET_LOCATOR,
            t09_bank["destroyed_resource_model_proof_bank_sha256"],
        ),
        "T10_CREDIT_ROUTING": (
            "credit-routing-proof",
            T10_TARGET_LOCATOR,
            t10_bank["routed_credit_semantics_proof_bank_sha256"],
        ),
    }
    for target_id, readiness in target_readiness.items():
        artifact = target_artifact_by_id.get(target_id)
        if readiness:
            require(artifact is not None, f"completed {target_id} missing target artifact")
            kind, locator, digest = target_specs[target_id]
            require(artifact["artifact_kind"] == kind, f"{target_id}: wrong target artifact kind")
            require(artifact["proof_locator"] == locator, f"{target_id}: target locator mismatch")
            require(artifact["proof_digest"] == digest, f"{target_id}: target digest mismatch")
        else:
            require(artifact is None, f"open {target_id} cannot contain target artifact")

    all_internal_artifact_ids = [
        artifact["artifact_id"]
        for artifact in active_artifacts + resource_artifacts + credit_artifacts
    ]
    require(len(all_internal_artifact_ids) == len(set(all_internal_artifact_ids)),
            "transition-resource artifacts: duplicate artifact_id")

    claims = {
        "expected_active_rows": len(active_rows),
        "open_active_rows": active_counts["open"],
        "proved_active_rows": active_counts["proved"],
        "literal_destroyed_resources": len(literal_resource_records),
        "resource_overlap_edges": len(overlap_edges),
        "derived_resource_scopes": len(scope_records),
        "open_resource_models": resource_counts["open"],
        "proved_resource_models": resource_counts["proved"],
        "literal_routed_credit_subjects": sum(
            len(record["credit_subjects"]) for record in credit_records
        ),
        "routed_credit_assignments": len(all_assignments),
        "open_credit_semantic_rows": credit_counts["open"],
        "proved_credit_semantic_rows": credit_counts["proved"],
        "t06_candidate_policy_ready": t06_ready,
        "t05_geometry_selector_ready": t05_ready,
        "t07_fate_transition_state_ready": t07_ready,
        "t08_active_row_family_ready": t08_ready,
        "t09_destroyed_resource_model_ready": t09_ready,
        "t10_routed_credit_semantics_ready": t10_ready,
        "exact_t02_application_active_row_census": 1,
        "exact_t06_winner_to_active_row_binding": 1,
        "exact_literal_destroyed_resource_reconstruction": 1,
        "exact_resource_overlap_scope_partition": 1,
        "exact_literal_routed_credit_subject_coverage": 1,
        "global_destroyed_resource_injectivity": 1,
        "global_child_obligation_injectivity": 1,
        "noncircular_t08_t09_t10_bank_binding": 1,
        "all_n_proved_by_checker": 0,
        "open_active_row_ids": [row["row_id"] for row in active_rows if row["status"] == "open"],
        "open_resource_model_row_ids": [
            row["row_id"] for row in resource_records if row["status"] == "open"
        ],
        "open_credit_semantic_row_ids": [
            row["row_id"] for row in credit_records if row["status"] == "open"
        ],
        "active_row_records_sha256": catalogue.canonical_digest(active_rows),
        "active_row_artifacts_sha256": catalogue.canonical_digest(active_artifacts),
        "active_row_family_proof_bank_sha256": t08_bank[
            "active_row_family_proof_bank_sha256"
        ],
        "destroyed_resource_model_records_sha256": catalogue.canonical_digest(resource_records),
        "literal_resource_records_sha256": catalogue.canonical_digest(literal_resource_records),
        "derived_resource_scopes_sha256": catalogue.canonical_digest(scope_records),
        "destroyed_resource_model_artifacts_sha256": catalogue.canonical_digest(resource_artifacts),
        "destroyed_resource_model_proof_bank_sha256": t09_bank[
            "destroyed_resource_model_proof_bank_sha256"
        ],
        "routed_credit_semantic_records_sha256": catalogue.canonical_digest(credit_records),
        "routed_credit_semantic_artifacts_sha256": catalogue.canonical_digest(credit_artifacts),
        "routed_credit_semantics_proof_bank_sha256": t10_bank[
            "routed_credit_semantics_proof_bank_sha256"
        ],
        "obligation_artifact_registry_sha256": obligation_certificate["certificate_sha256"],
        "atomic_target_artifact_registry_sha256": target_registry["certificate_sha256"],
    }
    return {
        "active_row_records": active_rows,
        "active_row_artifacts": active_artifacts,
        "active_row_bundle_records": active_bundles,
        "active_row_family_proof_bank": t08_bank,
        "destroyed_resource_model_records": resource_records,
        "literal_destroyed_resource_records": literal_resource_records,
        "resource_overlap_edges": [list(edge) for edge in sorted(overlap_edges)],
        "derived_resource_scope_records": scope_records,
        "destroyed_resource_model_artifacts": resource_artifacts,
        "destroyed_resource_model_bundle_records": resource_bundles,
        "destroyed_resource_model_proof_bank": t09_bank,
        "routed_credit_semantic_records": credit_records,
        "routed_credit_semantic_artifacts": credit_artifacts,
        "routed_credit_semantic_bundle_records": credit_bundles,
        "routed_credit_semantics_proof_bank": t10_bank,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in (
        "active_row_records",
        "active_row_artifacts",
        "active_row_bundle_records",
        "active_row_family_proof_bank",
        "destroyed_resource_model_records",
        "literal_destroyed_resource_records",
        "resource_overlap_edges",
        "derived_resource_scope_records",
        "destroyed_resource_model_artifacts",
        "destroyed_resource_model_bundle_records",
        "destroyed_resource_model_proof_bank",
        "routed_credit_semantic_records",
        "routed_credit_semantic_artifacts",
        "routed_credit_semantic_bundle_records",
        "routed_credit_semantics_proof_bank",
        "claims",
    ):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {
        "rows": claims["expected_active_rows"],
        "resources": claims["literal_destroyed_resources"],
        "credits": claims["literal_routed_credit_subjects"],
        "t08": claims["t08_active_row_family_ready"],
        "t09": claims["t09_destroyed_resource_model_ready"],
        "t10": claims["t10_routed_credit_semantics_ready"],
        "all_n": claims["all_n_proved_by_checker"],
    }


def build_certificate(
    t06_certificate: dict[str, Any],
    active_rows: list[dict[str, Any]],
    active_artifacts: list[dict[str, Any]],
    resource_records: list[dict[str, Any]],
    resource_artifacts: list[dict[str, Any]],
    credit_records: list[dict[str, Any]],
    credit_artifacts: list[dict[str, Any]],
) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "candidate_policy_frontier_certificate": t06_certificate,
        "active_row_records": active_rows,
        "active_row_artifacts": active_artifacts,
        "destroyed_resource_model_records": resource_records,
        "destroyed_resource_model_artifacts": resource_artifacts,
        "routed_credit_semantic_records": credit_records,
        "routed_credit_semantic_artifacts": credit_artifacts,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: check_prime_power_transition_resource_frontier.py certificate.json"
        )
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
