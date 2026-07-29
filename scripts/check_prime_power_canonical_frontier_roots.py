#!/usr/bin/env python3
"""Install and audit the canonical T19--T21 roots for the complete T01--T43 DAG.

The original atomic target table predates the exact T19 global-family and T20/T21 exceptional-chamber
frontiers.  Those later checkers therefore carried scoped compatibility contexts which temporarily changed
the shared target table and removed obsolete certificate support.  This module installs the corrected roots
once, verifies that the compatibility contexts are now behaviourally idempotent, and publishes the exact
downstream impact of the correction.

This is documentary dependency integrity only.  It does not prove any target and permanently reports
``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import json
import sys
from collections import deque
from pathlib import Path
from typing import Any

import check_prime_power_atomic_frontier_execution as atomic
import check_prime_power_atomic_target_artifact_registry as target_artifacts
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_exceptional_chamber_frontier as t21
import check_prime_power_global_family_exhaustiveness_frontier as t19


class CanonicalFrontierRootError(ValueError):
    """Raised when the shared atomic target roots drift from the canonical exact frontiers."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CanonicalFrontierRootError(message)


CANONICAL_ROOTS: dict[str, dict[str, tuple[str, ...]]] = {
    "T19_GLOBAL_FAMILY": {
        "proof_dependency_target_ids": (
            "T02_RULE_EXHAUSTIVENESS",
            "T18_ROW_THEOREMS",
        ),
        "research_dependency_target_ids": ("T18_ROW_THEOREMS",),
    },
    "T20_EXCEPTIONAL_ZERO_ROWS": {
        "proof_dependency_target_ids": (
            "T05_GEOMETRY_SELECTORS",
            "T18_ROW_THEOREMS",
            "T19_GLOBAL_FAMILY",
        ),
        "research_dependency_target_ids": ("T19_GLOBAL_FAMILY",),
    },
    "T21_HARD_CORE_ROWS": {
        "proof_dependency_target_ids": (
            "T05_GEOMETRY_SELECTORS",
            "T18_ROW_THEOREMS",
            "T19_GLOBAL_FAMILY",
        ),
        "research_dependency_target_ids": ("T19_GLOBAL_FAMILY",),
    },
}

LEGACY_FREE_SPECIAL_TARGET_IDS = frozenset(CANONICAL_ROOTS)
_ORIGINAL_SPECIAL_ATTRIBUTE = "_canonical_frontier_original_special_certificate_support"


def install_canonical_roots() -> None:
    """Install corrected roots and a stable legacy-free special-support dispatcher exactly once."""
    for target_id, fields in CANONICAL_ROOTS.items():
        definition = atomic.TARGETS[target_id]
        for field, expected in fields.items():
            definition[field] = tuple(expected)

    if not hasattr(target_artifacts, _ORIGINAL_SPECIAL_ATTRIBUTE):
        setattr(
            target_artifacts,
            _ORIGINAL_SPECIAL_ATTRIBUTE,
            target_artifacts.special_certificate_support,
        )
    original = getattr(target_artifacts, _ORIGINAL_SPECIAL_ATTRIBUTE)

    def canonical_special_certificate_support(
        target_id: str,
        surfaces: dict[str, Any],
    ) -> list[str]:
        if target_id in LEGACY_FREE_SPECIAL_TARGET_IDS:
            return []
        return original(target_id, surfaces)

    canonical_special_certificate_support.__name__ = "canonical_special_certificate_support"
    target_artifacts.special_certificate_support = canonical_special_certificate_support


install_canonical_roots()


def definition_records_by_id() -> dict[str, dict[str, Any]]:
    return {
        record["target_id"]: record
        for record in atomic.target_definition_records()
    }


def descendants(source: str, key: str) -> list[str]:
    require(source in atomic.TARGETS, f"unknown source target {source}")
    queue: deque[str] = deque([source])
    seen = {source}
    while queue:
        current = queue.popleft()
        for target_id, definition in atomic.TARGETS.items():
            if current in definition[key] and target_id not in seen:
                seen.add(target_id)
                queue.append(target_id)
    return [target_id for target_id in atomic.TARGETS if target_id in seen and target_id != source]


def root_record(target_id: str) -> dict[str, Any]:
    definition = atomic.TARGETS[target_id]
    record = {
        "target_id": target_id,
        "proof_dependency_target_ids": list(definition["proof_dependency_target_ids"]),
        "research_dependency_target_ids": list(definition["research_dependency_target_ids"]),
        "legacy_special_certificate_support_removed": int(
            target_artifacts.special_certificate_support(target_id, {}) == []
        ),
    }
    record["canonical_frontier_root_sha256"] = catalogue.canonical_digest(record)
    return record


def exact_audit() -> dict[str, Any]:
    install_canonical_roots()
    base_summary = atomic.validate_definitions()
    require(base_summary["targets"] == 43, "canonical atomic DAG must retain exactly 43 targets")

    for target_id, fields in CANONICAL_ROOTS.items():
        definition = atomic.TARGETS[target_id]
        for field, expected in fields.items():
            require(
                definition[field] == expected,
                f"target {target_id}: canonical {field} mismatch",
            )
        require(
            target_artifacts.special_certificate_support(target_id, {}) == [],
            f"target {target_id}: obsolete special certificate support remains",
        )

    before_records = definition_records_by_id()
    before_roots = {target_id: before_records[target_id] for target_id in CANONICAL_ROOTS}
    before_digest = catalogue.canonical_digest(before_roots)
    with t19.corrected_roots():
        with t21.corrected_roots():
            during_records = definition_records_by_id()
            during_roots = {target_id: during_records[target_id] for target_id in CANONICAL_ROOTS}
            require(
                during_roots == before_roots,
                "legacy corrected-root contexts changed canonical target definitions",
            )
            for target_id in CANONICAL_ROOTS:
                require(
                    target_artifacts.special_certificate_support(target_id, {}) == [],
                    f"target {target_id}: context restored obsolete support",
                )
    after_records = definition_records_by_id()
    after_roots = {target_id: after_records[target_id] for target_id in CANONICAL_ROOTS}
    require(after_roots == before_roots, "corrected-root contexts did not restore canonical definitions")

    t32_dependencies = atomic.TARGETS["T32_OBLIGATION_ARTIFACTS"][
        "proof_dependency_target_ids"
    ]
    expected_t32_dependencies = tuple(
        target_id
        for target_id, definition in atomic.TARGETS.items()
        if target_id < "T22" and definition["obligation_ids"]
    )
    require(
        t32_dependencies == expected_t32_dependencies,
        "T32 obligation target census changed under canonical roots",
    )

    proof_descendants = {
        target_id: descendants(target_id, "proof_dependency_target_ids")
        for target_id in CANONICAL_ROOTS
    }
    research_descendants = {
        target_id: descendants(target_id, "research_dependency_target_ids")
        for target_id in CANONICAL_ROOTS
    }
    for target_id in ("T19_GLOBAL_FAMILY", "T20_EXCEPTIONAL_ZERO_ROWS", "T21_HARD_CORE_ROWS"):
        require(
            "T43_ROOT_IMPLICATION" in proof_descendants[target_id],
            f"target {target_id}: correction must propagate to the root implication",
        )
    require(
        {"T20_EXCEPTIONAL_ZERO_ROWS", "T21_HARD_CORE_ROWS"}
        <= set(proof_descendants["T19_GLOBAL_FAMILY"]),
        "T19 must be an exact proof prerequisite of both exceptional targets",
    )
    require(
        {"T20_EXCEPTIONAL_ZERO_ROWS", "T21_HARD_CORE_ROWS"}
        <= set(research_descendants["T19_GLOBAL_FAMILY"]),
        "T19 must be the research-start prerequisite of both exceptional targets",
    )

    roots = [root_record(target_id) for target_id in CANONICAL_ROOTS]
    context_record = {
        "canonical_root_records_sha256_before_contexts": before_digest,
        "canonical_root_records_sha256_during_contexts": catalogue.canonical_digest(during_roots),
        "canonical_root_records_sha256_after_contexts": catalogue.canonical_digest(after_roots),
        "compatibility_contexts_definition_idempotent": 1,
        "compatibility_contexts_special_support_idempotent": 1,
    }
    context_record["compatibility_context_audit_sha256"] = catalogue.canonical_digest(context_record)

    impact_records = []
    for target_id in CANONICAL_ROOTS:
        record = {
            "target_id": target_id,
            "proof_descendant_target_ids": proof_descendants[target_id],
            "research_descendant_target_ids": research_descendants[target_id],
            "proof_descendants": len(proof_descendants[target_id]),
            "research_descendants": len(research_descendants[target_id]),
            "root_implication_proof_descendant": int(
                "T43_ROOT_IMPLICATION" in proof_descendants[target_id]
            ),
        }
        record["canonical_root_impact_sha256"] = catalogue.canonical_digest(record)
        impact_records.append(record)

    claims = {
        "frontier_groups": base_summary["frontiers"],
        "atomic_targets": base_summary["targets"],
        "canonical_corrected_roots": len(CANONICAL_ROOTS),
        "legacy_special_support_targets_removed": len(LEGACY_FREE_SPECIAL_TARGET_IDS),
        "proof_topological_order_targets": base_summary["proof_order"],
        "research_topological_order_targets": base_summary["research_order"],
        "canonical_roots_installed": 1,
        "canonical_target_dag_acyclic": 1,
        "compatibility_contexts_idempotent": 1,
        "t32_obligation_target_census_stable": 1,
        "canonical_corrections_reach_t43": 1,
        "all_n_proved_by_checker": 0,
        "canonical_root_records_sha256": catalogue.canonical_digest(roots),
        "canonical_root_impact_records_sha256": catalogue.canonical_digest(impact_records),
        "compatibility_context_audit_sha256": context_record[
            "compatibility_context_audit_sha256"
        ],
        "target_definitions_sha256": catalogue.canonical_digest(
            atomic.target_definition_records()
        ),
    }
    return {
        "canonical_frontier_root_records": roots,
        "canonical_root_impact_records": impact_records,
        "compatibility_context_audit": context_record,
        "claims": claims,
    }


def validate_audit(audit: Any) -> dict[str, int]:
    require(isinstance(audit, dict), "audit: expected object")
    exact = exact_audit()
    for key, value in exact.items():
        require(audit.get(key) == value, f"{key}: incorrect")
    claims = exact["claims"]
    return {
        "roots": claims["canonical_corrected_roots"],
        "targets": claims["atomic_targets"],
        "acyclic": claims["canonical_target_dag_acyclic"],
        "idempotent": claims["compatibility_contexts_idempotent"],
        "all_n": 0,
    }


def main() -> None:
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        audit = exact_audit()
        print(validate_audit(audit))
        return
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: check_prime_power_canonical_frontier_roots.py --self-test | audit.json"
        )
    audit = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_audit(audit))


if __name__ == "__main__":
    main()
