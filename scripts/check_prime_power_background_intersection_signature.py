#!/usr/bin/env python3
"""Validate exact tracked-line intersection occupancies for survivor backgrounds.

The feasibility checker stores every rational intersection pencil of the finite response-
line universe. This checker adds the exact occupancy bit of each common intersection,
the exact union size of each pencil, and the exact tracked-line degree of every
background point.
"""
from __future__ import annotations

import copy
import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path
from random import Random
from typing import Any

import check_prime_power_background_signature as signature
import check_prime_power_background_signature_feasibility as feasibility
import check_prime_power_canonical_raw_host_catalogue as catalogue

Point = tuple[int, int]
Line = tuple[int, int, int]


class IntersectionSignatureError(ValueError):
    """Raised when an intersection-occupancy signature is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise IntersectionSignatureError(message)


def point_on_line(point: Point, line: Line) -> bool:
    x, y = point
    a, b, c = line
    return a * x + b * y + c == 0


def parse_rational_pair(value: list[list[int]]) -> tuple[Fraction, Fraction]:
    require(
        isinstance(value, list)
        and len(value) == 2
        and all(isinstance(coordinate, list) and len(coordinate) == 2 for coordinate in value),
        "intersection: expected [[x_num,x_den],[y_num,y_den]]",
    )
    return Fraction(value[0][0], value[0][1]), Fraction(value[1][0], value[1][1])


def integer_intersection(point: tuple[Fraction, Fraction]) -> Point | None:
    if point[0].denominator != 1 or point[1].denominator != 1:
        return None
    return point[0].numerator, point[1].numerator


def exact_signature(side: int, background: list[Point]) -> dict[str, Any]:
    feasibility_basis = feasibility.basis_for_side(side)
    survivor = signature.exact_signature(side, background)
    lines = [tuple(line) for line in feasibility_basis["response_lines"]]
    line_counts = survivor["response_line_background_counts"]
    background_set = set(background)

    pencil_records: list[dict[str, Any]] = []
    occupied_intersections = 0
    tightened_pencils = 0
    total_union_mass = 0
    for pencil in feasibility_basis["intersection_pencils"]:
        point = parse_rational_pair(pencil["intersection"])
        integer_point = integer_intersection(point)
        occupied = int(integer_point is not None and integer_point in background_set)
        indices = pencil["line_indices"]
        union_points = [
            background_point
            for background_point in background
            if any(point_on_line(background_point, lines[index]) for index in indices)
        ]
        union_count = len(union_points)
        incidence_sum = sum(line_counts[index] for index in indices)
        expected_incidence = union_count + (len(indices) - 1) * occupied
        require(incidence_sum == expected_incidence, "pencil incidence identity failed")
        slack = len(background) - union_count
        require(slack >= 0, "pencil union exceeds background")
        sharpened_bound = len(background) + (len(indices) - 1) * occupied
        require(incidence_sum <= sharpened_bound, "sharpened pencil bound failed")
        if not occupied:
            tightened_pencils += 1
        occupied_intersections += occupied
        total_union_mass += union_count
        record = {
            "intersection": pencil["intersection"],
            "line_indices": indices,
            "intersection_occupied": occupied,
            "incidence_sum": incidence_sum,
            "union_count": union_count,
            "union_slack": slack,
            "sharpened_incidence_bound": sharpened_bound,
        }
        record["pencil_record_sha256"] = catalogue.canonical_digest(record)
        pencil_records.append(record)

    point_records: list[dict[str, Any]] = []
    degree_distribution: Counter[int] = Counter()
    total_degree = 0
    for point in sorted(background):
        line_indices = [index for index, line in enumerate(lines) if point_on_line(point, line)]
        degree = len(line_indices)
        require(
            degree <= feasibility_basis["maximum_line_concurrency"],
            "point exceeds maximum tracked-line concurrency",
        )
        degree_distribution[degree] += 1
        total_degree += degree
        point_records.append(
            {
                "point": list(point),
                "tracked_line_indices": line_indices,
                "tracked_line_degree": degree,
            }
        )
    require(total_degree == sum(line_counts), "global tracked incidence identity failed")

    output: dict[str, Any] = {
        "side": side,
        "background_points": [list(point) for point in background],
        "source_signature_sha256": survivor["signature_sha256"],
        "source_feasibility_sha256": feasibility.build_basis()["feasibility_sha256"],
        "pencil_records": pencil_records,
        "background_point_records": point_records,
        "claims": {
            "background_size": len(background),
            "tracked_lines": len(lines),
            "intersection_pencils": len(pencil_records),
            "occupied_intersections": occupied_intersections,
            "unoccupied_intersections": len(pencil_records) - occupied_intersections,
            "tightened_pencils": tightened_pencils,
            "total_pencil_union_mass": total_union_mass,
            "total_tracked_incidence": total_degree,
            "maximum_observed_degree": max([0] + [record["tracked_line_degree"] for record in point_records]),
            "degree_distribution": [[degree, degree_distribution[degree]] for degree in sorted(degree_distribution)],
            "pencil_records_sha256": catalogue.canonical_digest(pencil_records),
            "point_records_sha256": catalogue.canonical_digest(point_records),
        },
    }
    output["intersection_signature_sha256"] = catalogue.canonical_digest(output)
    return output


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    side = certificate.get("side")
    require(side in (4, 5), "side: expected 4 or 5")
    raw_background = certificate.get("background_points")
    require(isinstance(raw_background, list), "background_points: expected list")
    background = [
        signature.parse_point(value, f"background_points[{index}]")
        for index, value in enumerate(raw_background)
    ]
    require(len(background) == len(set(background)), "background_points: duplicates")
    grid = {(left, right) for left in range(side) for right in range(side)}
    require(not (set(background) & grid), "background_points: intersects response grid")

    feasibility_certificate = feasibility.build_certificate(side, background)
    feasibility.validate_certificate(feasibility_certificate)
    intersection = exact_signature(side, background)
    return {"feasibility_certificate": feasibility_certificate, "intersection_signature": intersection}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    exact = exact_certificate(certificate)
    require(
        certificate.get("feasibility_certificate") == exact["feasibility_certificate"],
        "feasibility_certificate: incorrect",
    )
    require(
        certificate.get("intersection_signature") == exact["intersection_signature"],
        "intersection_signature: incorrect",
    )
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(
        certificate.get("certificate_sha256") == catalogue.canonical_digest(payload),
        "certificate_sha256: incorrect",
    )
    claims = exact["intersection_signature"]["claims"]
    return {
        "background_points": claims["background_size"],
        "pencils": claims["intersection_pencils"],
        "occupied": claims["occupied_intersections"],
        "unoccupied": claims["unoccupied_intersections"],
        "tightened": claims["tightened_pencils"],
        "incidence": claims["total_tracked_incidence"],
        "maximum_degree": claims["maximum_observed_degree"],
        "side4": int(certificate["side"] == 4),
        "side5": int(certificate["side"] == 5),
    }


def build_certificate(side: int, background: list[Point]) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "side": side,
        "background_points": [list(point) for point in background],
    }
    exact = exact_certificate(certificate)
    certificate["feasibility_certificate"] = exact["feasibility_certificate"]
    certificate["intersection_signature"] = exact["intersection_signature"]
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def run_random_tests() -> tuple[int, Counter[str], Counter[int]]:
    random = Random(2150)
    totals: Counter[str] = Counter()
    maximum_degrees: Counter[int] = Counter()
    for _ in range(500):
        side = random.choice((4, 5))
        background = signature.random_background(side, random)
        summary = validate_certificate(build_certificate(side, background))
        totals.update(summary)
        maximum_degrees[summary["maximum_degree"]] += 1
        require(summary["tightened"] == summary["unoccupied"], "tightened/unoccupied pencil mismatch")
    return 500, totals, maximum_degrees


def run_mutation_tests() -> int:
    random = Random(157)
    background = signature.random_background(5, random)
    if not background:
        background = [(-1, -1)]
    certificate = build_certificate(5, background)
    validate_certificate(certificate)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(certificate)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data.update(certificate_sha256="0" * 64))
    add(lambda data: data.update(version=2))
    add(lambda data: data.update(side=3))
    add(lambda data: data["background_points"].append(data["background_points"][0]))
    add(lambda data: data["intersection_signature"]["pencil_records"].reverse())
    add(lambda data: data["intersection_signature"]["pencil_records"][0].update(intersection_occupied=2))
    add(lambda data: data["intersection_signature"]["pencil_records"][0].update(union_count=999))
    add(lambda data: data["intersection_signature"]["background_point_records"].pop())
    add(lambda data: data["intersection_signature"]["claims"].update(total_tracked_incidence=999))
    add(lambda data: data["intersection_signature"].update(intersection_signature_sha256="f" * 64))
    add(lambda data: data["feasibility_certificate"].update(certificate_sha256="0" * 64))
    add(lambda data: data["intersection_signature"]["claims"].update(maximum_observed_degree=999))

    rejected = 0
    for candidate in mutations:
        try:
            validate_certificate(candidate)
        except (
            IntersectionSignatureError,
            feasibility.FeasibilityError,
            signature.SignatureError,
            catalogue.CatalogueError,
        ):
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted intersection signature accepted")
    return rejected


def main() -> None:
    if len(sys.argv) == 2:
        certificate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        print(validate_certificate(certificate))
        return
    require(len(sys.argv) == 1, "usage: check_prime_power_background_intersection_signature.py [certificate.json]")
    systems, totals, maximum_degrees = run_random_tests()
    rejected = run_mutation_tests()
    print(
        "verified background intersection signatures: "
        f"{systems} systems, {totals['background_points']} background points, "
        f"{totals['pencils']} pencil checks, {totals['occupied']} occupied and "
        f"{totals['unoccupied']} unoccupied intersections, {totals['incidence']} tracked incidences, "
        f"maximum-degree distribution {sorted(maximum_degrees.items())}, and {rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
