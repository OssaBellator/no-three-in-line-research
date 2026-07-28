#!/usr/bin/env python3
"""Audit edgewise lexicographic descent in the final global support graph.

The existing quotient proves row-level strict weight margin or zero-margin rank descent. This
checker asks for the stronger optional property that every individual positive target edge
strictly decreases the pair (global weight, rank) lexicographically. It publishes all failures
rather than rejecting a valid row-level quotient.

Edgewise lexicographic descent is sufficient for pathwise termination but is not necessary for
a multiset or branching induction proof.
"""
from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_global_support_condensation as support


class EdgewiseLexError(ValueError):
    """Raised when the edgewise lexicographic support audit is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise EdgewiseLexError(message)


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    support_certificate = certificate.get("global_support_condensation_certificate")
    require(isinstance(support_certificate, dict),
            "global_support_condensation_certificate: expected object")
    support.validate_certificate(support_certificate)
    support_exact = support.exact_certificate(support_certificate)
    global_certificate = support_certificate["global_integer_family_certificate"]
    interface_certificate = global_certificate["interface_row_certificate"]
    weight_by_state = {
        record["global_state_id"]: record["global_weight"]
        for record in interface_certificate["final_global_weight_records"]
    }
    rank_by_state = {
        record["global_state_id"]: record["rank"]
        for record in interface_certificate["state_ranks"]
    }

    audit_records = []
    descending_edges: set[tuple[str, str]] = set()
    violations = []
    class_counts: Counter[str] = Counter()
    positive_weight_drops = []
    positive_rank_drops = []
    for edge in support_exact["support_edge_records"]:
        parent = edge["parent_global_state_id"]
        target = edge["target_global_state_id"]
        parent_weight = weight_by_state[parent]
        target_weight = weight_by_state[target]
        parent_rank = rank_by_state[parent]
        target_rank = rank_by_state[target]
        weight_drop = parent_weight - target_weight
        rank_drop = parent_rank - target_rank
        if weight_drop > 0:
            classification = "strict-weight-drop"
            descending = 1
            positive_weight_drops.append(weight_drop)
        elif weight_drop == 0 and rank_drop > 0:
            classification = "equal-weight-rank-drop"
            descending = 1
            positive_rank_drops.append(rank_drop)
        else:
            classification = "nondecreasing-edge"
            descending = 0
        class_counts[classification] += 1
        if descending:
            descending_edges.add((parent, target))
        record = {
            "parent_global_state_id": parent,
            "target_global_state_id": target,
            "row_id": edge["row_id"],
            "row_classification": edge["row_classification"],
            "multiplicity": edge["multiplicity"],
            "parent_weight": parent_weight,
            "target_weight": target_weight,
            "weight_drop": weight_drop,
            "parent_rank": parent_rank,
            "target_rank": target_rank,
            "rank_drop": rank_drop,
            "edgewise_classification": classification,
            "edgewise_lex_descending": descending,
        }
        record["edgewise_audit_sha256"] = catalogue.canonical_digest(record)
        audit_records.append(record)
        if not descending:
            violations.append(record)
    audit_records.sort(key=lambda item: (item["parent_global_state_id"], item["target_global_state_id"], item["row_id"]))
    violations.sort(key=lambda item: (item["parent_global_state_id"], item["target_global_state_id"], item["row_id"]))

    nodes = sorted(set(weight_by_state) | {value for edge in descending_edges for value in edge})
    adjacency: dict[str, list[str]] = defaultdict(list)
    indegree = {node: 0 for node in nodes}
    for left, right in sorted(descending_edges):
        adjacency[left].append(right)
        indegree[right] += 1
    queue = deque(sorted(node for node in nodes if indegree[node] == 0))
    topological = []
    while queue:
        node = queue.popleft()
        topological.append(node)
        for nxt in sorted(adjacency.get(node, [])):
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    require(len(topological) == len(nodes), "descending edge graph contains a cycle")

    longest = {node: 0 for node in nodes}
    predecessor: dict[str, str | None] = {node: None for node in nodes}
    for node in topological:
        for nxt in sorted(adjacency.get(node, [])):
            candidate = longest[node] + 1
            if candidate > longest[nxt] or (
                candidate == longest[nxt]
                and (predecessor[nxt] is None or node < predecessor[nxt])
            ):
                longest[nxt] = candidate
                predecessor[nxt] = node
    terminal = min(nodes, key=lambda node: (-longest[node], node))
    path = []
    current: str | None = terminal
    while current is not None:
        path.append(current)
        current = predecessor[current]
    path.reverse()

    complete = int(not violations and support_exact["claims"]["global_family_complete"])
    claims = {
        "global_states": len(nodes),
        "support_edge_records": len(audit_records),
        "edgewise_descending_edges": len(audit_records) - len(violations),
        "nondecreasing_edges": len(violations),
        "maximum_edgewise_lex_path_length": longest[terminal],
        "minimum_positive_weight_drop": min(positive_weight_drops, default=0),
        "minimum_positive_rank_drop_at_equal_weight": min(positive_rank_drops, default=0),
        "edgewise_classification_distribution": [[key, class_counts[key]] for key in sorted(class_counts)],
        "all_support_edges_lex_descending": int(not violations),
        "complete_edgewise_lex_termination": complete,
        "edgewise_criterion_sufficient_not_necessary": 1,
        "global_support_condensation_sha256": support_certificate["certificate_sha256"],
        "audit_records_sha256": catalogue.canonical_digest(audit_records),
        "violation_records_sha256": catalogue.canonical_digest(violations),
    }
    return {
        "edgewise_audit_records": audit_records,
        "nondecreasing_edge_records": violations,
        "edgewise_topological_state_ids": topological,
        "maximum_edgewise_lex_path_state_ids": path,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in (
        "edgewise_audit_records", "nondecreasing_edge_records", "edgewise_topological_state_ids",
        "maximum_edgewise_lex_path_state_ids", "claims",
    ):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {"edges": claims["support_edge_records"], "violations": claims["nondecreasing_edges"],
            "path_bound": claims["maximum_edgewise_lex_path_length"],
            "complete": claims["complete_edgewise_lex_termination"]}


def build_certificate(support_certificate: dict[str, Any]) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "global_support_condensation_certificate": support_certificate,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_edgewise_lexicographic_support.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
