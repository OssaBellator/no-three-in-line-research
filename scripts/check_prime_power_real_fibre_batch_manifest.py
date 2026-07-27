#!/usr/bin/env python3
"""Validate canonical batches of linked prime-power operation fibres.

Each entry composes three independently validated objects over the same operation:

* a linked literal operation/full-selector certificate;
* a residual survivor-background signature certificate;
* a labelled response-vector/Pareto certificate.

The batch checker enforces fibre uniqueness, canonical ordering, exact cross-object
identity, aggregate census reconstruction, and explicit coverage honesty.  A batch is
complete only relative to an explicitly supplied expected fibre-ID list.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from pathlib import Path
from random import Random
from typing import Any

import check_prime_power_background_residual_signature as residual
import check_prime_power_background_signature as signature
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_labelled_response_pareto as pareto
import check_prime_power_linked_operation_selector as linked


class FibreBatchError(ValueError):
    """Raised when a real-fibre batch manifest is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise FibreBatchError(message)


def exact_entry(entry: dict[str, Any]) -> dict[str, Any]:
    linked_certificate = entry.get("linked_operation_certificate")
    residual_certificate = entry.get("residual_signature_certificate")
    pareto_certificate = entry.get("labelled_pareto_certificate")
    require(isinstance(linked_certificate, dict), "linked_operation_certificate: expected object")
    require(isinstance(residual_certificate, dict), "residual_signature_certificate: expected object")
    require(isinstance(pareto_certificate, dict), "labelled_pareto_certificate: expected object")

    linked_summary = linked.validate_certificate(linked_certificate)
    residual_summary = residual.validate_certificate(residual_certificate)
    pareto_summary = pareto.validate_certificate(pareto_certificate)
    linked_exact = linked.exact_composition(linked_certificate)["claims"]
    residual_exact = residual.exact_certificate(residual_certificate)
    pareto_exact = pareto.exact_records(
        pareto_certificate["geometric_bundle"], pareto_certificate["child_weights"]
    )

    selector_certificate = linked_certificate["background_selector_certificate"]
    direct_bundle = linked_certificate["direct_delta_certificate"]["pool_certificate"][
        "geometric_bundle"
    ]
    require(
        pareto_certificate["geometric_bundle"] == direct_bundle,
        "labelled Pareto bundle differs from linked operation bundle",
    )
    require(
        residual_certificate["host_id"] == selector_certificate["host_id"],
        "residual/linked host mismatch",
    )
    require(
        residual_certificate["catalogue_record_sha256"]
        == selector_certificate["catalogue_record_sha256"],
        "residual/linked catalogue digest mismatch",
    )
    require(
        residual_certificate["background_points"] == selector_certificate["background_points"],
        "residual/linked survivor background mismatch",
    )
    require(
        residual_exact["claims"]["selected_response"] == linked_exact["full_selected_response"],
        "residual selector differs from linked full selector",
    )
    require(
        residual_exact["claims"]["minimum_new_triples"] == linked_exact["minimum_new_triples"],
        "residual minimum differs from linked full minimum",
    )
    require(
        pareto_certificate["geometric_bundle"]["source_sha256"] == linked_exact["source_sha256"],
        "Pareto/source fingerprint mismatch",
    )

    record = {
        "fibre_id": linked_exact["fibre_id"],
        "host_id": linked_exact["host_id"],
        "side": linked_certificate["linkage_certificate"]["source_manifest"]["side"],
        "policy": linked_exact["policy"],
        "source_sha256": linked_exact["source_sha256"],
        "background_signature_sha256": residual_certificate["residual_signature"][
            "residual_signature_sha256"
        ],
        "selector_signature_dimension": residual_certificate["claims"][
            "selector_signature_dimension"
        ],
        "responses": linked_exact["responses"],
        "primitive_witnesses": linked_exact["primitive_witnesses"],
        "background_points": linked_exact["background_points"],
        "destroyed_current_triples": linked_exact["destroyed_current_triples"],
        "minimum_new_triples": linked_exact["minimum_new_triples"],
        "minimum_delta": linked_exact["minimum_delta"],
        "strict_improvement": linked_exact["strict_improvement"],
        "full_selected_response": linked_exact["full_selected_response"],
        "policy_selected_response": linked_exact["policy_selected_response"],
        "policy_selector_penalty": linked_exact["policy_selector_penalty"],
        "policy_is_full_selector": linked_exact["policy_is_full_selector"],
        "residual_pair_mass": residual_exact["claims"]["residual_pair_mass"],
        "tracked_pair_mass": residual_exact["claims"]["tracked_pair_mass"],
        "labelled_children": pareto_exact["claims"]["children"],
        "labelled_unique_vectors": pareto_exact["claims"]["unique_vectors"],
        "labelled_pareto_vectors": pareto_exact["claims"]["pareto_vectors"],
        "labelled_dominated_responses": pareto_exact["claims"]["dominated_responses"],
        "weighted_selected_response": pareto_exact["claims"]["weighted_selected_response"],
        "weighted_selected_is_pareto": pareto_exact["claims"]["weighted_selected_is_pareto"],
        "linked_certificate_sha256": linked_certificate["certificate_sha256"],
        "residual_certificate_sha256": residual_certificate["certificate_sha256"],
        "pareto_certificate_sha256": pareto_certificate["certificate_sha256"],
    }
    require(record["weighted_selected_is_pareto"] == 1, "weighted response lost Pareto status")
    record["record_sha256"] = catalogue.canonical_digest(record)
    return {
        "record": record,
        "linked_summary": linked_summary,
        "residual_summary": residual_summary,
        "pareto_summary": pareto_summary,
    }


def exact_manifest(manifest: dict[str, Any]) -> dict[str, Any]:
    raw_entries = manifest.get("entries")
    require(isinstance(raw_entries, list), "entries: expected list")
    records: list[dict[str, Any]] = []
    for index, entry in enumerate(raw_entries):
        require(isinstance(entry, dict), f"entries[{index}]: expected object")
        records.append(exact_entry(entry)["record"])

    require(records == sorted(records, key=lambda record: record["fibre_id"]),
            "entries: canonical fibre_id order required")
    fibre_ids = [record["fibre_id"] for record in records]
    require(len(fibre_ids) == len(set(fibre_ids)), "entries: duplicate fibre_id")

    expected = manifest.get("expected_fibre_ids")
    if expected is None:
        complete = 0
    else:
        require(isinstance(expected, list), "expected_fibre_ids: expected list or null")
        require(expected == sorted(expected), "expected_fibre_ids: sorted order required")
        require(len(expected) == len(set(expected)), "expected_fibre_ids: duplicates")
        require(fibre_ids == expected, "entries do not exactly cover expected_fibre_ids")
        complete = 1

    side_distribution = Counter(record["side"] for record in records)
    policy_distribution = Counter(record["policy"] for record in records)
    host_distribution = Counter(record["host_id"] for record in records)
    selector_dimension_distribution = Counter(
        record["selector_signature_dimension"] for record in records
    )
    claims = {
        "operations": len(records),
        "unique_fibres": len(fibre_ids),
        "unique_hosts": len(host_distribution),
        "complete_relative_to_expected_ids": complete,
        "responses": sum(record["responses"] for record in records),
        "primitive_witnesses": sum(record["primitive_witnesses"] for record in records),
        "background_points": sum(record["background_points"] for record in records),
        "destroyed_current_triples": sum(record["destroyed_current_triples"] for record in records),
        "strict_improvements": sum(record["strict_improvement"] for record in records),
        "policy_full_selector_matches": sum(record["policy_is_full_selector"] for record in records),
        "policy_selector_penalty": sum(record["policy_selector_penalty"] for record in records),
        "residual_pair_mass": sum(record["residual_pair_mass"] for record in records),
        "tracked_pair_mass": sum(record["tracked_pair_mass"] for record in records),
        "labelled_unique_vectors": sum(record["labelled_unique_vectors"] for record in records),
        "labelled_pareto_vectors": sum(record["labelled_pareto_vectors"] for record in records),
        "labelled_dominated_responses": sum(
            record["labelled_dominated_responses"] for record in records
        ),
        "side_distribution": [[key, side_distribution[key]] for key in sorted(side_distribution)],
        "policy_distribution": [[key, policy_distribution[key]] for key in sorted(policy_distribution)],
        "selector_dimension_distribution": [
            [key, selector_dimension_distribution[key]]
            for key in sorted(selector_dimension_distribution)
        ],
        "host_multiplicity_distribution": [
            [multiplicity, sum(value == multiplicity for value in host_distribution.values())]
            for multiplicity in sorted(set(host_distribution.values()))
        ],
        "records_sha256": catalogue.canonical_digest(records),
    }
    return {"records": records, "claims": claims}


def validate_manifest(manifest: Any) -> dict[str, int]:
    require(isinstance(manifest, dict), "manifest: expected object")
    require(manifest.get("version") == 1, "version: expected 1")
    exact = exact_manifest(manifest)
    require(manifest.get("records") == exact["records"], "records: incorrect")
    require(manifest.get("claims") == exact["claims"], "claims: incorrect")
    payload = {key: value for key, value in manifest.items() if key != "batch_sha256"}
    require(manifest.get("batch_sha256") == catalogue.canonical_digest(payload),
            "batch_sha256: incorrect")
    claims = exact["claims"]
    return {
        "operations": claims["operations"],
        "responses": claims["responses"],
        "witnesses": claims["primitive_witnesses"],
        "strict": claims["strict_improvements"],
        "policy_matches": claims["policy_full_selector_matches"],
        "policy_penalty": claims["policy_selector_penalty"],
        "pareto_vectors": claims["labelled_pareto_vectors"],
        "dominated_responses": claims["labelled_dominated_responses"],
        "complete": claims["complete_relative_to_expected_ids"],
    }


def build_entry(
    host: dict[str, Any], background: list[tuple[int, int]], random: Random, policy: str
) -> dict[str, Any]:
    linked_certificate = linked.build_certificate(host, background, random, policy)
    residual_certificate = residual.build_certificate(host, background)
    bundle = linked_certificate["direct_delta_certificate"]["pool_certificate"][
        "geometric_bundle"
    ]
    weights = pareto.random_weights(bundle, random)
    pareto_certificate = pareto.build_certificate(bundle, weights)
    return {
        "linked_operation_certificate": linked_certificate,
        "residual_signature_certificate": residual_certificate,
        "labelled_pareto_certificate": pareto_certificate,
    }


def build_manifest(
    entries: list[dict[str, Any]], expected_fibre_ids: list[str] | None = None
) -> dict[str, Any]:
    entries = sorted(entries, key=lambda entry: exact_entry(entry)["record"]["fibre_id"])
    manifest: dict[str, Any] = {
        "version": 1,
        "expected_fibre_ids": expected_fibre_ids,
        "entries": entries,
    }
    exact = exact_manifest(manifest)
    manifest["records"] = exact["records"]
    manifest["claims"] = exact["claims"]
    manifest["batch_sha256"] = catalogue.canonical_digest(manifest)
    return manifest


def run_random_tests() -> tuple[int, Counter[str]]:
    random = Random(2086)
    source = catalogue.build_catalogue()
    entries: list[dict[str, Any]] = []
    seen: set[str] = set()
    while len(entries) < 120:
        host = random.choice(source["hosts"])
        background = signature.random_background(host["side"], random)
        policy = "canonical-rank3-selector" if len(entries) % 2 == 0 else "declared-response"
        entry = build_entry(host, background, random, policy)
        fibre_id = entry["linked_operation_certificate"]["claims"]["fibre_id"]
        if fibre_id in seen:
            continue
        seen.add(fibre_id)
        entries.append(entry)
    manifest = build_manifest(entries)
    summary = validate_manifest(manifest)
    require(summary["operations"] == 120, "random tests: wrong operation count")
    require(summary["complete"] == 0, "random tests: undeclared batch became complete")
    expected = [record["fibre_id"] for record in manifest["records"]]
    complete_manifest = build_manifest(entries, expected)
    complete_summary = validate_manifest(complete_manifest)
    require(complete_summary["complete"] == 1, "random tests: declared coverage not recognized")
    return 120, Counter(summary)


def run_mutation_tests() -> int:
    random = Random(109)
    source = catalogue.build_catalogue()
    entries = [
        build_entry(
            source["hosts"][index],
            signature.random_background(source["hosts"][index]["side"], random),
            random,
            "canonical-rank3-selector",
        )
        for index in (10, 20, 30)
    ]
    manifest = build_manifest(entries)
    validate_manifest(manifest)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(manifest)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data.update(batch_sha256="0" * 64))
    add(lambda data: data.update(version=2))
    add(lambda data: data["entries"].reverse())
    add(lambda data: data["entries"].append(copy.deepcopy(data["entries"][0])))
    add(lambda data: data["records"].pop())
    add(lambda data: data["claims"].update(operations=999))
    add(lambda data: data.update(expected_fibre_ids=[]))
    add(lambda data: data["entries"][0]["linked_operation_certificate"].update(host_id="s4-corrupt"))
    add(lambda data: data["entries"][0]["residual_signature_certificate"].update(host_id="s5-corrupt"))
    add(lambda data: data["entries"][0]["labelled_pareto_certificate"]["claims"].update(pareto_vectors=999))
    add(lambda data: data["records"][0].update(policy_selector_penalty=-1))
    add(lambda data: data["claims"]["side_distribution"].append([99, 1]))

    rejected = 0
    for candidate in mutations:
        try:
            validate_manifest(candidate)
        except ValueError:
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted batch accepted")
    return rejected


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit("usage: check_prime_power_real_fibre_batch_manifest.py [batch.json]")
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            manifest = json.load(handle)
        summary = validate_manifest(manifest)
        print(
            "accepted real-fibre batch manifest: "
            f"{summary['operations']} operations, {summary['responses']} responses, "
            f"complete={summary['complete']}"
        )
        return
    systems, totals = run_random_tests()
    rejected = run_mutation_tests()
    print(
        "verified real-fibre batch manifests: "
        f"{systems} operations, {totals['responses']} responses, {totals['witnesses']} witnesses, "
        f"{totals['strict']} strict selectors, {totals['pareto_vectors']} Pareto vectors, "
        f"{totals['dominated_responses']} dominated responses, and {rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
