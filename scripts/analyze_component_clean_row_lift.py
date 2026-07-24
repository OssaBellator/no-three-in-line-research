#!/usr/bin/env python3
"""Analyze PP3z/PP3aa after conditioning both row-lift components clean."""
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


def parse_rows(text: str, m: int) -> tuple[int, ...]:
    rows = tuple(sorted({int(part) for part in text.split(",") if part.strip()}))
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


def prob(count: int, total: int) -> Fraction:
    return Fraction(count, total)


def analyze(m: int, core: tuple[Point, ...], rows: tuple[int, ...], max_pairs: int) -> dict[str, Any]:
    t = len(rows)
    target = m + t
    new_values = tuple(range(m + 1, target + 1))
    row_set = set(rows)
    deleted = tuple(point for point in core if point[1] in row_set)
    retained = tuple(point for point in core if point[1] not in row_set)
    red, blue = balanced_coloring(deleted, t)

    all_m = movement_states(red, blue, new_values)
    all_f = refill_states(rows, new_values)
    movements = [state for state in all_m if no_three(state)]
    refills = [state for state in all_f if no_three(state)]
    if not movements or not refills:
        return {
            "source_n": m,
            "target_n": target,
            "t": t,
            "old_rows": list(rows),
            "movement_state_count": len(all_m),
            "refill_state_count": len(all_f),
            "clean_movement_state_count": len(movements),
            "clean_refill_state_count": len(refills),
            "component_clean_bank_nonempty": False,
        }

    product_count = len(movements) * len(refills)
    if product_count > max_pairs:
        raise ValueError(f"component-clean product has {product_count} pairs, above --max-pairs")

    ms = tuple(sorted(set().union(*movements)))
    fs = tuple(sorted(set().union(*refills)))
    retained_pairs = tuple(combinations(retained, 2))
    blocked_m = {z for z in ms if any(determinant(a, b, z) == 0 for a, b in retained_pairs)}
    blocked_f = {z for z in fs if any(determinant(a, b, z) == 0 for a, b in retained_pairs)}
    p_mm = {p for p in combinations(ms, 2) if any(determinant(*p, a) == 0 for a in retained)}
    p_ff = {p for p in combinations(fs, 2) if any(determinant(*p, a) == 0 for a in retained)}
    p_mf = {(x, y) for x in ms for y in fs if any(determinant(x, y, a) == 0 for a in retained)}
    t_mmf = {((x1, x2), y) for x1, x2 in combinations(ms, 2) for y in fs if determinant(x1, x2, y) == 0}
    t_mff = {(x, (y1, y2)) for x in ms for y1, y2 in combinations(fs, 2) if determinant(x, y1, y2) == 0}

    mc, mp = frequencies(movements)
    fc, fp = frequencies(refills)
    nm, nf = len(movements), len(refills)

    exact = sum((prob(mc[z], nm) for z in blocked_m), Fraction())
    exact += sum((prob(fc[z], nf) for z in blocked_f), Fraction())
    exact += sum((prob(mp[p], nm) for p in p_mm), Fraction())
    exact += sum((prob(fp[p], nf) for p in p_ff), Fraction())
    exact += sum((prob(mc[x], nm) * prob(fc[y], nf) for x, y in p_mf), Fraction())
    exact += sum((prob(mp[p], nm) * prob(fc[y], nf) for p, y in t_mmf), Fraction())
    exact += sum((prob(mc[x], nm) * prob(fp[p], nf) for x, p in t_mff), Fraction())

    max_mc = prob(max(mc.values()), nm)
    max_fc = prob(max(fc.values()), nf)
    max_mp = prob(max(mp.values()), nm)
    max_fp = prob(max(fp.values()), nf)
    alpha_m, alpha_f = t * max_mc, t * max_fc
    beta_m, beta_f = t * (t - 1) * max_mp, t * (t - 1) * max_fp
    bound = Fraction(alpha_m * len(blocked_m) + alpha_f * len(blocked_f), t)
    bound += Fraction(beta_m * len(p_mm) + beta_f * len(p_ff), t * (t - 1))
    bound += Fraction(alpha_m * alpha_f * len(p_mf), t * t)
    bound += Fraction(beta_m * alpha_f * len(t_mmf) + alpha_m * beta_f * len(t_mff), t * t * (t - 1))

    histogram: Counter[int] = Counter()
    clean: list[dict[str, Any]] = []
    for movement in movements:
        sm = set(movement)
        for refill in refills:
            sf = set(refill)
            defects = sum(z in blocked_m for z in movement) + sum(z in blocked_f for z in refill)
            defects += sum(a in sm and b in sm for a, b in p_mm)
            defects += sum(a in sf and b in sf for a, b in p_ff)
            defects += sum(a in sm and b in sf for a, b in p_mf)
            defects += sum(p[0] in sm and p[1] in sm and y in sf for p, y in t_mmf)
            defects += sum(x in sm and p[0] in sf and p[1] in sf for x, p in t_mff)
            histogram[defects] += 1
            if defects == 0:
                final = tuple(sorted(retained + movement + refill))
                if not saturated(final, target) or not no_three(final):
                    raise AssertionError("zero-certificate pair is invalid")
                clean.append({"points": [list(point) for point in final]})

    return {
        "source_n": m,
        "target_n": target,
        "t": t,
        "old_rows": list(rows),
        "movement_state_count": len(all_m),
        "refill_state_count": len(all_f),
        "clean_movement_state_count": nm,
        "clean_refill_state_count": nf,
        "component_clean_pair_count": product_count,
        "component_clean_bank_nonempty": True,
        "blocked_movement_cells": len(blocked_m),
        "blocked_refill_cells": len(blocked_f),
        "anchored_MM_pairs": len(p_mm),
        "anchored_FF_pairs": len(p_ff),
        "anchored_MF_pairs": len(p_mf),
        "cross_MMF_triples": len(t_mmf),
        "cross_MFF_triples": len(t_mff),
        "maximum_movement_cell_probability_fraction": str(max_mc),
        "maximum_refill_cell_probability_fraction": str(max_fc),
        "maximum_movement_pair_probability_fraction": str(max_mp),
        "maximum_refill_pair_probability_fraction": str(max_fp),
        "exact_PP3z_expectation_fraction": str(exact),
        "exact_PP3z_criterion_passes": exact < 1,
        "PP3aa_spread_bound_fraction": str(bound),
        "PP3aa_criterion_passes": bound < 1,
        "minimum_certificate_count": min(histogram),
        "maximum_certificate_count": max(histogram),
        "clean_pair_count": len(clean),
        "certificate_histogram": {str(k): histogram[k] for k in sorted(histogram)},
        "clean_pairs": clean,
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
        result = analyze(m, core, parse_rows(args.rows, m), args.max_pairs)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
