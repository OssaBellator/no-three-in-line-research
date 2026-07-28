#!/usr/bin/env python3
"""Validate and synchronize the exact T11 recurrent-block closure proof bank.

T04 fixes the skeleton-derived recurrent-block census, T06 fixes the selected operation for every
parent, and T10 fixes the selected active rows and routed-credit semantics.  This checker requires one
common positive state-weight certificate for every expected recurrent block and bridges each row in
that certificate back to the exact T03/T05/T06/T10 data.

For a proved block the finite common-weight checker must establish exact parent coverage, primitive
positive weights, no recurrent exit, strong connectivity, and a positive margin on every row.  The
bridge additionally requires the common row's linked geometry, labelled vectors and complete row-load
table to equal the selected slot data, its minimum load to equal the T06 score, and its selected credit
vector to equal the unit-level T10 routed-credit subjects.

This is documentary proof infrastructure.  It validates finite identities, exact ancestry, support and
digest binding; it does not prove that the supplied recurrence or semantic statements are genuine and
permanently reports ``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import copy
import json
import math
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_all_n_implication_closure as closure
import check_prime_power_atomic_frontier_execution as atomic
import check_prime_power_atomic_target_artifact_registry as target_artifacts
import check_prime_power_block_interface_population_frontier as t04_frontier
import check_prime_power_candidate_policy_frontier as t06_frontier
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_common_recurrent_block_weights as common
import check_prime_power_geometry_selector_frontier_v2 as t05_frontier
import check_prime_power_labelled_recurrent_row_margin as row_margin
import check_prime_power_obligation_artifact_registry as obligation_artifacts
import check_prime_power_slot_candidate_population_frontier as t03_frontier
import check_prime_power_transition_resource_frontier as t10_frontier


class RecurrentBlockClosureFrontierError(ValueError):
    """Raised when the exact T11 recurrent-block closure bank is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RecurrentBlockClosureFrontierError(message)


COMMON_WEIGHT_ARTIFACT_KIND = "recurrent-block-common-weight-proof"
BLOCK_CLOSURE_ARTIFACT_KIND = "recurrent-block-closure-proof"
BLOCK_OBLIGATION_LOCATOR = (
    "recurrent-block-closure-frontier://CLOSED_STRICT_RECURRENT_BLOCKS/block-closure-proof"
)
WEIGHT_OBLIGATION_LOCATOR = (
    "recurrent-block-closure-frontier://CLOSED_STRICT_RECURRENT_BLOCKS/common-weight-proof"
)
T11_TARGET_LOCATOR = "recurrent-block-closure-frontier://T11_RECURRENT_BLOCK_CLOSURE"


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


def response_key(response: list[list[int]]) -> tuple[tuple[int, int], ...]:
    return row_margin.response_key(response)


def exact_block_record(
    raw: dict[str, Any],
    *,
    unit: dict[str, Any],
    active_rows: list[dict[str, Any]],
    t04_payload: dict[str, Any] | None,
    path: str,
) -> dict[str, Any]:
    block_id = unit["object_id"]
    unit_id = unit["unit_id"]
    parent_globals = [binding["parent_global_state_id"] for binding in unit["parent_bindings"]]
    active_ids = [row["row_id"] for row in active_rows]
    local_parents = sorted({row["local_parent_state_id"] for row in active_rows})
    require(raw.get("block_id") == block_id, f"{path}.block_id: mismatch")
    require(raw.get("unit_id") == unit_id, f"{path}.unit_id: mismatch")
    require(raw.get("unit_identity_sha256") == unit["unit_identity_sha256"],
            f"{path}.unit_identity_sha256: mismatch")
    require(raw.get("parent_global_state_ids") == parent_globals,
            f"{path}.parent_global_state_ids: exact parent bank required")
    require(raw.get("local_parent_state_ids") == local_parents,
            f"{path}.local_parent_state_ids: exact parent bank required")
    require(raw.get("active_row_ids") == active_ids,
            f"{path}.active_row_ids: exact active-row bank required")
    payload_sha = None if t04_payload is None else t04_payload[
        "block_interface_population_payload_sha256"
    ]
    require(raw.get("t04_population_payload_sha256") == payload_sha,
            f"{path}.t04_population_payload_sha256: mismatch")
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
        require(t04_payload is not None, f"{path}: proved block requires T04 population payload")
        require(
            locator == f"recurrent-block-closure-registry://{block_id}",
            f"{path}.verification_locator: canonical block URI required",
        )
        require(isinstance(digest, str) and digest, f"{path}.verification_digest: required")
    core = {
        "block_id": block_id,
        "unit_id": unit_id,
        "unit_identity_sha256": unit["unit_identity_sha256"],
        "parent_global_state_ids": parent_globals,
        "local_parent_state_ids": local_parents,
        "active_row_ids": active_ids,
        "t04_population_payload_sha256": payload_sha,
        "status": status,
        "verification_locator": locator,
        "note": note,
    }
    core_sha = catalogue.canonical_digest(core)
    output = {
        **core,
        "verification_digest": digest,
        "block_closure_record_core_sha256": core_sha,
    }
    output["block_closure_record_sha256"] = catalogue.canonical_digest(output)
    return output


def common_state_records(common_certificate: dict[str, Any]) -> list[dict[str, Any]]:
    states: dict[str, dict[str, Any]] = {}
    for route_certificate in common_certificate["routed_row_certificates"]:
        source = route_certificate["row_margin_certificate"]["linked_operation_certificate"][
            "linkage_certificate"
        ]["source_manifest"]
        for raw_state in source["states"]:
            core = common.state_core(raw_state)
            previous = states.get(core["id"])
            require(previous is None or previous == core,
                    f"common state {core['id']}: definition drift")
            states[core["id"]] = core
    return [states[state_id] for state_id in sorted(states)]


def exact_credit_unit_bank(
    *,
    credit_record: dict[str, Any],
    selected_response: list[list[int]],
    selected_credit_routes: dict[str, int],
    path: str,
) -> list[dict[str, Any]]:
    subjects = credit_record["credit_subjects"]
    assignments = credit_record["route_assignments"]
    require(len(subjects) == len(assignments), f"{path}: subject/assignment cardinality mismatch")
    selected_response_sha = catalogue.canonical_digest(selected_response)
    units: list[dict[str, Any]] = []
    indices_by_child: dict[str, list[int]] = {}
    for index, (subject, assignment) in enumerate(zip(subjects, assignments)):
        value = subject["credit_value"]
        require(isinstance(value, dict), f"{path}.credit_subjects[{index}]: unit object required")
        require(
            tuple(value) == ("child_state_id", "unit_index", "selected_response_sha256"),
            f"{path}.credit_subjects[{index}]: exact ordered unit keys required",
        )
        child = value["child_state_id"]
        unit_index = value["unit_index"]
        require(isinstance(child, str) and child, f"{path}.credit_subjects[{index}].child_state_id")
        require(type(unit_index) is int and unit_index >= 0,
                f"{path}.credit_subjects[{index}].unit_index")
        require(value["selected_response_sha256"] == selected_response_sha,
                f"{path}.credit_subjects[{index}]: selected response mismatch")
        require(assignment["child_state_id"] == child,
                f"{path}.route_assignments[{index}]: child differs from literal credit unit")
        indices_by_child.setdefault(child, []).append(unit_index)
        unit = {
            "credit_subject_sha256": subject["credit_subject_sha256"],
            "child_state_id": child,
            "unit_index": unit_index,
            "selected_response_sha256": selected_response_sha,
            "destroyed_resource_key": assignment["destroyed_resource_key"],
            "fate_claim_id": assignment["fate_claim_id"],
            "state_claim_id": assignment["state_claim_id"],
            "transition_claim_ids": list(assignment["transition_claim_ids"]),
        }
        unit["common_weight_credit_unit_sha256"] = catalogue.canonical_digest(unit)
        units.append(unit)
    require(set(indices_by_child) <= set(selected_credit_routes),
            f"{path}: routed credit child absent from common row")
    for child, expected_count in selected_credit_routes.items():
        indices = sorted(indices_by_child.get(child, []))
        require(indices == list(range(expected_count)),
                f"{path}: child {child} unit indices do not realize exact selected credit count")
    require(len(units) == sum(selected_credit_routes.values()),
            f"{path}: literal credit units do not equal selected routed-unit count")
    return units


def exact_row_bridge(
    *,
    block_id: str,
    active_row: dict[str, Any],
    route_certificate: dict[str, Any],
    payload: dict[str, Any],
    geometry_wrapper: dict[str, Any],
    score_record: dict[str, Any],
    credit_record: dict[str, Any],
    path: str,
) -> dict[str, Any]:
    row_certificate = route_certificate["row_margin_certificate"]
    row_exact = row_margin.exact_certificate(row_certificate)
    source = row_certificate["linked_operation_certificate"]["linkage_certificate"]["source_manifest"]
    claims = row_exact["claims"]
    require(source["parent"] == active_row["local_parent_state_id"],
            f"{path}: common row parent differs from active row")
    require(claims["fibre_id"] == payload["fibre_id"],
            f"{path}: common row fibre differs from selected T03 slot")
    require(
        row_certificate["linked_operation_certificate"]
        == geometry_wrapper["linked_operation_selector_certificate"],
        f"{path}: common row linked geometry differs from exact T05 certificate",
    )
    population_data = payload["population_data"]
    require(population_data["labelled_vectors"] == row_certificate[
        "weight_exposure_certificate"
    ]["response_vectors"], f"{path}: T03 labelled vectors differ from common row exposure")
    require(population_data["row_loads"] == row_exact["row_records"],
            f"{path}: T03 row-load table differs from common row arithmetic")
    require(score_record["status"] == "proved", f"{path}: T06 score remains open")
    require(claims["minimum_row_load"] == score_record["minimum_labelled_row_load"],
            f"{path}: T06 score differs from common-weight minimum row load")
    require(claims["maximum_margin"] > 0 and claims["strict_row"] == 1,
            f"{path}: common row is not strict")

    selected_key = response_key(claims["selected_response"])
    selected_credit_record = {
        response_key(record["response"]): record
        for record in row_exact["response_credit_records"]
    }.get(selected_key)
    require(selected_credit_record is not None, f"{path}: selected response lacks credit record")
    credit_units = exact_credit_unit_bank(
        credit_record=credit_record,
        selected_response=claims["selected_response"],
        selected_credit_routes=selected_credit_record["credit_routes"],
        path=path,
    )
    require(population_data["routed_credits"] == [subject["credit_value"] for subject in credit_record[
        "credit_subjects"
    ]], f"{path}: T03 routed-credit units differ from T10 subject bank")

    output = {
        "block_id": block_id,
        "row_id": active_row["row_id"],
        "parent_global_state_id": active_row["parent_global_state_id"],
        "local_parent_state_id": active_row["local_parent_state_id"],
        "selected_slot_id": active_row["selected_slot_id"],
        "fibre_id": payload["fibre_id"],
        "active_row_record_sha256": active_row["active_row_record_sha256"],
        "slot_population_payload_sha256": payload["slot_population_payload_sha256"],
        "t03_labelled_vectors_sha256": catalogue.canonical_digest(population_data["labelled_vectors"]),
        "t03_routed_credits_sha256": catalogue.canonical_digest(population_data["routed_credits"]),
        "t03_row_loads_sha256": catalogue.canonical_digest(population_data["row_loads"]),
        "t05_linked_geometry_certificate_sha256": geometry_wrapper[
            "linked_operation_selector_certificate_sha256"
        ],
        "candidate_score_record_sha256": score_record["candidate_score_record_sha256"],
        "routed_credit_semantic_record_sha256": credit_record[
            "routed_credit_semantic_record_sha256"
        ],
        "common_routing_certificate_sha256": route_certificate["certificate_sha256"],
        "common_row_margin_certificate_sha256": row_certificate["certificate_sha256"],
        "common_response_credit_records_sha256": claims["credit_records_sha256"],
        "common_row_records_sha256": claims["row_records_sha256"],
        "selected_response": copy.deepcopy(claims["selected_response"]),
        "selected_response_sha256": catalogue.canonical_digest(claims["selected_response"]),
        "selected_credit_routes": copy.deepcopy(selected_credit_record["credit_routes"]),
        "selected_routed_units": selected_credit_record["routed_units"],
        "common_weight_credit_units": credit_units,
        "common_weight_credit_units_sha256": catalogue.canonical_digest(credit_units),
        "minimum_row_load": claims["minimum_row_load"],
        "parent_weight": claims["parent_budget"],
        "strict_margin": claims["maximum_margin"],
    }
    output["common_weight_row_bridge_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_common_weight_record(
    raw: dict[str, Any],
    *,
    block_record: dict[str, Any],
    unit: dict[str, Any],
    t04_payload: dict[str, Any],
    active_rows: list[dict[str, Any]],
    payload_by_slot: dict[str, dict[str, Any]],
    geometry_by_slot: dict[str, dict[str, Any]],
    score_by_slot: dict[str, dict[str, Any]],
    credit_by_row: dict[str, dict[str, Any]],
    path: str,
) -> dict[str, Any]:
    block_id = block_record["block_id"]
    require(raw.get("block_id") == block_id, f"{path}.block_id: mismatch")
    require(raw.get("unit_id") == unit["unit_id"], f"{path}.unit_id: mismatch")
    common_certificate = raw.get("common_weight_certificate")
    require(isinstance(common_certificate, dict), f"{path}.common_weight_certificate: required")
    common.validate_certificate(common_certificate)
    common_exact = common.exact_certificate(common_certificate)
    claims = common_exact["claims"]
    require(claims["complete_strict_scc"] == 1,
            f"{path}: common certificate is not a complete strict recurrent SCC")
    require(claims["closed_recurrent_block"] == 1,
            f"{path}: recurrent block has an external recurrent exit")
    require(claims["strongly_connected"] == 1, f"{path}: recurrent block is not strongly connected")
    require(claims["all_rows_strict"] == 1 and claims["minimum_margin"] > 0,
            f"{path}: recurrent block has a non-strict row")
    require(common_certificate["scc_state_ids"] == block_record["local_parent_state_ids"],
            f"{path}: SCC state bank differs from exact active-row parents")

    states = common_state_records(common_certificate)
    require(t04_payload["population_data"]["local_states"] == states,
            f"{path}: T04 local-state population differs from common state registry")
    require(t04_payload["population_data"]["recurrent_rows"] == block_record["active_row_ids"],
            f"{path}: T04 recurrent-row population differs from exact active rows")

    route_by_parent: dict[str, dict[str, Any]] = {}
    for route_certificate in common_certificate["routed_row_certificates"]:
        source = route_certificate["row_margin_certificate"]["linked_operation_certificate"][
            "linkage_certificate"
        ]["source_manifest"]
        parent = source["parent"]
        require(parent not in route_by_parent, f"{path}: duplicate common row parent {parent}")
        route_by_parent[parent] = route_certificate
    require(set(route_by_parent) == set(block_record["local_parent_state_ids"]),
            f"{path}: common rows do not cover exact local parent set")

    bridges = []
    for index, active_row in enumerate(active_rows):
        local_parent = active_row["local_parent_state_id"]
        slot_id = active_row["selected_slot_id"]
        require(active_row["status"] == "proved", f"{path}: active row {active_row['row_id']} remains open")
        require(slot_id in payload_by_slot, f"{path}: selected slot {slot_id} lacks T03 payload")
        require(slot_id in geometry_by_slot, f"{path}: selected slot {slot_id} lacks T05 geometry")
        require(slot_id in score_by_slot, f"{path}: selected slot {slot_id} lacks T06 score")
        require(active_row["row_id"] in credit_by_row,
                f"{path}: active row {active_row['row_id']} lacks T10 credit record")
        credit_record = credit_by_row[active_row["row_id"]]
        require(credit_record["status"] == "proved",
                f"{path}: T10 credit semantics remains open for {active_row['row_id']}")
        bridge = exact_row_bridge(
            block_id=block_id,
            active_row=active_row,
            route_certificate=route_by_parent[local_parent],
            payload=payload_by_slot[slot_id],
            geometry_wrapper=geometry_by_slot[slot_id],
            score_record=score_by_slot[slot_id],
            credit_record=credit_record,
            path=f"{path}.row_bridge_records[{index}]",
        )
        binding = unit["parent_bindings"][index]
        require(binding["parent_global_state_id"] == active_row["parent_global_state_id"],
                f"{path}: T04 parent order differs from active-row order")
        require(binding["operation_slot_id"] == active_row["selected_slot_id"],
                f"{path}: T04 selected slot differs from active row")
        bridges.append(bridge)
    require(raw.get("row_bridge_records") == bridges,
            f"{path}.row_bridge_records: exact canonical bridge bank required")

    weights = common_exact["state_weights"]
    require(math.gcd(*(record["weight"] for record in weights)) == 1,
            f"{path}: common state-weight vector is not primitive")
    output = {
        "block_id": block_id,
        "unit_id": unit["unit_id"],
        "t04_population_payload_sha256": t04_payload[
            "block_interface_population_payload_sha256"
        ],
        "common_weight_certificate": common_certificate,
        "common_weight_certificate_sha256": common_certificate["certificate_sha256"],
        "common_state_records": states,
        "common_state_records_sha256": catalogue.canonical_digest(states),
        "state_weights": weights,
        "state_weights_sha256": claims["weights_sha256"],
        "row_bridge_records": bridges,
        "row_bridge_records_sha256": catalogue.canonical_digest(bridges),
        "recurrent_edges": copy.deepcopy(claims["recurrent_edges"]),
        "external_recurrent_edge_records": copy.deepcopy(
            claims["external_recurrent_edge_records"]
        ),
        "nonrecurrent_exit_edge_records": copy.deepcopy(claims["exit_edge_records"]),
        "minimum_margin": claims["minimum_margin"],
        "strongly_connected": claims["strongly_connected"],
        "closed_recurrent_block": claims["closed_recurrent_block"],
        "all_rows_strict": claims["all_rows_strict"],
        "complete_strict_scc": claims["complete_strict_scc"],
    }
    output["recurrent_block_common_weight_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_internal_artifact(
    raw: dict[str, Any],
    *,
    block_id: str,
    unit_id: str,
    required_kind: str,
    bound_name: str,
    bound_digest: str,
    expected_support_fields: dict[str, list[str]],
    output_digest_name: str,
    path: str,
) -> dict[str, Any]:
    values = {
        key: raw.get(key)
        for key in (
            "artifact_id", "artifact_kind", "proof_locator", "proof_digest",
            "proof_statement", "evidence",
        )
    }
    for name, value in values.items():
        require(isinstance(value, str) and value, f"{path}.{name}: required")
    require(raw.get("block_id") == block_id, f"{path}.block_id: mismatch")
    require(raw.get("unit_id") == unit_id, f"{path}.unit_id: mismatch")
    require(values["artifact_kind"] == required_kind, f"{path}.artifact_kind: wrong kind")
    require(raw.get(bound_name) == bound_digest, f"{path}.{bound_name}: mismatch")
    output = {
        "block_id": block_id,
        "unit_id": unit_id,
        "artifact_id": values["artifact_id"],
        "artifact_kind": values["artifact_kind"],
        bound_name: bound_digest,
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


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    t10_certificate = certificate.get("transition_resource_frontier_certificate")
    raw_records = certificate.get("recurrent_block_closure_records")
    raw_common_records = certificate.get("recurrent_block_common_weight_records")
    raw_common_artifacts = certificate.get("recurrent_block_common_weight_artifacts")
    raw_closure_artifacts = certificate.get("recurrent_block_closure_artifacts")
    require(isinstance(t10_certificate, dict),
            "transition_resource_frontier_certificate: expected object")
    for name, value in (
        ("recurrent_block_closure_records", raw_records),
        ("recurrent_block_common_weight_records", raw_common_records),
        ("recurrent_block_common_weight_artifacts", raw_common_artifacts),
        ("recurrent_block_closure_artifacts", raw_closure_artifacts),
    ):
        require(isinstance(value, list), f"{name}: expected list")

    t10_frontier.validate_certificate(t10_certificate)
    t10_exact = t10_frontier.exact_certificate(t10_certificate)
    t06_certificate = t10_certificate["candidate_policy_frontier_certificate"]
    t06_frontier.validate_certificate(t06_certificate)
    t06_exact = t06_frontier.exact_certificate(t06_certificate)
    t05_certificate = t06_certificate["geometry_selector_frontier_certificate"]
    t05_frontier.validate_certificate(t05_certificate)
    t05_exact = t05_frontier.exact_certificate(t05_certificate)
    t04_certificate = t05_certificate["block_interface_population_frontier_certificate"]
    t04_frontier.validate_certificate(t04_certificate)
    t04_exact = t04_frontier.exact_certificate(t04_certificate)
    t03_certificate = t04_certificate["slot_candidate_population_frontier_certificate"]
    t03_frontier.validate_certificate(t03_certificate)
    t03_exact = t03_frontier.exact_certificate(t03_certificate)

    target_registry = t04_certificate["atomic_target_artifact_registry_certificate"]
    target_artifacts.validate_certificate(target_registry)
    target_exact = target_artifacts.exact_certificate(target_registry)
    current = target_registry["current_frontier_execution_certificate"]
    atomic_certificate = current["atomic_frontier_execution_certificate"]
    atomic.validate_certificate(atomic_certificate)
    atomic_exact = atomic.exact_certificate(atomic_certificate)

    rule_certificate = t03_certificate["rule_exhaustiveness_frontier_certificate"]
    source_registry = rule_certificate["source_truth_frontier_execution_certificate"][
        "source_statement_truth_registry_certificate"
    ]
    obligation_certificate = source_registry["obligation_artifact_registry_certificate"]
    obligation_artifacts.validate_certificate(obligation_certificate)
    obligation_exact = obligation_artifacts.exact_certificate(obligation_certificate)
    closure_certificate = obligation_certificate["all_n_implication_closure_certificate"]
    closure_exact = closure.exact_certificate(closure_certificate)

    expected_blocks = [
        unit for unit in t04_exact["expected_block_interface_population_units"]
        if unit["unit_kind"] == "recurrent-block"
    ]
    require(expected_blocks, "T11 requires at least one skeleton-derived recurrent block")
    active_by_global = {
        row["parent_global_state_id"]: row for row in t10_exact["active_row_records"]
    }
    active_rows_by_block: dict[str, list[dict[str, Any]]] = {}
    for unit in expected_blocks:
        rows = []
        for binding in unit["parent_bindings"]:
            parent = binding["parent_global_state_id"]
            require(parent in active_by_global,
                    f"block {unit['object_id']}: missing T08 active row for {parent}")
            rows.append(active_by_global[parent])
        active_rows_by_block[unit["object_id"]] = rows

    t04_record_by_unit = {
        record["unit_id"]: record for record in t04_exact["block_interface_population_records"]
    }
    t04_payload_by_unit = {
        payload["unit_id"]: payload for payload in t04_exact["block_interface_population_payloads"]
    }
    t04_artifact_by_unit = {
        artifact["unit_id"]: artifact["artifact_id"]
        for artifact in t04_exact["block_interface_population_artifacts"]
    }
    payload_by_slot = {
        payload["slot_id"]: payload for payload in t03_exact["slot_population_payloads"]
    }
    geometry_by_slot = {
        wrapper["slot_id"]: wrapper
        for wrapper in t05_exact["slot_linked_operation_selector_certificates"]
    }
    t05_artifact_by_slot = {
        artifact["slot_id"]: artifact["artifact_id"]
        for artifact in t05_exact["slot_geometry_selector_artifacts"]
    }
    score_by_slot = {
        record["slot_id"]: record for record in t06_exact["candidate_score_records"]
    }
    score_artifact_by_slot = {
        artifact["slot_id"]: artifact["artifact_id"]
        for artifact in t06_exact["candidate_score_artifacts"]
    }
    application_artifact_by_parent = {
        artifact["parent_global_state_id"]: artifact["artifact_id"]
        for artifact in t06_exact["candidate_policy_application_artifacts"]
    }
    credit_by_row = {
        record["row_id"]: record for record in t10_exact["routed_credit_semantic_records"]
    }
    credit_artifact_by_row = {
        artifact["row_id"]: artifact["artifact_id"]
        for artifact in t10_exact["routed_credit_semantic_artifacts"]
    }

    require(len(raw_records) == len(expected_blocks),
            "recurrent_block_closure_records: exact block cardinality required")
    require(
        [record.get("block_id") for record in raw_records]
        == [unit["object_id"] for unit in expected_blocks],
        "recurrent_block_closure_records: canonical block order required",
    )
    records = []
    for index, (raw, unit) in enumerate(zip(raw_records, expected_blocks)):
        unit_id = unit["unit_id"]
        record = exact_block_record(
            raw,
            unit=unit,
            active_rows=active_rows_by_block[unit["object_id"]],
            t04_payload=t04_payload_by_unit.get(unit_id),
            path=f"recurrent_block_closure_records[{index}]",
        )
        if record["status"] == "proved":
            require(t04_record_by_unit[unit_id]["status"] == "proved",
                    f"block {record['block_id']}: T04 population is not proved")
            require(unit_id in t04_artifact_by_unit,
                    f"block {record['block_id']}: T04 artifact missing")
        records.append(record)
    require(raw_records == records,
            "recurrent_block_closure_records: canonical records/digests required")
    record_by_block = {record["block_id"]: record for record in records}
    unit_by_block = {unit["object_id"]: unit for unit in expected_blocks}

    common_groups = {block_id: [] for block_id in record_by_block}
    for raw in raw_common_records:
        require(isinstance(raw, dict), "recurrent_block_common_weight_records: expected objects")
        block_id = raw.get("block_id")
        require(block_id in common_groups, f"common-weight record: unknown block {block_id}")
        common_groups[block_id].append(raw)
    common_records = []
    common_by_block: dict[str, dict[str, Any]] = {}
    for record in records:
        block_id = record["block_id"]
        group = common_groups[block_id]
        if record["status"] == "open":
            require(not group, f"block {block_id}: open block cannot contain common-weight record")
            continue
        require(len(group) == 1, f"block {block_id}: exactly one common-weight record required")
        unit = unit_by_block[block_id]
        exact = exact_common_weight_record(
            group[0],
            block_record=record,
            unit=unit,
            t04_payload=t04_payload_by_unit[unit["unit_id"]],
            active_rows=active_rows_by_block[block_id],
            payload_by_slot=payload_by_slot,
            geometry_by_slot=geometry_by_slot,
            score_by_slot=score_by_slot,
            credit_by_row=credit_by_row,
            path=f"recurrent_block_common_weight_record[{block_id}]",
        )
        common_records.append(exact)
        common_by_block[block_id] = exact
    require(raw_common_records == common_records,
            "recurrent_block_common_weight_records: canonical order/content required")

    common_artifact_groups = {block_id: [] for block_id in record_by_block}
    for raw in raw_common_artifacts:
        require(isinstance(raw, dict), "recurrent_block_common_weight_artifacts: expected objects")
        block_id = raw.get("block_id")
        require(block_id in common_artifact_groups,
                f"common-weight artifact: unknown block {block_id}")
        common_artifact_groups[block_id].append(raw)
    closure_artifact_groups = {block_id: [] for block_id in record_by_block}
    for raw in raw_closure_artifacts:
        require(isinstance(raw, dict), "recurrent_block_closure_artifacts: expected objects")
        block_id = raw.get("block_id")
        require(block_id in closure_artifact_groups,
                f"block-closure artifact: unknown block {block_id}")
        closure_artifact_groups[block_id].append(raw)

    common_artifacts = []
    closure_artifacts = []
    common_artifact_by_block: dict[str, str] = {}
    proof_bundles = []
    for record in records:
        block_id = record["block_id"]
        common_group = common_artifact_groups[block_id]
        closure_group = closure_artifact_groups[block_id]
        artifact_list: list[dict[str, Any]] = []
        if record["status"] == "open":
            require(not common_group, f"block {block_id}: open block cannot contain common-weight artifact")
            require(not closure_group, f"block {block_id}: open block cannot contain closure artifact")
        else:
            require(len(common_group) == 1,
                    f"block {block_id}: exactly one common-weight artifact required")
            require(len(closure_group) == 1,
                    f"block {block_id}: exactly one closure artifact required")
            unit = unit_by_block[block_id]
            common_record = common_by_block[block_id]
            rows = active_rows_by_block[block_id]
            selected_slots = sorted({row["selected_slot_id"] for row in rows})
            expected_t04 = [t04_artifact_by_unit[unit["unit_id"]]]
            expected_t05 = sorted(t05_artifact_by_slot[slot] for slot in selected_slots)
            expected_t06_scores = sorted(score_artifact_by_slot[slot] for slot in selected_slots)
            expected_t06_applications = sorted(
                application_artifact_by_parent[row["parent_global_state_id"]] for row in rows
            )
            expected_t10 = sorted(credit_artifact_by_row[row["row_id"]] for row in rows)
            common_artifact = exact_internal_artifact(
                common_group[0],
                block_id=block_id,
                unit_id=unit["unit_id"],
                required_kind=COMMON_WEIGHT_ARTIFACT_KIND,
                bound_name="recurrent_block_common_weight_record_sha256",
                bound_digest=common_record["recurrent_block_common_weight_record_sha256"],
                expected_support_fields={
                    "support_t04_population_artifact_ids": expected_t04,
                    "support_t05_geometry_artifact_ids": expected_t05,
                    "support_t06_score_artifact_ids": expected_t06_scores,
                    "support_t06_application_artifact_ids": expected_t06_applications,
                    "support_t10_credit_artifact_ids": expected_t10,
                },
                output_digest_name="recurrent_block_common_weight_artifact_sha256",
                path=f"recurrent_block_common_weight_artifact[{block_id}]",
            )
            common_artifacts.append(common_artifact)
            common_artifact_by_block[block_id] = common_artifact["artifact_id"]
            closure_artifact = exact_internal_artifact(
                closure_group[0],
                block_id=block_id,
                unit_id=unit["unit_id"],
                required_kind=BLOCK_CLOSURE_ARTIFACT_KIND,
                bound_name="block_closure_record_core_sha256",
                bound_digest=record["block_closure_record_core_sha256"],
                expected_support_fields={
                    "support_common_weight_artifact_ids": [common_artifact["artifact_id"]],
                },
                output_digest_name="recurrent_block_closure_artifact_sha256",
                path=f"recurrent_block_closure_artifact[{block_id}]",
            )
            closure_artifacts.append(closure_artifact)
            artifact_list = [common_artifact, closure_artifact]
            proof_bundle = {
                "block_id": block_id,
                "block_closure_record_core_sha256": record[
                    "block_closure_record_core_sha256"
                ],
                "recurrent_block_common_weight_record_sha256": common_record[
                    "recurrent_block_common_weight_record_sha256"
                ],
                "recurrent_block_common_weight_artifact_sha256": common_artifact[
                    "recurrent_block_common_weight_artifact_sha256"
                ],
                "recurrent_block_closure_artifact_sha256": closure_artifact[
                    "recurrent_block_closure_artifact_sha256"
                ],
                "support_common_weight_artifact_ids": [common_artifact["artifact_id"]],
            }
            proof_bundle["recurrent_block_closure_proof_bundle_sha256"] = catalogue.canonical_digest(
                proof_bundle
            )
            require(
                record["verification_digest"]
                == proof_bundle["recurrent_block_closure_proof_bundle_sha256"],
                f"block {block_id}: verification digest does not bind exact proof bundle",
            )
            proof_bundles.append(proof_bundle)
        bundle = {
            "block_id": block_id,
            "status": record["status"],
            "artifacts_sha256": catalogue.canonical_digest(artifact_list),
        }
        bundle["recurrent_block_artifact_bundle_sha256"] = catalogue.canonical_digest(bundle)
    require(raw_common_artifacts == common_artifacts,
            "recurrent_block_common_weight_artifacts: canonical order/content required")
    require(raw_closure_artifacts == closure_artifacts,
            "recurrent_block_closure_artifacts: canonical order/content required")
    all_internal_ids = [artifact["artifact_id"] for artifact in common_artifacts + closure_artifacts]
    require(len(all_internal_ids) == len(set(all_internal_ids)),
            "T11 internal artifacts: duplicate artifact_id")

    status_counts = Counter(record["status"] for record in records)
    t04_ready = int(t04_exact["claims"]["t04_block_interface_population_ready"])
    t06_ready = int(t06_exact["claims"]["candidate_policy_correct_ready"])
    t10_ready = int(t10_exact["claims"]["t10_routed_credit_semantics_ready"])
    t11_ready = int(
        t04_ready and t06_ready and t10_ready
        and status_counts["proved"] == len(records)
        and len(common_records) == len(records)
        and len(common_artifacts) == len(records)
        and len(closure_artifacts) == len(records)
    )

    common_weight_bank = {
        "t04_global_population_bank_sha256": t04_exact["claims"][
            "global_block_interface_population_bank_sha256"
        ],
        "t06_candidate_policy_bank_sha256": t06_exact["claims"][
            "candidate_policy_proof_bank_sha256"
        ],
        "t10_routed_credit_bank_sha256": t10_exact["claims"][
            "routed_credit_semantics_proof_bank_sha256"
        ],
        "expected_recurrent_blocks_sha256": catalogue.canonical_digest(expected_blocks),
        "recurrent_block_common_weight_records_sha256": catalogue.canonical_digest(common_records),
        "recurrent_block_common_weight_artifacts_sha256": catalogue.canonical_digest(common_artifacts),
    }
    common_weight_bank["recurrent_block_common_weight_proof_bank_sha256"] = catalogue.canonical_digest(
        common_weight_bank
    )
    closure_bank = {
        "common_weight_proof_bank_sha256": common_weight_bank[
            "recurrent_block_common_weight_proof_bank_sha256"
        ],
        "recurrent_block_closure_records_sha256": catalogue.canonical_digest(records),
        "recurrent_block_closure_artifacts_sha256": catalogue.canonical_digest(closure_artifacts),
        "recurrent_block_proof_bundles_sha256": catalogue.canonical_digest(proof_bundles),
    }
    closure_bank["recurrent_block_closure_proof_bank_sha256"] = catalogue.canonical_digest(
        closure_bank
    )
    combined_bank = {
        "common_weight_proof_bank_sha256": common_weight_bank[
            "recurrent_block_common_weight_proof_bank_sha256"
        ],
        "block_closure_proof_bank_sha256": closure_bank[
            "recurrent_block_closure_proof_bank_sha256"
        ],
    }
    combined_bank["t11_recurrent_block_closure_proof_bank_sha256"] = catalogue.canonical_digest(
        combined_bank
    )

    closure_by_id = {
        record["obligation_id"]: record
        for record in closure_exact["obligation_closure_records"]
    }
    require(
        int(closure_by_id["CLOSED_STRICT_RECURRENT_BLOCKS"]["closed"]) == t11_ready,
        "CLOSED_STRICT_RECURRENT_BLOCKS closure disagrees with exact T11 bank",
    )
    obligation_records = [
        artifact for artifact in obligation_exact["proof_artifacts"]
        if artifact["obligation_id"] == "CLOSED_STRICT_RECURRENT_BLOCKS"
    ]
    require(len(obligation_records) == (2 if t11_ready else 0),
            "CLOSED_STRICT_RECURRENT_BLOCKS artifact presence disagrees with readiness")
    if t11_ready:
        by_kind = {artifact["artifact_kind"]: artifact for artifact in obligation_records}
        require(set(by_kind) == {"block-closure-proof", "common-weight-proof"},
                "CLOSED_STRICT_RECURRENT_BLOCKS requires exact two artifact kinds")
        dependency_support = sorted(
            artifact["artifact_id"]
            for artifact in obligation_exact["proof_artifacts"]
            if artifact["obligation_id"] in {"CANDIDATE_POLICY_CORRECT", "CREDIT_ROUTING_SEMANTIC"}
        )
        closure_artifact = by_kind["block-closure-proof"]
        require(closure_artifact["locator"] == BLOCK_OBLIGATION_LOCATOR,
                "block-closure-proof locator does not bind T11 closure bank")
        require(closure_artifact["digest"] == closure_bank[
            "recurrent_block_closure_proof_bank_sha256"
        ], "block-closure-proof digest does not bind exact closure bank")
        require(closure_artifact["support_artifact_ids"] == dependency_support,
                "block-closure-proof requires exact T06/T10 obligation support")
        weight_artifact = by_kind["common-weight-proof"]
        require(weight_artifact["locator"] == WEIGHT_OBLIGATION_LOCATOR,
                "common-weight-proof locator does not bind T11 weight bank")
        require(weight_artifact["digest"] == common_weight_bank[
            "recurrent_block_common_weight_proof_bank_sha256"
        ], "common-weight-proof digest does not bind exact weight bank")
        require(weight_artifact["support_artifact_ids"] == dependency_support,
                "common-weight-proof requires exact T06/T10 obligation support")

    target_results = {
        record["target_id"]: record for record in atomic_exact["target_result_records"]
    }
    t11_complete = int(
        target_results["T11_RECURRENT_BLOCK_CLOSURE"]["effective_target_complete"]
    )
    require(t11_complete == t11_ready,
            "T11_RECURRENT_BLOCK_CLOSURE completion disagrees with exact T11 bank")
    target_artifact_by_id = {
        artifact["target_id"]: artifact for artifact in target_exact["atomic_target_artifacts"]
    }
    t11_artifact = target_artifact_by_id.get("T11_RECURRENT_BLOCK_CLOSURE")
    if t11_ready:
        require(t11_artifact is not None, "completed T11 target missing block-closure-proof artifact")
        require(t11_artifact["artifact_kind"] == "block-closure-proof",
                "T11 target requires block-closure-proof")
        require(t11_artifact["proof_locator"] == T11_TARGET_LOCATOR,
                "T11 target proof locator does not bind recurrent-block frontier")
        require(t11_artifact["proof_digest"] == combined_bank[
            "t11_recurrent_block_closure_proof_bank_sha256"
        ], "T11 target proof digest does not bind combined noncircular T11 bank")
    else:
        require(t11_artifact is None, "open T11 target cannot contain target artifact")

    claims = {
        "expected_recurrent_blocks": len(expected_blocks),
        "open_recurrent_blocks": status_counts["open"],
        "proved_recurrent_blocks": status_counts["proved"],
        "common_weight_certificates": len(common_records),
        "common_weight_artifacts": len(common_artifacts),
        "block_closure_artifacts": len(closure_artifacts),
        "state_weights": sum(len(record["state_weights"]) for record in common_records),
        "row_bridges": sum(len(record["row_bridge_records"]) for record in common_records),
        "nonrecurrent_exit_edges": sum(
            len(record["nonrecurrent_exit_edge_records"]) for record in common_records
        ),
        "minimum_block_margin": (
            min(record["minimum_margin"] for record in common_records)
            if common_records else None
        ),
        "t04_block_interface_population_ready": t04_ready,
        "t06_candidate_policy_ready": t06_ready,
        "t10_routed_credit_semantics_ready": t10_ready,
        "t11_recurrent_block_closure_ready": t11_ready,
        "exact_t04_recurrent_block_census": 1,
        "exact_t08_active_row_parent_coverage": 1,
        "exact_t03_t05_common_row_identity": 1,
        "exact_t06_score_to_common_minimum_binding": 1,
        "exact_t10_selected_credit_unit_binding": 1,
        "primitive_positive_common_state_weights": 1,
        "exact_recurrent_support_graph": 1,
        "noncircular_t11_bank_binding": 1,
        "all_n_proved_by_checker": 0,
        "open_block_ids": [record["block_id"] for record in records if record["status"] == "open"],
        "expected_recurrent_blocks_sha256": catalogue.canonical_digest(expected_blocks),
        "recurrent_block_closure_records_sha256": catalogue.canonical_digest(records),
        "recurrent_block_common_weight_records_sha256": catalogue.canonical_digest(common_records),
        "recurrent_block_common_weight_artifacts_sha256": catalogue.canonical_digest(common_artifacts),
        "recurrent_block_closure_artifacts_sha256": catalogue.canonical_digest(closure_artifacts),
        "recurrent_block_common_weight_proof_bank_sha256": common_weight_bank[
            "recurrent_block_common_weight_proof_bank_sha256"
        ],
        "recurrent_block_closure_proof_bank_sha256": closure_bank[
            "recurrent_block_closure_proof_bank_sha256"
        ],
        "t11_recurrent_block_closure_proof_bank_sha256": combined_bank[
            "t11_recurrent_block_closure_proof_bank_sha256"
        ],
        "obligation_artifact_registry_sha256": obligation_certificate["certificate_sha256"],
        "atomic_target_artifact_registry_sha256": target_registry["certificate_sha256"],
    }
    return {
        "recurrent_block_closure_records": records,
        "recurrent_block_common_weight_records": common_records,
        "recurrent_block_common_weight_artifacts": common_artifacts,
        "recurrent_block_closure_artifacts": closure_artifacts,
        "recurrent_block_closure_proof_bundles": proof_bundles,
        "recurrent_block_common_weight_proof_bank": common_weight_bank,
        "recurrent_block_closure_proof_bank": closure_bank,
        "t11_recurrent_block_closure_proof_bank": combined_bank,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int | None]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in (
        "recurrent_block_closure_records",
        "recurrent_block_common_weight_records",
        "recurrent_block_common_weight_artifacts",
        "recurrent_block_closure_artifacts",
        "recurrent_block_closure_proof_bundles",
        "recurrent_block_common_weight_proof_bank",
        "recurrent_block_closure_proof_bank",
        "t11_recurrent_block_closure_proof_bank",
        "claims",
    ):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {
        "blocks": claims["expected_recurrent_blocks"],
        "proved": claims["proved_recurrent_blocks"],
        "bridges": claims["row_bridges"],
        "minimum_margin": claims["minimum_block_margin"],
        "ready": claims["t11_recurrent_block_closure_ready"],
        "all_n": claims["all_n_proved_by_checker"],
    }


def build_certificate(
    t10_certificate: dict[str, Any],
    block_records: list[dict[str, Any]],
    common_weight_records: list[dict[str, Any]],
    common_weight_artifacts: list[dict[str, Any]],
    closure_artifacts: list[dict[str, Any]],
) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "transition_resource_frontier_certificate": t10_certificate,
        "recurrent_block_closure_records": block_records,
        "recurrent_block_common_weight_records": common_weight_records,
        "recurrent_block_common_weight_artifacts": common_weight_artifacts,
        "recurrent_block_closure_artifacts": closure_artifacts,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: check_prime_power_recurrent_block_closure_frontier.py certificate.json"
        )
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
