#!/usr/bin/env python3
"""Verify the explicit affine exchange normal form of the side-four hard core.

The eleven positive-minimum raw hosts use only two response matchings.  Nine hosts
admit both responses and two admit only the anti-diagonal response.  The two
responses differ on one alternating four-cycle, so every nontrivial full-selector
chamber is governed by one explicit integer functional.  This finite theorem does
not supply survivor signatures or labelled recurrent semantics and permanently
reports ``all_n_proved_by_checker = 0``.
"""
from __future__ import annotations

import copy
import hashlib
import json
import math
import random
from collections import Counter
from itertools import combinations, permutations, product
from typing import Any, Iterable

Edge = tuple[int, int]
Point = tuple[int, int]
Line = tuple[int, int, int]
Permutation = tuple[int, ...]

Q_ONE: Permutation = (3, 0, 1, 2)
Q_FOUR: Permutation = (3, 2, 1, 0)
EXPECTED_MANIFEST_SHA256 = "ae35c2afa6574f602ccc2bb10124c0a5743ae4d712ebd967f93e56680928b1bf"


class HardCoreExchangeError(ValueError):
    """Raised when the exact hard-core exchange normal form is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise HardCoreExchangeError(message)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def canonical_digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def partial_matchings(edges: Iterable[Edge]) -> list[tuple[Edge, ...]]:
    edge_list = sorted(edges)
    output: list[tuple[Edge, ...]] = []

    def recurse(index: int, chosen: list[Edge], used_left: set[int], used_right: set[int]) -> None:
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


def perfect_matchings(side: int, forbidden: set[Edge]) -> list[Permutation]:
    return [
        permutation
        for permutation in permutations(range(side))
        if all((left, permutation[left]) not in forbidden for left in range(side))
    ]


def points(permutation: Permutation) -> list[Point]:
    return [(left, permutation[left]) for left in range(len(permutation))]


def collinear(first: Point, second: Point, third: Point) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def response_triples(permutation: Permutation) -> list[tuple[Point, Point, Point]]:
    return [triple for triple in combinations(points(permutation), 3) if collinear(*triple)]


def normalized_line(first: Point, second: Point) -> Line:
    require(first != second, "line requires two distinct points")
    x1, y1 = first
    x2, y2 = second
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1
    divisor = math.gcd(math.gcd(abs(a), abs(b)), abs(c))
    require(divisor > 0, "degenerate line normalization")
    a //= divisor
    b //= divisor
    c //= divisor
    for value in (a, b, c):
        if value < 0:
            a, b, c = -a, -b, -c
            break
        if value > 0:
            break
    return a, b, c


def affine_row(permutation: Permutation) -> dict[str, Any]:
    response_points = points(permutation)
    cross = Counter(point for point in response_points if point[0] > 0 and point[1] > 0)
    line_coefficients = Counter(
        normalized_line(first, second)
        for first, second in combinations(response_points, 2)
    )
    return {
        "permutation": list(permutation),
        "rank1_cross_coefficients": [[list(point), value] for point, value in sorted(cross.items())],
        "rank2_line_coefficients": [[list(line), value] for line, value in sorted(line_coefficients.items())],
        "rank3_constant": len(response_triples(permutation)),
    }


def coefficient_map(records: list[list[Any]]) -> Counter[tuple[int, ...]]:
    return Counter({tuple(key): int(value) for key, value in records})


def row_difference(left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
    cross = coefficient_map(left["rank1_cross_coefficients"])
    cross.subtract(coefficient_map(right["rank1_cross_coefficients"]))
    lines = coefficient_map(left["rank2_line_coefficients"])
    lines.subtract(coefficient_map(right["rank2_line_coefficients"]))
    return {
        "left_permutation": left["permutation"],
        "right_permutation": right["permutation"],
        "rank1_cross_difference": [[list(key), value] for key, value in sorted(cross.items()) if value],
        "rank2_line_difference": [[list(key), value] for key, value in sorted(lines.items()) if value],
        "rank3_constant_difference": left["rank3_constant"] - right["rank3_constant"],
    }


def evaluate_row(row: dict[str, Any], cross_values: dict[Point, int], line_values: dict[Line, int]) -> int:
    return (
        sum(value * cross_values.get(tuple(point), 0) for point, value in row["rank1_cross_coefficients"])
        + sum(value * line_values.get(tuple(line), 0) for line, value in row["rank2_line_coefficients"])
        + int(row["rank3_constant"])
    )


def evaluate_difference(
    difference: dict[str, Any],
    cross_values: dict[Point, int],
    line_values: dict[Line, int],
) -> int:
    return (
        sum(value * cross_values.get(tuple(point), 0) for point, value in difference["rank1_cross_difference"])
        + sum(value * line_values.get(tuple(line), 0) for line, value in difference["rank2_line_difference"])
        + int(difference["rank3_constant_difference"])
    )


def host_identity(deletion: tuple[Edge, ...]) -> str:
    core = {"side": 4, "deletion_edges": [list(edge) for edge in deletion]}
    return f"s4-{canonical_digest(core)[:16]}"


def hard_core_hosts() -> list[dict[str, Any]]:
    side = 4
    diagonal = {(index, index) for index in range(side)}
    target = {(0, 1)}
    admissible = {
        (left, right)
        for left in range(side)
        for right in range(side)
    } - diagonal - target
    output: list[dict[str, Any]] = []
    for deletion in partial_matchings(admissible):
        responses = perfect_matchings(side, diagonal | target | set(deletion))
        if not responses:
            continue
        triple_counts = [len(response_triples(response)) for response in responses]
        if min(triple_counts) == 0:
            continue
        output.append(
            {
                "host_id": host_identity(deletion),
                "deletion_edges": [list(edge) for edge in deletion],
                "responses": [list(response) for response in responses],
                "response_triple_counts": triple_counts,
            }
        )
    return output


def exact_manifest() -> dict[str, Any]:
    row_one = affine_row(Q_ONE)
    row_four = affine_row(Q_FOUR)
    difference = row_difference(row_one, row_four)
    hosts = hard_core_hosts()
    for host in hosts:
        family = [tuple(response) for response in host["responses"]]
        if family == [Q_ONE, Q_FOUR]:
            host["chambers"] = [
                {"selected": list(Q_ONE), "condition": "delta_le_zero"},
                {"selected": list(Q_FOUR), "condition": "delta_gt_zero"},
            ]
        elif family == [Q_FOUR]:
            host["chambers"] = [{"selected": list(Q_FOUR), "condition": "all_signatures"}]
        else:
            raise HardCoreExchangeError(f"unexpected hard-core response family: {family}")

    payload: dict[str, Any] = {
        "version": 1,
        "responses": {"Q1": row_one, "Q4": row_four},
        "alternating_exchange": {
            "common_edges": [[0, 3], [2, 1]],
            "Q1_only_edges": [[1, 0], [3, 2]],
            "Q4_only_edges": [[1, 2], [3, 0]],
            "exchange_rows": [1, 3],
            "exchange_columns": [0, 2],
        },
        "delta_Q1_minus_Q4": difference,
        "hard_core_hosts": hosts,
    }
    payload["claims"] = {
        "hard_core_hosts": len(hosts),
        "two_response_hosts": sum(len(host["responses"]) == 2 for host in hosts),
        "one_response_hosts": sum(len(host["responses"]) == 1 for host in hosts),
        "hard_core_chambers": sum(len(host["chambers"]) for host in hosts),
        "distinct_nontrivial_chamber_functionals": 1,
        "Q1_rank3_triples": len(response_triples(Q_ONE)),
        "Q4_rank3_triples": len(response_triples(Q_FOUR)),
        "all_n_proved_by_checker": 0,
    }
    payload["manifest_sha256"] = canonical_digest(payload)
    return payload


def validate_manifest(manifest: Any) -> dict[str, int]:
    require(isinstance(manifest, dict), "manifest: expected object")
    expected = exact_manifest()
    require(manifest == expected, "manifest: canonical hard-core exchange normal form mismatch")
    claims = expected["claims"]
    require(
        claims
        == {
            "hard_core_hosts": 11,
            "two_response_hosts": 9,
            "one_response_hosts": 2,
            "hard_core_chambers": 20,
            "distinct_nontrivial_chamber_functionals": 1,
            "Q1_rank3_triples": 1,
            "Q4_rank3_triples": 4,
            "all_n_proved_by_checker": 0,
        },
        "claims: exact hard-core census mismatch",
    )
    expected_difference = {
        "left_permutation": list(Q_ONE),
        "right_permutation": list(Q_FOUR),
        "rank1_cross_difference": [
            [[1, 2], -1],
            [[3, 2], 1],
        ],
        "rank2_line_difference": [
            [[1, -1, -1], 3],
            [[1, 1, -3], -5],
            [[1, 3, -9], 1],
            [[3, 1, -3], 1],
        ],
        "rank3_constant_difference": -3,
    }
    require(expected["delta_Q1_minus_Q4"] == expected_difference, "explicit delta functional drift")
    require(
        expected["alternating_exchange"]
        == {
            "common_edges": [[0, 3], [2, 1]],
            "Q1_only_edges": [[1, 0], [3, 2]],
            "Q4_only_edges": [[1, 2], [3, 0]],
            "exchange_rows": [1, 3],
            "exchange_columns": [0, 2],
        },
        "alternating four-cycle drift",
    )
    if EXPECTED_MANIFEST_SHA256 != "TO_BE_FILLED":
        require(expected["manifest_sha256"] == EXPECTED_MANIFEST_SHA256, "built-in manifest digest drift")
    return dict(claims)


def verify_signature_cube(manifest: dict[str, Any]) -> int:
    row_one = manifest["responses"]["Q1"]
    row_four = manifest["responses"]["Q4"]
    difference = manifest["delta_Q1_minus_Q4"]
    cross_keys = [(1, 2), (3, 2)]
    line_keys = [(1, -1, -1), (1, 1, -3), (1, 3, -9), (3, 1, -3)]
    checked = 0
    for cross_pair in product(range(-2, 3), repeat=2):
        cross_values = dict(zip(cross_keys, cross_pair))
        for line_tuple in product(range(4), repeat=4):
            line_values = dict(zip(line_keys, line_tuple))
            value_one = evaluate_row(row_one, cross_values, line_values)
            value_four = evaluate_row(row_four, cross_values, line_values)
            delta = evaluate_difference(difference, cross_values, line_values)
            require(delta == value_one - value_four, "delta evaluation identity failed")
            selected = Q_ONE if value_one <= value_four else Q_FOUR
            selected_by_delta = Q_ONE if delta <= 0 else Q_FOUR
            require(selected == selected_by_delta, "lexicographic chamber partition failed")
            checked += 1
    return checked


def verify_random_signatures(manifest: dict[str, Any]) -> int:
    generator = random.Random(2722)
    row_one = manifest["responses"]["Q1"]
    row_four = manifest["responses"]["Q4"]
    difference = manifest["delta_Q1_minus_Q4"]
    all_cross = {(i, j) for i in range(1, 4) for j in range(1, 4)}
    all_lines = {
        normalized_line(first, second)
        for response in (Q_ONE, Q_FOUR)
        for first, second in combinations(points(response), 2)
    }
    for _ in range(1000):
        cross_values = {key: generator.randint(-20, 20) for key in all_cross}
        line_values = {key: generator.randint(0, 30) for key in all_lines}
        left = evaluate_row(row_one, cross_values, line_values)
        right = evaluate_row(row_four, cross_values, line_values)
        delta = evaluate_difference(difference, cross_values, line_values)
        require(delta == left - right, "random delta identity failed")
        require((left <= right) == (delta <= 0), "random weak Q1 chamber failed")
        require((right < left) == (delta > 0), "random strict Q4 chamber failed")
    return 1000


def mutation_tests() -> int:
    manifest = exact_manifest()
    validate_manifest(manifest)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(manifest)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data.update(version=2))
    add(lambda data: data.update(manifest_sha256="0" * 64))
    add(lambda data: data["claims"].update(hard_core_hosts=10))
    add(lambda data: data["responses"]["Q1"].update(rank3_constant=2))
    add(lambda data: data["responses"]["Q4"]["permutation"].reverse())
    add(lambda data: data["alternating_exchange"]["common_edges"].pop())
    add(lambda data: data["delta_Q1_minus_Q4"]["rank1_cross_difference"].pop())
    add(lambda data: data["delta_Q1_minus_Q4"].update(rank3_constant_difference=-2))
    add(lambda data: data["hard_core_hosts"].pop())
    add(lambda data: data["hard_core_hosts"][0]["chambers"][0].update(condition="delta_lt_zero"))

    rejected = 0
    for candidate in mutations:
        try:
            validate_manifest(candidate)
        except HardCoreExchangeError:
            rejected += 1
    require(rejected == len(mutations), "mutation suite accepted a corruption")
    return rejected


def main() -> None:
    manifest = exact_manifest()
    claims = validate_manifest(manifest)
    cube = verify_signature_cube(manifest)
    random_cases = verify_random_signatures(manifest)
    rejected = mutation_tests()
    print(
        json.dumps(
            {
                **claims,
                "signature_cube_cases": cube,
                "random_signature_cases": random_cases,
                "rejected_mutations": rejected,
                "manifest_sha256": manifest["manifest_sha256"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
