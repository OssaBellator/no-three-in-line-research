#!/usr/bin/env python3
"""Validate necessary finite realizability inequalities for survivor signatures.

The canonical background signature records occupancies h_B(L) on the finite response-
line universe and point-pair counts p_B(q) on the response grid.  This checker adds
four families of exact necessary constraints that can be checked before any selector
or labelled-row work:

* per-line bounds and the global tracked-pair budget;
* parallel-class occupancy budgets;
* concurrent-pencil occupancy budgets;
* tracked-pair residual nonnegativity at every response-grid point.

The conditions are necessary, not sufficient, for geometric realizability.
"""
from __future__ import annotations

import copy
import json
import math
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from random import Random
from typing import Any

import check_prime_power_background_signature as signature
import check_prime_power_canonical_raw_host_catalogue as catalogue

Point = tuple[int, int]
Line = tuple[int, int, int]
EXPECTED_FEASIBILITY_SHA256 = "ba1d47beb3e58e7700ecf9cfb08e8fae76c3be0299163311bb0f8d784ef6466c"


class FeasibilityError(ValueError):
    """Raised when a feasibility basis or certificate is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise FeasibilityError(message)


def point_on_line(point: Point, line: Line) -> bool:
    x, y = point
    a, b, c = line
    return a * x + b * y + c == 0


def rational_intersection(first: Line, second: Line) -> tuple[Fraction, Fraction] | None:
    a1, b1, c1 = first
    a2, b2, c2 = second
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return None
    x = Fraction(b1 * c2 - b2 * c1, determinant)
    y = Fraction(c1 * a2 - c2 * a1, determinant)
    return x, y


@lru_cache(maxsize=1)
def _build_basis_cached() -> dict[str, Any]:
    source = signature.build_basis()
    signature.validate_basis(source)
    side_records: list[dict[str, Any]] = []
    for side_record in source["sides"]:
        side = side_record["side"]
        lines = [tuple(line) for line in side_record["response_lines"]]

        parallel: dict[tuple[int, int], list[int]] = defaultdict(list)
        for index, (a, b, _c) in enumerate(lines):
            parallel[(a, b)].append(index)
        parallel_classes = [indices for indices in parallel.values() if len(indices) >= 2]
        parallel_classes.sort()

        point_to_lines: dict[tuple[Fraction, Fraction], set[int]] = defaultdict(set)
        for left in range(len(lines)):
            for right in range(left + 1, len(lines)):
                point = rational_intersection(lines[left], lines[right])
                if point is None:
                    continue
                point_to_lines[point].update((left, right))
        pencils = []
        for point, indices in point_to_lines.items():
            ordered = sorted(indices)
            pencils.append(
                {
                    "intersection": [
                        [point[0].numerator, point[0].denominator],
                        [point[1].numerator, point[1].denominator],
                    ],
                    "line_indices": ordered,
                }
            )
        pencils.sort(key=lambda record: (record["intersection"], record["line_indices"]))
        maximum_concurrency = max([1] + [len(record["line_indices"]) for record in pencils])

        grid = [tuple(point) for point in side_record["grid_points"]]
        point_line_indices = [
            [index for index, line in enumerate(lines) if point_on_line(point, line)]
            for point in grid
        ]

        side_records.append(
            {
                "side": side,
                "response_lines": [list(line) for line in lines],
                "parallel_classes": parallel_classes,
                "intersection_pencils": pencils,
                "point_line_indices": point_line_indices,
                "maximum_line_concurrency": maximum_concurrency,
                "parallel_class_count": len(parallel_classes),
                "pencil_count": len(pencils),
            }
        )

    payload: dict[str, Any] = {
        "version": 1,
        "source_signature_basis_sha256": source["basis_sha256"],
        "sides": side_records,
    }
    payload["claims"] = {
        "side4_parallel_classes": side_records[0]["parallel_class_count"],
        "side5_parallel_classes": side_records[1]["parallel_class_count"],
        "side4_pencils": side_records[0]["pencil_count"],
        "side5_pencils": side_records[1]["pencil_count"],
        "side4_maximum_concurrency": side_records[0]["maximum_line_concurrency"],
        "side5_maximum_concurrency": side_records[1]["maximum_line_concurrency"],
        "side4_point_constraints": len(side_records[0]["point_line_indices"]),
        "side5_point_constraints": len(side_records[1]["point_line_indices"]),
    }
    payload["feasibility_sha256"] = catalogue.canonical_digest(payload)
    return payload


def build_basis() -> dict[str, Any]:
    return copy.deepcopy(_build_basis_cached())


def validate_basis(basis: Any) -> dict[str, int]:
    require(isinstance(basis, dict), "basis: expected object")
    expected = _build_basis_cached()
    for key in ("version", "source_signature_basis_sha256", "sides", "claims", "feasibility_sha256"):
        require(basis.get(key) == expected[key], f"basis.{key}: canonical mismatch")
    if EXPECTED_FEASIBILITY_SHA256 != "TO_BE_FILLED":
        require(
            expected["feasibility_sha256"] == EXPECTED_FEASIBILITY_SHA256,
            "built-in feasibility digest drift",
        )
    return copy.deepcopy(expected["claims"])


def basis_for_side(side: int) -> dict[str, Any]:
    return next(record for record in _build_basis_cached()["sides"] if record["side"] == side)


def exact_constraints(side: int, background: list[Point]) -> dict[str, Any]:
    survivor = signature.exact_signature(side, background)
    basis = basis_for_side(side)
    h = survivor["response_line_background_counts"]
    p = survivor["rank1_point_pair_counts"]
    n = len(background)

    line_slacks = [n - value for value in h]
    pair_budget_slack = math.comb(n, 2) - sum(math.comb(value, 2) for value in h)
    parallel_slacks = [n - sum(h[index] for index in indices) for indices in basis["parallel_classes"]]
    pencil_slacks = [
        n + len(record["line_indices"]) - 1
        - sum(h[index] for index in record["line_indices"])
        for record in basis["intersection_pencils"]
    ]
    incidence_slack = basis["maximum_line_concurrency"] * n - sum(h)
    residuals = [
        observed - sum(math.comb(h[index], 2) for index in indices)
        for observed, indices in zip(p, basis["point_line_indices"])
    ]

    require(all(value >= 0 for value in line_slacks), "line occupancy exceeds background size")
    require(pair_budget_slack >= 0, "tracked-line pair budget exceeds all background pairs")
    require(all(value >= 0 for value in parallel_slacks), "parallel-class occupancy budget failed")
    require(all(value >= 0 for value in pencil_slacks), "concurrent-pencil occupancy budget failed")
    require(incidence_slack >= 0, "global line-incidence concurrency budget failed")
    require(all(value >= 0 for value in residuals), "tracked pair contribution exceeds point-pair count")

    return {
        "source_signature": survivor,
        "line_occupancy_slacks": line_slacks,
        "tracked_pair_budget_slack": pair_budget_slack,
        "parallel_class_slacks": parallel_slacks,
        "intersection_pencil_slacks": pencil_slacks,
        "global_incidence_slack": incidence_slack,
        "point_residual_pair_counts": residuals,
    }


def exact_certificate(certificate: dict[str, Any]) -> dict[str, Any]:
    side = certificate.get("side")
    require(side in (4, 5), "side: expected 4 or 5")
    raw_background = certificate.get("background_points")
    require(isinstance(raw_background, list), "background_points: expected list")
    background = [signature.parse_point(value, f"background_points[{index}]") for index, value in enumerate(raw_background)]
    require(len(background) == len(set(background)), "background_points: duplicates")
    grid = {(x, y) for x in range(side) for y in range(side)}
    require(not (set(background) & grid), "background_points: intersects response grid")
    constraints = exact_constraints(side, background)
    claims = {
        "side": side,
        "background_points": len(background),
        "response_lines": len(constraints["source_signature"]["response_line_background_counts"]),
        "parallel_classes": len(constraints["parallel_class_slacks"]),
        "intersection_pencils": len(constraints["intersection_pencil_slacks"]),
        "point_constraints": len(constraints["point_residual_pair_counts"]),
        "tracked_pairs": sum(
            math.comb(value, 2)
            for value in constraints["source_signature"]["response_line_background_counts"]
        ),
        "residual_pair_mass": sum(constraints["point_residual_pair_counts"]),
        "minimum_constraint_slack": min(
            constraints["line_occupancy_slacks"]
            + [constraints["tracked_pair_budget_slack"]]
            + constraints["parallel_class_slacks"]
            + constraints["intersection_pencil_slacks"]
            + [constraints["global_incidence_slack"]]
            + constraints["point_residual_pair_counts"]
        ),
        "constraints_sha256": catalogue.canonical_digest(constraints),
    }
    return {"constraints": constraints, "claims": claims}


def validate_certificate(certificate: Any) -> dict[str, int]:
    require(isinstance(certificate, dict), "certificate: expected object")
    require(certificate.get("version") == 1, "version: expected 1")
    require(
        certificate.get("feasibility_basis_sha256") == _build_basis_cached()["feasibility_sha256"],
        "feasibility_basis_sha256: incorrect",
    )
    exact = exact_certificate(certificate)
    require(certificate.get("constraints") == exact["constraints"], "constraints: incorrect")
    require(certificate.get("claims") == exact["claims"], "claims: incorrect")
    payload = {key: value for key, value in certificate.items() if key != "certificate_sha256"}
    require(certificate.get("certificate_sha256") == catalogue.canonical_digest(payload), "certificate_sha256: incorrect")
    return {
        "background_points": exact["claims"]["background_points"],
        "tracked_pairs": exact["claims"]["tracked_pairs"],
        "residual_pair_mass": exact["claims"]["residual_pair_mass"],
        "minimum_slack": exact["claims"]["minimum_constraint_slack"],
        "side4": int(exact["claims"]["side"] == 4),
        "side5": int(exact["claims"]["side"] == 5),
    }


def build_certificate(side: int, background: list[Point]) -> dict[str, Any]:
    certificate: dict[str, Any] = {
        "version": 1,
        "feasibility_basis_sha256": _build_basis_cached()["feasibility_sha256"],
        "side": side,
        "background_points": [list(point) for point in background],
    }
    exact = exact_certificate(certificate)
    certificate["constraints"] = exact["constraints"]
    certificate["claims"] = exact["claims"]
    certificate["certificate_sha256"] = catalogue.canonical_digest(certificate)
    return certificate


def run_random_tests() -> tuple[int, Counter[str], Counter[int]]:
    random = Random(2094)
    totals: Counter[str] = Counter()
    minimums: Counter[int] = Counter()
    for _ in range(500):
        side = random.choice((4, 5))
        background = signature.random_background(side, random)
        summary = validate_certificate(build_certificate(side, background))
        totals.update(summary)
        minimums[summary["minimum_slack"]] += 1
    return 500, totals, minimums


def run_mutation_tests() -> int:
    random = Random(113)
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
    add(lambda data: data.update(feasibility_basis_sha256="0" * 64))
    add(lambda data: data.update(version=2))
    add(lambda data: data.update(side=3))
    add(lambda data: data["background_points"].append(data["background_points"][0]))
    add(lambda data: data["constraints"]["line_occupancy_slacks"].pop())
    add(lambda data: data["constraints"].update(tracked_pair_budget_slack=-1))
    add(lambda data: data["constraints"]["parallel_class_slacks"].append(999))
    add(lambda data: data["constraints"]["intersection_pencil_slacks"].reverse())
    add(lambda data: data["constraints"].update(global_incidence_slack=999))
    add(lambda data: data["constraints"]["point_residual_pair_counts"].pop())
    add(lambda data: data["claims"].update(minimum_constraint_slack=-1))
    rejected = 0
    for candidate in mutations:
        try:
            validate_certificate(candidate)
        except (FeasibilityError, signature.SignatureError, catalogue.CatalogueError):
            rejected += 1
    require(rejected == len(mutations), "mutation tests: corrupted certificate accepted")
    return rejected


def main() -> None:
    if len(sys.argv) == 3 and sys.argv[1] == "--write-basis":
        basis = build_basis()
        validate_basis(basis)
        Path(sys.argv[2]).write_text(json.dumps(basis, sort_keys=True, indent=2) + "\n", encoding="utf-8")
        print(f"wrote signature feasibility basis: sha256 {basis['feasibility_sha256']}")
        return
    if len(sys.argv) == 2:
        with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
            certificate = json.load(handle)
        summary = validate_certificate(certificate)
        print(f"accepted signature feasibility certificate: {summary['background_points']} background points")
        return
    if len(sys.argv) != 1:
        raise SystemExit("usage: check_prime_power_background_signature_feasibility.py [certificate.json | --write-basis basis.json]")
    basis = build_basis()
    claims = validate_basis(basis)
    systems, totals, minimums = run_random_tests()
    rejected = run_mutation_tests()
    print(
        "verified signature feasibility constraints: "
        f"parallel classes {claims['side4_parallel_classes']}/{claims['side5_parallel_classes']}, "
        f"pencils {claims['side4_pencils']}/{claims['side5_pencils']}, "
        f"maximum concurrency {claims['side4_maximum_concurrency']}/{claims['side5_maximum_concurrency']}, "
        f"{systems} systems, {totals['background_points']} background points, "
        f"{totals['tracked_pairs']} tracked pairs, {totals['residual_pair_mass']} residual point-pair mass, "
        f"minimum-slack distribution {sorted(minimums.items())}, "
        f"basis sha256 {basis['feasibility_sha256']}, and {rejected} corruptions rejected"
    )


if __name__ == "__main__":
    main()
