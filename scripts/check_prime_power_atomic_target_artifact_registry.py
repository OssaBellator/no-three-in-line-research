#!/usr/bin/env python3
"""Validate typed artifacts for all completed atomic frontier targets.

For a completed target, the atomic completion locator is the canonical registry URI and the
completion digest is the reconstructed target-artifact bundle digest. The artifact inside the
bundle carries a separate external proof locator/digest, exact immediate target-artifact support,
namespace-qualified obligation/premise/handoff support, and role-qualified legacy certificate
bindings where those remain canonical.

T17 and T18 deliberately have no legacy global-quotient-refinement certificate binding: their exact
frontier checkers seal the T13--T18 banks directly. This is documentary integrity only and permanently
reports ``all_n_proved_by_checker = 0``.
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
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AtomicTargetArtifactError(message)


def exact_artifact(record: dict[str, Any], path: str) -> dict[str, Any]:
    target_id = record.get("target_id")
    values = {key: record.get(key) for key in (
        "artifact_id", "artifact_kind", "proof_locator", "proof_digest", "statement", "evidence"
    )}
    target_support = record.get("support_target_artifact_ids")
    external_support = record.get("support_external_artifact_refs")
    certificate_support = record.get("support_certificate_refs")
    require(target_id in atomic.TARGETS, f"{path}.target_id: unknown")
    for key, value in values.items():
        require(isinstance(value, str) and value, f"{path}.{key}: required")
    require(values["artifact_kind"] == atomic.TARGETS[target_id]["required_artifact_kind"],
            f"{path}.artifact_kind: wrong target artifact kind")
    for key, items in (
        ("support_target_artifact_ids", target_support),
        ("support_external_artifact_refs", external_support),
        ("support_certificate_refs", certificate_support),
    ):
        require(isinstance(items, list), f"{path}.{key}: expected list")
        require(all(isinstance(item, str) and item for item in items), f"{path}.{key}: bad value")
        require(items == sorted(items), f"{path}.{key}: sorted order required")
        require(len(items) == len(set(items)), f"{path}.{key}: duplicates")
    require(values["artifact_id"] not in target_support, f"{path}: artifact cannot support itself")
    output = {
        "target_id": target_id,
        **values,
        "support_target_artifact_ids": list(target_support),
        "support_external_artifact_refs": list(external_support),
        "support_certificate_refs": list(certificate_support),
    }
    output["atomic_target_artifact_sha256"] = catalogue.canonical_digest(output)
    return output


def certificate_ref(role: str, sha256: str) -> str:
    require(isinstance(role, str) and role, "certificate role: required")
    require(isinstance(sha256, str) and sha256, f"certificate role {role}: SHA-256 required")
    return f"{role}:{sha256}"


def special_certificate_support(target_id: str, surfaces: dict[str, Any]) -> list[str]:
    refs: list[str] = []
    add = lambda role, sha: refs.append(certificate_ref(role, sha))
    # T17/T18 are sealed by their exact frontier proof banks, not the older parallel refinement.
    if target_id == "T19_GLOBAL_FAMILY":
        add("global-family-skeleton", surfaces["skeleton"]["certificate_sha256"])
    if target_id == "T20_EXCEPTIONAL_ZERO_ROWS":
        add("exceptional-chamber-disposition-registry", surfaces["chamber"]["certificate_sha256"])
        add("zero-selector-dispositions", surfaces["chamber_claims"]["zero_dispositions_sha256"])
    if target_id == "T21_HARD_CORE_ROWS":
        add("exceptional-chamber-disposition-registry", surfaces["chamber"]["certificate_sha256"])
        add("hard-core-dispositions", surfaces["chamber_claims"]["hard_core_dispositions_sha256"])
    if target_id == "T32_OBLIGATION_ARTIFACTS":
        add("obligation-artifact-registry", surfaces["obligation"]["certificate_sha256"])
    if target_id == "T33_OBLIGATION_SUPPORT_DAG":
        add("obligation-artifact-support-dag", surfaces["support"]["certificate_sha256"])
    if target_id == "T34_PREMISE_ARTIFACTS":
        add("premise-artifact-registry", surfaces["premise"]["certificate_sha256"])
    if target_id in {
        "T35_BASE_HANDOFF", "T36_RECURRENCE_HANDOFF", "T37_INVARIANT_HANDOFF",
        "T38_TERMINATION_HANDOFF", "T39_EXCEPTIONAL_HANDOFF", "T40_TRANSLATION_HANDOFF",
    }:
        add("handoff-assertion-artifact-registry", surfaces["handoff_artifacts"]["certificate_sha256"])
    if target_id == "T41_FINAL_HANDOFF_REVIEW":
        add("final-induction-handoff", surfaces["handoff"]["certificate_sha256"])
    if target_id == "T42_FINAL_DOSSIER_AUDIT":
        add("final-dossier-integrity", surfaces["dossier"]["certificate_sha256"])
    return sorted(refs)


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    current = certificate.get("current_frontier_execution_certificate")
    raw_artifacts = certificate.get("atomic_target_artifacts")
    require(isinstance(current, dict), "current_frontier_execution_certificate: expected object")
    require(isinstance(raw_artifacts, list), "atomic_target_artifacts: expected list")
    current_frontier.validate_certificate(current)
    current_exact = current_frontier.exact_certificate(current)

    atomic_certificate = current["atomic_frontier_execution_certificate"]
    atomic.validate_certificate(atomic_certificate)
    atomic_exact = atomic.exact_certificate(atomic_certificate)
    dossier = atomic_certificate["final_dossier_integrity_certificate"]
    handoff = dossier["final_induction_handoff_certificate"]
    premise = handoff["premise_artifact_registry_certificate"]
    contract = premise["final_implication_premise_contract_certificate"]
    obligation = contract["obligation_artifact_registry_certificate"]
    closure_certificate = obligation["all_n_implication_closure_certificate"]
    support = handoff["artifact_support_dag_certificate"]
    refinement = handoff["global_quotient_semantic_refinement_certificate"]
    skeleton = closure_certificate["global_family_skeleton_certificate"]
    handoff_registry = current["handoff_assertion_artifact_registry_certificate"]
    chamber = current["exceptional_chamber_disposition_certificate"]

    obligation_artifacts.validate_certificate(obligation)
    premise_artifacts.validate_certificate(premise)
    handoff_artifacts.validate_certificate(handoff_registry)
    chambers.validate_certificate(chamber)
    obligation_exact = obligation_artifacts.exact_certificate(obligation)
    premise_exact = premise_artifacts.exact_certificate(premise)
    handoff_exact = handoff_artifacts.exact_certificate(handoff_registry)
    chamber_exact = chambers.exact_certificate(chamber)
    surfaces = {
        "dossier": dossier, "handoff": handoff, "premise": premise, "obligation": obligation,
        "support": support, "refinement": refinement, "skeleton": skeleton,
        "handoff_artifacts": handoff_registry, "chamber": chamber,
        "chamber_claims": chamber_exact["claims"],
    }

    target_order = list(atomic.TARGETS)
    order = {target_id: index for index, target_id in enumerate(target_order)}
    artifacts = [exact_artifact(record, f"atomic_target_artifacts[{index}]")
                 for index, record in enumerate(raw_artifacts)]
    require(raw_artifacts == artifacts, "atomic_target_artifacts: canonical records required")
    require(artifacts == sorted(artifacts, key=lambda item: (order[item["target_id"]], item["artifact_id"])),
            "atomic_target_artifacts: canonical target/artifact order required")
    artifact_ids = [record["artifact_id"] for record in artifacts]
    target_ids = [record["target_id"] for record in artifacts]
    require(len(artifact_ids) == len(set(artifact_ids)), "atomic_target_artifacts: duplicate artifact_id")
    require(len(target_ids) == len(set(target_ids)), "atomic_target_artifacts: at most one per target")
    artifact_by_target = {record["target_id"]: record for record in artifacts}

    completions = {record["target_id"]: record for record in atomic_exact["target_completion_records"]}
    results = {record["target_id"]: record for record in atomic_exact["target_result_records"]}
    obligation_ids = {obligation_id: [] for obligation_id in obligation_artifacts.REQUIRED_ARTIFACT_KINDS}
    for record in obligation_exact["proof_artifacts"]:
        obligation_ids[record["obligation_id"]].append(record["artifact_id"])
    premise_ids = {record["premise_id"]: record["artifact_id"]
                   for record in premise_exact["premise_artifacts"]}
    handoff_ids = {record["assertion_id"]: record["artifact_id"]
                   for record in handoff_exact["handoff_assertion_artifacts"]}

    bundles = []
    kind_counts: Counter[str] = Counter()
    for target_id in target_order:
        definition = atomic.TARGETS[target_id]
        completion = completions[target_id]
        effective = bool(results[target_id]["effective_target_complete"])
        artifact = artifact_by_target.get(target_id)
        dependency_ids = list(definition["proof_dependency_target_ids"])
        target_support = sorted(artifact_by_target[dependency]["artifact_id"]
                                for dependency in dependency_ids if dependency in artifact_by_target)
        external_support: list[str] = []
        for obligation_id in definition["obligation_ids"]:
            external_support.extend(f"obligation:{artifact_id}"
                                    for artifact_id in obligation_ids[obligation_id])
        for premise_id in definition["premise_ids"]:
            if premise_id in premise_ids:
                external_support.append(f"premise:{premise_ids[premise_id]}")
        for assertion_id in definition["handoff_assertion_ids"]:
            if assertion_id in handoff_ids:
                external_support.append(f"handoff:{handoff_ids[assertion_id]}")
        external_support.sort()
        certificate_support = special_certificate_support(target_id, surfaces)

        if effective:
            require(artifact is not None, f"target {target_id}: completed target missing typed artifact")
            require(len(target_support) == len(dependency_ids),
                    f"target {target_id}: dependency target artifact missing")
            require(artifact["support_target_artifact_ids"] == target_support,
                    f"target {target_id}: exact immediate target-artifact support required")
            require(artifact["support_external_artifact_refs"] == external_support,
                    f"target {target_id}: exact namespace-qualified external support required")
            require(artifact["support_certificate_refs"] == certificate_support,
                    f"target {target_id}: exact role-qualified certificate support required")
            artifact_list = [artifact]
            kind_counts[artifact["artifact_kind"]] += 1
        else:
            require(artifact is None, f"target {target_id}: open target cannot contain typed artifact")
            artifact_list = []

        bundle = {
            "target_id": target_id,
            "frontier_id": definition["frontier_id"],
            "effective_target_complete": int(effective),
            "required_artifact_kind": definition["required_artifact_kind"],
            "proof_dependency_target_ids": dependency_ids,
            "required_support_target_artifact_ids": target_support,
            "linked_obligation_ids": list(definition["obligation_ids"]),
            "linked_premise_ids": list(definition["premise_ids"]),
            "linked_handoff_assertion_ids": list(definition["handoff_assertion_ids"]),
            "required_support_external_artifact_refs": external_support,
            "required_support_certificate_refs": certificate_support,
            "artifact_ids": [record["artifact_id"] for record in artifact_list],
            "artifacts_sha256": catalogue.canonical_digest(artifact_list),
        }
        bundle["atomic_target_artifact_bundle_sha256"] = catalogue.canonical_digest(bundle)
        if effective:
            require(completion["artifact_locator"] == f"atomic-target-artifact-registry://{target_id}",
                    f"target {target_id}: completion locator does not bind target registry")
            require(completion["artifact_digest"] == bundle["atomic_target_artifact_bundle_sha256"],
                    f"target {target_id}: completion digest does not bind target bundle")
        bundles.append(bundle)

    completed = atomic_exact["claims"]["completed_targets"]
    complete_bank = int(len(artifacts) == len(atomic.TARGETS))
    final_ready = int(current_exact["claims"]["current_frontier_execution_ready"] and complete_bank)
    require(len(artifacts) == completed,
            "typed target artifact count must equal effective completed target count")
    claims = {
        "frontier_groups": atomic_exact["claims"]["frontier_groups"],
        "atomic_targets": len(atomic.TARGETS),
        "completed_targets": completed,
        "atomic_target_artifacts": len(artifacts),
        "proved_target_artifact_bundles": len(artifacts),
        "open_target_artifact_bundles": len(atomic.TARGETS) - len(artifacts),
        "exact_typed_target_artifact_coverage": 1,
        "exact_immediate_target_artifact_support": 1,
        "namespace_qualified_external_artifact_support": 1,
        "role_qualified_certificate_binding": 1,
        "exact_completion_to_bundle_binding": 1,
        "noncircular_ancestor_certificate_binding": 1,
        "legacy_t17_t18_refinement_binding_removed": 1,
        "complete_atomic_target_artifact_bank": complete_bank,
        "post_frontier_target_artifact_gate_ready": final_ready,
        "all_n_proved_by_checker": 0,
        "artifact_kind_distribution": [[kind, kind_counts[kind]] for kind in sorted(kind_counts)],
        "current_frontier_execution_sha256": current["certificate_sha256"],
        "atomic_frontier_execution_sha256": atomic_certificate["certificate_sha256"],
        "obligation_artifact_registry_sha256": obligation["certificate_sha256"],
        "premise_artifact_registry_sha256": premise["certificate_sha256"],
        "handoff_artifact_registry_sha256": handoff_registry["certificate_sha256"],
        "exceptional_chamber_disposition_sha256": chamber["certificate_sha256"],
        "atomic_target_artifacts_sha256": catalogue.canonical_digest(artifacts),
        "atomic_target_artifact_bundles_sha256": catalogue.canonical_digest(bundles),
    }
    return {"atomic_target_artifacts": artifacts,
            "atomic_target_artifact_bundle_records": bundles,
            "claims": claims}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 2, "version: expected 2")
    exact = exact_certificate(certificate)
    for key in ("atomic_target_artifacts", "atomic_target_artifact_bundle_records", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {"targets": claims["atomic_targets"], "artifacts": claims["atomic_target_artifacts"],
            "complete": claims["complete_atomic_target_artifact_bank"],
            "ready": claims["post_frontier_target_artifact_gate_ready"],
            "proved": claims["all_n_proved_by_checker"]}


def build_certificate(current: dict[str, Any], artifacts: list[dict[str, Any]]) -> dict[str, Any]:
    canonical = [exact_artifact(record, "atomic_target_artifact") for record in artifacts]
    order = {target_id: index for index, target_id in enumerate(atomic.TARGETS)}
    canonical.sort(key=lambda item: (order[item["target_id"]], item["artifact_id"]))
    certificate: dict[str, Any] = {"version": 2,
                                  "current_frontier_execution_certificate": current,
                                  "atomic_target_artifacts": canonical}
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_atomic_target_artifact_registry.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
