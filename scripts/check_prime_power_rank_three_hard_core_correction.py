#!/usr/bin/env python3
"""Validate the exact geometry and correction burden of the eleven-host hard core.

The input source is the exact zero-response blocker manifest.  For each blocker host,
the checker reconstructs the canonical rank-three minimizing response, enumerates its
literal collinear triples, records the unique supporting response line, and computes
the exact number of rank-three occurrence units that must be removed to make that
selected response rank-three-free.

With one JSON path, validate a stored manifest. With ``--write PATH``, write the
canonical manifest. With no arguments, run the exact census and corruption tests.
"""
from __future__ import annotations

import copy
import json
import math
import sys
from itertools import combinations
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_rank_three_exact_best_response as selector
import check_prime_power_rank_three_zero_response_blockers as blockers

EXPECTED_CORRECTION_SHA256 = "86902404bef228440c2ed6e1e940f3b45ffd8e0a3a193abd8a21fe9327d6ab62"


class CorrectionError(ValueError):
    """Raised when the hard-core correction manifest is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CorrectionError(message)


def collinear_triples(permutation: tuple[int, ...]) -> list[list[list[int]]]:
    points = [(left, permutation[left]) for left in range(len(permutation))]
    output: list[list[list[int]]] = []
    for indices in combinations(range(len(points)), 3):
        triple = [points[index] for index in indices]
        if catalogue.collinear(*triple):
            output.append([list(point) for point in triple])
    return output


def normalized_line(points: list[tuple[int, int]]) -> list[int]:
    require(len(points) >= 2, "line support requires two points")
    first, second = points[0], points[1]
    a = second[1] - first[1]
    b = first[0] - second[0]
    c = -(a * first[0] + b * first[1])
    divisor = math.gcd(math.gcd(abs(a), abs(b)), abs(c)) or 1
    a, b, c = a // divisor, b // divisor, c // divisor
    first_nonzero = next(value for value in (a, b, c) if value != 0)
    if first_nonzero < 0:
        a, b, c = -a, -b, -c
    return [a, b, c]


def build_manifest() -> dict[str, Any]:
    blocker_manifest = blockers.build_manifest()
    blockers.validate_manifest(blocker_manifest)
    selector_manifest = selector.build_selector_manifest()
    selector.validate_selector_manifest(selector_manifest)
    selector_by_id = {record["host_id"]: record for record in selector_manifest["hosts"]}

    records: list[dict[str, Any]] = []
    for blocker in blocker_manifest["blockers"]:
        selected = selector_by_id[blocker["host_id"]]
        permutation = tuple(selected["selected_response"])
        triples = collinear_triples(permutation)
        require(len(triples) == selected["minimum_response_triples"],
                "literal selected triple count mismatch")
        support_points = sorted({tuple(point) for triple in triples for point in triple})
        require(all(
            catalogue.collinear(support_points[0], support_points[1], point)
            for point in support_points[2:]
        ), "selected rank-three triples do not share one line")
        minimum = selected["minimum_response_triples"]
        records.append(
            {
                "host_id": blocker["host_id"],
                "catalogue_record_sha256": blocker["catalogue_record_sha256"],
                "deletion_edges": blocker["deletion_edges"],
                "selected_response": selected["selected_response"],
                "selected_rank3_triples": triples,
                "selected_support_points": [list(point) for point in support_points],
                "selected_support_line": normalized_line(support_points),
                "selected_rank3_occurrences": minimum,
                "minimum_rank3_occurrence_deletions": minimum,
                "uniform_rank3_correction_units": 4,
                "deterministic_saving_units": 4 - minimum,
            }
        )

    payload: dict[str, Any] = {
        "version": 1,
        "source_blocker_sha256": blocker_manifest["blocker_sha256"],
        "source_selector_sha256": selector_manifest["selector_sha256"],
        "records": records,
    }
    payload["correction_sha256"] = catalogue.canonical_digest(payload)
    payload["claims"] = {
        "hosts": len(records),
        "one_triple_hosts": sum(record["selected_rank3_occurrences"] == 1 for record in records),
        "four_triple_hosts": sum(record["selected_rank3_occurrences"] == 4 for record in records),
        "distinct_selected_responses": len({tuple(record["selected_response"]) for record in records}),
        "distinct_support_lines": len({tuple(record["selected_support_line"]) for record in records}),
        "deterministic_correction_units": sum(
            record["minimum_rank3_occurrence_deletions"] for record in records
        ),
        "uniform_correction_units": sum(
            record["uniform_rank3_correction_units"] for record in records
        ),
        "deterministic_saving_units": sum(
            record["deterministic_saving_units"] for record in records
        ),
        "support_distribution": [
            [list(line), sum(tuple(record["selected_support_line"]) == line for record in records)]
            for line in sorted({tuple(record["selected_support_line"]) for record in records})
        ],
    }
    return payload


def validate_manifest(manifest: Any) -> dict[str, Any]:
    require(isinstance(manifest, dict), "manifest: expected object")
    expected = build_manifest()
    require(manifest.get("version") == 1, "version: expected 1")
    for key in (
        "source_blocker_sha256",
        "source_selector_sha256",
        "records",
        "correction_sha256",
        "claims",
    ):
        require(manifest.get(key) == expected[key], f"{key}: canonical mismatch")

    claims = expected["claims"]
    require(expected["correction_sha256"] == EXPECTED_CORRECTION_SHA256,
            "built-in correction digest drift")
    require((claims["hosts"], claims["one_triple_hosts"], claims["four_triple_hosts"])
            == (11, 9, 2), "hard-core geometry census mismatch")
    require((claims["distinct_selected_responses"], claims["distinct_support_lines"])
            == (2, 2), "selected response/support census mismatch")
    require((claims["deterministic_correction_units"], claims["uniform_correction_units"],
             claims["deterministic_saving_units"]) == (17, 44, 27),
            "correction burden identity mismatch")
    require(claims["support_distribution"] == [
        [[1, -1, -1], 9],
        [[1, 1, -3], 2],
    ], "support line distribution mismatch")
    return copy.deepcopy(claims)


def run_mutation_tests() -> int:
    manifest = build_manifest()
    validate_manifest(manifest)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(manifest)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data.update(correction_sha256="0" * 64))
    add(lambda data: data.update(source_blocker_sha256="0" * 64))
    add(lambda data: data["claims"].update(deterministic_correction_units=18))
    add(lambda data: data["records"][0].update(host_id="s4-corrupt"))
    add(lambda data: data["records"][0]["selected_response"].reverse())
    add(lambda data: data["records"][0]["selected_rank3_triples"].pop())
    add(lambda data: data["records"][0]["selected_support_points"].pop())
    add(lambda data: data["records"][0].update(selected_support_line=[0, 0, 0]))
    add(lambda data: data["records"][0].update(minimum_rank3_occurrence_deletions=0))
    add(lambda data: data["records"].reverse())

    rejected = 0
    for candidate in mutations:
        try:
            validate_manifest(candidate)
        except (
            CorrectionError,
            blockers.BlockerError,
            selector.SelectorError,
            catalogue.CatalogueError,
        ):
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted manifest accepted")
    return rejected


def main() -> None:
    if len(sys.argv) == 3 and sys.argv[1] == "--write":
        manifest = build_manifest()
        validate_manifest(manifest)
        Path(sys.argv[2]).write_text(
            json.dumps(manifest, sort_keys=True, indent=2) + "\n", encoding="utf-8"
        )
        print(
            "wrote hard-core correction manifest: "
            f"{manifest['claims']['hosts']} hosts, "
            f"sha256 {manifest['correction_sha256']}"
        )
        return
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            manifest = json.load(handle)
        claims = validate_manifest(manifest)
        print(
            "accepted hard-core correction manifest: "
            f"{claims['hosts']} hosts, {claims['deterministic_correction_units']} "
            "deterministic correction units"
        )
        return
    if len(sys.argv) != 1:
        raise SystemExit(
            "usage: check_prime_power_rank_three_hard_core_correction.py "
            "[manifest.json | --write manifest.json]"
        )

    manifest = build_manifest()
    claims = validate_manifest(manifest)
    rejected = run_mutation_tests()
    print(
        "verified rank-three hard-core correction geometry: "
        f"{claims['hosts']} hosts, {claims['one_triple_hosts']} one-triple and "
        f"{claims['four_triple_hosts']} four-triple selectors, "
        f"{claims['deterministic_correction_units']} deterministic versus "
        f"{claims['uniform_correction_units']} uniform correction units, "
        f"sha256 {manifest['correction_sha256']}, and {rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
