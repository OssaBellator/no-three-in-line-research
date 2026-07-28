#!/usr/bin/env python3
"""Validate and synchronize the exact T04 recurrent-block/interface population bank.

T03 fixes one literal population payload for every expected operation slot. The global recurrence
skeleton separately derives the expected recurrent-block and return/interface/off-diagonal row IDs.
This checker joins those two independent surfaces without importing the later semantic quotient
certificates, which would create a dependency cycle.

Every expected block or interface row has one open, populated or proved record. A populated unit
carries literal assembly data bound to the exact T03 source slots. A proved unit additionally carries
one sealed population artifact with exact T03 slot-artifact support. The aggregate noncircular bank
digest is bound by the T04 atomic target artifact's external proof digest.

This is documentary population infrastructure. It does not verify mathematical truth and permanently
reports ``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_atomic_frontier_execution as atomic
import check_prime_power_atomic_target_artifact_registry as target_artifacts
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_rule_exhaustiveness_frontier as rule_frontier
import check_prime_power_slot_candidate_population_frontier as slot_population


class BlockInterfacePopulationFrontierError(ValueError):
    """Raised when the exact T04 population bank is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise BlockInterfacePopulationFrontierError(message)


BLOCK_DATA_KEYS = (
    "local_states",
    "recurrent_rows",
    "return_routes",
    "interface_attachments",
    "source_clause_bindings",
)
INTERFACE_DATA_KEYS = (
    "target_states",
    "route_data",
    "transition_data",
    "source_clause_binding",
)
ARTIFACT_KINDS = {
    "recurrent-block": "recurrent-block-population-proof",
    "interface-row": "interface-row-population-proof",
}


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


def expected_units(
    skeleton: dict[str, Any],
    rule_exact: dict[str, Any],
) -> list[dict[str, Any]]:
    application_by_parent = {
        record["identity"]["parent_global_state_id"]: record
        for record in rule_exact["rule_exhaustiveness_records"]
        if record["record_kind"] == "global-parent-application"
    }
    block_parents: dict[str, list[dict[str, Any]]] = {}
    interface_units: list[dict[str, Any]] = []
    for clause in skeleton["parent_clauses"]:
        parent = clause["parent_global_state_id"]
        require(parent in application_by_parent, f"skeleton parent {parent}: missing T02 application")
        application = application_by_parent[parent]
        identity = application["identity"]
        binding = {
            "parent_global_state_id": parent,
            "row_kind": clause["row_kind"],
            "source_case_id": identity["source_case_id"],
            "source_clause_id": identity["source_clause_id"],
            "operation_slot_id": identity["operation_slot_id"],
        }
        binding["parent_binding_sha256"] = catalogue.canonical_digest(binding)
        if clause["row_kind"] == "recurrent":
            block_id = clause["expected_block_id"]
            block_parents.setdefault(block_id, []).append(binding)
        else:
            row_id = clause["expected_interface_row_id"]
            unit = {
                "unit_id": f"interface::{row_id}",
                "unit_kind": "interface-row",
                "object_id": row_id,
                "row_kind": clause["row_kind"],
                "parent_bindings": [binding],
            }
            unit["unit_identity_sha256"] = catalogue.canonical_digest(unit)
            interface_units.append(unit)

    units: list[dict[str, Any]] = []
    for block_id in sorted(block_parents):
        bindings = sorted(
            block_parents[block_id],
            key=lambda record: record["parent_global_state_id"],
        )
        unit = {
            "unit_id": f"block::{block_id}",
            "unit_kind": "recurrent-block",
            "object_id": block_id,
            "row_kind": "recurrent",
            "parent_bindings": bindings,
        }
        unit["unit_identity_sha256"] = catalogue.canonical_digest(unit)
        units.append(unit)
    units.extend(sorted(interface_units, key=lambda record: record["unit_id"]))
    require(
        units == sorted(units, key=lambda record: record["unit_id"]),
        "expected units: canonical unit order failure",
    )
    return units


def exact_status_record(record: dict[str, Any], unit: dict[str, Any], path: str) -> dict[str, Any]:
    unit_id = unit["unit_id"]
    require(record.get("unit_id") == unit_id, f"{path}.unit_id: mismatch")
    require(record.get("unit_kind") == unit["unit_kind"], f"{path}.unit_kind: mismatch")
    require(
        record.get("unit_identity_sha256") == unit["unit_identity_sha256"],
        f"{path}.unit_identity_sha256: mismatch",
    )
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
            locator == f"block-interface-population-data://{unit_id}",
            f"{path}.population_locator: canonical data URI required",
        )
        require(isinstance(digest, str) and digest, f"{path}.population_digest: required")
    else:
        require(
            locator == f"block-interface-population-registry://{unit_id}",
            f"{path}.population_locator: canonical registry URI required",
        )
        require(isinstance(digest, str) and digest, f"{path}.population_digest: required")
    output = {
        "unit_id": unit_id,
        "unit_kind": unit["unit_kind"],
        "unit_identity_sha256": unit["unit_identity_sha256"],
        "status": status,
        "population_locator": locator,
        "population_digest": digest,
        "note": note,
    }
    output["block_interface_population_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_source_slot_bindings(
    unit: dict[str, Any],
    slot_payload_by_id: dict[str, dict[str, Any]],
    path: str,
) -> list[dict[str, Any]]:
    bindings = []
    for parent_binding in unit["parent_bindings"]:
        slot_id = parent_binding["operation_slot_id"]
        require(slot_id in slot_payload_by_id, f"{path}: source T03 slot {slot_id} is not populated")
        payload = slot_payload_by_id[slot_id]
        binding = {
            "parent_global_state_id": parent_binding["parent_global_state_id"],
            "operation_slot_id": slot_id,
            "slot_population_payload_sha256": payload["slot_population_payload_sha256"],
            "fibre_id": payload["fibre_id"],
            "source_sha256": payload["source_sha256"],
        }
        binding["source_slot_binding_sha256"] = catalogue.canonical_digest(binding)
        bindings.append(binding)
    return bindings


def exact_payload(
    payload: dict[str, Any],
    *,
    unit: dict[str, Any],
    slot_payload_by_id: dict[str, dict[str, Any]],
    path: str,
) -> dict[str, Any]:
    require(payload.get("unit_id") == unit["unit_id"], f"{path}.unit_id: mismatch")
    require(payload.get("unit_kind") == unit["unit_kind"], f"{path}.unit_kind: mismatch")
    require(
        payload.get("unit_identity_sha256") == unit["unit_identity_sha256"],
        f"{path}.unit_identity_sha256: mismatch",
    )
    source_bindings = payload.get("source_slot_bindings")
    population_data = payload.get("population_data")
    expected_source_bindings = exact_source_slot_bindings(unit, slot_payload_by_id, path)
    require(
        source_bindings == expected_source_bindings,
        f"{path}.source_slot_bindings: exact T03 source binding required",
    )
    require(isinstance(population_data, dict), f"{path}.population_data: expected object")
    keys = BLOCK_DATA_KEYS if unit["unit_kind"] == "recurrent-block" else INTERFACE_DATA_KEYS
    require(tuple(population_data) == keys, f"{path}.population_data: exact ordered keys required")
    canonical_data = {
        key: canonical_json_value(population_data[key], f"{path}.population_data.{key}")
        for key in keys
    }
    if unit["unit_kind"] == "recurrent-block":
        for key in BLOCK_DATA_KEYS:
            require(isinstance(canonical_data[key], list), f"{path}.population_data.{key}: expected list")
        require(canonical_data["recurrent_rows"], f"{path}.population_data.recurrent_rows: nonempty")
        require(
            canonical_data["source_clause_bindings"],
            f"{path}.population_data.source_clause_bindings: nonempty",
        )
    else:
        for key in ("target_states", "route_data", "transition_data"):
            require(isinstance(canonical_data[key], list), f"{path}.population_data.{key}: expected list")
        require(
            isinstance(canonical_data["source_clause_binding"], dict),
            f"{path}.population_data.source_clause_binding: expected object",
        )
    output = {
        "unit_id": unit["unit_id"],
        "unit_kind": unit["unit_kind"],
        "unit_identity_sha256": unit["unit_identity_sha256"],
        "source_slot_bindings": expected_source_bindings,
        "population_data": canonical_data,
    }
    output["block_interface_population_payload_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_artifact(
    artifact: dict[str, Any],
    *,
    unit: dict[str, Any],
    payload: dict[str, Any],
    expected_t03_support_ids: list[str],
    path: str,
) -> dict[str, Any]:
    values = {
        key: artifact.get(key)
        for key in (
            "artifact_id",
            "artifact_kind",
            "proof_locator",
            "proof_digest",
            "proof_statement",
            "evidence",
        )
    }
    require(artifact.get("unit_id") == unit["unit_id"], f"{path}.unit_id: mismatch")
    require(
        artifact.get("block_interface_population_payload_sha256")
        == payload["block_interface_population_payload_sha256"],
        f"{path}.block_interface_population_payload_sha256: mismatch",
    )
    support = artifact.get("support_t03_population_artifact_ids")
    for name, value in values.items():
        require(isinstance(value, str) and value, f"{path}.{name}: required")
    require(
        values["artifact_kind"] == ARTIFACT_KINDS[unit["unit_kind"]],
        f"{path}.artifact_kind: wrong kind",
    )
    require(
        support == expected_t03_support_ids,
        f"{path}.support_t03_population_artifact_ids: exact support required",
    )
    require(isinstance(support, list), f"{path}.support_t03_population_artifact_ids: list required")
    require(support == sorted(support), f"{path}.support_t03_population_artifact_ids: sorted")
    require(len(support) == len(set(support)), f"{path}: duplicate T03 support")
    require(values["artifact_id"] not in support, f"{path}: artifact cannot support itself")
    output = {
        "unit_id": unit["unit_id"],
        "artifact_id": values["artifact_id"],
        "artifact_kind": values["artifact_kind"],
        "block_interface_population_payload_sha256": payload[
            "block_interface_population_payload_sha256"
        ],
        "proof_locator": values["proof_locator"],
        "proof_digest": values["proof_digest"],
        "proof_statement": values["proof_statement"],
        "support_t03_population_artifact_ids": list(support),
        "evidence": values["evidence"],
    }
    output["block_interface_population_artifact_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    t03_certificate = certificate.get("slot_candidate_population_frontier_certificate")
    target_registry_certificate = certificate.get("atomic_target_artifact_registry_certificate")
    raw_records = certificate.get("block_interface_population_records")
    raw_payloads = certificate.get("block_interface_population_payloads")
    raw_artifacts = certificate.get("block_interface_population_artifacts")
    require(isinstance(t03_certificate, dict),
            "slot_candidate_population_frontier_certificate: expected object")
    require(isinstance(target_registry_certificate, dict),
            "atomic_target_artifact_registry_certificate: expected object")
    require(isinstance(raw_records, list), "block_interface_population_records: expected list")
    require(isinstance(raw_payloads, list), "block_interface_population_payloads: expected list")
    require(isinstance(raw_artifacts, list), "block_interface_population_artifacts: expected list")

    slot_population.validate_certificate(t03_certificate)
    t03_exact = slot_population.exact_certificate(t03_certificate)
    target_artifacts.validate_certificate(target_registry_certificate)
    target_exact = target_artifacts.exact_certificate(target_registry_certificate)

    rule_certificate = t03_certificate["rule_exhaustiveness_frontier_certificate"]
    rule_frontier.validate_certificate(rule_certificate)
    rule_exact = rule_frontier.exact_certificate(rule_certificate)
    source_frontier = rule_certificate["source_truth_frontier_execution_certificate"]
    source_certificate = source_frontier["source_statement_truth_registry_certificate"]
    obligation_certificate = source_certificate["obligation_artifact_registry_certificate"]
    closure_certificate = obligation_certificate["all_n_implication_closure_certificate"]
    skeleton_certificate = closure_certificate["global_family_skeleton_certificate"]
    skeleton = skeleton_certificate["recurrence_skeleton"]

    t03_current = source_frontier["current_frontier_execution_certificate"]
    target_current = target_registry_certificate["current_frontier_execution_certificate"]
    require(
        target_current["certificate_sha256"] == t03_current["certificate_sha256"],
        "T03 and atomic-target registries use different current-frontier certificates",
    )
    atomic_certificate = t03_current["atomic_frontier_execution_certificate"]
    atomic.validate_certificate(atomic_certificate)
    atomic_exact = atomic.exact_certificate(atomic_certificate)

    units = expected_units(skeleton, rule_exact)
    require(
        len(raw_records) == len(units),
        "block_interface_population_records: exact unit cardinality required",
    )
    require(
        [record.get("unit_id") for record in raw_records] == [unit["unit_id"] for unit in units],
        "block_interface_population_records: exact canonical unit order required",
    )
    records = [
        exact_status_record(record, unit, f"block_interface_population_records[{index}]")
        for index, (record, unit) in enumerate(zip(raw_records, units))
    ]
    require(
        raw_records == records,
        "block_interface_population_records: canonical records/digests required",
    )
    record_by_unit = {record["unit_id"]: record for record in records}

    t03_payload_by_slot = {
        payload["slot_id"]: payload for payload in t03_exact["slot_population_payloads"]
    }
    t03_artifact_by_slot = {
        artifact["slot_id"]: artifact["artifact_id"]
        for artifact in t03_exact["slot_population_artifacts"]
    }

    payload_groups: dict[str, list[dict[str, Any]]] = {unit["unit_id"]: [] for unit in units}
    for payload in raw_payloads:
        require(isinstance(payload, dict), "block_interface_population_payloads: expected objects")
        unit_id = payload.get("unit_id")
        require(unit_id in payload_groups, f"block_interface_population_payloads: unknown unit {unit_id}")
        payload_groups[unit_id].append(payload)

    artifact_groups: dict[str, list[dict[str, Any]]] = {unit["unit_id"]: [] for unit in units}
    for artifact in raw_artifacts:
        require(isinstance(artifact, dict), "block_interface_population_artifacts: expected objects")
        unit_id = artifact.get("unit_id")
        require(unit_id in artifact_groups, f"block_interface_population_artifacts: unknown unit {unit_id}")
        artifact_groups[unit_id].append(artifact)

    payloads: list[dict[str, Any]] = []
    artifacts: list[dict[str, Any]] = []
    bundle_records: list[dict[str, Any]] = []
    for unit in units:
        unit_id = unit["unit_id"]
        record = record_by_unit[unit_id]
        payload_group = payload_groups[unit_id]
        artifact_group = artifact_groups[unit_id]
        status = record["status"]
        payload_list: list[dict[str, Any]] = []
        artifact_list: list[dict[str, Any]] = []
        if status == "open":
            require(not payload_group, f"unit {unit_id}: open record cannot contain payload")
            require(not artifact_group, f"unit {unit_id}: open record cannot contain artifact")
        else:
            require(len(payload_group) == 1, f"unit {unit_id}: exactly one payload required")
            payload = exact_payload(
                payload_group[0],
                unit=unit,
                slot_payload_by_id=t03_payload_by_slot,
                path=f"block_interface_population_payload[{unit_id}]",
            )
            payloads.append(payload)
            payload_list = [payload]
            source_slot_ids = sorted({
                binding["operation_slot_id"] for binding in unit["parent_bindings"]
            })
            if status == "populated":
                require(
                    not artifact_group,
                    f"unit {unit_id}: populated record cannot contain proof artifact",
                )
                data_bundle = {
                    "unit_id": unit_id,
                    "unit_identity_sha256": unit["unit_identity_sha256"],
                    "block_interface_population_payload_sha256": payload[
                        "block_interface_population_payload_sha256"
                    ],
                }
                data_bundle["block_interface_population_data_bundle_sha256"] = catalogue.canonical_digest(
                    data_bundle
                )
                require(
                    record["population_digest"]
                    == data_bundle["block_interface_population_data_bundle_sha256"],
                    f"unit {unit_id}: populated digest does not bind payload",
                )
            else:
                require(
                    len(artifact_group) == 1,
                    f"unit {unit_id}: exactly one proof artifact required",
                )
                require(
                    all(slot_id in t03_artifact_by_slot for slot_id in source_slot_ids),
                    f"unit {unit_id}: all source T03 slots must be proved first",
                )
                expected_support = sorted({
                    t03_artifact_by_slot[slot_id] for slot_id in source_slot_ids
                })
                artifact = exact_artifact(
                    artifact_group[0],
                    unit=unit,
                    payload=payload,
                    expected_t03_support_ids=expected_support,
                    path=f"block_interface_population_artifact[{unit_id}]",
                )
                artifacts.append(artifact)
                artifact_list = [artifact]
                proof_bundle = {
                    "unit_id": unit_id,
                    "unit_identity_sha256": unit["unit_identity_sha256"],
                    "block_interface_population_payload_sha256": payload[
                        "block_interface_population_payload_sha256"
                    ],
                    "block_interface_population_artifact_sha256": artifact[
                        "block_interface_population_artifact_sha256"
                    ],
                    "support_t03_population_artifact_ids": expected_support,
                }
                proof_bundle["block_interface_population_proof_bundle_sha256"] = catalogue.canonical_digest(
                    proof_bundle
                )
                require(
                    record["population_digest"]
                    == proof_bundle["block_interface_population_proof_bundle_sha256"],
                    f"unit {unit_id}: proved digest does not bind payload/artifact bundle",
                )

        bundle = {
            "unit_id": unit_id,
            "unit_kind": unit["unit_kind"],
            "unit_identity_sha256": unit["unit_identity_sha256"],
            "status": status,
            "payloads_sha256": catalogue.canonical_digest(payload_list),
            "artifacts_sha256": catalogue.canonical_digest(artifact_list),
        }
        bundle["block_interface_population_bundle_sha256"] = catalogue.canonical_digest(bundle)
        bundle_records.append(bundle)

    require(
        raw_payloads == payloads,
        "block_interface_population_payloads: canonical unit order/content required",
    )
    require(
        raw_artifacts == artifacts,
        "block_interface_population_artifacts: canonical unit order/content required",
    )
    artifact_ids = [artifact["artifact_id"] for artifact in artifacts]
    require(
        len(artifact_ids) == len(set(artifact_ids)),
        "block_interface_population_artifacts: duplicate artifact_id",
    )

    status_counts = Counter(record["status"] for record in records)
    kind_counts = Counter(unit["unit_kind"] for unit in units)
    t03_ready = int(t03_exact["claims"]["slot_candidate_population_ready"])
    complete_population_data = int(status_counts["open"] == 0)
    all_units_proved = int(status_counts["proved"] == len(units))
    t04_ready = int(t03_ready and all_units_proved and len(artifacts) == len(units))

    global_bank = {
        "expected_slot_registry_sha256": t03_exact["claims"]["expected_slot_registry_sha256"],
        "rule_exhaustiveness_records_sha256": rule_exact["claims"][
            "rule_exhaustiveness_records_sha256"
        ],
        "rule_exhaustiveness_artifacts_sha256": rule_exact["claims"][
            "rule_exhaustiveness_artifacts_sha256"
        ],
        "t03_slot_population_records_sha256": t03_exact["claims"][
            "slot_population_records_sha256"
        ],
        "t03_slot_population_payloads_sha256": t03_exact["claims"][
            "slot_population_payloads_sha256"
        ],
        "t03_slot_population_artifacts_sha256": t03_exact["claims"][
            "slot_population_artifacts_sha256"
        ],
        "t03_slot_population_bundles_sha256": t03_exact["claims"][
            "slot_population_bundles_sha256"
        ],
        "global_family_skeleton_sha256": skeleton["recurrence_skeleton_sha256"],
        "expected_block_interface_units_sha256": catalogue.canonical_digest(units),
        "block_interface_population_records_sha256": catalogue.canonical_digest(records),
        "block_interface_population_payloads_sha256": catalogue.canonical_digest(payloads),
        "block_interface_population_artifacts_sha256": catalogue.canonical_digest(artifacts),
        "block_interface_population_bundles_sha256": catalogue.canonical_digest(bundle_records),
    }
    global_bank["global_block_interface_population_bank_sha256"] = catalogue.canonical_digest(
        global_bank
    )

    target_results = {
        record["target_id"]: record for record in atomic_exact["target_result_records"]
    }
    t04_complete = int(
        target_results["T04_BLOCK_INTERFACE_POPULATION"]["effective_target_complete"]
    )
    require(
        t04_complete == t04_ready,
        "T04_BLOCK_INTERFACE_POPULATION completion disagrees with exact T04 population bank",
    )

    target_artifact_by_id = {
        artifact["target_id"]: artifact for artifact in target_exact["atomic_target_artifacts"]
    }
    t04_target_artifact = target_artifact_by_id.get("T04_BLOCK_INTERFACE_POPULATION")
    if t04_ready:
        require(
            t04_target_artifact is not None,
            "T04 completed target missing global-population-bank",
        )
        require(
            t04_target_artifact["artifact_kind"] == "global-population-bank",
            "T04 target requires global-population-bank artifact",
        )
        require(
            t04_target_artifact["proof_locator"]
            == "block-interface-population-registry://T04_BLOCK_INTERFACE_POPULATION",
            "T04 target proof locator does not bind T04 registry",
        )
        require(
            t04_target_artifact["proof_digest"]
            == global_bank["global_block_interface_population_bank_sha256"],
            "T04 target proof digest does not bind noncircular T04 bank",
        )
    else:
        require(t04_target_artifact is None, "open T04 target cannot contain target artifact")

    claims = {
        "expected_population_units": len(units),
        "expected_recurrent_blocks": kind_counts["recurrent-block"],
        "expected_interface_rows": kind_counts["interface-row"],
        "open_population_units": status_counts["open"],
        "data_populated_units": status_counts["populated"],
        "proved_population_units": status_counts["proved"],
        "population_payloads": len(payloads),
        "population_artifacts": len(artifacts),
        "complete_population_data": complete_population_data,
        "t03_slot_candidate_population_ready": t03_ready,
        "t04_block_interface_population_ready": t04_ready,
        "exact_skeleton_derived_unit_bank": 1,
        "exact_t03_source_slot_binding": 1,
        "exact_t03_population_artifact_support": 1,
        "noncircular_global_population_bank_binding": 1,
        "t04_atomic_target_synchronized": 1,
        "all_n_proved_by_checker": 0,
        "open_unit_ids": [
            record["unit_id"] for record in records if record["status"] == "open"
        ],
        "data_populated_unit_ids": [
            record["unit_id"] for record in records if record["status"] == "populated"
        ],
        "global_family_skeleton_sha256": skeleton_certificate["certificate_sha256"],
        "slot_candidate_population_frontier_sha256": t03_certificate["certificate_sha256"],
        "atomic_target_artifact_registry_sha256": target_registry_certificate["certificate_sha256"],
        "expected_population_units_sha256": catalogue.canonical_digest(units),
        "block_interface_population_records_sha256": catalogue.canonical_digest(records),
        "block_interface_population_payloads_sha256": catalogue.canonical_digest(payloads),
        "block_interface_population_artifacts_sha256": catalogue.canonical_digest(artifacts),
        "block_interface_population_bundles_sha256": catalogue.canonical_digest(bundle_records),
        "global_block_interface_population_bank_sha256": global_bank[
            "global_block_interface_population_bank_sha256"
        ],
    }
    return {
        "expected_block_interface_population_units": units,
        "block_interface_population_records": records,
        "block_interface_population_payloads": payloads,
        "block_interface_population_artifacts": artifacts,
        "block_interface_population_bundle_records": bundle_records,
        "global_block_interface_population_bank": global_bank,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in (
        "expected_block_interface_population_units",
        "block_interface_population_records",
        "block_interface_population_payloads",
        "block_interface_population_artifacts",
        "block_interface_population_bundle_records",
        "global_block_interface_population_bank",
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
        "units": claims["expected_population_units"],
        "blocks": claims["expected_recurrent_blocks"],
        "interfaces": claims["expected_interface_rows"],
        "open": claims["open_population_units"],
        "populated": claims["data_populated_units"],
        "proved": claims["proved_population_units"],
        "ready": claims["t04_block_interface_population_ready"],
        "all_n": claims["all_n_proved_by_checker"],
    }


def build_certificate(
    t03_certificate: dict[str, Any],
    target_registry_certificate: dict[str, Any],
    records: list[dict[str, Any]],
    payloads: list[dict[str, Any]],
    artifacts: list[dict[str, Any]],
) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "slot_candidate_population_frontier_certificate": t03_certificate,
        "atomic_target_artifact_registry_certificate": target_registry_certificate,
        "block_interface_population_records": records,
        "block_interface_population_payloads": payloads,
        "block_interface_population_artifacts": artifacts,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: check_prime_power_block_interface_population_frontier.py certificate.json"
        )
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
