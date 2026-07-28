#!/usr/bin/env python3
"""Validate and synchronize the exact T03 slot/candidate population bank.

The T02 rule-exhaustiveness frontier fixes an independently expected operation-slot registry and
binds every global recurrence parent to one admitted slot. The older slot population audit checks
only slot IDs, hosts, fibre IDs and an unattached source digest. This checker makes the next atomic
frontier exact: every expected slot has one open, data-populated or proved record; every non-open
record carries the complete literal population payload; and every proved record has one sealed
slot-specific proof artifact with exact T02 case/clause/application support.

This is documentary population infrastructure. It does not verify the mathematical truth of any
payload or proof artifact and permanently reports ``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_all_n_implication_closure as closure
import check_prime_power_atomic_frontier_execution as atomic
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_obligation_artifact_registry as obligation_artifacts
import check_prime_power_operation_slot_registry as slot_registry
import check_prime_power_rule_exhaustiveness_frontier as rule_frontier


class SlotCandidatePopulationFrontierError(ValueError):
    """Raised when the exact T03 population bank is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SlotCandidatePopulationFrontierError(message)


POPULATION_DATA_KEYS = (
    "points",
    "removals",
    "survivor_background",
    "owner_fate_witnesses",
    "response_family",
    "feasibility_signatures",
    "selector_data",
    "labelled_vectors",
    "routed_credits",
    "row_loads",
    "transitions",
)
LIST_DATA_KEYS = tuple(key for key in POPULATION_DATA_KEYS if key != "selector_data")
REQUIRED_ARTIFACT_KIND = "slot-candidate-population-proof"


def canonical_json_value(value: Any, path: str) -> Any:
    require(
        value is None or isinstance(value, (bool, int, str, list, dict)),
        f"{path}: non-JSON value",
    )
    if isinstance(value, list):
        return [canonical_json_value(item, f"{path}[]") for item in value]
    if isinstance(value, dict):
        require(all(isinstance(key, str) for key in value), f"{path}: non-string key")
        return {key: canonical_json_value(value[key], f"{path}.{key}") for key in value}
    return value


def population_record_id(slot_id: str) -> str:
    return f"population::{slot_id}"


def exact_status_record(record: dict[str, Any], slot: dict[str, Any], path: str) -> dict[str, Any]:
    slot_id = slot["slot_id"]
    record_id = population_record_id(slot_id)
    require(record.get("record_id") == record_id, f"{path}.record_id: mismatch")
    require(record.get("slot_id") == slot_id, f"{path}.slot_id: mismatch")
    require(record.get("slot_sha256") == slot["slot_sha256"], f"{path}.slot_sha256: mismatch")
    status = record.get("status")
    locator = record.get("population_locator")
    digest = record.get("population_digest")
    note = record.get("note")
    require(status in {"open", "populated", "proved"}, f"{path}.status: expected open/populated/proved")
    require(isinstance(note, str) and note, f"{path}.note: required")
    if status == "open":
        require(locator is None, f"{path}.population_locator: open record requires null")
        require(digest is None, f"{path}.population_digest: open record requires null")
    elif status == "populated":
        require(
            locator == f"slot-candidate-population-data://{slot_id}",
            f"{path}.population_locator: canonical data URI required",
        )
        require(isinstance(digest, str) and digest, f"{path}.population_digest: required")
    else:
        require(
            locator == f"slot-candidate-population-registry://{slot_id}",
            f"{path}.population_locator: canonical registry URI required",
        )
        require(isinstance(digest, str) and digest, f"{path}.population_digest: required")
    output = {
        "record_id": record_id,
        "slot_id": slot_id,
        "slot_sha256": slot["slot_sha256"],
        "status": status,
        "population_locator": locator,
        "population_digest": digest,
        "note": note,
    }
    output["slot_population_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_population_payload(
    payload: dict[str, Any],
    slot: dict[str, Any],
    path: str,
) -> dict[str, Any]:
    slot_id = payload.get("slot_id")
    host_id = payload.get("host_id")
    fibre_id = payload.get("fibre_id")
    population_data = payload.get("population_data")
    source_sha256 = payload.get("source_sha256")
    require(slot_id == slot["slot_id"], f"{path}.slot_id: mismatch")
    require(host_id == slot["expected_host_id"], f"{path}.host_id: expected-host mismatch")
    require(isinstance(population_data, dict), f"{path}.population_data: expected object")
    require(
        tuple(population_data) == POPULATION_DATA_KEYS,
        f"{path}.population_data: exact ordered population keys required",
    )
    canonical_data = {
        key: canonical_json_value(population_data[key], f"{path}.population_data.{key}")
        for key in POPULATION_DATA_KEYS
    }
    for key in LIST_DATA_KEYS:
        require(isinstance(canonical_data[key], list), f"{path}.population_data.{key}: expected list")
    require(
        isinstance(canonical_data["selector_data"], dict),
        f"{path}.population_data.selector_data: expected object",
    )
    computed_source = catalogue.canonical_digest(canonical_data)
    require(source_sha256 == computed_source, f"{path}.source_sha256: population-data mismatch")
    require(
        fibre_id == f"{host_id}:{computed_source[:16]}",
        f"{path}.fibre_id: canonical host/source fibre ID required",
    )
    output = {
        "slot_id": slot_id,
        "host_id": host_id,
        "fibre_id": fibre_id,
        "population_data": canonical_data,
        "source_sha256": source_sha256,
    }
    output["slot_population_payload_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_population_artifact(
    artifact: dict[str, Any],
    *,
    slot: dict[str, Any],
    payload: dict[str, Any],
    expected_rule_support_ids: list[str],
    path: str,
) -> dict[str, Any]:
    slot_id = artifact.get("slot_id")
    artifact_id = artifact.get("artifact_id")
    artifact_kind = artifact.get("artifact_kind")
    payload_sha256 = artifact.get("slot_population_payload_sha256")
    proof_locator = artifact.get("proof_locator")
    proof_digest = artifact.get("proof_digest")
    proof_statement = artifact.get("proof_statement")
    rule_support = artifact.get("support_rule_exhaustiveness_artifact_ids")
    evidence = artifact.get("evidence")
    require(slot_id == slot["slot_id"], f"{path}.slot_id: mismatch")
    for name, value in (
        ("artifact_id", artifact_id),
        ("artifact_kind", artifact_kind),
        ("proof_locator", proof_locator),
        ("proof_digest", proof_digest),
        ("proof_statement", proof_statement),
        ("evidence", evidence),
    ):
        require(isinstance(value, str) and value, f"{path}.{name}: required")
    require(artifact_kind == REQUIRED_ARTIFACT_KIND, f"{path}.artifact_kind: wrong kind")
    require(
        payload_sha256 == payload["slot_population_payload_sha256"],
        f"{path}.slot_population_payload_sha256: payload mismatch",
    )
    require(
        rule_support == expected_rule_support_ids,
        f"{path}.support_rule_exhaustiveness_artifact_ids: exact support required",
    )
    require(isinstance(rule_support, list), f"{path}.support_rule_exhaustiveness_artifact_ids: list required")
    require(rule_support == sorted(rule_support), f"{path}.support_rule_exhaustiveness_artifact_ids: sorted")
    require(len(rule_support) == len(set(rule_support)), f"{path}: duplicate rule support")
    require(artifact_id not in rule_support, f"{path}: artifact cannot support itself")
    output = {
        "slot_id": slot_id,
        "artifact_id": artifact_id,
        "artifact_kind": artifact_kind,
        "slot_population_payload_sha256": payload_sha256,
        "proof_locator": proof_locator,
        "proof_digest": proof_digest,
        "proof_statement": proof_statement,
        "support_rule_exhaustiveness_artifact_ids": list(rule_support),
        "evidence": evidence,
    }
    output["slot_population_artifact_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    rule_certificate = certificate.get("rule_exhaustiveness_frontier_certificate")
    raw_records = certificate.get("slot_population_records")
    raw_payloads = certificate.get("slot_population_payloads")
    raw_artifacts = certificate.get("slot_population_artifacts")
    require(
        isinstance(rule_certificate, dict),
        "rule_exhaustiveness_frontier_certificate: expected object",
    )
    require(isinstance(raw_records, list), "slot_population_records: expected list")
    require(isinstance(raw_payloads, list), "slot_population_payloads: expected list")
    require(isinstance(raw_artifacts, list), "slot_population_artifacts: expected list")

    rule_frontier.validate_certificate(rule_certificate)
    rule_exact = rule_frontier.exact_certificate(rule_certificate)
    source_frontier_certificate = rule_certificate["source_truth_frontier_execution_certificate"]
    source_certificate = source_frontier_certificate["source_statement_truth_registry_certificate"]
    provenance_certificate = source_certificate["rule_source_provenance_certificate"]
    manifest = provenance_certificate["clause_manifest"]
    expected_registry = manifest["expected_slot_registry"]
    slot_registry.validate_registry(expected_registry)
    slots = expected_registry["slots"]
    slot_by_id = {slot["slot_id"]: slot for slot in slots}

    obligation_certificate = source_certificate["obligation_artifact_registry_certificate"]
    obligation_artifacts.validate_certificate(obligation_certificate)
    obligation_exact = obligation_artifacts.exact_certificate(obligation_certificate)
    closure_certificate = obligation_certificate["all_n_implication_closure_certificate"]
    closure_exact = closure.exact_certificate(closure_certificate)

    current_certificate = source_frontier_certificate["current_frontier_execution_certificate"]
    atomic_certificate = current_certificate["atomic_frontier_execution_certificate"]
    atomic_exact = atomic.exact_certificate(atomic_certificate)

    require(len(raw_records) == len(slots), "slot_population_records: exact slot cardinality required")
    require(
        [record.get("slot_id") for record in raw_records] == [slot["slot_id"] for slot in slots],
        "slot_population_records: exact canonical slot order required",
    )
    records = [
        exact_status_record(record, slot, f"slot_population_records[{index}]")
        for index, (record, slot) in enumerate(zip(raw_records, slots))
    ]
    require(raw_records == records, "slot_population_records: canonical records/digests required")
    record_by_slot = {record["slot_id"]: record for record in records}

    payload_by_slot_raw: dict[str, list[dict[str, Any]]] = {slot_id: [] for slot_id in slot_by_id}
    for payload in raw_payloads:
        require(isinstance(payload, dict), "slot_population_payloads: expected objects")
        slot_id = payload.get("slot_id")
        require(slot_id in payload_by_slot_raw, f"slot_population_payloads: unknown slot {slot_id}")
        payload_by_slot_raw[slot_id].append(payload)

    rule_artifact_by_record = {
        artifact["record_id"]: artifact["artifact_id"]
        for artifact in rule_exact["rule_exhaustiveness_artifacts"]
    }
    applications_by_slot: dict[str, list[str]] = {slot_id: [] for slot_id in slot_by_id}
    for record in rule_exact["rule_exhaustiveness_records"]:
        if record["record_kind"] != "global-parent-application":
            continue
        slot_id = record["identity"]["operation_slot_id"]
        require(slot_id in applications_by_slot, f"T02 application uses unknown slot {slot_id}")
        applications_by_slot[slot_id].append(record["record_id"])

    artifact_by_slot_raw: dict[str, list[dict[str, Any]]] = {slot_id: [] for slot_id in slot_by_id}
    for artifact in raw_artifacts:
        require(isinstance(artifact, dict), "slot_population_artifacts: expected objects")
        slot_id = artifact.get("slot_id")
        require(slot_id in artifact_by_slot_raw, f"slot_population_artifacts: unknown slot {slot_id}")
        artifact_by_slot_raw[slot_id].append(artifact)

    payloads: list[dict[str, Any]] = []
    artifacts: list[dict[str, Any]] = []
    bundle_records: list[dict[str, Any]] = []
    for slot in slots:
        slot_id = slot["slot_id"]
        record = record_by_slot[slot_id]
        raw_payload_group = payload_by_slot_raw[slot_id]
        raw_artifact_group = artifact_by_slot_raw[slot_id]
        status = record["status"]
        if status == "open":
            require(not raw_payload_group, f"slot {slot_id}: open record cannot contain payload")
            require(not raw_artifact_group, f"slot {slot_id}: open record cannot contain artifact")
            payload_list: list[dict[str, Any]] = []
            artifact_list: list[dict[str, Any]] = []
        else:
            require(len(raw_payload_group) == 1, f"slot {slot_id}: exactly one population payload required")
            payload = exact_population_payload(
                raw_payload_group[0],
                slot,
                f"slot_population_payload[{slot_id}]",
            )
            payloads.append(payload)
            payload_list = [payload]
            if status == "populated":
                require(
                    not raw_artifact_group,
                    f"slot {slot_id}: data-populated record cannot contain proof artifact",
                )
                artifact_list = []
                data_bundle = {
                    "slot_id": slot_id,
                    "slot_sha256": slot["slot_sha256"],
                    "slot_population_payload_sha256": payload["slot_population_payload_sha256"],
                }
                data_bundle["slot_population_data_bundle_sha256"] = catalogue.canonical_digest(data_bundle)
                require(
                    record["population_digest"] == data_bundle["slot_population_data_bundle_sha256"],
                    f"slot {slot_id}: populated digest does not bind payload",
                )
            else:
                require(len(raw_artifact_group) == 1, f"slot {slot_id}: exactly one proof artifact required")
                key = slot["operation_key"]
                dependency_record_ids = [
                    f"case::{key.get('case_id')}",
                    f"clause::{key.get('clause_id')}",
                    *sorted(applications_by_slot[slot_id]),
                ]
                require(
                    all(dep in rule_artifact_by_record for dep in dependency_record_ids),
                    f"slot {slot_id}: T02 dependencies must be proved before slot proof",
                )
                expected_rule_support = sorted(
                    rule_artifact_by_record[dep] for dep in dependency_record_ids
                )
                artifact = exact_population_artifact(
                    raw_artifact_group[0],
                    slot=slot,
                    payload=payload,
                    expected_rule_support_ids=expected_rule_support,
                    path=f"slot_population_artifact[{slot_id}]",
                )
                artifacts.append(artifact)
                artifact_list = [artifact]
                full_bundle = {
                    "slot_id": slot_id,
                    "slot_sha256": slot["slot_sha256"],
                    "slot_population_payload_sha256": payload["slot_population_payload_sha256"],
                    "slot_population_artifact_sha256": artifact["slot_population_artifact_sha256"],
                    "support_rule_exhaustiveness_artifact_ids": expected_rule_support,
                }
                full_bundle["slot_population_proof_bundle_sha256"] = catalogue.canonical_digest(full_bundle)
                require(
                    record["population_digest"] == full_bundle["slot_population_proof_bundle_sha256"],
                    f"slot {slot_id}: proved digest does not bind payload/artifact bundle",
                )

        bundle = {
            "slot_id": slot_id,
            "slot_sha256": slot["slot_sha256"],
            "status": status,
            "payload_sha256": catalogue.canonical_digest(payload_list),
            "artifact_sha256": catalogue.canonical_digest(artifact_list),
        }
        bundle["slot_population_bundle_sha256"] = catalogue.canonical_digest(bundle)
        bundle_records.append(bundle)

    require(raw_payloads == payloads, "slot_population_payloads: canonical slot order/content required")
    require(raw_artifacts == artifacts, "slot_population_artifacts: canonical slot order/content required")
    fibre_ids = [payload["fibre_id"] for payload in payloads]
    require(len(fibre_ids) == len(set(fibre_ids)), "slot_population_payloads: duplicate fibre_id")
    artifact_ids = [artifact["artifact_id"] for artifact in artifacts]
    require(len(artifact_ids) == len(set(artifact_ids)), "slot_population_artifacts: duplicate artifact_id")

    status_counts = Counter(record["status"] for record in records)
    rule_ready = int(rule_exact["claims"]["rule_exhaustiveness_ready"])
    complete_population_data = int(status_counts["open"] == 0)
    all_slots_proved = int(status_counts["proved"] == len(slots))
    population_ready = int(rule_ready and all_slots_proved and len(artifacts) == len(slots))

    population_proof_bundle = {
        "expected_slot_registry_sha256": expected_registry["registry_sha256"],
        "rule_exhaustiveness_records_sha256": rule_exact["claims"]["rule_exhaustiveness_records_sha256"],
        "rule_exhaustiveness_artifacts_sha256": rule_exact["claims"]["rule_exhaustiveness_artifacts_sha256"],
        "slot_population_records_sha256": catalogue.canonical_digest(records),
        "slot_population_payloads_sha256": catalogue.canonical_digest(payloads),
        "slot_population_artifacts_sha256": catalogue.canonical_digest(artifacts),
        "slot_population_bundles_sha256": catalogue.canonical_digest(bundle_records),
    }
    population_proof_bundle["slot_candidate_population_proof_bundle_sha256"] = catalogue.canonical_digest(
        population_proof_bundle
    )

    closure_by_id = {
        record["obligation_id"]: record for record in closure_exact["obligation_closure_records"]
    }
    population_closure = closure_by_id["SLOT_AND_CANDIDATE_POPULATION"]
    require(
        int(population_closure["closed"]) == population_ready,
        "SLOT_AND_CANDIDATE_POPULATION closure disagrees with exact slot population bank",
    )
    population_obligation_artifacts = [
        artifact for artifact in obligation_exact["proof_artifacts"]
        if artifact["obligation_id"] == "SLOT_AND_CANDIDATE_POPULATION"
    ]
    require(
        len(population_obligation_artifacts) == population_ready,
        "SLOT_AND_CANDIDATE_POPULATION artifact presence disagrees with readiness",
    )
    if population_ready:
        obligation_artifact = population_obligation_artifacts[0]
        require(
            obligation_artifact["artifact_kind"] == "population-certificate",
            "SLOT_AND_CANDIDATE_POPULATION requires population-certificate",
        )
        require(
            obligation_artifact["locator"]
            == "slot-candidate-population-registry://SLOT_AND_CANDIDATE_POPULATION",
            "population-certificate locator does not bind T03 registry",
        )
        require(
            obligation_artifact["digest"]
            == population_proof_bundle["slot_candidate_population_proof_bundle_sha256"],
            "population-certificate digest does not bind exact T03 bank",
        )

    target_by_id = {
        record["target_id"]: record for record in atomic_exact["target_result_records"]
    }
    t03_complete = int(target_by_id["T03_SLOT_CANDIDATE_POPULATION"]["effective_target_complete"])
    require(
        t03_complete == population_ready,
        "T03_SLOT_CANDIDATE_POPULATION completion disagrees with exact slot population bank",
    )

    open_slot_ids = [record["slot_id"] for record in records if record["status"] == "open"]
    populated_slot_ids = [record["slot_id"] for record in records if record["status"] == "populated"]
    claims = {
        "expected_slots": len(slots),
        "open_slots": status_counts["open"],
        "data_populated_slots": status_counts["populated"],
        "proved_slots": status_counts["proved"],
        "population_payloads": len(payloads),
        "population_artifacts": len(artifacts),
        "complete_population_data": complete_population_data,
        "rule_exhaustiveness_ready": rule_ready,
        "slot_candidate_population_ready": population_ready,
        "exact_expected_slot_coverage": 1,
        "exact_literal_population_payload_binding": 1,
        "exact_fibre_source_hash_binding": 1,
        "exact_t02_rule_artifact_support": 1,
        "population_obligation_synchronized": 1,
        "t03_slot_candidate_population_synchronized": 1,
        "all_n_proved_by_checker": 0,
        "open_slot_ids": open_slot_ids,
        "data_populated_slot_ids": populated_slot_ids,
        "expected_slot_registry_sha256": expected_registry["registry_sha256"],
        "rule_exhaustiveness_frontier_sha256": rule_certificate["certificate_sha256"],
        "obligation_artifact_registry_sha256": obligation_certificate["certificate_sha256"],
        "atomic_frontier_execution_sha256": atomic_certificate["certificate_sha256"],
        "slot_population_records_sha256": catalogue.canonical_digest(records),
        "slot_population_payloads_sha256": catalogue.canonical_digest(payloads),
        "slot_population_artifacts_sha256": catalogue.canonical_digest(artifacts),
        "slot_population_bundles_sha256": catalogue.canonical_digest(bundle_records),
        "slot_candidate_population_proof_bundle_sha256": population_proof_bundle[
            "slot_candidate_population_proof_bundle_sha256"
        ],
    }
    return {
        "slot_population_records": records,
        "slot_population_payloads": payloads,
        "slot_population_artifacts": artifacts,
        "slot_population_bundle_records": bundle_records,
        "slot_candidate_population_proof_bundle": population_proof_bundle,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in (
        "slot_population_records",
        "slot_population_payloads",
        "slot_population_artifacts",
        "slot_population_bundle_records",
        "slot_candidate_population_proof_bundle",
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
        "slots": claims["expected_slots"],
        "open": claims["open_slots"],
        "populated": claims["data_populated_slots"],
        "proved": claims["proved_slots"],
        "ready": claims["slot_candidate_population_ready"],
        "all_n": claims["all_n_proved_by_checker"],
    }


def build_certificate(
    rule_certificate: dict[str, Any],
    records: list[dict[str, Any]],
    payloads: list[dict[str, Any]],
    artifacts: list[dict[str, Any]],
) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "rule_exhaustiveness_frontier_certificate": rule_certificate,
        "slot_population_records": records,
        "slot_population_payloads": payloads,
        "slot_population_artifacts": artifacts,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: check_prime_power_slot_candidate_population_frontier.py certificate.json"
        )
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
