#!/usr/bin/env python3
"""Build and validate the exact line-incidence kernel for all 9,260 responses.

For every canonical raw host and every response permutation, the kernel stores the
response points and every affine line containing at least two response points. Each
line record carries its response occupancy r, rank-two pair multiplicity C(r,2), and
rank-three triple multiplicity C(r,3).

With one JSON path, validate a stored kernel. With ``--write PATH``, write the full
canonical kernel. With no arguments, run the exact census and mutation tests.
"""
from __future__ import annotations

import copy
import json
import math
import sys
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue

EXPECTED_KERNEL_SHA256 = "b591356b800b44ae1a20c9f57cdad0782aecc43ca0a2ee699c4c0337d3010697"


class KernelError(ValueError):
    """Raised when the response line-incidence kernel is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise KernelError(message)


def normalized_line(first: tuple[int, int], second: tuple[int, int]) -> tuple[int, int, int]:
    a = second[1] - first[1]
    b = first[0] - second[0]
    c = -(a * first[0] + b * first[1])
    divisor = math.gcd(math.gcd(abs(a), abs(b)), abs(c)) or 1
    a, b, c = a // divisor, b // divisor, c // divisor
    first_nonzero = next(value for value in (a, b, c) if value != 0)
    if first_nonzero < 0:
        a, b, c = -a, -b, -c
    return a, b, c


def response_geometry(permutation: list[int]) -> dict[str, Any]:
    points = [(left, permutation[left]) for left in range(len(permutation))]
    line_points: dict[tuple[int, int, int], set[tuple[int, int]]] = defaultdict(set)
    for first_index, second_index in combinations(range(len(points)), 2):
        line = normalized_line(points[first_index], points[second_index])
        line_points[line].update((points[first_index], points[second_index]))

    lines = []
    for line, support in sorted(line_points.items()):
        occupancy = len(support)
        lines.append(
            {
                "line": list(line),
                "response_points": [list(point) for point in sorted(support)],
                "response_occupancy": occupancy,
                "rank2_pair_multiplicity": math.comb(occupancy, 2),
                "rank3_triple_multiplicity": math.comb(occupancy, 3),
            }
        )

    geometry: dict[str, Any] = {
        "permutation": list(permutation),
        "response_points": [list(point) for point in points],
        "line_records": lines,
        "rank3_triples": sum(record["rank3_triple_multiplicity"] for record in lines),
        "occupancy_profile": sorted(record["response_occupancy"] for record in lines),
    }
    geometry["response_geometry_sha256"] = catalogue.canonical_digest(geometry)
    return geometry


@lru_cache(maxsize=1)
def _build_kernel_cached() -> dict[str, Any]:
    source = catalogue.build_catalogue()
    catalogue.validate_catalogue(source)
    hosts: list[dict[str, Any]] = []
    profile_counter: Counter[tuple[int, tuple[int, ...]]] = Counter()
    maximum_counter: Counter[int] = Counter()
    response_geometry_digests: set[str] = set()

    for host in source["hosts"]:
        response_records = []
        for source_response in host["responses"]:
            geometry = response_geometry(source_response["permutation"])
            require(
                geometry["rank3_triples"] == source_response["triple_count"],
                "rank-three kernel total disagrees with catalogue",
            )
            profile = tuple(geometry["occupancy_profile"])
            profile_counter[(host["side"], profile)] += 1
            maximum_counter[max(profile)] += 1
            response_geometry_digests.add(geometry["response_geometry_sha256"])
            response_records.append(geometry)

        host_record: dict[str, Any] = {
            "host_id": host["host_id"],
            "catalogue_record_sha256": host["record_sha256"],
            "side": host["side"],
            "responses": response_records,
        }
        host_record["host_kernel_sha256"] = catalogue.canonical_digest(host_record)
        hosts.append(host_record)

    profile_distribution = [
        {"side": side, "occupancy_profile": list(profile), "responses": count}
        for (side, profile), count in sorted(profile_counter.items())
    ]
    payload: dict[str, Any] = {
        "version": 1,
        "source_catalogue_sha256": source["catalogue_sha256"],
        "hosts": hosts,
    }
    payload["kernel_sha256"] = catalogue.canonical_digest(payload)
    payload["claims"] = {
        "hosts": len(hosts),
        "responses": sum(len(host["responses"]) for host in hosts),
        "line_records": sum(
            len(response["line_records"])
            for host in hosts
            for response in host["responses"]
        ),
        "rank3_triples": sum(
            response["rank3_triples"]
            for host in hosts
            for response in host["responses"]
        ),
        "unique_response_geometries": len(response_geometry_digests),
        "maximum_occupancy_distribution": [
            [occupancy, count] for occupancy, count in sorted(maximum_counter.items())
        ],
        "profile_distribution": profile_distribution,
    }
    return payload


def build_kernel() -> dict[str, Any]:
    return copy.deepcopy(_build_kernel_cached())


def validate_kernel(kernel: Any) -> dict[str, Any]:
    require(isinstance(kernel, dict), "kernel: expected object")
    expected = _build_kernel_cached()
    require(kernel.get("version") == 1, "version: expected 1")
    for key in ("source_catalogue_sha256", "hosts", "kernel_sha256", "claims"):
        require(kernel.get(key) == expected[key], f"{key}: canonical mismatch")

    claims = expected["claims"]
    require(expected["kernel_sha256"] == EXPECTED_KERNEL_SHA256,
            "built-in kernel digest drift")
    require((claims["hosts"], claims["responses"], claims["line_records"])
            == (740, 9260, 79736), "kernel census mismatch")
    require(claims["rank3_triples"] == 6485, "rank-three total mismatch")
    require(claims["unique_response_geometries"] == 39,
            "unique response geometry count mismatch")
    require(claims["maximum_occupancy_distribution"] == [
        [2, 4253], [3, 4697], [4, 310]
    ], "maximum occupancy distribution mismatch")
    require(claims["profile_distribution"] == [
        {"side": 4, "occupancy_profile": [2, 2, 2, 2, 2, 2], "responses": 137},
        {"side": 4, "occupancy_profile": [2, 2, 2, 3], "responses": 34},
        {"side": 4, "occupancy_profile": [4], "responses": 35},
        {"side": 5, "occupancy_profile": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], "responses": 4116},
        {"side": 5, "occupancy_profile": [2, 2, 2, 2, 2, 2, 2, 3], "responses": 4115},
        {"side": 5, "occupancy_profile": [2, 2, 2, 2, 3, 3], "responses": 548},
        {"side": 5, "occupancy_profile": [2, 2, 2, 2, 4], "responses": 275},
    ], "occupancy profile distribution mismatch")
    return copy.deepcopy(claims)


def rank2_from_kernel(response: dict[str, Any], background: list[tuple[int, int]]) -> int:
    total = 0
    for record in response["line_records"]:
        a, b, c = record["line"]
        background_height = sum(a * x + b * y + c == 0 for x, y in background)
        total += record["rank2_pair_multiplicity"] * background_height
    return total


def run_mutation_tests() -> int:
    kernel = build_kernel()
    validate_kernel(kernel)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(kernel)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data.update(kernel_sha256="0" * 64))
    add(lambda data: data.update(source_catalogue_sha256="0" * 64))
    add(lambda data: data["claims"].update(responses=9259))
    add(lambda data: data["hosts"][0].update(host_id="s4-corrupt"))
    add(lambda data: data["hosts"][0]["responses"][0]["permutation"].reverse())
    add(lambda data: data["hosts"][0]["responses"][0]["response_points"].pop())
    add(lambda data: data["hosts"][0]["responses"][0]["line_records"].pop())
    add(lambda data: data["hosts"][0]["responses"][0]["line_records"][0].update(response_occupancy=99))
    add(lambda data: data["hosts"][0]["responses"][0].update(rank3_triples=99))
    add(lambda data: data["hosts"].reverse())

    rejected = 0
    for candidate in mutations:
        try:
            validate_kernel(candidate)
        except (KernelError, catalogue.CatalogueError):
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted kernel accepted")
    return rejected


def main() -> None:
    if len(sys.argv) == 3 and sys.argv[1] == "--write":
        kernel = build_kernel()
        validate_kernel(kernel)
        Path(sys.argv[2]).write_text(
            json.dumps(kernel, sort_keys=True, indent=2) + "\n", encoding="utf-8"
        )
        print(
            "wrote response line-incidence kernel: "
            f"{kernel['claims']['responses']} responses, sha256 {kernel['kernel_sha256']}"
        )
        return
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            kernel = json.load(handle)
        claims = validate_kernel(kernel)
        print(
            "accepted response line-incidence kernel: "
            f"{claims['responses']} responses and {claims['line_records']} line records"
        )
        return
    if len(sys.argv) != 1:
        raise SystemExit(
            "usage: check_prime_power_response_line_incidence_kernel.py "
            "[kernel.json | --write kernel.json]"
        )

    kernel = build_kernel()
    claims = validate_kernel(kernel)
    rejected = run_mutation_tests()
    print(
        "verified response line-incidence kernel: "
        f"{claims['hosts']} hosts, {claims['responses']} responses, "
        f"{claims['line_records']} line records, {claims['unique_response_geometries']} "
        f"unique geometries, sha256 {kernel['kernel_sha256']}, and "
        f"{rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
