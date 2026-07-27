#!/usr/bin/env python3
"""Compose raw-host linkage, operation geometry, and the exact full selector.

A certificate contains one canonical owner/provenance fibre linkage, one literal
before/after response-delta certificate over the same source, and one exact
background-selector certificate.  The checker proves responsewise identity

    direct_delta(Q) = N_B(Q) - destroyed_current_triples

and audits the response selected by the declared parent policy against the true full
selector.  It proves finite linkage and geometry only, not rule-specific execution.
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
import check_prime_power_background_response_selector as selector
import check_prime_power_background_signature as signature
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_raw_host_fibre_linkage as linkage

class LinkedOperationError(ValueError):
    """Raised when a linked operation selector certificate is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise LinkedOperationError(message)


def response_to_permutation(response: list[list[int]], side: int) -> list[int]:
    by_left = {edge[0]: edge[1] for edge in response}
    require(set(by_left) == set(range(side)), "response does not cover every left vertex")
    return [by_left[left] for left in range(side)]


def normalize_deletion_evidence(certificate: dict[str, Any]) -> dict[str, Any]:
    output = copy.deepcopy(certificate)
    counter = 0
    for bucket in ("rank1", "rank2", "rank3"):
        for record in output["source_manifest"]["fates"][bucket]:
            if record["kind"] == "deleted":
                record["evidence"] = f"linked-operation-deletion-{counter:05d}"
                counter += 1
    source_sha256 = linkage.canonical_source_digest(output["source_manifest"])
    output["source_sha256"] = source_sha256
    output["fibre_id"] = (
        f"{output['host_id']}:"
        f"{catalogue.canonical_digest({'source': source_sha256, 'labels': output['state_labels']})[:16]}"
    )
    output.pop("claims", None)
    output.pop("linkage_sha256", None)
    output["claims"] = linkage.exact_linkage(output)["claims"]
    output["linkage_sha256"] = catalogue.canonical_digest(output)
    linkage.validate_certificate(output)
    return output


def exact_composition(certificate: dict[str, Any]) -> dict[str, Any]:
    linked = certificate.get("linkage_certificate")
    direct_certificate = certificate.get("direct_delta_certificate")
    selector_certificate = certificate.get("background_selector_certificate")
    require(isinstance(linked, dict), "linkage_certificate: expected object")
    require(isinstance(direct_certificate, dict), "direct_delta_certificate: expected object")
    require(isinstance(selector_certificate, dict), "background_selector_certificate: expected object")

    link_summary = linkage.validate_certificate(linked)
    direct_summary = direct.validate_certificate(direct_certificate)
    selector_summary = selector.validate_certificate(selector_certificate)
    linked_exact = linkage.exact_linkage(linked)
    direct_records, direct_exact = direct.exact_records(direct_certificate["pool_certificate"])
    selector_records, selector_exact = selector.exact_records(selector_certificate)

    source = linked["source_manifest"]
    direct_source = direct_certificate["pool_certificate"]["pool_manifest"]["source_manifest"]
    require(source == direct_source, "linkage/direct source mismatch")
    require(selector_certificate["host_id"] == linked["host_id"], "linkage/selector host mismatch")
    require(
        selector_certificate["catalogue_record_sha256"] == linked["catalogue_record_sha256"],
        "linkage/selector catalogue digest mismatch",
    )
    require(
        selector_certificate["background_points"] == source["background_points"],
        "selector background differs from linked source survivor background",
    )
    require(len(direct_records) == len(selector_records), "response record count mismatch")

    side = source["side"]
    response_checks = 0
    for direct_record, selector_record in zip(direct_records, selector_records):
        permutation = response_to_permutation(direct_record["response"], side)
        require(permutation == selector_record["permutation"], "response order mismatch")
        require(direct_record["rank_counts"] == selector_record["rank_counts"],
                "response rank counts mismatch")
        require(
            direct_record["direct_delta"]
            == selector_record["new_triples"] - direct_exact["destroyed_triples"],
            "response delta/threshold identity failed",
        )
        response_checks += 1

    direct_selected = response_to_permutation(direct_exact["selected_response"], side)
    require(direct_selected == selector_exact["selected_response"],
            "literal direct minimizer differs from background selector")
    require(
        direct_exact["minimum_delta"]
        == selector_exact["minimum_new_triples"] - direct_exact["destroyed_triples"],
        "minimum delta identity failed",
    )
    require(
        int(direct_exact["minimum_delta"] < 0)
        == int(selector_exact["minimum_new_triples"] < direct_exact["destroyed_triples"]),
        "strictness threshold equivalence failed",
    )

    policy_response = linked["selected_response"]
    policy_record = next(
        record for record in selector_records if record["permutation"] == policy_response
    )
    policy_penalty = policy_record["new_triples"] - selector_exact["minimum_new_triples"]
    require(policy_penalty >= 0, "policy response penalty became negative")
    policy_delta = policy_record["new_triples"] - direct_exact["destroyed_triples"]

    claims = {
        "host_id": linked["host_id"],
        "fibre_id": linked["fibre_id"],
        "policy": linked["policy"],
        "responses": len(direct_records),
        "primitive_witnesses": link_summary["witnesses"],
        "background_points": len(source["background_points"]),
        "destroyed_current_triples": direct_exact["destroyed_triples"],
        "minimum_new_triples": selector_exact["minimum_new_triples"],
        "minimum_delta": direct_exact["minimum_delta"],
        "strict_improvement": int(direct_exact["minimum_delta"] < 0),
        "full_selected_response": selector_exact["selected_response"],
        "full_minimizer_count": selector_exact["minimizer_count"],
        "raw_selector_penalty": selector_exact["selector_penalty"],
        "policy_selected_response": policy_response,
        "policy_selected_new_triples": policy_record["new_triples"],
        "policy_selected_delta": policy_delta,
        "policy_selector_penalty": policy_penalty,
        "policy_is_full_selector": int(policy_response == selector_exact["selected_response"]),
        "policy_has_minimum_value": int(policy_penalty == 0),
        "pool_capacity": direct_certificate["pool_certificate"]["claims"]["pool_capacity"],
        "pool_unused_credit": direct_certificate["pool_certificate"]["claims"]["pool_unused_credit"],
        "response_checks": response_checks,
        "source_sha256": linked_exact["source_sha256"],
        "selector_records_sha256": selector_exact["response_records_sha256"],
        "direct_records_sha256": direct_exact["response_records_sha256"],
    }
    return {
        "claims": claims,
        "link_summary": link_summary,
        "direct_summary": direct_summary,
        "selector_summary": selector_summary,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_composition(certificate)
    require(certificate.get("claims") == exact["claims"], "claims: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {
        "responses": claims["responses"],
        "witnesses": claims["primitive_witnesses"],
        "background_points": claims["background_points"],
        "destroyed": claims["destroyed_current_triples"],
        "strict": claims["strict_improvement"],
        "policy_full_selector": claims["policy_is_full_selector"],
        "policy_minimum_value": claims["policy_has_minimum_value"],
        "policy_penalty": claims["policy_selector_penalty"],
        "raw_penalty": claims["raw_selector_penalty"],
        "canonical_policy": int(claims["policy"] == "canonical-rank3-selector"),
        "declared_policy": int(claims["policy"] == "declared-response"),
        "response_checks": claims["response_checks"],
    }


def build_certificate(
    host: dict[str, Any], background: list[tuple[int, int]], random: Random, policy: str
) -> dict[str, Any]:
    linked = linkage.build_certificate(host, background, random, policy)
    linked = normalize_deletion_evidence(linked)
    direct_certificate = direct.build_certificate(linked["source_manifest"])
    selector_certificate = selector.build_certificate(host, background)
    certificate: dict[str, Any] = {
        "version": 1,
        "linkage_certificate": linked,
        "direct_delta_certificate": direct_certificate,
        "background_selector_certificate": selector_certificate,
    }
    certificate["claims"] = exact_composition(certificate)["claims"]
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def run_random_tests() -> tuple[int, Counter[str], Counter[int], Counter[int]]:
    random = Random(2062)
    source = catalogue.build_catalogue()
    totals: Counter[str] = Counter()
    policy_penalties: Counter[int] = Counter()
    raw_penalties: Counter[int] = Counter()
    systems = 0
    for index in range(240):
        host = random.choice(source["hosts"])
        background = signature.random_background(host["side"], random)
        policy = "canonical-rank3-selector" if index % 2 == 0 else "declared-response"
        certificate = build_certificate(host, background, random, policy)
        summary = validate_certificate(certificate)
        totals.update(summary)
        policy_penalties[summary["policy_penalty"]] += 1
        raw_penalties[summary["raw_penalty"]] += 1
        systems += 1
    require(totals["responses"] == totals["response_checks"], "random tests: incomplete responsewise composition")
    require((totals["canonical_policy"], totals["declared_policy"]) == (120, 120),
            "random tests: policy split mismatch")
    require(dict(totals) == {
        "responses": 2944,
        "witnesses": 3363,
        "background_points": 819,
        "destroyed": 589,
        "strict": 230,
        "policy_full_selector": 90,
        "policy_minimum_value": 106,
        "policy_penalty": 262,
        "raw_penalty": 148,
        "canonical_policy": 120,
        "declared_policy": 120,
        "response_checks": 2944,
    }, "random tests: linked-operation totals mismatch")
    require(dict(sorted(policy_penalties.items())) == {
        0: 106, 1: 74, 2: 29, 3: 9, 4: 14, 5: 5, 6: 2, 10: 1,
    }, "random tests: policy penalty distribution mismatch")
    require(dict(sorted(raw_penalties.items())) == {
        0: 153, 1: 53, 2: 24, 3: 3, 4: 3, 5: 2, 6: 1, 10: 1,
    }, "random tests: raw penalty distribution mismatch")
    return systems, totals, policy_penalties, raw_penalties


def run_mutation_tests() -> int:
    random = Random(97)
    host = catalogue.build_catalogue()["hosts"][200]
    certificate = build_certificate(host, signature.random_background(host["side"], random), random,
                                    "canonical-rank3-selector")
    validate_certificate(certificate)
    mutations: list[dict[str, Any]] = []
    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(certificate)
        mutator(candidate)
        mutations.append(candidate)
    add(lambda data: data.update(certificate_sha256="0" * 64))
    add(lambda data: data["claims"].update(responses=999))
    add(lambda data: data["claims"].update(minimum_delta=999))
    add(lambda data: data["claims"]["full_selected_response"].reverse())
    add(lambda data: data["linkage_certificate"].update(host_id="s5-corrupt"))
    add(lambda data: data["linkage_certificate"].update(source_sha256="0" * 64))
    add(lambda data: data["linkage_certificate"]["state_labels"].update(crt=""))
    add(lambda data: data["direct_delta_certificate"]["claims"].update(destroyed_triples=999))
    add(lambda data: data["direct_delta_certificate"]["claims"]["selected_response"].reverse())
    add(lambda data: data["background_selector_certificate"].update(host_id="s4-corrupt"))
    add(lambda data: data["background_selector_certificate"]["background_points"].append([0, 0]))
    add(lambda data: data["background_selector_certificate"]["claims"].update(minimum_new_triples=999))
    add(lambda data: data.update(version=2))
    add(lambda data: data["claims"].update(policy_selector_penalty=-1))
    rejected = 0
    for candidate in mutations:
        try:
            validate_certificate(candidate)
        except (
            LinkedOperationError,
            linkage.LinkageError,
            direct.DirectDeltaError,
            selector.BackgroundSelectorError,
            catalogue.CatalogueError,
        ):
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted composition accepted")
    return rejected


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit("usage: check_prime_power_linked_operation_selector.py [certificate.json]")
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            certificate = json.load(handle)
        summary = validate_certificate(certificate)
        print(
            "accepted linked operation selector: "
            f"{summary['responses']} responses, policy penalty {summary['policy_penalty']}"
        )
        return
    systems, totals, policy_penalties, raw_penalties = run_random_tests()
    rejected = run_mutation_tests()
    print(
        "verified linked operation selectors: "
        f"{systems} systems, {totals['responses']} response checks, "
        f"{totals['witnesses']} witnesses, {totals['background_points']} background points, "
        f"{totals['destroyed']} destroyed triples, {totals['strict']} strict systems, "
        f"{totals['policy_full_selector']} policy/full-selector matches, "
        f"policy penalties {sorted(policy_penalties.items())}, raw penalties {sorted(raw_penalties.items())}, "
        f"and {rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
