#!/usr/bin/env python3
"""Derive the minimal destroyed-resource scope partition for selected recurrent rows.

The simultaneous-credit checker accepts supplied resource-scope identifiers. This checker
removes that freedom: it reconstructs every selected row's complete literal destroyed-
triple universe, joins rows whose universes overlap, and defines scopes as the connected
components of that overlap graph. The resulting components are pairwise resource-disjoint.
"""
from __future__ import annotations

import json
import sys
from collections import Counter, deque
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_simultaneous_credit_nonreuse as simultaneous
import check_prime_power_witness_bound_destroyed_credit_routing as routing


class ScopePartitionError(ValueError):
    """Raised when a declared scope partition differs from literal resource overlap."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ScopePartitionError(message)


def point_triple_key(record: dict[str, Any]) -> str:
    points = sorted(tuple(point) for point in record["points"])
    return f"triple-{catalogue.canonical_digest(points)[:24]}"


def row_identity(record: dict[str, Any]) -> str:
    core = {
        "operation_instance_id": record["operation_instance_id"],
        "fibre_id": record["fibre_id"],
    }
    return f"row-{catalogue.canonical_digest(core)[:24]}"


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


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    simultaneous_certificate = certificate.get("simultaneous_credit_certificate")
    require(isinstance(simultaneous_certificate, dict),
            "simultaneous_credit_certificate: expected object")
    simultaneous.validate_certificate(simultaneous_certificate)
    simultaneous_exact = simultaneous.exact_certificate(simultaneous_certificate)

    row_records = []
    resources_by_row: dict[str, set[str]] = {}
    row_by_id: dict[str, dict[str, Any]] = {}
    for selected in simultaneous_exact["selected_rows"]:
        route_certificate = selected.get("routing_certificate")
        require(isinstance(route_certificate, dict),
                "selected row does not retain routing_certificate")
        routing.validate_certificate(route_certificate)
        route_exact = routing.exact_certificate(route_certificate)
        row_id = row_identity(selected)
        require(row_id not in row_by_id, "selected rows: row identity collision")
        resources = {point_triple_key(record) for record in route_exact["destroyed_triple_records"]}
        record = {
            "row_id": row_id,
            "operation_instance_id": selected["operation_instance_id"],
            "declared_scope_id": selected["resource_scope_id"],
            "parent_state_id": selected["parent_state_id"],
            "fibre_id": selected["fibre_id"],
            "literal_resource_keys": sorted(resources),
            "literal_resources": len(resources),
            "routing_certificate_sha256": route_certificate["certificate_sha256"],
        }
        record["row_resource_record_sha256"] = catalogue.canonical_digest(record)
        row_records.append(record)
        row_by_id[row_id] = record
        resources_by_row[row_id] = resources
    row_records.sort(key=lambda record: record["row_id"])

    edges: set[tuple[str, str]] = set()
    row_ids = [record["row_id"] for record in row_records]
    for left_index, left in enumerate(row_ids):
        for right in row_ids[left_index + 1:]:
            if resources_by_row[left] & resources_by_row[right]:
                edges.add((left, right))
    components = connected_components(row_ids, edges)

    scope_records = []
    derived_scope_by_row: dict[str, str] = {}
    component_resource_sets: list[set[str]] = []
    for rows in components:
        resources = set().union(*(resources_by_row[row_id] for row_id in rows))
        core = {"row_ids": rows, "literal_resource_keys": sorted(resources)}
        scope_id = f"scope-{catalogue.canonical_digest(core)[:24]}"
        for row_id in rows:
            derived_scope_by_row[row_id] = scope_id
        record = {
            "derived_scope_id": scope_id,
            "row_ids": rows,
            "literal_resource_keys": sorted(resources),
            "rows": len(rows),
            "literal_resources": len(resources),
        }
        record["scope_record_sha256"] = catalogue.canonical_digest(record)
        scope_records.append(record)
        component_resource_sets.append(resources)
    scope_records.sort(key=lambda record: record["derived_scope_id"])

    for index, left in enumerate(component_resource_sets):
        for right in component_resource_sets[index + 1:]:
            require(not (left & right), "derived scope components share a literal resource")
    for row in row_records:
        require(row["declared_scope_id"] == derived_scope_by_row[row["row_id"]],
                f"row {row['row_id']}: declared scope differs from overlap component")

    overlap_degree = Counter()
    for left, right in edges:
        overlap_degree[left] += 1
        overlap_degree[right] += 1
    claims = {
        "selected_rows": len(row_records),
        "derived_scopes": len(scope_records),
        "overlap_edges": len(edges),
        "rows_with_overlap": sum(overlap_degree[row_id] > 0 for row_id in row_ids),
        "isolated_rows": sum(overlap_degree[row_id] == 0 for row_id in row_ids),
        "total_row_resource_occurrences": sum(len(resources_by_row[row_id]) for row_id in row_ids),
        "distinct_literal_resources": len(set().union(*(resources_by_row[row_id] for row_id in row_ids))),
        "maximum_scope_rows": max(record["rows"] for record in scope_records),
        "maximum_scope_resources": max(record["literal_resources"] for record in scope_records),
        "scope_partition_exact": 1,
        "simultaneous_credit_sha256": simultaneous_certificate["certificate_sha256"],
        "row_resource_records_sha256": catalogue.canonical_digest(row_records),
        "overlap_edges_sha256": catalogue.canonical_digest([list(edge) for edge in sorted(edges)]),
        "scope_records_sha256": catalogue.canonical_digest(scope_records),
    }
    return {
        "row_resource_records": row_records,
        "resource_overlap_edges": [list(edge) for edge in sorted(edges)],
        "derived_scope_records": scope_records,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("row_resource_records", "resource_overlap_edges", "derived_scope_records", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {
        "rows": claims["selected_rows"],
        "scopes": claims["derived_scopes"],
        "overlap_edges": claims["overlap_edges"],
        "resources": claims["distinct_literal_resources"],
        "exact": claims["scope_partition_exact"],
    }


def build_certificate(simultaneous_certificate: dict[str, Any]) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "simultaneous_credit_certificate": simultaneous_certificate,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_resource_overlap_scope_partition.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
