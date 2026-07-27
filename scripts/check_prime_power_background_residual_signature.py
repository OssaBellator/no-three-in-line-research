#!/usr/bin/env python3
"""Validate residual survivor-background signatures and unified line-cluster scores.

The existing finite background signature records, for every response-grid point q,
the number p_B(q) of background pairs collinear with q and, for every canonical
response line L, its background occupancy h_B(L).  This checker partitions p_B(q)
into pairs lying on tracked response lines through q and a nonnegative residual.
It then verifies the exact identity

    N_B(Q) = sum_{q in Q} u_B(q)
             + sum_{L in L_s} [C(h_B(L)+r_Q(L),3)-C(h_B(L),3)].

With one JSON path, validate a certificate. With no argument, run deterministic tests.
"""
from __future__ import annotations

import copy
import json
import math
import sys
from collections import Counter
from pathlib import Path
from random import Random
from typing import Any

import check_prime_power_background_signature as signature
import check_prime_power_background_response_selector as selector
import check_prime_power_canonical_raw_host_catalogue as catalogue

Point = tuple[int, int]
Line = tuple[int, int, int]


class ResidualSignatureError(ValueError):
    """Raised when a residual background signature is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ResidualSignatureError(message)


def point_on_line(point: Point, line: Line) -> bool:
    x, y = point
    a, b, c = line
    return a * x + b * y + c == 0


def residual_signature(side: int, background: list[Point]) -> dict[str, Any]:
    basis = signature.basis_for_side(side)
    absolute = signature.exact_signature(side, background)
    grid = [tuple(point) for point in basis["grid_points"]]
    lines = [tuple(line) for line in basis["response_lines"]]
    point_counts = absolute["rank1_point_pair_counts"]
    line_counts = absolute["response_line_background_counts"]

    tracked: list[int] = []
    residual: list[int] = []
    for point, observed in zip(grid, point_counts):
        contribution = sum(
            math.comb(count, 2)
            for line, count in zip(lines, line_counts)
            if point_on_line(point, line)
        )
        require(contribution <= observed, "tracked response-line pair contribution exceeds p_B(q)")
        tracked.append(contribution)
        residual.append(observed - contribution)

    residual_by_point = dict(zip(grid, residual))
    baseline = (
        sum(residual_by_point[(left, 0)] for left in range(side))
        + sum(
            residual_by_point[(0, right)] - residual_by_point[(0, 0)]
            for right in range(side)
        )
    )
    cross = [
        residual_by_point[(left, right)]
        - residual_by_point[(left, 0)]
        - residual_by_point[(0, right)]
        + residual_by_point[(0, 0)]
        for left in range(1, side)
        for right in range(1, side)
    ]
    output: dict[str, Any] = {
        "side": side,
        "background_points": len(background),
        "source_signature_sha256": absolute["signature_sha256"],
        "tracked_response_line_pair_counts": tracked,
        "rank1_residual_pair_counts": residual,
        "residual_common_baseline": baseline,
        "residual_cross_differences": cross,
        "response_line_background_counts": line_counts,
    }
    output["residual_signature_sha256"] = catalogue.canonical_digest(output)
    return output


def score_from_residual(
    permutation: list[int], residual: dict[str, Any]
) -> tuple[int, int, int]:
    side = residual["side"]
    basis = signature.basis_for_side(side)
    grid = [tuple(point) for point in basis["grid_points"]]
    lines = [tuple(line) for line in basis["response_lines"]]
    residual_by_point = dict(zip(grid, residual["rank1_residual_pair_counts"]))
    response_points = [(left, permutation[left]) for left in range(side)]
    residual_rank1 = sum(residual_by_point[point] for point in response_points)
    line_cluster = 0
    for line, h in zip(lines, residual["response_line_background_counts"]):
        r = sum(point_on_line(point, line) for point in response_points)
        if r:
            line_cluster += math.comb(h + r, 3) - math.comb(h, 3)
    return residual_rank1, line_cluster, residual_rank1 + line_cluster


def score_from_reduced_residual(
    permutation: list[int], residual: dict[str, Any]
) -> int:
    side = residual["side"]
    basis = signature.basis_for_side(side)
    cross_index = {
        tuple(point): index
        for index, point in enumerate(basis["rank1_cross_coordinates"])
    }
    reduced_rank1 = residual["residual_common_baseline"]
    for left, right in enumerate(permutation):
        if (left, right) in cross_index:
            reduced_rank1 += residual["residual_cross_differences"][cross_index[(left, right)]]

    lines = [tuple(line) for line in basis["response_lines"]]
    response_points = [(left, permutation[left]) for left in range(side)]
    line_cluster = sum(
        math.comb(h + sum(point_on_line(point, line) for point in response_points), 3)
        - math.comb(h, 3)
        for line, h in zip(lines, residual["response_line_background_counts"])
    )
    return reduced_rank1 + line_cluster


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    hosts, _kernels = selector.host_maps()
    host_id = certificate.get("host_id")
    require(isinstance(host_id, str) and host_id in hosts, "host_id: unknown")
    host = hosts[host_id]
    require(
        certificate.get("catalogue_record_sha256") == host["record_sha256"],
        "catalogue_record_sha256: incorrect",
    )
    raw_background = certificate.get("background_points")
    require(isinstance(raw_background, list), "background_points: expected list")
    background = [
        signature.parse_point(value, f"background_points[{index}]")
        for index, value in enumerate(raw_background)
    ]
    require(len(background) == len(set(background)), "background_points: duplicates")
    grid = {(left, right) for left in range(host["side"]) for right in range(host["side"])}
    require(not (set(background) & grid), "background_points: intersects response grid")

    absolute_certificate = signature.build_certificate(host, background)
    signature.validate_certificate(absolute_certificate)
    residual = residual_signature(host["side"], background)
    response_scores: list[dict[str, Any]] = []
    for source_response, absolute_score in zip(
        host["responses"], signature.exact_certificate(absolute_certificate)["response_scores"]
    ):
        permutation = source_response["permutation"]
        residual_rank1, line_cluster, total = score_from_residual(permutation, residual)
        reduced_total = score_from_reduced_residual(permutation, residual)
        require(total == reduced_total, "reduced residual gauge reconstruction failed")
        require(total == absolute_score["new_triples"], "residual/absolute score mismatch")
        response_scores.append(
            {
                "permutation": permutation,
                "residual_rank1_pairs": residual_rank1,
                "tracked_line_cluster_triples": line_cluster,
                "new_triples": total,
            }
        )

    minimum = min(record["new_triples"] for record in response_scores)
    minimizers = [record for record in response_scores if record["new_triples"] == minimum]
    selected = min(minimizers, key=lambda record: record["permutation"])
    claims = {
        "side": host["side"],
        "responses": len(response_scores),
        "background_points": len(background),
        "selector_signature_dimension": signature.basis_for_side(host["side"])[
            "selector_signature_dimension"
        ],
        "nonnegative_residual_coordinates": sum(
            value >= 0 for value in residual["rank1_residual_pair_counts"]
        ),
        "positive_residual_coordinates": sum(
            value > 0 for value in residual["rank1_residual_pair_counts"]
        ),
        "residual_pair_mass": sum(residual["rank1_residual_pair_counts"]),
        "tracked_pair_mass": sum(residual["tracked_response_line_pair_counts"]),
        "minimum_new_triples": minimum,
        "minimizer_count": len(minimizers),
        "selected_response": selected["permutation"],
        "response_scores_sha256": catalogue.canonical_digest(response_scores),
    }
    return {
        "absolute_signature_certificate": absolute_certificate,
        "residual_signature": residual,
        "response_scores": response_scores,
        "claims": claims,
    }


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    require(
        certificate.get("basis_sha256") == signature.build_basis()["basis_sha256"],
        "basis_sha256: incorrect",
    )
    exact = exact_certificate(certificate)
    require(
        certificate.get("absolute_signature_certificate")
        == exact["absolute_signature_certificate"],
        "absolute_signature_certificate: incorrect",
    )
    require(certificate.get("residual_signature") == exact["residual_signature"],
            "residual_signature: incorrect")
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
        "positive_residual_coordinates": claims["positive_residual_coordinates"],
        "residual_pair_mass": claims["residual_pair_mass"],
        "tracked_pair_mass": claims["tracked_pair_mass"],
        "minimum_new_triples": claims["minimum_new_triples"],
    }


def build_certificate(host: dict[str, Any], background: list[Point]) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "basis_sha256": signature.build_basis()["basis_sha256"],
        "host_id": host["host_id"],
        "catalogue_record_sha256": host["record_sha256"],
        "background_points": [list(point) for point in background],
    }
    exact = exact_certificate(certificate)
    certificate["absolute_signature_certificate"] = exact["absolute_signature_certificate"]
    certificate["residual_signature"] = exact["residual_signature"]
    certificate["claims"] = exact["claims"]
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def run_random_tests() -> tuple[int, Counter[str], Counter[int]]:
    random = Random(2070)
    source = catalogue.build_catalogue()
    totals: Counter[str] = Counter()
    minimums: Counter[int] = Counter()
    for _ in range(500):
        host = random.choice(source["hosts"])
        background = signature.random_background(host["side"], random)
        summary = validate_certificate(build_certificate(host, background))
        totals.update(summary)
        minimums[summary["minimum_new_triples"]] += 1
    require(totals["responses"] > 0, "random tests: no response scores")
    require(totals["tracked_pair_mass"] >= 0, "random tests: invalid tracked mass")
    return 500, totals, minimums


def run_mutation_tests() -> int:
    random = Random(101)
    host = catalogue.build_catalogue()["hosts"][350]
    certificate = build_certificate(host, signature.random_background(host["side"], random))
    validate_certificate(certificate)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(certificate)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data.update(certificate_sha256="0" * 64))
    add(lambda data: data.update(basis_sha256="0" * 64))
    add(lambda data: data.update(host_id="s5-corrupt"))
    add(lambda data: data["background_points"].append(data["background_points"][0]))
    add(lambda data: data["residual_signature"]["tracked_response_line_pair_counts"].pop())
    add(lambda data: data["residual_signature"]["rank1_residual_pair_counts"].append(-1))
    add(lambda data: data["residual_signature"]["residual_cross_differences"].append(999))
    add(lambda data: data["residual_signature"].update(residual_common_baseline=999))
    add(lambda data: data["absolute_signature_certificate"]["claims"].update(responses=999))
    add(lambda data: data["claims"].update(residual_pair_mass=-1))
    add(lambda data: data["claims"]["selected_response"].reverse())
    add(lambda data: data.update(version=2))

    rejected = 0
    for candidate in mutations:
        try:
            validate_certificate(candidate)
        except (
            ResidualSignatureError,
            signature.SignatureError,
            selector.BackgroundSelectorError,
            catalogue.CatalogueError,
        ):
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted certificate accepted")
    return rejected


def main() -> None:
    if len(sys.argv) > 2:
        raise SystemExit(
            "usage: check_prime_power_background_residual_signature.py [certificate.json]"
        )
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            certificate = json.load(handle)
        summary = validate_certificate(certificate)
        print(
            "accepted residual background signature: "
            f"{summary['responses']} responses, residual pair mass "
            f"{summary['residual_pair_mass']}"
        )
        return
    systems, totals, minimums = run_random_tests()
    rejected = run_mutation_tests()
    print(
        "verified residual background signatures: "
        f"{systems} systems, {totals['responses']} response scores, "
        f"{totals['background_points']} background points, residual/tracked pair mass "
        f"{totals['residual_pair_mass']}/{totals['tracked_pair_mass']}, "
        f"minimum distribution {sorted(minimums.items())}, and {rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
