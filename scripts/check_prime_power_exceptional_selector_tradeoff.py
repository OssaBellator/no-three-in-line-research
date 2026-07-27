#!/usr/bin/env python3
"""Validate exact scalar/rank-three selector tradeoffs on exceptional hosts.

For one exceptional raw host, survivor background B and certified destroyed threshold T,
this checker compares three response policies:

* the unrestricted full new-triple minimizer;
* the best response among raw rank-three minimizers;
* when available, the best zero-rank-three response.

The resulting nonnegative penalties and strictness thresholds are exact.  They quantify
what is lost by imposing a rank-three constraint, but do not prove labelled recurrent
contraction or operation legality.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from pathlib import Path
from random import Random
from typing import Any

import check_prime_power_background_response_selector as selector
import check_prime_power_background_signature as signature
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_exceptional_selector_chamber_worklist as worklist


class TradeoffError(ValueError):
    """Raised when an exceptional selector tradeoff certificate is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise TradeoffError(message)


def lex_first(records: list[dict[str, Any]]) -> dict[str, Any]:
    require(records, "empty response class")
    return min(records, key=lambda record: record["permutation"])


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    host_id = certificate.get("host_id")
    require(isinstance(host_id, str), "host_id: expected string")
    destroyed = certificate.get("destroyed_current_triples")
    require(type(destroyed) is int and destroyed >= 0, "destroyed_current_triples: expected nonnegative integer")

    source = catalogue.build_catalogue()
    catalogue.validate_catalogue(source)
    hosts = {host["host_id"]: host for host in source["hosts"]}
    exceptional = {record["host_id"]: record for record in worklist.build_worklist()["hosts"]}
    require(host_id in exceptional, "host_id: not one of the 89 exceptional hosts")
    host = hosts[host_id]

    raw_background = certificate.get("background_points")
    require(isinstance(raw_background, list), "background_points: expected list")
    background = [
        signature.parse_point(value, f"background_points[{index}]")
        for index, value in enumerate(raw_background)
    ]
    require(len(background) == len(set(background)), "background_points: duplicates")
    grid = {(left, right) for left in range(host["side"]) for right in range(host["side"])}
    require(not (set(background) & grid), "background_points: intersects response grid")

    selector_certificate = selector.build_certificate(host, background)
    selector.validate_certificate(selector_certificate)
    records, selector_claims = selector.exact_records(selector_certificate)
    require(records, "host has no responses")

    full_minimum = min(record["new_triples"] for record in records)
    full_minimizers = [record for record in records if record["new_triples"] == full_minimum]
    full_selected = lex_first(full_minimizers)

    rank3_minimum = min(record["rank_counts"][2] for record in records)
    rank3_records = [record for record in records if record["rank_counts"][2] == rank3_minimum]
    rank3_constrained_minimum = min(record["new_triples"] for record in rank3_records)
    rank3_constrained_minimizers = [
        record for record in rank3_records if record["new_triples"] == rank3_constrained_minimum
    ]
    rank3_selected = lex_first(rank3_constrained_minimizers)
    rank3_penalty = rank3_constrained_minimum - full_minimum
    require(rank3_penalty >= 0, "rank-three constraint penalty became negative")

    zero_records = [record for record in records if record["rank_counts"][2] == 0]
    if zero_records:
        zero_minimum = min(record["new_triples"] for record in zero_records)
        zero_minimizers = [record for record in zero_records if record["new_triples"] == zero_minimum]
        zero_selected = lex_first(zero_minimizers)
        zero_penalty: int | None = zero_minimum - full_minimum
        require(zero_penalty >= 0, "zero-rank-three constraint penalty became negative")
        zero_strict: int | None = int(zero_minimum < destroyed)
        zero_delta: int | None = zero_minimum - destroyed
    else:
        zero_minimum = None
        zero_selected = None
        zero_penalty = None
        zero_strict = None
        zero_delta = None

    response_tradeoffs = [
        {
            "permutation": record["permutation"],
            "rank_counts": record["rank_counts"],
            "new_triples": record["new_triples"],
            "delta": record["new_triples"] - destroyed,
            "full_minimizer": int(record["new_triples"] == full_minimum),
            "rank3_minimum": int(record["rank_counts"][2] == rank3_minimum),
            "rank3_constrained_minimizer": int(
                record["rank_counts"][2] == rank3_minimum
                and record["new_triples"] == rank3_constrained_minimum
            ),
            "zero_rank3": int(record["rank_counts"][2] == 0),
        }
        for record in records
    ]

    chamber_record = exceptional[host_id]
    full_chamber_member = any(
        chamber["selected_permutation"] == full_selected["permutation"]
        and worklist.chamber_holds(chamber, selector_certificate["signature"])
        for chamber in chamber_record["selector_chambers"]
    )
    if chamber_record["worklist_kind"] == "positive-minimum-hard-core":
        require(full_chamber_member, "hard-core full selector missing from chamber atlas")
    else:
        require(
            full_chamber_member == (full_selected["rank_counts"][2] == 0),
            "zero-selector chamber union disagreement",
        )

    claims = {
        "host_id": host_id,
        "side": host["side"],
        "responses": len(records),
        "background_points": len(background),
        "destroyed_current_triples": destroyed,
        "worklist_kind": chamber_record["worklist_kind"],
        "full_minimum_new_triples": full_minimum,
        "full_minimum_delta": full_minimum - destroyed,
        "full_strict_improvement": int(full_minimum < destroyed),
        "full_minimizer_count": len(full_minimizers),
        "full_selected_response": full_selected["permutation"],
        "full_selected_rank3_triples": full_selected["rank_counts"][2],
        "rank3_minimum": rank3_minimum,
        "rank3_constrained_minimum_new_triples": rank3_constrained_minimum,
        "rank3_constrained_minimum_delta": rank3_constrained_minimum - destroyed,
        "rank3_constrained_strict_improvement": int(rank3_constrained_minimum < destroyed),
        "rank3_constrained_minimizer_count": len(rank3_constrained_minimizers),
        "rank3_constrained_selected_response": rank3_selected["permutation"],
        "rank3_constraint_penalty": rank3_penalty,
        "zero_rank3_available": int(bool(zero_records)),
        "zero_rank3_responses": len(zero_records),
        "zero_constrained_minimum_new_triples": zero_minimum,
        "zero_constrained_minimum_delta": zero_delta,
        "zero_constrained_strict_improvement": zero_strict,
        "zero_constrained_selected_response": None if zero_selected is None else zero_selected["permutation"],
        "zero_constraint_penalty": zero_penalty,
        "full_selected_in_published_worklist": int(full_chamber_member),
        "selector_response_records_sha256": selector_claims["response_records_sha256"],
        "tradeoff_records_sha256": catalogue.canonical_digest(response_tradeoffs),
    }
    return {
        "background_selector_certificate": selector_certificate,
        "response_tradeoffs": response_tradeoffs,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    require(
        certificate.get("background_selector_certificate")
        == exact["background_selector_certificate"],
        "background_selector_certificate: incorrect",
    )
    require(certificate.get("response_tradeoffs") == exact["response_tradeoffs"], "response_tradeoffs: incorrect")
    require(certificate.get("claims") == exact["claims"], "claims: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(
        certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
        "certificate_sha256: incorrect",
    )
    claims = exact["claims"]
    return {
        "responses": claims["responses"],
        "background_points": claims["background_points"],
        "destroyed": claims["destroyed_current_triples"],
        "full_strict": claims["full_strict_improvement"],
        "rank3_strict": claims["rank3_constrained_strict_improvement"],
        "zero_available": claims["zero_rank3_available"],
        "zero_strict": int(claims["zero_constrained_strict_improvement"] or 0),
        "rank3_penalty": claims["rank3_constraint_penalty"],
        "zero_penalty": int(claims["zero_constraint_penalty"] or 0),
        "full_selected_rank3": claims["full_selected_rank3_triples"],
        "hard_core": int(claims["worklist_kind"] == "positive-minimum-hard-core"),
    }


def build_certificate(
    host: dict[str, Any], background: list[tuple[int, int]], destroyed_current_triples: int
) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "host_id": host["host_id"],
        "background_points": [list(point) for point in background],
        "destroyed_current_triples": destroyed_current_triples,
    }
    exact = exact_certificate(certificate)
    certificate["background_selector_certificate"] = exact["background_selector_certificate"]
    certificate["response_tradeoffs"] = exact["response_tradeoffs"]
    certificate["claims"] = exact["claims"]
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def run_random_tests() -> tuple[int, Counter[str], Counter[int], Counter[int]]:
    random = Random(2134)
    source = catalogue.build_catalogue()
    hosts = {host["host_id"]: host for host in source["hosts"]}
    exceptional = worklist.build_worklist()["hosts"]
    totals: Counter[str] = Counter()
    rank3_penalties: Counter[int] = Counter()
    zero_penalties: Counter[int] = Counter()
    for _ in range(500):
        record = random.choice(exceptional)
        host = hosts[record["host_id"]]
        background = signature.random_background(host["side"], random)
        destroyed = random.randrange(0, 9)
        summary = validate_certificate(build_certificate(host, background, destroyed))
        totals.update(summary)
        rank3_penalties[summary["rank3_penalty"]] += 1
        if summary["zero_available"]:
            zero_penalties[summary["zero_penalty"]] += 1
        require(summary["rank3_strict"] <= summary["full_strict"], "constrained strictness exceeded full strictness")
        require(summary["zero_strict"] <= summary["full_strict"], "zero-constrained strictness exceeded full strictness")
    return 500, totals, rank3_penalties, zero_penalties


def run_mutation_tests() -> int:
    random = Random(137)
    source = catalogue.build_catalogue()
    record = worklist.build_worklist()["hosts"][0]
    host = next(host for host in source["hosts"] if host["host_id"] == record["host_id"])
    certificate = build_certificate(host, signature.random_background(host["side"], random), 3)
    validate_certificate(certificate)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(certificate)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data.update(certificate_sha256="0" * 64))
    add(lambda data: data.update(version=2))
    add(lambda data: data.update(host_id="s4-corrupt"))
    add(lambda data: data.update(destroyed_current_triples=-1))
    add(lambda data: data["background_points"].append(data["background_points"][0]) if data["background_points"] else data["background_points"].append([0, 0]))
    add(lambda data: data["response_tradeoffs"].reverse())
    add(lambda data: data["response_tradeoffs"][0].update(delta=999))
    add(lambda data: data["claims"].update(full_minimum_new_triples=999))
    add(lambda data: data["claims"].update(rank3_constraint_penalty=-1))
    add(lambda data: data["claims"].update(full_selected_in_published_worklist=0))
    add(lambda data: data["background_selector_certificate"].update(selector_sha256="f" * 64))
    add(lambda data: data["claims"].update(tradeoff_records_sha256="0" * 64))

    rejected = 0
    for candidate in mutations:
        try:
            validate_certificate(candidate)
        except (
            TradeoffError,
            selector.BackgroundSelectorError,
            signature.SignatureError,
            worklist.WorklistError,
            catalogue.CatalogueError,
        ):
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted tradeoff certificate accepted")
    return rejected


def main() -> None:
    if len(sys.argv) == 2:
        certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        print(validate_certificate(certificate))
        return
    require(len(sys.argv) == 1, "usage: check_prime_power_exceptional_selector_tradeoff.py [certificate.json]")
    systems, totals, rank3_penalties, zero_penalties = run_random_tests()
    rejected = run_mutation_tests()
    print(
        "verified exceptional selector tradeoffs: "
        f"{systems} systems, {totals['responses']} responses, {totals['hard_core']} hard-core samples, "
        f"{totals['full_strict']} full-strict, {totals['rank3_strict']} rank3-constrained-strict, "
        f"{totals['zero_strict']} zero-constrained-strict, rank3 penalties {sorted(rank3_penalties.items())}, "
        f"zero penalties {sorted(zero_penalties.items())}, and {rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
