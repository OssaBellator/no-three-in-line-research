#!/usr/bin/env python3
"""Compute the exact blocker frontier and parallel completion schedule for all-n obligations.

The fixed obligation DAG is treated as an AND-dependency graph. The checker reconstructs every
transitive blocker set, the currently actionable frontier, downstream impact of each frontier
item, and the minimum number of dependency waves required if every open proof artifact were
supplied as soon as its prerequisites allow.

This is planning arithmetic over declared proof status. It does not establish any obligation.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import check_prime_power_all_n_implication_closure as closure
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_obligation_artifact_registry as artifacts


class ObligationScheduleError(ValueError):
    """Raised when the proof-obligation blocker schedule is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ObligationScheduleError(message)


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
    closure_by_id = {record["obligation_id"]: record
                     for record in closure_exact["obligation_closure_records"]}

    transitive: dict[str, set[str]] = {}
    waves: dict[str, int] = {}
    chains: dict[str, list[str]] = {}
    for obligation_id in obligation_order:
        dependencies = closure.OBLIGATION_DEPENDENCIES[obligation_id]
        dependency_closure: set[str] = set(dependencies)
        for dependency in dependencies:
            dependency_closure.update(transitive[dependency])
        transitive[obligation_id] = dependency_closure
        if closure_by_id[obligation_id]["closed"]:
            waves[obligation_id] = 0
            chains[obligation_id] = []
        else:
            open_dependencies = [dependency for dependency in dependencies
                                 if not closure_by_id[dependency]["closed"]]
            if open_dependencies:
                predecessor = min(open_dependencies, key=lambda item: (-waves[item], item))
                waves[obligation_id] = waves[predecessor] + 1
                chains[obligation_id] = chains[predecessor] + [obligation_id]
            else:
                waves[obligation_id] = 1
                chains[obligation_id] = [obligation_id]

    schedule_records = []
    for obligation_id in obligation_order:
        open_blockers = sorted(
            dependency for dependency in transitive[obligation_id] | {obligation_id}
            if not closure_by_id[dependency]["closed"]
        )
        downstream = [
            target for target in obligation_order
            if not closure_by_id[target]["closed"]
            and (target == obligation_id or obligation_id in transitive[target])
        ]
        record = {
            "obligation_id": obligation_id,
            "closed": closure_by_id[obligation_id]["closed"],
            "transitive_dependency_ids": sorted(transitive[obligation_id]),
            "open_blocker_ids": open_blockers,
            "open_blocker_count": len(open_blockers),
            "earliest_completion_wave": waves[obligation_id],
            "longest_open_dependency_chain": chains[obligation_id],
            "downstream_unclosed_obligation_ids": downstream,
            "downstream_unclosed_impact": len(downstream),
        }
        record["obligation_schedule_sha256"] = catalogue.canonical_digest(record)
        schedule_records.append(record)

    frontier = [
        obligation_id for obligation_id in obligation_order
        if not closure_by_id[obligation_id]["closed"]
        and all(closure_by_id[dependency]["closed"]
                for dependency in closure.OBLIGATION_DEPENDENCIES[obligation_id])
    ]
    frontier_records = []
    for obligation_id in frontier:
        schedule_record = next(record for record in schedule_records if record["obligation_id"] == obligation_id)
        bundle = next(record for record in registry_exact["artifact_bundle_records"]
                      if record["obligation_id"] == obligation_id)
        record = {
            "obligation_id": obligation_id,
            "required_artifact_kinds": bundle["required_artifact_kinds"],
            "downstream_unclosed_impact": schedule_record["downstream_unclosed_impact"],
            "earliest_completion_wave": schedule_record["earliest_completion_wave"],
        }
        record["frontier_record_sha256"] = catalogue.canonical_digest(record)
        frontier_records.append(record)

    root = "GLOBAL_QUOTIENT_IMPLIES_ALL_N"
    root_schedule = next(record for record in schedule_records if record["obligation_id"] == root)
    claims = {
        "proof_obligations": len(obligation_order),
        "closed_obligations": sum(record["closed"] for record in schedule_records),
        "unclosed_obligations": sum(not record["closed"] for record in schedule_records),
        "current_frontier_obligations": len(frontier_records),
        "minimum_parallel_completion_waves": root_schedule["earliest_completion_wave"],
        "root_open_blockers": root_schedule["open_blocker_count"],
        "root_longest_open_dependency_chain_length": len(root_schedule["longest_open_dependency_chain"]),
        "root_ready": int(root_schedule["closed"]),
        "closure_sha256": closure_certificate["certificate_sha256"],
        "artifact_registry_sha256": registry_certificate["certificate_sha256"],
        "schedule_records_sha256": catalogue.canonical_digest(schedule_records),
        "frontier_records_sha256": catalogue.canonical_digest(frontier_records),
    }
    return {"obligation_schedule_records": schedule_records,
            "current_frontier_records": frontier_records,
            "claims": claims}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("obligation_schedule_records", "current_frontier_records", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {"closed": claims["closed_obligations"], "frontier": claims["current_frontier_obligations"],
            "waves": claims["minimum_parallel_completion_waves"], "ready": claims["root_ready"]}


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
        raise SystemExit("usage: check_prime_power_obligation_blocker_schedule.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
