#!/usr/bin/env python3
"""Validate the exact side-four blockers of all zero-rank-three responses.

The undeleted side-four raw host has fixed forbidden diagonal and target edge (0,1).
Among its six response matchings exactly four have zero collinear response triples.
A canonical partial-matching deletion set has positive minimum rank-three load exactly
when it intersects every one of those four zero-triple responses while leaving at
least one response.  This checker reconstructs the blocker hypergraph, its three
inclusion-minimal transversals, and all eleven surviving canonical blockers.

With one JSON path, validate a stored manifest.  With ``--write PATH``, write the
canonical manifest.  With no arguments, run the exact census and mutation tests.
"""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_rank_three_exact_best_response as selector

EXPECTED_BLOCKER_SHA256 = "94713659dd58fea0ccb015d4a5ce25e447c766ebd2936fff696f39ce1e539fc3"


class BlockerError(ValueError):
    """Raised when the zero-response blocker manifest is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise BlockerError(message)


def response_edges(permutation: tuple[int, ...]) -> set[tuple[int, int]]:
    return {(left, permutation[left]) for left in range(len(permutation))}


def build_manifest() -> dict[str, Any]:
    source = catalogue.build_catalogue()
    catalogue.validate_catalogue(source)
    selected = selector.build_selector_manifest()
    selector.validate_selector_manifest(selected)

    side = 4
    diagonal = {(index, index) for index in range(side)}
    target = {(0, 1)}
    base_forbidden = diagonal | target
    base_responses = catalogue.perfect_matchings(side, base_forbidden)
    base_records = [
        {
            "permutation": list(permutation),
            "triple_count": catalogue.response_triples(permutation),
        }
        for permutation in base_responses
    ]
    zero_responses = [
        tuple(record["permutation"])
        for record in base_records
        if record["triple_count"] == 0
    ]
    positive_responses = [
        tuple(record["permutation"])
        for record in base_records
        if record["triple_count"] > 0
    ]

    admissible = {
        (left, right)
        for left in range(side)
        for right in range(side)
    } - base_forbidden

    blockers: list[dict[str, Any]] = []
    for deletion in catalogue.partial_matchings(admissible):
        deletion_set = set(deletion)
        hits_all_zero = all(
            bool(deletion_set & response_edges(permutation))
            for permutation in zero_responses
        )
        responses = catalogue.perfect_matchings(side, base_forbidden | deletion_set)
        if not hits_all_zero or not responses:
            continue
        host = catalogue.build_host_record(side, deletion)
        require(host is not None, "blocker unexpectedly has no host record")
        blockers.append(
            {
                "host_id": host["host_id"],
                "catalogue_record_sha256": host["record_sha256"],
                "deletion_edges": host["deletion_edges"],
                "deletion_size": host["deletion_size"],
                "surviving_responses": host["responses"],
                "minimum_response_triples": min(
                    record["triple_count"] for record in host["responses"]
                ),
            }
        )

    blocker_sets = [
        {tuple(edge) for edge in record["deletion_edges"]}
        for record in blockers
    ]
    minimal_sets = [
        deletion
        for deletion in blocker_sets
        if not any(other < deletion for other in blocker_sets)
    ]
    minimal_blockers = [
        [list(edge) for edge in sorted(deletion)]
        for deletion in sorted(minimal_sets, key=lambda value: (len(value), sorted(value)))
    ]

    hard_ids = selected["claims"]["positive_minimum_host_ids"]
    blocker_ids = [record["host_id"] for record in blockers]
    require(blocker_ids == hard_ids, "blocker host order differs from selector hard core")

    payload: dict[str, Any] = {
        "version": 1,
        "source_catalogue_sha256": source["catalogue_sha256"],
        "source_selector_sha256": selected["selector_sha256"],
        "base_forbidden_edges": [list(edge) for edge in sorted(base_forbidden)],
        "base_responses": base_records,
        "zero_response_permutations": [list(value) for value in zero_responses],
        "positive_response_permutations": [list(value) for value in positive_responses],
        "minimal_blockers": minimal_blockers,
        "blockers": blockers,
    }
    payload["blocker_sha256"] = catalogue.canonical_digest(payload)
    payload["claims"] = {
        "base_responses": len(base_records),
        "zero_responses": len(zero_responses),
        "positive_responses": len(positive_responses),
        "minimal_blockers": len(minimal_blockers),
        "canonical_blockers": len(blockers),
        "size_distribution": [
            [size, sum(record["deletion_size"] == size for record in blockers)]
            for size in sorted({record["deletion_size"] for record in blockers})
        ],
        "minimum_distribution": [
            [minimum, sum(record["minimum_response_triples"] == minimum for record in blockers)]
            for minimum in sorted(
                {record["minimum_response_triples"] for record in blockers}
            )
        ],
        "hard_core_host_ids": blocker_ids,
    }
    return payload


def validate_manifest(manifest: Any) -> dict[str, Any]:
    require(isinstance(manifest, dict), "manifest: expected object")
    expected = build_manifest()
    require(manifest.get("version") == 1, "version: expected 1")
    for key in (
        "source_catalogue_sha256",
        "source_selector_sha256",
        "base_forbidden_edges",
        "base_responses",
        "zero_response_permutations",
        "positive_response_permutations",
        "minimal_blockers",
        "blockers",
        "blocker_sha256",
        "claims",
    ):
        require(manifest.get(key) == expected[key], f"{key}: canonical mismatch")

    claims = expected["claims"]
    require(expected["blocker_sha256"] == EXPECTED_BLOCKER_SHA256,
            "built-in blocker digest drift")
    require((claims["base_responses"], claims["zero_responses"], claims["positive_responses"])
            == (6, 4, 2), "base response census mismatch")
    require(claims["minimal_blockers"] == 3, "minimal blocker count mismatch")
    require(claims["canonical_blockers"] == 11, "canonical blocker count mismatch")
    require(claims["size_distribution"] == [[2, 3], [3, 6], [4, 2]],
            "blocker size distribution mismatch")
    require(claims["minimum_distribution"] == [[1, 9], [4, 2]],
            "blocker minimum distribution mismatch")
    return copy.deepcopy(claims)


def run_mutation_tests() -> int:
    manifest = build_manifest()
    validate_manifest(manifest)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(manifest)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data.update(blocker_sha256="0" * 64))
    add(lambda data: data.update(source_catalogue_sha256="0" * 64))
    add(lambda data: data["claims"].update(canonical_blockers=10))
    add(lambda data: data["base_responses"][0].update(triple_count=99))
    add(lambda data: data["zero_response_permutations"].pop())
    add(lambda data: data["minimal_blockers"][0].pop())
    add(lambda data: data["blockers"][0].update(host_id="s4-corrupt"))
    add(lambda data: data["blockers"][0]["deletion_edges"].pop())
    add(lambda data: data["blockers"][0]["surviving_responses"].pop())
    add(lambda data: data["claims"]["hard_core_host_ids"].reverse())

    rejected = 0
    for candidate in mutations:
        try:
            validate_manifest(candidate)
        except (BlockerError, catalogue.CatalogueError, selector.SelectorError):
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
            "wrote zero-response blocker manifest: "
            f"{manifest['claims']['canonical_blockers']} blockers, "
            f"sha256 {manifest['blocker_sha256']}"
        )
        return
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            manifest = json.load(handle)
        claims = validate_manifest(manifest)
        print(
            "accepted zero-response blocker manifest: "
            f"{claims['canonical_blockers']} blockers from "
            f"{claims['minimal_blockers']} minimal transversals"
        )
        return
    if len(sys.argv) != 1:
        raise SystemExit(
            "usage: check_prime_power_rank_three_zero_response_blockers.py "
            "[manifest.json | --write manifest.json]"
        )

    manifest = build_manifest()
    claims = validate_manifest(manifest)
    rejected = run_mutation_tests()
    print(
        "verified side-four zero-response blockers: "
        f"{claims['base_responses']} base responses, {claims['zero_responses']} zero, "
        f"{claims['minimal_blockers']} minimal transversals, "
        f"{claims['canonical_blockers']} canonical blockers, blocker sha256 "
        f"{manifest['blocker_sha256']}, and {rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
