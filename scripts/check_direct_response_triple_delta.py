#!/usr/bin/env python3
"""Validate literal before/after triple deltas for every response matching.

The input wraps one accepted response-pool cancellation bundle.  The checker
constructs the actual post-response point set B union Q for every perfect matching
Q, counts collinear triples directly, compares the result with the primitive-
witness rank decomposition, and verifies the response-pool upper bound.

With one JSON path, validate that certificate.  With no argument, run deterministic
mixed systems and corruption tests.
"""
from __future__ import annotations

import copy
import hashlib
import json
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path
from random import Random
from typing import Any

import check_geometric_owner_fate_manifest as owner_fate
import check_response_pool_cancellation_bundle as pool

Point = tuple[int, int]
Edge = tuple[int, int]
Prescription = tuple[Edge, ...]


class DirectDeltaError(ValueError):
    """Raised when a direct response-delta certificate is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise DirectDeltaError(message)


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


def collinear_triples(points: list[Point]) -> set[tuple[int, int, int]]:
    return {
        triple
        for triple in combinations(range(len(points)), 3)
        if collinear(points[triple[0]], points[triple[1]], points[triple[2]])
    }


def response_contains(response: tuple[Edge, ...], prescription: Prescription) -> bool:
    return set(prescription).issubset(response)


def witness_rank_counts(
    expected: dict[int, set[tuple[int, Prescription, tuple[int, ...]]]],
    response: tuple[Edge, ...],
) -> tuple[int, int, int]:
    return tuple(
        sum(
            response_contains(response, prescription)
            for _rank, prescription, _witness in expected[rank]
        )
        for rank in (1, 2, 3)
    )


def post_rank_counts(
    background: list[Point], response: tuple[Edge, ...]
) -> tuple[int, int, int]:
    points = background + list(response)
    split = len(background)
    counts = [0, 0, 0, 0]
    for triple in collinear_triples(points):
        response_rank = sum(index >= split for index in triple)
        counts[response_rank] += 1
    return counts[1], counts[2], counts[3]


def canonical_digest(value: Any) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def exact_records(
    pool_certificate: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    pool_summary = pool.validate_certificate(pool_certificate)
    pool_manifest = pool_certificate["pool_manifest"]
    source = pool_manifest["source_manifest"]
    bundle = pool_certificate["geometric_bundle"]

    points = [tuple(value) for value in pool_manifest["pre_response_points"]]
    removed = set(pool_manifest["removed_point_indices"])
    background = [point for index, point in enumerate(points) if index not in removed]
    require(
        background == [tuple(value) for value in source["background_points"]],
        "pool certificate surviving background mismatch",
    )

    responses = owner_fate.perfect_matchings(
        source["side"], {tuple(edge) for edge in source["allowed_edges"]}
    )
    edges, pairs, triples = owner_fate.extendable_prescriptions(responses)
    expected = owner_fate.expected_witnesses(edges, pairs, triples, background)
    scores = pool.exact_scores(bundle)
    require(len(scores) == len(responses), "response score count mismatch")

    pre_triples = collinear_triples(points)
    background_triples = collinear_triples(background)
    destroyed = len(pre_triples) - len(background_triples)
    require(
        destroyed == pool_summary["destroyed"],
        "literal destroyed-triple count disagrees with pool certificate",
    )

    unused_credit = pool_summary["pool_unused_credit"]
    records: list[dict[str, Any]] = []
    rank_totals = Counter()
    for index, response in enumerate(responses):
        rank_counts = post_rank_counts(background, response)
        witness_counts = witness_rank_counts(expected, response)
        require(
            rank_counts == witness_counts,
            f"response[{index}]: rank decomposition mismatch",
        )
        raw_occurring = sum(rank_counts)
        post_count = len(background_triples) + raw_occurring
        direct_delta = post_count - len(pre_triples)
        require(
            direct_delta == raw_occurring - destroyed,
            f"response[{index}]: direct delta identity failed",
        )
        pool_bound = scores[index] - unused_credit
        require(
            direct_delta <= pool_bound,
            f"response[{index}]: pool upper bound failed",
        )
        for rank, value in enumerate(rank_counts, start=1):
            rank_totals[rank] += value
        records.append(
            {
                "response": [list(edge) for edge in response],
                "rank_counts": list(rank_counts),
                "post_triples": post_count,
                "direct_delta": direct_delta,
                "exported_score": scores[index],
                "pool_bound": pool_bound,
            }
        )

    deltas = [record["direct_delta"] for record in records]
    minimum = min(deltas)
    minimizers = [record for record in records if record["direct_delta"] == minimum]
    selected = min(minimizers, key=lambda record: record["response"])
    summary: dict[str, Any] = {
        "responses": len(records),
        "pre_triples": len(pre_triples),
        "background_triples": len(background_triples),
        "destroyed_triples": destroyed,
        "rank1_occurrences": rank_totals[1],
        "rank2_occurrences": rank_totals[2],
        "rank3_occurrences": rank_totals[3],
        "sum_post_triples": sum(record["post_triples"] for record in records),
        "sum_direct_delta": sum(deltas),
        "minimum_delta": minimum,
        "maximum_delta": max(deltas),
        "improving_responses": sum(delta < 0 for delta in deltas),
        "nonincreasing_responses": sum(delta <= 0 for delta in deltas),
        "minimizer_count": len(minimizers),
        "selected_response": selected["response"],
        "response_records_sha256": canonical_digest(records),
    }
    return records, summary


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    pool_certificate = certificate.get("pool_certificate")
    require(isinstance(pool_certificate, dict), "pool_certificate: expected object")
    records, exact = exact_records(pool_certificate)

    claims = certificate.get("claims")
    require(isinstance(claims, dict), "claims: expected object")
    integer_keys = (
        "responses",
        "pre_triples",
        "background_triples",
        "destroyed_triples",
        "rank1_occurrences",
        "rank2_occurrences",
        "rank3_occurrences",
        "sum_post_triples",
        "sum_direct_delta",
        "minimum_delta",
        "maximum_delta",
        "improving_responses",
        "nonincreasing_responses",
        "minimizer_count",
    )
    for key in integer_keys:
        observed = parse_integer(claims.get(key), f"claims.{key}")
        require(observed == exact[key], f"claims.{key}: incorrect")

    selected = claims.get("selected_response")
    require(selected == exact["selected_response"], "claims.selected_response: incorrect")
    digest = claims.get("response_records_sha256")
    require(
        isinstance(digest, str) and digest == exact["response_records_sha256"],
        "claims.response_records_sha256: incorrect",
    )
    return {
        "responses": exact["responses"],
        "witness_occurrences": (
            exact["rank1_occurrences"]
            + exact["rank2_occurrences"]
            + exact["rank3_occurrences"]
        ),
        "improving_responses": exact["improving_responses"],
        "exact_strict": int(exact["minimum_delta"] < 0),
        "all_strict": int(exact["maximum_delta"] < 0),
        "records": len(records),
    }


def build_certificate(source: dict[str, Any]) -> dict[str, Any]:
    pool_certificate = pool.build_certificate(source)
    _records, claims = exact_records(pool_certificate)
    return {"version": 1, "pool_certificate": pool_certificate, "claims": claims}


def run_random_tests() -> tuple[int, Counter[str]]:
    random = Random(1958)
    totals: Counter[str] = Counter()
    systems = 0
    for _ in range(200):
        certificate = build_certificate(pool.colored.random_source(random))
        summary = validate_certificate(certificate)
        totals.update(summary)
        systems += 1
    for _ in range(100):
        certificate = build_certificate(pool.pool_gap_source(random))
        summary = validate_certificate(certificate)
        totals.update(summary)
        systems += 1
    require(systems == 300, "random tests: wrong system count")
    require(totals["responses"] > 0, "random tests: no responses checked")
    require(
        totals["records"] == totals["responses"],
        "random tests: incomplete direct response records",
    )
    return systems, totals


def run_mutation_tests() -> int:
    random = Random(61)
    certificate = build_certificate(pool.colored.random_source(random))
    validate_certificate(certificate)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(certificate)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data["claims"].update(pre_triples=-1))
    add(lambda data: data["claims"].update(destroyed_triples=-1))
    add(lambda data: data["claims"].update(rank1_occurrences=-1))
    add(lambda data: data["claims"].update(sum_direct_delta=999999))
    add(lambda data: data["claims"].update(minimum_delta=999999))
    add(lambda data: data["claims"].update(improving_responses=-1))
    add(lambda data: data["claims"].update(selected_response=[]))
    add(lambda data: data["claims"].update(response_records_sha256="0" * 64))
    add(lambda data: data["pool_certificate"]["claims"].update(pool_capacity=999))
    add(
        lambda data: data["pool_certificate"]["geometric_bundle"].update(
            denominator=999
        )
    )

    rejected = 0
    for candidate in mutations:
        try:
            validate_certificate(candidate)
        except (DirectDeltaError, pool.PoolCancellationError):
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted certificate accepted")
    return rejected


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit("usage: check_direct_response_triple_delta.py [certificate.json]")
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            certificate = json.load(handle)
        summary = validate_certificate(certificate)
        print(
            "accepted direct response-triple delta certificate: "
            f"{summary['responses']} responses, "
            f"{summary['witness_occurrences']} witness occurrences, "
            f"{summary['improving_responses']} improving responses"
        )
        return
    systems, totals = run_random_tests()
    rejected = run_mutation_tests()
    print(
        "verified direct response-triple deltas: "
        f"{systems} systems, {totals['responses']} literal post-response counts, "
        f"{totals['witness_occurrences']} witness occurrences, "
        f"{totals['improving_responses']} improving responses, "
        f"and {rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
