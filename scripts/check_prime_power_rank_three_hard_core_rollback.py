#!/usr/bin/env python3
"""Validate exact minimum deletion rollback from the eleven-host rank-three core.

A rollback removes one or more edges from the canonical partial-matching deletion set,
thereby restoring response options.  For each positive-minimum side-four host, this
checker exhaustively finds the least number of deletion restrictions that must be
undone to restore at least one zero-rank-three response.

With one JSON path, validate a stored manifest. With ``--write PATH``, write the
canonical manifest. With no arguments, run the exact census and mutation tests.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue

EXPECTED_ROLLBACK_SHA256 = "6663bcaa9504dc361a65b230ef88e39919e80acdca93647a95c103a10e8c487b"


class RollbackError(ValueError):
    """Raised when the hard-core rollback manifest is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RollbackError(message)


def hard_core_hosts(source: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        host
        for host in source["hosts"]
        if min(record["triple_count"] for record in host["responses"]) > 0
    ]


def build_manifest() -> dict[str, Any]:
    source = catalogue.build_catalogue()
    catalogue.validate_catalogue(source)
    records: list[dict[str, Any]] = []

    for host in hard_core_hosts(source):
        deletion = [tuple(edge) for edge in host["deletion_edges"]]
        minimum_distance: int | None = None
        options: list[dict[str, Any]] = []

        for distance in range(1, len(deletion) + 1):
            for rolled_back in combinations(deletion, distance):
                rolled_back_set = set(rolled_back)
                restored_deletion = tuple(
                    edge for edge in deletion if edge not in rolled_back_set
                )
                restored = catalogue.build_host_record(host["side"], restored_deletion)
                require(restored is not None, "rollback unexpectedly destroys all responses")
                zero_responses = [
                    record["permutation"]
                    for record in restored["responses"]
                    if record["triple_count"] == 0
                ]
                if not zero_responses:
                    continue
                if minimum_distance is None:
                    minimum_distance = distance
                if distance == minimum_distance:
                    options.append(
                        {
                            "rolled_back_edges": [list(edge) for edge in rolled_back],
                            "restored_host_id": restored["host_id"],
                            "restored_record_sha256": restored["record_sha256"],
                            "restored_deletion_edges": restored["deletion_edges"],
                            "restored_denominator": restored["denominator"],
                            "restored_rank3_slack": restored["rank3_slack"],
                            "zero_response_count": len(zero_responses),
                            "selected_zero_response": min(zero_responses),
                        }
                    )
            if minimum_distance is not None:
                break

        require(minimum_distance is not None, "hard-core host has no finite rollback")
        records.append(
            {
                "host_id": host["host_id"],
                "catalogue_record_sha256": host["record_sha256"],
                "deletion_edges": host["deletion_edges"],
                "deletion_size": host["deletion_size"],
                "minimum_response_triples": min(
                    record["triple_count"] for record in host["responses"]
                ),
                "rollback_distance": minimum_distance,
                "minimal_rollback_options": options,
            }
        )

    option_count_distribution = Counter(
        len(record["minimal_rollback_options"]) for record in records
    )
    distance_distribution = Counter(record["rollback_distance"] for record in records)
    zero_count_distribution = Counter(
        option["zero_response_count"]
        for record in records
        for option in record["minimal_rollback_options"]
    )
    restored_slack_distribution = Counter(
        option["restored_rank3_slack"]
        for record in records
        for option in record["minimal_rollback_options"]
    )

    payload: dict[str, Any] = {
        "version": 1,
        "source_catalogue_sha256": source["catalogue_sha256"],
        "records": records,
    }
    payload["rollback_sha256"] = catalogue.canonical_digest(payload)
    payload["claims"] = {
        "hosts": len(records),
        "distance_distribution": [
            [distance, count] for distance, count in sorted(distance_distribution.items())
        ],
        "total_independent_rollback_distance": sum(
            record["rollback_distance"] for record in records
        ),
        "minimal_rollback_options": sum(
            len(record["minimal_rollback_options"]) for record in records
        ),
        "option_count_distribution": [
            [count, hosts] for count, hosts in sorted(option_count_distribution.items())
        ],
        "distinct_restored_hosts": len(
            {
                option["restored_host_id"]
                for record in records
                for option in record["minimal_rollback_options"]
            }
        ),
        "restored_zero_count_distribution": [
            [count, options] for count, options in sorted(zero_count_distribution.items())
        ],
        "restored_slack_distribution": [
            [slack, options]
            for slack, options in sorted(restored_slack_distribution.items())
        ],
        "distance_two_host_ids": [
            record["host_id"] for record in records if record["rollback_distance"] == 2
        ],
    }
    return payload


def validate_manifest(manifest: Any) -> dict[str, Any]:
    require(isinstance(manifest, dict), "manifest: expected object")
    expected = build_manifest()
    require(manifest.get("version") == 1, "version: expected 1")
    for key in (
        "source_catalogue_sha256",
        "records",
        "rollback_sha256",
        "claims",
    ):
        require(manifest.get(key) == expected[key], f"{key}: canonical mismatch")

    claims = expected["claims"]
    require(expected["rollback_sha256"] == EXPECTED_ROLLBACK_SHA256,
            "built-in rollback digest drift")
    require(claims["hosts"] == 11, "expected eleven hard-core hosts")
    require(claims["distance_distribution"] == [[1, 10], [2, 1]],
            "rollback-distance distribution mismatch")
    require(claims["total_independent_rollback_distance"] == 12,
            "total rollback distance mismatch")
    require(claims["minimal_rollback_options"] == 21,
            "minimal rollback option count mismatch")
    require(claims["option_count_distribution"] == [[1, 2], [2, 8], [3, 1]],
            "option-count distribution mismatch")
    require(claims["distinct_restored_hosts"] == 13,
            "restored-host count mismatch")
    require(claims["restored_zero_count_distribution"] == [[1, 19], [2, 2]],
            "restored-zero distribution mismatch")
    require(claims["restored_slack_distribution"] == [[-2, 19], [-1, 2]],
            "restored-slack distribution mismatch")
    require(claims["distance_two_host_ids"] == ["s4-59ac56096a7f627f"],
            "distance-two host mismatch")
    return copy.deepcopy(claims)


def run_mutation_tests() -> int:
    manifest = build_manifest()
    validate_manifest(manifest)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(manifest)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data.update(rollback_sha256="0" * 64))
    add(lambda data: data.update(source_catalogue_sha256="0" * 64))
    add(lambda data: data["claims"].update(hosts=10))
    add(lambda data: data["claims"].update(total_independent_rollback_distance=11))
    add(lambda data: data["records"][0].update(host_id="s4-corrupt"))
    add(lambda data: data["records"][0].update(rollback_distance=2))
    add(lambda data: data["records"][0]["deletion_edges"].pop())
    add(lambda data: data["records"][0]["minimal_rollback_options"].pop())
    add(lambda data: data["records"][0]["minimal_rollback_options"][0]["rolled_back_edges"].pop())
    add(lambda data: data["records"].reverse())

    rejected = 0
    for candidate in mutations:
        try:
            validate_manifest(candidate)
        except (RollbackError, catalogue.CatalogueError):
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
            "wrote hard-core rollback manifest: "
            f"{manifest['claims']['hosts']} hosts, sha256 {manifest['rollback_sha256']}"
        )
        return
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            manifest = json.load(handle)
        claims = validate_manifest(manifest)
        print(
            "accepted hard-core rollback manifest: "
            f"distance distribution {claims['distance_distribution']}"
        )
        return
    if len(sys.argv) != 1:
        raise SystemExit(
            "usage: check_prime_power_rank_three_hard_core_rollback.py "
            "[manifest.json | --write manifest.json]"
        )

    manifest = build_manifest()
    claims = validate_manifest(manifest)
    rejected = run_mutation_tests()
    print(
        "verified hard-core deletion rollback: "
        f"{claims['hosts']} hosts, distance distribution {claims['distance_distribution']}, "
        f"{claims['minimal_rollback_options']} minimal options, total independent distance "
        f"{claims['total_independent_rollback_distance']}, sha256 "
        f"{manifest['rollback_sha256']}, and {rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
