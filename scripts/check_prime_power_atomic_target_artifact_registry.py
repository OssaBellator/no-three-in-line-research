#!/usr/bin/env python3
"""Bind one exact typed proof artifact to every completed atomic frontier target.

The atomic execution checker currently accepts a locator/digest pair for each declared-complete
proof target. This checker removes that opaque last step. Every effectively complete target must
have exactly one target-specific artifact whose locator and digest equal the atomic completion
record, whose target-artifact support is exactly the set of immediate proof dependencies, and
whose external support is exactly the linked obligation, premise and handoff artifact set.
Selected integration targets additionally bind the authoritative chamber, semantic-refinement,
support-DAG, handoff, dossier or current-frontier certificate digests.

Passing proves typed documentary linkage only. It does not verify mathematical truth, logical
sufficiency or the no-three-in-line conjecture, and permanently reports
``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_atomic_frontier_execution as atomic
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_current_frontier_execution as current_frontier
import check_prime_power_exceptional_chamber_disposition_registry as chambers
import check_prime_power_handoff_assertion_artifact_registry as handoff_artifacts
import check_prime_power_obligation_artifact_registry as obligation_artifacts
import check_prime_power_premise_artifact_registry as premise_artifacts


class AtomicTargetArtifactError(ValueError):
    """Raised when the atomic target artifact bank is incomplete or inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AtomicTargetArtifactError(message)


def exact_artifact(record: dict[str, Any], path: str) -> dict[str, Any]:
    target_id = record.get("target_id")
    artifact_id = record.get("artifact_id")
    artifact_kind = record.get("artifact_kind")
    locator = record.get("locator")
    digest = record.get("digest")
    statement = record.get("statement")
    target_support = record.get("support_target_artifact_ids")
    external_support = record.get("support_external_artifact_ids")
    certificate_support = record.get("support_certificate_sha256s")
    evidence = record.get("evidence")

    require(target_id in atomic.TARGETS, f"{path}.target_id: unknown")
    for name, value in (
        ("artifact_id", artifact_id),
        ("artifact_kind", artifact_kind),
        ("locator", locator),
        ("digest", digest),
        ("statement", statement),
        ("evidence", evidence),
    ):
        require(isinstance(value, str) and value, f"{path}.{name}: required")
    require(
        artifact_kind == atomic.TARGETS[target_id]["required_artifact_kind"],
        f"{path}.artifact_kind: wrong target artifact kind",
    )
    for name, values in (
        ("support_target_artifact_ids", target_support),
        ("support_external_artifact_ids", external_support),
        ("support_certificate_sha256s", certificate_support),
    ):
        require(isinstance(values, list), f"{path}.{name}: expected list")
        require(all(isinstance(value, str) and value for value in values),
                f"{path}.{name}: bad value")
        require(values == sorted(values), f"{path}.{name}: sorted order required")
        require(len(values) == len(set(values)), f"{path}.{name}: duplicates")
    require(artifact_id not in target_support, f"{path}: artifact cannot support itself")

    output = {
        "target_id": target_id,
        "artifact_id": artifact_id,
        "artifact_kind": artifact_kind,
        "locator": locator,
        "digest": digest,
        "statement": statement,
        "support_target_artifact_ids": list(target_support),
        "support_external_artifact_ids": list(external_support),
        "support_certificate_sha256s": list(certificate_support),
        "evidence": evidence,
    }
    output["atomic_target_artifact_sha256"] = catalogue.canonical_digest(output)
    return output


def special_certificate_support(
    target_id: str,
    *,
    current_certificate: dict[str, Any],
    dossier_certificate: dict[str, Any],
    final_handoff_certificate: dict[str, Any],
    obligation_certificate: dict[str, Any],
    premise_certificate: dict[str, Any],
    handoff_artifact_certificate: dict[str, Any],
    chamber_certificate: dict[str, Any],
    chamber_claims: dict[str, Any],
    support_certificate: dict[str, Any],
    refinement_certificate: dict[str, Any],
    skeleton_certificate: dict[str, Any],
) -> list[str]:
    values: list[str] = []
    if target_id in {"T17_STATE_PREDICATES", "T18_ROW_THEOREMS"}:
        values.append(refinement_certificate["certificate_sha256"])
    if target_id == "T19_GLOBAL_FAMILY":
        values.append(skeleton_certificate["certificate_sha256"])
    if target_id == "T20_EXCEPTIONAL_ZERO_ROWS":
        values.extend([
            chamber_certificate["certificate_sha256"],
            chamber_claims["zero_dispositions_sha256"],
        ])
    if target_id == "T21_HARD_CORE_ROWS":
        values.extend([
            chamber_certificate["certificate_sha256"],
            chamber_claims["hard_core_dispositions_sha256"],
        ])
    if target_id == "T32_OBLIGATION_ARTIFACTS":
        values.append(obligation_certificate["certificate_sha256"])
    if target_id == "T33_OBLIGATION_SUPPORT_DAG":
        values.append(support_certificate["certificate_sha256"])
    if target_id == "T34_PREMISE_ARTIFACTS":
        values.append(premise_certificate["certificate_sha256"])
    if target_id in {
        "T35_BASE_HANDOFF",
        "T36_RECURRENCE_HANDOFF",
        "T37_INVARIANT_HANDOFF",
        "T38_TERMINATION_HANDOFF",
        "T39_EXCEPTIONAL_HANDOFF",
        "T40_TRANSLATION_HANDOFF",
    }:
        values.append(handoff_artifact_certificate["certificate_sha256"])
    if target_id == "T41_FINAL_HANDOFF_REVIEW":
        values.append(final_handoff_certificate["certificate_sha256"])
    if target_id == "T42_FINAL_DOSSIER_AUDIT":
        values.append(dossier_certificate["certificate_sha256"])
    if target_id == "T43_ROOT_IMPLICATION":
        values.append(current_certificate["certificate_sha256"])
    return sorted(values)


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    current_certificate = certificate.get("current_frontier_execution_certificate")
    raw_artifacts = certificate.get("atomic_target_artifacts")
    require(isinstance(current_certificate, dict),
            "current_frontier_execution_certificate: expected object")
    require(isinstance(raw_artifacts, list), "atomic_target_artifacts: expected list")

    current_frontier.validate_certificate(current_certificate)
    current_exact = current_frontier.exact_certificate(current_certificate)
    atomic_certificate = current_certificate["atomic_frontier_execution_certificate"]
    atomic.validate_certificate(atomic_certificate)
    atomic_exact = atomic.exact_certificate(atomic_certificate)

    dossier_certificate = atomic_certificate["final_dossier_integrity_certificate"]
    final_handoff_certificate = dossier_certificate["final_induction_handoff_certificate"]
    premise_certificate = final_handoff_certificate["premise_artifact_registry_certificate"]
    contract_certificate = premise_certificate["final_implication_premise_contract_certificate"]
    obligation_certificate = contract_certificate["obligation_artifact_registry_certificate"]
    closure_certificate = obligation_certificate["all_n_implication_closure_certificate"]
    support_certificate = final_handoff_certificate["artifact_support_dag_certificate"]
    refinement_certificate = final_handoff_certificate[
        "global_quotient_semantic_refinement_certificate"
    ]
    skeleton_certificate = closure_certificate["global_family_skeleton_certificate"]
    handoff_artifact_certificate = current_certificate[
        "handoff_assertion_artifact_registry_certificate"
    ]
    chamber_certificate = current_certificate["exceptional_chamber_disposition_certificate"]

    obligation_artifacts.validate_certificate(obligation_certificate)
    premise_artifacts.validate_certificate(premise_certificate)
    handoff_artifacts.validate_certificate(handoff_artifact_certificate)
    chambers.validate_certificate(chamber_certificate)
    obligation_exact = obligation_artifacts.exact_certificate(obligation_certificate)
    premise_exact = premise_artifacts.exact_certificate(premise_certificate)
    handoff_exact = handoff_artifacts.exact_certificate(handoff_artifact_certificate)
    chamber_exact = chambers.exact_certificate(chamber_certificate)

    target_order = list(atomic.TARGETS)
    order = {target_id: index for index, target_id in enumerate(target_order)}
    artifacts = [
        exact_artifact(record, f"atomic_target_artifacts[{index}]")
        for index, record in enumerate(raw_artifacts)
    ]
    require(raw_artifacts == artifacts,
            "atomic_target_artifacts: canonical records or digests required")
    require(
        artifacts == sorted(artifacts, key=lambda item: (order[item["target_id"]], item["artifact_id"])),
        "atomic_target_artifacts: canonical target/artifact order required",
    )
    artifact_ids = [record["artifact_id"] for record in artifacts]
    target_ids = [record["target_id"] for record in artifacts]
    require(len(artifact_ids) == len(set(artifact_ids)),
            "atomic_target_artifacts: duplicate artifact_id")
    require(len(target_ids) == len(set(target_ids)),
            "atomic_target_artifacts: at most one artifact per target")
    artifact_by_target = {record["target_id"]: record for record in artifacts}

    target_completion_by_id = {
        record["target_id"]: record for record in atomic_exact["target_completion_records"]
    }
    target_result_by_id = {
        record["target_id"]: record for record in atomic_exact["target_result_records"]
    }
    obligation_artifact_ids: dict[str, list[str]] = {
        obligation_id: [] for obligation_id in obligation_artifacts.REQUIRED_ARTIFACT_KINDS
    }
    for record in obligation_exact["proof_artifacts"]:
        obligation_artifact_ids[record["obligation_id"]].append(record["artifact_id"])
    premise_artifact_by_id = {
        record["premise_id"]: record["artifact_id"]
        for record in premise_exact["premise_artifacts"]
    }
    handoff_artifact_by_id = {
        record["assertion_id"]: record["artifact_id"]
        for record in handoff_exact["handoff_assertion_artifacts"]
    }

    bundle_records = []
    kind_counts: Counter[str] = Counter()
    for target_id in target_order:
        definition = atomic.TARGETS[target_id]
        completion = target_completion_by_id[target_id]
        result = target_result_by_id[target_id]
        artifact = artifact_by_target.get(target_id)
        effective = bool(result["effective_target_complete"])

        dependency_ids = list(definition["proof_dependency_target_ids"])
        expected_target_support = sorted(
            artifact_by_target[dependency_id]["artifact_id"]
            for dependency_id in dependency_ids
            if dependency_id in artifact_by_target
        )
        expected_external_support: list[str] = []
        for obligation_id in definition["obligation_ids"]:
            expected_external_support.extend(obligation_artifact_ids[obligation_id])
        for premise_id in definition["premise_ids"]:
            if premise_id in premise_artifact_by_id:
                expected_external_support.append(premise_artifact_by_id[premise_id])
        for assertion_id in definition["handoff_assertion_ids"]:
            if assertion_id in handoff_artifact_by_id:
                expected_external_support.append(handoff_artifact_by_id[assertion_id])
        expected_external_support = sorted(expected_external_support)
        expected_certificate_support = special_certificate_support(
            target_id,
            current_certificate=current_certificate,
            dossier_certificate=dossier_certificate,
            final_handoff_certificate=final_handoff_certificate,
            obligation_certificate=obligation_certificate,
            premise_certificate=premise_certificate,
            handoff_artifact_certificate=handoff_artifact_certificate,
            chamber_certificate=chamber_certificate,
            chamber_claims=chamber_exact["claims"],
            support_certificate=support_certificate,
            refinement_certificate=refinement_certificate,
            skeleton_certificate=skeleton_certificate,
        )

        if effective:
            require(artifact is not None,
                    f"target {target_id}: completed target missing typed artifact")
            require(
                len(expected_target_support) == len(dependency_ids),
                f"target {target_id}: dependency target artifact missing",
            )
            require(
                artifact["support_target_artifact_ids"] == expected_target_support,
                f"target {target_id}: exact immediate target-artifact support required",
            )
            require(
                artifact["support_external_artifact_ids"] == expected_external_support,
                f"target {target_id}: exact external artifact support required",
            )
            require(
                artifact["support_certificate_sha256s"] == expected_certificate_support,
                f"target {target_id}: exact external certificate binding required",
            )
            require(artifact["locator"] == completion["artifact_locator"],
                    f"target {target_id}: locator does not bind completion record")
            require(artifact["digest"] == completion["artifact_digest"],
                    f"target {target_id}: digest does not bind completion record")
            artifact_list = [artifact]
            kind_counts[artifact["artifact_kind"]] += 1
        else:
            require(artifact is None,
                    f"target {target_id}: open target cannot contain typed artifact")
            artifact_list = []

        bundle = {
            "target_id": target_id,
            "frontier_id": definition["frontier_id"],
            "effective_target_complete": int(effective),
            "required_artifact_kind": definition["required_artifact_kind"],
            "proof_dependency_target_ids": dependency_ids,
            "required_support_target_artifact_ids": expected_target_support,
            "linked_obligation_ids": list(definition["obligation_ids"]),
            "linked_premise_ids": list(definition["premise_ids"]),
            "linked_handoff_assertion_ids": list(definition["handoff_assertion_ids"]),
            "required_support_external_artifact_ids": expected_external_support,
            "required_support_certificate_sha256s": expected_certificate_support,
            "artifact_ids": [record["artifact_id"] for record in artifact_list],
            "artifacts_sha256": catalogue.canonical_digest(artifact_list),
        }
        bundle["atomic_target_artifact_bundle_sha256"] = catalogue.canonical_digest(bundle)
        bundle_records.append(bundle)

    completed_targets = atomic_exact["claims"]["completed_targets"]
    target_artifact_bank_complete = int(len(artifacts) == len(atomic.TARGETS))
    current_ready = int(current_exact["claims"]["current_frontier_execution_ready"])
    final_ready = int(current_ready and target_artifact_bank_complete)
    claims = {
        "frontier_groups": atomic_exact["claims"]["frontier_groups"],
        "atomic_targets": len(atomic.TARGETS),
        "completed_targets": completed_targets,
        "atomic_target_artifacts": len(artifacts),
        "proved_target_artifact_bundles": len(artifacts),
        "open_target_artifact_bundles": len(atomic.TARGETS) - len(artifacts),
        "exact_typed_target_artifact_coverage": 1,
        "exact_immediate_target_artifact_support": 1,
        "exact_external_registry_binding": 1,
        "complete_atomic_target_artifact_bank": target_artifact_bank_complete,
        "post_frontier_target_artifact_gate_ready": final_ready,
        "all_n_proved_by_checker": 0,
        "artifact_kind_distribution": [
            [kind, kind_counts[kind]] for kind in sorted(kind_counts)
        ],
        "current_frontier_execution_sha256": current_certificate["certificate_sha256"],
        "atomic_frontier_execution_sha256": atomic_certificate["certificate_sha256"],
        "obligation_artifact_registry_sha256": obligation_certificate["certificate_sha256"],
        "premise_artifact_registry_sha256": premise_certificate["certificate_sha256"],
        "handoff_artifact_registry_sha256": handoff_artifact_certificate[
            "certificate_sha256"
        ],
        "exceptional_chamber_disposition_sha256": chamber_certificate[
            "certificate_sha256"
        ],
        "atomic_target_artifacts_sha256": catalogue.canonical_digest(artifacts),
        "atomic_target_artifact_bundles_sha256": catalogue.canonical_digest(bundle_records),
    }
    require(
        len(artifacts) == completed_targets,
        "typed target artifact count must equal effective completed target count",
    )
    return {
        "atomic_target_artifacts": artifacts,
        "atomic_target_artifact_bundle_records": bundle_records,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in (
        "atomic_target_artifacts",
        "atomic_target_artifact_bundle_records",
        "claims",
    ):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(
        certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
        "certificate_sha256: incorrect",
    )
    claims = exact["claims"]
    return {
        "targets": claims["atomic_targets"],
        "artifacts": claims["atomic_target_artifacts"],
        "complete": claims["complete_atomic_target_artifact_bank"],
        "ready": claims["post_frontier_target_artifact_gate_ready"],
        "proved": claims["all_n_proved_by_checker"],
    }


def build_certificate(
    current_certificate: dict[str, Any],
    artifacts: list[dict[str, Any]],
) -> dict[str, Any]:
    canonical = [exact_artifact(record, "atomic_target_artifact") for record in artifacts]
    order = {target_id: index for index, target_id in enumerate(atomic.TARGETS)}
    canonical.sort(key=lambda item: (order[item["target_id"]], item["artifact_id"]))
    certificate: dict[str, Any] = {
        "version": 1,
        "current_frontier_execution_certificate": current_certificate,
        "atomic_target_artifacts": canonical,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: check_prime_power_atomic_target_artifact_registry.py certificate.json"
        )
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
