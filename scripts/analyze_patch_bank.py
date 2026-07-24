#!/usr/bin/env python3
"""Verify a finite internally clean patch bank and evaluate PP2j/PP2k.

Bank JSON is either a list of states or {"states": [...]}. A state may be a
point list directly or an object with "label" and "points". Points are the
inserted cells, not the full target configuration.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any

from analyze_reservoir_patch_loads import (
    Point,
    determinant,
    load_case,
    no_three,
    parse_point,
)


def json_point(raw: Any, label: str) -> Point:
    if not isinstance(raw, list) or len(raw) != 2:
        raise ValueError(f"{label}: malformed point")
    x, y = raw
    if (
        isinstance(x, bool)
        or isinstance(y, bool)
        or not isinstance(x, int)
        or not isinstance(y, int)
    ):
        raise ValueError(f"{label}: nonintegral point")
    return x, y


def load_bank(path: Path) -> list[tuple[str, tuple[Point, ...]]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    raw_states = payload.get("states") if isinstance(payload, dict) else payload
    if not isinstance(raw_states, list) or not raw_states:
        raise ValueError("bank must contain a nonempty state list")

    bank: list[tuple[str, tuple[Point, ...]]] = []
    for ordinal, raw in enumerate(raw_states, 1):
        if isinstance(raw, dict):
            raw_points = raw.get("points")
            label = str(raw.get("label", f"state-{ordinal}"))
        else:
            raw_points = raw
            label = f"state-{ordinal}"
        if not isinstance(raw_points, list):
            raise ValueError(f"{label}: points must be a list")
        points = tuple(
            sorted(
                json_point(point, f"{label} point {index}")
                for index, point in enumerate(raw_points)
            )
        )
        bank.append((label, points))
    return bank


def analyze(
    core: tuple[Point, ...],
    m: int,
    t: int,
    deleted: frozenset[Point],
    bank: list[tuple[str, tuple[Point, ...]]],
) -> dict[str, Any]:
    target_n = m + t
    retained = tuple(point for point in core if point not in deleted)
    retained_set = frozenset(retained)

    column_deficit: Counter[int] = Counter(x for x, _ in deleted)
    row_deficit: Counter[int] = Counter(y for _, y in deleted)
    for index in range(m + 1, target_n + 1):
        column_deficit[index] = 2
        row_deficit[index] = 2
    N = sum(column_deficit.values())
    if N != sum(row_deficit.values()):
        raise AssertionError("deficit sums disagree")

    checked: list[tuple[str, tuple[Point, ...]]] = []
    for label, points in bank:
        if len(points) != N:
            raise ValueError(f"{label}: expected {N} inserted cells, found {len(points)}")
        if len(set(points)) != len(points):
            raise ValueError(f"{label}: duplicate inserted cells")
        if any(not (1 <= x <= target_n and 1 <= y <= target_n) for x, y in points):
            raise ValueError(f"{label}: cell outside [1,{target_n}]^2")
        overlap = sorted(set(points).intersection(retained_set))
        if overlap:
            raise ValueError(f"{label}: overlaps retained points: {overlap}")
        actual_columns = Counter(x for x, _ in points)
        actual_rows = Counter(y for _, y in points)
        if any(actual_columns[index] != column_deficit[index] for index in range(1, target_n + 1)):
            raise ValueError(f"{label}: column deficits are not filled exactly")
        if any(actual_rows[index] != row_deficit[index] for index in range(1, target_n + 1)):
            raise ValueError(f"{label}: row deficits are not filled exactly")
        if not no_three(points):
            raise ValueError(f"{label}: inserted state has an internal collinear triple")
        checked.append((label, points))

    old_pairs = tuple(combinations(retained, 2))
    cell_frequency: Counter[Point] = Counter()
    pair_frequency: Counter[tuple[Point, Point]] = Counter()
    certificate_counts: list[int] = []

    for _, points in checked:
        cell_frequency.update(points)
        pairs = tuple(combinations(points, 2))
        pair_frequency.update(pairs)
        blocked = sum(
            any(determinant(a, b, point) == 0 for a, b in old_pairs)
            for point in points
        )
        anchored = sum(
            any(determinant(pair[0], pair[1], anchor) == 0 for anchor in retained)
            for pair in pairs
        )
        certificate_counts.append(blocked + anchored)

    state_count = len(checked)
    support_cells = tuple(sorted(cell_frequency))
    blocked_support = {
        point
        for point in support_cells
        if any(determinant(a, b, point) == 0 for a, b in old_pairs)
    }
    anchored_support_pairs = {
        pair
        for pair in combinations(support_cells, 2)
        if any(determinant(pair[0], pair[1], anchor) == 0 for anchor in retained)
    }

    exact_expectation = Fraction(sum(certificate_counts), state_count)
    max_cell_probability = Fraction(max(cell_frequency.values(), default=0), state_count)
    max_pair_probability = Fraction(max(pair_frequency.values(), default=0), state_count)
    spread_bound = (
        max_cell_probability * len(blocked_support)
        + max_pair_probability * len(anchored_support_pairs)
    )
    clean_states = [
        {"label": label, "points": [list(point) for point in points]}
        for (label, points), count in zip(checked, certificate_counts)
        if count == 0
    ]

    return {
        "source_n": m,
        "target_n": target_n,
        "t": t,
        "deleted": [list(point) for point in sorted(deleted)],
        "clone_size": N,
        "state_count": state_count,
        "support_cells": len(support_cells),
        "blocked_support_cells": len(blocked_support),
        "anchored_support_pairs": len(anchored_support_pairs),
        "max_cell_probability_fraction": str(max_cell_probability),
        "max_pair_probability_fraction": str(max_pair_probability),
        "exact_PP2j_expectation_fraction": str(exact_expectation),
        "exact_PP2j_criterion_passes": exact_expectation < 1,
        "PP2k_spread_bound_fraction": str(spread_bound),
        "PP2k_criterion_passes": spread_bound < 1,
        "clean_state_count": len(clean_states),
        "clean_states": clean_states,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("bank", type=Path)
    parser.add_argument("--n", type=int, help="select one source size from a list")
    parser.add_argument("--t", type=int, required=True)
    parser.add_argument("--delete", type=parse_point, action="append", default=[], metavar="X,Y")
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
        result = analyze(core, m, args.t, deleted, load_bank(args.bank))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
