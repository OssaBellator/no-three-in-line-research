#!/usr/bin/env python3
"""Exact documentary T22--T31 final-premise frontiers.

The ten final premises are reconstructed above the canonical T01--T21 target banks. Every
premise derives its complete dependency-target support census, carries one reviewed semantic
implication, and binds the same noncircular proof-bundle digest into both the typed premise
artifact and the atomic target artifact. No ancestor certificate SHA is used to define that
bundle, because those ancestors contain the outward proof pointers being checked.

This validates documentary identity and support only and permanently reports
``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from contextlib import contextmanager
from pathlib import Path
from typing import Any

import check_prime_power_atomic_frontier_execution as atomic
import check_prime_power_atomic_target_artifact_registry as targets
import check_prime_power_canonical_raw_host_catalogue as cat
import check_prime_power_exceptional_chamber_frontier as t21
import check_prime_power_final_implication_premise_contract as contract
import check_prime_power_global_family_exhaustiveness_frontier as t19
import check_prime_power_premise_artifact_registry as premise_artifacts


class FinalPremiseFrontierError(ValueError):
    """Raised when one of the exact T22--T31 premise banks is inconsistent."""


def req(value: bool, message: str) -> None:
    if not value:
        raise FinalPremiseFrontierError(message)


def text(value: Any, path: str) -> str:
    req(isinstance(value, str) and bool(value), f"{path}: nonempty string required")
    return value


def exact_list(value: Any, expected: list[str], path: str) -> list[str]:
    req(isinstance(value, list) and value == expected, f"{path}: exact list required")
    req(len(value) == len(set(value)), f"{path}: duplicates")
    req(all(isinstance(item, str) and item for item in value), f"{path}: bad value")
    return list(value)


PREMISE_TARGETS: dict[str, str] = {
    "BASE_CASES_COMPLETE": "T22_BASE_CASES_PREMISE",
    "RECURRENCE_EXHAUSTIVE": "T23_RECURRENCE_PREMISE",
    "STATE_INVARIANTS_PRESERVED": "T24_INVARIANT_PREMISE",
    "OPERATION_SELECTION_SOUND": "T25_SELECTION_PREMISE",
    "RESOURCE_AND_CREDIT_SOUND": "T26_RESOURCE_PREMISE",
    "BLOCK_AND_AUXILIARY_CONTRACTION": "T27_CONTRACTION_PREMISE",
    "CROSS_BLOCK_ASSEMBLY_SOUND": "T28_CROSS_BLOCK_PREMISE",
    "EXCEPTIONAL_CASES_CLOSED": "T29_EXCEPTIONAL_PREMISE",
    "TERMINATION_ARGUMENT": "T30_TERMINATION_PREMISE",
    "OBJECTIVE_TRANSLATION_TO_D_EQ_2N": "T31_OBJECTIVE_TRANSLATION_PREMISE",
}


@contextmanager
def corrected_upstream_roots():
    """Reproduce the canonical T19 and T20/T21 target definitions for nested registries."""
    with t19.corrected_roots():
        with t21.corrected_roots():
            yield


def premise_artifact_core(record: dict[str, Any]) -> dict[str, Any]:
    """Return stable premise-artifact fields, excluding the outward frontier pointer."""
    return {
        "premise_id": record["premise_id"],
        "artifact_id": record["artifact_id"],
        "artifact_kind": record["artifact_kind"],
        "statement": record["statement"],
        "support_obligation_artifact_ids": list(record["support_obligation_artifact_ids"]),
        "finite_certificate_sha256": record["finite_certificate_sha256"],
        "evidence": record["evidence"],
    }


def target_artifact_core(record: dict[str, Any]) -> dict[str, Any]:
    """Return stable target-artifact fields, excluding the outward frontier pointer."""
    return {
        "target_id": record["target_id"],
        "artifact_id": record["artifact_id"],
        "artifact_kind": record["artifact_kind"],
        "statement": record["statement"],
        "evidence": record["evidence"],
        "support_target_artifact_ids": list(record["support_target_artifact_ids"]),
        "support_external_artifact_refs": list(record["support_external_artifact_refs"]),
        "support_certificate_refs": list(record["support_certificate_refs"]),
    }


def dependency_support_records(
    premise_id: str,
    target_id: str,
    result_by_target: dict[str, dict[str, Any]],
    artifact_by_target: dict[str, dict[str, Any]],
    bundle_by_target: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    records = []
    dependencies = list(atomic.TARGETS[target_id]["proof_dependency_target_ids"])
    req(
        dependencies and all(dependency < "T22" for dependency in dependencies),
        f"premise {premise_id}: dependencies must be exact T01--T21 targets",
    )
    for dependency_id in dependencies:
        result = result_by_target[dependency_id]
        artifact = artifact_by_target.get(dependency_id)
        bundle = bundle_by_target[dependency_id]
        effective = int(result["effective_target_complete"])
        if effective:
            req(artifact is not None, f"dependency {dependency_id}: completed target artifact missing")
            req(
                bundle["artifact_ids"] == [artifact["artifact_id"]],
                f"dependency {dependency_id}: target bundle artifact mismatch",
            )
        else:
            req(
                artifact is None and bundle["artifact_ids"] == [],
                f"dependency {dependency_id}: open target contains artifact",
            )
        record = {
            "premise_id": premise_id,
            "target_id": target_id,
            "dependency_target_id": dependency_id,
            "dependency_effective_target_complete": effective,
            "dependency_target_result_sha256": result["target_result_sha256"],
            "dependency_target_completion_sha256": result["target_completion_sha256"],
            "dependency_target_artifact_id": None if artifact is None else artifact["artifact_id"],
            "dependency_target_artifact_sha256": (
                None if artifact is None else artifact["atomic_target_artifact_sha256"]
            ),
            "dependency_target_artifact_bundle_sha256": bundle[
                "atomic_target_artifact_bundle_sha256"
            ],
            "dependency_proof_locator": None if artifact is None else artifact["proof_locator"],
            "dependency_proof_digest": None if artifact is None else artifact["proof_digest"],
        }
        record["final_premise_dependency_support_sha256"] = cat.canonical_digest(record)
        records.append(record)
    return records


def exact_record(
    raw: dict[str, Any],
    premise_id: str,
    target_id: str,
    support_records: list[dict[str, Any]],
    contract_premise: dict[str, Any],
    path: str,
) -> dict[str, Any]:
    dependency_ids = list(atomic.TARGETS[target_id]["proof_dependency_target_ids"])
    req(
        raw.get("premise_id") == premise_id and raw.get("target_id") == target_id,
        f"{path}: premise/target identity mismatch",
    )
    status = raw.get("status")
    proof_mode = raw.get("proof_mode")
    req(status in {"open", "proved"}, f"{path}.status: open/proved required")
    req(status == contract_premise["status"], f"{path}.status: final contract mismatch")
    req(proof_mode == contract_premise["proof_mode"], f"{path}.proof_mode: final contract mismatch")
    exact_list(raw.get("dependency_target_ids"), dependency_ids, f"{path}.dependency_target_ids")
    support_sha = cat.canonical_digest(support_records)
    req(
        raw.get("dependency_target_support_records_sha256") == support_sha,
        f"{path}: dependency support digest mismatch",
    )
    locator = raw.get("verification_locator")
    digest = raw.get("verification_digest")
    if status == "open":
        req(locator is None and digest is None, f"{path}: open verification fields must be null")
    else:
        req(
            locator == f"final-premise-frontier://{premise_id}",
            f"{path}: canonical verification locator required",
        )
        req(isinstance(digest, str) and digest, f"{path}: proved verification digest required")
    core = {
        "premise_id": premise_id,
        "target_id": target_id,
        "status": status,
        "proof_mode": proof_mode,
        "dependency_target_ids": dependency_ids,
        "dependency_target_support_records_sha256": support_sha,
        "verification_locator": locator,
        "note": text(raw.get("note"), f"{path}.note"),
    }
    output = {
        **core,
        "verification_digest": digest,
        "final_premise_frontier_record_core_sha256": cat.canonical_digest(core),
    }
    output["final_premise_frontier_record_sha256"] = cat.canonical_digest(output)
    return output


def exact_semantic(
    raw: dict[str, Any],
    record: dict[str, Any],
    support_records: list[dict[str, Any]],
    path: str,
) -> dict[str, Any]:
    req(
        raw.get("premise_id") == record["premise_id"]
        and raw.get("target_id") == record["target_id"],
        f"{path}: premise/target identity mismatch",
    )
    req(raw.get("proof_mode") == record["proof_mode"], f"{path}: proof mode mismatch")
    req(
        raw.get("dependency_target_support_records") == support_records,
        f"{path}: exact dependency support records required",
    )
    output = {
        "premise_id": record["premise_id"],
        "target_id": record["target_id"],
        "proof_mode": record["proof_mode"],
        "dependency_target_support_records": support_records,
        "dependency_target_support_records_sha256": cat.canonical_digest(support_records),
        "mathematical_premise_statement": text(
            raw.get("mathematical_premise_statement"), f"{path}.mathematical_premise_statement"
        ),
        "dependency_implication_statement": text(
            raw.get("dependency_implication_statement"), f"{path}.dependency_implication_statement"
        ),
        "arbitrary_n_scope_statement": text(
            raw.get("arbitrary_n_scope_statement"), f"{path}.arbitrary_n_scope_statement"
        ),
        "review_boundary": text(raw.get("review_boundary"), f"{path}.review_boundary"),
        "evidence": text(raw.get("evidence"), f"{path}.evidence"),
    }
    output["final_premise_semantic_sha256"] = cat.canonical_digest(output)
    return output


def _exact(certificate: dict[str, Any]) -> dict[str, Any]:
    t21c = certificate.get("exceptional_chamber_frontier_certificate")
    raw_records = certificate.get("final_premise_frontier_records")
    raw_semantics = certificate.get("final_premise_semantic_certificates")
    raw_bundles = certificate.get("final_premise_proof_bundles")
    req(isinstance(t21c, dict), "exceptional_chamber_frontier_certificate: expected object")
    req(isinstance(raw_records, list), "final_premise_frontier_records: expected list")
    req(isinstance(raw_semantics, list), "final_premise_semantic_certificates: expected list")
    req(isinstance(raw_bundles, list), "final_premise_proof_bundles: expected list")

    t21.validate_certificate(t21c)
    t21x = t21.exact_certificate(t21c)
    t19c = t21c["global_family_exhaustiveness_frontier_certificate"]
    t18c = t19c["row_theorem_frontier_certificate"]
    t17c = t18c["state_predicate_frontier_certificate"]
    t16c = t17c["global_rank_frontier_certificate"]
    t15c = t16c["interface_exhaustiveness_frontier_certificate"]
    t14c = t15c["component_scale_frontier_certificate"]
    t13c = t14c["state_equivalence_frontier_certificate"]
    t07c = t13c["fate_transition_state_frontier_certificate"]
    t04c = t07c["block_interface_population_frontier_certificate"]
    target_registry = t04c["atomic_target_artifact_registry_certificate"]

    with corrected_upstream_roots():
        targets.validate_certificate(target_registry)
        targetx = targets.exact_certificate(target_registry)
        atomc = target_registry["current_frontier_execution_certificate"][
            "atomic_frontier_execution_certificate"
        ]
        atomic.validate_certificate(atomc)
        atomx = atomic.exact_certificate(atomc)

    dossier = atomc["final_dossier_integrity_certificate"]
    handoff = dossier["final_induction_handoff_certificate"]
    premise_registry = handoff["premise_artifact_registry_certificate"]
    premise_artifacts.validate_certificate(premise_registry)
    premisex = premise_artifacts.exact_certificate(premise_registry)
    contractc = premise_registry["final_implication_premise_contract_certificate"]
    contract.validate_certificate(contractc)
    contractx = contract.exact_certificate(contractc)

    premise_order = list(PREMISE_TARGETS)
    req(
        premise_order == list(contract.PREMISE_DEPENDENCIES),
        "premise target map must match canonical final-contract order",
    )
    req(
        [raw.get("premise_id") for raw in raw_records] == premise_order,
        "final_premise_frontier_records: exact canonical premise order required",
    )

    result_by_target = {record["target_id"]: record for record in atomx["target_result_records"]}
    target_artifact_by_target = {
        record["target_id"]: record for record in targetx["atomic_target_artifacts"]
    }
    target_bundle_by_target = {
        record["target_id"]: record for record in targetx["atomic_target_artifact_bundle_records"]
    }
    contract_premise_by_id = {
        record["premise_id"]: record for record in contractx["implication_premises"]
    }
    contract_result_by_id = {
        record["premise_id"]: record for record in contractx["premise_result_records"]
    }
    premise_artifact_by_id = {
        record["premise_id"]: record for record in premisex["premise_artifacts"]
    }

    support_by_premise: dict[str, list[dict[str, Any]]] = {}
    records = []
    for index, premise_id in enumerate(premise_order):
        target_id = PREMISE_TARGETS[premise_id]
        support_records = dependency_support_records(
            premise_id,
            target_id,
            result_by_target,
            target_artifact_by_target,
            target_bundle_by_target,
        )
        support_by_premise[premise_id] = support_records
        records.append(
            exact_record(
                raw_records[index],
                premise_id,
                target_id,
                support_records,
                contract_premise_by_id[premise_id],
                f"final_premise_frontier_records[{index}]",
            )
        )
    req(raw_records == records, "final_premise_frontier_records: noncanonical records")
    record_by_id = {record["premise_id"]: record for record in records}

    semantic_groups = {premise_id: [] for premise_id in premise_order}
    for raw in raw_semantics:
        premise_id = raw.get("premise_id")
        req(premise_id in semantic_groups, "final_premise_semantic_certificates: unknown premise")
        semantic_groups[premise_id].append(raw)

    semantics = []
    semantic_by_id: dict[str, dict[str, Any]] = {}
    for premise_id in premise_order:
        record = record_by_id[premise_id]
        group = semantic_groups[premise_id]
        if record["status"] == "open":
            req(not group, f"premise {premise_id}: open premise cannot contain semantic certificate")
            continue
        req(len(group) == 1, f"premise {premise_id}: exactly one semantic certificate required")
        req(
            all(
                item["dependency_effective_target_complete"]
                for item in support_by_premise[premise_id]
            ),
            f"premise {premise_id}: proved before every dependency target completed",
        )
        semantic = exact_semantic(
            group[0],
            record,
            support_by_premise[premise_id],
            f"final_premise_semantic[{premise_id}]",
        )
        semantics.append(semantic)
        semantic_by_id[premise_id] = semantic
    req(raw_semantics == semantics, "final_premise_semantic_certificates: noncanonical records")

    bundles = []
    ready_by_id: dict[str, int] = {}
    for premise_id in premise_order:
        target_id = PREMISE_TARGETS[premise_id]
        record = record_by_id[premise_id]
        contract_result = contract_result_by_id[premise_id]
        target_result = result_by_target[target_id]
        premise_artifact = premise_artifact_by_id.get(premise_id)
        target_artifact = target_artifact_by_target.get(target_id)
        dependency_artifact_ids = sorted(
            item["dependency_target_artifact_id"]
            for item in support_by_premise[premise_id]
            if item["dependency_target_artifact_id"] is not None
        )
        dependencies_complete = int(
            all(
                item["dependency_effective_target_complete"]
                for item in support_by_premise[premise_id]
            )
        )
        ready = int(
            record["status"] == "proved"
            and dependencies_complete
            and contract_result["effective_premise_closed"]
            and target_result["effective_target_complete"]
            and premise_artifact is not None
            and target_artifact is not None
        )
        ready_by_id[premise_id] = ready
        req(
            int(contract_result["effective_premise_closed"]) == ready,
            f"premise {premise_id}: final-contract effectiveness mismatch",
        )
        req(
            int(target_result["effective_target_complete"]) == ready,
            f"premise {premise_id}: atomic target completion mismatch",
        )

        if not ready:
            req(record["status"] == "open", f"premise {premise_id}: ineffective proved record")
            req(
                premise_artifact is None and target_artifact is None,
                f"premise {premise_id}: open premise contains typed artifact",
            )
            continue

        semantic = semantic_by_id[premise_id]
        premise_core = premise_artifact_core(premise_artifact)
        target_core = target_artifact_core(target_artifact)
        req(
            target_artifact["support_target_artifact_ids"] == dependency_artifact_ids,
            f"premise {premise_id}: atomic target does not cite exact dependency target artifacts",
        )
        req(
            f"premise:{premise_artifact['artifact_id']}"
            in target_artifact["support_external_artifact_refs"],
            f"premise {premise_id}: atomic target does not cite its typed premise artifact",
        )
        req(
            target_artifact["artifact_kind"] == atomic.TARGETS[target_id]["required_artifact_kind"],
            f"premise {premise_id}: wrong atomic target artifact kind",
        )

        bundle = {
            "premise_id": premise_id,
            "target_id": target_id,
            "final_premise_frontier_record_core_sha256": record[
                "final_premise_frontier_record_core_sha256"
            ],
            "final_premise_semantic_sha256": semantic["final_premise_semantic_sha256"],
            "dependency_target_support_records_sha256": cat.canonical_digest(
                support_by_premise[premise_id]
            ),
            "dependency_target_artifact_ids": dependency_artifact_ids,
            "premise_artifact_core_sha256": cat.canonical_digest(premise_core),
            "atomic_target_artifact_core_sha256": cat.canonical_digest(target_core),
        }
        bundle["final_premise_frontier_proof_bundle_sha256"] = cat.canonical_digest(bundle)
        digest = bundle["final_premise_frontier_proof_bundle_sha256"]
        req(
            record["verification_digest"] == digest,
            f"premise {premise_id}: frontier verification digest mismatch",
        )
        req(
            premise_artifact["locator"] == f"final-premise-frontier://{premise_id}"
            and premise_artifact["digest"] == digest,
            f"premise {premise_id}: typed premise artifact does not bind frontier bundle",
        )
        req(
            target_artifact["proof_locator"] == f"final-premise-frontier://{target_id}"
            and target_artifact["proof_digest"] == digest,
            f"premise {premise_id}: atomic target artifact does not bind frontier bundle",
        )
        bundles.append(bundle)

    counts = Counter(record["status"] for record in records)
    ready = int(all(ready_by_id.values()))
    flattened_support = [
        item for premise_id in premise_order for item in support_by_premise[premise_id]
    ]
    proof_bank = {
        "t20_zero_selector_chamber_frontier_proof_bank_sha256": t21x["claims"][
            "zero_selector_chamber_frontier_proof_bank_sha256"
        ],
        "t21_hard_core_chamber_frontier_proof_bank_sha256": t21x["claims"][
            "hard_core_chamber_frontier_proof_bank_sha256"
        ],
        "final_premise_dependency_support_records_sha256": cat.canonical_digest(flattened_support),
        "final_premise_frontier_records_sha256": cat.canonical_digest(records),
        "final_premise_semantic_certificates_sha256": cat.canonical_digest(semantics),
        "final_premise_proof_bundles_sha256": cat.canonical_digest(bundles),
    }
    proof_bank["final_premise_frontiers_proof_bank_sha256"] = cat.canonical_digest(proof_bank)

    claims = {
        "final_premises": len(premise_order),
        "open_final_premises": counts["open"],
        "proved_final_premises": counts["proved"],
        "dependency_target_support_records": len(flattened_support),
        "t22_t31_final_premise_frontiers_ready": ready,
        "exact_t01_t21_dependency_target_census": 1,
        "exact_dependency_target_artifact_support": 1,
        "exact_contract_premise_synchronization": 1,
        "exact_typed_premise_artifact_binding": 1,
        "exact_atomic_target_artifact_binding": 1,
        "noncircular_frontier_bundle_binding": 1,
        "all_n_proved_by_checker": 0,
        "open_premise_ids": [record["premise_id"] for record in records if record["status"] == "open"],
        "open_premise_target_ids": [
            record["target_id"] for record in records if record["status"] == "open"
        ],
        "exceptional_chamber_frontier_sha256": t21c["certificate_sha256"],
        "atomic_target_artifact_registry_sha256": target_registry["certificate_sha256"],
        "final_implication_premise_contract_sha256": contractc["certificate_sha256"],
        "premise_artifact_registry_sha256": premise_registry["certificate_sha256"],
        "final_premise_frontiers_proof_bank_sha256": proof_bank[
            "final_premise_frontiers_proof_bank_sha256"
        ],
    }
    return {
        "final_premise_dependency_support_records": flattened_support,
        "final_premise_frontier_records": records,
        "final_premise_semantic_certificates": semantics,
        "final_premise_proof_bundles": bundles,
        "final_premise_frontiers_proof_bank": proof_bank,
        "claims": claims,
    }


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    return _exact(certificate)


def validate_certificate(certificate: Any) -> dict[str, Any]:
    req(
        isinstance(certificate, dict) and certificate.get("version") == 1,
        "version 1 certificate required",
    )
    exact = exact_certificate(certificate)
    for key, value in exact.items():
        req(certificate.get(key) == value, f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    req(
        certificate.get("certificate_sha256") == cat.canonical_digest(payload),
        "certificate digest incorrect",
    )
    claims = exact["claims"]
    return {
        "premises": claims["final_premises"],
        "proved": claims["proved_final_premises"],
        "open": claims["open_final_premises"],
        "ready": claims["t22_t31_final_premise_frontiers_ready"],
        "all_n": 0,
    }


def build_certificate(
    t21_certificate: dict[str, Any],
    records: list[dict[str, Any]],
    semantics: list[dict[str, Any]],
) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "exceptional_chamber_frontier_certificate": t21_certificate,
        "final_premise_frontier_records": records,
        "final_premise_semantic_certificates": semantics,
        "final_premise_proof_bundles": [],
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = cat.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_final_premise_frontiers.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
