#!/usr/bin/env python3
"""Validate complete exceptional-selector tradeoffs inside a slot-covered fibre batch.

The input is one complete slot/fibre batch-conformance certificate and one exact selector-
tradeoff certificate for every populated exceptional fibre. The checker identifies the
exceptional fibres from the canonical host catalogue, requires exact fibre/background/
destroyed-threshold linkage, reconstructs every policy penalty and certifies that no
exceptional fibre in the covered batch is omitted or duplicated.

Completeness remains relative to the supplied expected slot registry. Passing this
checker does not prove that the registry is the genuine exhaustive parent rule, nor does
scalar threshold improvement prove labelled recurrent contraction.
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
import check_prime_power_exceptional_selector_chamber_worklist as worklist
import check_prime_power_exceptional_selector_tradeoff as tradeoff
import check_prime_power_operation_slot_registry as slots
import check_prime_power_real_fibre_batch_manifest as batch
import check_prime_power_slot_fibre_batch_conformance as conformance


class ExceptionalBatchError(ValueError):
    """Raised when an exceptional-fibre tradeoff batch is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ExceptionalBatchError(message)


def exact_entry(raw: dict[str, Any], fibre_entries: dict[str, dict[str, Any]],
                exceptional_hosts: set[str]) -> dict[str, Any]:
    fibre_id = raw.get("fibre_id")
    certificate = raw.get("tradeoff_certificate")
    require(isinstance(fibre_id, str) and fibre_id in fibre_entries, "tradeoff entry: unknown fibre")
    require(isinstance(certificate, dict), "tradeoff entry: certificate expected")
    tradeoff.validate_certificate(certificate)
    batch_entry = fibre_entries[fibre_id]
    linked_certificate = batch_entry["linked_operation_certificate"]
    linked_claims = linked_certificate["claims"]
    source = linked_certificate["linkage_certificate"]["source_manifest"]
    host_id = linked_claims["host_id"]
    require(host_id in exceptional_hosts, "tradeoff entry: host is not exceptional")
    require(certificate["host_id"] == host_id, "tradeoff entry: host mismatch")
    require(certificate["background_points"] == source["background_points"],
            "tradeoff entry: survivor background mismatch")
    require(certificate["destroyed_current_triples"] == linked_claims["destroyed_current_triples"],
            "tradeoff entry: destroyed threshold mismatch")
    require(certificate["background_selector_certificate"] == linked_certificate["background_selector_certificate"],
            "tradeoff entry: selector certificate differs from linked operation")
    claims = certificate["claims"]
    output = {
        "fibre_id": fibre_id, "host_id": host_id, "side": claims["side"],
        "worklist_kind": claims["worklist_kind"], "responses": claims["responses"],
        "background_points": claims["background_points"],
        "destroyed_current_triples": claims["destroyed_current_triples"],
        "full_minimum_new_triples": claims["full_minimum_new_triples"],
        "full_minimum_delta": claims["full_minimum_delta"],
        "full_strict_improvement": claims["full_strict_improvement"],
        "rank3_minimum": claims["rank3_minimum"],
        "rank3_constrained_minimum_new_triples": claims["rank3_constrained_minimum_new_triples"],
        "rank3_constrained_strict_improvement": claims["rank3_constrained_strict_improvement"],
        "rank3_constraint_penalty": claims["rank3_constraint_penalty"],
        "zero_rank3_available": claims["zero_rank3_available"],
        "zero_constrained_minimum_new_triples": claims["zero_constrained_minimum_new_triples"],
        "zero_constrained_strict_improvement": claims["zero_constrained_strict_improvement"],
        "zero_constraint_penalty": claims["zero_constraint_penalty"],
        "full_selected_rank3_triples": claims["full_selected_rank3_triples"],
        "tradeoff_certificate_sha256": certificate["certificate_sha256"],
        "linked_operation_sha256": linked_certificate["certificate_sha256"],
    }
    output["exceptional_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    conformance_certificate = certificate.get("slot_batch_conformance_certificate")
    raw_entries = certificate.get("exceptional_tradeoff_entries")
    require(isinstance(conformance_certificate, dict), "slot_batch_conformance_certificate: expected object")
    require(isinstance(raw_entries, list), "exceptional_tradeoff_entries: expected list")
    conformance_summary = conformance.validate_certificate(conformance_certificate)
    require(conformance_summary["complete"] == 1,
            "slot-covered batch must be complete relative to its supplied registry")
    fibre_batch = conformance_certificate["fibre_batch"]
    batch.validate_manifest(fibre_batch)
    batch_exact = batch.exact_manifest(fibre_batch)
    fibre_entries = {batch.exact_entry(entry)["record"]["fibre_id"]: entry for entry in fibre_batch["entries"]}
    exceptional_records = worklist.build_worklist()["hosts"]
    exceptional_hosts = {record["host_id"] for record in exceptional_records}
    host_kind = {record["host_id"]: record["worklist_kind"] for record in exceptional_records}
    expected_fibres = sorted(record["fibre_id"] for record in batch_exact["records"]
                             if record["host_id"] in exceptional_hosts)

    canonical_entries = []
    records = []
    for raw in raw_entries:
        require(isinstance(raw, dict), "exceptional tradeoff entry: expected object")
        record = exact_entry(raw, fibre_entries, exceptional_hosts)
        core = {"fibre_id": raw.get("fibre_id"), "tradeoff_certificate": raw.get("tradeoff_certificate"),
                "record": record}
        core["entry_sha256"] = catalogue.canonical_digest(core)
        require(raw == core, "exceptional_tradeoff_entries: canonical record or digest mismatch")
        canonical_entries.append(core)
        records.append(record)
    require(canonical_entries == sorted(canonical_entries, key=lambda record: record["fibre_id"]),
            "exceptional_tradeoff_entries: canonical fibre order required")
    entry_fibres = [record["fibre_id"] for record in records]
    require(entry_fibres == expected_fibres,
            "exceptional tradeoff entries do not exactly cover exceptional fibres")
    require(len(entry_fibres) == len(set(entry_fibres)), "exceptional tradeoff entries: duplicate fibre")
    require(all(record["worklist_kind"] == host_kind[record["host_id"]] for record in records),
            "worklist kind mismatch")
    require(all(record["rank3_constrained_strict_improvement"] <= record["full_strict_improvement"]
                for record in records), "rank3 strictness hierarchy failed")
    require(all(int(record["zero_constrained_strict_improvement"] or 0) <= record["full_strict_improvement"]
                for record in records), "zero strictness hierarchy failed")

    host_counts = Counter(record["host_id"] for record in records)
    rank3_penalties = Counter(record["rank3_constraint_penalty"] for record in records)
    zero_penalties = Counter(record["zero_constraint_penalty"] for record in records
                             if record["zero_rank3_available"])
    selected_rank3 = Counter(record["full_selected_rank3_triples"] for record in records)
    claims = {
        "covered_slots": conformance_summary["covered"],
        "batch_operations": conformance_summary["operations"],
        "exceptional_fibres": len(records),
        "unique_exceptional_hosts": len(host_counts),
        "zero_capable_fibres": sum(record["zero_rank3_available"] for record in records),
        "hard_core_fibres": sum(record["worklist_kind"] == "positive-minimum-hard-core" for record in records),
        "responses": sum(record["responses"] for record in records),
        "background_points": sum(record["background_points"] for record in records),
        "destroyed_current_triples": sum(record["destroyed_current_triples"] for record in records),
        "full_strict_improvements": sum(record["full_strict_improvement"] for record in records),
        "rank3_constrained_strict_improvements": sum(record["rank3_constrained_strict_improvement"]
                                                      for record in records),
        "zero_constrained_strict_improvements": sum(int(record["zero_constrained_strict_improvement"] or 0)
                                                     for record in records),
        "total_rank3_constraint_penalty": sum(record["rank3_constraint_penalty"] for record in records),
        "total_zero_constraint_penalty": sum(int(record["zero_constraint_penalty"] or 0)
                                             for record in records),
        "rank3_penalty_distribution": [[key, rank3_penalties[key]] for key in sorted(rank3_penalties)],
        "zero_penalty_distribution": [[key, zero_penalties[key]] for key in sorted(zero_penalties)],
        "full_selected_rank3_distribution": [[key, selected_rank3[key]] for key in sorted(selected_rank3)],
        "host_multiplicity_distribution": [
            [multiplicity, sum(count == multiplicity for count in host_counts.values())]
            for multiplicity in sorted(set(host_counts.values()))],
        "exceptional_records_sha256": catalogue.canonical_digest(records),
        "slot_batch_conformance_sha256": conformance_certificate["certificate_sha256"],
    }
    return {"records": records, "claims": claims}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    require(certificate.get("records") == exact["records"], "records: incorrect")
    require(certificate.get("claims") == exact["claims"], "claims: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {"operations": claims["batch_operations"], "exceptional": claims["exceptional_fibres"],
            "hosts": claims["unique_exceptional_hosts"], "zero_capable": claims["zero_capable_fibres"],
            "hard_core": claims["hard_core_fibres"], "responses": claims["responses"],
            "destroyed": claims["destroyed_current_triples"], "full_strict": claims["full_strict_improvements"],
            "rank3_strict": claims["rank3_constrained_strict_improvements"],
            "zero_strict": claims["zero_constrained_strict_improvements"],
            "rank3_penalty": claims["total_rank3_constraint_penalty"],
            "zero_penalty": claims["total_zero_constraint_penalty"]}


def build_certificate(conformance_certificate: dict[str, Any],
                      tradeoff_certificates: dict[str, dict[str, Any]]) -> dict[str, Any]:
    fibre_batch = conformance_certificate["fibre_batch"]
    fibre_entries = {batch.exact_entry(entry)["record"]["fibre_id"]: entry for entry in fibre_batch["entries"]}
    entries = []
    for fibre_id in sorted(tradeoff_certificates):
        core = {"fibre_id": fibre_id, "tradeoff_certificate": tradeoff_certificates[fibre_id]}
        core["record"] = exact_entry(core, fibre_entries, {tradeoff_certificates[fibre_id]["host_id"]})
        core["entry_sha256"] = catalogue.canonical_digest(core)
        entries.append(core)
    certificate: dict[str, Any] = {"version": 1,
        "slot_batch_conformance_certificate": conformance_certificate,
        "exceptional_tradeoff_entries": entries}
    exact = exact_certificate(certificate)
    certificate["records"] = exact["records"]
    certificate["claims"] = exact["claims"]
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def synthetic_certificate(random: Random) -> dict[str, Any]:
    host_records = catalogue.build_catalogue()["hosts"]
    exceptional = worklist.build_worklist()["hosts"]
    exceptional_hosts = [next(host for host in host_records if host["host_id"] == record["host_id"])
                         for record in exceptional]
    fibre_entries = []
    seen = set()
    while len(fibre_entries) < 36:
        host = random.choice(exceptional_hosts)
        entry = batch.build_entry(host, signature.random_background(host["side"], random),
                                  random, "canonical-rank3-selector")
        fibre_id = batch.exact_entry(entry)["record"]["fibre_id"]
        if fibre_id not in seen:
            seen.add(fibre_id); fibre_entries.append(entry)
    fibre_batch = batch.build_manifest(fibre_entries)
    slot_cores = []
    for index, entry in enumerate(fibre_batch["entries"]):
        exact = batch.exact_entry(entry)["record"]
        linkage = entry["linked_operation_certificate"]["linkage_certificate"]
        slot_cores.append({
            "parent_state_id": f"exceptional-parent-{index:03d}",
            "operation_kind": "exceptional-selector-operation",
            "operation_key": {"ordinal": index, "fibre_prefix": exact["fibre_id"][:16]},
            "expected_host_id": exact["host_id"], "state_labels": linkage["state_labels"]})
    registry = slots.build_registry("synthetic-exceptional-covered-batch-v1",
        {"enumerator": "deterministic-exceptional-regression", "seed": 2182,
         "operations": len(slot_cores)}, slot_cores)
    assignments = []
    for slot_record in registry["slots"]:
        entry = fibre_batch["entries"][slot_record["operation_key"]["ordinal"]]
        exact = batch.exact_entry(entry)["record"]
        assignments.append({"slot_id": slot_record["slot_id"], "fibre_id": exact["fibre_id"],
                            "host_id": exact["host_id"], "source_sha256": exact["source_sha256"]})
    conformance_certificate = conformance.build_certificate(registry, fibre_batch, assignments)
    require(conformance.validate_certificate(conformance_certificate)["complete"] == 1,
            "synthetic conformance incomplete")
    tradeoffs = {}
    for entry in fibre_batch["entries"]:
        exact = batch.exact_entry(entry)["record"]
        linked_certificate = entry["linked_operation_certificate"]
        host = next(host for host in host_records if host["host_id"] == exact["host_id"])
        background = [tuple(point) for point in linked_certificate["linkage_certificate"]["source_manifest"]["background_points"]]
        tradeoffs[exact["fibre_id"]] = tradeoff.build_certificate(
            host, background, linked_certificate["claims"]["destroyed_current_triples"])
    return build_certificate(conformance_certificate, tradeoffs)


def run_random_tests() -> tuple[int, Counter[str]]:
    random = Random(2182); totals: Counter[str] = Counter()
    for _ in range(4): totals.update(validate_certificate(synthetic_certificate(random)))
    return 4, totals


def run_mutation_tests() -> int:
    random = Random(181); certificate = synthetic_certificate(random); validate_certificate(certificate)
    mutations = []
    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(certificate); mutator(candidate); mutations.append(candidate)
    add(lambda data: data.update(certificate_sha256="0" * 64))
    add(lambda data: data.update(version=2))
    add(lambda data: data["exceptional_tradeoff_entries"].reverse())
    add(lambda data: data["exceptional_tradeoff_entries"].pop())
    add(lambda data: data["exceptional_tradeoff_entries"].append(copy.deepcopy(data["exceptional_tradeoff_entries"][0])))
    add(lambda data: data["records"].pop())
    add(lambda data: data["claims"].update(exceptional_fibres=999))
    add(lambda data: data["slot_batch_conformance_certificate"].update(certificate_sha256="0" * 64))
    add(lambda data: data["exceptional_tradeoff_entries"][0]["tradeoff_certificate"].update(host_id="s4-corrupt"))
    add(lambda data: data["exceptional_tradeoff_entries"][0]["tradeoff_certificate"].update(destroyed_current_triples=999))
    add(lambda data: data["exceptional_tradeoff_entries"][0].update(entry_sha256="f" * 64))
    add(lambda data: data["exceptional_tradeoff_entries"][0]["record"].update(full_minimum_delta=999))
    rejected = 0
    for candidate in mutations:
        try: validate_certificate(candidate)
        except (ExceptionalBatchError, tradeoff.TradeoffError, conformance.SlotBatchError,
                batch.FibreBatchError, slots.SlotRegistryError, catalogue.CatalogueError): rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted exceptional batch accepted")
    return rejected


def main() -> None:
    if len(sys.argv) == 2:
        print(validate_certificate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))); return
    require(len(sys.argv) == 1,
            "usage: check_prime_power_exceptional_fibre_tradeoff_batch.py [certificate.json]")
    systems, totals = run_random_tests(); rejected = run_mutation_tests()
    print("verified exceptional-fibre tradeoff batches: "
          f"{systems} slot-covered batches, {totals['operations']} operations, {totals['exceptional']} exceptional fibres, "
          f"{totals['hosts']} represented hosts, {totals['responses']} responses, {totals['destroyed']} destroyed triples, "
          f"strict counts {totals['full_strict']}/{totals['rank3_strict']}/{totals['zero_strict']}, "
          f"constraint penalties {totals['rank3_penalty']}/{totals['zero_penalty']}, and {rejected} corruptions rejected")


if __name__ == "__main__": main()
