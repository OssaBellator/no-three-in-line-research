#!/usr/bin/env python3
"""Compose conflict-colored destroyed-triple cancellation with exact coefficients.

The checker computes the gain over globally injective reservation and the exact
average/all-response strictness margins. With no argument it runs deterministic
mixed, reuse-strict, and corruption tests.
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
import check_geometric_conflict_colored_cancellation as colored
import check_geometric_owner_fate_manifest as owner_fate

Edge = tuple[int, int]
Prescription = tuple[Edge, ...]


class ColoredBundleError(ValueError):
    """Raised when a conflict-colored coefficient bundle is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ColoredBundleError(message)


def parse_integer(value: Any, path: str) -> int:
    require(type(value) is int, f"{path}: expected integer")
    return value


def response_contains(response: tuple[Edge, ...], prescription: Prescription) -> bool:
    return set(prescription).issubset(response)


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
    colored_manifest = certificate.get("colored_cancellation_manifest")
    geometric_bundle = certificate.get("geometric_bundle")
    require(isinstance(colored_manifest, dict), "colored_cancellation_manifest: expected object")
    require(isinstance(geometric_bundle, dict), "geometric_bundle: expected object")

    try:
        colored_summary = colored.validate_manifest(colored_manifest)
    except colored.ColoredCancellationError as error:
        raise ColoredBundleError(f"colored_cancellation_manifest: {error}") from error
    try:
        bundle_summary = assignment_bundle.validate_bundle(geometric_bundle)
    except assignment_bundle.BundleError as error:
        raise ColoredBundleError(f"geometric_bundle: {error}") from error

    source = colored_manifest["source_manifest"]
    require(source == geometric_bundle["source_manifest"], "source mismatch")
    require(colored_summary["responses"] == bundle_summary["responses"], "response denominator mismatch")

    scores = exact_scores(geometric_bundle)
    denominator = len(scores)
    exported_numerator = sum(scores)
    maximum_score = max(scores)
    destroyed = colored_summary["destroyed"]
    deleted = colored_summary["deleted"]
    used = colored_summary["used_credits"]
    saved = colored_summary["saved_credits"]
    unused = colored_summary["unused_credit"]

    injective_unused = destroyed - deleted
    average_slack = denominator * unused - exported_numerator
    uniform_slack = unused - maximum_score
    injective_average_slack = denominator * injective_unused - exported_numerator
    injective_uniform_slack = injective_unused - maximum_score
    average_gain = denominator * saved
    uniform_gain = saved
    require(average_slack == injective_average_slack + average_gain, "average gain identity failed")
    require(uniform_slack == injective_uniform_slack + uniform_gain, "uniform gain identity failed")

    claims = certificate.get("claims")
    require(isinstance(claims, dict), "claims: expected object")
    expected_claims = {
        "used_credits": used,
        "saved_credits": saved,
        "unused_credit": unused,
        "injective_unused_credit": injective_unused,
        "exported_numerator": exported_numerator,
        "maximum_response_score": maximum_score,
        "average_slack": average_slack,
        "uniform_slack": uniform_slack,
        "injective_average_slack": injective_average_slack,
        "injective_uniform_slack": injective_uniform_slack,
        "average_slack_gain": average_gain,
        "uniform_slack_gain": uniform_gain,
        "average_strict": int(average_slack > 0),
        "uniform_strict": int(uniform_slack > 0),
        "reuse_only_average_strict": int(average_slack > 0 >= injective_average_slack),
        "reuse_only_uniform_strict": int(uniform_slack > 0 >= injective_uniform_slack),
        "optimal": colored_summary["optimal"],
    }
    for key, expected in expected_claims.items():
        observed = parse_integer(claims.get(key), f"claims.{key}")
        require(observed == expected, f"claims.{key}: incorrect")

    return {
        "responses": denominator,
        "witnesses": colored_summary["witnesses"],
        "deleted": deleted,
        "used_credits": used,
        "saved_credits": saved,
        "unused_credit": unused,
        "coefficient_bins": bundle_summary["coefficient_bins"],
        "coefficient_mass": bundle_summary["coefficient_mass"],
        "exported_numerator": exported_numerator,
        "average_slack_gain": average_gain,
        "uniform_slack_gain": uniform_gain,
        "average_strict": int(average_slack > 0),
        "uniform_strict": int(uniform_slack > 0),
        "reuse_only_average_strict": int(average_slack > 0 >= injective_average_slack),
        "reuse_only_uniform_strict": int(uniform_slack > 0 >= injective_uniform_slack),
        "optimal": colored_summary["optimal"],
    }


def make_all_deleted(source: dict[str, Any]) -> dict[str, Any]:
    output = copy.deepcopy(source)
    counter = 0
    for name in ("rank1", "rank2", "rank3"):
        for record in output["fates"][name]:
            record["kind"] = "deleted"
            record.pop("child", None)
            record.pop("multiplicity", None)
            record["evidence"] = f"colored-deletion-{counter:05d}"
            counter += 1
    owner_fate.validate_manifest(output)
    return output


def build_certificate(source: dict[str, Any]) -> dict[str, Any]:
    colored_manifest = colored.build_manifest(source)
    geometric_bundle = assignment_bundle.build_bundle(source)
    colored_summary = colored.validate_manifest(colored_manifest)
    scores = exact_scores(geometric_bundle)
    denominator = len(scores)
    destroyed = colored_summary["destroyed"]
    deleted = colored_summary["deleted"]
    used = colored_summary["used_credits"]
    saved = colored_summary["saved_credits"]
    unused = colored_summary["unused_credit"]
    numerator = sum(scores)
    maximum = max(scores)
    injective_unused = destroyed - deleted
    average_slack = denominator * unused - numerator
    uniform_slack = unused - maximum
    injective_average = denominator * injective_unused - numerator
    injective_uniform = injective_unused - maximum
    return {
        "version": 1,
        "colored_cancellation_manifest": colored_manifest,
        "geometric_bundle": geometric_bundle,
        "claims": {
            "used_credits": used,
            "saved_credits": saved,
            "unused_credit": unused,
            "injective_unused_credit": injective_unused,
            "exported_numerator": numerator,
            "maximum_response_score": maximum,
            "average_slack": average_slack,
            "uniform_slack": uniform_slack,
            "injective_average_slack": injective_average,
            "injective_uniform_slack": injective_uniform,
            "average_slack_gain": denominator * saved,
            "uniform_slack_gain": saved,
            "average_strict": int(average_slack > 0),
            "uniform_strict": int(uniform_slack > 0),
            "reuse_only_average_strict": int(average_slack > 0 >= injective_average),
            "reuse_only_uniform_strict": int(uniform_slack > 0 >= injective_uniform),
            "optimal": colored_summary["optimal"],
        },
    }


def small_reuse_source(random: Random) -> dict[str, Any]:
    for _ in range(200):
        source = colored.random_source(random)
        all_deleted = make_all_deleted(source)
        deleted = colored.deleted_evidence_and_prescriptions(all_deleted)
        if 2 <= len(deleted) <= 14:
            responses = owner_fate.perfect_matchings(
                all_deleted["side"], {tuple(edge) for edge in all_deleted["allowed_edges"]}
            )
            conflicts = colored.conflict_pairs(sorted(deleted), deleted, responses)
            coloring, _clique = colored.exact_small_coloring(sorted(deleted), conflicts)
            used = 0 if not coloring else max(coloring.values()) + 1
            if used < len(deleted):
                return all_deleted
    raise AssertionError("could not generate small credit-reuse source")


def run_random_tests() -> tuple[int, Counter[str]]:
    random = Random(1942)
    totals: Counter[str] = Counter()
    systems = 0
    for _ in range(200):
        certificate = build_certificate(colored.random_source(random))
        summary = validate_certificate(certificate)
        for key in (
            "responses", "witnesses", "deleted", "used_credits", "saved_credits",
            "unused_credit", "coefficient_bins", "coefficient_mass", "exported_numerator",
            "average_slack_gain", "uniform_slack_gain", "average_strict", "uniform_strict",
            "reuse_only_average_strict", "reuse_only_uniform_strict", "optimal",
        ):
            totals[key] += summary[key]
        systems += 1

    for _ in range(100):
        certificate = build_certificate(small_reuse_source(random))
        summary = validate_certificate(certificate)
        require(summary["saved_credits"] > 0, "reuse tests: expected saved credits")
        require(summary["reuse_only_average_strict"] == 1, "reuse tests: expected reuse-only average strictness")
        require(summary["reuse_only_uniform_strict"] == 1, "reuse tests: expected reuse-only uniform strictness")
        for key in (
            "responses", "witnesses", "deleted", "used_credits", "saved_credits",
            "unused_credit", "coefficient_bins", "coefficient_mass", "exported_numerator",
            "average_slack_gain", "uniform_slack_gain", "average_strict", "uniform_strict",
            "reuse_only_average_strict", "reuse_only_uniform_strict", "optimal",
        ):
            totals[key] += summary[key]
        systems += 1

    require(systems == 300, "random tests: wrong system count")
    require(totals["saved_credits"] > 0, "random tests: expected saved credits")
    require(totals["reuse_only_average_strict"] >= 100, "random tests: missing reuse-only average cases")
    require(totals["reuse_only_uniform_strict"] >= 100, "random tests: missing reuse-only uniform cases")
    return systems, totals


def run_mutation_tests() -> int:
    random = Random(47)
    certificate = build_certificate(colored.random_source(random))
    validate_certificate(certificate)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(certificate)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data["claims"].update(saved_credits=-1))
    add(lambda data: data["claims"].update(average_slack_gain=0))
    add(lambda data: data["claims"].update(uniform_slack_gain=0))
    add(lambda data: data["claims"].update(injective_unused_credit=9999))
    add(lambda data: data["claims"].update(reuse_only_average_strict=1 - data["claims"]["reuse_only_average_strict"]))
    add(lambda data: data["geometric_bundle"].update(denominator=999))
    add(lambda data: data["geometric_bundle"].update(source_sha256="0" * 64))
    add(lambda data: data["colored_cancellation_manifest"]["credit_assignments"].pop())

    def change_source_only(data: dict[str, Any]) -> None:
        data["colored_cancellation_manifest"]["source_manifest"]["entry_order"].reverse()

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
        except ColoredBundleError:
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted certificate accepted")
    return rejected


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit("usage: check_conflict_colored_cancellation_bundle.py [certificate.json]")
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            certificate = json.load(handle)
        summary = validate_certificate(certificate)
        print(
            "accepted conflict-colored cancellation bundle: "
            f"{summary['responses']} responses, {summary['saved_credits']} saved credits, "
            f"average gain {summary['average_slack_gain']}, uniform gain {summary['uniform_slack_gain']}, "
            f"reuse-only average strict={summary['reuse_only_average_strict']} and "
            f"reuse-only uniform strict={summary['reuse_only_uniform_strict']}"
        )
        return
    systems, totals = run_random_tests()
    rejected = run_mutation_tests()
    print(
        "verified conflict-colored cancellation bundles: "
        f"{systems} systems, {totals['deleted']} deleted witnesses, "
        f"{totals['saved_credits']} saved credits, average slack gain {totals['average_slack_gain']}, "
        f"uniform slack gain {totals['uniform_slack_gain']}, "
        f"{totals['reuse_only_average_strict']} reuse-only average-strict and "
        f"{totals['reuse_only_uniform_strict']} reuse-only uniform-strict systems, "
        f"and {rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
