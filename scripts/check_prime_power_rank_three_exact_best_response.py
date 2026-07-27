#!/usr/bin/env python3
"""Build and validate exact rank-three best-response selectors on all 740 raw hosts.

For each canonical raw host, enumerate every surviving perfect matching, minimize the
literal number of collinear response triples, and select the lexicographically first
minimizer.

With one JSON path, validate a stored selector manifest. With ``--write PATH``, write
the canonical manifest. With no arguments, run the exact census and mutation tests.
"""

from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue

EXPECTED_SELECTOR_SHA256 = "32a20dd3772777fd6341b87f337ca5d0481d0b715e019fb11a7becd31de6e5b0"

EXPECTED_POSITIVE_MINIMUM_HOST_IDS = [
    "s4-052ffa4a215a18a9",
    "s4-0fbc34634d623179",
    "s4-e40ff6c9796d9cf7",
    "s4-108c0c435a2c6f4c",
    "s4-135a89f2e544ae23",
    "s4-0fa734ca1eb93499",
    "s4-08b391f7108d0a76",
    "s4-b61d66dda89f7836",
    "s4-59ac56096a7f627f",
    "s4-90525b9981c7d092",
    "s4-cb701ee28781f0bb",
]


class SelectorError(ValueError):
    """Raised when a rank-three selector manifest is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SelectorError(message)


def build_selector_manifest() -> dict[str, Any]:
    source = catalogue.build_catalogue()
    catalogue.validate_catalogue(source)
    hosts: list[dict[str, Any]] = []
    for host in source["hosts"]:
        minimum = min(response["triple_count"] for response in host["responses"])
        minimizers = [
            response["permutation"]
            for response in host["responses"]
            if response["triple_count"] == minimum
        ]
        hosts.append(
            {
                "host_id": host["host_id"],
                "catalogue_record_sha256": host["record_sha256"],
                "side": host["side"],
                "denominator": host["denominator"],
                "rank3_numerator": host["rank3_numerator"],
                "rank3_slack": host["rank3_slack"],
                "minimum_response_triples": minimum,
                "minimizer_count": len(minimizers),
                "selected_response": min(minimizers),
                "zero_rank3_response": minimum == 0,
                "response_triple_histogram": host["response_triple_histogram"],
            }
        )

    payload: dict[str, Any] = {
        "version": 1,
        "source_catalogue_sha256": source["catalogue_sha256"],
        "hosts": hosts,
    }
    payload["selector_sha256"] = catalogue.canonical_digest(payload)
    payload["claims"] = {
        "hosts": len(hosts),
        "zero_minimum_hosts": sum(record["minimum_response_triples"] == 0 for record in hosts),
        "positive_minimum_hosts": sum(record["minimum_response_triples"] > 0 for record in hosts),
        "side4_zero_minimum_hosts": sum(
            record["side"] == 4 and record["minimum_response_triples"] == 0
            for record in hosts
        ),
        "side4_positive_minimum_hosts": sum(
            record["side"] == 4 and record["minimum_response_triples"] > 0
            for record in hosts
        ),
        "side5_zero_minimum_hosts": sum(
            record["side"] == 5 and record["minimum_response_triples"] == 0
            for record in hosts
        ),
        "strict_zero_minimum_hosts": sum(
            record["rank3_slack"] > 0 and record["minimum_response_triples"] == 0
            for record in hosts
        ),
        "critical_zero_minimum_hosts": sum(
            record["rank3_slack"] == 0 and record["minimum_response_triples"] == 0
            for record in hosts
        ),
        "excess_zero_minimum_hosts": sum(
            record["rank3_slack"] < 0 and record["minimum_response_triples"] == 0
            for record in hosts
        ),
        "exceptional_zero_minimum_hosts": sum(
            record["rank3_slack"] <= 0 and record["minimum_response_triples"] == 0
            for record in hosts
        ),
        "exceptional_positive_minimum_hosts": sum(
            record["rank3_slack"] <= 0 and record["minimum_response_triples"] > 0
            for record in hosts
        ),
        "minimum_distribution": [
            [minimum, count]
            for minimum, count in sorted(
                Counter(record["minimum_response_triples"] for record in hosts).items()
            )
        ],
        "positive_minimum_host_ids": [
            record["host_id"]
            for record in hosts
            if record["minimum_response_triples"] > 0
        ],
    }
    return payload


def validate_selector_manifest(manifest: Any) -> dict[str, Any]:
    require(isinstance(manifest, dict), "manifest: expected object")
    expected = build_selector_manifest()
    require(manifest.get("version") == 1, "version: expected 1")
    require(
        manifest.get("source_catalogue_sha256") == expected["source_catalogue_sha256"],
        "source_catalogue_sha256: incorrect",
    )
    require(manifest.get("selector_sha256") == expected["selector_sha256"],
            "selector_sha256: incorrect")
    require(manifest.get("hosts") == expected["hosts"], "hosts: selector table mismatch")
    require(manifest.get("claims") == expected["claims"], "claims: incorrect")

    claims = expected["claims"]
    require(expected["selector_sha256"] == EXPECTED_SELECTOR_SHA256,
            "built-in selector digest drift")
    require(claims["hosts"] == 740, "expected 740 hosts")
    require((claims["zero_minimum_hosts"], claims["positive_minimum_hosts"]) == (729, 11),
            "zero/positive minimum census mismatch")
    require(
        (
            claims["side4_zero_minimum_hosts"],
            claims["side4_positive_minimum_hosts"],
            claims["side5_zero_minimum_hosts"],
        ) == (75, 11, 654),
        "side-specific minimum census mismatch",
    )
    require(
        (
            claims["strict_zero_minimum_hosts"],
            claims["critical_zero_minimum_hosts"],
            claims["excess_zero_minimum_hosts"],
        ) == (651, 44, 34),
        "sign-specific zero-response census mismatch",
    )
    require(
        (
            claims["exceptional_zero_minimum_hosts"],
            claims["exceptional_positive_minimum_hosts"],
        ) == (78, 11),
        "exceptional-host selector census mismatch",
    )
    require(claims["minimum_distribution"] == [[0, 729], [1, 9], [4, 2]],
            "minimum response-triple distribution mismatch")
    require(claims["positive_minimum_host_ids"] == EXPECTED_POSITIVE_MINIMUM_HOST_IDS,
            "positive-minimum hard-core host list mismatch")
    return copy.deepcopy(claims)


def run_mutation_tests() -> int:
    manifest = build_selector_manifest()
    validate_selector_manifest(manifest)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(manifest)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data.update(selector_sha256="0" * 64))
    add(lambda data: data.update(source_catalogue_sha256="0" * 64))
    add(lambda data: data["claims"].update(zero_minimum_hosts=728))
    add(lambda data: data["hosts"][0].update(host_id="s4-corrupt"))
    add(lambda data: data["hosts"][0].update(minimum_response_triples=99))
    add(lambda data: data["hosts"][0].update(minimizer_count=99))
    add(lambda data: data["hosts"][0]["selected_response"].reverse())
    add(lambda data: data["hosts"][0].update(zero_rank3_response=False))
    add(lambda data: data["hosts"][0]["response_triple_histogram"].pop())
    add(lambda data: data["claims"]["positive_minimum_host_ids"].reverse())

    rejected = 0
    for candidate in mutations:
        try:
            validate_selector_manifest(candidate)
        except (SelectorError, catalogue.CatalogueError):
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted manifest accepted")
    return rejected


def main() -> None:
    if len(sys.argv) == 3 and sys.argv[1] == "--write":
        manifest = build_selector_manifest()
        validate_selector_manifest(manifest)
        Path(sys.argv[2]).write_text(
            json.dumps(manifest, sort_keys=True, indent=2) + "\n", encoding="utf-8"
        )
        print(
            f"wrote rank-three selector manifest: "
            f"{manifest['claims']['hosts']} hosts, "
            f"{manifest['claims']['zero_minimum_hosts']} zero-minimum hosts, "
            f"sha256 {manifest['selector_sha256']}"
        )
        return
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            manifest = json.load(handle)
        claims = validate_selector_manifest(manifest)
        print(
            "accepted rank-three selector manifest: "
            f"{claims['zero_minimum_hosts']} zero-minimum hosts and "
            f"{claims['positive_minimum_hosts']} positive-minimum hosts"
        )
        return
    if len(sys.argv) != 1:
        raise SystemExit(
            "usage: check_prime_power_rank_three_exact_best_response.py "
            "[manifest.json | --write manifest.json]"
        )

    manifest = build_selector_manifest()
    claims = validate_selector_manifest(manifest)
    rejected = run_mutation_tests()
    print(
        "verified exact rank-three best responses: "
        f"{claims['hosts']} hosts, minimum distribution "
        f"{claims['minimum_distribution']}, "
        f"{claims['exceptional_zero_minimum_hosts']} of 89 exceptional hosts "
        f"have a zero-rank-three response, selector sha256 "
        f"{manifest['selector_sha256']}, and {rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
