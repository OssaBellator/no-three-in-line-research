#!/usr/bin/env python3
"""Validate exact source statements and sealed typed verification artifacts.

For every source in the rule-provenance certificate, this checker binds literal UTF-8 statement
text to the stored statement SHA-256. A proved statement has exactly one source-kind-specific
verification artifact. The statement's verification locator is a canonical registry URI and its
verification digest is the reconstructed per-source artifact-bundle digest; the artifact carries
a separate external proof locator/digest and an acyclic support list.

This is documentary verification infrastructure. It does not decide whether a supplied proof is
mathematically valid and permanently reports ``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from heapq import heappop, heappush
from pathlib import Path
from typing import Any

import check_prime_power_all_n_implication_closure as closure
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_obligation_artifact_registry as obligation_artifacts
import check_prime_power_rule_source_provenance as provenance


class SourceStatementTruthError(ValueError):
    """Raised when source-statement truth records or verification artifacts are inconsistent."""


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


def exact_verification_artifact(
    record: dict[str, Any],
    source: dict[str, Any],
    statement: dict[str, Any],
    path: str,
) -> dict[str, Any]:
    source_id = record.get("source_id")
    artifact_id = record.get("artifact_id")
    artifact_kind = record.get("artifact_kind")
    statement_digest = record.get("statement_sha256")
    proof_locator = record.get("proof_locator")
    proof_digest = record.get("proof_digest")
    proof_statement = record.get("proof_statement")
    support_ids = record.get("support_artifact_ids")
    evidence = record.get("evidence")

    require(source_id == source["source_id"], f"{path}.source_id: provenance mismatch")
    for name, value in (
        ("artifact_id", artifact_id),
        ("artifact_kind", artifact_kind),
        ("proof_locator", proof_locator),
        ("proof_digest", proof_digest),
        ("proof_statement", proof_statement),
        ("evidence", evidence),
    ):
        require(isinstance(value, str) and value, f"{path}.{name}: required")
    require(
        artifact_kind == REQUIRED_VERIFICATION_KIND[source["kind"]],
        f"{path}.artifact_kind: wrong source-kind-specific artifact kind",
    )
    require(statement_digest == statement["statement_sha256"],
            f"{path}.statement_sha256: source statement mismatch")
    require(isinstance(support_ids, list), f"{path}.support_artifact_ids: expected list")
    require(all(isinstance(value, str) and value for value in support_ids),
            f"{path}.support_artifact_ids: bad value")
    require(support_ids == sorted(support_ids), f"{path}.support_artifact_ids: sorted order required")
    require(len(support_ids) == len(set(support_ids)), f"{path}.support_artifact_ids: duplicates")
    require(artifact_id not in support_ids, f"{path}: artifact cannot support itself")

    output = {
        "source_id": source_id,
        "artifact_id": artifact_id,
        "artifact_kind": artifact_kind,
        "statement_sha256": statement_digest,
        "proof_locator": proof_locator,
        "proof_digest": proof_digest,
        "proof_statement": proof_statement,
        "support_artifact_ids": list(support_ids),
        "evidence": evidence,
    }
    output["source_verification_artifact_sha256"] = catalogue.canonical_digest(output)
    return output


def topological_artifact_order(
    artifacts: list[dict[str, Any]],
) -> tuple[list[str], int]:
    artifact_by_id = {record["artifact_id"]: record for record in artifacts}
    children: dict[str, list[str]] = {artifact_id: [] for artifact_id in artifact_by_id}
    indegree = {artifact_id: 0 for artifact_id in artifact_by_id}
    edge_count = 0
    for record in artifacts:
        artifact_id = record["artifact_id"]
        for support_id in record["support_artifact_ids"]:
            require(support_id in artifact_by_id,
                    f"artifact {artifact_id}: unknown support artifact {support_id}")
            children[support_id].append(artifact_id)
            indegree[artifact_id] += 1
            edge_count += 1
    heap: list[str] = []
    for artifact_id, degree in indegree.items():
        if degree == 0:
            heappush(heap, artifact_id)
    order: list[str] = []
    while heap:
        artifact_id = heappop(heap)
        order.append(artifact_id)
        for child in sorted(children[artifact_id]):
            indegree[child] -= 1
            if indegree[child] == 0:
                heappush(heap, child)
    require(len(order) == len(artifacts),
            "source verification artifact support graph must be acyclic")
    return order, edge_count


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    provenance_certificate = certificate.get("rule_source_provenance_certificate")
    obligation_certificate = certificate.get("obligation_artifact_registry_certificate")
    raw_statements = certificate.get("source_statement_records")
    raw_artifacts = certificate.get("source_verification_artifacts")
    require(isinstance(provenance_certificate, dict),
            "rule_source_provenance_certificate: expected object")
    require(isinstance(obligation_certificate, dict),
            "obligation_artifact_registry_certificate: expected object")
    require(isinstance(raw_statements, list), "source_statement_records: expected list")
    require(isinstance(raw_artifacts, list), "source_verification_artifacts: expected list")

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
    source_by_id = {record["source_id"]: record for record in sources}
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
    statement_by_id = {record["source_id"]: record for record in statements}

    artifacts = []
    for index, record in enumerate(raw_artifacts):
        source_id = record.get("source_id")
        require(source_id in source_by_id,
                f"source_verification_artifacts[{index}].source_id: unknown source")
        require(source_id in statement_by_id,
                f"source_verification_artifacts[{index}].source_id: missing statement")
        artifacts.append(
            exact_verification_artifact(
                record,
                source_by_id[source_id],
                statement_by_id[source_id],
                f"source_verification_artifacts[{index}]",
            )
        )
    source_order = {record["source_id"]: index for index, record in enumerate(sources)}
    require(raw_artifacts == artifacts,
            "source_verification_artifacts: canonical records or digests required")
    require(
        artifacts == sorted(
            artifacts,
            key=lambda record: (source_order[record["source_id"]], record["artifact_id"]),
        ),
        "source_verification_artifacts: canonical source/artifact order required",
    )
    artifact_ids = [record["artifact_id"] for record in artifacts]
    artifact_source_ids = [record["source_id"] for record in artifacts]
    require(len(artifact_ids) == len(set(artifact_ids)),
            "source_verification_artifacts: duplicate artifact_id")
    require(len(artifact_source_ids) == len(set(artifact_source_ids)),
            "source_verification_artifacts: at most one artifact per source")
    artifact_by_source = {record["source_id"]: record for record in artifacts}
    topological_order, support_edges = topological_artifact_order(artifacts)

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

    bundle_records = []
    status_counts: Counter[str] = Counter()
    kind_counts: Counter[str] = Counter()
    artifact_kind_counts: Counter[str] = Counter()
    for source in sources:
        source_id = source["source_id"]
        statement = statement_by_id[source_id]
        artifact = artifact_by_source.get(source_id)
        proved = statement["verification_status"] == "proved"
        if proved:
            require(artifact is not None,
                    f"source {source_id}: proved statement missing sealed verification artifact")
            artifact_list = [artifact]
            artifact_kind_counts[artifact["artifact_kind"]] += 1
        else:
            require(artifact is None,
                    f"source {source_id}: open statement cannot contain verification artifact")
            artifact_list = []

        artifact_bundle = {
            "source_id": source_id,
            "required_verification_artifact_kind": REQUIRED_VERIFICATION_KIND[source["kind"]],
            "artifact_ids": [record["artifact_id"] for record in artifact_list],
            "artifacts_sha256": catalogue.canonical_digest(artifact_list),
        }
        artifact_bundle["source_verification_artifact_bundle_sha256"] = catalogue.canonical_digest(
            artifact_bundle
        )
        if proved:
            require(
                statement["verification_artifact_locator"]
                == f"source-verification-artifact-registry://{source_id}",
                f"source {source_id}: verification locator does not bind artifact registry",
            )
            require(
                statement["verification_artifact_digest"]
                == artifact_bundle["source_verification_artifact_bundle_sha256"],
                f"source {source_id}: verification digest does not bind artifact bundle",
            )

        footprint = {key: sorted(values) for key, values in usage[source_id].items()}
        bundle = {
            "source_id": source_id,
            "source_kind": source["kind"],
            "verification_status": statement["verification_status"],
            "statement_sha256": source["statement_sha256"],
            "source_statement_record_sha256": statement["source_statement_record_sha256"],
            "verification_artifact_ids": artifact_bundle["artifact_ids"],
            "verification_artifacts_sha256": artifact_bundle["artifacts_sha256"],
            "verification_artifact_bundle_sha256": artifact_bundle[
                "source_verification_artifact_bundle_sha256"
            ],
            **footprint,
            "total_rule_uses": sum(len(values) for values in footprint.values()),
        }
        bundle["source_truth_bundle_sha256"] = catalogue.canonical_digest(bundle)
        bundle_records.append(bundle)
        status_counts[statement["verification_status"]] += 1
        kind_counts[source["kind"]] += 1

    source_truth_bundle_digest = catalogue.canonical_digest(bundle_records)
    source_truth_ready = int(
        status_counts["proved"] == len(sources) and len(artifacts) == len(sources)
    )
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
        require(source_artifact["digest"] == source_truth_bundle_digest,
                "source-truth-proof digest does not bind source truth bundles")

    open_by_impact = sorted(
        (record for record in bundle_records if record["verification_status"] == "open"),
        key=lambda record: (-record["total_rule_uses"], record["source_id"]),
    )
    claims = {
        "sources": len(sources),
        "proved_source_statements": status_counts["proved"],
        "open_source_statements": status_counts["open"],
        "source_verification_artifacts": len(artifacts),
        "source_verification_support_edges": support_edges,
        "source_statement_truth_ready": source_truth_ready,
        "source_truth_obligation_synchronized": 1,
        "exact_statement_text_hash_binding": 1,
        "exact_source_usage_footprints": 1,
        "exact_source_verification_artifact_coverage": 1,
        "exact_statement_to_verification_bundle_binding": 1,
        "acyclic_source_verification_artifact_support": 1,
        "all_n_proved_by_checker": 0,
        "open_source_ids_by_downstream_use": [record["source_id"] for record in open_by_impact],
        "source_verification_artifact_topological_order": topological_order,
        "source_kind_distribution": [[kind, kind_counts[kind]] for kind in sorted(kind_counts)],
        "verification_artifact_kind_distribution": [
            [kind, artifact_kind_counts[kind]] for kind in sorted(artifact_kind_counts)
        ],
        "rule_source_provenance_sha256": provenance_certificate["certificate_sha256"],
        "obligation_artifact_registry_sha256": obligation_certificate["certificate_sha256"],
        "all_n_implication_closure_sha256": closure_certificate["certificate_sha256"],
        "global_family_skeleton_sha256": skeleton_certificate["certificate_sha256"],
        "source_statement_records_sha256": catalogue.canonical_digest(statements),
        "source_verification_artifacts_sha256": catalogue.canonical_digest(artifacts),
        "source_truth_bundles_sha256": source_truth_bundle_digest,
    }
    return {
        "source_statement_records": statements,
        "source_verification_artifacts": artifacts,
        "source_truth_bundle_records": bundle_records,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 2, "version: expected 2")
    exact = exact_certificate(certificate)
    for key in (
        "source_statement_records",
        "source_verification_artifacts",
        "source_truth_bundle_records",
        "claims",
    ):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {
        "sources": claims["sources"],
        "proved": claims["proved_source_statements"],
        "open": claims["open_source_statements"],
        "artifacts": claims["source_verification_artifacts"],
        "ready": claims["source_statement_truth_ready"],
        "all_n": claims["all_n_proved_by_checker"],
    }


def build_certificate(
    provenance_certificate: dict[str, Any],
    obligation_certificate: dict[str, Any],
    statement_records: list[dict[str, Any]],
    verification_artifacts: list[dict[str, Any]],
) -> dict[str, Any]:
    sources = provenance.exact_certificate(provenance_certificate)["sources"]
    source_by_id = {record["source_id"]: record for record in sources}
    canonical_statements = [
        exact_statement(record, source_by_id[record["source_id"]], "source_statement")
        for record in statement_records
    ]
    canonical_statements.sort(key=lambda record: record["source_id"])
    statement_by_id = {record["source_id"]: record for record in canonical_statements}
    canonical_artifacts = [
        exact_verification_artifact(
            record,
            source_by_id[record["source_id"]],
            statement_by_id[record["source_id"]],
            "source_verification_artifact",
        )
        for record in verification_artifacts
    ]
    source_order = {record["source_id"]: index for index, record in enumerate(sources)}
    canonical_artifacts.sort(
        key=lambda record: (source_order[record["source_id"]], record["artifact_id"])
    )
    certificate: dict[str, Any] = {
        "version": 2,
        "rule_source_provenance_certificate": provenance_certificate,
        "obligation_artifact_registry_certificate": obligation_certificate,
        "source_statement_records": canonical_statements,
        "source_verification_artifacts": canonical_artifacts,
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
