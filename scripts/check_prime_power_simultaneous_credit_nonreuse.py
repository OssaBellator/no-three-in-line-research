#!/usr/bin/env python3
"""Validate global nonreuse across simultaneously selected witness-bound credit routes.

A witness-routing certificate is injective inside each alternative response. This checker
chooses the deterministic row-selected response for every simultaneously active row,
places literal destroyed triples into explicit resource scopes, and requires injectivity
of both physical destroyed resources and child obligations across the complete selected
execution family.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_labelled_recurrent_row_margin as row_margin
import check_prime_power_witness_bound_destroyed_credit_routing as routing


class SimultaneousCreditError(ValueError):
    """Raised when selected simultaneous routes reuse a resource or obligation."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SimultaneousCreditError(message)


def response_key(response: list[list[int]]) -> tuple[tuple[int, int], ...]:
    return row_margin.response_key(response)


def global_resource_id(scope_id: str, destroyed_record: dict[str, Any]) -> str:
    core = {"resource_scope_id": scope_id, "points": sorted(destroyed_record["points"])}
    return f"resource-{catalogue.canonical_digest(core)[:24]}"


def global_obligation_id(instance_id: str, witness_record: dict[str, Any]) -> str:
    core = {
        "operation_instance_id": instance_id,
        "witness_id": witness_record["witness_id"],
        "child": witness_record["child"],
    }
    return f"obligation-{catalogue.canonical_digest(core)[:24]}"


def exact_selected_row(record: dict[str, Any], path: str) -> dict[str, Any]:
    instance_id = record.get("operation_instance_id")
    scope_id = record.get("resource_scope_id")
    certificate = record.get("routing_certificate")
    require(isinstance(instance_id, str) and instance_id, f"{path}.operation_instance_id: required")
    require(isinstance(scope_id, str) and scope_id, f"{path}.resource_scope_id: required")
    require(isinstance(certificate, dict), f"{path}.routing_certificate: expected object")
    routing.validate_certificate(certificate)
    exact = routing.exact_certificate(certificate)
    row_certificate = certificate["row_margin_certificate"]
    selected_response = row_certificate["claims"]["selected_response"]
    selected_key = response_key(selected_response)
    route_map = {response_key(route["response"]): route for route in exact["response_routes"]}
    require(selected_key in route_map, f"{path}: selected response missing route record")
    selected_route = route_map[selected_key]
    destroyed_map = {item["destroyed_id"]: item for item in exact["destroyed_triple_records"]}
    witness_map = {item["witness_id"]: item for item in exact["child_witness_records"]}
    assignments = []
    for assignment in selected_route["assignments"]:
        destroyed = destroyed_map[assignment["destroyed_id"]]
        witness = witness_map[assignment["witness_id"]]
        output = {
            "destroyed_id": assignment["destroyed_id"],
            "witness_id": assignment["witness_id"],
            "child": assignment["child"],
            "global_resource_id": global_resource_id(scope_id, destroyed),
            "global_obligation_id": global_obligation_id(instance_id, witness),
            "resource_points": sorted(destroyed["points"]),
            "evidence": assignment["evidence"],
        }
        output["selected_assignment_sha256"] = catalogue.canonical_digest(output)
        assignments.append(output)
    assignments.sort(key=lambda item: (item["global_resource_id"], item["global_obligation_id"]))
    output = {
        "operation_instance_id": instance_id,
        "resource_scope_id": scope_id,
        "parent_state_id": row_certificate["linked_operation_certificate"]["linkage_certificate"]["source_manifest"]["parent"],
        "fibre_id": row_certificate["claims"]["fibre_id"],
        "selected_response": selected_response,
        "selected_assignments": assignments,
        "selected_routed_units": len(assignments),
        "routing_certificate_sha256": certificate["certificate_sha256"],
    }
    output["selected_row_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    execution_id = certificate.get("execution_id")
    raw_rows = certificate.get("selected_rows")
    require(isinstance(execution_id, str) and execution_id, "execution_id: nonempty string required")
    require(isinstance(raw_rows, list) and raw_rows, "selected_rows: nonempty list required")
    rows = [exact_selected_row(record, f"selected_rows[{index}]") for index, record in enumerate(raw_rows)]
    require(raw_rows == rows, "selected_rows: canonical records or digests required")
    require(rows == sorted(rows, key=lambda item: (item["resource_scope_id"], item["operation_instance_id"], item["fibre_id"])),
            "selected_rows: canonical order required")
    row_keys = [(row["operation_instance_id"], row["fibre_id"]) for row in rows]
    require(len(row_keys) == len(set(row_keys)), "selected_rows: duplicate operation-instance/fibre row")

    assignments = [assignment for row in rows for assignment in row["selected_assignments"]]
    resources = [assignment["global_resource_id"] for assignment in assignments]
    obligations = [assignment["global_obligation_id"] for assignment in assignments]
    require(len(resources) == len(set(resources)), "selected execution: destroyed resource reused across rows")
    require(len(obligations) == len(set(obligations)), "selected execution: child obligation paid more than once")

    scope_counts = Counter(row["resource_scope_id"] for row in rows)
    child_counts = Counter(assignment["child"] for assignment in assignments)
    claims = {
        "selected_rows": len(rows),
        "resource_scopes": len(scope_counts),
        "operation_instances": len({row["operation_instance_id"] for row in rows}),
        "selected_routed_units": len(assignments),
        "distinct_global_resources": len(set(resources)),
        "distinct_global_obligations": len(set(obligations)),
        "rows_with_selected_routes": sum(row["selected_routed_units"] > 0 for row in rows),
        "maximum_selected_row_routes": max([0] + [row["selected_routed_units"] for row in rows]),
        "scope_row_distribution": [[scope, scope_counts[scope]] for scope in sorted(scope_counts)],
        "child_route_distribution": [[child, child_counts[child]] for child in sorted(child_counts)],
        "selected_rows_sha256": catalogue.canonical_digest(rows),
        "selected_assignments_sha256": catalogue.canonical_digest(assignments),
    }
    return {"selected_rows": rows, "claims": claims}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("selected_rows", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload), "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {
        "rows": claims["selected_rows"],
        "scopes": claims["resource_scopes"],
        "instances": claims["operation_instances"],
        "routes": claims["selected_routed_units"],
        "resources": claims["distinct_global_resources"],
        "obligations": claims["distinct_global_obligations"],
    }


def build_certificate(execution_id: str, selected_rows: list[dict[str, Any]]) -> dict[str, Any]:
    canonical_rows = [exact_selected_row(record, "selected_row") for record in selected_rows]
    canonical_rows.sort(key=lambda item: (item["resource_scope_id"], item["operation_instance_id"], item["fibre_id"]))
    certificate: dict[str, Any] = {"version": 1, "execution_id": execution_id, "selected_rows": canonical_rows}
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_simultaneous_credit_nonreuse.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
