#!/usr/bin/env python3
"""Validate acyclic, dependency-aligned support among typed semantic proof artifacts.

The typed obligation artifact registry checks bundle coverage but permits arbitrary support
references. This checker turns those references into a finite DAG, requires support to come
only from the same obligation or one of its semantic dependencies, and requires every proved
non-root bundle to cite at least one artifact from each immediate dependency obligation.

Passing proves documentary support structure only. It does not verify any artifact statement.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict, deque
from pathlib import Path
from typing import Any

import check_prime_power_all_n_implication_closure as closure
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_obligation_artifact_registry as registry


class ArtifactSupportDagError(ValueError):
    """Raised when the proof-artifact support graph is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ArtifactSupportDagError(message)


def transitive_dependencies() -> dict[str, set[str]]:
    output: dict[str, set[str]] = {}
    for obligation_id, dependencies in closure.OBLIGATION_DEPENDENCIES.items():
        values = set(dependencies)
        for dependency in dependencies:
            values.update(output[dependency])
        output[obligation_id] = values
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    registry_certificate = certificate.get("obligation_artifact_registry_certificate")
    require(isinstance(registry_certificate, dict),
            "obligation_artifact_registry_certificate: expected object")
    registry.validate_certificate(registry_certificate)
    registry_exact = registry.exact_certificate(registry_certificate)
    artifacts = registry_exact["proof_artifacts"]
    artifact_by_id = {record["artifact_id"]: record for record in artifacts}
    transitive = transitive_dependencies()

    adjacency: dict[str, list[str]] = defaultdict(list)
    indegree = {artifact_id: 0 for artifact_id in artifact_by_id}
    edge_records = []
    for artifact in artifacts:
        target_id = artifact["artifact_id"]
        target_obligation = artifact["obligation_id"]
        allowed_obligations = transitive[target_obligation] | {target_obligation}
        for source_id in artifact["support_artifact_ids"]:
            source = artifact_by_id[source_id]
            require(source["obligation_id"] in allowed_obligations,
                    f"artifact {target_id}: support obligation {source['obligation_id']} is not admissible")
            adjacency[source_id].append(target_id)
            indegree[target_id] += 1
            edge = {
                "source_artifact_id": source_id,
                "source_obligation_id": source["obligation_id"],
                "target_artifact_id": target_id,
                "target_obligation_id": target_obligation,
                "same_obligation_support": int(source["obligation_id"] == target_obligation),
            }
            edge["artifact_support_edge_sha256"] = catalogue.canonical_digest(edge)
            edge_records.append(edge)
    edge_records.sort(key=lambda item: (item["source_artifact_id"], item["target_artifact_id"]))

    queue = deque(sorted(artifact_id for artifact_id, value in indegree.items() if value == 0))
    topological = []
    while queue:
        current = queue.popleft()
        topological.append(current)
        for nxt in sorted(adjacency.get(current, [])):
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    require(len(topological) == len(artifacts), "proof artifact support graph contains a cycle")

    depth: dict[str, int] = {}
    ancestors: dict[str, set[str]] = {}
    for artifact_id in topological:
        supports = artifact_by_id[artifact_id]["support_artifact_ids"]
        if supports:
            depth[artifact_id] = 1 + max(depth[support_id] for support_id in supports)
            values = set(supports)
            for support_id in supports:
                values.update(ancestors[support_id])
            ancestors[artifact_id] = values
        else:
            depth[artifact_id] = 0
            ancestors[artifact_id] = set()

    support_records = []
    for artifact_id in sorted(artifact_by_id):
        artifact = artifact_by_id[artifact_id]
        record = {
            "artifact_id": artifact_id,
            "obligation_id": artifact["obligation_id"],
            "direct_support_artifact_ids": list(artifact["support_artifact_ids"]),
            "transitive_support_artifact_ids": sorted(ancestors[artifact_id]),
            "support_depth": depth[artifact_id],
            "foundation_artifact": int(not artifact["support_artifact_ids"]),
        }
        record["artifact_support_record_sha256"] = catalogue.canonical_digest(record)
        support_records.append(record)

    artifacts_by_obligation: dict[str, list[dict[str, Any]]] = {
        obligation_id: [] for obligation_id in closure.OBLIGATION_DEPENDENCIES
    }
    for artifact in artifacts:
        artifacts_by_obligation[artifact["obligation_id"]].append(artifact)

    obligation_records = []
    for obligation_id, dependencies in closure.OBLIGATION_DEPENDENCIES.items():
        bundle = artifacts_by_obligation[obligation_id]
        cited_obligations = sorted({
            artifact_by_id[support_id]["obligation_id"]
            for artifact in bundle for support_id in artifact["support_artifact_ids"]
        })
        bundle_status = next(
            record["declared_status"] for record in registry_exact["artifact_bundle_records"]
            if record["obligation_id"] == obligation_id
        )
        if bundle_status == "proved":
            missing = [dependency for dependency in dependencies if dependency not in cited_obligations]
            require(not missing,
                    f"obligation {obligation_id}: bundle does not cite immediate dependency artifacts {missing}")
        record = {
            "obligation_id": obligation_id,
            "declared_status": bundle_status,
            "immediate_dependency_ids": list(dependencies),
            "cited_support_obligation_ids": cited_obligations,
            "dependency_artifact_coverage": int(
                all(dependency in cited_obligations for dependency in dependencies)
                if bundle_status == "proved" else not bundle
            ),
            "artifact_ids": [artifact["artifact_id"] for artifact in bundle],
        }
        record["obligation_support_record_sha256"] = catalogue.canonical_digest(record)
        obligation_records.append(record)

    claims = {
        "proof_artifacts": len(artifacts),
        "support_edges": len(edge_records),
        "foundation_artifacts": sum(record["foundation_artifact"] for record in support_records),
        "maximum_support_depth": max((record["support_depth"] for record in support_records), default=0),
        "acyclic_artifact_support": 1,
        "dependency_aligned_support": 1,
        "immediate_dependency_artifact_coverage": 1,
        "artifact_registry_sha256": registry_certificate["certificate_sha256"],
        "support_edges_sha256": catalogue.canonical_digest(edge_records),
        "artifact_support_records_sha256": catalogue.canonical_digest(support_records),
        "obligation_support_records_sha256": catalogue.canonical_digest(obligation_records),
    }
    return {
        "artifact_support_edge_records": edge_records,
        "artifact_support_records": support_records,
        "obligation_support_records": obligation_records,
        "artifact_topological_order": topological,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in (
        "artifact_support_edge_records", "artifact_support_records", "obligation_support_records",
        "artifact_topological_order", "claims",
    ):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {"artifacts": claims["proof_artifacts"], "edges": claims["support_edges"],
            "depth": claims["maximum_support_depth"], "acyclic": claims["acyclic_artifact_support"]}


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
        raise SystemExit("usage: check_prime_power_artifact_support_dag.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
