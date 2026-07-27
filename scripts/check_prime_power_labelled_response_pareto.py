#!/usr/bin/env python3
"""Validate exact labelled response vectors and Pareto pruning.

A geometric assignment bundle exports labelled coefficient bins indexed by response
prescriptions.  For each perfect response matching Q this checker reconstructs the
complete nonnegative child vector v(Q), verifies that its coordinate sum is the
exported scalar score, removes duplicate vectors, identifies the exact componentwise
Pareto frontier, and validates a deterministic strictly-positive weighted selector.

With one JSON path, validate a certificate. With no argument, run deterministic tests.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from pathlib import Path
from random import Random
from typing import Any

import check_geometric_assignment_bundle as assignment
import check_geometric_owner_fate_manifest as owner_fate

Edge = tuple[int, int]
Prescription = tuple[Edge, ...]


class LabelledParetoError(ValueError):
    """Raised when a labelled response Pareto certificate is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise LabelledParetoError(message)


def response_contains(response: tuple[Edge, ...], prescription: Prescription) -> bool:
    return set(prescription).issubset(response)


def table_bins(bundle: dict[str, Any]) -> list[tuple[str, Prescription, int]]:
    output: list[tuple[str, Prescription, int]] = []
    table = bundle["coefficient_table"]
    for name, rank in (("edge", 1), ("pair", 2), ("triple", 3)):
        for entry in table[name]:
            if rank == 1:
                prescription = (tuple(entry["edge"]),)
            else:
                prescription = tuple(sorted(tuple(edge) for edge in entry["edges"]))
            output.append((entry["child"], prescription, entry["value"]))
    return output


def dominates(first: tuple[int, ...], second: tuple[int, ...]) -> bool:
    return all(left <= right for left, right in zip(first, second)) and any(
        left < right for left, right in zip(first, second)
    )


def exact_records(bundle: dict[str, Any], weights: dict[str, int]) -> dict[str, Any]:
    summary = assignment.validate_bundle(bundle)
    source = bundle["source_manifest"]
    responses = owner_fate.perfect_matchings(
        source["side"], {tuple(edge) for edge in source["allowed_edges"]}
    )
    require(len(responses) == summary["responses"], "response denominator mismatch")

    children = sorted(
        state["id"]
        for state in source["states"]
        if isinstance(state, dict) and isinstance(state.get("id"), str)
    )
    require(children, "source has no child states")
    require(set(weights) == set(children), "weights must name every source child exactly")
    for child in children:
        require(type(weights[child]) is int and weights[child] > 0,
                f"weights.{child}: expected positive integer")

    bins = table_bins(bundle)
    records: list[dict[str, Any]] = []
    for response in responses:
        vector_by_child = {child: 0 for child in children}
        for child, prescription, value in bins:
            if response_contains(response, prescription):
                vector_by_child[child] += value
        vector = tuple(vector_by_child[child] for child in children)
        scalar = sum(vector)
        weighted = sum(weights[child] * vector_by_child[child] for child in children)
        records.append(
            {
                "response": [list(edge) for edge in response],
                "child_vector": list(vector),
                "exported_scalar_score": scalar,
                "weighted_score": weighted,
            }
        )

    vector_to_responses: dict[tuple[int, ...], list[list[list[int]]]] = {}
    for record in records:
        vector_to_responses.setdefault(tuple(record["child_vector"]), []).append(record["response"])
    unique_vectors = sorted(vector_to_responses)
    pareto_vectors = [
        vector
        for vector in unique_vectors
        if not any(dominates(other, vector) for other in unique_vectors)
    ]
    pareto_set = set(pareto_vectors)
    for record in records:
        record["pareto"] = int(tuple(record["child_vector"]) in pareto_set)

    minimum_weighted = min(record["weighted_score"] for record in records)
    weighted_minimizers = [record for record in records if record["weighted_score"] == minimum_weighted]
    weighted_selected = min(weighted_minimizers, key=lambda record: record["response"])
    require(weighted_selected["pareto"] == 1,
            "strictly positive weighted minimizer is not Pareto-minimal")

    scalar_minimum = min(record["exported_scalar_score"] for record in records)
    scalar_minimizers = [record for record in records if record["exported_scalar_score"] == scalar_minimum]
    scalar_selected = min(scalar_minimizers, key=lambda record: record["response"])

    vector_records = [
        {
            "child_vector": list(vector),
            "responses": sorted(vector_to_responses[vector]),
            "pareto": int(vector in pareto_set),
        }
        for vector in unique_vectors
    ]
    claims = {
        "responses": len(records),
        "children": len(children),
        "coefficient_bins": summary["coefficient_bins"],
        "coefficient_mass": summary["coefficient_mass"],
        "unique_vectors": len(unique_vectors),
        "pareto_vectors": len(pareto_vectors),
        "pareto_responses": sum(record["pareto"] for record in records),
        "dominated_responses": sum(not record["pareto"] for record in records),
        "scalar_minimum": scalar_minimum,
        "scalar_minimizer_count": len(scalar_minimizers),
        "scalar_selected_response": scalar_selected["response"],
        "weighted_minimum": minimum_weighted,
        "weighted_minimizer_count": len(weighted_minimizers),
        "weighted_selected_response": weighted_selected["response"],
        "weighted_selected_vector": weighted_selected["child_vector"],
        "weighted_selected_is_pareto": weighted_selected["pareto"],
        "response_records_sha256": assignment.canonical_digest(records),
        "vector_records_sha256": assignment.canonical_digest(vector_records),
    }
    return {
        "children": children,
        "response_records": records,
        "vector_records": vector_records,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    bundle = certificate.get("geometric_bundle")
    weights = certificate.get("child_weights")
    require(isinstance(bundle, dict), "geometric_bundle: expected object")
    require(isinstance(weights, dict), "child_weights: expected object")
    exact = exact_records(bundle, weights)
    require(certificate.get("children") == exact["children"], "children: incorrect")
    require(certificate.get("response_records") == exact["response_records"],
            "response_records: incorrect")
    require(certificate.get("vector_records") == exact["vector_records"],
            "vector_records: incorrect")
    require(certificate.get("claims") == exact["claims"], "claims: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == assignment.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {
        "responses": claims["responses"],
        "children": claims["children"],
        "vectors": claims["unique_vectors"],
        "pareto_vectors": claims["pareto_vectors"],
        "pareto_responses": claims["pareto_responses"],
        "dominated_responses": claims["dominated_responses"],
        "coefficient_mass": claims["coefficient_mass"],
    }


def build_certificate(bundle: dict[str, Any], weights: dict[str, int]) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "geometric_bundle": bundle,
        "child_weights": dict(sorted(weights.items())),
    }
    exact = exact_records(bundle, certificate["child_weights"])
    certificate["children"] = exact["children"]
    certificate["response_records"] = exact["response_records"]
    certificate["vector_records"] = exact["vector_records"]
    certificate["claims"] = exact["claims"]
    certificate["certificate_sha256"] = assignment.canonical_digest(certificate)
    return certificate


def random_weights(bundle: dict[str, Any], random: Random) -> dict[str, int]:
    return {
        state["id"]: random.randint(1, 7)
        for state in bundle["source_manifest"]["states"]
        if isinstance(state, dict) and isinstance(state.get("id"), str)
    }


def run_random_tests() -> tuple[int, Counter[str], Counter[int]]:
    random = Random(2078)
    totals: Counter[str] = Counter()
    pareto_sizes: Counter[int] = Counter()
    for _ in range(300):
        bundle = assignment.build_bundle(assignment.random_source(random))
        certificate = build_certificate(bundle, random_weights(bundle, random))
        summary = validate_certificate(certificate)
        totals.update(summary)
        pareto_sizes[summary["pareto_vectors"]] += 1
    require(totals["responses"] > 0, "random tests: no responses")
    require(totals["pareto_responses"] > 0, "random tests: no Pareto responses")
    return 300, totals, pareto_sizes


def run_mutation_tests() -> int:
    random = Random(107)
    bundle = assignment.build_bundle(assignment.random_source(random))
    certificate = build_certificate(bundle, random_weights(bundle, random))
    validate_certificate(certificate)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(certificate)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data.update(certificate_sha256="0" * 64))
    add(lambda data: data.update(version=2))
    first_child = certificate["children"][0]
    add(lambda data: data["child_weights"].update({first_child: 0}))
    add(lambda data: data["child_weights"].pop(first_child))
    add(lambda data: data["children"].reverse())
    add(lambda data: data["response_records"][0]["child_vector"].append(999))
    add(lambda data: data["response_records"][0].update(weighted_score=-1))
    add(lambda data: data["response_records"][0].update(pareto=1-data["response_records"][0]["pareto"]))
    add(lambda data: data["vector_records"].pop())
    add(lambda data: data["claims"].update(unique_vectors=999))
    add(lambda data: data["claims"]["weighted_selected_response"].reverse())
    add(lambda data: data["geometric_bundle"].update(denominator=999))

    rejected = 0
    for candidate in mutations:
        try:
            validate_certificate(candidate)
        except (LabelledParetoError, assignment.BundleError, owner_fate.FateError):
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted certificate accepted")
    return rejected


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit("usage: check_prime_power_labelled_response_pareto.py [certificate.json]")
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            certificate = json.load(handle)
        summary = validate_certificate(certificate)
        print(
            "accepted labelled response Pareto certificate: "
            f"{summary['responses']} responses, {summary['pareto_vectors']} Pareto vectors"
        )
        return
    systems, totals, pareto_sizes = run_random_tests()
    rejected = run_mutation_tests()
    print(
        "verified labelled response Pareto certificates: "
        f"{systems} systems, {totals['responses']} responses, {totals['vectors']} unique vectors, "
        f"{totals['pareto_vectors']} Pareto vectors, {totals['dominated_responses']} dominated responses, "
        f"Pareto-size distribution {sorted(pareto_sizes.items())}, and {rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
