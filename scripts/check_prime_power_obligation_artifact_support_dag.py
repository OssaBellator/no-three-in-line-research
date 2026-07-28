#!/usr/bin/env python3
"""Validate noncircular, dependency-aligned support for typed proof artifacts.

The typed artifact registry records direct support-artifact IDs but, by itself, does not reject
support cycles or support from unrelated/downstream semantic obligations. This checker builds
the exact artifact-support graph, requires every edge to stay within one obligation or point to
a transitive prerequisite obligation, rejects cycles, and verifies that each proved obligation's
bundle reaches every artifact in each immediate prerequisite bundle.

This remains a documentary integrity check. It does not verify the mathematical truth or
sufficiency of any artifact.
"""
from __future__ import annotations

import heapq
import json
import sys
from pathlib import Path
from typing import Any

import check_prime_power_all_n_implication_closure as closure
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_obligation_artifact_registry as artifacts


class ObligationArtifactSupportError(ValueError):
    """Raised when proof-artifact support is circular or dependency-inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ObligationArtifactSupportError(message)


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    registry_certificate = certificate.get("obligation_artifact_registry_certificate")
    require(isinstance(registry_certificate, dict),
            "obligation_artifact_registry_certificate: expected object")
    artifacts.validate_certificate(registry_certificate)
    registry_exact = artifacts.exact_certificate(registry_certificate)
    closure_certificate = registry_certificate["all_n_implication_closure_certificate"]
    closure.validate_certificate(closure_certificate)
    closure_exact = closure.exact_certificate(closure_certificate)

    obligation_order = list(closure.OBLIGATION_DEPENDENCIES)
    transitive_dependencies: dict[str, set[str]] = {}
    for obligation_id in obligation_order:
        dependencies = closure.OBLIGATION_DEPENDENCIES[obligation_id]
        expanded = set(dependencies)
        for dependency in dependencies:
            expanded.update(transitive_dependencies[dependency])
        transitive_dependencies[obligation_id] = expanded

    proof_artifacts = registry_exact["proof_artifacts"]
    artifact_by_id = {record["artifact_id"]: record for record in proof_artifacts}
    bundles_by_id = {
        record["obligation_id"]: record
        for record in registry_exact["artifact_bundle_records"]
    }
    obligation_by_id = {
        record["obligation_id"]: record
        for record in closure_exact["proof_obligations"]
    }

    support_edges = []
    supports_by_artifact: dict[str, list[str]] = {}
    dependents_by_artifact: dict[str, list[str]] = {artifact_id: [] for artifact_id in artifact_by_id}
    indegree: dict[str, int] = {artifact_id: 0 for artifact_id in artifact_by_id}
    for record in proof_artifacts:
        artifact_id = record["artifact_id"]
        obligation_id = record["obligation_id"]
        direct_support_ids = list(record["support_artifact_ids"])
        supports_by_artifact[artifact_id] = direct_support_ids
        for support_id in direct_support_ids:
            support_record = artifact_by_id[support_id]
            support_obligation_id = support_record["obligation_id"]
            require(
                support_obligation_id == obligation_id
                or support_obligation_id in transitive_dependencies[obligation_id],
                f"artifact {artifact_id}: support {support_id} belongs to unrelated or downstream obligation",
            )
            edge = {
                "support_artifact_id": support_id,
                "supported_artifact_id": artifact_id,
                "support_obligation_id": support_obligation_id,
                "supported_obligation_id": obligation_id,
                "same_obligation": int(support_obligation_id == obligation_id),
            }
            edge["artifact_support_edge_sha256"] = catalogue.canonical_digest(edge)
            support_edges.append(edge)
            dependents_by_artifact[support_id].append(artifact_id)
            indegree[artifact_id] += 1

    support_edges.sort(key=lambda item: (item["supported_artifact_id"], item["support_artifact_id"]))
    for artifact_id in dependents_by_artifact:
        dependents_by_artifact[artifact_id].sort()

    queue = [artifact_id for artifact_id, degree in indegree.items() if degree == 0]
    heapq.heapify(queue)
    topological_order = []
    while queue:
        artifact_id = heapq.heappop(queue)
        topological_order.append(artifact_id)
        for dependent_id in dependents_by_artifact[artifact_id]:
            indegree[dependent_id] -= 1
            if indegree[dependent_id] == 0:
                heapq.heappush(queue, dependent_id)
    require(len(topological_order) == len(proof_artifacts),
            "proof_artifacts: support graph contains a directed cycle")

    transitive_support: dict[str, set[str]] = {}
    support_depth: dict[str, int] = {}
    root_supports: dict[str, set[str]] = {}
    for artifact_id in topological_order:
        direct = supports_by_artifact[artifact_id]
        expanded: set[str] = set(direct)
        roots: set[str] = set()
        if direct:
            for support_id in direct:
                expanded.update(transitive_support[support_id])
                roots.update(root_supports[support_id])
            depth = 1 + max(support_depth[support_id] for support_id in direct)
        else:
            roots.add(artifact_id)
            depth = 0
        transitive_support[artifact_id] = expanded
        root_supports[artifact_id] = roots
        support_depth[artifact_id] = depth

    artifact_support_records = []
    for record in proof_artifacts:
        artifact_id = record["artifact_id"]
        support_record = {
            "artifact_id": artifact_id,
            "obligation_id": record["obligation_id"],
            "direct_support_artifact_ids": supports_by_artifact[artifact_id],
            "transitive_support_artifact_ids": sorted(transitive_support[artifact_id]),
            "support_root_artifact_ids": sorted(root_supports[artifact_id]),
            "support_depth": support_depth[artifact_id],
        }
        support_record["artifact_support_record_sha256"] = catalogue.canonical_digest(support_record)
        artifact_support_records.append(support_record)

    obligation_support_records = []
    proved_complete = 0
    for obligation_id in obligation_order:
        obligation = obligation_by_id[obligation_id]
        bundle = bundles_by_id[obligation_id]
        artifact_ids = list(bundle["artifact_ids"])
        reachable: set[str] = set()
        for artifact_id in artifact_ids:
            reachable.update(transitive_support[artifact_id])
        immediate_dependencies = list(closure.OBLIGATION_DEPENDENCIES[obligation_id])
        required_dependency_artifact_ids = sorted(
            artifact_id
            for dependency_id in immediate_dependencies
            for artifact_id in bundles_by_id[dependency_id]["artifact_ids"]
        )
        reachable_dependency_artifact_ids = sorted(
            set(required_dependency_artifact_ids) & reachable
        )
        missing_dependency_artifact_ids = sorted(
            set(required_dependency_artifact_ids) - reachable
        )
        dependency_support_complete = int(not missing_dependency_artifact_ids)
        if obligation["status"] == "proved":
            require(
                dependency_support_complete,
                f"obligation {obligation_id}: artifact bundle does not support every immediate dependency artifact",
            )
            proved_complete += 1
        record = {
            "obligation_id": obligation_id,
            "declared_status": obligation["status"],
            "immediate_dependency_ids": immediate_dependencies,
            "artifact_ids": artifact_ids,
            "required_dependency_artifact_ids": required_dependency_artifact_ids,
            "reachable_dependency_artifact_ids": reachable_dependency_artifact_ids,
            "missing_dependency_artifact_ids": missing_dependency_artifact_ids,
            "dependency_support_complete": dependency_support_complete,
            "bundle_transitive_support_artifact_ids": sorted(reachable),
        }
        record["obligation_support_record_sha256"] = catalogue.canonical_digest(record)
        obligation_support_records.append(record)

    root_artifacts = sorted(
        artifact_id for artifact_id, direct in supports_by_artifact.items() if not direct
    )
    max_depth = max(support_depth.values(), default=0)
    claims = {
        "proof_obligations": len(obligation_order),
        "proof_artifacts": len(proof_artifacts),
        "artifact_support_edges": len(support_edges),
        "artifact_support_roots": len(root_artifacts),
        "maximum_artifact_support_depth": max_depth,
        "proved_obligations": sum(obligation_by_id[obligation_id]["status"] == "proved"
                                  for obligation_id in obligation_order),
        "proved_obligations_with_complete_dependency_support": proved_complete,
        "artifact_support_acyclic": 1,
        "artifact_support_dependency_aligned": 1,
        "exact_dependency_artifact_support_coverage": 1,
        "root_artifact_ids": root_artifacts,
        "artifact_topological_order": topological_order,
        "closure_sha256": closure_certificate["certificate_sha256"],
        "artifact_registry_sha256": registry_certificate["certificate_sha256"],
        "artifact_support_edges_sha256": catalogue.canonical_digest(support_edges),
        "artifact_support_records_sha256": catalogue.canonical_digest(artifact_support_records),
        "obligation_support_records_sha256": catalogue.canonical_digest(obligation_support_records),
    }
    return {
        "artifact_support_edges": support_edges,
        "artifact_support_records": artifact_support_records,
        "obligation_support_records": obligation_support_records,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("artifact_support_edges", "artifact_support_records",
                "obligation_support_records", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {
        "artifacts": claims["proof_artifacts"],
        "edges": claims["artifact_support_edges"],
        "depth": claims["maximum_artifact_support_depth"],
        "acyclic": claims["artifact_support_acyclic"],
    }


def build_certificate(registry_certificate: dict[str, Any]) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "obligation_artifact_registry_certificate": registry_certificate,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: check_prime_power_obligation_artifact_support_dag.py certificate.json"
        )
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
