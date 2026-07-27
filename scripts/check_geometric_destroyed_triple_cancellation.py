#!/usr/bin/env python3
"""Validate destroyed-triple cancellation evidence for deleted geometric witnesses.

A manifest contains one complete geometric owner/fate source, the exact point set
before removal, the removed point indices, and an injective cancellation map from
every deleted primitive witness to one current collinear triple destroyed by that
removal.

With one JSON path, validate that manifest. With no argument, run deterministic
random systems, responsewise inequalities, and corruption tests.
"""

from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from itertools import combinations
from math import comb
from pathlib import Path
from random import Random
from typing import Any

import check_geometric_owner_fate_manifest as owner_fate

Point = tuple[int, int]
Edge = tuple[int, int]
Prescription = tuple[Edge, ...]


class CancellationError(ValueError):
    """Raised when destroyed-triple cancellation evidence is invalid."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CancellationError(message)


def parse_integer(value: Any, path: str) -> int:
    require(type(value) is int, f"{path}: expected integer")
    return value


def parse_point(value: Any, path: str) -> Point:
    require(isinstance(value, list) and len(value) == 2, f"{path}: expected [x,y]")
    return parse_integer(value[0], f"{path}[0]"), parse_integer(value[1], f"{path}[1]")


def collinear(first: Point, second: Point, third: Point) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def deleted_evidence_and_prescriptions(
    source: dict[str, Any],
) -> dict[str, Prescription]:
    output: dict[str, Prescription] = {}
    side = source["side"]
    for rank, name in ((1, "rank1"), (2, "rank2"), (3, "rank3")):
        records = source["fates"].get(name, [])
        for index, record in enumerate(records):
            if record.get("kind") != "deleted":
                continue
            evidence = record.get("evidence")
            path = f"source_manifest.fates.{name}[{index}].evidence"
            require(isinstance(evidence, str) and evidence, f"{path}: required")
            require(evidence not in output, f"{path}: deletion evidence must be unique")
            if rank == 1:
                prescription = (
                    owner_fate.parse_edge(record["response"], f"{path}.response", side),
                )
            else:
                prescription = tuple(
                    sorted(
                        owner_fate.parse_edge(edge, f"{path}.response", side)
                        for edge in record["response"]
                    )
                )
            output[evidence] = prescription
    return output


def destroyed_triples(
    points: list[Point], removed: set[int]
) -> set[tuple[int, int, int]]:
    return {
        triple
        for triple in combinations(range(len(points)), 3)
        if removed.intersection(triple)
        and collinear(points[triple[0]], points[triple[1]], points[triple[2]])
    }


def response_contains(response: tuple[Edge, ...], prescription: Prescription) -> bool:
    response_set = set(response)
    return all(edge in response_set for edge in prescription)


def validate_manifest(manifest: Any, *, check_responses: bool = True) -> dict[str, int]:
    require(isinstance(manifest, dict), "manifest: expected object")
    require(manifest.get("version") == 1, "version: expected 1")
    source = manifest.get("source_manifest")
    require(isinstance(source, dict), "source_manifest: expected object")
    try:
        source_summary = owner_fate.validate_manifest(source)
    except owner_fate.FateError as error:
        raise CancellationError(f"source_manifest: {error}") from error

    raw_points = manifest.get("pre_response_points")
    require(isinstance(raw_points, list), "pre_response_points: expected list")
    points = [
        parse_point(value, f"pre_response_points[{index}]")
        for index, value in enumerate(raw_points)
    ]
    require(len(set(points)) == len(points), "pre_response_points: duplicates")

    raw_removed = manifest.get("removed_point_indices")
    require(isinstance(raw_removed, list), "removed_point_indices: expected list")
    removed_list = [
        parse_integer(value, f"removed_point_indices[{index}]")
        for index, value in enumerate(raw_removed)
    ]
    removed = set(removed_list)
    require(len(removed) == len(removed_list), "removed_point_indices: duplicates")
    require(
        all(0 <= index < len(points) for index in removed),
        "removed_point_indices: out of range",
    )
    require(removed, "removed_point_indices: expected at least one removal")

    surviving = [point for index, point in enumerate(points) if index not in removed]
    source_background = [tuple(point) for point in source["background_points"]]
    require(
        surviving == source_background,
        "surviving points must equal source background_points in order",
    )

    available_destroyed = destroyed_triples(points, removed)
    deleted = deleted_evidence_and_prescriptions(source)

    records = manifest.get("cancellations")
    require(isinstance(records, list), "cancellations: expected list")
    observed_evidence: set[str] = set()
    used_triples: set[tuple[int, int, int]] = set()
    for index, record in enumerate(records):
        path = f"cancellations[{index}]"
        require(isinstance(record, dict), f"{path}: expected object")
        evidence = record.get("evidence")
        require(isinstance(evidence, str) and evidence, f"{path}.evidence: required")
        require(evidence in deleted, f"{path}.evidence: unknown deleted witness")
        require(evidence not in observed_evidence, f"{path}.evidence: duplicate")
        observed_evidence.add(evidence)

        raw_triple = record.get("destroyed_triple")
        require(
            isinstance(raw_triple, list) and len(raw_triple) == 3,
            f"{path}.destroyed_triple: expected three indices",
        )
        triple = tuple(
            parse_integer(value, f"{path}.destroyed_triple[{entry}]")
            for entry, value in enumerate(raw_triple)
        )
        require(tuple(sorted(triple)) == triple, f"{path}.destroyed_triple: sort indices")
        require(len(set(triple)) == 3, f"{path}.destroyed_triple: duplicate index")
        require(
            all(0 <= point_index < len(points) for point_index in triple),
            f"{path}.destroyed_triple: index out of range",
        )
        require(triple in available_destroyed, f"{path}: not a destroyed collinear triple")
        require(triple not in used_triples, f"{path}: destroyed triple credit reused")
        used_triples.add(triple)

    require(
        observed_evidence == set(deleted),
        "cancellations: omitted or extraneous deletion evidence",
    )

    unused_credit = len(available_destroyed) - len(used_triples)
    response_checks = 0
    if check_responses:
        side = source["side"]
        allowed = {tuple(edge) for edge in source["allowed_edges"]}
        responses = owner_fate.perfect_matchings(side, allowed)
        exported = source_summary["exported_bins"]
        deleted_prescriptions = tuple(deleted.values())
        destroyed_count = len(available_destroyed)
        edges, pairs, triples = owner_fate.extendable_prescriptions(responses)
        background = [tuple(point) for point in source["background_points"]]
        expected = owner_fate.expected_witnesses(edges, pairs, triples, background)

        for response in responses:
            deleted_occurring = sum(
                response_contains(response, prescription)
                for prescription in deleted_prescriptions
            )
            exported_occurring = sum(
                value
                for (_rank, _child, prescription), value in exported.items()
                if response_contains(response, prescription)
            )
            raw_occurring = sum(
                response_contains(response, prescription)
                for rank in (1, 2, 3)
                for _rank, prescription, _witness in expected[rank]
            )

            require(
                raw_occurring - destroyed_count
                <= exported_occurring - unused_credit,
                "responsewise cancellation inequality failed",
            )
            require(
                deleted_occurring <= len(used_triples),
                "deleted witness cancellation capacity failed",
            )
            response_checks += 1

    return {
        "responses": source_summary["responses"],
        "witnesses": source_summary["witnesses"],
        "deleted": len(deleted),
        "destroyed": len(available_destroyed),
        "reserved": len(used_triples),
        "unused_credit": unused_credit,
        "response_checks": response_checks,
    }


def make_manifest(source: dict[str, Any]) -> dict[str, Any]:
    counter = 0
    for name in ("rank1", "rank2", "rank3"):
        for record in source["fates"][name]:
            if record["kind"] == "deleted":
                record["evidence"] = f"destroyed-credit-{counter:05d}"
                counter += 1

    background = [tuple(point) for point in source["background_points"]]
    removed_count = 3
    while comb(removed_count, 3) < counter:
        removed_count += 1
    removed_points = [(10000 + index, 20000) for index in range(removed_count)]
    points = background + removed_points
    removed = set(range(len(background), len(points)))
    credits = sorted(destroyed_triples(points, removed))
    require(len(credits) >= counter, "internal generator: insufficient credits")

    deleted = deleted_evidence_and_prescriptions(source)
    return {
        "version": 1,
        "source_manifest": source,
        "pre_response_points": [list(point) for point in points],
        "removed_point_indices": sorted(removed),
        "cancellations": [
            {
                "evidence": evidence,
                "destroyed_triple": list(triple),
            }
            for evidence, triple in zip(sorted(deleted), credits)
        ],
    }


def random_source(random: Random) -> dict[str, Any]:
    side = random.randint(3, 5)
    permutation = list(range(side))
    random.shuffle(permutation)
    allowed = {(left, permutation[left]) for left in range(side)}
    for left in range(side):
        for right in range(side):
            if random.random() < 0.56:
                allowed.add((left, right))
    grid = {(left, right) for left in range(side) for right in range(side)}
    background: list[Point] = []
    target_size = random.randint(3, 7)
    while len(background) < target_size:
        point = (
            random.randint(-4, side + 3),
            random.randint(-4, side + 3),
        )
        if point not in grid and point not in background:
            background.append(point)
    return owner_fate.make_manifest(side, allowed, background, random)


def run_random_tests() -> tuple[int, Counter[str]]:
    random = Random(1918)
    totals: Counter[str] = Counter()
    systems = 0
    for _ in range(300):
        manifest = make_manifest(random_source(random))
        summary = validate_manifest(manifest)
        for key in (
            "responses",
            "witnesses",
            "deleted",
            "destroyed",
            "reserved",
            "unused_credit",
            "response_checks",
        ):
            totals[key] += summary[key]
        systems += 1
    require(systems == 300, "random tests: wrong system count")
    require(
        totals
        == Counter(
            {
                "witnesses": 3761,
                "responses": 2310,
                "response_checks": 2310,
                "destroyed": 1304,
                "deleted": 832,
                "reserved": 832,
                "unused_credit": 472,
            }
        ),
        "random tests: unexpected totals",
    )
    return systems, totals


def run_mutation_tests() -> int:
    random = Random(29)
    manifest = make_manifest(random_source(random))
    while len(manifest["cancellations"]) < 2:
        manifest = make_manifest(random_source(random))
    validate_manifest(manifest)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(manifest)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data["removed_point_indices"].append(data["removed_point_indices"][0]))
    add(lambda data: data["removed_point_indices"].pop())
    add(lambda data: data["pre_response_points"].append(data["pre_response_points"][0]))
    add(lambda data: data["cancellations"].pop())
    add(
        lambda data: data["cancellations"].append(
            copy.deepcopy(data["cancellations"][0])
        )
    )
    add(lambda data: data["cancellations"][0].update(evidence="unknown-evidence"))
    add(
        lambda data: data["cancellations"][1].update(
            destroyed_triple=data["cancellations"][0]["destroyed_triple"]
        )
    )

    def break_collinearity(data: dict[str, Any]) -> None:
        triple = data["cancellations"][0]["destroyed_triple"]
        point_index = triple[-1]
        data["pre_response_points"][point_index][1] += 1

    add(break_collinearity)

    def duplicate_deleted_evidence(data: dict[str, Any]) -> None:
        deleted_records = [
            record
            for name in ("rank1", "rank2", "rank3")
            for record in data["source_manifest"]["fates"][name]
            if record["kind"] == "deleted"
        ]
        deleted_records[1]["evidence"] = deleted_records[0]["evidence"]

    add(duplicate_deleted_evidence)

    def survivor_mismatch(data: dict[str, Any]) -> None:
        data["pre_response_points"][0][0] += 100

    add(survivor_mismatch)

    rejected = 0
    for candidate in mutations:
        try:
            validate_manifest(candidate)
        except CancellationError:
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted manifest accepted")
    return rejected


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit(
            "usage: check_geometric_destroyed_triple_cancellation.py [manifest.json]"
        )
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            manifest = json.load(handle)
        summary = validate_manifest(manifest)
        print(
            "accepted destroyed-triple cancellation manifest: "
            f"{summary['responses']} responses, {summary['witnesses']} witnesses, "
            f"{summary['deleted']} deleted witnesses, {summary['reserved']} reserved "
            f"destroyed triples and {summary['unused_credit']} unused credits"
        )
        return

    systems, totals = run_random_tests()
    rejected = run_mutation_tests()
    print(
        "verified destroyed-triple cancellation checker: "
        f"{systems} random systems, {totals['witnesses']} witnesses, "
        f"{totals['deleted']} deleted witnesses, {totals['destroyed']} destroyed triples, "
        f"{totals['unused_credit']} unused credits, {totals['response_checks']} "
        f"responsewise inequalities and {rejected} corrupted manifests rejected"
    )


if __name__ == "__main__":
    main()
