#!/usr/bin/env python3
"""Validate typed proof-artifact bundles for the fixed all-n obligation DAG.

A proved semantic obligation must carry an exact obligation-specific set of artifact kinds.
The bundle digest is bound back into the underlying closure certificate. Open obligations may
not smuggle placeholder artifacts into the registry.

This checker validates documentary coverage and linkage only. It does not verify the truth of
any cited proof artifact.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_all_n_implication_closure as closure
import check_prime_power_canonical_raw_host_catalogue as catalogue


class ObligationArtifactError(ValueError):
    """Raised when typed proof-artifact coverage is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ObligationArtifactError(message)


REQUIRED_ARTIFACT_KINDS: dict[str, tuple[str, ...]] = {
    "SOURCE_STATEMENTS_TRUE": ("source-truth-proof",),
    "RULE_EXHAUSTIVE": ("rule-exhaustiveness-proof", "rule-manifest"),
    "SLOT_AND_CANDIDATE_POPULATION": ("population-certificate",),
    "GEOMETRY_SELECTOR_CORRECT": ("geometry-proof", "selector-proof"),
    "FATE_TRANSITION_STATE_SEMANTICS": ("state-semantics-proof", "transition-proof"),
    "CANDIDATE_POLICY_CORRECT": ("candidate-policy-proof",),
    "ACTIVE_ROW_FAMILY_EXHAUSTIVE": ("active-family-exhaustiveness-proof",),
    "DESTROYED_RESOURCE_MODEL_EXHAUSTIVE": ("resource-model-proof",),
    "CREDIT_ROUTING_SEMANTIC": ("credit-routing-proof",),
    "CLOSED_STRICT_RECURRENT_BLOCKS": ("block-closure-proof", "common-weight-proof"),
    "AUXILIARY_EXPANSIONS_SEMANTIC": ("auxiliary-expansion-proof",),
    "CROSS_BLOCK_STATE_IDENTITY_SEMANTIC": ("state-equivalence-proof",),
    "COMPONENT_SCALE_SEMANTIC": ("component-scale-proof",),
    "INTERFACE_RETURN_ROWS_EXHAUSTIVE": ("interface-exhaustiveness-proof",),
    "GLOBAL_RANK_WELL_FOUNDED": ("rank-well-foundedness-proof",),
    "EXPECTED_GLOBAL_FAMILY_EXHAUSTIVE": ("global-family-exhaustiveness-proof",),
    "EXCEPTIONAL_ZERO_ROWS_CLOSED": ("exceptional-zero-row-proof",),
    "HARD_CORE_ROWS_CLOSED": ("hard-core-row-proof",),
    "GLOBAL_QUOTIENT_IMPLIES_ALL_N": (
        "all-n-implication-proof",
        "base-case-proof",
        "invariant-preservation-proof",
    ),
}


def exact_artifact(record: dict[str, Any], path: str) -> dict[str, Any]:
    artifact_id = record.get("artifact_id")
    obligation_id = record.get("obligation_id")
    artifact_kind = record.get("artifact_kind")
    locator = record.get("locator")
    digest = record.get("digest")
    statement = record.get("statement")
    support_ids = record.get("support_artifact_ids")
    evidence = record.get("evidence")
    require(isinstance(artifact_id, str) and artifact_id, f"{path}.artifact_id: required")
    require(obligation_id in REQUIRED_ARTIFACT_KINDS, f"{path}.obligation_id: unknown")
    require(isinstance(artifact_kind, str) and artifact_kind, f"{path}.artifact_kind: required")
    require(isinstance(locator, str) and locator, f"{path}.locator: required")
    require(isinstance(digest, str) and digest, f"{path}.digest: required")
    require(isinstance(statement, str) and statement, f"{path}.statement: required")
    require(isinstance(support_ids, list), f"{path}.support_artifact_ids: expected list")
    require(all(isinstance(value, str) and value for value in support_ids),
            f"{path}.support_artifact_ids: bad value")
    require(support_ids == sorted(support_ids), f"{path}.support_artifact_ids: sorted order required")
    require(len(support_ids) == len(set(support_ids)), f"{path}.support_artifact_ids: duplicates")
    require(artifact_id not in support_ids, f"{path}: artifact cannot support itself")
    require(isinstance(evidence, str) and evidence, f"{path}.evidence: required")
    output = {
        "artifact_id": artifact_id,
        "obligation_id": obligation_id,
        "artifact_kind": artifact_kind,
        "locator": locator,
        "digest": digest,
        "statement": statement,
        "support_artifact_ids": list(support_ids),
        "evidence": evidence,
    }
    output["artifact_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    closure_certificate = certificate.get("all_n_implication_closure_certificate")
    raw_artifacts = certificate.get("proof_artifacts")
    require(isinstance(closure_certificate, dict),
            "all_n_implication_closure_certificate: expected object")
    require(isinstance(raw_artifacts, list), "proof_artifacts: expected list")
    closure.validate_certificate(closure_certificate)
    closure_exact = closure.exact_certificate(closure_certificate)

    order = {obligation_id: index for index, obligation_id in enumerate(REQUIRED_ARTIFACT_KINDS)}
    artifacts = [exact_artifact(record, f"proof_artifacts[{index}]")
                 for index, record in enumerate(raw_artifacts)]
    require(raw_artifacts == artifacts, "proof_artifacts: canonical records or digests required")
    require(
        artifacts == sorted(
            artifacts,
            key=lambda item: (order[item["obligation_id"]], item["artifact_kind"], item["artifact_id"]),
        ),
        "proof_artifacts: canonical obligation/kind/id order required",
    )
    artifact_ids = [record["artifact_id"] for record in artifacts]
    require(len(artifact_ids) == len(set(artifact_ids)), "proof_artifacts: duplicate artifact_id")
    artifact_by_id = {record["artifact_id"]: record for record in artifacts}
    for record in artifacts:
        require(set(record["support_artifact_ids"]) <= set(artifact_by_id),
                f"artifact {record['artifact_id']}: unknown support artifact")

    by_obligation: dict[str, list[dict[str, Any]]] = {key: [] for key in REQUIRED_ARTIFACT_KINDS}
    for record in artifacts:
        by_obligation[record["obligation_id"]].append(record)

    obligation_by_id = {record["obligation_id"]: record
                        for record in closure_exact["proof_obligations"]}
    bundles = []
    proved_bundles = 0
    artifact_kind_counts: Counter[str] = Counter()
    for obligation_id in REQUIRED_ARTIFACT_KINDS:
        obligation = obligation_by_id[obligation_id]
        records = by_obligation[obligation_id]
        kinds = tuple(record["artifact_kind"] for record in records)
        required = REQUIRED_ARTIFACT_KINDS[obligation_id]
        if obligation["status"] == "proved":
            require(kinds == required,
                    f"obligation {obligation_id}: exact required artifact-kind sequence missing")
            proved_bundles += 1
        else:
            require(not records, f"obligation {obligation_id}: open obligation cannot contain artifacts")
        artifact_kind_counts.update(kinds)
        bundle = {
            "obligation_id": obligation_id,
            "declared_status": obligation["status"],
            "required_artifact_kinds": list(required),
            "artifact_ids": [record["artifact_id"] for record in records],
            "artifact_count": len(records),
            "artifacts_sha256": catalogue.canonical_digest(records),
        }
        bundle["artifact_bundle_sha256"] = catalogue.canonical_digest(bundle)
        if obligation["status"] == "proved":
            require(obligation["artifact_locator"] == f"artifact-registry://{obligation_id}",
                    f"obligation {obligation_id}: closure locator does not bind artifact registry")
            require(obligation["artifact_digest"] == bundle["artifact_bundle_sha256"],
                    f"obligation {obligation_id}: closure digest does not bind artifact bundle")
        bundles.append(bundle)

    claims = {
        "proof_obligations": len(REQUIRED_ARTIFACT_KINDS),
        "proof_artifacts": len(artifacts),
        "proved_artifact_bundles": proved_bundles,
        "open_artifact_bundles": len(REQUIRED_ARTIFACT_KINDS) - proved_bundles,
        "exact_typed_artifact_coverage": 1,
        "artifact_kind_distribution": [[kind, artifact_kind_counts[kind]]
                                       for kind in sorted(artifact_kind_counts)],
        "closure_sha256": closure_certificate["certificate_sha256"],
        "artifacts_sha256": catalogue.canonical_digest(artifacts),
        "artifact_bundles_sha256": catalogue.canonical_digest(bundles),
    }
    return {"proof_artifacts": artifacts, "artifact_bundle_records": bundles, "claims": claims}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("proof_artifacts", "artifact_bundle_records", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {"obligations": claims["proof_obligations"], "artifacts": claims["proof_artifacts"],
            "proved_bundles": claims["proved_artifact_bundles"],
            "exact": claims["exact_typed_artifact_coverage"]}


def build_certificate(closure_certificate: dict[str, Any], proof_artifacts: list[dict[str, Any]]) -> dict[str, Any]:
    ordered = [exact_artifact(record, "proof_artifact") for record in proof_artifacts]
    order = {obligation_id: index for index, obligation_id in enumerate(REQUIRED_ARTIFACT_KINDS)}
    ordered.sort(key=lambda item: (order[item["obligation_id"]], item["artifact_kind"], item["artifact_id"]))
    certificate: dict[str, Any] = {
        "version": 1,
        "all_n_implication_closure_certificate": closure_certificate,
        "proof_artifacts": ordered,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_obligation_artifact_registry.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
