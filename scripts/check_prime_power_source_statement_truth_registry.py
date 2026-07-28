#!/usr/bin/env python3
"""Validate exact statement text and typed verification for every cited rule source.

The existing rule-provenance certificate records a locator and statement SHA-256 for every
source, but does not carry the statement text or verify that the hash belongs to that text. This
checker supplies one canonical statement record per source, recomputes the UTF-8 SHA-256, records
an exact source-kind-specific verification artifact when proved, reconstructs every source's use
footprint, and seals the SOURCE_STATEMENTS_TRUE obligation with the complete registry bundle.

This is documentary verification infrastructure. It does not decide whether a supplied proof is
mathematically valid and permanently reports ``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_all_n_implication_closure as closure
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_rule_source_provenance as provenance
import check_prime_power_obligation_artifact_registry as obligation_artifacts


class SourceStatementTruthError(ValueError):
    """Raised when source statement truth records are incomplete or inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SourceStatementTruthError(message)


REQUIRED_VERIFICATION_KIND: dict[str, str] = {
    "definition": "definition-conformance-proof",
    "case-split": "case-split-exhaustiveness-proof",
    "lemma": "lemma-proof",
    "domain": "domain-characterization-proof",
    "exclusion": "exclusion-proof",
    "computation": "reproducible-computation-proof",
}


def text_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def exact_statement(record: dict[str, Any], source: dict[str, Any], path: str) -> dict[str, Any]:
    source_id = record.get("source_id")
    source_kind = record.get("source_kind")
    source_locator = record.get("source_locator")
    statement_text = record.get("statement_text")
    statement_digest = record.get("statement_sha256")
    status = record.get("verification_status")
    artifact_kind = record.get("verification_artifact_kind")
    artifact_locator = record.get("verification_artifact_locator")
    artifact_digest = record.get("verification_artifact_digest")
    note = record.get("verification_note")

    require(source_id == source["source_id"], f"{path}.source_id: source order/identity mismatch")
    require(source_kind == source["kind"], f"{path}.source_kind: provenance mismatch")
    require(source_locator == source["locator"], f"{path}.source_locator: provenance mismatch")
    require(isinstance(statement_text, str) and statement_text, f"{path}.statement_text: required")
    require(statement_text == statement_text.strip(), f"{path}.statement_text: outer whitespace forbidden")
    computed = text_sha256(statement_text)
    require(statement_digest == computed, f"{path}.statement_sha256: text digest mismatch")
    require(statement_digest == source["statement_sha256"], f"{path}.statement_sha256: provenance mismatch")
    require(status in {"proved", "open"}, f"{path}.verification_status: expected proved/open")
    require(isinstance(note, str) and note, f"{path}.verification_note: required")

    required_kind = REQUIRED_VERIFICATION_KIND[source_kind]
    if status == "proved":
        require(artifact_kind == required_kind, f"{path}.verification_artifact_kind: wrong kind")
        require(isinstance(artifact_locator, str) and artifact_locator,
                f"{path}.verification_artifact_locator: required")
        require(isinstance(artifact_digest, str) and artifact_digest,
                f"{path}.verification_artifact_digest: required")
    else:
        require(artifact_kind is None, f"{path}.verification_artifact_kind: open statement requires null")
        require(artifact_locator is None,
                f"{path}.verification_artifact_locator: open statement requires null")
        require(artifact_digest is None,
                f"{path}.verification_artifact_digest: open statement requires null")

    output = {
        "source_id": source_id,
        "source_kind": source_kind,
        "source_locator": source_locator,
        "statement_text": statement_text,
        "statement_sha256": statement_digest,
        "verification_status": status,
        "required_verification_artifact_kind": required_kind,
        "verification_artifact_kind": artifact_kind,
        "verification_artifact_locator": artifact_locator,
        "verification_artifact_digest": artifact_digest,
        "verification_note": note,
        "source_record_sha256": source["source_record_sha256"],
    }
    output["source_statement_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    provenance_certificate = certificate.get("rule_source_provenance_certificate")
    obligation_certificate = certificate.get("obligation_artifact_registry_certificate")
    raw_statements = certificate.get("source_statement_records")
    require(isinstance(provenance_certificate, dict),
            "rule_source_provenance_certificate: expected object")
    require(isinstance(obligation_certificate, dict),
            "obligation_artifact_registry_certificate: expected object")
    require(isinstance(raw_statements, list), "source_statement_records: expected list")

    provenance.validate_certificate(provenance_certificate)
    obligation_artifacts.validate_certificate(obligation_certificate)
    provenance_exact = provenance.exact_certificate(provenance_certificate)
    obligation_exact = obligation_artifacts.exact_certificate(obligation_certificate)
    closure_certificate = obligation_certificate["all_n_implication_closure_certificate"]
    closure_exact = closure.exact_certificate(closure_certificate)

    manifest = provenance_certificate["clause_manifest"]
    skeleton_certificate = closure_certificate["global_family_skeleton_certificate"]
    skeleton_exact = skeleton_certificate["recurrence_skeleton"]
    skeleton_rule_ids = {record["source_rule_id"] for record in skeleton_exact["parent_clauses"]}
    skeleton_case_ids = {record["source_case_id"] for record in skeleton_exact["parent_clauses"]}
    manifest_case_ids = {record["case_id"] for record in manifest["parent_cases"]}
    require(skeleton_rule_ids == {manifest["rule_id"]},
            "source provenance and global skeleton use different rule IDs")
    require(skeleton_case_ids == manifest_case_ids,
            "source provenance and global skeleton use different parent-case sets")

    sources = provenance_exact["sources"]
    require(len(raw_statements) == len(sources),
            "source_statement_records: exact source cardinality required")
    require([record.get("source_id") for record in raw_statements]
            == [record["source_id"] for record in sources],
            "source_statement_records: exact canonical source order required")
    statements = [
        exact_statement(record, source, f"source_statement_records[{index}]")
        for index, (record, source) in enumerate(zip(raw_statements, sources))
    ]
    require(raw_statements == statements,
            "source_statement_records: canonical records or digests required")

    usage: dict[str, dict[str, list[str]]] = {
        source["source_id"]: {"case_ids": [], "clause_ids": [], "axis_refs": [], "exclusion_refs": []}
        for source in sources
    }
    for record in provenance_exact["case_links"]:
        for source_id in record["source_ids"]:
            usage[source_id]["case_ids"].append(record["case_id"])
    for record in provenance_exact["clause_links"]:
        for source_id in record["source_ids"]:
            usage[source_id]["clause_ids"].append(record["clause_id"])
    for record in provenance_exact["axis_links"]:
        ref = f"{record['clause_id']}::{record['axis_name']}"
        for source_id in record["source_ids"]:
            usage[source_id]["axis_refs"].append(ref)
    for record in provenance_exact["exclusion_links"]:
        ref = f"{record['clause_id']}::{record['row_sha256']}"
        for source_id in record["source_ids"]:
            usage[source_id]["exclusion_refs"].append(ref)

    statement_by_id = {record["source_id"]: record for record in statements}
    bundle_records = []
    for source in sources:
        source_id = source["source_id"]
        footprint = {key: sorted(values) for key, values in usage[source_id].items()}
        impact = sum(len(values) for values in footprint.values())
        bundle = {
            "source_id": source_id,
            "source_kind": source["kind"],
            "verification_status": statement_by_id[source_id]["verification_status"],
            "statement_sha256": source["statement_sha256"],
            "source_statement_record_sha256": statement_by_id[source_id][
                "source_statement_record_sha256"
            ],
            **footprint,
            "total_rule_uses": impact,
        }
        bundle["source_truth_bundle_sha256"] = catalogue.canonical_digest(bundle)
        bundle_records.append(bundle)

    bundle_digest = catalogue.canonical_digest(bundle_records)
    source_truth_ready = int(all(record["verification_status"] == "proved" for record in statements))
    obligation_by_id = {
        record["obligation_id"]: record for record in closure_exact["proof_obligations"]
    }
    closure_by_id = {
        record["obligation_id"]: record for record in closure_exact["obligation_closure_records"]
    }
    source_obligation = obligation_by_id["SOURCE_STATEMENTS_TRUE"]
    source_closure = closure_by_id["SOURCE_STATEMENTS_TRUE"]
    require(int(source_closure["closed"]) == source_truth_ready,
            "SOURCE_STATEMENTS_TRUE closure disagrees with exact source verification census")

    source_artifacts = [
        record for record in obligation_exact["proof_artifacts"]
        if record["obligation_id"] == "SOURCE_STATEMENTS_TRUE"
    ]
    require(len(source_artifacts) == source_truth_ready,
            "SOURCE_STATEMENTS_TRUE typed artifact presence disagrees with source truth readiness")
    if source_truth_ready:
        source_artifact = source_artifacts[0]
        require(source_artifact["artifact_kind"] == "source-truth-proof",
                "SOURCE_STATEMENTS_TRUE requires source-truth-proof artifact")
        require(
            source_artifact["locator"]
            == "source-statement-truth-registry://SOURCE_STATEMENTS_TRUE",
            "source-truth-proof locator does not bind source truth registry",
        )
        require(source_artifact["digest"] == bundle_digest,
                "source-truth-proof digest does not bind source truth bundles")

    status_counts = Counter(record["verification_status"] for record in statements)
    kind_counts = Counter(record["source_kind"] for record in statements)
    open_by_impact = sorted(
        (record for record in bundle_records if record["verification_status"] == "open"),
        key=lambda record: (-record["total_rule_uses"], record["source_id"]),
    )
    claims = {
        "sources": len(sources),
        "proved_source_statements": status_counts["proved"],
        "open_source_statements": status_counts["open"],
        "source_statement_truth_ready": source_truth_ready,
        "source_truth_obligation_synchronized": 1,
        "exact_statement_text_hash_binding": 1,
        "exact_source_usage_footprints": 1,
        "all_n_proved_by_checker": 0,
        "open_source_ids_by_downstream_use": [record["source_id"] for record in open_by_impact],
        "source_kind_distribution": [[kind, kind_counts[kind]] for kind in sorted(kind_counts)],
        "rule_source_provenance_sha256": provenance_certificate["certificate_sha256"],
        "obligation_artifact_registry_sha256": obligation_certificate["certificate_sha256"],
        "all_n_implication_closure_sha256": closure_certificate["certificate_sha256"],
        "global_family_skeleton_sha256": skeleton_certificate["certificate_sha256"],
        "source_statement_records_sha256": catalogue.canonical_digest(statements),
        "source_truth_bundles_sha256": bundle_digest,
    }
    return {
        "source_statement_records": statements,
        "source_truth_bundle_records": bundle_records,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("source_statement_records", "source_truth_bundle_records", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {
        "sources": claims["sources"],
        "proved": claims["proved_source_statements"],
        "open": claims["open_source_statements"],
        "ready": claims["source_statement_truth_ready"],
        "all_n": claims["all_n_proved_by_checker"],
    }


def build_certificate(
    provenance_certificate: dict[str, Any],
    obligation_certificate: dict[str, Any],
    statement_records: list[dict[str, Any]],
) -> dict[str, Any]:
    sources = provenance.exact_certificate(provenance_certificate)["sources"]
    source_by_id = {record["source_id"]: record for record in sources}
    canonical = [
        exact_statement(record, source_by_id[record["source_id"]], "source_statement")
        for record in statement_records
    ]
    canonical.sort(key=lambda record: record["source_id"])
    certificate: dict[str, Any] = {
        "version": 1,
        "rule_source_provenance_certificate": provenance_certificate,
        "obligation_artifact_registry_certificate": obligation_certificate,
        "source_statement_records": canonical,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: check_prime_power_source_statement_truth_registry.py certificate.json"
        )
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
