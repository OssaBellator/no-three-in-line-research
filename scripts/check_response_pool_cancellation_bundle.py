#!/usr/bin/env python3
"""Validate exact response-pool destroyed-triple cancellation and coefficient slacks.

Destroyed triples are indistinguishable units of the scalar real-triple potential.
After a response Q is selected, they may pay any deleted witnesses occurring in Q.
The exact required capacity is K=max_Q N_deleted(Q), not the total deleted count and
not a static coloring number.

With one JSON path, validate a certificate. With no argument, run deterministic
mixed, pool-strict, and corruption tests.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from pathlib import Path
from random import Random
from typing import Any

import check_geometric_assignment_bundle as assignment_bundle
import check_geometric_conflict_colored_cancellation as colored
import check_geometric_owner_fate_manifest as owner_fate

Edge = tuple[int, int]
Prescription = tuple[Edge, ...]
Point = tuple[int, int]


class PoolCancellationError(ValueError):
    """Raised when a response-pool cancellation certificate is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise PoolCancellationError(message)


def parse_integer(value: Any, path: str) -> int:
    require(type(value) is int, f"{path}: expected integer")
    return value


def parse_point(value: Any, path: str) -> Point:
    require(isinstance(value, list) and len(value) == 2, f"{path}: expected [x,y]")
    return parse_integer(value[0], f"{path}[0]"), parse_integer(value[1], f"{path}[1]")


def response_contains(response: tuple[Edge, ...], prescription: Prescription) -> bool:
    return set(prescription).issubset(response)


def table_bins(bundle: dict[str, Any]) -> dict[tuple[int, str, Prescription], int]:
    output: dict[tuple[int, str, Prescription], int] = {}
    for rank, name in ((1, "edge"), (2, "pair"), (3, "triple")):
        for entry in bundle["coefficient_table"].get(name, []):
            if rank == 1:
                prescription = (tuple(entry["edge"]),)
            else:
                prescription = tuple(sorted(tuple(edge) for edge in entry["edges"]))
            output[(rank, entry["child"], prescription)] = entry["value"]
    return output


def exact_scores(bundle: dict[str, Any]) -> list[int]:
    source = bundle["source_manifest"]
    responses = owner_fate.perfect_matchings(
        source["side"], {tuple(edge) for edge in source["allowed_edges"]}
    )
    bins = table_bins(bundle)
    return [
        sum(
            value
            for (_rank, _child, prescription), value in bins.items()
            if response_contains(response, prescription)
        )
        for response in responses
    ]


def validate_pool_manifest(manifest: Any) -> dict[str, Any]:
    require(isinstance(manifest, dict), "pool_manifest: expected object")
    require(manifest.get("version") == 1, "pool_manifest.version: expected 1")
    source = manifest.get("source_manifest")
    require(isinstance(source, dict), "pool_manifest.source_manifest: expected object")
    try:
        source_summary = owner_fate.validate_manifest(source)
    except owner_fate.FateError as error:
        raise PoolCancellationError(f"pool_manifest.source_manifest: {error}") from error

    raw_points = manifest.get("pre_response_points")
    require(isinstance(raw_points, list), "pool_manifest.pre_response_points: expected list")
    points = [parse_point(value, f"pool_manifest.pre_response_points[{index}]") for index, value in enumerate(raw_points)]
    require(len(set(points)) == len(points), "pool_manifest.pre_response_points: duplicates")

    raw_removed = manifest.get("removed_point_indices")
    require(isinstance(raw_removed, list), "pool_manifest.removed_point_indices: expected list")
    removed_list = [parse_integer(value, f"pool_manifest.removed_point_indices[{index}]") for index, value in enumerate(raw_removed)]
    removed = set(removed_list)
    require(len(removed) == len(removed_list), "pool_manifest.removed_point_indices: duplicates")
    require(removed, "pool_manifest.removed_point_indices: expected at least one removal")
    require(all(0 <= index < len(points) for index in removed), "pool_manifest.removed_point_indices: out of range")

    surviving = [point for index, point in enumerate(points) if index not in removed]
    source_background = [tuple(point) for point in source["background_points"]]
    require(surviving == source_background, "pool_manifest: surviving points do not equal source background")

    destroyed = colored.destroyed_triples(points, removed)
    deleted = colored.deleted_evidence_and_prescriptions(source)
    responses = owner_fate.perfect_matchings(
        source["side"], {tuple(edge) for edge in source["allowed_edges"]}
    )
    deleted_loads = [
        sum(response_contains(response, prescription) for prescription in deleted.values())
        for response in responses
    ]
    required_capacity = max(deleted_loads, default=0)
    require(required_capacity <= len(destroyed), "pool_manifest: insufficient destroyed-triple capacity")
    unused_credit = len(destroyed) - required_capacity
    injective_saved = len(deleted) - required_capacity

    histogram = Counter(deleted_loads)
    observed_histogram = manifest.get("deleted_load_histogram")
    require(isinstance(observed_histogram, list), "pool_manifest.deleted_load_histogram: expected list")
    parsed_histogram: dict[int, int] = {}
    for index, entry in enumerate(observed_histogram):
        path = f"pool_manifest.deleted_load_histogram[{index}]"
        require(isinstance(entry, list) and len(entry) == 2, f"{path}: expected [load,count]")
        load = parse_integer(entry[0], f"{path}[0]")
        count = parse_integer(entry[1], f"{path}[1]")
        require(load >= 0 and count > 0, f"{path}: invalid nonnegative load/positive count")
        require(load not in parsed_histogram, f"{path}: duplicate load")
        parsed_histogram[load] = count
    require(parsed_histogram == dict(sorted(histogram.items())), "pool_manifest.deleted_load_histogram: incorrect")

    claims = manifest.get("claims")
    require(isinstance(claims, dict), "pool_manifest.claims: expected object")
    expected_claims = {
        "deleted_witnesses": len(deleted),
        "destroyed_triples": len(destroyed),
        "required_capacity": required_capacity,
        "injective_saved_credits": injective_saved,
        "unused_credit": unused_credit,
    }
    for key, expected in expected_claims.items():
        observed = parse_integer(claims.get(key), f"pool_manifest.claims.{key}")
        require(observed == expected, f"pool_manifest.claims.{key}: incorrect")

    exported = source_summary["exported_bins"]
    edges, pairs, triples = owner_fate.extendable_prescriptions(responses)
    expected_witnesses = owner_fate.expected_witnesses(edges, pairs, triples, source_background)
    response_checks = 0
    for response, deleted_occurring in zip(responses, deleted_loads):
        raw_occurring = sum(
            response_contains(response, prescription)
            for rank in (1, 2, 3)
            for _rank, prescription, _witness in expected_witnesses[rank]
        )
        exported_occurring = sum(
            value
            for (_rank, _child, prescription), value in exported.items()
            if response_contains(response, prescription)
        )
        require(deleted_occurring <= required_capacity, "pool_manifest: response exceeds required capacity")
        require(
            raw_occurring - len(destroyed) <= exported_occurring - unused_credit,
            "pool_manifest: responsewise pool cancellation inequality failed",
        )
        response_checks += 1

    return {
        "source": source,
        "responses": len(responses),
        "witnesses": source_summary["witnesses"],
        "deleted": len(deleted),
        "destroyed": len(destroyed),
        "required_capacity": required_capacity,
        "injective_saved_credits": injective_saved,
        "unused_credit": unused_credit,
        "response_checks": response_checks,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "certificate.version: expected 1")
    pool_manifest = certificate.get("pool_manifest")
    geometric_bundle = certificate.get("geometric_bundle")
    colored_manifest = certificate.get("colored_manifest")
    require(isinstance(pool_manifest, dict), "pool_manifest: expected object")
    require(isinstance(geometric_bundle, dict), "geometric_bundle: expected object")
    require(isinstance(colored_manifest, dict), "colored_manifest: expected object")

    pool_summary = validate_pool_manifest(pool_manifest)
    try:
        bundle_summary = assignment_bundle.validate_bundle(geometric_bundle)
    except assignment_bundle.BundleError as error:
        raise PoolCancellationError(f"geometric_bundle: {error}") from error
    try:
        colored_summary = colored.validate_manifest(colored_manifest)
    except colored.ColoredCancellationError as error:
        raise PoolCancellationError(f"colored_manifest: {error}") from error

    source = pool_summary["source"]
    require(source == geometric_bundle["source_manifest"], "certificate: pool/bundle source mismatch")
    require(source == colored_manifest["source_manifest"], "certificate: pool/colored source mismatch")
    require(pool_manifest["pre_response_points"] == colored_manifest["pre_response_points"], "certificate: point-set mismatch")
    require(pool_manifest["removed_point_indices"] == colored_manifest["removed_point_indices"], "certificate: removal-set mismatch")
    require(pool_summary["responses"] == bundle_summary["responses"], "certificate: denominator mismatch")

    scores = exact_scores(geometric_bundle)
    denominator = len(scores)
    exported_numerator = sum(scores)
    maximum_score = max(scores)
    pool_capacity = pool_summary["required_capacity"]
    color_capacity = colored_summary["used_credits"]
    deleted = pool_summary["deleted"]
    destroyed = pool_summary["destroyed"]
    require(pool_capacity <= color_capacity <= deleted, "certificate: capacity dominance failed")

    pool_unused = destroyed - pool_capacity
    color_unused = destroyed - color_capacity
    injective_unused = destroyed - deleted
    color_gain = color_capacity - pool_capacity
    injective_gain = deleted - pool_capacity
    average_slack = denominator * pool_unused - exported_numerator
    uniform_slack = pool_unused - maximum_score
    color_average_slack = denominator * color_unused - exported_numerator
    color_uniform_slack = color_unused - maximum_score
    injective_average_slack = denominator * injective_unused - exported_numerator
    injective_uniform_slack = injective_unused - maximum_score

    require(average_slack == color_average_slack + denominator * color_gain, "certificate: color gain identity failed")
    require(average_slack == injective_average_slack + denominator * injective_gain, "certificate: injective gain identity failed")
    require(uniform_slack == color_uniform_slack + color_gain, "certificate: uniform color gain identity failed")
    require(uniform_slack == injective_uniform_slack + injective_gain, "certificate: uniform injective gain identity failed")

    claims = certificate.get("claims")
    require(isinstance(claims, dict), "claims: expected object")
    expected_claims = {
        "pool_capacity": pool_capacity,
        "color_capacity": color_capacity,
        "deleted_witnesses": deleted,
        "pool_unused_credit": pool_unused,
        "color_unused_credit": color_unused,
        "injective_unused_credit": injective_unused,
        "pool_over_color_saved_credits": color_gain,
        "pool_over_injective_saved_credits": injective_gain,
        "exported_numerator": exported_numerator,
        "maximum_response_score": maximum_score,
        "average_slack": average_slack,
        "uniform_slack": uniform_slack,
        "color_average_slack": color_average_slack,
        "color_uniform_slack": color_uniform_slack,
        "injective_average_slack": injective_average_slack,
        "injective_uniform_slack": injective_uniform_slack,
        "average_strict": int(average_slack > 0),
        "uniform_strict": int(uniform_slack > 0),
        "pool_only_average_strict": int(average_slack > 0 >= color_average_slack),
        "pool_only_uniform_strict": int(uniform_slack > 0 >= color_uniform_slack),
    }
    for key, expected in expected_claims.items():
        observed = parse_integer(claims.get(key), f"claims.{key}")
        require(observed == expected, f"claims.{key}: incorrect")

    return {
        "responses": denominator,
        "witnesses": pool_summary["witnesses"],
        "deleted": deleted,
        "destroyed": destroyed,
        "pool_capacity": pool_capacity,
        "color_capacity": color_capacity,
        "pool_over_color_saved_credits": color_gain,
        "pool_over_injective_saved_credits": injective_gain,
        "pool_unused_credit": pool_unused,
        "coefficient_bins": bundle_summary["coefficient_bins"],
        "coefficient_mass": bundle_summary["coefficient_mass"],
        "exported_numerator": exported_numerator,
        "average_strict": int(average_slack > 0),
        "uniform_strict": int(uniform_slack > 0),
        "pool_only_average_strict": int(average_slack > 0 >= color_average_slack),
        "pool_only_uniform_strict": int(uniform_slack > 0 >= color_uniform_slack),
    }


def make_pool_manifest(colored_manifest: dict[str, Any]) -> dict[str, Any]:
    source = colored_manifest["source_manifest"]
    points = colored_manifest["pre_response_points"]
    removed = colored_manifest["removed_point_indices"]
    parsed_points = [tuple(point) for point in points]
    removed_set = set(removed)
    destroyed = colored.destroyed_triples(parsed_points, removed_set)
    deleted = colored.deleted_evidence_and_prescriptions(source)
    responses = owner_fate.perfect_matchings(
        source["side"], {tuple(edge) for edge in source["allowed_edges"]}
    )
    loads = [
        sum(response_contains(response, prescription) for prescription in deleted.values())
        for response in responses
    ]
    capacity = max(loads, default=0)
    histogram = Counter(loads)
    return {
        "version": 1,
        "source_manifest": source,
        "pre_response_points": copy.deepcopy(points),
        "removed_point_indices": list(removed),
        "deleted_load_histogram": [[load, count] for load, count in sorted(histogram.items())],
        "claims": {
            "deleted_witnesses": len(deleted),
            "destroyed_triples": len(destroyed),
            "required_capacity": capacity,
            "injective_saved_credits": len(deleted) - capacity,
            "unused_credit": len(destroyed) - capacity,
        },
    }


def build_certificate(source: dict[str, Any]) -> dict[str, Any]:
    colored_manifest = colored.build_manifest(source)
    pool_manifest = make_pool_manifest(colored_manifest)
    geometric_bundle = assignment_bundle.build_bundle(source)
    pool_summary = validate_pool_manifest(pool_manifest)
    colored_summary = colored.validate_manifest(colored_manifest)
    scores = exact_scores(geometric_bundle)
    denominator = len(scores)
    numerator = sum(scores)
    maximum = max(scores)
    deleted = pool_summary["deleted"]
    destroyed = pool_summary["destroyed"]
    pool_capacity = pool_summary["required_capacity"]
    color_capacity = colored_summary["used_credits"]
    pool_unused = destroyed - pool_capacity
    color_unused = destroyed - color_capacity
    injective_unused = destroyed - deleted
    average = denominator * pool_unused - numerator
    uniform = pool_unused - maximum
    color_average = denominator * color_unused - numerator
    color_uniform = color_unused - maximum
    injective_average = denominator * injective_unused - numerator
    injective_uniform = injective_unused - maximum
    return {
        "version": 1,
        "pool_manifest": pool_manifest,
        "colored_manifest": colored_manifest,
        "geometric_bundle": geometric_bundle,
        "claims": {
            "pool_capacity": pool_capacity,
            "color_capacity": color_capacity,
            "deleted_witnesses": deleted,
            "pool_unused_credit": pool_unused,
            "color_unused_credit": color_unused,
            "injective_unused_credit": injective_unused,
            "pool_over_color_saved_credits": color_capacity - pool_capacity,
            "pool_over_injective_saved_credits": deleted - pool_capacity,
            "exported_numerator": numerator,
            "maximum_response_score": maximum,
            "average_slack": average,
            "uniform_slack": uniform,
            "color_average_slack": color_average,
            "color_uniform_slack": color_uniform,
            "injective_average_slack": injective_average,
            "injective_uniform_slack": injective_uniform,
            "average_strict": int(average > 0),
            "uniform_strict": int(uniform > 0),
            "pool_only_average_strict": int(average > 0 >= color_average),
            "pool_only_uniform_strict": int(uniform > 0 >= color_uniform),
        },
    }


def make_all_deleted(source: dict[str, Any]) -> dict[str, Any]:
    output = copy.deepcopy(source)
    counter = 0
    for name in ("rank1", "rank2", "rank3"):
        for record in output["fates"][name]:
            record["kind"] = "deleted"
            record.pop("child", None)
            record.pop("multiplicity", None)
            record["evidence"] = f"pool-deletion-{counter:05d}"
            counter += 1
    owner_fate.validate_manifest(output)
    return output


def pool_gap_source(random: Random) -> dict[str, Any]:
    """Construct an actual side-five geometric source with K=2 and chi=3."""
    side = 5
    allowed = {
        (0, 1), (0, 2), (0, 4),
        (1, 1), (1, 3),
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
        (3, 0), (3, 2), (3, 3),
        (4, 1), (4, 2), (4, 3), (4, 4),
    }
    background = [(-2, 6), (9, 5), (-1, 7), (9, -3), (8, -3)]
    source = owner_fate.make_manifest(side, allowed, background, random)

    for name in ("rank1", "rank2", "rank3"):
        for record in source["fates"][name]:
            owner = tuple(record["owner"])
            record["kind"] = "retained"
            record["child"] = f"O_{owner[0]}_{owner[1]}"
            record.pop("evidence", None)
            record.pop("multiplicity", None)

    selected: list[tuple[int, Prescription]] = [
        (2, ((1, 3), (2, 1))),
        (1, ((2, 4),)),
        (3, ((1, 1), (3, 3), (4, 4))),
        (2, ((0, 1), (2, 0))),
        (2, ((1, 1), (3, 0))),
        (2, ((3, 3), (4, 2))),
        (3, ((0, 2), (1, 3), (2, 4))),
        (1, ((4, 2),)),
        (3, ((2, 0), (3, 2), (4, 4))),
    ]
    used_records: set[tuple[int, int]] = set()
    for index, (rank, prescription) in enumerate(selected):
        name = {1: "rank1", 2: "rank2", 3: "rank3"}[rank]
        found = False
        for record_index, record in enumerate(source["fates"][name]):
            if (rank, record_index) in used_records:
                continue
            if rank == 1:
                observed = (tuple(record["response"]),)
            else:
                observed = tuple(sorted(tuple(edge) for edge in record["response"]))
            if observed != prescription:
                continue
            record["kind"] = "deleted"
            record.pop("child", None)
            record.pop("multiplicity", None)
            record["evidence"] = f"pool-gap-{index:02d}"
            used_records.add((rank, record_index))
            found = True
            break
        require(found, f"pool gap generator: missing prescription {prescription}")

    owner_fate.validate_manifest(source)
    return source


def run_random_tests() -> tuple[int, Counter[str]]:
    random = Random(1950)
    totals: Counter[str] = Counter()
    systems = 0
    for _ in range(200):
        certificate = build_certificate(colored.random_source(random))
        summary = validate_certificate(certificate)
        for key in (
            "responses", "witnesses", "deleted", "destroyed", "pool_capacity",
            "color_capacity", "pool_over_color_saved_credits",
            "pool_over_injective_saved_credits", "pool_unused_credit", "coefficient_bins",
            "coefficient_mass", "exported_numerator", "average_strict", "uniform_strict",
            "pool_only_average_strict", "pool_only_uniform_strict",
        ):
            totals[key] += summary[key]
        systems += 1

    for _ in range(100):
        certificate = build_certificate(pool_gap_source(random))
        summary = validate_certificate(certificate)
        require(summary["pool_over_color_saved_credits"] == 1, "pool tests: expected one saved credit beyond coloring")
        for key in (
            "responses", "witnesses", "deleted", "destroyed", "pool_capacity",
            "color_capacity", "pool_over_color_saved_credits",
            "pool_over_injective_saved_credits", "pool_unused_credit", "coefficient_bins",
            "coefficient_mass", "exported_numerator", "average_strict", "uniform_strict",
            "pool_only_average_strict", "pool_only_uniform_strict",
        ):
            totals[key] += summary[key]
        systems += 1

    require(systems == 300, "random tests: wrong system count")
    require(totals["pool_over_color_saved_credits"] > 0, "random tests: expected pool gain")
    return systems, totals


def run_mutation_tests() -> int:
    random = Random(53)
    certificate = build_certificate(colored.random_source(random))
    validate_certificate(certificate)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(certificate)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data["pool_manifest"]["deleted_load_histogram"].pop())
    add(lambda data: data["pool_manifest"]["claims"].update(required_capacity=999))
    add(lambda data: data["claims"].update(pool_capacity=-1))
    add(lambda data: data["claims"].update(pool_over_color_saved_credits=-1))
    add(lambda data: data["claims"].update(pool_only_average_strict=1 - data["claims"]["pool_only_average_strict"]))
    add(lambda data: data["geometric_bundle"].update(denominator=999))
    add(lambda data: data["geometric_bundle"].update(source_sha256="0" * 64))
    add(lambda data: data["colored_manifest"]["credit_assignments"].pop())

    def change_pool_source(data: dict[str, Any]) -> None:
        data["pool_manifest"]["source_manifest"]["entry_order"].reverse()

    add(change_pool_source)

    def change_table(data: dict[str, Any]) -> None:
        table = data["geometric_bundle"]["coefficient_table"]
        for name in ("edge", "pair", "triple"):
            if table[name]:
                table[name][0]["value"] += 1
                return
        raise AssertionError("mutation source unexpectedly has no coefficient")

    add(change_table)

    rejected = 0
    for candidate in mutations:
        try:
            validate_certificate(candidate)
        except PoolCancellationError:
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted certificate accepted")
    return rejected


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit("usage: check_response_pool_cancellation_bundle.py [certificate.json]")
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            certificate = json.load(handle)
        summary = validate_certificate(certificate)
        print(
            "accepted response-pool cancellation bundle: "
            f"pool capacity {summary['pool_capacity']}, color capacity {summary['color_capacity']}, "
            f"{summary['pool_over_color_saved_credits']} extra saved credits, "
            f"pool-only average strict={summary['pool_only_average_strict']} and "
            f"pool-only uniform strict={summary['pool_only_uniform_strict']}"
        )
        return
    systems, totals = run_random_tests()
    rejected = run_mutation_tests()
    print(
        "verified response-pool cancellation bundles: "
        f"{systems} systems, {totals['deleted']} deleted witnesses, "
        f"{totals['pool_over_color_saved_credits']} credits saved beyond coloring, "
        f"{totals['pool_over_injective_saved_credits']} beyond global injection, "
        f"{totals['pool_only_average_strict']} pool-only average-strict and "
        f"{totals['pool_only_uniform_strict']} pool-only uniform-strict systems, "
        f"and {rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
