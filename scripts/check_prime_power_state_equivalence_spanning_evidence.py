#!/usr/bin/env python3
"""Require spanning equivalence evidence for every shared cross-block global-state class.

Each shared class receives a canonical evidence tree on its local members. Every tree edge
names a bidirectional equivalence claim and source digest. Connectivity permits transitive
identification of all members while the exact n-1 edge condition rejects redundant or cyclic
claims. Passing proves documentary coverage relative to the supplied evidence statements;
it does not prove those statements mathematically true.
"""
from __future__ import annotations

import json
import sys
from collections import deque
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_cross_block_state_identification as identification


class StateEquivalenceEvidenceError(ValueError):
    """Raised when a global-state equivalence evidence tree is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise StateEquivalenceEvidenceError(message)


def member_ref(block_id: str, local_state_id: str) -> str:
    return f"{block_id}::{local_state_id}"


def exact_edge(record: dict[str, Any], path: str) -> dict[str, Any]:
    global_id = record.get("global_state_id")
    left_block = record.get("left_block_id")
    left_state = record.get("left_local_state_id")
    right_block = record.get("right_block_id")
    right_state = record.get("right_local_state_id")
    relation_id = record.get("relation_id")
    source_locator = record.get("source_locator")
    statement_digest = record.get("statement_digest")
    evidence = record.get("evidence")
    for name, value in (
        ("global_state_id", global_id), ("left_block_id", left_block),
        ("left_local_state_id", left_state), ("right_block_id", right_block),
        ("right_local_state_id", right_state), ("relation_id", relation_id),
        ("source_locator", source_locator), ("statement_digest", statement_digest),
        ("evidence", evidence),
    ):
        require(isinstance(value, str) and value, f"{path}.{name}: required")
    left = (left_block, left_state)
    right = (right_block, right_state)
    require(left != right, f"{path}: self equivalence edge")
    if right < left:
        left, right = right, left
    output = {
        "global_state_id": global_id,
        "left_block_id": left[0],
        "left_local_state_id": left[1],
        "right_block_id": right[0],
        "right_local_state_id": right[1],
        "relation_id": relation_id,
        "source_locator": source_locator,
        "statement_digest": statement_digest,
        "evidence": evidence,
    }
    output["equivalence_edge_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    id_certificate = certificate.get("state_identification_certificate")
    raw_edges = certificate.get("equivalence_edges")
    require(isinstance(id_certificate, dict), "state_identification_certificate: expected object")
    require(isinstance(raw_edges, list), "equivalence_edges: expected list")
    identification.validate_certificate(id_certificate)
    id_exact = identification.exact_certificate(id_certificate)

    edges = [exact_edge(record, f"equivalence_edges[{index}]") for index, record in enumerate(raw_edges)]
    require(raw_edges == edges, "equivalence_edges: canonical records or digests required")
    require(edges == sorted(edges, key=lambda item: (
        item["global_state_id"], item["left_block_id"], item["left_local_state_id"],
        item["right_block_id"], item["right_local_state_id"], item["relation_id"])),
        "equivalence_edges: canonical order required")
    pair_keys = [(
        record["global_state_id"], record["left_block_id"], record["left_local_state_id"],
        record["right_block_id"], record["right_local_state_id"]
    ) for record in edges]
    require(len(pair_keys) == len(set(pair_keys)), "equivalence_edges: duplicate unordered member pair")

    class_members: dict[str, set[tuple[str, str]]] = {}
    for record in id_exact["global_state_records"]:
        class_members[record["global_state_id"]] = {
            (member["block_id"], member["local_state_id"]) for member in record["members"]
        }
    edges_by_class: dict[str, list[dict[str, Any]]] = {key: [] for key in class_members}
    for edge in edges:
        global_id = edge["global_state_id"]
        require(global_id in class_members, f"equivalence edge: unknown global state {global_id}")
        left = (edge["left_block_id"], edge["left_local_state_id"])
        right = (edge["right_block_id"], edge["right_local_state_id"])
        require(left in class_members[global_id] and right in class_members[global_id],
                f"global state {global_id}: evidence edge endpoint outside class")
        edges_by_class[global_id].append(edge)

    class_records = []
    total_path_edges = 0
    for global_id in sorted(class_members):
        members = sorted(class_members[global_id])
        class_edges = edges_by_class[global_id]
        expected_edges = max(0, len(members) - 1)
        require(len(class_edges) == expected_edges,
                f"global state {global_id}: evidence must contain exactly member_count-1 edges")
        adjacency: dict[tuple[str, str], list[tuple[tuple[str, str], str]]] = {member: [] for member in members}
        for edge in class_edges:
            left = (edge["left_block_id"], edge["left_local_state_id"])
            right = (edge["right_block_id"], edge["right_local_state_id"])
            adjacency[left].append((right, edge["equivalence_edge_sha256"]))
            adjacency[right].append((left, edge["equivalence_edge_sha256"]))
        root = members[0]
        parent: dict[tuple[str, str], tuple[tuple[str, str] | None, str | None]] = {root: (None, None)}
        queue = deque([root])
        while queue:
            current = queue.popleft()
            for nxt, edge_sha in sorted(adjacency[current]):
                if nxt not in parent:
                    parent[nxt] = (current, edge_sha)
                    queue.append(nxt)
        require(set(parent) == set(members), f"global state {global_id}: evidence graph disconnected")
        paths = []
        for member in members:
            chain = []
            current = member
            while parent[current][0] is not None:
                previous, edge_sha = parent[current]
                chain.append(edge_sha)
                current = previous  # type: ignore[assignment]
            chain.reverse()
            total_path_edges += len(chain)
            paths.append({
                "member_ref": member_ref(member[0], member[1]),
                "root_path_edge_sha256s": chain,
                "path_length": len(chain),
            })
        record = {
            "global_state_id": global_id,
            "root_member_ref": member_ref(root[0], root[1]),
            "member_refs": [member_ref(block, state) for block, state in members],
            "member_count": len(members),
            "tree_edge_count": len(class_edges),
            "tree_edge_sha256s": sorted(edge["equivalence_edge_sha256"] for edge in class_edges),
            "root_paths": paths,
            "spanning_tree_complete": 1,
        }
        record["class_equivalence_sha256"] = catalogue.canonical_digest(record)
        class_records.append(record)

    claims = {
        "global_states": len(class_records),
        "shared_global_states": sum(record["member_count"] > 1 for record in class_records),
        "singleton_global_states": sum(record["member_count"] == 1 for record in class_records),
        "equivalence_edges": len(edges),
        "total_root_path_edges": total_path_edges,
        "maximum_tree_edges": max(record["tree_edge_count"] for record in class_records),
        "complete_spanning_equivalence_evidence": 1,
        "state_identification_sha256": id_certificate["certificate_sha256"],
        "equivalence_edges_sha256": catalogue.canonical_digest(edges),
        "class_records_sha256": catalogue.canonical_digest(class_records),
    }
    return {"equivalence_edges": edges, "class_equivalence_records": class_records, "claims": claims}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("equivalence_edges", "class_equivalence_records", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload), "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {"states": claims["global_states"], "shared": claims["shared_global_states"],
            "edges": claims["equivalence_edges"], "complete": claims["complete_spanning_equivalence_evidence"]}


def build_certificate(id_certificate: dict[str, Any], equivalence_edges: list[dict[str, Any]]) -> dict[str, Any]:
    canonical = [exact_edge(record, "equivalence_edge") for record in equivalence_edges]
    canonical.sort(key=lambda item: (
        item["global_state_id"], item["left_block_id"], item["left_local_state_id"],
        item["right_block_id"], item["right_local_state_id"], item["relation_id"]))
    certificate: dict[str, Any] = {
        "version": 1,
        "state_identification_certificate": id_certificate,
        "equivalence_edges": canonical,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_state_equivalence_spanning_evidence.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
