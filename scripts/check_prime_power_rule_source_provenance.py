#!/usr/bin/env python3
"""Validate complete source provenance for a declarative parent-rule clause manifest.

This checker does not decide whether a cited source statement is mathematically true. It
binds every parent case, clause, finite parameter axis and excluded row to explicit source
records, checks exact bidirectional coverage, rejects dangling or unused citations, and
protects the complete provenance graph by canonical digests.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_parent_rule_clause_enumerator as clauses

SOURCE_KINDS = {"definition", "case-split", "lemma", "domain", "exclusion", "computation"}


class RuleProvenanceError(ValueError):
    """Raised when rule-clause provenance is incomplete or inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuleProvenanceError(message)


def exact_source(record: dict[str, Any]) -> dict[str, Any]:
    source_id = record.get("source_id")
    kind = record.get("kind")
    locator = record.get("locator")
    statement_sha256 = record.get("statement_sha256")
    note = record.get("note")
    require(isinstance(source_id, str) and source_id, "source_id: nonempty string required")
    require(kind in SOURCE_KINDS, f"source {source_id}: unsupported kind")
    require(isinstance(locator, str) and locator, f"source {source_id}: locator required")
    require(
        isinstance(statement_sha256, str)
        and len(statement_sha256) == 64
        and all(character in "0123456789abcdef" for character in statement_sha256),
        f"source {source_id}: lowercase statement SHA-256 required",
    )
    require(isinstance(note, str), f"source {source_id}: note must be a string")
    output = {
        "source_id": source_id,
        "kind": kind,
        "locator": locator,
        "statement_sha256": statement_sha256,
        "note": note,
    }
    output["source_record_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_link(record: dict[str, Any], identity_keys: tuple[str, ...], path: str) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key in identity_keys:
        value = record.get(key)
        require(isinstance(value, str) and value, f"{path}.{key}: nonempty string required")
        output[key] = value
    source_ids = record.get("source_ids")
    require(isinstance(source_ids, list) and source_ids, f"{path}.source_ids: nonempty list required")
    require(all(isinstance(value, str) and value for value in source_ids), f"{path}.source_ids: bad value")
    require(source_ids == sorted(source_ids), f"{path}.source_ids: sorted order required")
    require(len(source_ids) == len(set(source_ids)), f"{path}.source_ids: duplicates")
    output["source_ids"] = list(source_ids)
    output["link_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    manifest = certificate.get("clause_manifest")
    raw_sources = certificate.get("sources")
    raw_case_links = certificate.get("case_links")
    raw_clause_links = certificate.get("clause_links")
    raw_axis_links = certificate.get("axis_links")
    raw_exclusion_links = certificate.get("exclusion_links")
    require(isinstance(manifest, dict), "clause_manifest: expected object")
    require(isinstance(raw_sources, list) and raw_sources, "sources: nonempty list required")
    require(isinstance(raw_case_links, list), "case_links: expected list")
    require(isinstance(raw_clause_links, list), "clause_links: expected list")
    require(isinstance(raw_axis_links, list), "axis_links: expected list")
    require(isinstance(raw_exclusion_links, list), "exclusion_links: expected list")

    clauses.validate_manifest(manifest)
    exact_manifest = clauses.exact_enumerator(manifest)
    sources = [exact_source(record) for record in raw_sources]
    require(raw_sources == sources, "sources: canonical records or digests required")
    require(sources == sorted(sources, key=lambda record: record["source_id"]), "sources: canonical order required")
    source_ids = [record["source_id"] for record in sources]
    require(len(source_ids) == len(set(source_ids)), "sources: duplicate source_id")
    source_map = {record["source_id"]: record for record in sources}

    case_links = [exact_link(record, ("case_id",), f"case_links[{index}]") for index, record in enumerate(raw_case_links)]
    clause_links = [exact_link(record, ("clause_id",), f"clause_links[{index}]") for index, record in enumerate(raw_clause_links)]
    axis_links = [exact_link(record, ("clause_id", "axis_name"), f"axis_links[{index}]") for index, record in enumerate(raw_axis_links)]
    exclusion_links = [exact_link(record, ("clause_id", "row_sha256"), f"exclusion_links[{index}]") for index, record in enumerate(raw_exclusion_links)]
    for name, raw, exact, key in (
        ("case_links", raw_case_links, case_links, lambda record: record["case_id"]),
        ("clause_links", raw_clause_links, clause_links, lambda record: record["clause_id"]),
        ("axis_links", raw_axis_links, axis_links, lambda record: (record["clause_id"], record["axis_name"])),
        ("exclusion_links", raw_exclusion_links, exclusion_links, lambda record: (record["clause_id"], record["row_sha256"])),
    ):
        require(raw == exact, f"{name}: canonical records or digests required")
        require(exact == sorted(exact, key=key), f"{name}: canonical order required")
        keys = [key(record) for record in exact]
        require(len(keys) == len(set(keys)), f"{name}: duplicate identity")

    expected_cases = {record["case_id"] for record in exact_manifest["parent_cases"]}
    expected_clauses = {record["clause_id"] for record in exact_manifest["clauses"]}
    expected_axes = {
        (clause["clause_id"], axis["name"])
        for clause in exact_manifest["clauses"]
        for axis in clause["parameter_axes"]
    }
    expected_exclusions = {
        (clause["clause_id"], catalogue.canonical_digest(record["row"]))
        for clause in exact_manifest["clauses"]
        for record in clause["excluded_parameter_rows"]
    }
    require({record["case_id"] for record in case_links} == expected_cases, "case_links: incomplete or extraneous coverage")
    require({record["clause_id"] for record in clause_links} == expected_clauses, "clause_links: incomplete or extraneous coverage")
    require({(record["clause_id"], record["axis_name"]) for record in axis_links} == expected_axes,
            "axis_links: incomplete or extraneous coverage")
    require({(record["clause_id"], record["row_sha256"]) for record in exclusion_links} == expected_exclusions,
            "exclusion_links: incomplete or extraneous coverage")

    usage: Counter[str] = Counter()
    required_kinds = {
        "case": {"definition", "case-split", "lemma"},
        "clause": {"definition", "lemma"},
        "axis": {"definition", "domain", "lemma", "computation"},
        "exclusion": {"exclusion", "lemma", "computation"},
    }
    for kind, records in (("case", case_links), ("clause", clause_links), ("axis", axis_links), ("exclusion", exclusion_links)):
        for record in records:
            require(set(record["source_ids"]) <= set(source_map), f"{kind} link: unknown source")
            require(any(source_map[source_id]["kind"] in required_kinds[kind] for source_id in record["source_ids"]),
                    f"{kind} link: no source of an admissible kind")
            usage.update(record["source_ids"])
    require(set(usage) == set(source_map), "sources: every source must be used and every use must resolve")

    kind_counts = Counter(record["kind"] for record in sources)
    claims = {
        "sources": len(sources),
        "parent_cases": len(case_links),
        "clauses": len(clause_links),
        "parameter_axes": len(axis_links),
        "excluded_rows": len(exclusion_links),
        "source_uses": sum(usage.values()),
        "source_kind_distribution": [[key, kind_counts[key]] for key in sorted(kind_counts)],
        "rule_source_sha256": catalogue.canonical_digest(manifest["rule_source"]),
        "clause_manifest_sha256": manifest["manifest_sha256"],
        "sources_sha256": catalogue.canonical_digest(sources),
        "case_links_sha256": catalogue.canonical_digest(case_links),
        "clause_links_sha256": catalogue.canonical_digest(clause_links),
        "axis_links_sha256": catalogue.canonical_digest(axis_links),
        "exclusion_links_sha256": catalogue.canonical_digest(exclusion_links),
    }
    return {
        "sources": sources,
        "case_links": case_links,
        "clause_links": clause_links,
        "axis_links": axis_links,
        "exclusion_links": exclusion_links,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    for key in ("sources", "case_links", "clause_links", "axis_links", "exclusion_links", "claims"):
        require(certificate.get(key) == exact[key], f"{key}: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload), "certificate_sha256: incorrect")
    claims = exact["claims"]
    return {
        "sources": claims["sources"],
        "cases": claims["parent_cases"],
        "clauses": claims["clauses"],
        "axes": claims["parameter_axes"],
        "exclusions": claims["excluded_rows"],
        "uses": claims["source_uses"],
    }


def build_certificate(manifest: dict[str, Any], sources: list[dict[str, Any]], case_links: list[dict[str, Any]],
                      clause_links: list[dict[str, Any]], axis_links: list[dict[str, Any]],
                      exclusion_links: list[dict[str, Any]]) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "clause_manifest": manifest,
        "sources": sorted((exact_source(record) for record in sources), key=lambda record: record["source_id"]),
        "case_links": sorted((exact_link(record, ("case_id",), "case_link") for record in case_links),
                             key=lambda record: record["case_id"]),
        "clause_links": sorted((exact_link(record, ("clause_id",), "clause_link") for record in clause_links),
                               key=lambda record: record["clause_id"]),
        "axis_links": sorted((exact_link(record, ("clause_id", "axis_name"), "axis_link") for record in axis_links),
                           key=lambda record: (record["clause_id"], record["axis_name"])),
        "exclusion_links": sorted((exact_link(record, ("clause_id", "row_sha256"), "exclusion_link") for record in exclusion_links),
                                key=lambda record: (record["clause_id"], record["row_sha256"])),
    }
    certificate.update(exact_certificate(certificate))
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_prime_power_rule_source_provenance.py certificate.json")
    certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(validate_certificate(certificate))


if __name__ == "__main__":
    main()
