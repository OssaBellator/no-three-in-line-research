#!/usr/bin/env python3
"""Compose destroyed-triple cancellation with the exact assignment coefficient bundle.

For every response Q, the checker certifies
    net_new_triples(Q) <= exported_score(Q) - unused_destroyed_credit.
It also computes the exact uniform-response numerator and the average/all-response
strictness margins.

With one JSON path, validate that certificate. With no argument, run deterministic
mixed and strict systems plus corruption tests.
"""

from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from pathlib import Path
from random import Random
from typing import Any

import check_geometric_assignment_bundle as assignment_bundle
import check_geometric_destroyed_triple_cancellation as cancellation
import check_geometric_owner_fate_manifest as owner_fate

Edge = tuple[int, int]
Prescription = tuple[Edge, ...]


class CreditError(ValueError):
    """Raised when a cancellation-certified coefficient bundle is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CreditError(message)


def parse_integer(value: Any, path: str) -> int:
    require(type(value) is int, f"{path}: expected integer")
    return value


def table_bins(bundle: dict[str, Any]) -> dict[tuple[int, str, Prescription], int]:
    output: dict[tuple[int, str, Prescription], int] = {}
    for rank, name in ((1, "edge"), (2, "pair"), (3, "triple")):
        for entry in bundle["coefficient_table"].get(name, []):
            if rank == 1:
                prescription = (tuple(entry["edge"]),)
            else:
                prescription = tuple(sorted(tuple(edge) for edge in entry["edges"]))
            output[(rank, entry["child"], prescription)] = entry["value"]
    return output


def response_contains(response: tuple[Edge, ...], prescription: Prescription) -> bool:
    response_set = set(response)
    return all(edge in response_set for edge in prescription)


def exact_scores(bundle: dict[str, Any]) -> list[int]:
    source = bundle["source_manifest"]
    responses = owner_fate.perfect_matchings(
        source["side"], {tuple(edge) for edge in source["allowed_edges"]}
    )
    bins = table_bins(bundle)
    return [
        sum(
            value
            for (_rank, _child, prescription), value in bins.items()
            if response_contains(response, prescription)
        )
        for response in responses
    ]


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    cancellation_manifest = certificate.get("cancellation_manifest")
    geometric_bundle = certificate.get("geometric_bundle")
    require(
        isinstance(cancellation_manifest, dict),
        "cancellation_manifest: expected object",
    )
    require(isinstance(geometric_bundle, dict), "geometric_bundle: expected object")

    try:
        cancellation_summary = cancellation.validate_manifest(cancellation_manifest)
    except cancellation.CancellationError as error:
        raise CreditError(f"cancellation_manifest: {error}") from error
    try:
        bundle_summary = assignment_bundle.validate_bundle(geometric_bundle)
    except assignment_bundle.BundleError as error:
        raise CreditError(f"geometric_bundle: {error}") from error

    cancellation_source = cancellation_manifest["source_manifest"]
    bundle_source = geometric_bundle["source_manifest"]
    require(
        cancellation_source == bundle_source,
        "source mismatch between cancellation and coefficient bundle",
    )
    require(
        cancellation_summary["responses"] == bundle_summary["responses"],
        "response denominator mismatch",
    )

    scores = exact_scores(geometric_bundle)
    denominator = len(scores)
    unused_credit = cancellation_summary["unused_credit"]
    exported_numerator = sum(scores)
    maximum_score = max(scores)
    average_slack = denominator * unused_credit - exported_numerator
    uniform_slack = unused_credit - maximum_score

    claims = certificate.get("claims")
    require(isinstance(claims, dict), "claims: expected object")
    expected_claims = {
        "unused_destroyed_credit": unused_credit,
        "exported_numerator": exported_numerator,
        "maximum_response_score": maximum_score,
        "average_slack": average_slack,
        "uniform_slack": uniform_slack,
    }
    for key, expected in expected_claims.items():
        observed = parse_integer(claims.get(key), f"claims.{key}")
        require(observed == expected, f"claims.{key}: incorrect")

    return {
        "responses": denominator,
        "witnesses": cancellation_summary["witnesses"],
        "deleted": cancellation_summary["deleted"],
        "unused_credit": unused_credit,
        "coefficient_bins": bundle_summary["coefficient_bins"],
        "coefficient_mass": bundle_summary["coefficient_mass"],
        "exported_numerator": exported_numerator,
        "maximum_score": maximum_score,
        "average_slack": average_slack,
        "uniform_slack": uniform_slack,
        "average_strict": int(average_slack > 0),
        "uniform_strict": int(uniform_slack > 0),
    }


def build_certificate(source: dict[str, Any], *, force_extra_credit: bool = False) -> dict[str, Any]:
    cancellation_manifest = cancellation.make_manifest(source)
    if force_extra_credit:
        points = cancellation_manifest["pre_response_points"]
        new_index = len(points)
        points.append([30000 + new_index, 20000])
        cancellation_manifest["removed_point_indices"].append(new_index)
    geometric_bundle = assignment_bundle.build_bundle(source)
    scores = exact_scores(geometric_bundle)
    cancellation_summary = cancellation.validate_manifest(cancellation_manifest)
    unused_credit = cancellation_summary["unused_credit"]
    return {
        "version": 1,
        "cancellation_manifest": cancellation_manifest,
        "geometric_bundle": geometric_bundle,
        "claims": {
            "unused_destroyed_credit": unused_credit,
            "exported_numerator": sum(scores),
            "maximum_response_score": max(scores),
            "average_slack": len(scores) * unused_credit - sum(scores),
            "uniform_slack": unused_credit - max(scores),
        },
    }


def make_all_deleted(source: dict[str, Any]) -> dict[str, Any]:
    output = copy.deepcopy(source)
    counter = 0
    for name in ("rank1", "rank2", "rank3"):
        for record in output["fates"][name]:
            record["kind"] = "deleted"
            record.pop("child", None)
            record.pop("multiplicity", None)
            record["evidence"] = f"pending-cancellation-{counter:05d}"
            counter += 1
    owner_fate.validate_manifest(output)
    return output


def random_source(random: Random) -> dict[str, Any]:
    return cancellation.random_source(random)


def run_random_tests() -> tuple[int, Counter[str]]:
    random = Random(1926)
    totals: Counter[str] = Counter()
    systems = 0

    for _ in range(200):
        certificate = build_certificate(random_source(random))
        summary = validate_certificate(certificate)
        for key in (
            "responses",
            "witnesses",
            "deleted",
            "unused_credit",
            "coefficient_bins",
            "coefficient_mass",
            "exported_numerator",
            "average_strict",
            "uniform_strict",
        ):
            totals[key] += summary[key]
        systems += 1

    for _ in range(100):
        source = make_all_deleted(random_source(random))
        certificate = build_certificate(source, force_extra_credit=True)
        summary = validate_certificate(certificate)
        require(summary["average_slack"] > 0, "strict tests: expected average improvement")
        require(summary["uniform_slack"] > 0, "strict tests: expected every response improves")
        for key in (
            "responses",
            "witnesses",
            "deleted",
            "unused_credit",
            "coefficient_bins",
            "coefficient_mass",
            "exported_numerator",
            "average_strict",
            "uniform_strict",
        ):
            totals[key] += summary[key]
        systems += 1

    require(systems == 300, "random tests: wrong system count")
    require(
        totals
        == Counter(
            {
                "witnesses": 3717,
                "responses": 2262,
                "deleted": 1766,
                "unused_credit": 1881,
                "coefficient_bins": 2014,
                "coefficient_mass": 2655,
                "exported_numerator": 4557,
                "average_strict": 129,
                "uniform_strict": 105,
            }
        ),
        "random tests: unexpected totals",
    )
    return systems, totals


def run_mutation_tests() -> int:
    random = Random(37)
    certificate = build_certificate(random_source(random))
    validate_certificate(certificate)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(certificate)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data["claims"].update(unused_destroyed_credit=999999))
    add(lambda data: data["claims"].update(exported_numerator=-1))
    add(lambda data: data["claims"].update(maximum_response_score=-1))
    add(lambda data: data["claims"].update(average_slack=0))
    add(lambda data: data["claims"].update(uniform_slack=0))
    add(lambda data: data["geometric_bundle"].update(denominator=999))
    add(lambda data: data["geometric_bundle"].update(source_sha256="0" * 64))
    add(lambda data: data["cancellation_manifest"]["cancellations"].pop())

    def change_source_only(data: dict[str, Any]) -> None:
        data["cancellation_manifest"]["source_manifest"]["entry_order"].reverse()

    add(change_source_only)

    def change_table(data: dict[str, Any]) -> None:
        table = data["geometric_bundle"]["coefficient_table"]
        for name in ("edge", "pair", "triple"):
            if table[name]:
                table[name][0]["value"] += 1
                return
        raise AssertionError("mutation source unexpectedly has no coefficient")

    add(change_table)

    rejected = 0
    for candidate in mutations:
        try:
            validate_certificate(candidate)
        except CreditError:
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted certificate accepted")
    return rejected


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit(
            "usage: check_cancellation_certified_assignment_bundle.py [certificate.json]"
        )
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            certificate = json.load(handle)
        summary = validate_certificate(certificate)
        print(
            "accepted cancellation-certified assignment bundle: "
            f"{summary['responses']} responses, {summary['witnesses']} witnesses, "
            f"{summary['unused_credit']} unused destroyed credits, "
            f"exported numerator {summary['exported_numerator']}, "
            f"average slack {summary['average_slack']} and "
            f"uniform slack {summary['uniform_slack']}"
        )
        return

    systems, totals = run_random_tests()
    rejected = run_mutation_tests()
    print(
        "verified cancellation-certified assignment bundles: "
        f"{systems} systems, {totals['witnesses']} witnesses, "
        f"{totals['deleted']} deleted witnesses, {totals['unused_credit']} unused credits, "
        f"{totals['exported_numerator']} exported numerator units, "
        f"{totals['average_strict']} average-strict and "
        f"{totals['uniform_strict']} uniform-strict systems, "
        f"and {rejected} corrupted certificates rejected"
    )


if __name__ == "__main__":
    main()
