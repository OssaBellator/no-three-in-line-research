#!/usr/bin/env python3
"""Build and validate the canonical 89-host rank-three priority manifest.

The source is the exact 740-host canonical catalogue. Every critical or excess host
receives a stable host ID, exact response summary, minimum rank-three correction,
and deterministic exact-signature class.

With one JSON path, validate a stored manifest. With ``--write PATH``, write the
canonical manifest. With no arguments, run exact census and mutation tests.
"""

from __future__ import annotations

import copy
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue

EXPECTED_PRIORITY_SHA256 = "730d06e8fab61c302b565ad09fc63bd625c886ec521a7fc71d8b6914fe769444"


class PriorityError(ValueError):
    """Raised when an exceptional-host priority manifest is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise PriorityError(message)


def build_priority_manifest() -> dict[str, Any]:
    source = catalogue.build_catalogue()
    catalogue.validate_catalogue(source)
    exceptional_hosts: list[dict[str, Any]] = []
    class_cores: dict[str, dict[str, Any]] = {}
    class_members: dict[str, list[str]] = defaultdict(list)

    for host in source["hosts"]:
        slack = host["rank3_slack"]
        if slack > 0:
            continue
        signature_core: dict[str, Any] = {
            "side": host["side"],
            "denominator": host["denominator"],
            "rank3_slack": slack,
            "deletion_size": host["deletion_size"],
            "response_triple_histogram": host["response_triple_histogram"],
        }
        class_id = f"x-{catalogue.canonical_digest(signature_core)[:16]}"
        class_cores[class_id] = signature_core
        class_members[class_id].append(host["host_id"])
        triple_counts = [response["triple_count"] for response in host["responses"]]
        exceptional_hosts.append(
            {
                "host_id": host["host_id"],
                "signature_class_id": class_id,
                "side": host["side"],
                "deletion_edges": host["deletion_edges"],
                "deletion_size": host["deletion_size"],
                "denominator": host["denominator"],
                "rank3_numerator": host["rank3_numerator"],
                "rank3_slack": slack,
                "rank3_reduction_required": 1 - slack,
                "minimum_response_triples": min(triple_counts),
                "maximum_response_triples": max(triple_counts),
                "positive_triple_responses": sum(value > 0 for value in triple_counts),
                "response_triple_histogram": host["response_triple_histogram"],
                "catalogue_record_sha256": host["record_sha256"],
            }
        )

    exceptional_hosts.sort(
        key=lambda record: (
            -record["rank3_reduction_required"],
            record["side"],
            record["denominator"],
            record["host_id"],
        )
    )
    signature_classes = [
        {
            "signature_class_id": class_id,
            **class_cores[class_id],
            "rank3_reduction_required": 1 - class_cores[class_id]["rank3_slack"],
            "host_count": len(class_members[class_id]),
            "host_ids": sorted(class_members[class_id]),
        }
        for class_id in sorted(class_cores)
    ]

    payload: dict[str, Any] = {
        "version": 1,
        "source_catalogue_sha256": source["catalogue_sha256"],
        "exceptional_hosts": exceptional_hosts,
        "signature_classes": signature_classes,
    }
    payload["priority_sha256"] = catalogue.canonical_digest(payload)
    payload["claims"] = {
        "exceptional_hosts": len(exceptional_hosts),
        "critical_hosts": sum(record["rank3_slack"] == 0 for record in exceptional_hosts),
        "excess_hosts": sum(record["rank3_slack"] < 0 for record in exceptional_hosts),
        "side4_exceptional_hosts": sum(record["side"] == 4 for record in exceptional_hosts),
        "side5_exceptional_hosts": sum(record["side"] == 5 for record in exceptional_hosts),
        "signature_classes": len(signature_classes),
        "total_rank3_reduction_required": sum(
            record["rank3_reduction_required"] for record in exceptional_hosts
        ),
        "maximum_rank3_reduction_required": max(
            record["rank3_reduction_required"] for record in exceptional_hosts
        ),
        "reduction_distribution": [
            [reduction, count]
            for reduction, count in sorted(
                Counter(
                    record["rank3_reduction_required"]
                    for record in exceptional_hosts
                ).items()
            )
        ],
    }
    return payload


def validate_priority_manifest(manifest: Any) -> dict[str, Any]:
    require(isinstance(manifest, dict), "manifest: expected object")
    expected = build_priority_manifest()
    require(manifest.get("version") == 1, "version: expected 1")
    require(
        manifest.get("source_catalogue_sha256") == expected["source_catalogue_sha256"],
        "source_catalogue_sha256: incorrect",
    )
    require(manifest.get("priority_sha256") == expected["priority_sha256"],
            "priority_sha256: incorrect")
    require(manifest.get("exceptional_hosts") == expected["exceptional_hosts"],
            "exceptional_hosts: canonical priority list mismatch")
    require(manifest.get("signature_classes") == expected["signature_classes"],
            "signature_classes: canonical class list mismatch")
    require(manifest.get("claims") == expected["claims"], "claims: incorrect")

    claims = expected["claims"]
    require(expected["priority_sha256"] == EXPECTED_PRIORITY_SHA256,
            "built-in priority digest drift")
    require(claims["exceptional_hosts"] == 89, "expected 89 exceptional hosts")
    require((claims["critical_hosts"], claims["excess_hosts"]) == (44, 45),
            "critical/excess census mismatch")
    require((claims["side4_exceptional_hosts"], claims["side5_exceptional_hosts"]) == (33, 56),
            "side-specific exceptional census mismatch")
    require(claims["signature_classes"] == 49, "expected 49 exact signature classes")
    require(claims["total_rank3_reduction_required"] == 179,
            "total required rank-three reduction mismatch")
    require(claims["maximum_rank3_reduction_required"] == 5,
            "maximum required rank-three reduction mismatch")
    require(claims["reduction_distribution"] == [[1, 44], [2, 14], [3, 18], [4, 12], [5, 1]],
            "rank-three reduction distribution mismatch")
    return copy.deepcopy(claims)


def run_mutation_tests() -> int:
    manifest = build_priority_manifest()
    validate_priority_manifest(manifest)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(manifest)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data.update(priority_sha256="0" * 64))
    add(lambda data: data.update(source_catalogue_sha256="0" * 64))
    add(lambda data: data["claims"].update(exceptional_hosts=88))
    add(lambda data: data["exceptional_hosts"][0].update(host_id="s5-corrupt"))
    add(lambda data: data["exceptional_hosts"][0].update(rank3_slack=1))
    add(lambda data: data["exceptional_hosts"][0].update(rank3_reduction_required=0))
    add(lambda data: data["exceptional_hosts"][0]["deletion_edges"].pop())
    add(lambda data: data["exceptional_hosts"][0]["response_triple_histogram"].pop())
    add(lambda data: data["signature_classes"][0].update(host_count=999))
    add(lambda data: data["signature_classes"][0]["host_ids"].reverse())

    rejected = 0
    for candidate in mutations:
        try:
            validate_priority_manifest(candidate)
        except (PriorityError, catalogue.CatalogueError):
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted manifest accepted")
    return rejected


def main() -> None:
    if len(sys.argv) == 3 and sys.argv[1] == "--write":
        manifest = build_priority_manifest()
        validate_priority_manifest(manifest)
        Path(sys.argv[2]).write_text(
            json.dumps(manifest, sort_keys=True, indent=2) + "\n", encoding="utf-8"
        )
        print(
            f"wrote exceptional-host priority manifest: "
            f"{manifest['claims']['exceptional_hosts']} hosts, "
            f"{manifest['claims']['signature_classes']} classes, "
            f"sha256 {manifest['priority_sha256']}"
        )
        return
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            manifest = json.load(handle)
        claims = validate_priority_manifest(manifest)
        print(
            "accepted exceptional-host priority manifest: "
            f"{claims['exceptional_hosts']} hosts, "
            f"{claims['signature_classes']} signature classes, "
            f"{claims['total_rank3_reduction_required']} total required reduction units"
        )
        return
    if len(sys.argv) != 1:
        raise SystemExit(
            "usage: check_prime_power_exceptional_host_priority_manifest.py "
            "[manifest.json | --write manifest.json]"
        )

    manifest = build_priority_manifest()
    claims = validate_priority_manifest(manifest)
    rejected = run_mutation_tests()
    print(
        "verified exceptional-host priority manifest: "
        f"{claims['exceptional_hosts']} hosts in {claims['signature_classes']} classes, "
        f"reduction distribution {claims['reduction_distribution']}, "
        f"priority sha256 {manifest['priority_sha256']}, "
        f"and {rejected} corrupted manifests rejected"
    )


if __name__ == "__main__":
    main()
