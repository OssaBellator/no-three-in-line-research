#!/usr/bin/env python3
"""Certify the global support graph, SCC condensation and critical-rank termination bound.

Support edges are reconstructed from positive target multiplicities in the global integer
quotient family. Every critical-descending row contributes rank-decreasing critical edges.
The critical-edge subgraph must be acyclic, its exact longest path is computed, and every
cycle in the full support graph is thereby forced to contain at least one strict row edge.

This is a finite graph/arithmetic consequence of the supplied quotient. It does not prove
that the quotient rows are the genuine exhaustive recurrence.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict, deque
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_global_integer_quotient_family as global_family


class GlobalSupportError(ValueError):
    """Raised when global support condensation or critical descent is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GlobalSupportError(message)


def tarjan(nodes: list[str], edges: set[tuple[str, str]]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = defaultdict(list)
    for left, right in sorted(edges):
        adjacency[left].append(right)
    index = 0
    stack: list[str] = []
    on_stack: set[str] = set()
    indices: dict[str, int] = {}
    low: dict[str, int] = {}
    components: list[list[str]] = []

    def visit(node: str) -> None:
        nonlocal index
        indices[node] = index
        low[node] = index
        index += 1
        stack.append(node)
        on_stack.add(node)
        for nxt in adjacency.get(node, []):
            if nxt not in indices:
                visit(nxt)
                low[node] = min(low[node], low[nxt])
            elif nxt in on_stack:
                low[node] = min(low[node], indices[nxt])
        if low[node] == indices[node]:
            component = []
            while True:
                current = stack.pop()
                on_stack.remove(current)
                component.append(current)
                if current == node:
                    break
            components.append(sorted(component))

    for node in sorted(nodes):
        if node not in indices:
            visit(node)
    components.sort(key=lambda component: component[0])
    return components


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    global_certificate = certificate.get("global_integer_family_certificate")
    require(isinstance(global_certificate, dict), "global_integer_family_certificate: expected object")
    global_family.validate_certificate(global_certificate)
    global_exact = global_family.exact_certificate(global_certificate)
    rows = global_exact["global_row_records"]
    quotient = global_exact["global_integer_quotient"]
    nodes = sorted(set(quotient["column_global_state_ids"]) | set(quotient["row_parent_global_state_ids"]))
    rank_by_state = {
        record["global_state_id"]: record["rank"]
        for record in global_certificate["interface_row_certificate"]["state_ranks"]
    }
    require(set(nodes) <= set(rank_by_state), "global support: missing rank for state")

    support_edges: set[tuple[str, str]] = set()
    strict_edges: set[tuple[str, str]] = set()
    critical_edges: set[tuple[str, str]] = set()
    edge_records = []
    for row in rows:
        parent = row["parent_global_state_id"]
        for target, multiplicity in row["target_multiplicities"]:
            require(type(multiplicity) is int and multiplicity > 0, f"row {row['row_id']}: bad target multiplicity")
            edge = (parent, target)
            support_edges.add(edge)
            if row["classification"] == "strict":
                strict_edges.add(edge)
            elif row["classification"] == "critical-descending":
                require(rank_by_state[target] < rank_by_state[parent],
                        f"row {row['row_id']}: critical edge does not descend rank")
                critical_edges.add(edge)
            else:
                raise GlobalSupportError(f"row {row['row_id']}: unsupported classification")
            edge_record = {
                "parent_global_state_id": parent,
                "target_global_state_id": target,
                "multiplicity": multiplicity,
                "row_id": row["row_id"],
                "row_classification": row["classification"],
                "parent_rank": rank_by_state[parent],
                "target_rank": rank_by_state[target],
            }
            edge_record["support_edge_record_sha256"] = catalogue.canonical_digest(edge_record)
            edge_records.append(edge_record)
    edge_records.sort(key=lambda item: (item["parent_global_state_id"], item["target_global_state_id"], item["row_id"]))

    components = tarjan(nodes, support_edges)
    component_of = {state: index for index, component in enumerate(components) for state in component}
    condensation_edges = sorted({
        (component_of[left], component_of[right])
        for left, right in support_edges if component_of[left] != component_of[right]
    })
    component_records = []
    cyclic_components = 0
    for index, component in enumerate(components):
        self_loop = any((state, state) in support_edges for state in component)
        cyclic = int(len(component) > 1 or self_loop)
        cyclic_components += cyclic
        internal_edges = sorted([edge for edge in support_edges if edge[0] in component and edge[1] in component])
        internal_strict = sorted([edge for edge in strict_edges if edge[0] in component and edge[1] in component])
        internal_critical = sorted([edge for edge in critical_edges if edge[0] in component and edge[1] in component])
        if cyclic:
            require(internal_strict, f"support SCC {index}: directed cycle has no strict edge")
        record = {
            "component_index": index,
            "state_ids": component,
            "state_count": len(component),
            "internal_edge_count": len(internal_edges),
            "internal_strict_edge_count": len(internal_strict),
            "internal_critical_edge_count": len(internal_critical),
            "cyclic_component": cyclic,
            "minimum_rank": min(rank_by_state[state] for state in component),
            "maximum_rank": max(rank_by_state[state] for state in component),
        }
        record["support_component_sha256"] = catalogue.canonical_digest(record)
        component_records.append(record)

    critical_adjacency: dict[str, list[str]] = defaultdict(list)
    indegree = {node: 0 for node in nodes}
    for left, right in critical_edges:
        critical_adjacency[left].append(right)
        indegree[right] += 1
    queue = deque(sorted(node for node in nodes if indegree[node] == 0))
    topological = []
    while queue:
        node = queue.popleft()
        topological.append(node)
        for nxt in sorted(critical_adjacency.get(node, [])):
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    require(len(topological) == len(nodes), "critical-edge support graph contains a cycle")
    longest = {node: 0 for node in nodes}
    predecessor: dict[str, str | None] = {node: None for node in nodes}
    for node in topological:
        for nxt in sorted(critical_adjacency.get(node, [])):
            candidate = longest[node] + 1
            if candidate > longest[nxt] or (candidate == longest[nxt] and (predecessor[nxt] is None or node < predecessor[nxt])):
                longest[nxt] = candidate
                predecessor[nxt] = node
    terminal = min((node for node in nodes), key=lambda node: (-longest[node], node))
    maximum_critical_path = longest[terminal]
    path = []
    current: str | None = terminal
    while current is not None:
        path.append(current)
        current = predecessor[current]
    path.reverse()
    maximum_rank = max(rank_by_state.values())
    minimum_rank = min(rank_by_state.values())
    require(maximum_critical_path <= maximum_rank - minimum_rank,
            "critical path exceeds strict integer-rank descent bound")

    condensation_records = []
    for left, right in condensation_edges:
        record = {"source_component_index": left, "target_component_index": right}
        record["condensation_edge_sha256"] = catalogue.canonical_digest(record)
        condensation_records.append(record)

    claims = {
        "global_states": len(nodes),
        "global_rows": len(rows),
        "support_edges": len(support_edges),
        "strict_edges": len(strict_edges),
        "critical_edges": len(critical_edges),
        "support_components": len(components),
        "cyclic_support_components": cyclic_components,
        "condensation_edges": len(condensation_edges),
        "maximum_critical_path_length": maximum_critical_path,
        "critical_path_rank_bound": maximum_rank - minimum_rank,
        "critical_edge_graph_acyclic": 1,
        "every_support_cycle_contains_strict_edge": 1,
        "global_family_complete": global_exact["claims"]["complete_global_integer_family"],
        "global_family_sha256": global_certificate["certificate_sha256"],
        "edge_records_sha256": catalogue.canonical_digest(edge_records),
        "component_records_sha256": catalogue.canonical_digest(component_records),
        "condensation_sha256": catalogue.canonical_digest(condensation_records),
    }
    return {
        "support_edge_records": edge_records,
        "support_component_records": component_records,
        "condensation_edge_records": condensation_records,
        "critical_topological_state_ids": topological,
        "maximum_critical_path_state_ids": path,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in (
        "support_edge_records", "support_component_records", "condensation_edge_records",
        "critical_topological_state_ids", "maximum_critical_path_state_ids", "claims",
    ):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload), "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {"states": claims["global_states"], "edges": claims["support_edges"],
            "components": claims["support_components"], "critical_bound": claims["maximum_critical_path_length"]}


def build_certificate(global_certificate: dict[str, Any]) -> dict[str, Any]:
    certificate: dict[str, Any] = {"version": 1, "global_integer_family_certificate": global_certificate}
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_global_support_condensation.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
