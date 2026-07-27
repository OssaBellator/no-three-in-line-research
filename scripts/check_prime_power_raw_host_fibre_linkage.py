#!/usr/bin/env python3
"""Validate canonical raw-host linkage for owner/provenance fibre sources.

A linked fibre contains one accepted owner/fate source, a canonical raw-host ID and
record digest, one response policy, a selected response, and the complete parent
state-label tuple.  The checker reconstructs the catalogue host from the source's
allowed edge set, compares the entire response list and denominator, and verifies
canonical rank-three selection when that policy is declared.

This checker proves linkage and finite equality only.  Nonempty state labels are not
proof of collision, local-line, interface, root, thin, CRT, or provenance semantics.

With one JSON path, validate a stored certificate. With no argument, run deterministic
mixed-policy and corruption tests.
"""
from __future__ import annotations

import copy
import json
import sys
from functools import lru_cache
from pathlib import Path
from random import Random
from typing import Any

import check_geometric_owner_fate_manifest as owner_fate
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_rank_three_exact_best_response as selector

LABEL_KEYS = (
    "provenance",
    "collision",
    "local_line",
    "interface",
    "root",
    "thin",
    "crt",
)
POLICIES = {"canonical-rank3-selector", "declared-response"}


class LinkageError(ValueError):
    """Raised when a raw-host fibre linkage certificate is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise LinkageError(message)


def response_to_permutation(response: tuple[tuple[int, int], ...], side: int) -> list[int]:
    by_left = {left: right for left, right in response}
    require(set(by_left) == set(range(side)), "response does not cover every left vertex")
    return [by_left[left] for left in range(side)]


def canonical_source_digest(source: Any) -> str:
    return catalogue.canonical_digest(source)


@lru_cache(maxsize=1)
def host_maps() -> tuple[dict[str, dict[str, Any]], dict[frozenset[tuple[int, int]], dict[str, Any]]]:
    source = catalogue.build_catalogue()
    catalogue.validate_catalogue(source)
    by_id = {record["host_id"]: record for record in source["hosts"]}
    by_allowed: dict[frozenset[tuple[int, int]], dict[str, Any]] = {}
    for record in source["hosts"]:
        side = record["side"]
        grid = {(left, right) for left in range(side) for right in range(side)}
        forbidden = {tuple(edge) for edge in record["forbidden_edges"]}
        allowed = frozenset(grid - forbidden)
        require(allowed not in by_allowed, "catalogue allowed-edge collision")
        by_allowed[allowed] = record
    return by_id, by_allowed


@lru_cache(maxsize=1)
def selector_map() -> dict[str, dict[str, Any]]:
    manifest = selector.build_selector_manifest()
    selector.validate_selector_manifest(manifest)
    return {record["host_id"]: record for record in manifest["hosts"]}


def exact_linkage(certificate: dict[str, Any]) -> dict[str, Any]:
    source_manifest = certificate.get("source_manifest")
    require(isinstance(source_manifest, dict), "source_manifest: expected object")
    source_summary = owner_fate.validate_manifest(source_manifest)

    by_id, by_allowed = host_maps()
    side = source_manifest["side"]
    allowed = frozenset(tuple(edge) for edge in source_manifest["allowed_edges"])
    require(allowed in by_allowed, "source allowed edges do not identify a canonical raw host")
    identified = by_allowed[allowed]

    host_id = certificate.get("host_id")
    require(isinstance(host_id, str) and host_id in by_id, "host_id: unknown canonical host")
    require(by_id[host_id] == identified, "host_id: does not match source allowed edges")
    require(
        certificate.get("catalogue_record_sha256") == identified["record_sha256"],
        "catalogue_record_sha256: incorrect",
    )
    require(side == identified["side"], "source side mismatch")

    source_responses = owner_fate.perfect_matchings(side, set(allowed))
    source_permutations = [response_to_permutation(response, side) for response in source_responses]
    catalogue_permutations = [record["permutation"] for record in identified["responses"]]
    require(source_permutations == catalogue_permutations, "complete response list mismatch")
    require(source_summary["responses"] == identified["denominator"], "denominator mismatch")

    policy = certificate.get("policy")
    require(policy in POLICIES, "policy: unsupported")
    selected_response = certificate.get("selected_response")
    require(selected_response in catalogue_permutations, "selected_response: not available")

    selector_record = selector_map()[host_id]
    canonical_selected = selector_record["selected_response"]
    if policy == "canonical-rank3-selector":
        require(selected_response == canonical_selected,
                "selected_response: not the canonical rank-three selector")

    labels = certificate.get("state_labels")
    require(isinstance(labels, dict), "state_labels: expected object")
    require(tuple(labels.keys()) == LABEL_KEYS, "state_labels: exact ordered keys required")
    for key in LABEL_KEYS:
        require(isinstance(labels[key], str) and labels[key].strip(),
                f"state_labels.{key}: nonempty string required")

    source_sha256 = canonical_source_digest(source_manifest)
    require(certificate.get("source_sha256") == source_sha256, "source_sha256: incorrect")
    label_sha256 = catalogue.canonical_digest(labels)
    exact_fibre_id = f"{host_id}:{catalogue.canonical_digest({'source': source_sha256, 'labels': labels})[:16]}"
    require(certificate.get("fibre_id") == exact_fibre_id, "fibre_id: incorrect")

    selected_triples = catalogue.response_triples(tuple(selected_response))
    claims = {
        "side": side,
        "denominator": identified["denominator"],
        "rank3_slack": identified["rank3_slack"],
        "canonical_rank3_minimum": selector_record["minimum_response_triples"],
        "selected_rank3_triples": selected_triples,
        "selected_is_canonical_minimizer": int(selected_response == canonical_selected),
        "source_responses": len(source_permutations),
        "source_witnesses": source_summary["witnesses"],
        "label_sha256": label_sha256,
        "response_list_sha256": catalogue.canonical_digest(catalogue_permutations),
    }
    return {
        "host_id": host_id,
        "record": identified,
        "source_summary": source_summary,
        "claims": claims,
        "fibre_id": exact_fibre_id,
        "source_sha256": source_sha256,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_linkage(certificate)
    require(certificate.get("claims") == exact["claims"], "claims: incorrect")

    payload = {key: value for key, value in certificate.items() if key != "linkage_sha256"}
    linkage_sha256 = catalogue.canonical_digest(payload)
    require(certificate.get("linkage_sha256") == linkage_sha256,
            "linkage_sha256: incorrect")
    return {
        "responses": exact["claims"]["source_responses"],
        "witnesses": exact["claims"]["source_witnesses"],
        "canonical_policy": int(certificate["policy"] == "canonical-rank3-selector"),
        "declared_policy": int(certificate["policy"] == "declared-response"),
        "canonical_selected": exact["claims"]["selected_is_canonical_minimizer"],
    }


def build_certificate(
    host: dict[str, Any],
    background: list[tuple[int, int]],
    random: Random,
    policy: str,
) -> dict[str, Any]:
    side = host["side"]
    grid = {(left, right) for left in range(side) for right in range(side)}
    forbidden = {tuple(edge) for edge in host["forbidden_edges"]}
    allowed = grid - forbidden
    source_manifest = owner_fate.make_manifest(side, allowed, background, random)

    selector_record = selector_map()[host["host_id"]]
    if policy == "canonical-rank3-selector":
        selected_response = selector_record["selected_response"]
    else:
        selected_response = random.choice(host["responses"])["permutation"]

    labels = {
        "provenance": f"prov-{host['host_id']}",
        "collision": f"collision-{random.randrange(7)}",
        "local_line": f"line-{random.randrange(11)}",
        "interface": f"interface-{random.randrange(5)}",
        "root": f"root-{random.randrange(3)}",
        "thin": f"thin-{random.randrange(4)}",
        "crt": f"crt-{side}-{random.randrange(6)}",
    }
    source_sha256 = canonical_source_digest(source_manifest)
    fibre_id = f"{host['host_id']}:{catalogue.canonical_digest({'source': source_sha256, 'labels': labels})[:16]}"
    certificate: dict[str, Any] = {
        "version": 1,
        "host_id": host["host_id"],
        "catalogue_record_sha256": host["record_sha256"],
        "fibre_id": fibre_id,
        "source_manifest": source_manifest,
        "source_sha256": source_sha256,
        "policy": policy,
        "selected_response": selected_response,
        "state_labels": labels,
    }
    exact = exact_linkage(certificate)
    certificate["claims"] = exact["claims"]
    certificate["linkage_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def random_background(side: int, random: Random) -> list[tuple[int, int]]:
    grid = {(left, right) for left in range(side) for right in range(side)}
    output: list[tuple[int, int]] = []
    target = random.randrange(0, 6)
    while len(output) < target:
        point = (random.randrange(-4, side + 5), random.randrange(-4, side + 5))
        if point not in grid and point not in output:
            output.append(point)
    return output


def run_random_tests() -> tuple[int, dict[str, int]]:
    random = Random(2014)
    source = catalogue.build_catalogue()
    totals = {
        "responses": 0,
        "witnesses": 0,
        "canonical_policy": 0,
        "declared_policy": 0,
        "canonical_selected": 0,
    }
    systems = 0
    for index in range(300):
        host = random.choice(source["hosts"])
        policy = "canonical-rank3-selector" if index % 2 == 0 else "declared-response"
        certificate = build_certificate(
            host, random_background(host["side"], random), random, policy
        )
        summary = validate_certificate(certificate)
        for key, value in summary.items():
            totals[key] += value
        systems += 1
    require(systems == 300, "random tests: wrong system count")
    require((totals["canonical_policy"], totals["declared_policy"]) == (150, 150),
            "random tests: policy split mismatch")
    require(totals["responses"] > 0, "random tests: no responses")
    return systems, totals


def run_mutation_tests() -> int:
    random = Random(71)
    host = catalogue.build_catalogue()["hosts"][100]
    certificate = build_certificate(
        host, random_background(host["side"], random), random,
        "canonical-rank3-selector",
    )
    validate_certificate(certificate)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(certificate)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data.update(linkage_sha256="0" * 64))
    add(lambda data: data.update(host_id="s4-corrupt"))
    add(lambda data: data.update(catalogue_record_sha256="0" * 40))
    add(lambda data: data.update(source_sha256="0" * 64))
    add(lambda data: data.update(fibre_id="corrupt"))
    add(lambda data: data.update(policy="unknown"))
    add(lambda data: data["selected_response"].reverse())
    add(lambda data: data["state_labels"].update(provenance=""))
    add(lambda data: data["state_labels"].pop("crt"))
    add(lambda data: data["source_manifest"]["allowed_edges"].pop())
    add(lambda data: data["claims"].update(denominator=999))
    add(lambda data: data["claims"].update(selected_rank3_triples=999))

    rejected = 0
    for candidate in mutations:
        try:
            validate_certificate(candidate)
        except (
            LinkageError,
            owner_fate.FateError,
            catalogue.CatalogueError,
            selector.SelectorError,
        ):
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted linkage accepted")
    return rejected


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit("usage: check_prime_power_raw_host_fibre_linkage.py [certificate.json]")
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            certificate = json.load(handle)
        summary = validate_certificate(certificate)
        print(
            "accepted raw-host fibre linkage: "
            f"{summary['responses']} responses, {summary['witnesses']} witnesses"
        )
        return

    systems, totals = run_random_tests()
    rejected = run_mutation_tests()
    print(
        "verified raw-host fibre linkage: "
        f"{systems} systems, {totals['responses']} response records, "
        f"{totals['witnesses']} primitive witnesses, "
        f"{totals['canonical_policy']} canonical and {totals['declared_policy']} declared policies, "
        f"and {rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
