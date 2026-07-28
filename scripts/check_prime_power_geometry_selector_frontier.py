#!/usr/bin/env python3
"""Validate and synchronize the exact T05 geometry/selector proof bank.

T03 supplies literal slot payloads and T04 supplies skeleton-derived block/interface assembly.
This checker binds each expected slot to one finite linked-operation geometry certificate, verifies
that the certificate is projected exactly into the T03 payload, and seals the resulting geometry
and selector proof banks into the two typed GEOMETRY_SELECTOR_CORRECT obligation artifacts and the
T05 atomic target artifact.

This is documentary proof infrastructure. The nested finite checkers establish exact arithmetic for
the supplied finite systems; this checker does not prove that those systems are the genuine
exhaustive recurrence for arbitrary n and permanently reports ``all_n_proved_by_checker = 0``.
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
import check_prime_power_atomic_target_artifact_registry as target_artifacts
import check_prime_power_block_interface_population_frontier as t04_frontier
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_linked_operation_selector as linked
import check_prime_power_obligation_artifact_registry as obligation_artifacts


class GeometrySelectorFrontierError(ValueError):
    """Raised when the exact T05 geometry/selector bank is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GeometrySelectorFrontierError(message)


REQUIRED_SLOT_ARTIFACT_KIND = "slot-geometry-selector-proof"
GEOMETRY_OBLIGATION_LOCATOR = (
    "geometry-selector-frontier://GEOMETRY_SELECTOR_CORRECT/geometry-proof"
)
SELECTOR_OBLIGATION_LOCATOR = (
    "geometry-selector-frontier://GEOMETRY_SELECTOR_CORRECT/selector-proof"
)
T05_TARGET_LOCATOR = "geometry-selector-frontier://T05_GEOMETRY_SELECTORS"


def flatten_fates(source_manifest: dict[str, Any]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for rank, bucket in ((1, "rank1"), (2, "rank2"), (3, "rank3")):
        for record in source_manifest["fates"][bucket]:
            item = {"rank": rank, **copy.deepcopy(record)}
            item["owner_fate_witness_sha256"] = catalogue.canonical_digest(item)
            records.append(item)
    records.sort(key=lambda item: (item["rank"], item["owner_fate_witness_sha256"]))
    return records


def geometry_projection(
    certificate: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    linked.validate_certificate(certificate)
    exact = linked.exact_composition(certificate)
    linkage_certificate = certificate["linkage_certificate"]
    direct_certificate = certificate["direct_delta_certificate"]
    selector_certificate = certificate["background_selector_certificate"]
    pool_manifest = direct_certificate["pool_certificate"]["pool_manifest"]
    source_manifest = linkage_certificate["source_manifest"]
    direct_records, direct_exact = __import__(
        "check_direct_response_triple_delta"
    ).exact_records(direct_certificate["pool_certificate"])
    _selector_records, selector_exact = __import__(
        "check_prime_power_background_response_selector"
    ).exact_records(selector_certificate)

    population_projection = {
        "points": copy.deepcopy(pool_manifest["pre_response_points"]),
        "removals": copy.deepcopy(pool_manifest["removed_point_indices"]),
        "survivor_background": copy.deepcopy(source_manifest["background_points"]),
        "owner_fate_witnesses": flatten_fates(source_manifest),
        "response_family": [
            copy.deepcopy(record["response"]) for record in direct_records
        ],
        "selector_data": {
            "host_id": linkage_certificate["host_id"],
            "catalogue_record_sha256": linkage_certificate[
                "catalogue_record_sha256"
            ],
            "linked_fibre_id": linkage_certificate["fibre_id"],
            "linked_source_sha256": linkage_certificate["source_sha256"],
            "linked_operation_selector_sha256": certificate["certificate_sha256"],
            "direct_delta_certificate_sha256": catalogue.canonical_digest(direct_certificate),
            "background_selector_certificate_sha256": selector_certificate["selector_sha256"],
            "selected_response": copy.deepcopy(
                selector_exact["selected_response"]
            ),
            "minimum_new_triples": selector_exact["minimum_new_triples"],
            "destroyed_current_triples": direct_exact["destroyed_triples"],
            "minimum_delta": direct_exact["minimum_delta"],
            "strict_improvement": int(direct_exact["minimum_delta"] < 0),
            "full_minimizer_count": selector_exact["minimizer_count"],
            "response_records_sha256": direct_exact["response_records_sha256"],
            "selector_records_sha256": selector_exact[
                "response_records_sha256"
            ],
            "responsewise_delta_threshold_identity": 1,
        },
    }
    geometry_summary = {
        "host_id": linkage_certificate["host_id"],
        "catalogue_record_sha256": linkage_certificate[
            "catalogue_record_sha256"
        ],
        "linked_source_sha256": linkage_certificate["source_sha256"],
        "pre_response_points_sha256": catalogue.canonical_digest(
            pool_manifest["pre_response_points"]
        ),
        "removed_point_indices_sha256": catalogue.canonical_digest(
            pool_manifest["removed_point_indices"]
        ),
        "survivor_background_sha256": catalogue.canonical_digest(
            source_manifest["background_points"]
        ),
        "owner_fate_witnesses_sha256": catalogue.canonical_digest(
            population_projection["owner_fate_witnesses"]
        ),
        "response_family_sha256": catalogue.canonical_digest(
            population_projection["response_family"]
        ),
        "direct_delta_certificate_sha256": catalogue.canonical_digest(direct_certificate),
        "direct_response_records_sha256": direct_exact[
            "response_records_sha256"
        ],
        "destroyed_current_triples": direct_exact["destroyed_triples"],
        "minimum_delta": direct_exact["minimum_delta"],
    }
    geometry_summary["slot_geometry_summary_sha256"] = catalogue.canonical_digest(
        geometry_summary
    )
    selector_summary = {
        "host_id": linkage_certificate["host_id"],
        "background_selector_certificate_sha256": selector_certificate["selector_sha256"],
        "selector_response_records_sha256": selector_exact[
            "response_records_sha256"
        ],
        "minimum_new_triples": selector_exact["minimum_new_triples"],
        "selected_response": copy.deepcopy(selector_exact["selected_response"]),
        "minimizer_count": selector_exact["minimizer_count"],
        "strict_improvement": int(direct_exact["minimum_delta"] < 0),
        "threshold_equivalence_verified": int(
            exact["claims"]["strict_improvement"]
            == int(
                selector_exact["minimum_new_triples"]
                < direct_exact["destroyed_triples"]
            )
        ),
        "policy_is_full_selector": exact["claims"]["policy_is_full_selector"],
        "policy_has_minimum_value": exact["claims"][
            "policy_has_minimum_value"
        ],
        "policy_selector_penalty": exact["claims"][
            "policy_selector_penalty"
        ],
    }
    require(
        selector_summary["threshold_equivalence_verified"] == 1,
        "linked selector: threshold equivalence not verified",
    )
    selector_summary["slot_selector_summary_sha256"] = catalogue.canonical_digest(
        selector_summary
    )
    return population_projection, geometry_summary, selector_summary


def exact_status_record(
    record: dict[str, Any],
    *,
    slot_id: str,
    slot_payload_sha256: str | None,
    path: str,
) -> dict[str, Any]:
    record_id = f"geometry::{slot_id}"
    require(record.get("record_id") == record_id, f"{path}.record_id: mismatch")
    require(record.get("slot_id") == slot_id, f"{path}.slot_id: mismatch")
    require(
        record.get("slot_population_payload_sha256") == slot_payload_sha256,
        f"{path}.slot_population_payload_sha256: mismatch",
    )
    status = record.get("status")
    locator = record.get("verification_locator")
    digest = record.get("verification_digest")
    note = record.get("note")
    require(status in {"open", "proved"}, f"{path}.status: expected open/proved")
    require(isinstance(note, str) and note, f"{path}.note: required")
    if status == "open":
        require(locator is None, f"{path}.verification_locator: open requires null")
        require(digest is None, f"{path}.verification_digest: open requires null")
    else:
        require(
            locator == f"geometry-selector-slot-registry://{slot_id}",
            f"{path}.verification_locator: canonical slot URI required",
        )
        require(
            isinstance(digest, str) and digest,
            f"{path}.verification_digest: required",
        )
        require(
            slot_payload_sha256 is not None,
            f"{path}: proved geometry requires populated T03 slot",
        )
    output = {
        "record_id": record_id,
        "slot_id": slot_id,
        "slot_population_payload_sha256": slot_payload_sha256,
        "status": status,
        "verification_locator": locator,
        "verification_digest": digest,
        "note": note,
    }
    output["geometry_selector_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_slot_artifact(
    artifact: dict[str, Any],
    *,
    slot_id: str,
    slot_payload_sha256: str,
    geometry_certificate_sha256: str,
    expected_t03_support: list[str],
    expected_t04_support: list[str],
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
    for name, value in values.items():
        require(isinstance(value, str) and value, f"{path}.{name}: required")
    require(artifact.get("slot_id") == slot_id, f"{path}.slot_id: mismatch")
    require(
        values["artifact_kind"] == REQUIRED_SLOT_ARTIFACT_KIND,
        f"{path}.artifact_kind: wrong kind",
    )
    require(
        artifact.get("slot_population_payload_sha256")
        == slot_payload_sha256,
        f"{path}.slot_population_payload_sha256: mismatch",
    )
    require(
        artifact.get("geometry_certificate_sha256")
        == geometry_certificate_sha256,
        f"{path}.geometry_certificate_sha256: mismatch",
    )
    t03_support = artifact.get("support_t03_population_artifact_ids")
    t04_support = artifact.get("support_t04_population_artifact_ids")
    require(
        t03_support == expected_t03_support,
        f"{path}.support_t03_population_artifact_ids: exact support required",
    )
    require(
        t04_support == expected_t04_support,
        f"{path}.support_t04_population_artifact_ids: exact support required",
    )
    for name, support in (
        ("support_t03_population_artifact_ids", t03_support),
        ("support_t04_population_artifact_ids", t04_support),
    ):
        require(isinstance(support, list), f"{path}.{name}: list required")
        require(support == sorted(support), f"{path}.{name}: sorted")
        require(len(support) == len(set(support)), f"{path}.{name}: duplicates")
        require(values["artifact_id"] not in support, f"{path}: self support")
    output = {
        "slot_id": slot_id,
        "artifact_id": values["artifact_id"],
        "artifact_kind": values["artifact_kind"],
        "slot_population_payload_sha256": slot_payload_sha256,
        "geometry_certificate_sha256": geometry_certificate_sha256,
        "proof_locator": values["proof_locator"],
        "proof_digest": values["proof_digest"],
        "proof_statement": values["proof_statement"],
        "support_t03_population_artifact_ids": list(t03_support),
        "support_t04_population_artifact_ids": list(t04_support),
        "evidence": values["evidence"],
    }
    output["geometry_selector_artifact_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    t04_certificate = certificate.get(
        "block_interface_population_frontier_certificate"
    )
    raw_records = certificate.get("slot_geometry_selector_records")
    raw_geometry_certificates = certificate.get(
        "slot_linked_operation_selector_certificates"
    )
    raw_artifacts = certificate.get("slot_geometry_selector_artifacts")
    require(
        isinstance(t04_certificate, dict),
        "block_interface_population_frontier_certificate: expected object",
    )
    require(
        isinstance(raw_records, list),
        "slot_geometry_selector_records: expected list",
    )
    require(
        isinstance(raw_geometry_certificates, list),
        "slot_linked_operation_selector_certificates: expected list",
    )
    require(
        isinstance(raw_artifacts, list),
        "slot_geometry_selector_artifacts: expected list",
    )

    t04_frontier.validate_certificate(t04_certificate)
    t04_exact = t04_frontier.exact_certificate(t04_certificate)
    t03_certificate = t04_certificate[
        "slot_candidate_population_frontier_certificate"
    ]
    t03_exact = __import__(
        "check_prime_power_slot_candidate_population_frontier"
    ).exact_certificate(t03_certificate)
    rule_certificate = t03_certificate[
        "rule_exhaustiveness_frontier_certificate"
    ]
    source_frontier = rule_certificate[
        "source_truth_frontier_execution_certificate"
    ]
    source_registry = source_frontier[
        "source_statement_truth_registry_certificate"
    ]
    obligation_certificate = source_registry[
        "obligation_artifact_registry_certificate"
    ]
    obligation_artifacts.validate_certificate(obligation_certificate)
    obligation_exact = obligation_artifacts.exact_certificate(
        obligation_certificate
    )
    closure_certificate = obligation_certificate[
        "all_n_implication_closure_certificate"
    ]
    closure_exact = closure.exact_certificate(closure_certificate)
    target_registry = t04_certificate[
        "atomic_target_artifact_registry_certificate"
    ]
    target_artifacts.validate_certificate(target_registry)
    target_exact = target_artifacts.exact_certificate(target_registry)
    current = target_registry["current_frontier_execution_certificate"]
    atomic_certificate = current["atomic_frontier_execution_certificate"]
    atomic.validate_certificate(atomic_certificate)
    atomic_exact = atomic.exact_certificate(atomic_certificate)

    slots = rule_certificate[
        "source_truth_frontier_execution_certificate"
    ]["source_statement_truth_registry_certificate"][
        "rule_source_provenance_certificate"
    ][
        "clause_manifest"
    ][
        "expected_slot_registry"
    ][
        "slots"
    ]
    payload_by_slot = {
        payload["slot_id"]: payload
        for payload in t03_exact["slot_population_payloads"]
    }
    t03_artifact_by_slot = {
        artifact["slot_id"]: artifact["artifact_id"]
        for artifact in t03_exact["slot_population_artifacts"]
    }
    t04_artifact_by_unit = {
        artifact["unit_id"]: artifact["artifact_id"]
        for artifact in t04_exact["block_interface_population_artifacts"]
    }
    units_by_slot: dict[str, list[str]] = {slot["slot_id"]: [] for slot in slots}
    for unit in t04_exact["expected_block_interface_population_units"]:
        for binding in unit["parent_bindings"]:
            slot_id = binding["operation_slot_id"]
            require(slot_id in units_by_slot, f"T04 unit uses unknown slot {slot_id}")
            units_by_slot[slot_id].append(unit["unit_id"])
    for slot_id in units_by_slot:
        units_by_slot[slot_id] = sorted(set(units_by_slot[slot_id]))

    require(
        len(raw_records) == len(slots),
        "slot_geometry_selector_records: exact slot cardinality required",
    )
    require(
        [record.get("slot_id") for record in raw_records]
        == [slot["slot_id"] for slot in slots],
        "slot_geometry_selector_records: exact canonical slot order required",
    )
    records = []
    for index, (raw, slot) in enumerate(zip(raw_records, slots)):
        payload = payload_by_slot.get(slot["slot_id"])
        records.append(
            exact_status_record(
                raw,
                slot_id=slot["slot_id"],
                slot_payload_sha256=(
                    None
                    if payload is None
                    else payload["slot_population_payload_sha256"]
                ),
                path=f"slot_geometry_selector_records[{index}]",
            )
        )
    require(
        raw_records == records,
        "slot_geometry_selector_records: canonical records/digests required",
    )
    record_by_slot = {record["slot_id"]: record for record in records}

    certificate_groups: dict[str, list[dict[str, Any]]] = {
        slot["slot_id"]: [] for slot in slots
    }
    for item in raw_geometry_certificates:
        require(
            isinstance(item, dict),
            "slot_linked_operation_selector_certificates: expected objects",
        )
        slot_id = item.get("slot_id")
        require(
            slot_id in certificate_groups,
            f"slot geometry certificate: unknown slot {slot_id}",
        )
        certificate_groups[slot_id].append(item)

    artifact_groups: dict[str, list[dict[str, Any]]] = {
        slot["slot_id"]: [] for slot in slots
    }
    for item in raw_artifacts:
        require(
            isinstance(item, dict),
            "slot_geometry_selector_artifacts: expected objects",
        )
        slot_id = item.get("slot_id")
        require(
            slot_id in artifact_groups,
            f"slot geometry artifact: unknown slot {slot_id}",
        )
        artifact_groups[slot_id].append(item)

    geometry_certificates: list[dict[str, Any]] = []
    artifacts: list[dict[str, Any]] = []
    geometry_summaries: list[dict[str, Any]] = []
    selector_summaries: list[dict[str, Any]] = []
    bundle_records: list[dict[str, Any]] = []

    for slot in slots:
        slot_id = slot["slot_id"]
        record = record_by_slot[slot_id]
        cert_group = certificate_groups[slot_id]
        artifact_group = artifact_groups[slot_id]
        geometry_list: list[dict[str, Any]] = []
        artifact_list: list[dict[str, Any]] = []
        geometry_summary_list: list[dict[str, Any]] = []
        selector_summary_list: list[dict[str, Any]] = []

        if record["status"] == "open":
            require(
                not cert_group,
                f"slot {slot_id}: open record cannot contain geometry certificate",
            )
            require(
                not artifact_group,
                f"slot {slot_id}: open record cannot contain proof artifact",
            )
        else:
            require(
                len(cert_group) == 1,
                f"slot {slot_id}: exactly one linked geometry certificate required",
            )
            require(
                len(artifact_group) == 1,
                f"slot {slot_id}: exactly one geometry proof artifact required",
            )
            require(
                slot_id in payload_by_slot,
                f"slot {slot_id}: proved geometry requires T03 payload",
            )
            require(
                slot_id in t03_artifact_by_slot,
                f"slot {slot_id}: proved geometry requires proved T03 slot",
            )
            payload = payload_by_slot[slot_id]
            wrapper = cert_group[0]
            require(wrapper.get("slot_id") == slot_id, f"slot {slot_id}: wrapper mismatch")
            nested = wrapper.get("linked_operation_selector_certificate")
            require(
                isinstance(nested, dict),
                f"slot {slot_id}: linked_operation_selector_certificate required",
            )
            projection, geometry_summary, selector_summary = geometry_projection(
                nested
            )
            data = payload["population_data"]
            for key in (
                "points",
                "removals",
                "survivor_background",
                "owner_fate_witnesses",
                "response_family",
                "selector_data",
            ):
                require(
                    data[key] == projection[key],
                    f"slot {slot_id}: T03 {key} differs from linked geometry projection",
                )
            require(
                payload["host_id"] == projection["selector_data"]["host_id"],
                f"slot {slot_id}: host differs from linked geometry",
            )
            canonical_wrapper = {
                "slot_id": slot_id,
                "slot_population_payload_sha256": payload[
                    "slot_population_payload_sha256"
                ],
                "linked_operation_selector_certificate": nested,
                "linked_operation_selector_certificate_sha256": nested[
                    "certificate_sha256"
                ],
                "geometry_projection_sha256": catalogue.canonical_digest(
                    projection
                ),
            }
            canonical_wrapper[
                "slot_linked_geometry_certificate_sha256"
            ] = catalogue.canonical_digest(canonical_wrapper)
            require(
                wrapper == canonical_wrapper,
                f"slot {slot_id}: noncanonical linked geometry wrapper",
            )
            geometry_certificates.append(canonical_wrapper)
            geometry_list = [canonical_wrapper]

            geometry_summary = {
                "slot_id": slot_id,
                "slot_population_payload_sha256": payload[
                    "slot_population_payload_sha256"
                ],
                **geometry_summary,
            }
            geometry_summary["slot_geometry_bank_record_sha256"] = (
                catalogue.canonical_digest(geometry_summary)
            )
            selector_summary = {
                "slot_id": slot_id,
                "slot_population_payload_sha256": payload[
                    "slot_population_payload_sha256"
                ],
                **selector_summary,
            }
            selector_summary["slot_selector_bank_record_sha256"] = (
                catalogue.canonical_digest(selector_summary)
            )
            geometry_summaries.append(geometry_summary)
            selector_summaries.append(selector_summary)
            geometry_summary_list = [geometry_summary]
            selector_summary_list = [selector_summary]

            expected_t03_support = [t03_artifact_by_slot[slot_id]]
            expected_t04_support = sorted(
                t04_artifact_by_unit[unit_id]
                for unit_id in units_by_slot[slot_id]
                if unit_id in t04_artifact_by_unit
            )
            require(
                len(expected_t04_support) == len(units_by_slot[slot_id]),
                f"slot {slot_id}: every using T04 unit must be proved",
            )
            artifact = exact_slot_artifact(
                artifact_group[0],
                slot_id=slot_id,
                slot_payload_sha256=payload[
                    "slot_population_payload_sha256"
                ],
                geometry_certificate_sha256=canonical_wrapper[
                    "slot_linked_geometry_certificate_sha256"
                ],
                expected_t03_support=expected_t03_support,
                expected_t04_support=expected_t04_support,
                path=f"slot_geometry_selector_artifact[{slot_id}]",
            )
            artifacts.append(artifact)
            artifact_list = [artifact]

            proof_bundle = {
                "slot_id": slot_id,
                "slot_population_payload_sha256": payload[
                    "slot_population_payload_sha256"
                ],
                "slot_linked_geometry_certificate_sha256": canonical_wrapper[
                    "slot_linked_geometry_certificate_sha256"
                ],
                "slot_geometry_bank_record_sha256": geometry_summary[
                    "slot_geometry_bank_record_sha256"
                ],
                "slot_selector_bank_record_sha256": selector_summary[
                    "slot_selector_bank_record_sha256"
                ],
                "geometry_selector_artifact_sha256": artifact[
                    "geometry_selector_artifact_sha256"
                ],
                "support_t03_population_artifact_ids": expected_t03_support,
                "support_t04_population_artifact_ids": expected_t04_support,
            }
            proof_bundle[
                "slot_geometry_selector_proof_bundle_sha256"
            ] = catalogue.canonical_digest(proof_bundle)
            require(
                record["verification_digest"]
                == proof_bundle[
                    "slot_geometry_selector_proof_bundle_sha256"
                ],
                f"slot {slot_id}: verification digest does not bind proof bundle",
            )

        bundle = {
            "slot_id": slot_id,
            "status": record["status"],
            "geometry_certificates_sha256": catalogue.canonical_digest(
                geometry_list
            ),
            "geometry_summaries_sha256": catalogue.canonical_digest(
                geometry_summary_list
            ),
            "selector_summaries_sha256": catalogue.canonical_digest(
                selector_summary_list
            ),
            "artifacts_sha256": catalogue.canonical_digest(artifact_list),
        }
        bundle["slot_geometry_selector_bundle_sha256"] = catalogue.canonical_digest(
            bundle
        )
        bundle_records.append(bundle)

    require(
        raw_geometry_certificates == geometry_certificates,
        "slot_linked_operation_selector_certificates: canonical slot order/content required",
    )
    require(
        raw_artifacts == artifacts,
        "slot_geometry_selector_artifacts: canonical slot order/content required",
    )
    artifact_ids = [artifact["artifact_id"] for artifact in artifacts]
    require(
        len(artifact_ids) == len(set(artifact_ids)),
        "slot_geometry_selector_artifacts: duplicate artifact_id",
    )

    status_counts = Counter(record["status"] for record in records)
    t03_ready = int(t03_exact["claims"]["slot_candidate_population_ready"])
    t04_ready = int(t04_exact["claims"]["t04_block_interface_population_ready"])
    all_slots_proved = int(status_counts["proved"] == len(slots))
    geometry_ready = int(
        t03_ready
        and t04_ready
        and all_slots_proved
        and len(artifacts) == len(slots)
    )

    geometry_bank = {
        "expected_slot_registry_sha256": t03_exact["claims"][
            "expected_slot_registry_sha256"
        ],
        "t03_slot_population_payloads_sha256": t03_exact["claims"][
            "slot_population_payloads_sha256"
        ],
        "t03_slot_population_artifacts_sha256": t03_exact["claims"][
            "slot_population_artifacts_sha256"
        ],
        "t04_expected_population_units_sha256": t04_exact["claims"][
            "expected_population_units_sha256"
        ],
        "t04_population_payloads_sha256": t04_exact["claims"][
            "block_interface_population_payloads_sha256"
        ],
        "t04_population_artifacts_sha256": t04_exact["claims"][
            "block_interface_population_artifacts_sha256"
        ],
        "slot_geometry_selector_records_sha256": catalogue.canonical_digest(
            records
        ),
        "slot_linked_geometry_certificates_sha256": catalogue.canonical_digest(
            geometry_certificates
        ),
        "slot_geometry_summaries_sha256": catalogue.canonical_digest(
            geometry_summaries
        ),
        "slot_geometry_selector_artifacts_sha256": catalogue.canonical_digest(
            artifacts
        ),
        "slot_geometry_selector_bundles_sha256": catalogue.canonical_digest(
            bundle_records
        ),
    }
    geometry_bank["geometry_proof_bank_sha256"] = catalogue.canonical_digest(
        geometry_bank
    )
    selector_bank = {
        "expected_slot_registry_sha256": t03_exact["claims"][
            "expected_slot_registry_sha256"
        ],
        "slot_linked_geometry_certificates_sha256": catalogue.canonical_digest(
            geometry_certificates
        ),
        "slot_selector_summaries_sha256": catalogue.canonical_digest(
            selector_summaries
        ),
        "slot_geometry_selector_artifacts_sha256": catalogue.canonical_digest(
            artifacts
        ),
        "slot_geometry_selector_bundles_sha256": catalogue.canonical_digest(
            bundle_records
        ),
    }
    selector_bank["selector_proof_bank_sha256"] = catalogue.canonical_digest(
        selector_bank
    )
    combined_bank = {
        "geometry_proof_bank_sha256": geometry_bank[
            "geometry_proof_bank_sha256"
        ],
        "selector_proof_bank_sha256": selector_bank[
            "selector_proof_bank_sha256"
        ],
        "slot_geometry_selector_records_sha256": catalogue.canonical_digest(
            records
        ),
        "slot_geometry_selector_artifacts_sha256": catalogue.canonical_digest(
            artifacts
        ),
    }
    combined_bank[
        "geometry_selector_frontier_proof_bank_sha256"
    ] = catalogue.canonical_digest(combined_bank)

    closure_by_id = {
        record["obligation_id"]: record
        for record in closure_exact["proof_obligations"]
    }
    geometry_closure = closure_by_id["GEOMETRY_SELECTOR_CORRECT"]
    require(
        int(geometry_closure["closed"]) == geometry_ready,
        "GEOMETRY_SELECTOR_CORRECT closure disagrees with exact T05 bank",
    )

    obligation_by_kind = {
        artifact["artifact_kind"]: artifact
        for artifact in obligation_exact["proof_artifacts"]
        if artifact["obligation_id"] == "GEOMETRY_SELECTOR_CORRECT"
    }
    population_artifact_ids = sorted(
        artifact["artifact_id"]
        for artifact in obligation_exact["proof_artifacts"]
        if artifact["obligation_id"] == "SLOT_AND_CANDIDATE_POPULATION"
    )
    require(
        len(obligation_by_kind) == (2 if geometry_ready else 0),
        "GEOMETRY_SELECTOR_CORRECT obligation artifact presence disagrees with readiness",
    )
    if geometry_ready:
        geometry_obligation = obligation_by_kind.get("geometry-proof")
        selector_obligation = obligation_by_kind.get("selector-proof")
        require(
            geometry_obligation is not None and selector_obligation is not None,
            "GEOMETRY_SELECTOR_CORRECT requires geometry-proof and selector-proof",
        )
        require(
            geometry_obligation["locator"] == GEOMETRY_OBLIGATION_LOCATOR,
            "geometry-proof locator does not bind T05 geometry bank",
        )
        require(
            geometry_obligation["digest"]
            == geometry_bank["geometry_proof_bank_sha256"],
            "geometry-proof digest does not bind exact geometry bank",
        )
        require(
            selector_obligation["locator"] == SELECTOR_OBLIGATION_LOCATOR,
            "selector-proof locator does not bind T05 selector bank",
        )
        require(
            selector_obligation["digest"]
            == selector_bank["selector_proof_bank_sha256"],
            "selector-proof digest does not bind exact selector bank",
        )
        require(
            geometry_obligation["support_artifact_ids"]
            == population_artifact_ids,
            "geometry-proof requires exact population-artifact support",
        )
        require(
            selector_obligation["support_artifact_ids"]
            == population_artifact_ids,
            "selector-proof requires exact population-artifact support",
        )

    target_results = {
        record["target_id"]: record
        for record in atomic_exact["target_result_records"]
    }
    t05_complete = int(
        target_results["T05_GEOMETRY_SELECTORS"]["effective_target_complete"]
    )
    require(
        t05_complete == geometry_ready,
        "T05_GEOMETRY_SELECTORS completion disagrees with exact geometry/selector bank",
    )
    target_artifact_by_id = {
        artifact["target_id"]: artifact
        for artifact in target_exact["atomic_target_artifacts"]
    }
    t05_artifact = target_artifact_by_id.get("T05_GEOMETRY_SELECTORS")
    if geometry_ready:
        require(
            t05_artifact is not None,
            "completed T05 target missing geometry-selector-proof artifact",
        )
        require(
            t05_artifact["artifact_kind"] == "geometry-selector-proof",
            "T05 target requires geometry-selector-proof",
        )
        require(
            t05_artifact["proof_locator"] == T05_TARGET_LOCATOR,
            "T05 target proof locator does not bind T05 frontier",
        )
        require(
            t05_artifact["proof_digest"]
            == combined_bank[
                "geometry_selector_frontier_proof_bank_sha256"
            ],
            "T05 target proof digest does not bind noncircular T05 bank",
        )
    else:
        require(
            t05_artifact is None,
            "open T05 target cannot contain target artifact",
        )

    claims = {
        "expected_slots": len(slots),
        "open_geometry_slots": status_counts["open"],
        "proved_geometry_slots": status_counts["proved"],
        "linked_geometry_certificates": len(geometry_certificates),
        "geometry_selector_artifacts": len(artifacts),
        "t03_slot_candidate_population_ready": t03_ready,
        "t04_block_interface_population_ready": t04_ready,
        "geometry_selector_correct_ready": geometry_ready,
        "exact_t03_geometry_projection_binding": 1,
        "exact_t04_usage_artifact_support": 1,
        "exact_responsewise_delta_threshold_binding": 1,
        "noncircular_geometry_selector_bank_binding": 1,
        "geometry_obligation_synchronized": 1,
        "selector_obligation_synchronized": 1,
        "t05_atomic_target_synchronized": 1,
        "all_n_proved_by_checker": 0,
        "open_slot_ids": [
            record["slot_id"] for record in records if record["status"] == "open"
        ],
        "slot_geometry_selector_records_sha256": catalogue.canonical_digest(
            records
        ),
        "slot_linked_geometry_certificates_sha256": catalogue.canonical_digest(
            geometry_certificates
        ),
        "slot_geometry_summaries_sha256": catalogue.canonical_digest(
            geometry_summaries
        ),
        "slot_selector_summaries_sha256": catalogue.canonical_digest(
            selector_summaries
        ),
        "slot_geometry_selector_artifacts_sha256": catalogue.canonical_digest(
            artifacts
        ),
        "slot_geometry_selector_bundles_sha256": catalogue.canonical_digest(
            bundle_records
        ),
        "geometry_proof_bank_sha256": geometry_bank[
            "geometry_proof_bank_sha256"
        ],
        "selector_proof_bank_sha256": selector_bank[
            "selector_proof_bank_sha256"
        ],
        "geometry_selector_frontier_proof_bank_sha256": combined_bank[
            "geometry_selector_frontier_proof_bank_sha256"
        ],
        "obligation_artifact_registry_sha256": obligation_certificate[
            "certificate_sha256"
        ],
        "atomic_target_artifact_registry_sha256": target_registry[
            "certificate_sha256"
        ],
    }
    return {
        "slot_geometry_selector_records": records,
        "slot_linked_operation_selector_certificates": geometry_certificates,
        "slot_geometry_selector_artifacts": artifacts,
        "slot_geometry_summaries": geometry_summaries,
        "slot_selector_summaries": selector_summaries,
        "slot_geometry_selector_bundle_records": bundle_records,
        "geometry_proof_bank": geometry_bank,
        "selector_proof_bank": selector_bank,
        "geometry_selector_frontier_proof_bank": combined_bank,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in (
        "slot_geometry_selector_records",
        "slot_linked_operation_selector_certificates",
        "slot_geometry_selector_artifacts",
        "slot_geometry_summaries",
        "slot_selector_summaries",
        "slot_geometry_selector_bundle_records",
        "geometry_proof_bank",
        "selector_proof_bank",
        "geometry_selector_frontier_proof_bank",
        "claims",
    ):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {
        key: value
        for key, value in certificate.items()
        if key != "certificate_sha256"
    }
    require(
        certificate.get("certificate_sha256")
        == catalogue.canonical_digest(payload),
        "certificate_sha256: incorrect",
    )
    claims = exact["claims"]
    return {
        "slots": claims["expected_slots"],
        "open": claims["open_geometry_slots"],
        "proved": claims["proved_geometry_slots"],
        "ready": claims["geometry_selector_correct_ready"],
        "all_n": claims["all_n_proved_by_checker"],
    }


def build_certificate(
    t04_certificate: dict[str, Any],
    records: list[dict[str, Any]],
    geometry_certificates: list[dict[str, Any]],
    artifacts: list[dict[str, Any]],
) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "block_interface_population_frontier_certificate": t04_certificate,
        "slot_geometry_selector_records": records,
        "slot_linked_operation_selector_certificates": geometry_certificates,
        "slot_geometry_selector_artifacts": artifacts,
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: check_prime_power_geometry_selector_frontier.py certificate.json"
        )
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
