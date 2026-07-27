#!/usr/bin/env python3
"""Validate noncircular operation-slot coverage of a canonical fibre batch.

The older fibre batch can validate each populated operation exactly, but its optional
``expected_fibre_ids`` field is source-dependent.  This checker composes that batch with
an independently validated operation-slot registry.  Every populated fibre must be
assigned to exactly one expected slot, and the assignment must agree on host, source,
fibre identity and ordered state labels.

Passing this checker proves slot-to-record conformance and exact coverage only.  It does
not prove that the parent-rule slot enumerator is exhaustive or that state labels have
their intended semantics.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from pathlib import Path
from random import Random
from typing import Any

import check_prime_power_background_signature as signature
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_operation_slot_registry as slots
import check_prime_power_real_fibre_batch_manifest as batch


class SlotBatchError(ValueError):
    """Raised when a slot-covered fibre batch is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SlotBatchError(message)


def exact_assignment(record: dict[str, Any]) -> dict[str, Any]:
    slot_id = record.get("slot_id")
    fibre_id = record.get("fibre_id")
    host_id = record.get("host_id")
    source_sha256 = record.get("source_sha256")
    require(isinstance(slot_id, str) and slot_id, "slot_id: expected nonempty string")
    require(isinstance(fibre_id, str) and fibre_id, "fibre_id: expected nonempty string")
    require(isinstance(host_id, str) and host_id, "host_id: expected nonempty string")
    require(
        isinstance(source_sha256, str)
        and len(source_sha256) == 64
        and all(character in "0123456789abcdef" for character in source_sha256),
        "source_sha256: expected lowercase SHA-256",
    )
    output = {
        "slot_id": slot_id,
        "fibre_id": fibre_id,
        "host_id": host_id,
        "source_sha256": source_sha256,
    }
    output["assignment_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    registry = certificate.get("expected_slot_registry")
    fibre_batch = certificate.get("fibre_batch")
    raw_assignments = certificate.get("slot_assignments")
    require(isinstance(registry, dict), "expected_slot_registry: expected object")
    require(isinstance(fibre_batch, dict), "fibre_batch: expected object")
    require(isinstance(raw_assignments, list), "slot_assignments: expected list")

    registry_summary = slots.validate_registry(registry)
    batch_summary = batch.validate_manifest(fibre_batch)
    require(
        fibre_batch.get("expected_fibre_ids") is None,
        "fibre_batch.expected_fibre_ids: source-dependent completeness must remain undeclared",
    )
    require(batch_summary["complete"] == 0, "fibre batch unexpectedly declared source-dependent completeness")

    batch_exact = batch.exact_manifest(fibre_batch)
    records_by_fibre = {record["fibre_id"]: record for record in batch_exact["records"]}
    entries_by_fibre: dict[str, dict[str, Any]] = {}
    for entry in fibre_batch["entries"]:
        exact_entry = batch.exact_entry(entry)
        fibre_id = exact_entry["record"]["fibre_id"]
        require(fibre_id not in entries_by_fibre, "fibre_batch: duplicate exact fibre")
        entries_by_fibre[fibre_id] = entry

    assignments: list[dict[str, Any]] = []
    for index, raw in enumerate(raw_assignments):
        require(isinstance(raw, dict), f"slot_assignments[{index}]: expected object")
        exact = exact_assignment(raw)
        require(raw == exact, f"slot_assignments[{index}]: noncanonical assignment")
        assignments.append(exact)
    require(
        assignments == sorted(assignments, key=lambda item: (item["slot_id"], item["fibre_id"])),
        "slot_assignments: canonical order required",
    )
    require(
        len({assignment["slot_id"] for assignment in assignments}) == len(assignments),
        "slot_assignments: duplicate slot",
    )
    require(
        len({assignment["fibre_id"] for assignment in assignments}) == len(assignments),
        "slot_assignments: duplicate fibre",
    )

    expected_slots = {slot["slot_id"]: slot for slot in registry["slots"]}
    label_matches = 0
    population_entries: list[dict[str, Any]] = []
    for index, assignment in enumerate(assignments):
        fibre_id = assignment["fibre_id"]
        slot_id = assignment["slot_id"]
        require(fibre_id in records_by_fibre, f"slot_assignments[{index}]: unknown fibre")
        require(slot_id in expected_slots, f"slot_assignments[{index}]: unexpected slot")
        record = records_by_fibre[fibre_id]
        require(assignment["host_id"] == record["host_id"], f"slot_assignments[{index}]: host mismatch")
        require(
            assignment["source_sha256"] == record["source_sha256"],
            f"slot_assignments[{index}]: source mismatch",
        )
        require(
            expected_slots[slot_id]["expected_host_id"] == record["host_id"],
            f"slot_assignments[{index}]: expected host mismatch",
        )
        linkage = entries_by_fibre[fibre_id]["linked_operation_certificate"]["linkage_certificate"]
        require(
            linkage["state_labels"] == expected_slots[slot_id]["state_labels"],
            f"slot_assignments[{index}]: ordered state-label mismatch",
        )
        label_matches += 1
        population_entries.append(
            {
                "slot_id": slot_id,
                "host_id": record["host_id"],
                "fibre_id": fibre_id,
                "source_sha256": record["source_sha256"],
            }
        )

    require(
        set(records_by_fibre) == {assignment["fibre_id"] for assignment in assignments},
        "slot_assignments: every batch fibre must be assigned exactly once",
    )
    audit = slots.build_population_audit(registry, population_entries)
    audit_summary = slots.validate_population_audit(audit)

    host_counts = Counter(record["host_id"] for record in records_by_fibre.values())
    claims = {
        "expected_slots": registry_summary["slots"],
        "batch_operations": batch_summary["operations"],
        "assignments": len(assignments),
        "covered_slots": audit_summary["covered"],
        "missing_slots": audit_summary["missing"],
        "unexpected_slots": audit_summary["unexpected"],
        "duplicate_slots": audit_summary["duplicates"],
        "host_mismatches": audit_summary["mismatches"],
        "complete": audit_summary["complete"],
        "label_matches": label_matches,
        "unique_hosts": len(host_counts),
        "responses": batch_summary["responses"],
        "primitive_witnesses": batch_summary["witnesses"],
        "strict_improvements": batch_summary["strict"],
        "policy_full_selector_matches": batch_summary["policy_matches"],
        "policy_selector_penalty": batch_summary["policy_penalty"],
        "pareto_vectors": batch_summary["pareto_vectors"],
        "dominated_responses": batch_summary["dominated_responses"],
        "population_audit_sha256": audit["audit_sha256"],
        "assignments_sha256": catalogue.canonical_digest(assignments),
        "batch_records_sha256": batch_exact["claims"]["records_sha256"],
    }
    return {"slot_assignments": assignments, "population_audit": audit, "claims": claims}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    require(certificate.get("slot_assignments") == exact["slot_assignments"], "slot_assignments: incorrect")
    require(certificate.get("population_audit") == exact["population_audit"], "population_audit: incorrect")
    require(certificate.get("claims") == exact["claims"], "claims: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(
        certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
        "certificate_sha256: incorrect",
    )
    claims = exact["claims"]
    return {
        "expected": claims["expected_slots"],
        "operations": claims["batch_operations"],
        "assignments": claims["assignments"],
        "covered": claims["covered_slots"],
        "missing": claims["missing_slots"],
        "complete": claims["complete"],
        "responses": claims["responses"],
        "witnesses": claims["primitive_witnesses"],
        "strict": claims["strict_improvements"],
        "pareto": claims["pareto_vectors"],
    }


def build_certificate(
    registry: dict[str, Any], fibre_batch: dict[str, Any], assignments: list[dict[str, Any]]
) -> dict[str, Any]:
    canonical_assignments = sorted(
        (exact_assignment(assignment) for assignment in assignments),
        key=lambda item: (item["slot_id"], item["fibre_id"]),
    )
    certificate: dict[str, Any] = {
        "version": 1,
        "expected_slot_registry": registry,
        "fibre_batch": fibre_batch,
        "slot_assignments": canonical_assignments,
    }
    exact = exact_certificate(certificate)
    certificate["population_audit"] = exact["population_audit"]
    certificate["claims"] = exact["claims"]
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def synthetic_system(count: int = 60) -> tuple[dict[str, Any], dict[str, Any], list[dict[str, Any]]]:
    random = Random(2126)
    source = catalogue.build_catalogue()
    entries: list[dict[str, Any]] = []
    seen: set[str] = set()
    while len(entries) < count:
        host = random.choice(source["hosts"])
        background = signature.random_background(host["side"], random)
        policy = "canonical-rank3-selector" if len(entries) % 2 == 0 else "declared-response"
        entry = batch.build_entry(host, background, random, policy)
        record = batch.exact_entry(entry)["record"]
        if record["fibre_id"] in seen:
            continue
        seen.add(record["fibre_id"])
        entries.append(entry)
    fibre_batch = batch.build_manifest(entries)

    slot_cores: list[dict[str, Any]] = []
    record_by_fibre = {record["fibre_id"]: record for record in fibre_batch["records"]}
    entry_by_fibre = {
        batch.exact_entry(entry)["record"]["fibre_id"]: entry for entry in fibre_batch["entries"]
    }
    for ordinal, fibre_id in enumerate(sorted(record_by_fibre)):
        record = record_by_fibre[fibre_id]
        linkage = entry_by_fibre[fibre_id]["linked_operation_certificate"]["linkage_certificate"]
        slot_cores.append(
            {
                "parent_state_id": f"synthetic-parent-{ordinal % 12:02d}",
                "operation_kind": "linked-response-operation",
                "operation_key": {"ordinal": ordinal, "policy": record["policy"]},
                "expected_host_id": record["host_id"],
                "state_labels": linkage["state_labels"],
            }
        )
    registry = slots.build_registry(
        "synthetic-slot-batch-conformance-v1",
        {"enumerator": "deterministic-composition-regression", "seed": 2126, "slots": count},
        slot_cores,
    )
    assignments: list[dict[str, Any]] = []
    ordered_fibres = sorted(record_by_fibre)
    for slot in registry["slots"]:
        fibre_id = ordered_fibres[slot["operation_key"]["ordinal"]]
        record = record_by_fibre[fibre_id]
        assignments.append(
            {
                "slot_id": slot["slot_id"],
                "fibre_id": fibre_id,
                "host_id": record["host_id"],
                "source_sha256": record["source_sha256"],
            }
        )
    return registry, fibre_batch, assignments


def run_regressions() -> tuple[dict[str, int], dict[str, int]]:
    registry, fibre_batch, assignments = synthetic_system()
    complete = validate_certificate(build_certificate(registry, fibre_batch, assignments))
    require((complete["expected"], complete["operations"], complete["complete"]) == (60, 60, 1),
            "complete slot/batch regression mismatch")

    partial_assignments = assignments[:-10]
    partial_fibres = {assignment["fibre_id"] for assignment in partial_assignments}
    partial_entries = [
        entry
        for entry in fibre_batch["entries"]
        if batch.exact_entry(entry)["record"]["fibre_id"] in partial_fibres
    ]
    partial_batch = batch.build_manifest(partial_entries)
    partial = validate_certificate(build_certificate(registry, partial_batch, partial_assignments))
    require((partial["operations"], partial["covered"], partial["missing"], partial["complete"]) == (50, 50, 10, 0),
            "partial slot/batch regression mismatch")
    return complete, partial


def run_mutation_tests() -> int:
    registry, fibre_batch, assignments = synthetic_system(6)
    certificate = build_certificate(registry, fibre_batch, assignments)
    validate_certificate(certificate)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(certificate)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data.update(certificate_sha256="0" * 64))
    add(lambda data: data.update(version=2))
    add(lambda data: data["slot_assignments"].reverse())
    add(lambda data: data["slot_assignments"].append(copy.deepcopy(data["slot_assignments"][0])))
    add(lambda data: data["slot_assignments"][0].update(host_id="s4-corrupt"))
    add(lambda data: data["slot_assignments"][0].update(source_sha256="0" * 64))
    add(lambda data: data["slot_assignments"][0].update(fibre_id="unknown-fibre"))
    add(lambda data: data["slot_assignments"][0].update(assignment_sha256="f" * 64))
    add(lambda data: data["population_audit"]["claims"].update(complete=0))
    add(lambda data: data["claims"].update(assignments=999))
    add(lambda data: data["fibre_batch"].update(expected_fibre_ids=[]))
    add(lambda data: data["expected_slot_registry"]["slots"][0]["state_labels"].update(crt="changed"))

    rejected = 0
    for candidate in mutations:
        try:
            validate_certificate(candidate)
        except (
            SlotBatchError,
            slots.SlotRegistryError,
            batch.FibreBatchError,
            catalogue.CatalogueError,
        ):
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted slot/batch certificate accepted")
    return rejected


def main() -> None:
    if len(sys.argv) == 2:
        certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        print(validate_certificate(certificate))
        return
    require(len(sys.argv) == 1, "usage: check_prime_power_slot_fibre_batch_conformance.py [certificate.json]")
    complete, partial = run_regressions()
    rejected = run_mutation_tests()
    print(
        "verified slot/fibre batch conformance: "
        f"complete {complete['operations']}/{complete['expected']} operations with "
        f"{complete['responses']} responses and {complete['witnesses']} witnesses; "
        f"partial {partial['operations']}/{partial['expected']} with {partial['missing']} missing; "
        f"and {rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
