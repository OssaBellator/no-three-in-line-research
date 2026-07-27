#!/usr/bin/env python3
"""Validate the exact decomposition of response-pool upper-bound slack.

For each response Q,

    (B(Q)-U_pool) - DeltaPsi(Q)
      = (K-d(Q)) + domination_surplus(Q).

The first term is unused simultaneous deletion capacity.  The second is the explicit
multiplicity inflation of dominated witnesses.  There is no other gap between the
literal before/after triple count and the response-pool coefficient bound.

With one JSON path, validate a certificate.  With no argument, run deterministic
mixed, exact-only, and corruption tests.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from pathlib import Path
from random import Random
from typing import Any

import check_direct_response_triple_delta as direct
import check_geometric_owner_fate_manifest as owner_fate
import check_response_pool_cancellation_bundle as pool

Edge = tuple[int, int]
Prescription = tuple[Edge, ...]


class GapDecompositionError(ValueError):
    """Raised when a pool-gap decomposition certificate is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise GapDecompositionError(message)


def parse_integer(value: Any, path: str) -> int:
    require(type(value) is int, f"{path}: expected integer")
    return value


def response_contains(response: tuple[Edge, ...], prescription: Prescription) -> bool:
    return set(prescription).issubset(response)


def fate_prescription(rank: int, record: dict[str, Any]) -> Prescription:
    if rank == 1:
        return (tuple(record["response"]),)
    return tuple(sorted(tuple(edge) for edge in record["response"]))


def fate_profiles(
    source: dict[str, Any],
) -> tuple[list[Prescription], list[tuple[Prescription, int]]]:
    deleted: list[Prescription] = []
    nondeleted: list[tuple[Prescription, int]] = []
    for rank, name in ((1, "rank1"), (2, "rank2"), (3, "rank3")):
        for record in source["fates"].get(name, []):
            prescription = fate_prescription(rank, record)
            kind = record["kind"]
            if kind == "deleted":
                deleted.append(prescription)
                continue
            multiplicity = record.get("multiplicity", 1)
            nondeleted.append((prescription, multiplicity))
    return deleted, nondeleted


def exact_gap_records(
    direct_certificate: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    direct.validate_certificate(direct_certificate)
    direct_records, direct_claims = direct.exact_records(
        direct_certificate["pool_certificate"]
    )
    pool_certificate = direct_certificate["pool_certificate"]
    pool_summary = pool.validate_certificate(pool_certificate)
    source = pool_certificate["pool_manifest"]["source_manifest"]
    responses = owner_fate.perfect_matchings(
        source["side"], {tuple(edge) for edge in source["allowed_edges"]}
    )
    require(len(responses) == len(direct_records), "response count mismatch")

    deleted, nondeleted = fate_profiles(source)
    capacity = pool_summary["pool_capacity"]
    unused_credit = pool_summary["pool_unused_credit"]
    output: list[dict[str, Any]] = []
    totals = Counter()
    for index, (response, record) in enumerate(zip(responses, direct_records)):
        deleted_load = sum(
            response_contains(response, prescription) for prescription in deleted
        )
        unit_export = sum(
            response_contains(response, prescription)
            for prescription, _multiplicity in nondeleted
        )
        domination_surplus = sum(
            multiplicity - 1
            for prescription, multiplicity in nondeleted
            if response_contains(response, prescription)
        )
        exported_score = record["exported_score"]
        require(
            exported_score == unit_export + domination_surplus,
            f"response[{index}]: exported score decomposition failed",
        )
        capacity_slack = capacity - deleted_load
        require(
            capacity_slack >= 0,
            f"response[{index}]: deleted load exceeds pool capacity",
        )
        observed_gap = record["pool_bound"] - record["direct_delta"]
        expected_gap = capacity_slack + domination_surplus
        require(
            observed_gap == expected_gap,
            f"response[{index}]: gap identity failed",
        )
        require(
            record["pool_bound"] == exported_score - unused_credit,
            f"response[{index}]: pool bound reconstruction failed",
        )
        output.append(
            {
                "response": record["response"],
                "deleted_load": deleted_load,
                "capacity_slack": capacity_slack,
                "unit_export": unit_export,
                "domination_surplus": domination_surplus,
                "direct_delta": record["direct_delta"],
                "pool_bound": record["pool_bound"],
                "bound_gap": observed_gap,
            }
        )
        totals["deleted_load"] += deleted_load
        totals["capacity_slack"] += capacity_slack
        totals["unit_export"] += unit_export
        totals["domination_surplus"] += domination_surplus
        totals["bound_gap"] += observed_gap

    denominator = len(responses)
    exported_numerator = pool_summary["exported_numerator"]
    pool_average_slack = denominator * unused_credit - exported_numerator
    exact_average_slack = -direct_claims["sum_direct_delta"]
    require(
        exact_average_slack == pool_average_slack + totals["bound_gap"],
        "global average gap identity failed",
    )
    require(
        totals["bound_gap"]
        == totals["capacity_slack"] + totals["domination_surplus"],
        "global gap components do not sum",
    )
    claims: dict[str, Any] = {
        "responses": denominator,
        "pool_capacity": capacity,
        "unused_credit": unused_credit,
        "total_deleted_load": totals["deleted_load"],
        "total_capacity_slack": totals["capacity_slack"],
        "total_unit_export": totals["unit_export"],
        "total_domination_surplus": totals["domination_surplus"],
        "total_bound_gap": totals["bound_gap"],
        "minimum_bound_gap": min(record["bound_gap"] for record in output),
        "maximum_bound_gap": max(record["bound_gap"] for record in output),
        "pool_average_slack": pool_average_slack,
        "exact_average_slack": exact_average_slack,
        "pool_average_strict": int(pool_average_slack > 0),
        "exact_average_strict": int(exact_average_slack > 0),
        "exact_only_average_strict": int(
            exact_average_slack > 0 >= pool_average_slack
        ),
        "direct_minimum_delta": direct_claims["minimum_delta"],
        "direct_improving_responses": direct_claims["improving_responses"],
        "gap_records_sha256": direct.canonical_digest(output),
    }
    return output, claims


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    direct_certificate = certificate.get("direct_certificate")
    require(isinstance(direct_certificate, dict), "direct_certificate: expected object")
    records, exact = exact_gap_records(direct_certificate)
    claims = certificate.get("claims")
    require(isinstance(claims, dict), "claims: expected object")

    integer_keys = (
        "responses",
        "pool_capacity",
        "unused_credit",
        "total_deleted_load",
        "total_capacity_slack",
        "total_unit_export",
        "total_domination_surplus",
        "total_bound_gap",
        "minimum_bound_gap",
        "maximum_bound_gap",
        "pool_average_slack",
        "exact_average_slack",
        "pool_average_strict",
        "exact_average_strict",
        "exact_only_average_strict",
        "direct_minimum_delta",
        "direct_improving_responses",
    )
    for key in integer_keys:
        observed = parse_integer(claims.get(key), f"claims.{key}")
        require(observed == exact[key], f"claims.{key}: incorrect")
    digest = claims.get("gap_records_sha256")
    require(
        isinstance(digest, str) and digest == exact["gap_records_sha256"],
        "claims.gap_records_sha256: incorrect",
    )
    return {
        "responses": exact["responses"],
        "bound_gap": exact["total_bound_gap"],
        "capacity_slack": exact["total_capacity_slack"],
        "domination_surplus": exact["total_domination_surplus"],
        "exact_average_strict": exact["exact_average_strict"],
        "exact_only_average_strict": exact["exact_only_average_strict"],
        "records": len(records),
    }


def build_certificate(source: dict[str, Any]) -> dict[str, Any]:
    direct_certificate = direct.build_certificate(source)
    _records, claims = exact_gap_records(direct_certificate)
    return {"version": 1, "direct_certificate": direct_certificate, "claims": claims}


def inflate_recurrent_multiplicities(
    source: dict[str, Any], multiplicity: int
) -> dict[str, Any]:
    output = copy.deepcopy(source)
    counter = 0
    for name in ("rank1", "rank2", "rank3"):
        for record in output["fates"][name]:
            if record["kind"] not in {"retained", "dominated"}:
                continue
            record["kind"] = "dominated"
            record["multiplicity"] = multiplicity
            record["evidence"] = f"explicit-regression-upper-{counter:05d}"
            counter += 1
    owner_fate.validate_manifest(output)
    return output


def run_random_tests() -> tuple[int, Counter[str]]:
    random = Random(1966)
    totals: Counter[str] = Counter()
    systems = 0
    for _ in range(200):
        certificate = build_certificate(pool.colored.random_source(random))
        summary = validate_certificate(certificate)
        totals.update(summary)
        systems += 1
    for _ in range(100):
        source = inflate_recurrent_multiplicities(
            pool.pool_gap_source(random), 1000
        )
        certificate = build_certificate(source)
        summary = validate_certificate(certificate)
        totals.update(summary)
        systems += 1
    require(systems == 300, "random tests: wrong system count")
    require(
        totals["responses"] == totals["records"],
        "random tests: incomplete records",
    )
    require(
        totals["bound_gap"]
        == totals["capacity_slack"] + totals["domination_surplus"],
        "random tests: aggregate gap identity failed",
    )
    require(
        totals["exact_only_average_strict"] > 0,
        "random tests: expected exact-only strict cases",
    )
    return systems, totals


def run_mutation_tests() -> int:
    random = Random(67)
    certificate = build_certificate(pool.colored.random_source(random))
    validate_certificate(certificate)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(certificate)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data["claims"].update(total_deleted_load=-1))
    add(lambda data: data["claims"].update(total_capacity_slack=-1))
    add(lambda data: data["claims"].update(total_domination_surplus=-1))
    add(lambda data: data["claims"].update(total_bound_gap=-1))
    add(lambda data: data["claims"].update(pool_average_slack=999999))
    add(lambda data: data["claims"].update(exact_average_slack=999999))
    add(
        lambda data: data["claims"].update(
            exact_only_average_strict=
            1 - data["claims"]["exact_only_average_strict"]
        )
    )
    add(lambda data: data["claims"].update(gap_records_sha256="0" * 64))
    add(
        lambda data: data["direct_certificate"]["claims"].update(
            minimum_delta=999999
        )
    )
    add(
        lambda data: data["direct_certificate"]["pool_certificate"]["claims"].update(
            pool_capacity=999999
        )
    )

    rejected = 0
    for candidate in mutations:
        try:
            validate_certificate(candidate)
        except (
            GapDecompositionError,
            direct.DirectDeltaError,
            pool.PoolCancellationError,
        ):
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted certificate accepted")
    return rejected


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit(
            "usage: check_response_pool_gap_decomposition.py [certificate.json]"
        )
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            certificate = json.load(handle)
        summary = validate_certificate(certificate)
        print(
            "accepted response-pool gap decomposition: "
            f"{summary['responses']} responses, total gap {summary['bound_gap']}, "
            f"capacity slack {summary['capacity_slack']}, "
            f"domination surplus {summary['domination_surplus']}"
        )
        return
    systems, totals = run_random_tests()
    rejected = run_mutation_tests()
    print(
        "verified response-pool gap decompositions: "
        f"{systems} systems, {totals['responses']} response identities, "
        f"total gap {totals['bound_gap']} = capacity {totals['capacity_slack']} "
        f"+ domination {totals['domination_surplus']}, "
        f"{totals['exact_only_average_strict']} exact-only average certificates, "
        f"and {rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
