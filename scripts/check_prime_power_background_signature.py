#!/usr/bin/env python3
"""Validate exact finite survivor-background signatures for canonical response hosts.

For side four or five, the selector-relevant background data consist of:

* rank-one pair counts at response-grid points, reduced modulo row/column potentials;
* background occupancies on the finite union of canonical response lines.

The checker proves that these data reconstruct every response's exact new-triple score.
With one JSON path, validate a certificate. With no argument, run deterministic tests.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from functools import lru_cache
from itertools import combinations
from pathlib import Path
from random import Random
from typing import Any

import check_prime_power_background_response_selector as selector
import check_prime_power_canonical_raw_host_catalogue as catalogue
import check_prime_power_response_line_incidence_kernel as kernel

Point = tuple[int, int]
EXPECTED_BASIS_SHA256 = "385ebe3b5f44ae14b6e954623af154a0152cd33562c0bb0e0f2875f6041444fd"


class SignatureError(ValueError):
    """Raised when a survivor-background signature is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SignatureError(message)


def parse_integer(value: Any, path: str) -> int:
    require(type(value) is int, f"{path}: expected integer")
    return value


def parse_point(value: Any, path: str) -> Point:
    require(isinstance(value, list) and len(value) == 2, f"{path}: expected [x,y]")
    return parse_integer(value[0], f"{path}[0]"), parse_integer(value[1], f"{path}[1]")


@lru_cache(maxsize=1)
def _basis_cached() -> dict[str, Any]:
    source = catalogue.build_catalogue()
    catalogue.validate_catalogue(source)
    line_source = kernel.build_kernel()
    kernel.validate_kernel(line_source)
    sides = []
    for side in (4, 5):
        lines = sorted({
            tuple(line_record["line"])
            for host in line_source["hosts"] if host["side"] == side
            for response in host["responses"]
            for line_record in response["line_records"]
        })
        grid = [(left, right) for left in range(side) for right in range(side)]
        cross = [(left, right) for left in range(1, side) for right in range(1, side)]
        sides.append({
            "side": side,
            "grid_points": [list(point) for point in grid],
            "rank1_cross_coordinates": [list(point) for point in cross],
            "response_lines": [list(line) for line in lines],
            "full_signature_dimension": len(grid) + len(lines),
            "selector_signature_dimension": len(cross) + len(lines),
        })
    payload: dict[str, Any] = {
        "version": 1,
        "source_catalogue_sha256": source["catalogue_sha256"],
        "source_kernel_sha256": line_source["kernel_sha256"],
        "sides": sides,
    }
    payload["basis_sha256"] = catalogue.canonical_digest(payload)
    payload["claims"] = {
        "side4_lines": len(sides[0]["response_lines"]),
        "side5_lines": len(sides[1]["response_lines"]),
        "side4_full_dimension": sides[0]["full_signature_dimension"],
        "side5_full_dimension": sides[1]["full_signature_dimension"],
        "side4_selector_dimension": sides[0]["selector_signature_dimension"],
        "side5_selector_dimension": sides[1]["selector_signature_dimension"],
        "rank1_gauge_reduction": (
            sides[0]["full_signature_dimension"] - sides[0]["selector_signature_dimension"]
            + sides[1]["full_signature_dimension"] - sides[1]["selector_signature_dimension"]
        ),
    }
    return payload


def build_basis() -> dict[str, Any]:
    return copy.deepcopy(_basis_cached())


def validate_basis(basis: Any) -> dict[str, int]:
    require(isinstance(basis, dict), "basis: expected object")
    expected = _basis_cached()
    for key in ("version", "source_catalogue_sha256", "source_kernel_sha256", "sides", "basis_sha256", "claims"):
        require(basis.get(key) == expected[key], f"basis.{key}: canonical mismatch")
    claims = expected["claims"]
    require(claims == {
        "side4_lines": 23,
        "side5_lines": 83,
        "side4_full_dimension": 39,
        "side5_full_dimension": 108,
        "side4_selector_dimension": 32,
        "side5_selector_dimension": 99,
        "rank1_gauge_reduction": 16,
    }, "background basis census mismatch")
    if EXPECTED_BASIS_SHA256 != "TO_BE_FILLED":
        require(expected["basis_sha256"] == EXPECTED_BASIS_SHA256, "built-in basis digest drift")
    return copy.deepcopy(claims)


def basis_for_side(side: int) -> dict[str, Any]:
    return next(record for record in _basis_cached()["sides"] if record["side"] == side)


def point_pair_count(point: Point, background: list[Point]) -> int:
    return sum(catalogue.collinear(point, first, second) for first, second in combinations(background, 2))


def exact_signature(side: int, background: list[Point]) -> dict[str, Any]:
    basis = basis_for_side(side)
    grid = [tuple(point) for point in basis["grid_points"]]
    lines = [tuple(line) for line in basis["response_lines"]]
    point_counts = {point: point_pair_count(point, background) for point in grid}
    baseline = (
        sum(point_counts[(left, 0)] for left in range(side))
        + sum(point_counts[(0, right)] - point_counts[(0, 0)] for right in range(side))
    )
    cross = [
        point_counts[(left, right)]
        - point_counts[(left, 0)]
        - point_counts[(0, right)]
        + point_counts[(0, 0)]
        for left in range(1, side)
        for right in range(1, side)
    ]
    line_counts = [
        sum(a * x + b * y + c == 0 for x, y in background)
        for a, b, c in lines
    ]
    signature: dict[str, Any] = {
        "side": side,
        "background_points": len(background),
        "rank1_point_pair_counts": [point_counts[point] for point in grid],
        "rank1_common_baseline": baseline,
        "rank1_cross_differences": cross,
        "response_line_background_counts": line_counts,
    }
    signature["signature_sha256"] = catalogue.canonical_digest(signature)
    return signature


def score_from_signature(
    geometry: dict[str, Any], signature: dict[str, Any]
) -> tuple[int, int, int, int]:
    side = signature["side"]
    basis = basis_for_side(side)
    cross_index = {
        tuple(point): index for index, point in enumerate(basis["rank1_cross_coordinates"])
    }
    line_index = {
        tuple(line): index for index, line in enumerate(basis["response_lines"])
    }
    rank1 = signature["rank1_common_baseline"]
    for point in map(tuple, geometry["response_points"]):
        if point in cross_index:
            rank1 += signature["rank1_cross_differences"][cross_index[point]]
    rank2 = sum(
        record["rank2_pair_multiplicity"]
        * signature["response_line_background_counts"][line_index[tuple(record["line"])]]
        for record in geometry["line_records"]
    )
    rank3 = geometry["rank3_triples"]
    return rank1, rank2, rank3, rank1 + rank2 + rank3


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    hosts, kernels = selector.host_maps()
    host_id = certificate.get("host_id")
    require(isinstance(host_id, str) and host_id in hosts, "host_id: unknown")
    host = hosts[host_id]
    require(certificate.get("catalogue_record_sha256") == host["record_sha256"],
            "catalogue_record_sha256: incorrect")
    raw_background = certificate.get("background_points")
    require(isinstance(raw_background, list), "background_points: expected list")
    background = [parse_point(value, f"background_points[{index}]") for index, value in enumerate(raw_background)]
    require(len(set(background)) == len(background), "background_points: duplicates")
    grid = {(left, right) for left in range(host["side"]) for right in range(host["side"])}
    require(not (set(background) & grid), "background_points: intersects response grid")

    signature = exact_signature(host["side"], background)
    if "signature" in certificate:
        require(certificate.get("signature") == signature, "signature: incorrect")
    response_scores = []
    for source_response, geometry in zip(host["responses"], kernels[host_id]["responses"]):
        require(source_response["permutation"] == geometry["permutation"], "response order mismatch")
        rank1, rank2, rank3, total = score_from_signature(geometry, signature)
        direct = selector.direct_rank_counts(source_response["permutation"], background)
        require((rank1, rank2, rank3) == direct, "signature/direct rank mismatch")
        response_scores.append({
            "permutation": source_response["permutation"],
            "rank_counts": [rank1, rank2, rank3],
            "new_triples": total,
        })
    minimum = min(record["new_triples"] for record in response_scores)
    minimizers = [record for record in response_scores if record["new_triples"] == minimum]
    selected = min(minimizers, key=lambda record: record["permutation"])
    exact = {
        "responses": len(response_scores),
        "background_points": len(background),
        "full_signature_dimension": basis_for_side(host["side"])["full_signature_dimension"],
        "selector_signature_dimension": basis_for_side(host["side"])["selector_signature_dimension"],
        "minimum_new_triples": minimum,
        "minimizer_count": len(minimizers),
        "selected_response": selected["permutation"],
        "response_scores_sha256": catalogue.canonical_digest(response_scores),
    }
    return {"signature": signature, "response_scores": response_scores, "claims": exact}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    require(certificate.get("basis_sha256") == _basis_cached()["basis_sha256"], "basis_sha256: incorrect")
    exact = exact_certificate(certificate)
    require(certificate.get("signature") == exact["signature"], "signature: mismatch")
    require(certificate.get("claims") == exact["claims"], "claims: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
            "certificate_sha256: incorrect")
    return {
        "responses": exact["claims"]["responses"],
        "background_points": exact["claims"]["background_points"],
        "minimum_new_triples": exact["claims"]["minimum_new_triples"],
        "selector_dimension": exact["claims"]["selector_signature_dimension"],
    }


def build_certificate(host: dict[str, Any], background: list[Point]) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "basis_sha256": _basis_cached()["basis_sha256"],
        "host_id": host["host_id"],
        "catalogue_record_sha256": host["record_sha256"],
        "background_points": [list(point) for point in background],
    }
    exact = exact_certificate(certificate)
    certificate["signature"] = exact["signature"]
    certificate["claims"] = exact["claims"]
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def random_background(side: int, random: Random) -> list[Point]:
    grid = {(left, right) for left in range(side) for right in range(side)}
    output: list[Point] = []
    target = random.randrange(0, 8)
    while len(output) < target:
        point = (random.randrange(-7, side + 8), random.randrange(-7, side + 8))
        if point not in grid and point not in output:
            output.append(point)
    return output


def run_random_tests() -> tuple[int, Counter[str], Counter[int]]:
    random = Random(2046)
    source = catalogue.build_catalogue()
    totals: Counter[str] = Counter()
    minimums: Counter[int] = Counter()
    for _ in range(500):
        host = random.choice(source["hosts"])
        certificate = build_certificate(host, random_background(host["side"], random))
        summary = validate_certificate(certificate)
        totals.update(summary)
        minimums[summary["minimum_new_triples"]] += 1
    return 500, totals, minimums


def run_mutation_tests() -> int:
    random = Random(89)
    host = catalogue.build_catalogue()["hosts"][400]
    certificate = build_certificate(host, random_background(host["side"], random))
    validate_certificate(certificate)
    mutations: list[dict[str, Any]] = []
    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(certificate)
        mutator(candidate)
        mutations.append(candidate)
    add(lambda data: data.update(certificate_sha256="0" * 64))
    add(lambda data: data.update(basis_sha256="0" * 64))
    add(lambda data: data.update(host_id="s5-corrupt"))
    add(lambda data: data.update(catalogue_record_sha256="0" * 40))
    add(lambda data: data["background_points"].append(data["background_points"][0]))
    add(lambda data: data["signature"]["rank1_point_pair_counts"].pop())
    add(lambda data: data["signature"]["rank1_cross_differences"].append(999))
    add(lambda data: data["signature"]["response_line_background_counts"].pop())
    add(lambda data: data["signature"].update(rank1_common_baseline=999))
    add(lambda data: data["claims"].update(responses=999))
    add(lambda data: data["claims"]["selected_response"].reverse())
    add(lambda data: data.update(version=2))
    rejected = 0
    for candidate in mutations:
        try:
            validate_certificate(candidate)
        except (SignatureError, selector.BackgroundSelectorError, catalogue.CatalogueError, kernel.KernelError):
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted certificate accepted")
    return rejected


def main() -> None:
    if len(sys.argv) == 3 and sys.argv[1] == "--write-basis":
        basis = build_basis()
        validate_basis(basis)
        Path(sys.argv[2]).write_text(json.dumps(basis, sort_keys=True, indent=2) + "\n", encoding="utf-8")
        print(f"wrote background signature basis: sha256 {basis['basis_sha256']}")
        return
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            certificate = json.load(handle)
        summary = validate_certificate(certificate)
        print(f"accepted background signature: {summary['responses']} responses")
        return
    if len(sys.argv) != 1:
        raise SystemExit("usage: check_prime_power_background_signature.py [certificate.json | --write-basis basis.json]")
    basis = build_basis()
    claims = validate_basis(basis)
    systems, totals, minimums = run_random_tests()
    rejected = run_mutation_tests()
    print(
        "verified finite background signatures: "
        f"side line counts {claims['side4_lines']}/{claims['side5_lines']}, "
        f"selector dimensions {claims['side4_selector_dimension']}/{claims['side5_selector_dimension']}, "
        f"{systems} systems, {totals['responses']} response scores, "
        f"{totals['background_points']} background points, minimum distribution "
        f"{sorted(minimums.items())}, basis sha256 {basis['basis_sha256']}, "
        f"and {rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
