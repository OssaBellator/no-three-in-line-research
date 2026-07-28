#!/usr/bin/env python3
"""Validate the exact documentary T16 global-rank well-foundedness frontier.

T16 derives every critical edge from T15 ``critical-unranked`` rows before reading any rank
data.  It accepts either the nonnegative integers or a fixed finite lexicographic product of
nonnegative integers as the rank domain, requires exact state and edge proof artifacts, audits
the complete critical graph, and synchronizes GLOBAL_RANK_WELL_FOUNDED and T16_GLOBAL_RANK.

This checker validates finite identity, arithmetic, support and sealing only.  It does not prove
the supplied semantic statements true and permanently reports ``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Any

import check_prime_power_all_n_implication_closure as closure
import check_prime_power_atomic_frontier_execution as atomic
import check_prime_power_atomic_target_artifact_registry as target_artifacts
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_interface_exhaustiveness_frontier as t15_frontier
import check_prime_power_obligation_artifact_registry as obligation_artifacts


class GlobalRankFrontierError(ValueError):
    """Raised when the exact T16 rank bank is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GlobalRankFrontierError(message)


def nonempty_text(value: Any, path: str) -> str:
    require(isinstance(value, str) and value, f"{path}: nonempty string required")
    return value


def exact_sorted_ids(value: Any, expected: list[str], path: str) -> list[str]:
    require(value == expected, f"{path}: exact support required")
    require(isinstance(value, list), f"{path}: list required")
    require(value == sorted(value), f"{path}: sorted order required")
    require(len(value) == len(set(value)), f"{path}: duplicates")
    return list(value)


def canonical_rank_value(value: Any, kind: str, coordinates: int, path: str) -> int | list[int]:
    if kind == "nonnegative-integer":
        require(type(value) is int and value >= 0, f"{path}: nonnegative integer required")
        return value
    require(
        isinstance(value, list)
        and len(value) == coordinates
        and all(type(item) is int and item >= 0 for item in value),
        f"{path}: {coordinates} nonnegative integer coordinates required",
    )
    return list(value)


def rank_key(value: int | list[int]) -> tuple[int, ...]:
    return (value,) if type(value) is int else tuple(value)


def critical_edge_subjects(t15_exact: dict[str, Any]) -> list[dict[str, Any]]:
    artifact_by_row = {
        artifact["row_id"]: artifact["artifact_id"]
        for artifact in t15_exact["interface_row_artifacts"]
    }
    output = []
    for row in t15_exact["interface_row_semantic_certificates"]:
        if row["classification"] != "critical-unranked":
            continue
        require(row["row_id"] in artifact_by_row, f"critical row {row['row_id']}: T15 artifact missing")
        for target in row["target_semantics"]:
            core = {
                "row_id": row["row_id"],
                "parent_global_state_id": row["parent_global_state_id"],
                "target_global_state_id": target["global_state_id"],
                "multiplicity": target["multiplicity"],
                "interface_row_semantic_certificate_sha256": row[
                    "interface_row_semantic_certificate_sha256"
                ],
                "interface_target_semantic_sha256": target["interface_target_semantic_sha256"],
                "t15_interface_row_artifact_id": artifact_by_row[row["row_id"]],
                "parent_t13_class_artifact_id": row["parent_t13_class_artifact_id"],
                "target_t13_class_artifact_id": target["t13_class_artifact_id"],
                "parent_final_global_weight": row["parent_final_global_weight"],
                "target_final_global_weight": target["final_global_weight"],
            }
            record = {
                "critical_edge_id": f"critical-edge::{catalogue.canonical_digest(core)[:32]}",
                **core,
            }
            record["critical_edge_subject_sha256"] = catalogue.canonical_digest(record)
            output.append(record)
    output.sort(
        key=lambda item: (
            item["parent_global_state_id"],
            item["target_global_state_id"],
            item["row_id"],
            item["critical_edge_id"],
        )
    )
    require(
        len({item["critical_edge_id"] for item in output}) == len(output),
        "critical edge subjects: duplicate ID",
    )
    return output


def exact_domain_record(raw: Any, has_edges: bool) -> dict[str, Any] | None:
    if not has_edges:
        require(raw is None, "rank_domain_record: must be null when no critical edges exist")
        return None
    require(isinstance(raw, dict), "rank_domain_record: object required")
    domain_id = nonempty_text(raw.get("rank_domain_id"), "rank_domain_id")
    kind = raw.get("rank_domain_kind")
    coordinates = raw.get("coordinate_count")
    require(
        kind in {"nonnegative-integer", "lexicographic-nonnegative-integers"},
        "rank_domain_kind: unsupported",
    )
    if kind == "nonnegative-integer":
        require(coordinates == 1, "coordinate_count: integer domain requires one coordinate")
    else:
        require(type(coordinates) is int and coordinates >= 2, "coordinate_count: lex domain requires >=2")
    status = raw.get("status")
    require(status in {"open", "proved"}, "rank_domain_record.status: open/proved required")
    locator = raw.get("verification_locator")
    digest = raw.get("verification_digest")
    if status == "open":
        require(locator is None and digest is None, "open rank domain requires null verification")
    else:
        require(
            locator == f"global-rank-domain-registry://{domain_id}"
            and isinstance(digest, str)
            and digest,
            "proved rank domain requires canonical verification",
        )
    core = {
        "rank_domain_id": domain_id,
        "rank_domain_kind": kind,
        "coordinate_count": coordinates,
        "status": status,
        "verification_locator": locator,
        "well_founded_statement": nonempty_text(
            raw.get("well_founded_statement"), "well_founded_statement"
        ),
        "evidence": nonempty_text(raw.get("evidence"), "rank domain evidence"),
        "note": nonempty_text(raw.get("note"), "rank domain note"),
    }
    output = {
        **core,
        "verification_digest": digest,
        "rank_domain_record_core_sha256": catalogue.canonical_digest(core),
    }
    output["rank_domain_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_domain_artifact(
    raw: Any, domain: dict[str, Any] | None
) -> dict[str, Any] | None:
    if domain is None or domain["status"] == "open":
        require(raw is None, "rank_domain_artifact: absent unless domain proved")
        return None
    require(isinstance(raw, dict), "rank_domain_artifact: object required")
    require(
        raw.get("artifact_kind") == "rank-domain-well-foundedness-proof",
        "rank_domain_artifact: wrong kind",
    )
    require(
        raw.get("rank_domain_record_core_sha256") == domain["rank_domain_record_core_sha256"],
        "rank_domain_artifact: domain binding mismatch",
    )
    output = {
        "artifact_id": nonempty_text(raw.get("artifact_id"), "rank domain artifact ID"),
        "artifact_kind": "rank-domain-well-foundedness-proof",
        "rank_domain_record_core_sha256": domain["rank_domain_record_core_sha256"],
        "proof_locator": nonempty_text(raw.get("proof_locator"), "rank domain proof locator"),
        "proof_digest": nonempty_text(raw.get("proof_digest"), "rank domain proof digest"),
        "proof_statement": nonempty_text(raw.get("proof_statement"), "rank domain proof statement"),
        "support_artifact_ids": exact_sorted_ids(
            raw.get("support_artifact_ids"), [], "rank domain support"
        ),
        "evidence": nonempty_text(raw.get("evidence"), "rank domain artifact evidence"),
    }
    require(output["artifact_id"] not in output["support_artifact_ids"], "rank domain self support")
    output["rank_domain_artifact_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_state_record(
    raw: dict[str, Any],
    *,
    state_id: str,
    class_artifact_id: str,
    domain: dict[str, Any],
    path: str,
) -> dict[str, Any]:
    require(raw.get("global_state_id") == state_id, f"{path}.global_state_id: mismatch")
    require(
        raw.get("t13_class_artifact_id") == class_artifact_id,
        f"{path}.t13_class_artifact_id: mismatch",
    )
    status = raw.get("status")
    require(status in {"open", "proved"}, f"{path}.status: open/proved required")
    value = raw.get("rank_value")
    locator = raw.get("verification_locator")
    digest = raw.get("verification_digest")
    if status == "open":
        require(value is None, f"{path}.rank_value: open requires null")
        require(locator is None and digest is None, f"{path}: open requires null verification")
        canonical_value = None
    else:
        canonical_value = canonical_rank_value(
            value, domain["rank_domain_kind"], domain["coordinate_count"], f"{path}.rank_value"
        )
        require(
            locator == f"global-rank-state-registry://{state_id}"
            and isinstance(digest, str)
            and digest,
            f"{path}: proved requires canonical verification",
        )
    core = {
        "global_state_id": state_id,
        "t13_class_artifact_id": class_artifact_id,
        "rank_domain_id": domain["rank_domain_id"],
        "rank_value": canonical_value,
        "status": status,
        "verification_locator": locator,
        "rank_statement": nonempty_text(raw.get("rank_statement"), f"{path}.rank_statement"),
        "evidence": nonempty_text(raw.get("evidence"), f"{path}.evidence"),
        "note": nonempty_text(raw.get("note"), f"{path}.note"),
    }
    output = {
        **core,
        "verification_digest": digest,
        "global_state_rank_record_core_sha256": catalogue.canonical_digest(core),
    }
    output["global_state_rank_record_sha256"] = catalogue.canonical_digest(output)
    return output


def graph_audit(
    states: list[str], edges: list[dict[str, Any]], rank_by_state: dict[str, int | list[int]]
) -> tuple[list[str], list[str], list[dict[str, Any]], int]:
    adjacency: dict[str, list[str]] = defaultdict(list)
    indegree = {state: 0 for state in states}
    for edge in edges:
        left = edge["parent_global_state_id"]
        right = edge["target_global_state_id"]
        adjacency[left].append(right)
        indegree[right] += 1
    queue = deque(sorted(state for state in states if indegree[state] == 0))
    topological = []
    while queue:
        state = queue.popleft()
        topological.append(state)
        for target in sorted(adjacency.get(state, [])):
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    require(len(topological) == len(states), "critical-edge graph contains a directed cycle")
    longest = {state: 0 for state in states}
    predecessor: dict[str, str | None] = {state: None for state in states}
    for state in topological:
        for target in sorted(adjacency.get(state, [])):
            candidate = longest[state] + 1
            if candidate > longest[target] or (
                candidate == longest[target]
                and (predecessor[target] is None or state < predecessor[target])
            ):
                longest[target] = candidate
                predecessor[target] = state
    terminal = min(states, key=lambda state: (-longest[state], state)) if states else None
    path = []
    current = terminal
    while current is not None:
        path.append(current)
        current = predecessor[current]
    path.reverse()
    components = []
    # Strict rank decrease makes SCCs singleton; publish the exact finite audit explicitly.
    for index, state in enumerate(sorted(states)):
        self_loop = any(
            edge["parent_global_state_id"] == state
            and edge["target_global_state_id"] == state
            for edge in edges
        )
        require(not self_loop, f"critical state {state}: self-loop")
        record = {
            "component_index": index,
            "state_ids": [state],
            "state_count": 1,
            "internal_critical_edge_count": 0,
            "minimum_rank_value": rank_by_state[state],
            "maximum_rank_value": rank_by_state[state],
        }
        record["critical_support_component_sha256"] = catalogue.canonical_digest(record)
        components.append(record)
    return topological, path, components, 0 if terminal is None else longest[terminal]


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    t15_certificate = certificate.get("interface_exhaustiveness_frontier_certificate")
    require(
        isinstance(t15_certificate, dict),
        "interface_exhaustiveness_frontier_certificate: object required",
    )
    t15_frontier.validate_certificate(t15_certificate)
    t15_exact = t15_frontier.exact_certificate(t15_certificate)

    for name in (
        "global_state_rank_records",
        "global_state_rank_artifacts",
        "global_state_rank_proof_bundles",
        "critical_edge_records",
        "critical_edge_semantic_certificates",
        "critical_edge_artifacts",
        "critical_edge_proof_bundles",
        "critical_topological_state_ids",
        "maximum_critical_path_state_ids",
        "critical_support_component_records",
    ):
        require(isinstance(certificate.get(name), list), f"{name}: list required")

    edge_subjects = critical_edge_subjects(t15_exact)
    state_class_artifacts: dict[str, str] = {}
    for edge in edge_subjects:
        for state_key, artifact_key in (
            ("parent_global_state_id", "parent_t13_class_artifact_id"),
            ("target_global_state_id", "target_t13_class_artifact_id"),
        ):
            state = edge[state_key]
            artifact = edge[artifact_key]
            previous = state_class_artifacts.get(state)
            require(previous is None or previous == artifact, f"state {state}: T13 artifact drift")
            state_class_artifacts[state] = artifact
    state_ids = sorted(state_class_artifacts)

    domain = exact_domain_record(certificate.get("rank_domain_record"), bool(edge_subjects))
    domain_artifact = exact_domain_artifact(certificate.get("rank_domain_artifact"), domain)
    if domain is not None and domain["status"] == "proved":
        require(domain_artifact is not None, "proved rank domain requires artifact")
        domain_bundle = {
            "rank_domain_record_core_sha256": domain["rank_domain_record_core_sha256"],
            "rank_domain_artifact_sha256": domain_artifact["rank_domain_artifact_sha256"],
        }
        domain_bundle["rank_domain_proof_bundle_sha256"] = catalogue.canonical_digest(domain_bundle)
        require(
            domain["verification_digest"] == domain_bundle["rank_domain_proof_bundle_sha256"],
            "rank domain verification digest mismatch",
        )
    else:
        domain_bundle = None

    raw_state_records = certificate["global_state_rank_records"]
    require(
        [record.get("global_state_id") for record in raw_state_records] == state_ids,
        "global_state_rank_records: exact canonical critical-state census required",
    )
    if state_ids:
        require(domain is not None, "critical states require rank domain")
        state_records = [
            exact_state_record(
                raw,
                state_id=state_id,
                class_artifact_id=state_class_artifacts[state_id],
                domain=domain,
                path=f"global_state_rank_records[{index}]",
            )
            for index, (raw, state_id) in enumerate(zip(raw_state_records, state_ids))
        ]
    else:
        state_records = []
    require(raw_state_records == state_records, "global_state_rank_records: noncanonical")

    state_artifact_groups = {state: [] for state in state_ids}
    for raw in certificate["global_state_rank_artifacts"]:
        state = raw.get("global_state_id")
        require(state in state_artifact_groups, f"state rank artifact: unknown state {state}")
        state_artifact_groups[state].append(raw)
    state_artifacts = []
    state_bundles = []
    state_artifact_by_id: dict[str, str] = {}
    state_record_by_id = {record["global_state_id"]: record for record in state_records}
    for record in state_records:
        state = record["global_state_id"]
        group = state_artifact_groups[state]
        if record["status"] == "open":
            require(not group, f"state {state}: open rank has artifact")
            continue
        require(
            len(group) == 1 and domain_artifact is not None,
            f"state {state}: one artifact and proved domain required",
        )
        raw = group[0]
        supports = sorted(
            [domain_artifact["artifact_id"], record["t13_class_artifact_id"]]
        )
        require(
            raw.get("artifact_kind") == "global-state-rank-proof"
            and raw.get("global_state_rank_record_core_sha256")
            == record["global_state_rank_record_core_sha256"],
            f"state {state}: artifact binding mismatch",
        )
        exact_sorted_ids(raw.get("support_artifact_ids"), supports, f"state {state} support")
        artifact = {
            "global_state_id": state,
            "artifact_id": nonempty_text(raw.get("artifact_id"), f"state {state} artifact ID"),
            "artifact_kind": "global-state-rank-proof",
            "global_state_rank_record_core_sha256": record[
                "global_state_rank_record_core_sha256"
            ],
            "proof_locator": nonempty_text(raw.get("proof_locator"), f"state {state} locator"),
            "proof_digest": nonempty_text(raw.get("proof_digest"), f"state {state} digest"),
            "proof_statement": nonempty_text(
                raw.get("proof_statement"), f"state {state} proof statement"
            ),
            "support_artifact_ids": supports,
            "evidence": nonempty_text(raw.get("evidence"), f"state {state} artifact evidence"),
        }
        require(artifact["artifact_id"] not in supports, f"state {state}: self support")
        artifact["global_state_rank_artifact_sha256"] = catalogue.canonical_digest(artifact)
        bundle = {
            "global_state_id": state,
            "global_state_rank_record_core_sha256": record[
                "global_state_rank_record_core_sha256"
            ],
            "global_state_rank_artifact_sha256": artifact[
                "global_state_rank_artifact_sha256"
            ],
        }
        bundle["global_state_rank_proof_bundle_sha256"] = catalogue.canonical_digest(bundle)
        require(
            record["verification_digest"] == bundle["global_state_rank_proof_bundle_sha256"],
            f"state {state}: verification digest mismatch",
        )
        state_artifacts.append(artifact)
        state_bundles.append(bundle)
        state_artifact_by_id[state] = artifact["artifact_id"]
    require(
        certificate["global_state_rank_artifacts"] == state_artifacts,
        "global_state_rank_artifacts: noncanonical",
    )
    require(
        certificate["global_state_rank_proof_bundles"] == state_bundles,
        "global_state_rank_proof_bundles: incorrect",
    )

    raw_edge_records = certificate["critical_edge_records"]
    require(
        len(raw_edge_records) == len(edge_subjects),
        "critical_edge_records: exact critical-edge cardinality required",
    )
    edge_records = []
    for index, (raw, subject) in enumerate(zip(raw_edge_records, edge_subjects)):
        path = f"critical_edge_records[{index}]"
        require(
            all(raw.get(key) == value for key, value in subject.items()),
            f"{path}: derived edge identity mismatch",
        )
        status = raw.get("status")
        require(status in {"open", "proved"}, f"{path}.status: open/proved required")
        locator = raw.get("verification_locator")
        digest = raw.get("verification_digest")
        if status == "open":
            require(locator is None and digest is None, f"{path}: open requires null verification")
        else:
            require(
                locator == f"global-rank-edge-registry://{subject['critical_edge_id']}"
                and isinstance(digest, str)
                and digest,
                f"{path}: proved requires canonical verification",
            )
        core = {
            **subject,
            "status": status,
            "verification_locator": locator,
            "note": nonempty_text(raw.get("note"), f"{path}.note"),
        }
        record = {
            **core,
            "verification_digest": digest,
            "critical_edge_record_core_sha256": catalogue.canonical_digest(core),
        }
        record["critical_edge_record_sha256"] = catalogue.canonical_digest(record)
        edge_records.append(record)
    require(raw_edge_records == edge_records, "critical_edge_records: noncanonical")

    semantic_groups = {record["critical_edge_id"]: [] for record in edge_records}
    for raw in certificate["critical_edge_semantic_certificates"]:
        edge_id = raw.get("critical_edge_id")
        require(edge_id in semantic_groups, f"critical edge semantic: unknown edge {edge_id}")
        semantic_groups[edge_id].append(raw)
    semantics = []
    semantic_by_edge: dict[str, dict[str, Any]] = {}
    for record in edge_records:
        edge_id = record["critical_edge_id"]
        group = semantic_groups[edge_id]
        if record["status"] == "open":
            require(not group, f"edge {edge_id}: open edge has semantic certificate")
            continue
        parent = state_record_by_id[record["parent_global_state_id"]]
        target = state_record_by_id[record["target_global_state_id"]]
        require(
            parent["status"] == target["status"] == "proved",
            f"edge {edge_id}: proved edge requires proved endpoint ranks",
        )
        require(len(group) == 1, f"edge {edge_id}: exactly one semantic certificate required")
        raw = group[0]
        require(
            raw.get("critical_edge_subject_sha256") == record["critical_edge_subject_sha256"],
            f"edge {edge_id}: subject binding mismatch",
        )
        require(
            raw.get("parent_global_state_rank_record_sha256")
            == parent["global_state_rank_record_sha256"]
            and raw.get("target_global_state_rank_record_sha256")
            == target["global_state_rank_record_sha256"],
            f"edge {edge_id}: endpoint rank binding mismatch",
        )
        require(
            raw.get("parent_rank_value") == parent["rank_value"]
            and raw.get("target_rank_value") == target["rank_value"],
            f"edge {edge_id}: rank value mismatch",
        )
        require(
            rank_key(target["rank_value"]) < rank_key(parent["rank_value"]),
            f"edge {edge_id}: rank does not strictly descend",
        )
        semantic = {
            **record,
            "parent_global_state_rank_record_sha256": parent[
                "global_state_rank_record_sha256"
            ],
            "target_global_state_rank_record_sha256": target[
                "global_state_rank_record_sha256"
            ],
            "parent_rank_value": parent["rank_value"],
            "target_rank_value": target["rank_value"],
            "strict_rank_descent": 1,
            "descent_statement": nonempty_text(
                raw.get("descent_statement"), f"edge {edge_id} descent statement"
            ),
            "evidence": nonempty_text(raw.get("evidence"), f"edge {edge_id} evidence"),
        }
        semantic.pop("verification_digest")
        semantic.pop("critical_edge_record_sha256")
        semantic["critical_edge_descent_semantic_sha256"] = catalogue.canonical_digest(semantic)
        semantics.append(semantic)
        semantic_by_edge[edge_id] = semantic
    require(
        certificate["critical_edge_semantic_certificates"] == semantics,
        "critical_edge_semantic_certificates: noncanonical",
    )

    edge_artifact_groups = {record["critical_edge_id"]: [] for record in edge_records}
    for raw in certificate["critical_edge_artifacts"]:
        edge_id = raw.get("critical_edge_id")
        require(edge_id in edge_artifact_groups, f"critical edge artifact: unknown edge {edge_id}")
        edge_artifact_groups[edge_id].append(raw)
    edge_artifacts = []
    edge_bundles = []
    for record in edge_records:
        edge_id = record["critical_edge_id"]
        group = edge_artifact_groups[edge_id]
        if record["status"] == "open":
            require(not group, f"edge {edge_id}: open edge has artifact")
            continue
        require(len(group) == 1, f"edge {edge_id}: exactly one artifact required")
        semantic = semantic_by_edge[edge_id]
        supports = sorted(
            [
                record["t15_interface_row_artifact_id"],
                state_artifact_by_id[record["parent_global_state_id"]],
                state_artifact_by_id[record["target_global_state_id"]],
            ]
        )
        raw = group[0]
        require(
            raw.get("artifact_kind") == "critical-edge-rank-descent-proof"
            and raw.get("critical_edge_descent_semantic_sha256")
            == semantic["critical_edge_descent_semantic_sha256"],
            f"edge {edge_id}: artifact binding mismatch",
        )
        exact_sorted_ids(raw.get("support_artifact_ids"), supports, f"edge {edge_id} support")
        artifact = {
            "critical_edge_id": edge_id,
            "artifact_id": nonempty_text(raw.get("artifact_id"), f"edge {edge_id} artifact ID"),
            "artifact_kind": "critical-edge-rank-descent-proof",
            "critical_edge_descent_semantic_sha256": semantic[
                "critical_edge_descent_semantic_sha256"
            ],
            "proof_locator": nonempty_text(raw.get("proof_locator"), f"edge {edge_id} locator"),
            "proof_digest": nonempty_text(raw.get("proof_digest"), f"edge {edge_id} digest"),
            "proof_statement": nonempty_text(
                raw.get("proof_statement"), f"edge {edge_id} proof statement"
            ),
            "support_artifact_ids": supports,
            "evidence": nonempty_text(raw.get("evidence"), f"edge {edge_id} artifact evidence"),
        }
        require(artifact["artifact_id"] not in supports, f"edge {edge_id}: self support")
        artifact["critical_edge_artifact_sha256"] = catalogue.canonical_digest(artifact)
        bundle = {
            "critical_edge_id": edge_id,
            "critical_edge_record_core_sha256": record["critical_edge_record_core_sha256"],
            "critical_edge_descent_semantic_sha256": semantic[
                "critical_edge_descent_semantic_sha256"
            ],
            "critical_edge_artifact_sha256": artifact["critical_edge_artifact_sha256"],
        }
        bundle["critical_edge_proof_bundle_sha256"] = catalogue.canonical_digest(bundle)
        require(
            record["verification_digest"] == bundle["critical_edge_proof_bundle_sha256"],
            f"edge {edge_id}: verification digest mismatch",
        )
        edge_artifacts.append(artifact)
        edge_bundles.append(bundle)
    require(
        certificate["critical_edge_artifacts"] == edge_artifacts,
        "critical_edge_artifacts: noncanonical",
    )
    require(
        certificate["critical_edge_proof_bundles"] == edge_bundles,
        "critical_edge_proof_bundles: incorrect",
    )
    all_internal_ids = [
        *([] if domain_artifact is None else [domain_artifact["artifact_id"]]),
        *(artifact["artifact_id"] for artifact in state_artifacts),
        *(artifact["artifact_id"] for artifact in edge_artifacts),
    ]
    require(len(all_internal_ids) == len(set(all_internal_ids)), "T16 internal artifact IDs duplicate")

    counts_state = Counter(record["status"] for record in state_records)
    counts_edge = Counter(record["status"] for record in edge_records)
    ready = int(
        t15_exact["claims"]["t15_interface_exhaustiveness_ready"]
        and (
            not edge_subjects
            or (
                domain is not None
                and domain["status"] == "proved"
                and domain_artifact is not None
                and counts_state["proved"] == len(state_records)
                and len(state_artifacts) == len(state_records)
                and counts_edge["proved"] == len(edge_records)
                and len(edge_artifacts) == len(edge_records)
            )
        )
    )

    rank_by_state = {
        record["global_state_id"]: record["rank_value"]
        for record in state_records
        if record["status"] == "proved"
    }
    if ready and edge_subjects:
        topological, longest_path, components, maximum_path = graph_audit(
            state_ids, semantics, rank_by_state
        )
    else:
        topological, longest_path, components, maximum_path = [], [], [], 0
    require(
        certificate["critical_topological_state_ids"] == topological,
        "critical_topological_state_ids: incorrect",
    )
    require(
        certificate["maximum_critical_path_state_ids"] == longest_path,
        "maximum_critical_path_state_ids: incorrect",
    )
    require(
        certificate["critical_support_component_records"] == components,
        "critical_support_component_records: incorrect",
    )

    bank = {
        "t15_interface_exhaustiveness_frontier_proof_bank_sha256": t15_exact["claims"][
            "interface_exhaustiveness_frontier_proof_bank_sha256"
        ],
        "critical_edge_subjects_sha256": catalogue.canonical_digest(edge_subjects),
        "rank_domain_record_sha256": None if domain is None else domain["rank_domain_record_sha256"],
        "rank_domain_artifact_sha256": (
            None if domain_artifact is None else domain_artifact["rank_domain_artifact_sha256"]
        ),
        "rank_domain_proof_bundle_sha256": (
            None if domain_bundle is None else domain_bundle["rank_domain_proof_bundle_sha256"]
        ),
        "global_state_rank_records_sha256": catalogue.canonical_digest(state_records),
        "global_state_rank_artifacts_sha256": catalogue.canonical_digest(state_artifacts),
        "global_state_rank_proof_bundles_sha256": catalogue.canonical_digest(state_bundles),
        "critical_edge_records_sha256": catalogue.canonical_digest(edge_records),
        "critical_edge_semantic_certificates_sha256": catalogue.canonical_digest(semantics),
        "critical_edge_artifacts_sha256": catalogue.canonical_digest(edge_artifacts),
        "critical_edge_proof_bundles_sha256": catalogue.canonical_digest(edge_bundles),
        "critical_topological_state_ids_sha256": catalogue.canonical_digest(topological),
        "maximum_critical_path_state_ids_sha256": catalogue.canonical_digest(longest_path),
        "critical_support_component_records_sha256": catalogue.canonical_digest(components),
    }
    bank["global_rank_frontier_proof_bank_sha256"] = catalogue.canonical_digest(bank)

    t14_certificate = t15_certificate["component_scale_frontier_certificate"]
    t13_certificate = t14_certificate["state_equivalence_frontier_certificate"]
    t07_certificate = t13_certificate["fate_transition_state_frontier_certificate"]
    t04_certificate = t07_certificate["block_interface_population_frontier_certificate"]
    registry = t04_certificate["atomic_target_artifact_registry_certificate"]
    target_artifacts.validate_certificate(registry)
    target_exact = target_artifacts.exact_certificate(registry)
    atomic_certificate = registry["current_frontier_execution_certificate"][
        "atomic_frontier_execution_certificate"
    ]
    atomic.validate_certificate(atomic_certificate)
    atomic_exact = atomic.exact_certificate(atomic_certificate)
    rule_certificate = t04_certificate["slot_candidate_population_frontier_certificate"][
        "rule_exhaustiveness_frontier_certificate"
    ]
    source_registry = rule_certificate["source_truth_frontier_execution_certificate"][
        "source_statement_truth_registry_certificate"
    ]
    obligation_certificate = source_registry["obligation_artifact_registry_certificate"]
    obligation_artifacts.validate_certificate(obligation_certificate)
    obligation_exact = obligation_artifacts.exact_certificate(obligation_certificate)
    closure_exact = closure.exact_certificate(
        obligation_certificate["all_n_implication_closure_certificate"]
    )

    closure_by_id = {
        record["obligation_id"]: record
        for record in closure_exact["obligation_closure_records"]
    }
    require(
        int(closure_by_id["GLOBAL_RANK_WELL_FOUNDED"]["closed"]) == ready,
        "T16 obligation closure mismatch",
    )
    obligation_rows = [
        artifact
        for artifact in obligation_exact["proof_artifacts"]
        if artifact["obligation_id"] == "GLOBAL_RANK_WELL_FOUNDED"
    ]
    require(
        len(obligation_rows) == (1 if ready else 0),
        "T16 obligation artifact presence mismatch",
    )
    if ready:
        t15_support = sorted(
            artifact["artifact_id"]
            for artifact in obligation_exact["proof_artifacts"]
            if artifact["obligation_id"] == "INTERFACE_RETURN_ROWS_EXHAUSTIVE"
        )
        artifact = obligation_rows[0]
        require(
            artifact["artifact_kind"] == "rank-well-foundedness-proof"
            and artifact["locator"] == "global-rank-frontier://GLOBAL_RANK_WELL_FOUNDED"
            and artifact["digest"] == bank["global_rank_frontier_proof_bank_sha256"]
            and artifact["support_artifact_ids"] == t15_support,
            "T16 obligation artifact mismatch",
        )

    result_by_id = {
        record["target_id"]: record for record in atomic_exact["target_result_records"]
    }
    require(
        int(result_by_id["T16_GLOBAL_RANK"]["effective_target_complete"]) == ready,
        "T16 atomic target mismatch",
    )
    target_artifact = {
        artifact["target_id"]: artifact
        for artifact in target_exact["atomic_target_artifacts"]
    }.get("T16_GLOBAL_RANK")
    if ready:
        require(
            target_artifact is not None
            and target_artifact["artifact_kind"] == "rank-well-foundedness-proof"
            and target_artifact["proof_locator"] == "global-rank-frontier://T16_GLOBAL_RANK"
            and target_artifact["proof_digest"] == bank["global_rank_frontier_proof_bank_sha256"],
            "T16 target artifact mismatch",
        )
    else:
        require(target_artifact is None, "open T16 target has artifact")

    claims = {
        "critical_interface_rows": sum(
            row["classification"] == "critical-unranked"
            for row in t15_exact["interface_row_semantic_certificates"]
        ),
        "critical_edge_subjects": len(edge_subjects),
        "critical_rank_states": len(state_ids),
        "open_rank_states": counts_state["open"],
        "proved_rank_states": counts_state["proved"],
        "open_critical_edges": counts_edge["open"],
        "proved_critical_edges": counts_edge["proved"],
        "maximum_critical_path_length": maximum_path,
        "critical_edge_graph_acyclic": int(ready),
        "every_critical_edge_strictly_descends_rank": int(ready),
        "rank_domain_well_founded_artifact_present": int(domain_artifact is not None),
        "exact_t15_critical_edge_census": 1,
        "strict_t15_rows_need_no_rank_edge": 1,
        "t16_global_rank_ready": ready,
        "all_n_proved_by_checker": 0,
        "open_rank_state_ids": [
            record["global_state_id"] for record in state_records if record["status"] == "open"
        ],
        "open_critical_edge_ids": [
            record["critical_edge_id"] for record in edge_records if record["status"] == "open"
        ],
        "global_rank_frontier_proof_bank_sha256": bank[
            "global_rank_frontier_proof_bank_sha256"
        ],
    }
    return {
        "rank_domain_record": domain,
        "rank_domain_artifact": domain_artifact,
        "rank_domain_proof_bundle": domain_bundle,
        "global_state_rank_records": state_records,
        "global_state_rank_artifacts": state_artifacts,
        "global_state_rank_proof_bundles": state_bundles,
        "critical_edge_subjects": edge_subjects,
        "critical_edge_records": edge_records,
        "critical_edge_semantic_certificates": semantics,
        "critical_edge_artifacts": edge_artifacts,
        "critical_edge_proof_bundles": edge_bundles,
        "critical_topological_state_ids": topological,
        "maximum_critical_path_state_ids": longest_path,
        "critical_support_component_records": components,
        "global_rank_frontier_proof_bank": bank,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, Any]:
    require(isinstance(certificate, dict), "certificate: object required")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key, value in exact.items():
        require(certificate.get(key) == value, f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(
        certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
        "certificate_sha256: incorrect",
    )
    claims = exact["claims"]
    return {
        "critical_rows": claims["critical_interface_rows"],
        "critical_edges": claims["critical_edge_subjects"],
        "rank_states": claims["critical_rank_states"],
        "maximum_path": claims["maximum_critical_path_length"],
        "ready": claims["t16_global_rank_ready"],
        "all_n": 0,
    }


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_global_rank_frontier.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
