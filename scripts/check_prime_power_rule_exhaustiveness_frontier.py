#!/usr/bin/env python3
"""Validate and synchronize the exact T02 rule-exhaustiveness proof bank.

The parent-rule clause manifest enumerates operation slots relative to supplied rule data, while
the global recurrence skeleton currently names only a source rule and source case for each global
parent. This checker makes the T02 proof surface exact. It requires one sealed proof record for
every parent case, clause, parameter axis, excluded row and global-parent application. Every
global parent application must identify one exact enumerated operation slot and therefore one
exact source clause and admitted parameter row.

The checker also binds the existing ``rule-manifest`` and ``rule-exhaustiveness-proof`` obligation
artifacts to reconstructed bundles and synchronizes the result with ``RULE_EXHAUSTIVE`` and
``T02_RULE_EXHAUSTIVENESS``. It verifies documentary identity and support only, never mathematical
truth, and permanently reports ``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_all_n_implication_closure as closure
import check_prime_power_atomic_frontier_execution as atomic
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_obligation_artifact_registry as obligation_artifacts
import check_prime_power_parent_rule_clause_enumerator as clauses
import check_prime_power_rule_source_provenance as provenance
import check_prime_power_source_statement_truth_registry as source_truth
import check_prime_power_source_truth_frontier_execution as source_frontier


class RuleExhaustivenessFrontierError(ValueError):
    """Raised when the exact T02 rule-exhaustiveness bank is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuleExhaustivenessFrontierError(message)


RECORD_KINDS = {
    "parent-case": "parent-case-exhaustiveness-proof",
    "clause": "clause-exhaustiveness-proof",
    "axis": "axis-domain-exhaustiveness-proof",
    "exclusion": "exclusion-validity-proof",
    "global-parent-application": "global-parent-application-proof",
}


def record_id_for(kind: str, *parts: str) -> str:
    return "::".join((kind, *parts))


def exact_status_record(
    record: dict[str, Any],
    *,
    record_id: str,
    record_kind: str,
    identity: dict[str, str],
    path: str,
) -> dict[str, Any]:
    require(record.get("record_id") == record_id, f"{path}.record_id: mismatch")
    require(record.get("record_kind") == record_kind, f"{path}.record_kind: mismatch")
    require(record.get("identity") == identity, f"{path}.identity: exact identity required")
    status = record.get("status")
    locator = record.get("verification_locator")
    digest = record.get("verification_digest")
    note = record.get("note")
    require(status in {"proved", "open"}, f"{path}.status: expected proved/open")
    require(isinstance(note, str) and note, f"{path}.note: required")
    if status == "proved":
        require(
            locator == f"rule-exhaustiveness-artifact-registry://{record_id}",
            f"{path}.verification_locator: canonical registry URI required",
        )
        require(isinstance(digest, str) and digest, f"{path}.verification_digest: required")
    else:
        require(locator is None, f"{path}.verification_locator: open record requires null")
        require(digest is None, f"{path}.verification_digest: open record requires null")
    output = {
        "record_id": record_id,
        "record_kind": record_kind,
        "identity": dict(identity),
        "status": status,
        "verification_locator": locator,
        "verification_digest": digest,
        "note": note,
    }
    output["rule_exhaustiveness_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_artifact(
    record: dict[str, Any],
    *,
    status_record: dict[str, Any],
    required_kind: str,
    expected_source_support_ids: list[str],
    expected_rule_support_ids: list[str],
    path: str,
) -> dict[str, Any]:
    record_id = record.get("record_id")
    artifact_id = record.get("artifact_id")
    artifact_kind = record.get("artifact_kind")
    proof_locator = record.get("proof_locator")
    proof_digest = record.get("proof_digest")
    proof_statement = record.get("proof_statement")
    source_support = record.get("support_source_verification_artifact_ids")
    rule_support = record.get("support_rule_exhaustiveness_artifact_ids")
    evidence = record.get("evidence")

    require(record_id == status_record["record_id"], f"{path}.record_id: status-record mismatch")
    for name, value in (
        ("artifact_id", artifact_id),
        ("artifact_kind", artifact_kind),
        ("proof_locator", proof_locator),
        ("proof_digest", proof_digest),
        ("proof_statement", proof_statement),
        ("evidence", evidence),
    ):
        require(isinstance(value, str) and value, f"{path}.{name}: required")
    require(artifact_kind == required_kind, f"{path}.artifact_kind: wrong kind")
    require(
        source_support == expected_source_support_ids,
        f"{path}.support_source_verification_artifact_ids: exact support required",
    )
    require(
        rule_support == expected_rule_support_ids,
        f"{path}.support_rule_exhaustiveness_artifact_ids: exact support required",
    )
    require(artifact_id not in rule_support, f"{path}: artifact cannot support itself")
    output = {
        "record_id": record_id,
        "artifact_id": artifact_id,
        "artifact_kind": artifact_kind,
        "proof_locator": proof_locator,
        "proof_digest": proof_digest,
        "proof_statement": proof_statement,
        "support_source_verification_artifact_ids": list(source_support),
        "support_rule_exhaustiveness_artifact_ids": list(rule_support),
        "evidence": evidence,
    }
    output["rule_exhaustiveness_artifact_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    source_frontier_certificate = certificate.get("source_truth_frontier_execution_certificate")
    raw_records = certificate.get("rule_exhaustiveness_records")
    raw_artifacts = certificate.get("rule_exhaustiveness_artifacts")
    require(
        isinstance(source_frontier_certificate, dict),
        "source_truth_frontier_execution_certificate: expected object",
    )
    require(isinstance(raw_records, list), "rule_exhaustiveness_records: expected list")
    require(isinstance(raw_artifacts, list), "rule_exhaustiveness_artifacts: expected list")

    source_frontier.validate_certificate(source_frontier_certificate)
    source_certificate = source_frontier_certificate["source_statement_truth_registry_certificate"]
    source_truth.validate_certificate(source_certificate)
    source_exact = source_truth.exact_certificate(source_certificate)
    provenance_certificate = source_certificate["rule_source_provenance_certificate"]
    provenance.validate_certificate(provenance_certificate)
    provenance_exact = provenance.exact_certificate(provenance_certificate)
    manifest = provenance_certificate["clause_manifest"]
    clauses.validate_manifest(manifest)
    manifest_exact = clauses.exact_enumerator(manifest)
    slot_registry = manifest["expected_slot_registry"]

    obligation_certificate = source_certificate["obligation_artifact_registry_certificate"]
    obligation_artifacts.validate_certificate(obligation_certificate)
    obligation_exact = obligation_artifacts.exact_certificate(obligation_certificate)
    closure_certificate = obligation_certificate["all_n_implication_closure_certificate"]
    closure_exact = closure.exact_certificate(closure_certificate)
    skeleton_certificate = closure_certificate["global_family_skeleton_certificate"]
    skeleton = skeleton_certificate["recurrence_skeleton"]

    current_certificate = source_frontier_certificate["current_frontier_execution_certificate"]
    atomic_certificate = current_certificate["atomic_frontier_execution_certificate"]
    atomic_exact = atomic.exact_certificate(atomic_certificate)

    source_artifact_by_source = {
        record["source_id"]: record["artifact_id"]
        for record in source_exact["source_verification_artifacts"]
    }
    case_source_ids = {
        record["case_id"]: record["source_ids"] for record in provenance_exact["case_links"]
    }
    clause_source_ids = {
        record["clause_id"]: record["source_ids"] for record in provenance_exact["clause_links"]
    }
    axis_source_ids = {
        (record["clause_id"], record["axis_name"]): record["source_ids"]
        for record in provenance_exact["axis_links"]
    }
    exclusion_source_ids = {
        (record["clause_id"], record["row_sha256"]): record["source_ids"]
        for record in provenance_exact["exclusion_links"]
    }

    cases = {record["case_id"]: record for record in manifest_exact["parent_cases"]}
    manifest_clauses = {record["clause_id"]: record for record in manifest_exact["clauses"]}
    slots = {record["slot_id"]: record for record in slot_registry["slots"]}
    skeleton_by_parent = {
        record["parent_global_state_id"]: record for record in skeleton["parent_clauses"]
    }

    expected_specs: list[dict[str, Any]] = []
    for case_id in sorted(cases):
        expected_specs.append({
            "record_id": record_id_for("case", case_id),
            "record_kind": "parent-case",
            "identity": {"case_id": case_id},
        })
    for clause_id in sorted(manifest_clauses):
        expected_specs.append({
            "record_id": record_id_for("clause", clause_id),
            "record_kind": "clause",
            "identity": {"clause_id": clause_id},
        })
    for clause_id in sorted(manifest_clauses):
        clause = manifest_clauses[clause_id]
        for axis in clause["parameter_axes"]:
            expected_specs.append({
                "record_id": record_id_for("axis", clause_id, axis["name"]),
                "record_kind": "axis",
                "identity": {"clause_id": clause_id, "axis_name": axis["name"]},
            })
    for clause_id in sorted(manifest_clauses):
        clause = manifest_clauses[clause_id]
        for excluded in clause["excluded_parameter_rows"]:
            row_sha = catalogue.canonical_digest(excluded["row"])
            expected_specs.append({
                "record_id": record_id_for("exclusion", clause_id, row_sha),
                "record_kind": "exclusion",
                "identity": {"clause_id": clause_id, "row_sha256": row_sha},
            })
    for parent in sorted(skeleton_by_parent):
        raw = next(
            (
                record for record in raw_records
                if record.get("record_id") == record_id_for("application", parent)
            ),
            None,
        )
        require(isinstance(raw, dict), f"application {parent}: exact record required")
        identity = raw.get("identity")
        require(isinstance(identity, dict), f"application {parent}.identity: expected object")
        expected_specs.append({
            "record_id": record_id_for("application", parent),
            "record_kind": "global-parent-application",
            "identity": {
                "parent_global_state_id": parent,
                "source_case_id": identity.get("source_case_id"),
                "source_clause_id": identity.get("source_clause_id"),
                "operation_slot_id": identity.get("operation_slot_id"),
            },
        })

    require(len(raw_records) == len(expected_specs), "rule_exhaustiveness_records: exact count required")
    require(
        [record.get("record_id") for record in raw_records]
        == [spec["record_id"] for spec in expected_specs],
        "rule_exhaustiveness_records: exact canonical order required",
    )
    records = [
        exact_status_record(
            record,
            record_id=spec["record_id"],
            record_kind=spec["record_kind"],
            identity=spec["identity"],
            path=f"rule_exhaustiveness_records[{index}]",
        )
        for index, (record, spec) in enumerate(zip(raw_records, expected_specs))
    ]
    require(raw_records == records, "rule_exhaustiveness_records: canonical records/digests required")
    record_by_id = {record["record_id"]: record for record in records}

    for parent, skeleton_clause in skeleton_by_parent.items():
        record = record_by_id[record_id_for("application", parent)]
        identity = record["identity"]
        case_id = identity["source_case_id"]
        clause_id = identity["source_clause_id"]
        slot_id = identity["operation_slot_id"]
        require(case_id == skeleton_clause["source_case_id"],
                f"application {parent}: skeleton case mismatch")
        require(skeleton_clause["source_rule_id"] == manifest["rule_id"],
                f"application {parent}: skeleton rule mismatch")
        require(case_id in cases, f"application {parent}: unknown case")
        require(clause_id in manifest_clauses, f"application {parent}: unknown clause")
        require(slot_id in slots, f"application {parent}: unknown operation slot")
        case = cases[case_id]
        clause = manifest_clauses[clause_id]
        slot = slots[slot_id]
        key = slot["operation_key"]
        require(key.get("case_id") == case_id, f"application {parent}: slot case mismatch")
        require(key.get("clause_id") == clause_id, f"application {parent}: slot clause mismatch")
        require(clause_id in case["applicable_clause_ids"],
                f"application {parent}: clause not applicable to case")
        require(case_id in clause["case_ids"],
                f"application {parent}: case absent from clause")
        require(slot["parent_state_id"] == case["parent_state_id"],
                f"application {parent}: parent-state mismatch")
        require(slot["expected_host_id"] == case["expected_host_id"],
                f"application {parent}: expected-host mismatch")
        require(slot["state_labels"] == case["state_labels"],
                f"application {parent}: state-label mismatch")
        require(slot["operation_kind"] == clause["operation_kind"],
                f"application {parent}: operation-kind mismatch")

    artifact_by_record_raw: dict[str, list[dict[str, Any]]] = {
        record["record_id"]: [] for record in records
    }
    for artifact in raw_artifacts:
        require(isinstance(artifact, dict), "rule_exhaustiveness_artifacts: expected objects")
        record_id = artifact.get("record_id")
        require(record_id in artifact_by_record_raw,
                f"rule_exhaustiveness_artifacts: unknown record {record_id}")
        artifact_by_record_raw[record_id].append(artifact)

    artifacts: list[dict[str, Any]] = []
    rule_artifact_id_by_record: dict[str, str] = {}
    for record in records:
        record_id = record["record_id"]
        raw_group = artifact_by_record_raw[record_id]
        if record["status"] == "proved":
            require(len(raw_group) == 1, f"record {record_id}: exactly one artifact required")
            rule_artifact_id_by_record[record_id] = raw_group[0].get("artifact_id")
        else:
            require(not raw_group, f"record {record_id}: open record cannot contain artifact")

    for record in records:
        if record["status"] != "proved":
            continue
        record_id = record["record_id"]
        kind = record["record_kind"]
        identity = record["identity"]
        if kind == "parent-case":
            case_id = identity["case_id"]
            source_ids = case_source_ids[case_id]
            dependency_record_ids = [
                record_id_for("clause", clause_id)
                for clause_id in sorted(cases[case_id]["applicable_clause_ids"])
            ]
        elif kind == "clause":
            clause_id = identity["clause_id"]
            source_ids = clause_source_ids[clause_id]
            dependency_record_ids = [
                record_id_for("axis", clause_id, axis["name"])
                for axis in manifest_clauses[clause_id]["parameter_axes"]
            ] + [
                record_id_for(
                    "exclusion",
                    clause_id,
                    catalogue.canonical_digest(excluded["row"]),
                )
                for excluded in manifest_clauses[clause_id]["excluded_parameter_rows"]
            ]
        elif kind == "axis":
            key = (identity["clause_id"], identity["axis_name"])
            source_ids = axis_source_ids[key]
            dependency_record_ids = []
        elif kind == "exclusion":
            key = (identity["clause_id"], identity["row_sha256"])
            source_ids = exclusion_source_ids[key]
            dependency_record_ids = []
        else:
            case_id = identity["source_case_id"]
            clause_id = identity["source_clause_id"]
            source_ids = sorted(set(case_source_ids[case_id]) | set(clause_source_ids[clause_id]))
            dependency_record_ids = [
                record_id_for("case", case_id),
                record_id_for("clause", clause_id),
            ]

        require(
            all(source_id in source_artifact_by_source for source_id in source_ids),
            f"record {record_id}: source statements must be proved before rule record",
        )
        require(
            all(dep in rule_artifact_id_by_record for dep in dependency_record_ids),
            f"record {record_id}: dependent rule records must be proved first",
        )
        expected_source_support = sorted(
            source_artifact_by_source[source_id] for source_id in source_ids
        )
        expected_rule_support = sorted(
            rule_artifact_id_by_record[dep] for dep in dependency_record_ids
        )
        raw_artifact = artifact_by_record_raw[record_id][0]
        artifact = exact_artifact(
            raw_artifact,
            status_record=record,
            required_kind=RECORD_KINDS[kind],
            expected_source_support_ids=expected_source_support,
            expected_rule_support_ids=expected_rule_support,
            path=f"rule_exhaustiveness_artifact[{record_id}]",
        )
        bundle = {
            "record_id": record_id,
            "required_artifact_kind": RECORD_KINDS[kind],
            "artifact_ids": [artifact["artifact_id"]],
            "artifacts_sha256": catalogue.canonical_digest([artifact]),
        }
        bundle["rule_exhaustiveness_artifact_bundle_sha256"] = catalogue.canonical_digest(bundle)
        require(
            record["verification_digest"]
            == bundle["rule_exhaustiveness_artifact_bundle_sha256"],
            f"record {record_id}: verification digest does not bind artifact bundle",
        )
        artifacts.append(artifact)

    require(
        raw_artifacts == artifacts,
        "rule_exhaustiveness_artifacts: canonical record order/content required",
    )
    artifact_ids = [record["artifact_id"] for record in artifacts]
    require(len(artifact_ids) == len(set(artifact_ids)),
            "rule_exhaustiveness_artifacts: duplicate artifact_id")
    artifact_id_set = set(artifact_ids)
    for artifact in artifacts:
        require(
            set(artifact["support_rule_exhaustiveness_artifact_ids"]) <= artifact_id_set,
            f"artifact {artifact['artifact_id']}: unknown rule support artifact",
        )

    manifest_bundle = {
        "rule_id": manifest["rule_id"],
        "rule_source_sha256": catalogue.canonical_digest(manifest["rule_source"]),
        "clause_manifest_sha256": manifest["manifest_sha256"],
        "expected_slot_registry_sha256": slot_registry["registry_sha256"],
        "recurrence_skeleton_sha256": skeleton["recurrence_skeleton_sha256"],
        "parent_cases_sha256": catalogue.canonical_digest(manifest_exact["parent_cases"]),
        "clauses_sha256": catalogue.canonical_digest(manifest_exact["clauses"]),
    }
    manifest_bundle["rule_manifest_bundle_sha256"] = catalogue.canonical_digest(manifest_bundle)

    proof_bundle = {
        "rule_manifest_bundle_sha256": manifest_bundle["rule_manifest_bundle_sha256"],
        "source_statement_truth_registry_sha256": source_certificate["certificate_sha256"],
        "rule_exhaustiveness_records_sha256": catalogue.canonical_digest(records),
        "rule_exhaustiveness_artifacts_sha256": catalogue.canonical_digest(artifacts),
    }
    proof_bundle["rule_exhaustiveness_proof_bundle_sha256"] = catalogue.canonical_digest(proof_bundle)

    source_ready = int(source_exact["claims"]["source_statement_truth_ready"])
    all_records_proved = int(all(record["status"] == "proved" for record in records))
    rule_ready = int(source_ready and all_records_proved and len(artifacts) == len(records))

    obligation_by_id = {
        record["obligation_id"]: record for record in closure_exact["proof_obligations"]
    }
    closure_by_id = {
        record["obligation_id"]: record for record in closure_exact["obligation_closure_records"]
    }
    rule_closure = closure_by_id["RULE_EXHAUSTIVE"]
    require(int(rule_closure["closed"]) == rule_ready,
            "RULE_EXHAUSTIVE closure disagrees with exact rule proof bank")

    rule_obligation_artifacts = [
        record for record in obligation_exact["proof_artifacts"]
        if record["obligation_id"] == "RULE_EXHAUSTIVE"
    ]
    require(len(rule_obligation_artifacts) == 2 * rule_ready,
            "RULE_EXHAUSTIVE typed artifact presence disagrees with rule readiness")
    if rule_ready:
        by_kind = {record["artifact_kind"]: record for record in rule_obligation_artifacts}
        require(set(by_kind) == {"rule-exhaustiveness-proof", "rule-manifest"},
                "RULE_EXHAUSTIVE requires exact two artifact kinds")
        require(
            by_kind["rule-manifest"]["locator"]
            == "rule-exhaustiveness-registry://RULE_EXHAUSTIVE/rule-manifest",
            "rule-manifest locator does not bind rule registry",
        )
        require(
            by_kind["rule-manifest"]["digest"] == manifest_bundle["rule_manifest_bundle_sha256"],
            "rule-manifest digest does not bind manifest bundle",
        )
        require(
            by_kind["rule-exhaustiveness-proof"]["locator"]
            == "rule-exhaustiveness-registry://RULE_EXHAUSTIVE/rule-exhaustiveness-proof",
            "rule-exhaustiveness-proof locator does not bind rule registry",
        )
        require(
            by_kind["rule-exhaustiveness-proof"]["digest"]
            == proof_bundle["rule_exhaustiveness_proof_bundle_sha256"],
            "rule-exhaustiveness-proof digest does not bind proof bundle",
        )

    target_by_id = {
        record["target_id"]: record for record in atomic_exact["target_result_records"]
    }
    t02_complete = int(target_by_id["T02_RULE_EXHAUSTIVENESS"]["effective_target_complete"])
    require(t02_complete == rule_ready,
            "T02_RULE_EXHAUSTIVENESS completion disagrees with exact rule proof bank")

    status_counts = Counter(record["status"] for record in records)
    kind_counts = Counter(record["record_kind"] for record in records)
    open_record_ids = [record["record_id"] for record in records if record["status"] == "open"]
    application_count = sum(
        record["record_kind"] == "global-parent-application" for record in records
    )
    claims = {
        "rule_exhaustiveness_records": len(records),
        "proved_rule_exhaustiveness_records": status_counts["proved"],
        "open_rule_exhaustiveness_records": status_counts["open"],
        "global_parent_applications": application_count,
        "rule_exhaustiveness_artifacts": len(artifacts),
        "source_statement_truth_ready": source_ready,
        "rule_exhaustiveness_ready": rule_ready,
        "exact_global_parent_to_operation_slot_binding": 1,
        "exact_rule_record_artifact_coverage": 1,
        "exact_rule_artifact_support": 1,
        "rule_obligation_synchronized": 1,
        "t02_rule_exhaustiveness_synchronized": 1,
        "all_n_proved_by_checker": 0,
        "open_rule_record_ids": open_record_ids,
        "record_kind_distribution": [
            [kind, kind_counts[kind]] for kind in sorted(kind_counts)
        ],
        "source_truth_frontier_execution_sha256": source_frontier_certificate["certificate_sha256"],
        "source_statement_truth_registry_sha256": source_certificate["certificate_sha256"],
        "rule_source_provenance_sha256": provenance_certificate["certificate_sha256"],
        "clause_manifest_sha256": manifest["manifest_sha256"],
        "expected_slot_registry_sha256": slot_registry["registry_sha256"],
        "global_family_skeleton_sha256": skeleton_certificate["certificate_sha256"],
        "obligation_artifact_registry_sha256": obligation_certificate["certificate_sha256"],
        "atomic_frontier_execution_sha256": atomic_certificate["certificate_sha256"],
        "rule_manifest_bundle_sha256": manifest_bundle["rule_manifest_bundle_sha256"],
        "rule_exhaustiveness_proof_bundle_sha256": proof_bundle[
            "rule_exhaustiveness_proof_bundle_sha256"
        ],
        "rule_exhaustiveness_records_sha256": catalogue.canonical_digest(records),
        "rule_exhaustiveness_artifacts_sha256": catalogue.canonical_digest(artifacts),
    }
    return {
        "rule_exhaustiveness_records": records,
        "rule_exhaustiveness_artifacts": artifacts,
        "rule_manifest_bundle": manifest_bundle,
        "rule_exhaustiveness_proof_bundle": proof_bundle,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in (
        "rule_exhaustiveness_records",
        "rule_exhaustiveness_artifacts",
        "rule_manifest_bundle",
        "rule_exhaustiveness_proof_bundle",
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
        "records": claims["rule_exhaustiveness_records"],
        "proved": claims["proved_rule_exhaustiveness_records"],
        "open": claims["open_rule_exhaustiveness_records"],
        "applications": claims["global_parent_applications"],
        "ready": claims["rule_exhaustiveness_ready"],
        "all_n": claims["all_n_proved_by_checker"],
    }


def build_certificate(
    source_frontier_certificate: dict[str, Any],
    records: list[dict[str, Any]],
    artifacts: list[dict[str, Any]],
) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "source_truth_frontier_execution_certificate": source_frontier_certificate,
        "rule_exhaustiveness_records": records,
        "rule_exhaustiveness_artifacts": artifacts,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: check_prime_power_rule_exhaustiveness_frontier.py certificate.json"
        )
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
