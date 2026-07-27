#!/usr/bin/env python3
"""Validate exact background-dependent response selectors on canonical raw hosts.

For one canonical host and one ordered background point set disjoint from the response
grid, the checker evaluates every response. It counts rank-one triples directly,
checks rank-two counts both directly and through the canonical line-incidence kernel,
checks rank-three counts through the same kernel, and publishes the lexicographically
first response minimizing the complete number of new triples.

With one JSON path, validate a stored certificate. With no argument, run deterministic
mixed-background and mutation tests.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from functools import lru_cache
from itertools import combinations
from pathlib import Path
from random import Random
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_response_line_incidence_kernel as line_kernel

Point = tuple[int, int]


class BackgroundSelectorError(ValueError):
    """Raised when a background response-selector certificate is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise BackgroundSelectorError(message)


def parse_integer(value: Any, path: str) -> int:
    require(type(value) is int, f"{path}: expected integer")
    return value


def parse_point(value: Any, path: str) -> Point:
    require(isinstance(value, list) and len(value) == 2, f"{path}: expected [x,y]")
    return parse_integer(value[0], f"{path}[0]"), parse_integer(value[1], f"{path}[1]")


@lru_cache(maxsize=1)
def host_maps() -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    source = catalogue.build_catalogue()
    catalogue.validate_catalogue(source)
    kernel = line_kernel.build_kernel()
    line_kernel.validate_kernel(kernel)
    hosts = {record["host_id"]: record for record in source["hosts"]}
    kernels = {record["host_id"]: record for record in kernel["hosts"]}
    require(set(hosts) == set(kernels), "catalogue/kernel host mismatch")
    return hosts, kernels


def direct_rank_counts(
    permutation: list[int], background: list[Point]
) -> tuple[int, int, int]:
    response = [(left, permutation[left]) for left in range(len(permutation))]
    rank1 = sum(
        catalogue.collinear(response_point, first, second)
        for response_point in response
        for first, second in combinations(background, 2)
    )
    rank2 = sum(
        catalogue.collinear(first, second, background_point)
        for first, second in combinations(response, 2)
        for background_point in background
    )
    rank3 = catalogue.response_triples(tuple(permutation))
    return rank1, rank2, rank3


def exact_records(certificate: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    hosts, kernels = host_maps()
    host_id = certificate.get("host_id")
    require(isinstance(host_id, str) and host_id in hosts, "host_id: unknown")
    host = hosts[host_id]
    require(
        certificate.get("catalogue_record_sha256") == host["record_sha256"],
        "catalogue_record_sha256: incorrect",
    )

    raw_background = certificate.get("background_points")
    require(isinstance(raw_background, list), "background_points: expected list")
    background = [
        parse_point(value, f"background_points[{index}]")
        for index, value in enumerate(raw_background)
    ]
    require(len(set(background)) == len(background), "background_points: duplicates")
    grid = {
        (left, right)
        for left in range(host["side"])
        for right in range(host["side"])
    }
    require(not (set(background) & grid), "background_points: intersects response grid")

    host_kernel = kernels[host_id]
    require(
        host_kernel["catalogue_record_sha256"] == host["record_sha256"],
        "host kernel record digest mismatch",
    )
    require(len(host_kernel["responses"]) == len(host["responses"]),
            "host kernel response count mismatch")

    records: list[dict[str, Any]] = []
    totals = Counter()
    for source_response, geometry in zip(host["responses"], host_kernel["responses"]):
        permutation = source_response["permutation"]
        require(geometry["permutation"] == permutation,
                "catalogue/kernel response order mismatch")
        rank_counts = direct_rank_counts(permutation, background)
        rank2_kernel = line_kernel.rank2_from_kernel(geometry, background)
        require(rank_counts[1] == rank2_kernel, "rank-two kernel mismatch")
        require(rank_counts[2] == geometry["rank3_triples"],
                "rank-three kernel mismatch")
        new_triples = sum(rank_counts)
        totals.update({"rank1": rank_counts[0], "rank2": rank_counts[1], "rank3": rank_counts[2]})
        records.append(
            {
                "permutation": permutation,
                "rank_counts": list(rank_counts),
                "new_triples": new_triples,
                "response_geometry_sha256": geometry["response_geometry_sha256"],
            }
        )

    minimum = min(record["new_triples"] for record in records)
    minimizers = [record for record in records if record["new_triples"] == minimum]
    selected = min(minimizers, key=lambda record: record["permutation"])

    rank3_minimum = min(record["rank_counts"][2] for record in records)
    rank3_minimizers = [
        record for record in records if record["rank_counts"][2] == rank3_minimum
    ]
    canonical_rank3 = min(rank3_minimizers, key=lambda record: record["permutation"])
    penalty = canonical_rank3["new_triples"] - minimum
    require(penalty >= 0, "selector penalty became negative")

    exact = {
        "responses": len(records),
        "background_points": len(background),
        "rank1_occurrences": totals["rank1"],
        "rank2_occurrences": totals["rank2"],
        "rank3_occurrences": totals["rank3"],
        "minimum_new_triples": minimum,
        "maximum_new_triples": max(record["new_triples"] for record in records),
        "minimizer_count": len(minimizers),
        "selected_response": selected["permutation"],
        "canonical_rank3_response": canonical_rank3["permutation"],
        "canonical_rank3_new_triples": canonical_rank3["new_triples"],
        "selector_penalty": penalty,
        "canonical_has_minimum_value": int(penalty == 0),
        "canonical_is_full_selector": int(
            canonical_rank3["permutation"] == selected["permutation"]
        ),
        "response_records_sha256": catalogue.canonical_digest(records),
    }
    return records, exact


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    _records, exact = exact_records(certificate)
    require(certificate.get("claims") == exact, "claims: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "selector_sha256"}
    require(
        certificate.get("selector_sha256") == catalogue.canonical_digest(payload),
        "selector_sha256: incorrect",
    )
    return {
        "responses": exact["responses"],
        "background_points": exact["background_points"],
        "rank1_occurrences": exact["rank1_occurrences"],
        "rank2_occurrences": exact["rank2_occurrences"],
        "rank3_occurrences": exact["rank3_occurrences"],
        "canonical_minimum_value": exact["canonical_has_minimum_value"],
        "canonical_full_selector": exact["canonical_is_full_selector"],
        "selector_changed": int(
            exact["canonical_rank3_response"] != exact["selected_response"]
        ),
        "positive_penalty": int(exact["selector_penalty"] > 0),
        "selector_penalty": exact["selector_penalty"],
        "minimum_new_triples": exact["minimum_new_triples"],
    }


def build_certificate(host: dict[str, Any], background: list[Point]) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "host_id": host["host_id"],
        "catalogue_record_sha256": host["record_sha256"],
        "background_points": [list(point) for point in background],
    }
    _records, claims = exact_records(certificate)
    certificate["claims"] = claims
    certificate["selector_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def random_background(side: int, random: Random) -> list[Point]:
    grid = {(left, right) for left in range(side) for right in range(side)}
    output: list[Point] = []
    target = random.randrange(0, 7)
    while len(output) < target:
        point = (random.randrange(-5, side + 6), random.randrange(-5, side + 6))
        if point not in grid and point not in output:
            output.append(point)
    return output


def run_random_tests() -> tuple[int, Counter[str], Counter[int], Counter[int]]:
    random = Random(2038)
    source = catalogue.build_catalogue()
    totals: Counter[str] = Counter()
    penalty_distribution: Counter[int] = Counter()
    minimum_distribution: Counter[int] = Counter()

    for _ in range(400):
        host = random.choice(source["hosts"])
        certificate = build_certificate(host, random_background(host["side"], random))
        summary = validate_certificate(certificate)
        totals.update(summary)
        penalty_distribution[summary["selector_penalty"]] += 1
        minimum_distribution[summary["minimum_new_triples"]] += 1

    require(totals["responses"] == 5077, "random tests: response total mismatch")
    require(totals["background_points"] == 1260,
            "random tests: background-point total mismatch")
    require(
        (totals["rank1_occurrences"], totals["rank2_occurrences"], totals["rank3_occurrences"])
        == (1782, 4102, 3603),
        "random tests: rank occurrence totals mismatch",
    )
    require(
        (
            totals["canonical_minimum_value"],
            totals["canonical_full_selector"],
            totals["selector_changed"],
            totals["positive_penalty"],
            totals["selector_penalty"],
        ) == (240, 234, 166, 160, 239),
        "random tests: selector comparison totals mismatch",
    )
    require(dict(sorted(penalty_distribution.items())) == {0: 240, 1: 107, 2: 36, 3: 9, 4: 7, 5: 1},
            "random tests: penalty distribution mismatch")
    require(dict(sorted(minimum_distribution.items())) == {0: 293, 1: 78, 2: 22, 3: 5, 5: 2},
            "random tests: minimum distribution mismatch")
    return 400, totals, penalty_distribution, minimum_distribution


def run_mutation_tests() -> int:
    random = Random(73)
    host = catalogue.build_catalogue()["hosts"][300]
    certificate = build_certificate(host, random_background(host["side"], random))
    validate_certificate(certificate)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(certificate)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data.update(selector_sha256="0" * 64))
    add(lambda data: data.update(host_id="s5-corrupt"))
    add(lambda data: data.update(catalogue_record_sha256="0" * 40))
    add(lambda data: data["background_points"].append(data["background_points"][0]))
    add(lambda data: data["background_points"].append([0, 0]))
    add(lambda data: data["claims"].update(responses=999))
    add(lambda data: data["claims"].update(rank1_occurrences=999))
    add(lambda data: data["claims"]["selected_response"].reverse())
    add(lambda data: data["claims"].update(selector_penalty=-1))
    add(lambda data: data["claims"].update(canonical_has_minimum_value=2))
    add(lambda data: data["claims"].update(response_records_sha256="0" * 64))
    add(lambda data: data.update(version=2))

    rejected = 0
    for candidate in mutations:
        try:
            validate_certificate(candidate)
        except (
            BackgroundSelectorError,
            catalogue.CatalogueError,
            line_kernel.KernelError,
        ):
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted certificate accepted")
    return rejected


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit(
            "usage: check_prime_power_background_response_selector.py [certificate.json]"
        )
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            certificate = json.load(handle)
        summary = validate_certificate(certificate)
        print(
            "accepted background response selector: "
            f"{summary['responses']} responses, selector penalty "
            f"{summary['selector_penalty']}"
        )
        return

    systems, totals, penalty_distribution, minimum_distribution = run_random_tests()
    rejected = run_mutation_tests()
    print(
        "verified background-dependent response selectors: "
        f"{systems} systems, {totals['responses']} responses, "
        f"{totals['background_points']} background points, "
        f"{totals['selector_changed']} raw-selector changes, penalty distribution "
        f"{sorted(penalty_distribution.items())}, minimum distribution "
        f"{sorted(minimum_distribution.items())}, and {rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
