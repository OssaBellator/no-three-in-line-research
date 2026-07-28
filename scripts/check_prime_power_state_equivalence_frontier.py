#!/usr/bin/env python3
"""Validate and synchronize the exact T13 cross-block state-equivalence proof bank.

T04 supplies the exact recurrent-block census and literal local-state population, while T07 supplies
the exact state-claim and semantic-artifact banks for every slot used by those blocks. This checker
requires one local-to-global identity claim for every T04 local state, reconstructs every global class,
and requires a canonical spanning proof tree for each proved class.

The checker validates documentary identity, coverage, support and graph arithmetic only. It does not
decide whether any state-equivalence statement is mathematically true and permanently reports
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
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_fate_transition_state_frontier as t07_frontier
import check_prime_power_obligation_artifact_registry as obligation_artifacts


class StateEquivalenceFrontierError(ValueError):
    """Raised when the exact T13 state-equivalence bank is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise StateEquivalenceFrontierError(message)


CLASS_ARTIFACT_KIND = "global-state-equivalence-class-proof"
OBLIGATION_LOCATOR = (
    "state-equivalence-frontier://CROSS_BLOCK_STATE_IDENTITY_SEMANTIC"
)
T13_TARGET_LOCATOR = "state-equivalence-frontier://T13_STATE_EQUIVALENCE"


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


def exact_local_state(raw: Any, *, block_id: str, unit_id: str, index: int) -> dict[str, Any]:
    require(isinstance(raw, dict), f"block {block_id}.local_states[{index}]: expected object")
    state_id = raw.get("id")
    role = raw.get("role")
    stratum = raw.get("stratum")
    owner = raw.get("owner")
    require(isinstance(state_id, str) and state_id, f"block {block_id}: state.id required")
    require(
        role in {"recurrent", "offdiagonal", "auxiliary", "sink"},
        f"block {block_id}, state {state_id}: bad role",
    )
    require(type(stratum) is int and stratum >= 0, f"block {block_id}, state {state_id}: bad stratum")
    require(
        owner is None or (isinstance(owner, list) and len(owner) == 2),
        f"block {block_id}, state {state_id}: bad owner",
    )
    output = {
        "block_id": block_id,
        "unit_id": unit_id,
        "local_state_id": state_id,
        "role": role,
        "stratum": stratum,
        "owner": canonical_json_value(copy.deepcopy(owner), f"block {block_id}.state {state_id}.owner"),
        "t04_local_state_value_sha256": catalogue.canonical_digest(
            canonical_json_value(copy.deepcopy(raw), f"block {block_id}.local_states[{index}]")
        ),
    }
    output["local_state_subject_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_claim_ids(raw: Any, *, allowed: set[str], path: str) -> list[str]:
    require(isinstance(raw, list), f"{path}: expected list")
    require(all(isinstance(value, str) and value for value in raw), f"{path}: bad claim ID")
    require(raw == sorted(raw), f"{path}: sorted order required")
    require(len(raw) == len(set(raw)), f"{path}: duplicates")
    require(bool(raw), f"{path}: nonempty support required")
    require(set(raw) <= allowed, f"{path}: claim outside exact block T07 state bank")
    return list(raw)


def exact_link(
    raw: dict[str, Any],
    *,
    subject: dict[str, Any],
    allowed_state_claim_ids: set[str],
    path: str,
) -> dict[str, Any]:
    require(raw.get("block_id") == subject["block_id"], f"{path}.block_id: mismatch")
    require(raw.get("unit_id") == subject["unit_id"], f"{path}.unit_id: mismatch")
    require(
        raw.get("local_state_id") == subject["local_state_id"],
        f"{path}.local_state_id: mismatch",
    )
    require(
        raw.get("local_state_subject_sha256") == subject["local_state_subject_sha256"],
        f"{path}.local_state_subject_sha256: mismatch",
    )
    global_state_id = raw.get("global_state_id")
    statement = raw.get("identity_statement")
    evidence = raw.get("evidence")
    require(
        isinstance(global_state_id, str) and global_state_id,
        f"{path}.global_state_id: required",
    )
    require(isinstance(statement, str) and statement, f"{path}.identity_statement: required")
    require(isinstance(evidence, str) and evidence, f"{path}.evidence: required")
    support = exact_claim_ids(
        raw.get("support_state_claim_ids"),
        allowed=allowed_state_claim_ids,
        path=f"{path}.support_state_claim_ids",
    )
    output = {
        "block_id": subject["block_id"],
        "unit_id": subject["unit_id"],
        "local_state_id": subject["local_state_id"],
        "local_state_subject_sha256": subject["local_state_subject_sha256"],
        "global_state_id": global_state_id,
        "support_state_claim_ids": support,
        "identity_statement": statement,
        "evidence": evidence,
    }
    output["local_to_global_state_link_sha256"] = catalogue.canonical_digest(output)
    return output


def member_ref(block_id: str, local_state_id: str) -> str:
    return f"{block_id}::{local_state_id}"


def exact_class_status(
    raw: dict[str, Any],
    *,
    global_record: dict[str, Any],
    path: str,
) -> dict[str, Any]:
    global_state_id = global_record["global_state_id"]
    require(raw.get("global_state_id") == global_state_id, f"{path}.global_state_id: mismatch")
    require(
        raw.get("global_state_record_sha256") == global_record["global_state_record_sha256"],
        f"{path}.global_state_record_sha256: mismatch",
    )
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
        require(
            locator == f"state-equivalence-class-registry://{global_state_id}",
            f"{path}.verification_locator: canonical class URI required",
        )
        require(isinstance(digest, str) and digest, f"{path}.verification_digest: required")
    core = {
        "global_state_id": global_state_id,
        "global_state_record_sha256": global_record["global_state_record_sha256"],
        "status": status,
        "verification_locator": locator,
        "note": note,
    }
    output = {
        **core,
        "verification_digest": digest,
        "state_equivalence_class_record_core_sha256": catalogue.canonical_digest(core),
    }
    output["state_equivalence_class_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_edge(
    raw: dict[str, Any],
    *,
    global_record: dict[str, Any],
    link_by_ref: dict[tuple[str, str], dict[str, Any]],
    path: str,
) -> dict[str, Any]:
    global_state_id = global_record["global_state_id"]
    require(raw.get("global_state_id") == global_state_id, f"{path}.global_state_id: mismatch")
    left = (raw.get("left_block_id"), raw.get("left_local_state_id"))
    right = (raw.get("right_block_id"), raw.get("right_local_state_id"))
    require(
        all(isinstance(value, str) and value for value in (*left, *right)),
        f"{path}: endpoint IDs required",
    )
    require(left != right, f"{path}: self equivalence edge")
    if right < left:
        left, right = right, left
    members = {
        (member["block_id"], member["local_state_id"])
        for member in global_record["members"]
    }
    require(left in members and right in members, f"{path}: endpoint outside class")
    require(left[0] != right[0], f"{path}: one class cannot merge two local states in one block")
    statement = raw.get("equivalence_statement")
    evidence = raw.get("evidence")
    require(isinstance(statement, str) and statement, f"{path}.equivalence_statement: required")
    require(isinstance(evidence, str) and evidence, f"{path}.evidence: required")
    expected_left_support = link_by_ref[left]["support_state_claim_ids"]
    expected_right_support = link_by_ref[right]["support_state_claim_ids"]
    require(
        raw.get("left_support_state_claim_ids") == expected_left_support,
        f"{path}.left_support_state_claim_ids: exact endpoint support required",
    )
    require(
        raw.get("right_support_state_claim_ids") == expected_right_support,
        f"{path}.right_support_state_claim_ids: exact endpoint support required",
    )
    output = {
        "global_state_id": global_state_id,
        "left_block_id": left[0],
        "left_local_state_id": left[1],
        "right_block_id": right[0],
        "right_local_state_id": right[1],
        "left_support_state_claim_ids": list(expected_left_support),
        "right_support_state_claim_ids": list(expected_right_support),
        "equivalence_statement": statement,
        "evidence": evidence,
    }
    output["state_equivalence_edge_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_tree(
    *,
    global_record: dict[str, Any],
    edges: list[dict[str, Any]],
) -> dict[str, Any]:
    global_state_id = global_record["global_state_id"]
    members = sorted(
        (member["block_id"], member["local_state_id"])
        for member in global_record["members"]
    )
    expected_edges = max(0, len(members) - 1)
    require(
        len(edges) == expected_edges,
        f"global state {global_state_id}: proved class requires exactly member_count-1 edges",
    )
    pair_keys = [
        (
            edge["left_block_id"],
            edge["left_local_state_id"],
            edge["right_block_id"],
            edge["right_local_state_id"],
        )
        for edge in edges
    ]
    require(len(pair_keys) == len(set(pair_keys)), f"global state {global_state_id}: duplicate pair")
    adjacency: dict[tuple[str, str], list[tuple[tuple[str, str], str]]] = {
        member: [] for member in members
    }
    for edge in edges:
        left = (edge["left_block_id"], edge["left_local_state_id"])
        right = (edge["right_block_id"], edge["right_local_state_id"])
        adjacency[left].append((right, edge["state_equivalence_edge_sha256"]))
        adjacency[right].append((left, edge["state_equivalence_edge_sha256"]))
    root = members[0]
    parent: dict[tuple[str, str], tuple[tuple[str, str] | None, str | None]] = {
        root: (None, None)
    }
    queue = deque([root])
    while queue:
        current = queue.popleft()
        for nxt, edge_sha in sorted(adjacency[current]):
            if nxt not in parent:
                parent[nxt] = (current, edge_sha)
                queue.append(nxt)
    require(set(parent) == set(members), f"global state {global_state_id}: evidence graph disconnected")
    paths = []
    for member in members:
        chain: list[str] = []
        current = member
        while parent[current][0] is not None:
            previous, edge_sha = parent[current]
            require(edge_sha is not None, "tree parent edge missing")
            chain.append(edge_sha)
            require(previous is not None, "tree parent missing")
            current = previous
        chain.reverse()
        paths.append(
            {
                "member_ref": member_ref(member[0], member[1]),
                "root_path_edge_sha256s": chain,
                "path_length": len(chain),
            }
        )
    output = {
        "global_state_id": global_state_id,
        "root_member_ref": member_ref(root[0], root[1]),
        "member_refs": [member_ref(block, state) for block, state in members],
        "member_count": len(members),
        "tree_edge_count": len(edges),
        "tree_edge_sha256s": sorted(
            edge["state_equivalence_edge_sha256"] for edge in edges
        ),
        "root_paths": paths,
        "spanning_tree_complete": 1,
    }
    output["state_equivalence_tree_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_class_artifact(
    raw: dict[str, Any],
    *,
    global_record: dict[str, Any],
    tree: dict[str, Any],
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
    global_state_id = global_record["global_state_id"]
    require(raw.get("global_state_id") == global_state_id, f"{path}.global_state_id: mismatch")
    require(
        raw.get("global_state_record_sha256") == global_record["global_state_record_sha256"],
        f"{path}.global_state_record_sha256: mismatch",
    )
    require(
        raw.get("state_equivalence_tree_sha256") == tree["state_equivalence_tree_sha256"],
        f"{path}.state_equivalence_tree_sha256: mismatch",
    )
    require(values["artifact_kind"] == CLASS_ARTIFACT_KIND, f"{path}.artifact_kind: wrong kind")
    support = raw.get("support_t07_semantic_artifact_ids")
    require(
        support == expected_t07_support,
        f"{path}.support_t07_semantic_artifact_ids: exact support required",
    )
    require(isinstance(support, list), f"{path}.support_t07_semantic_artifact_ids: list required")
    require(support == sorted(support), f"{path}.support_t07_semantic_artifact_ids: sorted")
    require(len(support) == len(set(support)), f"{path}: duplicate T07 support")
    require(values["artifact_id"] not in support, f"{path}: self support")
    output = {
        "global_state_id": global_state_id,
        "artifact_id": values["artifact_id"],
        "artifact_kind": values["artifact_kind"],
        "global_state_record_sha256": global_record["global_state_record_sha256"],
        "state_equivalence_tree_sha256": tree["state_equivalence_tree_sha256"],
        "proof_locator": values["proof_locator"],
        "proof_digest": values["proof_digest"],
        "proof_statement": values["proof_statement"],
        "support_t07_semantic_artifact_ids": list(support),
        "evidence": values["evidence"],
    }
    output["state_equivalence_class_artifact_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    t07_certificate = certificate.get("fate_transition_state_frontier_certificate")
    raw_links = certificate.get("local_to_global_state_links")
    raw_statuses = certificate.get("state_equivalence_class_records")
    raw_edges = certificate.get("state_equivalence_edge_records")
    raw_artifacts = certificate.get("state_equivalence_class_artifacts")
    require(isinstance(t07_certificate, dict),
            "fate_transition_state_frontier_certificate: expected object")
    for name, value in (
        ("local_to_global_state_links", raw_links),
        ("state_equivalence_class_records", raw_statuses),
        ("state_equivalence_edge_records", raw_edges),
        ("state_equivalence_class_artifacts", raw_artifacts),
    ):
        require(isinstance(value, list), f"{name}: expected list")

    t07_frontier.validate_certificate(t07_certificate)
    t07_exact = t07_frontier.exact_certificate(t07_certificate)
    t04_certificate = t07_certificate["block_interface_population_frontier_certificate"]
    t04_frontier.validate_certificate(t04_certificate)
    t04_exact = t04_frontier.exact_certificate(t04_certificate)

    target_registry = t04_certificate["atomic_target_artifact_registry_certificate"]
    target_artifacts.validate_certificate(target_registry)
    target_exact = target_artifacts.exact_certificate(target_registry)
    current = target_registry["current_frontier_execution_certificate"]
    atomic_certificate = current["atomic_frontier_execution_certificate"]
    atomic.validate_certificate(atomic_certificate)
    atomic_exact = atomic.exact_certificate(atomic_certificate)

    t03_certificate = t04_certificate["slot_candidate_population_frontier_certificate"]
    rule_certificate = t03_certificate["rule_exhaustiveness_frontier_certificate"]
    source_registry = rule_certificate["source_truth_frontier_execution_certificate"][
        "source_statement_truth_registry_certificate"
    ]
    obligation_certificate = source_registry["obligation_artifact_registry_certificate"]
    obligation_artifacts.validate_certificate(obligation_certificate)
    obligation_exact = obligation_artifacts.exact_certificate(obligation_certificate)
    closure_certificate = obligation_certificate["all_n_implication_closure_certificate"]
    closure_exact = closure.exact_certificate(closure_certificate)

    units = [
        unit for unit in t04_exact["expected_block_interface_population_units"]
        if unit["unit_kind"] == "recurrent-block"
    ]
    require(units, "T13 requires at least one skeleton-derived recurrent block")
    payload_by_unit = {
        payload["unit_id"]: payload
        for payload in t04_exact["block_interface_population_payloads"]
    }
    record_by_unit = {
        record["unit_id"]: record
        for record in t04_exact["block_interface_population_records"]
    }
    semantic_by_slot = {
        item["slot_id"]: item
        for item in t07_exact["slot_fate_transition_state_semantic_certificates"]
    }
    semantic_artifact_by_slot = {
        item["slot_id"]: item["artifact_id"]
        for item in t07_exact["slot_fate_transition_state_artifacts"]
    }

    state_claim_ids_by_slot: dict[str, set[str]] = {}
    for slot_id, semantic in semantic_by_slot.items():
        state_claim_ids_by_slot[slot_id] = {
            claim["claim_id"] for claim in semantic["state_claims"]
        }

    subjects: list[dict[str, Any]] = []
    allowed_claims_by_block: dict[str, set[str]] = {}
    slots_by_block: dict[str, list[str]] = {}
    for unit in units:
        unit_id = unit["unit_id"]
        block_id = unit["object_id"]
        require(
            record_by_unit[unit_id]["status"] != "open" and unit_id in payload_by_unit,
            f"block {block_id}: T04 local-state population is absent",
        )
        payload = payload_by_unit[unit_id]
        local_states = payload["population_data"]["local_states"]
        require(isinstance(local_states, list) and local_states,
                f"block {block_id}: nonempty local_states required")
        block_subjects = [
            exact_local_state(raw, block_id=block_id, unit_id=unit_id, index=index)
            for index, raw in enumerate(local_states)
        ]
        require(
            block_subjects == sorted(block_subjects, key=lambda item: item["local_state_id"]),
            f"block {block_id}: local_states canonical local-state order required",
        )
        require(
            len({item["local_state_id"] for item in block_subjects}) == len(block_subjects),
            f"block {block_id}: duplicate local state",
        )
        subjects.extend(block_subjects)
        slots = sorted({
            binding["operation_slot_id"] for binding in unit["parent_bindings"]
        })
        slots_by_block[block_id] = slots
        require(all(slot in semantic_by_slot for slot in slots),
                f"block {block_id}: using slot lacks T07 semantic certificate")
        allowed_claims_by_block[block_id] = {
            claim_id
            for slot in slots
            for claim_id in state_claim_ids_by_slot[slot]
        }
        require(allowed_claims_by_block[block_id],
                f"block {block_id}: exact T07 state-claim bank is empty")

    subjects.sort(key=lambda item: (item["block_id"], item["local_state_id"]))
    require(
        len(raw_links) == len(subjects),
        "local_to_global_state_links: exact local-state cardinality required",
    )
    require(
        [
            (item.get("block_id"), item.get("local_state_id"))
            for item in raw_links
        ] == [
            (item["block_id"], item["local_state_id"])
            for item in subjects
        ],
        "local_to_global_state_links: exact canonical local-state order required",
    )
    links = [
        exact_link(
            raw,
            subject=subject,
            allowed_state_claim_ids=allowed_claims_by_block[subject["block_id"]],
            path=f"local_to_global_state_links[{index}]",
        )
        for index, (raw, subject) in enumerate(zip(raw_links, subjects))
    ]
    require(raw_links == links, "local_to_global_state_links: canonical records/digests required")
    link_by_ref = {
        (link["block_id"], link["local_state_id"]): link for link in links
    }

    subject_by_ref = {
        (subject["block_id"], subject["local_state_id"]): subject for subject in subjects
    }
    members_by_global: dict[str, list[dict[str, Any]]] = {}
    for link in links:
        subject = subject_by_ref[(link["block_id"], link["local_state_id"])]
        member = {
            "block_id": link["block_id"],
            "unit_id": link["unit_id"],
            "local_state_id": link["local_state_id"],
            "role": subject["role"],
            "stratum": subject["stratum"],
            "owner": copy.deepcopy(subject["owner"]),
            "local_state_subject_sha256": subject["local_state_subject_sha256"],
            "local_to_global_state_link_sha256": link["local_to_global_state_link_sha256"],
            "support_state_claim_ids": list(link["support_state_claim_ids"]),
        }
        members_by_global.setdefault(link["global_state_id"], []).append(member)

    global_records: list[dict[str, Any]] = []
    for global_state_id in sorted(members_by_global):
        members = sorted(
            members_by_global[global_state_id],
            key=lambda item: (item["block_id"], item["local_state_id"]),
        )
        require(
            len({member["block_id"] for member in members}) == len(members),
            f"global state {global_state_id}: at most one member per block required",
        )
        cores = {
            (
                member["role"],
                member["stratum"],
                json.dumps(member["owner"], sort_keys=True, separators=(",", ":")),
            )
            for member in members
        }
        require(len(cores) == 1, f"global state {global_state_id}: semantic-core drift")
        record = {
            "global_state_id": global_state_id,
            "role": members[0]["role"],
            "stratum": members[0]["stratum"],
            "owner": copy.deepcopy(members[0]["owner"]),
            "members": members,
            "member_count": len(members),
            "member_blocks": sorted(member["block_id"] for member in members),
        }
        record["global_state_record_sha256"] = catalogue.canonical_digest(record)
        global_records.append(record)

    require(
        len(raw_statuses) == len(global_records),
        "state_equivalence_class_records: exact class cardinality required",
    )
    require(
        [item.get("global_state_id") for item in raw_statuses]
        == [item["global_state_id"] for item in global_records],
        "state_equivalence_class_records: canonical class order required",
    )
    statuses = [
        exact_class_status(
            raw,
            global_record=global_record,
            path=f"state_equivalence_class_records[{index}]",
        )
        for index, (raw, global_record) in enumerate(zip(raw_statuses, global_records))
    ]
    require(raw_statuses == statuses,
            "state_equivalence_class_records: canonical records/digests required")
    status_by_global = {item["global_state_id"]: item for item in statuses}

    edge_groups = {item["global_state_id"]: [] for item in global_records}
    for raw in raw_edges:
        require(isinstance(raw, dict), "state_equivalence_edge_records: expected objects")
        global_state_id = raw.get("global_state_id")
        require(global_state_id in edge_groups,
                f"state_equivalence_edge_records: unknown class {global_state_id}")
        edge_groups[global_state_id].append(raw)

    edges: list[dict[str, Any]] = []
    trees: list[dict[str, Any]] = []
    tree_by_global: dict[str, dict[str, Any]] = {}
    for global_record in global_records:
        global_state_id = global_record["global_state_id"]
        group = edge_groups[global_state_id]
        if status_by_global[global_state_id]["status"] == "open":
            require(not group, f"global state {global_state_id}: open class cannot contain edges")
            continue
        exact_edges = [
            exact_edge(
                raw,
                global_record=global_record,
                link_by_ref=link_by_ref,
                path=f"state_equivalence_edge[{global_state_id}][{index}]",
            )
            for index, raw in enumerate(group)
        ]
        require(
            exact_edges == sorted(
                exact_edges,
                key=lambda item: (
                    item["left_block_id"],
                    item["left_local_state_id"],
                    item["right_block_id"],
                    item["right_local_state_id"],
                ),
            ),
            f"global state {global_state_id}: canonical edge order required",
        )
        tree = exact_tree(global_record=global_record, edges=exact_edges)
        edges.extend(exact_edges)
        trees.append(tree)
        tree_by_global[global_state_id] = tree
    require(raw_edges == edges, "state_equivalence_edge_records: canonical order/content required")

    artifact_groups = {item["global_state_id"]: [] for item in global_records}
    for raw in raw_artifacts:
        require(isinstance(raw, dict), "state_equivalence_class_artifacts: expected objects")
        global_state_id = raw.get("global_state_id")
        require(global_state_id in artifact_groups,
                f"state_equivalence_class_artifacts: unknown class {global_state_id}")
        artifact_groups[global_state_id].append(raw)

    artifacts: list[dict[str, Any]] = []
    proof_bundles: list[dict[str, Any]] = []
    for global_record in global_records:
        global_state_id = global_record["global_state_id"]
        status = status_by_global[global_state_id]
        group = artifact_groups[global_state_id]
        if status["status"] == "open":
            require(not group, f"global state {global_state_id}: open class cannot contain artifact")
            continue
        require(len(group) == 1, f"global state {global_state_id}: exactly one artifact required")
        member_blocks = global_record["member_blocks"]
        expected_slots = sorted({
            slot for block_id in member_blocks for slot in slots_by_block[block_id]
        })
        require(
            all(slot in semantic_artifact_by_slot for slot in expected_slots),
            f"global state {global_state_id}: selected T07 artifact missing",
        )
        expected_t07_support = sorted(
            semantic_artifact_by_slot[slot] for slot in expected_slots
        )
        tree = tree_by_global[global_state_id]
        artifact = exact_class_artifact(
            group[0],
            global_record=global_record,
            tree=tree,
            expected_t07_support=expected_t07_support,
            path=f"state_equivalence_class_artifact[{global_state_id}]",
        )
        artifacts.append(artifact)
        proof_bundle = {
            "global_state_id": global_state_id,
            "state_equivalence_class_record_core_sha256": status[
                "state_equivalence_class_record_core_sha256"
            ],
            "global_state_record_sha256": global_record["global_state_record_sha256"],
            "state_equivalence_tree_sha256": tree["state_equivalence_tree_sha256"],
            "state_equivalence_class_artifact_sha256": artifact[
                "state_equivalence_class_artifact_sha256"
            ],
            "support_t07_semantic_artifact_ids": artifact[
                "support_t07_semantic_artifact_ids"
            ],
        }
        proof_bundle["state_equivalence_class_proof_bundle_sha256"] = (
            catalogue.canonical_digest(proof_bundle)
        )
        require(
            status["verification_digest"]
            == proof_bundle["state_equivalence_class_proof_bundle_sha256"],
            f"global state {global_state_id}: verification digest does not bind exact proof bundle",
        )
        proof_bundles.append(proof_bundle)
    require(raw_artifacts == artifacts,
            "state_equivalence_class_artifacts: canonical order/content required")
    artifact_ids = [artifact["artifact_id"] for artifact in artifacts]
    require(len(artifact_ids) == len(set(artifact_ids)),
            "state_equivalence_class_artifacts: duplicate artifact_id")

    counts = Counter(item["status"] for item in statuses)
    t07_ready = int(t07_exact["claims"]["fate_transition_state_semantics_ready"])
    t13_ready = int(
        t07_ready
        and counts["proved"] == len(statuses)
        and len(artifacts) == len(statuses)
        and len(trees) == len(statuses)
    )
    proof_bank = {
        "t04_expected_recurrent_blocks_sha256": catalogue.canonical_digest(units),
        "t04_recurrent_block_payloads_sha256": catalogue.canonical_digest(
            [payload_by_unit[unit["unit_id"]] for unit in units]
        ),
        "t07_state_semantics_proof_bank_sha256": t07_exact["claims"][
            "state_semantics_proof_bank_sha256"
        ],
        "local_state_subjects_sha256": catalogue.canonical_digest(subjects),
        "local_to_global_state_links_sha256": catalogue.canonical_digest(links),
        "global_state_records_sha256": catalogue.canonical_digest(global_records),
        "state_equivalence_class_records_sha256": catalogue.canonical_digest(statuses),
        "state_equivalence_edge_records_sha256": catalogue.canonical_digest(edges),
        "state_equivalence_trees_sha256": catalogue.canonical_digest(trees),
        "state_equivalence_class_artifacts_sha256": catalogue.canonical_digest(artifacts),
        "state_equivalence_class_proof_bundles_sha256": catalogue.canonical_digest(
            proof_bundles
        ),
    }
    proof_bank["state_equivalence_frontier_proof_bank_sha256"] = catalogue.canonical_digest(
        proof_bank
    )

    closure_by_id = {
        item["obligation_id"]: item
        for item in closure_exact["obligation_closure_records"]
    }
    require(
        int(closure_by_id["CROSS_BLOCK_STATE_IDENTITY_SEMANTIC"]["closed"]) == t13_ready,
        "CROSS_BLOCK_STATE_IDENTITY_SEMANTIC closure disagrees with exact T13 bank",
    )
    obligation_records = [
        artifact for artifact in obligation_exact["proof_artifacts"]
        if artifact["obligation_id"] == "CROSS_BLOCK_STATE_IDENTITY_SEMANTIC"
    ]
    require(
        len(obligation_records) == (1 if t13_ready else 0),
        "CROSS_BLOCK_STATE_IDENTITY_SEMANTIC artifact presence disagrees with readiness",
    )
    if t13_ready:
        artifact = obligation_records[0]
        require(artifact["artifact_kind"] == "state-equivalence-proof",
                "CROSS_BLOCK_STATE_IDENTITY_SEMANTIC: wrong artifact kind")
        require(artifact["locator"] == OBLIGATION_LOCATOR,
                "CROSS_BLOCK_STATE_IDENTITY_SEMANTIC: locator mismatch")
        require(
            artifact["digest"] == proof_bank["state_equivalence_frontier_proof_bank_sha256"],
            "CROSS_BLOCK_STATE_IDENTITY_SEMANTIC: digest mismatch",
        )
        expected_support = sorted(
            item["artifact_id"]
            for item in obligation_exact["proof_artifacts"]
            if item["obligation_id"] == "FATE_TRANSITION_STATE_SEMANTICS"
        )
        require(
            artifact["support_artifact_ids"] == expected_support,
            "CROSS_BLOCK_STATE_IDENTITY_SEMANTIC: exact T07 obligation support required",
        )

    target_results = {
        item["target_id"]: item for item in atomic_exact["target_result_records"]
    }
    require(
        int(target_results["T13_STATE_EQUIVALENCE"]["effective_target_complete"])
        == t13_ready,
        "T13_STATE_EQUIVALENCE completion disagrees with exact T13 bank",
    )
    target_artifact_by_id = {
        artifact["target_id"]: artifact
        for artifact in target_exact["atomic_target_artifacts"]
    }
    target_artifact = target_artifact_by_id.get("T13_STATE_EQUIVALENCE")
    if t13_ready:
        require(target_artifact is not None, "completed T13 target missing artifact")
        require(target_artifact["artifact_kind"] == "state-equivalence-proof",
                "T13 target requires state-equivalence-proof")
        require(target_artifact["proof_locator"] == T13_TARGET_LOCATOR,
                "T13 target proof locator mismatch")
        require(
            target_artifact["proof_digest"]
            == proof_bank["state_equivalence_frontier_proof_bank_sha256"],
            "T13 target proof digest mismatch",
        )
    else:
        require(target_artifact is None, "open T13 target cannot contain target artifact")

    claims = {
        "expected_recurrent_blocks": len(units),
        "local_state_subjects": len(subjects),
        "global_state_classes": len(global_records),
        "shared_global_state_classes": sum(
            item["member_count"] > 1 for item in global_records
        ),
        "singleton_global_state_classes": sum(
            item["member_count"] == 1 for item in global_records
        ),
        "open_state_equivalence_classes": counts["open"],
        "proved_state_equivalence_classes": counts["proved"],
        "state_equivalence_edges": len(edges),
        "state_equivalence_class_artifacts": len(artifacts),
        "t07_fate_transition_state_ready": t07_ready,
        "t13_state_equivalence_ready": t13_ready,
        "exact_t04_local_state_census": 1,
        "exact_t07_state_claim_support": 1,
        "exact_one_link_per_local_state": 1,
        "exact_semantic_core_consistency": 1,
        "exact_spanning_tree_per_proved_class": 1,
        "noncircular_t13_bank_binding": 1,
        "all_n_proved_by_checker": 0,
        "open_global_state_ids": [
            item["global_state_id"] for item in statuses if item["status"] == "open"
        ],
        "local_state_subjects_sha256": catalogue.canonical_digest(subjects),
        "local_to_global_state_links_sha256": catalogue.canonical_digest(links),
        "global_state_records_sha256": catalogue.canonical_digest(global_records),
        "state_equivalence_class_records_sha256": catalogue.canonical_digest(statuses),
        "state_equivalence_edge_records_sha256": catalogue.canonical_digest(edges),
        "state_equivalence_trees_sha256": catalogue.canonical_digest(trees),
        "state_equivalence_class_artifacts_sha256": catalogue.canonical_digest(artifacts),
        "state_equivalence_frontier_proof_bank_sha256": proof_bank[
            "state_equivalence_frontier_proof_bank_sha256"
        ],
        "obligation_artifact_registry_sha256": obligation_certificate["certificate_sha256"],
        "atomic_target_artifact_registry_sha256": target_registry["certificate_sha256"],
    }
    return {
        "local_state_subject_records": subjects,
        "local_to_global_state_links": links,
        "global_state_records": global_records,
        "state_equivalence_class_records": statuses,
        "state_equivalence_edge_records": edges,
        "state_equivalence_tree_records": trees,
        "state_equivalence_class_artifacts": artifacts,
        "state_equivalence_class_proof_bundles": proof_bundles,
        "state_equivalence_frontier_proof_bank": proof_bank,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in (
        "local_state_subject_records",
        "local_to_global_state_links",
        "global_state_records",
        "state_equivalence_class_records",
        "state_equivalence_edge_records",
        "state_equivalence_tree_records",
        "state_equivalence_class_artifacts",
        "state_equivalence_class_proof_bundles",
        "state_equivalence_frontier_proof_bank",
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
        "blocks": claims["expected_recurrent_blocks"],
        "local_states": claims["local_state_subjects"],
        "global_states": claims["global_state_classes"],
        "shared": claims["shared_global_state_classes"],
        "proved": claims["proved_state_equivalence_classes"],
        "ready": claims["t13_state_equivalence_ready"],
        "all_n": claims["all_n_proved_by_checker"],
    }


def build_certificate(
    t07_certificate: dict[str, Any],
    links: list[dict[str, Any]],
    class_records: list[dict[str, Any]],
    edge_records: list[dict[str, Any]],
    class_artifacts: list[dict[str, Any]],
) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "fate_transition_state_frontier_certificate": t07_certificate,
        "local_to_global_state_links": links,
        "state_equivalence_class_records": class_records,
        "state_equivalence_edge_records": edge_records,
        "state_equivalence_class_artifacts": class_artifacts,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: check_prime_power_state_equivalence_frontier.py certificate.json"
        )
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
