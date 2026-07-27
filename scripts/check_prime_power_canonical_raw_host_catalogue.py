#!/usr/bin/env python3
"""Build and validate the canonical side-four/five raw-host catalogue.

The raw host identity is determined by:
  * matching side;
  * the fixed forbidden diagonal and target edge; and
  * one canonical partial-matching deletion set.

Every derived field is reconstructed: forbidden edges, all response permutations,
response triple counts, denominator Z, rank-three numerator A3, slack S3, and the
response-triple histogram.

With one JSON path, validate a stored full catalogue. With ``--write PATH``, write
the canonical full catalogue. With no arguments, run exact census and mutation tests.
"""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from collections import Counter
from itertools import combinations, permutations
from pathlib import Path
from typing import Any

Edge = tuple[int, int]
Point = tuple[int, int]

EXPECTED_CATALOGUE_SHA256 = "f333bc7dda6fc5aa0de25336f641d4d444b601be0ff27ab59c9853361f6d1d92"


class CatalogueError(ValueError):
    """Raised when a raw-host catalogue violates an exact condition."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CatalogueError(message)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def canonical_digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def partial_matchings(edges: set[Edge]) -> list[tuple[Edge, ...]]:
    edge_list = sorted(edges)
    output: list[tuple[Edge, ...]] = []

    def recurse(
        index: int,
        chosen: list[Edge],
        used_left: set[int],
        used_right: set[int],
    ) -> None:
        if index == len(edge_list):
            output.append(tuple(chosen))
            return
        recurse(index + 1, chosen, used_left, used_right)
        left, right = edge_list[index]
        if left not in used_left and right not in used_right:
            chosen.append((left, right))
            used_left.add(left)
            used_right.add(right)
            recurse(index + 1, chosen, used_left, used_right)
            used_right.remove(right)
            used_left.remove(left)
            chosen.pop()

    recurse(0, [], set(), set())
    return output


def perfect_matchings(side: int, forbidden: set[Edge]) -> list[tuple[int, ...]]:
    return [
        permutation
        for permutation in permutations(range(side))
        if all((left, permutation[left]) not in forbidden for left in range(side))
    ]


def collinear(first: Point, second: Point, third: Point) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def response_triples(permutation: tuple[int, ...]) -> int:
    points = [(left, permutation[left]) for left in range(len(permutation))]
    return sum(collinear(*triple) for triple in combinations(points, 3))


def host_identity(side: int, deletion: tuple[Edge, ...]) -> str:
    core = {"side": side, "deletion_edges": [list(edge) for edge in deletion]}
    return f"s{side}-{canonical_digest(core)[:16]}"


def build_host_record(side: int, deletion: tuple[Edge, ...]) -> dict[str, Any] | None:
    opposite = {(index, index) for index in range(side)}
    target = {(0, 1)}
    forbidden = opposite | target | set(deletion)
    responses = perfect_matchings(side, forbidden)
    if not responses:
        return None

    response_records = [
        {
            "permutation": list(permutation),
            "triple_count": response_triples(permutation),
        }
        for permutation in responses
    ]
    triple_histogram = Counter(record["triple_count"] for record in response_records)
    denominator = len(response_records)
    numerator = sum(record["triple_count"] for record in response_records)

    record: dict[str, Any] = {
        "host_id": host_identity(side, deletion),
        "side": side,
        "deletion_edges": [list(edge) for edge in deletion],
        "deletion_size": len(deletion),
        "forbidden_edges": [list(edge) for edge in sorted(forbidden)],
        "responses": response_records,
        "denominator": denominator,
        "rank3_numerator": numerator,
        "rank3_slack": denominator - numerator,
        "response_triple_histogram": [
            [triple_count, count]
            for triple_count, count in sorted(triple_histogram.items())
        ],
    }
    record["record_sha256"] = canonical_digest(record)
    return record


def build_catalogue() -> dict[str, Any]:
    hosts: list[dict[str, Any]] = []
    for side in (4, 5):
        opposite = {(index, index) for index in range(side)}
        target = {(0, 1)}
        admissible = {
            (left, right)
            for left in range(side)
            for right in range(side)
        } - opposite - target
        for deletion in partial_matchings(admissible):
            record = build_host_record(side, deletion)
            if record is not None:
                hosts.append(record)

    payload: dict[str, Any] = {"version": 1, "hosts": hosts}
    payload["catalogue_sha256"] = canonical_digest(
        {"version": payload["version"], "hosts": payload["hosts"]}
    )
    payload["claims"] = {
        "hosts": len(hosts),
        "side4_hosts": sum(host["side"] == 4 for host in hosts),
        "side5_hosts": sum(host["side"] == 5 for host in hosts),
        "responses": sum(host["denominator"] for host in hosts),
        "strict_hosts": sum(host["rank3_slack"] > 0 for host in hosts),
        "critical_hosts": sum(host["rank3_slack"] == 0 for host in hosts),
        "excess_hosts": sum(host["rank3_slack"] < 0 for host in hosts),
        "unique_host_ids": len({host["host_id"] for host in hosts}),
        "unique_record_digests": len({host["record_sha256"] for host in hosts}),
    }
    return payload


def validate_catalogue(catalogue: Any) -> dict[str, int]:
    require(isinstance(catalogue, dict), "catalogue: expected object")
    expected = build_catalogue()
    require(catalogue.get("version") == 1, "version: expected 1")
    require(catalogue.get("catalogue_sha256") == expected["catalogue_sha256"],
            "catalogue_sha256: incorrect")
    require(catalogue.get("hosts") == expected["hosts"], "hosts: canonical catalogue mismatch")
    require(catalogue.get("claims") == expected["claims"], "claims: incorrect")

    claims = expected["claims"]
    require(expected["catalogue_sha256"] == EXPECTED_CATALOGUE_SHA256,
            "built-in catalogue digest drift")
    require(claims["hosts"] == 740, "expected 740 hosts")
    require(claims["side4_hosts"] == 86, "expected 86 side-four hosts")
    require(claims["side5_hosts"] == 654, "expected 654 side-five hosts")
    require(claims["responses"] == 9260, "expected 9,260 responses")
    require(
        (claims["strict_hosts"], claims["critical_hosts"], claims["excess_hosts"])
        == (651, 44, 45),
        "rank-three sign census mismatch",
    )
    require(claims["unique_host_ids"] == 740, "host-id collision")
    require(claims["unique_record_digests"] == 740, "record-digest collision")
    return dict(claims)


def run_mutation_tests() -> int:
    catalogue = build_catalogue()
    validate_catalogue(catalogue)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(catalogue)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data.update(catalogue_sha256="0" * 64))
    add(lambda data: data["claims"].update(hosts=739))
    add(lambda data: data["hosts"][0].update(host_id="s4-corrupt"))
    add(lambda data: data["hosts"][0]["deletion_edges"].append([3, 2]))
    add(lambda data: data["hosts"][0]["forbidden_edges"].pop())
    add(lambda data: data["hosts"][0]["responses"][0]["permutation"].reverse())
    add(lambda data: data["hosts"][0]["responses"][0].update(triple_count=99))
    add(lambda data: data["hosts"][0].update(denominator=99))
    add(lambda data: data["hosts"][0].update(rank3_slack=99))
    add(lambda data: data["hosts"][0].update(record_sha256="0" * 64))

    rejected = 0
    for candidate in mutations:
        try:
            validate_catalogue(candidate)
        except CatalogueError:
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted catalogue accepted")
    return rejected


def main() -> None:
    if len(sys.argv) == 3 and sys.argv[1] == "--write":
        catalogue = build_catalogue()
        validate_catalogue(catalogue)
        path = Path(sys.argv[2])
        path.write_text(
            json.dumps(catalogue, sort_keys=True, indent=2) + "\n",
            encoding="utf-8",
        )
        print(
            f"wrote canonical raw-host catalogue: {catalogue['claims']['hosts']} hosts, "
            f"{catalogue['claims']['responses']} responses, "
            f"sha256 {catalogue['catalogue_sha256']}"
        )
        return
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            catalogue = json.load(handle)
        claims = validate_catalogue(catalogue)
        print(
            "accepted canonical raw-host catalogue: "
            f"{claims['hosts']} hosts, {claims['responses']} responses, "
            f"{claims['strict_hosts']} strict, {claims['critical_hosts']} critical and "
            f"{claims['excess_hosts']} excess"
        )
        return
    if len(sys.argv) != 1:
        raise SystemExit(
            "usage: check_prime_power_canonical_raw_host_catalogue.py "
            "[catalogue.json | --write catalogue.json]"
        )

    catalogue = build_catalogue()
    claims = validate_catalogue(catalogue)
    rejected = run_mutation_tests()
    print(
        "verified canonical raw-host catalogue: "
        f"{claims['hosts']} hosts, {claims['responses']} responses, "
        f"{claims['unique_host_ids']} unique host IDs, "
        f"catalogue sha256 {catalogue['catalogue_sha256']}, "
        f"and {rejected} corrupted catalogues rejected"
    )


if __name__ == "__main__":
    main()
