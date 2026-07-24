#!/usr/bin/env python3
"""Compute pair-aware clone loads for a deleted-reservoir patch.

The source is a saturated no-three certificate on [m]^2. Repeated --delete
arguments remove reservoir points, and --t adds t new rows and columns. The
active host contains every cell joining a positive-deficit column to a
positive-deficit row, except retained cells and cells on retained old-pair
secants. Exact clone-weighted unavailable-cell, duplicate-cell, old-anchor-pair,
and internal-triple loads are then evaluated.

This is an exhaustive finite profiler for modest active hosts, not an
asymptotic proof that the load criterion holds.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any, Iterable

Point = tuple[int, int]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def no_three(points: Iterable[Point]) -> bool:
    pts = tuple(points)
    return all(determinant(a, b, c) != 0 for a, b, c in combinations(pts, 3))


def saturated(points: Iterable[Point], n: int) -> bool:
    pts = tuple(points)
    return (
        len(pts) == 2 * n
        and len(set(pts)) == len(pts)
        and all(sum(x == col for x, _ in pts) == 2 for col in range(1, n + 1))
        and all(sum(y == row for _, y in pts) == 2 for row in range(1, n + 1))
    )


def parse_point(text: str) -> Point:
    try:
        x_text, y_text = text.split(",", 1)
        return int(x_text), int(y_text)
    except (ValueError, TypeError) as exc:
        raise argparse.ArgumentTypeError("points must have form X,Y") from exc


def load_case(path: Path, selected_n: int | None) -> tuple[int, tuple[Point, ...]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    raw_cases = payload if isinstance(payload, list) else [payload]
    parsed: list[tuple[int, tuple[Point, ...]]] = []
    for ordinal, raw in enumerate(raw_cases, 1):
        if not isinstance(raw, dict):
            raise ValueError(f"case {ordinal}: expected an object")
        n = raw.get("n")
        raw_points = raw.get("points")
        if isinstance(n, bool) or not isinstance(n, int) or n < 2:
            raise ValueError(f"case {ordinal}: invalid n")
        if not isinstance(raw_points, list):
            raise ValueError(f"case {ordinal}: points must be a list")
        points: list[Point] = []
        for index, raw_point in enumerate(raw_points):
            if not isinstance(raw_point, list) or len(raw_point) != 2:
                raise ValueError(f"case {ordinal}: malformed point {index}")
            x, y = raw_point
            if (
                isinstance(x, bool)
                or isinstance(y, bool)
                or not isinstance(x, int)
                or not isinstance(y, int)
            ):
                raise ValueError(f"case {ordinal}: nonintegral point {index}")
            points.append((x, y))
        if not saturated(points, n) or not no_three(points):
            raise ValueError(f"case {ordinal}: not a saturated no-three certificate")
        parsed.append((n, tuple(sorted(points))))

    if selected_n is not None:
        parsed = [case for case in parsed if case[0] == selected_n]
    if len(parsed) != 1:
        raise ValueError("select exactly one certificate, using --n for a list")
    return parsed[0]


def falling(n: int, rank: int) -> int:
    out = 1
    for offset in range(rank):
        out *= n - offset
    return out


def analyze(
    core: tuple[Point, ...],
    m: int,
    t: int,
    deleted: frozenset[Point],
) -> dict[str, Any]:
    retained = tuple(point for point in core if point not in deleted)
    target_n = m + t

    column_deficit: dict[int, int] = {}
    row_deficit: dict[int, int] = {}
    for x, y in deleted:
        column_deficit[x] = column_deficit.get(x, 0) + 1
        row_deficit[y] = row_deficit.get(y, 0) + 1
    for index in range(m + 1, target_n + 1):
        column_deficit[index] = 2
        row_deficit[index] = 2

    N = sum(column_deficit.values())
    if N != sum(row_deficit.values()):
        raise AssertionError("row and column deficit sums disagree")
    if N < 3:
        raise ValueError("the active clone size must be at least three")
    if max(column_deficit.values(), default=0) > 2 or max(row_deficit.values(), default=0) > 2:
        raise AssertionError("a saturated deletion can create deficit at most two")

    active_columns = tuple(sorted(column_deficit))
    active_rows = tuple(sorted(row_deficit))
    retained_set = frozenset(retained)
    old_pairs = tuple(combinations(retained, 2))

    all_cells = tuple((x, y) for x in active_columns for y in active_rows)
    unavailable = {
        cell
        for cell in all_cells
        if cell in retained_set
        or any(determinant(first, second, cell) == 0 for first, second in old_pairs)
    }
    allowed = tuple(cell for cell in all_cells if cell not in unavailable)

    forbidden_pairs: list[tuple[Point, Point]] = []
    for first, second in combinations(allowed, 2):
        if first[0] == second[0] or first[1] == second[1]:
            continue
        if any(determinant(first, second, anchor) == 0 for anchor in retained):
            forbidden_pairs.append((first, second))

    internal_triples: list[tuple[Point, Point, Point]] = []
    for triple in combinations(allowed, 3):
        if len({point[0] for point in triple}) < 3:
            continue
        if len({point[1] for point in triple}) < 3:
            continue
        if determinant(*triple) == 0:
            internal_triples.append(triple)

    denominator2 = falling(N, 2)
    denominator3 = falling(N, 3)
    loads: dict[tuple[str, int], tuple[int, int, int, int, Fraction]] = {}

    for x in active_columns:
        unavailable_weight = sum(row_deficit[y] for xx, y in unavailable if xx == x)
        duplicate_weight = sum(
            row_deficit[y] * (column_deficit[x] - 1) * (row_deficit[y] - 1)
            for xx, y in allowed
            if xx == x
        )
        pair_weight = 0
        for first, second in forbidden_pairs:
            if first[0] == x:
                pair_weight += (
                    row_deficit[first[1]]
                    * column_deficit[second[0]]
                    * row_deficit[second[1]]
                )
            elif second[0] == x:
                pair_weight += (
                    row_deficit[second[1]]
                    * column_deficit[first[0]]
                    * row_deficit[first[1]]
                )
        triple_weight = 0
        for triple in internal_triples:
            for index, point in enumerate(triple):
                if point[0] != x:
                    continue
                weight = row_deficit[point[1]]
                for other_index, other in enumerate(triple):
                    if other_index != index:
                        weight *= column_deficit[other[0]] * row_deficit[other[1]]
                triple_weight += weight

        load = (
            Fraction(unavailable_weight, N)
            + Fraction(duplicate_weight + pair_weight, denominator2)
            + Fraction(triple_weight, denominator3)
        )
        loads[("column", x)] = (
            unavailable_weight,
            duplicate_weight,
            pair_weight,
            triple_weight,
            load,
        )

    for y in active_rows:
        unavailable_weight = sum(column_deficit[x] for x, yy in unavailable if yy == y)
        duplicate_weight = sum(
            column_deficit[x] * (row_deficit[y] - 1) * (column_deficit[x] - 1)
            for x, yy in allowed
            if yy == y
        )
        pair_weight = 0
        for first, second in forbidden_pairs:
            if first[1] == y:
                pair_weight += (
                    column_deficit[first[0]]
                    * column_deficit[second[0]]
                    * row_deficit[second[1]]
                )
            elif second[1] == y:
                pair_weight += (
                    column_deficit[second[0]]
                    * column_deficit[first[0]]
                    * row_deficit[first[1]]
                )
        triple_weight = 0
        for triple in internal_triples:
            for index, point in enumerate(triple):
                if point[1] != y:
                    continue
                weight = column_deficit[point[0]]
                for other_index, other in enumerate(triple):
                    if other_index != index:
                        weight *= column_deficit[other[0]] * row_deficit[other[1]]
                triple_weight += weight

        load = (
            Fraction(unavailable_weight, N)
            + Fraction(duplicate_weight + pair_weight, denominator2)
            + Fraction(triple_weight, denominator3)
        )
        loads[("row", y)] = (
            unavailable_weight,
            duplicate_weight,
            pair_weight,
            triple_weight,
            load,
        )

    worst_key, worst_data = max(loads.items(), key=lambda item: item[1][-1])

    unavailable_incidence = {
        ("column", x): sum(1 for xx, _ in unavailable if xx == x)
        for x in active_columns
    }
    unavailable_incidence.update({
        ("row", y): sum(1 for _, yy in unavailable if yy == y)
        for y in active_rows
    })
    pair_incidence = {
        ("column", x): sum(x in (a[0], b[0]) for a, b in forbidden_pairs)
        for x in active_columns
    }
    pair_incidence.update({
        ("row", y): sum(y in (a[1], b[1]) for a, b in forbidden_pairs)
        for y in active_rows
    })
    triple_incidence = {
        ("column", x): sum(any(point[0] == x for point in triple) for triple in internal_triples)
        for x in active_columns
    }
    triple_incidence.update({
        ("row", y): sum(any(point[1] == y for point in triple) for triple in internal_triples)
        for y in active_rows
    })

    u_star = max(unavailable_incidence.values(), default=0)
    pi_star = max(pair_incidence.values(), default=0)
    tau_star = max(triple_incidence.values(), default=0)
    coarse_load = (
        Fraction(2 * u_star, N)
        + Fraction(1, N - 1)
        + Fraction(8 * pi_star, denominator2)
        + Fraction(32 * tau_star, denominator3)
    )

    return {
        "source_n": m,
        "target_n": target_n,
        "t": t,
        "deleted": [list(point) for point in sorted(deleted)],
        "clone_size": N,
        "active_columns": {str(x): column_deficit[x] for x in active_columns},
        "active_rows": {str(y): row_deficit[y] for y in active_rows},
        "candidate_cells": len(all_cells),
        "allowed_cells": len(allowed),
        "unavailable_cells": len(unavailable),
        "forbidden_old_anchor_pairs": len(forbidden_pairs),
        "internal_candidate_triples": len(internal_triples),
        "exact_max_load_fraction": f"{worst_data[-1].numerator}/{worst_data[-1].denominator}",
        "exact_max_load_decimal": float(worst_data[-1]),
        "exact_worst_coordinate": {"kind": worst_key[0], "index": worst_key[1]},
        "exact_criterion_passes": worst_data[-1] <= Fraction(1, 24),
        "u_star": u_star,
        "pi_star": pi_star,
        "tau_star": tau_star,
        "coarse_load_fraction": f"{coarse_load.numerator}/{coarse_load.denominator}",
        "coarse_load_decimal": float(coarse_load),
        "coarse_criterion_passes": coarse_load <= Fraction(1, 24),
        "robust_bounds_pass": (
            N >= 200
            and 200 * u_star <= N
            and 1600 * pi_star <= N * N
            and 3200 * tau_star <= N * N * N
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int, help="select one source size from a list")
    parser.add_argument("--t", type=int, required=True)
    parser.add_argument(
        "--delete",
        type=parse_point,
        action="append",
        default=[],
        metavar="X,Y",
        help="delete one source point; may be repeated",
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.t < 1:
        raise SystemExit("t must be positive")

    try:
        m, core = load_case(args.certificate, args.n)
        deleted = frozenset(args.delete)
        if len(deleted) != len(args.delete):
            raise ValueError("duplicate --delete point")
        missing = sorted(deleted.difference(core))
        if missing:
            raise ValueError(f"deleted points are not in the source certificate: {missing}")
        result = analyze(core, m, args.t, deleted)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
