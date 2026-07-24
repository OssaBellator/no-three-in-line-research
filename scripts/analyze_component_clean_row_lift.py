#!/usr/bin/env python3
"""Analyze PP3z/PP3aa after conditioning both row-lift components clean.

The movement and refill banks are enumerated separately, restricted to states
with no internal collinear triple, and then paired. Exact enumeration is
intended for at most five reservoir rows.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any

from analyze_row_lift_bank import (
    balanced_coloring,
    determinant,
    load_case,
    movement_states,
    no_three,
    refill_states,
    saturated,
)

Point = tuple[int, int]
Pair = tuple[Point, Point]
Triple = tuple[Point, Point, Point]


def parse_rows(text: str, m: int) -> tuple[int, ...]:
    try:
        rows = tuple(sorted({int(part) for part in text.split(",") if part.strip()}))
    except ValueError as exc:
        raise ValueError("rows must be comma-separated integers") from exc
    if not 2 <= len(rows) <= 5:
        raise ValueError("choose between two and five reservoir rows")
    if any(row < 1 or row > m for row in rows):
        raise ValueError(f"rows must lie in [1,{m}]")
    return rows


def frequencies(states: list[tuple[Point, ...]]) -> tuple[Counter[Point], Counter[Pair]]:
    cells: Counter[Point] = Counter()
    pairs: Counter[Pair] = Counter()
    for state in states:
        cells.update(state)
        pairs.update(combinations(state, 2))
    return cells, pairs


def probability(count: int, state_count: int) -> Fraction:
    return Fraction(count, state_count)


def analyze(
    m: int,
    core: tuple[Point, ...],
    old_rows: tuple[int, ...],
    max_pairs: int,
) -> dict[str, Any]:
    t = len(old_rows)
    target_n = m + t
    new_values = tuple(range(m + 1, target_n + 1))
    old_row_set = set(old_rows)
    deleted = tuple(point for point in core if point[1] in old_row_set)
    retained = tuple(point for point in core if point[1] not in old_row_set)
    red, blue = balanced_coloring(deleted, t)

    all_movements = movement_states(red, blue, new_values)
    all_refills = refill_states(old_rows, new_values)
    movements = [state for state in all_movements if no_three(state)]
    refills = [state for state in all_refills if no_three(state)]
    if not movements or not refills:
        return {
            "source_n": m,
            "target_n": target_n,
            "t": t,
            "old_rows": list(old_rows),
            "movement_state_count": len(all_movements),
            "refill_state_count": len(all_refills),
            "clean_movement_state_count": len(movements),
            "clean_refill_state_count": len(refills),
            "component_clean_bank_nonempty": False,
        }

    pair_count = len(movements) * len(refills)
    if pair_count > max_pairs:
        raise ValueError(
            f"component-clean product has {pair_count} pairs, above --max-pairs={max_pairs}"
        )

    movement_support = tuple(sorted(set().union(*movements)))
    refill_support = tuple(sorted(set().union(*refills)))
    retained_pairs = tuple(combinations(retained, 2))

    blocked_m = {
        point
        for point in movement_support
        if any(determinant(first, second, point) == 0 for first, second in retained_pairs)
    }
    blocked_f = {
        point
        for point in refill_support
        if any(determinant(first, second, point) == 0 for first, second in retained_pairs)
    }
    anchored_mm = {
        pair
        for pair in combinations(movement_support, 2)
        if any(determinant(pair[0], pair[1], anchor) == 0 for anchor in retained)
    }
    anchored_ff = {
        pair
        for pair in combinations(refill_support, 2)
        if any(determinant(pair[0], pair[1], anchor) == 0 for anchor in retained)
    }
    anchored_mf = {
        (first, second)
        for first in movement_support
        for second in refill_support
        if any(determinant(first, second, anchor) == 0 for anchor in retained)
    }
    triples_mmf = {
        tuple(sorted((first, second, third)))
        for first, second in combinations(movement_support, 2)
        for third in refill_support
        if determinant(first, second, third) == 0
    }
    triples_mff = {
        tuple(sorted((first, second, third)))
        for first in movement_support
        for second, third in combinations(refill_support, 2)
        if determinant(first, second, third) == 0
    }

    m_cells, m_pairs = frequencies(movements)
    f_cells, f_pairs = frequencies(refills)
    m_count = len(movements)
    f_count = len(refills)

    exact_expectation = Fraction()
    exact_expectation += sum(
        (probability(m_cells[point], m_count) for point in blocked_m), Fraction()
    )
    exact_expectation += sum(
        (probability(f_cells[point], f_count) for point in blocked_f), Fraction()
    )
    exact_expectation += sum(
        (probability(m_pairs[pair], m_count) for pair in anchored_mm), Fraction()
    )
    exact_expectation += sum(
        (probability(f_pairs[pair], f_count) for pair in anchored_ff), Fraction()
    )
    exact_expectation += sum(
        (
            probability(m_cells[first], m_count)
            * probability(f_cells[second], f_count)
            for first, second in anchored_mf
        ),
        Fraction(),
    )
    exact_expectation += sum(
        (
            probability(m_pairs[tuple(sorted((first, second)))], m_count)
            * probability(f_cells[third], f_count)
            for first, second, third in triples_mmf
        ),
        Fraction(),
    )
    exact_expectation += sum(
        (
            probability(m_cells[first], m_count)
            * probability(f_pairs[tuple(sorted((second, third)))], f_count)
            for first, second, third in triples_mff
        ),
        Fraction(),
    )

    max_m_cell = probability(max(m_cells.values(), default=0), m_count)
    max_f_cell = probability(max(f_cells.values(), default=0), f_count)
    max_m_pair = probability(max(m_pairs.values(), default=0), m_count)
    max_f_pair = probability(max(f_pairs.values(), default=0), f_count)
    alpha_m = t * max_m_cell
    alpha_f = t * max_f_cell
    beta_m = t * (t - 1) * max_m_pair
    beta_f = t * (t - 1) * max_f_pair

    spread_bound = (
        Fraction(alpha_m * len(blocked_m), t)
        + Fraction(alpha_f * len(blocked_f), t)
        + Fraction(beta_m * len(anchored_mm), t * (t - 1))
        + Fraction(beta_f * len(anchored_ff), t * (t - 1))
        + Fraction(alpha_m * alpha_f * len(anchored_mf), t * t)
        + Fraction(
            beta_m * alpha_f * len(triples_mmf)
            + alpha_m * beta_f * len(triples_mff),
            t * t * (t - 1),
        )
    )

    histogram: Counter[int] = Counter()
    clean_pairs: list[dict[str, Any]] = []
    for movement in movements:
        movement_set = set(movement)
        for refill in refills:
            refill_set = set(refill)
            defects = sum(point in blocked_m for point in movement)
            defects += sum(point in blocked_f for point in refill)
            defects += sum(first in movement_set and second in movement_set for first, second in anchored_mm)
            defects += sum(first in refill_set and second in refill_set for first, second in anchored_ff)
            defects += sum(first in movement_set and second in refill_set for first, second in anchored_mf)
            defects += sum(
                first in movement_set and second in movement_set and third in refill_set
                for first, second, third in triples_mmf
            )
            defects += sum(
                first in movement_set and second in refill_set and third in refill_set
                for first, second, third in triples_mff
            )
            histogram[defects] += 1
            if defects == 0:
                final = tuple(sorted(retained + movement + refill))
                if not saturated(final, target_n) or not no_three(final):
                    raise AssertionError("zero-certificate component pair is invalid")
                clean_pairs.append(
                    {
                        "movement": [list(point) for point in movement],
                        "refill": [list(point) for point in refill],
                        "points": [list(point) for point in final],
                    }
                )

    return {
        "source_n": m,
        "target_n": target_n,
        "t": t,
        "old_rows": list(old_rows),
        "movement_state_count": len(all_movements),
        "refill_state_count": len(all_refills),
        "clean_movement_state_count": m_count,
        "clean_refill_state_count": f_count,
        "component_clean_pair_count": pair_count,
        "component_clean_bank_nonempty": True,
        "movement_support_cells": len(movement_support),
        "refill_support_cells": len(refill_support),
        "blocked_movement_cells": len(blocked_m),
        "blocked_refill_cells": len(blocked_f),
        "anchored_MM_pairs": len(anchored_mm),
        "anchored_FF_pairs": len(anchored_ff),
        "anchored_MF_pairs": len(anchored_mf),
        "cross_MMF_triples": len(triples_mmf),
        "cross_MFF_triples": len(triples_mff),
        "maximum_movement_cell_probability_fraction": f"{max_m_cell.numerator}/{max_m_cell.denominator}",
        "maximum_refill_cell_probability_fraction": f"{max_f_cell.numerator}/{max_f_cell.denominator}",
        "maximum_movement_pair_probability_fraction": f"{max_m_pair.numerator}/{max_m_pair.denominator}",
        "maximum_refill_pair_probability_fraction": f"{max_f_pair.numerator}/{max_f_pair.denominator}",
        "exact_PP3z_expectation_fraction": f"{exact_expectation.numerator}/{exact_expectation.denominator}",
        "exact_PP3z_criterion_passes": exact_expectation < 1,
        "PP3aa_spread_bound_fraction": f"{spread_bound.numerator}/{spread_bound.denominator}",
        "PP3aa_criterion_passes": spread_bound < 1,
        "minimum_certificate_count": min(histogram),
        "maximum_certificate_count": max(histogram),
        "clean_pair_count": len(clean_pairs),
        "certificate_histogram": {
            str(key): histogram[key] for key in sorted(histogram)
        },
        "clean_pairs": clean_pairs,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int)
    parser.add_argument("--rows", required=True)
    parser.add_argument("--max-pairs", type=int, default=100_000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        m, core = load_case(args.certificate, args.n)
        rows = parse_rows(args.rows, m)
        result = analyze(m, core, rows, args.max_pairs)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
