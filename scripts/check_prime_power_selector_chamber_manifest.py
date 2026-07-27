#!/usr/bin/env python3
"""Build exact affine selector chambers over the reduced background signature.

Every canonical response score is a common rank-one baseline plus one affine integer
form in the reduced survivor-background signature.  A lexicographic selector chamber
is the finite family of strict/non-strict pairwise inequalities against the other
responses of its host.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from functools import lru_cache
from pathlib import Path
from random import Random
from typing import Any

import check_prime_power_background_signature as signature
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_response_line_incidence_kernel as kernel

EXPECTED_CHAMBER_SHA256 = "34ced8ddcb096a238e91d576754e8d77c924c667ae122e991c99c473fa882b27"


class ChamberError(ValueError):
    """Raised when an affine selector chamber manifest is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ChamberError(message)


def affine_row(side: int, geometry: dict[str, Any]) -> dict[str, Any]:
    basis = signature.basis_for_side(side)
    cross_index = {tuple(point): index for index, point in enumerate(basis["rank1_cross_coordinates"])}
    line_index = {tuple(line): index for index, line in enumerate(basis["response_lines"])}
    cross = sorted(
        cross_index[point]
        for point in map(tuple, geometry["response_points"])
        if point in cross_index
    )
    lines = sorted(
        [line_index[tuple(record["line"])], record["rank2_pair_multiplicity"]]
        for record in geometry["line_records"]
    )
    row: dict[str, Any] = {
        "side": side,
        "permutation": geometry["permutation"],
        "response_geometry_sha256": geometry["response_geometry_sha256"],
        "rank1_cross_unit_indices": cross,
        "rank2_line_coefficients": lines,
        "rank3_constant": geometry["rank3_triples"],
    }
    row["row_sha256"] = catalogue.canonical_digest(row)
    return row


def evaluate_row(row: dict[str, Any], survivor_signature: dict[str, Any]) -> int:
    return (
        sum(survivor_signature["rank1_cross_differences"][index]
            for index in row["rank1_cross_unit_indices"])
        + sum(value * survivor_signature["response_line_background_counts"][index]
              for index, value in row["rank2_line_coefficients"])
        + row["rank3_constant"]
    )


@lru_cache(maxsize=1)
def _build_manifest_cached() -> dict[str, Any]:
    source = catalogue.build_catalogue()
    catalogue.validate_catalogue(source)
    line_source = kernel.build_kernel()
    kernel.validate_kernel(line_source)
    basis = signature.build_basis()
    signature.validate_basis(basis)

    row_by_key: dict[tuple[int, tuple[int, ...]], dict[str, Any]] = {}
    kernel_by_host = {host["host_id"]: host for host in line_source["hosts"]}
    host_records = []
    comparison_counts = Counter()
    ordered_pairs: dict[int, set[tuple[str, str]]] = {4: set(), 5: set()}

    for host in source["hosts"]:
        host_kernel = kernel_by_host[host["host_id"]]
        row_ids = []
        for response, geometry in zip(host["responses"], host_kernel["responses"]):
            require(response["permutation"] == geometry["permutation"], "catalogue/kernel response mismatch")
            key = (host["side"], tuple(response["permutation"]))
            row = affine_row(host["side"], geometry)
            if key in row_by_key:
                require(row_by_key[key] == row, "response permutation has inconsistent affine row")
            else:
                row_by_key[key] = row
            row_ids.append(row["row_sha256"])
        for left in row_ids:
            for right in row_ids:
                if left != right:
                    ordered_pairs[host["side"]].add((left, right))
                    comparison_counts[host["side"]] += 1
        host_record: dict[str, Any] = {
            "host_id": host["host_id"],
            "catalogue_record_sha256": host["record_sha256"],
            "side": host["side"],
            "response_row_sha256s": row_ids,
        }
        host_record["host_chamber_sha256"] = catalogue.canonical_digest(host_record)
        host_records.append(host_record)

    rows = [row_by_key[key] for key in sorted(row_by_key)]
    pair_records = [
        {"side": side, "left_row_sha256": left, "right_row_sha256": right}
        for side in (4, 5)
        for left, right in sorted(ordered_pairs[side])
    ]
    payload: dict[str, Any] = {
        "version": 1,
        "source_catalogue_sha256": source["catalogue_sha256"],
        "source_kernel_sha256": line_source["kernel_sha256"],
        "source_signature_basis_sha256": basis["basis_sha256"],
        "affine_rows": rows,
        "host_chambers": host_records,
        "ordered_row_pairs": pair_records,
    }
    payload["chamber_sha256"] = catalogue.canonical_digest(payload)
    payload["claims"] = {
        "hosts": len(host_records),
        "response_occurrences": sum(len(host["response_row_sha256s"]) for host in host_records),
        "affine_rows": len(rows),
        "side4_affine_rows": sum(row["side"] == 4 for row in rows),
        "side5_affine_rows": sum(row["side"] == 5 for row in rows),
        "host_ordered_comparisons": sum(comparison_counts.values()),
        "side4_host_ordered_comparisons": comparison_counts[4],
        "side5_host_ordered_comparisons": comparison_counts[5],
        "unique_ordered_row_pairs": len(pair_records),
        "side4_unique_ordered_row_pairs": len(ordered_pairs[4]),
        "side5_unique_ordered_row_pairs": len(ordered_pairs[5]),
    }
    return payload


def build_manifest() -> dict[str, Any]:
    return copy.deepcopy(_build_manifest_cached())


def validate_manifest(manifest: Any) -> dict[str, int]:
    require(isinstance(manifest, dict), "manifest: expected object")
    expected = _build_manifest_cached()
    for key in (
        "version", "source_catalogue_sha256", "source_kernel_sha256",
        "source_signature_basis_sha256", "affine_rows", "host_chambers",
        "ordered_row_pairs", "chamber_sha256", "claims",
    ):
        require(manifest.get(key) == expected[key], f"{key}: canonical mismatch")
    claims = expected["claims"]
    require(claims == {
        "hosts": 740,
        "response_occurrences": 9260,
        "affine_rows": 39,
        "side4_affine_rows": 6,
        "side5_affine_rows": 33,
        "host_ordered_comparisons": 125448,
        "side4_host_ordered_comparisons": 378,
        "side5_host_ordered_comparisons": 125070,
        "unique_ordered_row_pairs": 1086,
        "side4_unique_ordered_row_pairs": 30,
        "side5_unique_ordered_row_pairs": 1056,
    }, "selector chamber census mismatch")
    if EXPECTED_CHAMBER_SHA256 != "TO_BE_FILLED":
        require(expected["chamber_sha256"] == EXPECTED_CHAMBER_SHA256, "built-in chamber digest drift")
    return copy.deepcopy(claims)


@lru_cache(maxsize=1)
def chamber_maps() -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    manifest = _build_manifest_cached()
    rows = {row["row_sha256"]: row for row in manifest["affine_rows"]}
    hosts = {host["host_id"]: host for host in manifest["host_chambers"]}
    return rows, hosts


def selected_row(host_id: str, survivor_signature: dict[str, Any]) -> tuple[dict[str, Any], list[int]]:
    rows, hosts = chamber_maps()
    host = hosts[host_id]
    host_rows = [rows[row_id] for row_id in host["response_row_sha256s"]]
    values = [evaluate_row(row, survivor_signature) for row in host_rows]
    minimum = min(values)
    index = values.index(minimum)
    return host_rows[index], values


def chamber_inequalities(host_id: str, selected_sha256: str, survivor_signature: dict[str, Any]) -> list[dict[str, Any]]:
    rows, hosts = chamber_maps()
    host = hosts[host_id]
    require(selected_sha256 in host["response_row_sha256s"], "selected row not in host")
    selected_index = host["response_row_sha256s"].index(selected_sha256)
    selected_value = evaluate_row(rows[selected_sha256], survivor_signature)
    output = []
    for index, row_id in enumerate(host["response_row_sha256s"]):
        if row_id == selected_sha256:
            continue
        other_value = evaluate_row(rows[row_id], survivor_signature)
        strict = index < selected_index
        satisfied = selected_value < other_value if strict else selected_value <= other_value
        output.append({
            "other_row_sha256": row_id,
            "strict": strict,
            "selected_value": selected_value,
            "other_value": other_value,
            "satisfied": satisfied,
        })
    return output


def run_random_tests() -> tuple[int, Counter[str]]:
    random = Random(2054)
    source = catalogue.build_catalogue()
    totals: Counter[str] = Counter()
    for _ in range(500):
        host = random.choice(source["hosts"])
        background = signature.random_background(host["side"], random)
        certificate = signature.build_certificate(host, background)
        signature.validate_certificate(certificate)
        selected, values = selected_row(host["host_id"], certificate["signature"])
        require(selected["permutation"] == certificate["claims"]["selected_response"],
                "affine chamber selector disagrees with exact signature selector")
        inequalities = chamber_inequalities(host["host_id"], selected["row_sha256"], certificate["signature"])
        require(all(record["satisfied"] for record in inequalities), "selected chamber inequality failed")
        totals["responses"] += len(values)
        totals["inequalities"] += len(inequalities)
        totals["background_points"] += len(background)
        totals["side4"] += int(host["side"] == 4)
        totals["side5"] += int(host["side"] == 5)
    return 500, totals


def run_mutation_tests() -> int:
    manifest = build_manifest()
    validate_manifest(manifest)
    mutations: list[dict[str, Any]] = []
    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(manifest)
        mutator(candidate)
        mutations.append(candidate)
    add(lambda data: data.update(chamber_sha256="0" * 64))
    add(lambda data: data.update(source_signature_basis_sha256="0" * 64))
    add(lambda data: data["claims"].update(affine_rows=38))
    add(lambda data: data["affine_rows"][0].update(row_sha256="0" * 64))
    add(lambda data: data["affine_rows"][0]["permutation"].reverse())
    add(lambda data: data["affine_rows"][0]["rank1_cross_unit_indices"].append(999))
    add(lambda data: data["affine_rows"][0]["rank2_line_coefficients"].pop())
    add(lambda data: data["affine_rows"][0].update(rank3_constant=999))
    add(lambda data: data["host_chambers"][0]["response_row_sha256s"].pop())
    add(lambda data: data["ordered_row_pairs"].pop())
    add(lambda data: data["host_chambers"].reverse())
    add(lambda data: data.update(version=2))
    rejected = 0
    for candidate in mutations:
        try:
            validate_manifest(candidate)
        except (ChamberError, signature.SignatureError, catalogue.CatalogueError, kernel.KernelError):
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted chamber manifest accepted")
    return rejected


def main() -> None:
    if len(sys.argv) == 3 and sys.argv[1] == "--write":
        manifest = build_manifest()
        validate_manifest(manifest)
        Path(sys.argv[2]).write_text(json.dumps(manifest, sort_keys=True, indent=2) + "\n", encoding="utf-8")
        print(f"wrote selector chamber manifest: sha256 {manifest['chamber_sha256']}")
        return
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            manifest = json.load(handle)
        claims = validate_manifest(manifest)
        print(f"accepted selector chamber manifest: {claims['affine_rows']} affine rows")
        return
    if len(sys.argv) != 1:
        raise SystemExit("usage: check_prime_power_selector_chamber_manifest.py [manifest.json | --write manifest.json]")
    manifest = build_manifest()
    claims = validate_manifest(manifest)
    systems, totals = run_random_tests()
    rejected = run_mutation_tests()
    print(
        "verified affine selector chambers: "
        f"{claims['affine_rows']} affine rows, {claims['unique_ordered_row_pairs']} unique ordered pairs, "
        f"{claims['host_ordered_comparisons']} host comparisons, {systems} systems, "
        f"{totals['responses']} response evaluations, {totals['inequalities']} chamber inequalities, "
        f"sha256 {manifest['chamber_sha256']}, and {rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
