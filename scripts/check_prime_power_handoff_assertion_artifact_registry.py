#!/usr/bin/env python3
"""Bind typed proof artifacts to the six final induction-handoff assertions.

Each declared proved handoff assertion receives exactly one assertion-specific artifact. The
artifact must cite the complete typed premise-artifact set of every final premise on which the
assertion depends, and the reconstructed bundle digest must be the digest stored by the handoff
assertion itself.

Passing proves documentary linkage only. It does not verify any assertion or supporting proof.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_final_induction_handoff as handoff
import check_prime_power_premise_artifact_registry as premise_registry


class HandoffAssertionArtifactError(ValueError):
    """Raised when a handoff-assertion artifact bundle is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise HandoffAssertionArtifactError(message)


REQUIRED_ASSERTION_ARTIFACT_KIND: dict[str, str] = {
    "BASE_DOMAIN_ESTABLISHED": "base-domain-handoff-proof",
    "NONBASE_RECURRENCE_COVERS_ALL_CASES": "nonbase-coverage-handoff-proof",
    "STATE_AND_RESOURCE_INVARIANTS_PRESERVED": "invariant-handoff-proof",
    "EVERY_RECURRENCE_BRANCH_TERMINATES": "termination-handoff-proof",
    "EXCEPTIONAL_AND_HARD_CORE_CASES_CLOSED": "exceptional-handoff-proof",
    "QUOTIENT_CONCLUSION_TRANSLATES_TO_D_EQ_2N": "objective-translation-handoff-proof",
}


def exact_artifact(record: dict[str, Any], path: str) -> dict[str, Any]:
    assertion_id = record.get("assertion_id")
    artifact_id = record.get("artifact_id")
    artifact_kind = record.get("artifact_kind")
    locator = record.get("locator")
    digest = record.get("digest")
    statement = record.get("statement")
    support_ids = record.get("support_premise_artifact_ids")
    evidence = record.get("evidence")
    require(assertion_id in REQUIRED_ASSERTION_ARTIFACT_KIND, f"{path}.assertion_id: unknown")
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
        artifact_kind == REQUIRED_ASSERTION_ARTIFACT_KIND[assertion_id],
        f"{path}: wrong assertion artifact kind",
    )
    require(isinstance(support_ids, list), f"{path}.support_premise_artifact_ids: expected list")
    require(
        all(isinstance(value, str) and value for value in support_ids),
        f"{path}.support_premise_artifact_ids: bad value",
    )
    require(
        support_ids == sorted(support_ids),
        f"{path}.support_premise_artifact_ids: sorted order required",
    )
    require(
        len(support_ids) == len(set(support_ids)),
        f"{path}.support_premise_artifact_ids: duplicates",
    )
    output = {
        "assertion_id": assertion_id,
        "artifact_id": artifact_id,
        "artifact_kind": artifact_kind,
        "locator": locator,
        "digest": digest,
        "statement": statement,
        "support_premise_artifact_ids": list(support_ids),
        "evidence": evidence,
    }
    output["handoff_assertion_artifact_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    handoff_certificate = certificate.get("final_induction_handoff_certificate")
    raw_artifacts = certificate.get("handoff_assertion_artifacts")
    require(isinstance(handoff_certificate, dict), "final_induction_handoff_certificate: expected object")
    require(isinstance(raw_artifacts, list), "handoff_assertion_artifacts: expected list")
    handoff.validate_certificate(handoff_certificate)
    handoff_exact = handoff.exact_certificate(handoff_certificate)

    premise_certificate = handoff_certificate["premise_artifact_registry_certificate"]
    premise_registry.validate_certificate(premise_certificate)
    premise_exact = premise_registry.exact_certificate(premise_certificate)
    premise_artifact_by_id = {
        record["artifact_id"]: record for record in premise_exact["premise_artifacts"]
    }
    premise_artifact_by_premise = {
        record["premise_id"]: record for record in premise_exact["premise_artifacts"]
    }

    order = {
        assertion_id: index for index, assertion_id in enumerate(REQUIRED_ASSERTION_ARTIFACT_KIND)
    }
    artifacts = [
        exact_artifact(record, f"handoff_assertion_artifacts[{index}]")
        for index, record in enumerate(raw_artifacts)
    ]
    require(raw_artifacts == artifacts, "handoff_assertion_artifacts: canonical records required")
    require(
        artifacts
        == sorted(artifacts, key=lambda item: (order[item["assertion_id"]], item["artifact_id"])),
        "handoff_assertion_artifacts: canonical assertion/artifact order required",
    )
    artifact_ids = [record["artifact_id"] for record in artifacts]
    require(len(artifact_ids) == len(set(artifact_ids)), "handoff_assertion_artifacts: duplicate artifact_id")
    assertion_ids = [record["assertion_id"] for record in artifacts]
    require(len(assertion_ids) == len(set(assertion_ids)), "handoff_assertion_artifacts: at most one per assertion")
    for artifact in artifacts:
        require(
            set(artifact["support_premise_artifact_ids"]) <= set(premise_artifact_by_id),
            f"assertion {artifact['assertion_id']}: unknown premise support artifact",
        )

    artifact_by_assertion = {record["assertion_id"]: record for record in artifacts}
    assertion_by_id = {
        record["assertion_id"]: record for record in handoff_exact["handoff_assertions"]
    }
    result_by_id = {
        record["assertion_id"]: record
        for record in handoff_exact["handoff_assertion_result_records"]
    }

    bundle_records = []
    kind_counts: Counter[str] = Counter()
    for assertion_id in REQUIRED_ASSERTION_ARTIFACT_KIND:
        assertion = assertion_by_id[assertion_id]
        result = result_by_id[assertion_id]
        artifact = artifact_by_assertion.get(assertion_id)
        required_support_ids = sorted(
            premise_artifact_by_premise[premise_id]["artifact_id"]
            for premise_id in assertion["dependency_premise_ids"]
            if premise_id in premise_artifact_by_premise
        )
        if assertion["status"] == "proved":
            require(artifact is not None, f"assertion {assertion_id}: proved assertion missing typed artifact")
            require(
                artifact["support_premise_artifact_ids"] == required_support_ids,
                f"assertion {assertion_id}: exact dependent premise-artifact support required",
            )
            require(
                len(required_support_ids) == len(assertion["dependency_premise_ids"]),
                f"assertion {assertion_id}: dependent premise artifact missing",
            )
            kind_counts[artifact["artifact_kind"]] += 1
            artifact_list = [artifact]
        else:
            require(artifact is None, f"assertion {assertion_id}: open assertion cannot contain artifact")
            artifact_list = []
        bundle = {
            "assertion_id": assertion_id,
            "declared_status": assertion["status"],
            "required_artifact_kind": REQUIRED_ASSERTION_ARTIFACT_KIND[assertion_id],
            "dependency_premise_ids": list(assertion["dependency_premise_ids"]),
            "required_support_premise_artifact_ids": required_support_ids,
            "artifact_ids": [record["artifact_id"] for record in artifact_list],
            "artifacts_sha256": catalogue.canonical_digest(artifact_list),
            "effective_assertion_closed": result["effective_assertion_closed"],
        }
        bundle["handoff_assertion_artifact_bundle_sha256"] = catalogue.canonical_digest(bundle)
        if assertion["status"] == "proved":
            require(
                assertion["artifact_locator"] == f"handoff-artifact-registry://{assertion_id}",
                f"assertion {assertion_id}: locator does not bind handoff artifact registry",
            )
            require(
                assertion["artifact_digest"] == bundle["handoff_assertion_artifact_bundle_sha256"],
                f"assertion {assertion_id}: digest does not bind handoff artifact bundle",
            )
        bundle_records.append(bundle)

    claims = {
        "handoff_assertions": len(REQUIRED_ASSERTION_ARTIFACT_KIND),
        "handoff_assertion_artifacts": len(artifacts),
        "proved_assertion_bundles": sum(record["declared_status"] == "proved" for record in bundle_records),
        "open_assertion_bundles": sum(record["declared_status"] == "open" for record in bundle_records),
        "exact_typed_handoff_artifact_coverage": 1,
        "artifact_kind_distribution": [[kind, kind_counts[kind]] for kind in sorted(kind_counts)],
        "final_induction_handoff_sha256": handoff_certificate["certificate_sha256"],
        "premise_artifact_registry_sha256": premise_certificate["certificate_sha256"],
        "handoff_assertion_artifacts_sha256": catalogue.canonical_digest(artifacts),
        "handoff_assertion_bundle_records_sha256": catalogue.canonical_digest(bundle_records),
    }
    return {
        "handoff_assertion_artifacts": artifacts,
        "handoff_assertion_artifact_bundle_records": bundle_records,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in (
        "handoff_assertion_artifacts",
        "handoff_assertion_artifact_bundle_records",
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
        "assertions": claims["handoff_assertions"],
        "artifacts": claims["handoff_assertion_artifacts"],
        "exact": claims["exact_typed_handoff_artifact_coverage"],
    }


def build_certificate(
    handoff_certificate: dict[str, Any],
    assertion_artifacts: list[dict[str, Any]],
) -> dict[str, Any]:
    canonical = [exact_artifact(record, "handoff_assertion_artifact") for record in assertion_artifacts]
    order = {
        assertion_id: index for index, assertion_id in enumerate(REQUIRED_ASSERTION_ARTIFACT_KIND)
    }
    canonical.sort(key=lambda item: (order[item["assertion_id"]], item["artifact_id"]))
    certificate: dict[str, Any] = {
        "version": 1,
        "final_induction_handoff_certificate": handoff_certificate,
        "handoff_assertion_artifacts": canonical,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_handoff_assertion_artifact_registry.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
