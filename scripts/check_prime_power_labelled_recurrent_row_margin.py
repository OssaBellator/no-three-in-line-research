#!/usr/bin/env python3
"""Validate exact labelled recurrent-row margins over a linked operation.

One certificate composes a linked literal operation, the exact labelled response-vector
exposure certificate over the same source, one certified positive child-weight vector,
response-local routed credits, a fixed load and a parent row budget.

Passing this checker proves exact integer accounting only. It does not prove that the
credit routes are semantically legal or that the parent budget extends to a global SCC
Lyapunov vector.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from pathlib import Path
from random import Random
from typing import Any

import check_prime_power_background_signature as signature
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_labelled_weight_exposure as exposure
import check_prime_power_linked_operation_selector as linked


class RowMarginError(ValueError):
    """Raised when a labelled recurrent-row margin certificate is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RowMarginError(message)


def response_key(response: list[list[int]]) -> tuple[tuple[int, int], ...]:
    require(isinstance(response, list), "response: expected list")
    edges = tuple(tuple(edge) for edge in response)
    require(
        all(len(edge) == 2 and all(type(value) is int for value in edge) for edge in edges),
        "response: expected integer edges",
    )
    return edges


def exact_credit_record(record: dict[str, Any], children: list[str], destroyed: int) -> dict[str, Any]:
    response = record.get("response")
    raw_routes = record.get("credit_routes")
    require(isinstance(response, list), "credit record response: expected list")
    require(
        isinstance(raw_routes, dict) and tuple(raw_routes) == tuple(children),
        "credit_routes: exact ordered child keys required",
    )
    routes: dict[str, int] = {}
    for child in children:
        value = raw_routes[child]
        require(type(value) is int and value >= 0, f"credit_routes.{child}: expected nonnegative integer")
        routes[child] = value
    units = sum(routes.values())
    require(units <= destroyed, "credit_routes: routed units exceed destroyed-current-triple budget")
    output = {"response": response, "credit_routes": routes, "routed_units": units}
    output["credit_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    linked_certificate = certificate.get("linked_operation_certificate")
    exposure_certificate = certificate.get("weight_exposure_certificate")
    require(isinstance(linked_certificate, dict), "linked_operation_certificate: expected object")
    require(isinstance(exposure_certificate, dict), "weight_exposure_certificate: expected object")

    linked.validate_certificate(linked_certificate)
    exposure.validate_certificate(exposure_certificate)
    linked_claims = linked.exact_composition(linked_certificate)["claims"]
    exposure_exact = exposure.exact(exposure_certificate["geometric_bundle"])

    direct_bundle = linked_certificate["direct_delta_certificate"]["pool_certificate"]["geometric_bundle"]
    require(
        exposure_certificate["geometric_bundle"] == direct_bundle,
        "weight exposure bundle differs from linked operation bundle",
    )
    require(
        exposure_certificate["geometric_bundle"]["source_sha256"] == linked_claims["source_sha256"],
        "source fingerprint mismatch",
    )

    children = exposure_exact["children"]
    weights = certificate.get("child_weights")
    require(
        isinstance(weights, dict) and tuple(weights) == tuple(children),
        "child_weights: exact ordered child keys required",
    )
    weight_vector: list[int] = []
    for child in children:
        value = weights[child]
        require(type(value) is int and value > 0, f"child_weights.{child}: expected positive integer")
        weight_vector.append(value)

    supported_classes = [
        record
        for record in exposure_exact["pareto_classifications"]
        if record["classification"] == "positive-weight-supported"
        and record["certificate"]["weights"] == weight_vector
    ]
    require(supported_classes, "child_weights: not one of the exact positive-support certificates")
    supported_vectors = {tuple(record["child_vector"]) for record in supported_classes}
    pareto_vectors = {
        tuple(record["child_vector"]) for record in exposure_exact["pareto_classifications"]
    }

    fixed_load = certificate.get("fixed_load")
    parent_budget = certificate.get("parent_budget")
    require(type(fixed_load) is int and fixed_load >= 0, "fixed_load: expected nonnegative integer")
    require(type(parent_budget) is int and parent_budget > 0, "parent_budget: expected positive integer")

    destroyed = linked_claims["destroyed_current_triples"]
    raw_credit_records = certificate.get("response_credit_records")
    require(isinstance(raw_credit_records, list), "response_credit_records: expected list")
    credit_records = [exact_credit_record(record, children, destroyed) for record in raw_credit_records]
    require(
        credit_records == sorted(credit_records, key=lambda record: record["response"]),
        "response_credit_records: canonical response order required",
    )
    require(
        len({response_key(record["response"]) for record in credit_records}) == len(credit_records),
        "response_credit_records: duplicate response",
    )
    credits_by_response = {response_key(record["response"]): record for record in credit_records}

    response_vectors = exposure_exact["response_vectors"]
    require(
        set(credits_by_response) == {response_key(record["response"]) for record in response_vectors},
        "response_credit_records: must cover every response exactly",
    )

    row_records: list[dict[str, Any]] = []
    total_routed_units = 0
    total_weighted_credit = 0
    for response_record in response_vectors:
        key = response_key(response_record["response"])
        credit = credits_by_response[key]
        vector = response_record["child_vector"]
        weighted_child_load = sum(weight * value for weight, value in zip(weight_vector, vector))
        weighted_credit = sum(weights[child] * credit["credit_routes"][child] for child in children)
        row_load = fixed_load + weighted_child_load - weighted_credit
        margin = parent_budget - row_load
        total_routed_units += credit["routed_units"]
        total_weighted_credit += weighted_credit
        row_records.append(
            {
                "response": response_record["response"],
                "child_vector": vector,
                "pareto_before_credit": int(tuple(vector) in pareto_vectors),
                "stored_support_certificate_matches_weight": int(tuple(vector) in supported_vectors),
                "weighted_child_load": weighted_child_load,
                "credit_routes": credit["credit_routes"],
                "routed_units": credit["routed_units"],
                "weighted_credit": weighted_credit,
                "fixed_load": fixed_load,
                "row_load": row_load,
                "parent_budget": parent_budget,
                "margin": margin,
            }
        )

    minimum_load = min(record["row_load"] for record in row_records)
    minimizers = [record for record in row_records if record["row_load"] == minimum_load]
    selected = min(minimizers, key=lambda record: record["response"])
    maximum_margin = parent_budget - minimum_load
    require(maximum_margin == max(record["margin"] for record in row_records), "margin/load duality failed")

    uncredited_loads = [fixed_load + record["weighted_child_load"] for record in row_records]
    uncredited_minimum = min(uncredited_loads)
    uncredited_minimizers = [
        record for record in row_records if fixed_load + record["weighted_child_load"] == uncredited_minimum
    ]
    require(
        all(record["pareto_before_credit"] for record in uncredited_minimizers),
        "positive weighted minimizer lost Pareto status",
    )

    claims = {
        "host_id": linked_claims["host_id"],
        "fibre_id": linked_claims["fibre_id"],
        "source_sha256": linked_claims["source_sha256"],
        "responses": len(row_records),
        "children": len(children),
        "destroyed_current_triples": destroyed,
        "fixed_load": fixed_load,
        "parent_budget": parent_budget,
        "uncredited_minimum_load": uncredited_minimum,
        "uncredited_minimizer_count": len(uncredited_minimizers),
        "minimum_row_load": minimum_load,
        "minimum_row_load_count": len(minimizers),
        "selected_response": selected["response"],
        "selected_child_vector": selected["child_vector"],
        "selected_pareto_before_credit": selected["pareto_before_credit"],
        "selected_stored_support_certificate_matches_weight": selected[
            "stored_support_certificate_matches_weight"
        ],
        "maximum_margin": maximum_margin,
        "strict_row": int(maximum_margin > 0),
        "critical_row": int(maximum_margin == 0),
        "excess_row": int(maximum_margin < 0),
        "total_routed_units": total_routed_units,
        "total_weighted_credit": total_weighted_credit,
        "maximum_response_routed_units": max(record["routed_units"] for record in row_records),
        "row_records_sha256": catalogue.canonical_digest(row_records),
        "credit_records_sha256": catalogue.canonical_digest(credit_records),
        "weight_exposure_sha256": exposure_certificate["certificate_sha256"],
        "linked_operation_sha256": linked_certificate["certificate_sha256"],
    }
    return {"response_credit_records": credit_records, "row_records": row_records, "claims": claims}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    require(
        certificate.get("response_credit_records") == exact["response_credit_records"],
        "response_credit_records: incorrect",
    )
    require(certificate.get("row_records") == exact["row_records"], "row_records: incorrect")
    require(certificate.get("claims") == exact["claims"], "claims: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(
        certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
        "certificate_sha256: incorrect",
    )
    claims = exact["claims"]
    return {
        "responses": claims["responses"],
        "children": claims["children"],
        "destroyed": claims["destroyed_current_triples"],
        "routed_units": claims["total_routed_units"],
        "weighted_credit": claims["total_weighted_credit"],
        "margin": claims["maximum_margin"],
        "strict": claims["strict_row"],
        "critical": claims["critical_row"],
        "excess": claims["excess_row"],
        "selected_pareto": claims["selected_pareto_before_credit"],
        "selected_support_match": claims["selected_stored_support_certificate_matches_weight"],
    }


def build_certificate(
    linked_certificate: dict[str, Any],
    exposure_certificate: dict[str, Any],
    child_weights: dict[str, int],
    fixed_load: int,
    parent_budget: int,
    routes: dict[tuple[tuple[int, int], ...], dict[str, int]],
) -> dict[str, Any]:
    children = exposure_certificate["children"]
    destroyed = linked.exact_composition(linked_certificate)["claims"]["destroyed_current_triples"]
    credit_records = []
    for response_record in exposure_certificate["response_vectors"]:
        key = response_key(response_record["response"])
        credit_records.append(
            exact_credit_record(
                {
                    "response": response_record["response"],
                    "credit_routes": routes.get(key, {child: 0 for child in children}),
                },
                children,
                destroyed,
            )
        )
    credit_records.sort(key=lambda record: record["response"])
    certificate: dict[str, Any] = {
        "version": 1,
        "linked_operation_certificate": linked_certificate,
        "weight_exposure_certificate": exposure_certificate,
        "child_weights": {child: child_weights[child] for child in children},
        "fixed_load": fixed_load,
        "parent_budget": parent_budget,
        "response_credit_records": credit_records,
    }
    exact = exact_certificate(certificate)
    certificate["row_records"] = exact["row_records"]
    certificate["claims"] = exact["claims"]
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def first_supported_weights(exposure_certificate: dict[str, Any]) -> dict[str, int]:
    for classification in exposure_certificate["pareto_classifications"]:
        if classification["classification"] == "positive-weight-supported":
            return dict(zip(exposure_certificate["children"], classification["certificate"]["weights"]))
    raise RowMarginError("synthetic exposure unexpectedly has no supported Pareto vector")


def run_random_tests() -> tuple[int, Counter[str], Counter[int]]:
    random = Random(2142)
    source = catalogue.build_catalogue()
    totals: Counter[str] = Counter()
    margin_distribution: Counter[int] = Counter()
    systems = 0
    for index in range(100):
        host = random.choice(source["hosts"])
        background = signature.random_background(host["side"], random)
        policy = "canonical-rank3-selector" if index % 2 == 0 else "declared-response"
        linked_certificate = linked.build_certificate(host, background, random, policy)
        bundle = linked_certificate["direct_delta_certificate"]["pool_certificate"]["geometric_bundle"]
        exposure_certificate = exposure.build_certificate(bundle)
        weights = first_supported_weights(exposure_certificate)
        destroyed = linked.exact_composition(linked_certificate)["claims"]["destroyed_current_triples"]
        routes: dict[tuple[tuple[int, int], ...], dict[str, int]] = {}
        children = exposure_certificate["children"]
        for response_record in exposure_certificate["response_vectors"]:
            units = {child: 0 for child in children}
            if destroyed and random.random() < 0.35:
                child = random.choice(children)
                units[child] = random.randrange(0, destroyed + 1)
            routes[response_key(response_record["response"])] = units
        fixed_load = random.randrange(0, 4)
        uncredited = [
            fixed_load
            + sum(weights[child] * value for child, value in zip(children, record["child_vector"]))
            for record in exposure_certificate["response_vectors"]
        ]
        baseline = min(uncredited)
        parent_budget = max(1, baseline + random.choice((-1, 0, 1, 2)))
        summary = validate_certificate(
            build_certificate(
                linked_certificate,
                exposure_certificate,
                weights,
                fixed_load,
                parent_budget,
                routes,
            )
        )
        totals.update(summary)
        margin_distribution[summary["margin"]] += 1
        systems += 1
    require(
        totals["strict"] + totals["critical"] + totals["excess"] == systems,
        "row sign partition failed",
    )
    return systems, totals, margin_distribution


def run_mutation_tests() -> int:
    random = Random(149)
    host = catalogue.build_catalogue()["hosts"][300]
    linked_certificate = linked.build_certificate(
        host, signature.random_background(host["side"], random), random, "canonical-rank3-selector"
    )
    bundle = linked_certificate["direct_delta_certificate"]["pool_certificate"]["geometric_bundle"]
    exposure_certificate = exposure.build_certificate(bundle)
    weights = first_supported_weights(exposure_certificate)
    certificate = build_certificate(linked_certificate, exposure_certificate, weights, 1, 5, {})
    validate_certificate(certificate)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(certificate)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data.update(certificate_sha256="0" * 64))
    add(lambda data: data.update(version=2))
    first_child = certificate["weight_exposure_certificate"]["children"][0]
    add(lambda data: data["child_weights"].update({first_child: 0}))
    add(lambda data: data["child_weights"].pop(first_child))
    add(lambda data: data.update(fixed_load=-1))
    add(lambda data: data.update(parent_budget=0))
    add(lambda data: data["response_credit_records"].reverse())
    add(lambda data: data["response_credit_records"][0]["credit_routes"].update({first_child: 999}))
    add(lambda data: data["response_credit_records"][0].update(credit_record_sha256="f" * 64))
    add(lambda data: data["row_records"][0].update(margin=999))
    add(lambda data: data["claims"].update(maximum_margin=999))
    add(lambda data: data["linked_operation_certificate"].update(certificate_sha256="0" * 64))

    rejected = 0
    for candidate in mutations:
        try:
            validate_certificate(candidate)
        except (
            RowMarginError,
            exposure.ExposureError,
            linked.LinkedOperationError,
            catalogue.CatalogueError,
        ):
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted row-margin certificate accepted")
    return rejected


def main() -> None:
    if len(sys.argv) == 2:
        certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        print(validate_certificate(certificate))
        return
    require(len(sys.argv) == 1, "usage: check_prime_power_labelled_recurrent_row_margin.py [certificate.json]")
    systems, totals, margins = run_random_tests()
    rejected = run_mutation_tests()
    print(
        "verified labelled recurrent-row margins: "
        f"{systems} systems, {totals['responses']} response rows, {totals['children']} child coordinates, "
        f"{totals['destroyed']} destroyed units, {totals['routed_units']} routed units, "
        f"sign split {totals['strict']}/{totals['critical']}/{totals['excess']}, "
        f"margin distribution {sorted(margins.items())}, and {rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
