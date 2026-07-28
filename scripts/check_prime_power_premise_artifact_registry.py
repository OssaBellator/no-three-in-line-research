#!/usr/bin/env python3
"""Bind typed proof artifacts to the ten final implication premises.

The final implication premise contract currently accepts opaque locator/digest pairs. This
checker replaces each proved premise's opaque pair by one exact premise-specific artifact
bundle and requires that bundle to cite artifacts from every semantic obligation on which the
premise depends.

Passing proves documentary linkage only, not the truth of premise artifacts.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_final_implication_premise_contract as contract
import check_prime_power_obligation_artifact_registry as obligation_artifacts


class PremiseArtifactError(ValueError):
    """Raised when a final-premise artifact bundle is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise PremiseArtifactError(message)


REQUIRED_PREMISE_ARTIFACT_KIND: dict[str, str] = {
    "BASE_CASES_COMPLETE": "base-case-domain-proof",
    "RECURRENCE_EXHAUSTIVE": "recurrence-exhaustiveness-proof",
    "STATE_INVARIANTS_PRESERVED": "invariant-preservation-proof",
    "OPERATION_SELECTION_SOUND": "operation-selection-soundness-proof",
    "RESOURCE_AND_CREDIT_SOUND": "resource-credit-soundness-proof",
    "BLOCK_AND_AUXILIARY_CONTRACTION": "block-auxiliary-contraction-proof",
    "CROSS_BLOCK_ASSEMBLY_SOUND": "cross-block-assembly-proof",
    "EXCEPTIONAL_CASES_CLOSED": "exceptional-hard-core-closure-proof",
    "TERMINATION_ARGUMENT": "termination-proof",
    "OBJECTIVE_TRANSLATION_TO_D_EQ_2N": "objective-translation-proof",
}


def exact_artifact(record: dict[str, Any], path: str) -> dict[str, Any]:
    premise_id = record.get("premise_id")
    artifact_id = record.get("artifact_id")
    kind = record.get("artifact_kind")
    locator = record.get("locator")
    digest = record.get("digest")
    statement = record.get("statement")
    support_ids = record.get("support_obligation_artifact_ids")
    finite_sha = record.get("finite_certificate_sha256")
    evidence = record.get("evidence")
    require(premise_id in REQUIRED_PREMISE_ARTIFACT_KIND, f"{path}.premise_id: unknown")
    for name, value in (("artifact_id", artifact_id), ("artifact_kind", kind),
                        ("locator", locator), ("digest", digest),
                        ("statement", statement), ("evidence", evidence)):
        require(isinstance(value, str) and value, f"{path}.{name}: required")
    require(kind == REQUIRED_PREMISE_ARTIFACT_KIND[premise_id], f"{path}: wrong premise artifact kind")
    require(isinstance(support_ids, list), f"{path}.support_obligation_artifact_ids: expected list")
    require(all(isinstance(value, str) and value for value in support_ids),
            f"{path}.support_obligation_artifact_ids: bad value")
    require(support_ids == sorted(support_ids), f"{path}.support_obligation_artifact_ids: sorted order required")
    require(len(support_ids) == len(set(support_ids)), f"{path}.support_obligation_artifact_ids: duplicates")
    require(finite_sha is None or (isinstance(finite_sha, str) and finite_sha),
            f"{path}.finite_certificate_sha256: bad value")
    output = {
        "premise_id": premise_id,
        "artifact_id": artifact_id,
        "artifact_kind": kind,
        "locator": locator,
        "digest": digest,
        "statement": statement,
        "support_obligation_artifact_ids": list(support_ids),
        "finite_certificate_sha256": finite_sha,
        "evidence": evidence,
    }
    output["premise_artifact_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    contract_certificate = certificate.get("final_implication_premise_contract_certificate")
    raw_artifacts = certificate.get("premise_artifacts")
    require(isinstance(contract_certificate, dict),
            "final_implication_premise_contract_certificate: expected object")
    require(isinstance(raw_artifacts, list), "premise_artifacts: expected list")
    contract.validate_certificate(contract_certificate)
    contract_exact = contract.exact_certificate(contract_certificate)

    obligation_registry = contract_certificate["obligation_artifact_registry_certificate"]
    obligation_artifacts.validate_certificate(obligation_registry)
    obligation_exact = obligation_artifacts.exact_certificate(obligation_registry)
    obligation_artifact_by_id = {
        record["artifact_id"]: record for record in obligation_exact["proof_artifacts"]
    }

    order = {premise_id: index for index, premise_id in enumerate(REQUIRED_PREMISE_ARTIFACT_KIND)}
    artifacts = [exact_artifact(record, f"premise_artifacts[{index}]")
                 for index, record in enumerate(raw_artifacts)]
    require(raw_artifacts == artifacts, "premise_artifacts: canonical records or digests required")
    require(artifacts == sorted(artifacts, key=lambda item: (order[item["premise_id"]], item["artifact_id"])),
            "premise_artifacts: canonical premise/artifact order required")
    artifact_ids = [record["artifact_id"] for record in artifacts]
    require(len(artifact_ids) == len(set(artifact_ids)), "premise_artifacts: duplicate artifact_id")
    require(len({record["premise_id"] for record in artifacts}) == len(artifacts),
            "premise_artifacts: at most one artifact per premise")
    for artifact in artifacts:
        require(set(artifact["support_obligation_artifact_ids"]) <= set(obligation_artifact_by_id),
                f"premise {artifact['premise_id']}: unknown obligation support artifact")

    artifact_by_premise = {record["premise_id"]: record for record in artifacts}
    premise_by_id = {record["premise_id"]: record for record in contract_exact["implication_premises"]}
    result_by_id = {record["premise_id"]: record for record in contract_exact["premise_result_records"]}
    edgewise_sha = contract_certificate["edgewise_lexicographic_support_certificate"]["certificate_sha256"]

    bundle_records = []
    kind_counts: Counter[str] = Counter()
    for premise_id in REQUIRED_PREMISE_ARTIFACT_KIND:
        premise = premise_by_id[premise_id]
        result = result_by_id[premise_id]
        artifact = artifact_by_premise.get(premise_id)
        if premise["status"] == "proved":
            require(artifact is not None, f"premise {premise_id}: proved premise missing typed artifact")
            cited_obligations = {
                obligation_artifact_by_id[artifact_id]["obligation_id"]
                for artifact_id in artifact["support_obligation_artifact_ids"]
            }
            missing = [dependency for dependency in premise["dependency_obligation_ids"]
                       if dependency not in cited_obligations]
            require(not missing, f"premise {premise_id}: missing dependency artifact support {missing}")
            if premise_id == "TERMINATION_ARGUMENT" and premise["proof_mode"] == "edgewise-lex":
                require(artifact["finite_certificate_sha256"] == edgewise_sha,
                        "TERMINATION_ARGUMENT: edgewise proof must bind exact edgewise certificate")
            else:
                require(artifact["finite_certificate_sha256"] is None,
                        f"premise {premise_id}: unexpected finite certificate binding")
            kind_counts[artifact["artifact_kind"]] += 1
            artifact_list = [artifact]
        else:
            require(artifact is None, f"premise {premise_id}: open premise cannot contain typed artifact")
            artifact_list = []
        bundle = {
            "premise_id": premise_id,
            "declared_status": premise["status"],
            "proof_mode": premise["proof_mode"],
            "required_artifact_kind": REQUIRED_PREMISE_ARTIFACT_KIND[premise_id],
            "artifact_ids": [record["artifact_id"] for record in artifact_list],
            "artifacts_sha256": catalogue.canonical_digest(artifact_list),
            "dependency_obligation_ids": list(premise["dependency_obligation_ids"]),
            "effective_premise_closed": result["effective_premise_closed"],
        }
        bundle["premise_artifact_bundle_sha256"] = catalogue.canonical_digest(bundle)
        if premise["status"] == "proved":
            require(premise["artifact_locator"] == f"premise-artifact-registry://{premise_id}",
                    f"premise {premise_id}: locator does not bind premise registry")
            require(premise["artifact_digest"] == bundle["premise_artifact_bundle_sha256"],
                    f"premise {premise_id}: digest does not bind premise artifact bundle")
        bundle_records.append(bundle)

    claims = {
        "implication_premises": len(REQUIRED_PREMISE_ARTIFACT_KIND),
        "premise_artifacts": len(artifacts),
        "proved_premise_bundles": sum(record["declared_status"] == "proved" for record in bundle_records),
        "open_premise_bundles": sum(record["declared_status"] == "open" for record in bundle_records),
        "exact_typed_premise_artifact_coverage": 1,
        "artifact_kind_distribution": [[kind, kind_counts[kind]] for kind in sorted(kind_counts)],
        "final_contract_sha256": contract_certificate["certificate_sha256"],
        "obligation_artifact_registry_sha256": obligation_registry["certificate_sha256"],
        "premise_artifacts_sha256": catalogue.canonical_digest(artifacts),
        "premise_bundle_records_sha256": catalogue.canonical_digest(bundle_records),
    }
    return {"premise_artifacts": artifacts, "premise_artifact_bundle_records": bundle_records, "claims": claims}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("premise_artifacts", "premise_artifact_bundle_records", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {"premises": claims["implication_premises"], "artifacts": claims["premise_artifacts"],
            "exact": claims["exact_typed_premise_artifact_coverage"]}


def build_certificate(contract_certificate: dict[str, Any], premise_artifacts: list[dict[str, Any]]) -> dict[str, Any]:
    canonical = [exact_artifact(record, "premise_artifact") for record in premise_artifacts]
    order = {premise_id: index for index, premise_id in enumerate(REQUIRED_PREMISE_ARTIFACT_KIND)}
    canonical.sort(key=lambda item: (order[item["premise_id"]], item["artifact_id"]))
    certificate: dict[str, Any] = {
        "version": 1,
        "final_implication_premise_contract_certificate": contract_certificate,
        "premise_artifacts": canonical,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_premise_artifact_registry.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
