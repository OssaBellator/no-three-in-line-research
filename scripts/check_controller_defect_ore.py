#!/usr/bin/env python3
"""Check the controller-defect Ore bounds of PP3lx--PP3lz.

The input JSON contains exact defect counts:

{
  "R": 12,
  "T": 4,
  "gamma": "1/2",
  "h": 1,
  "movement_defects": [[...], ...],
  "refill_defects": [[...], ...],
  "anchor_counts": [[[...], ...], ...]
}

All calculations use fractions.  The script builds the compatibility graph
certified by the union lower bound R-a-b-u >= gamma*R, computes actual degrees in
that certified graph, and compares them with the PP3ly score bounds.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    return parser.parse_args()


def as_fraction(value: Any, name: str) -> Fraction:
    try:
        return Fraction(value)
    except (ValueError, TypeError, ZeroDivisionError) as exc:
        raise ValueError(f"invalid rational {name}: {value!r}") from exc


def validate_matrix(
    value: Any, rows: int, cols: int, name: str
) -> list[list[int]]:
    if not isinstance(value, list) or len(value) != rows:
        raise ValueError(f"{name} must have {rows} rows")
    result: list[list[int]] = []
    for row_index, row in enumerate(value):
        if not isinstance(row, list) or len(row) != cols:
            raise ValueError(f"{name}[{row_index}] must have {cols} entries")
        if not all(isinstance(entry, int) and entry >= 0 for entry in row):
            raise ValueError(f"{name}[{row_index}] must contain nonnegative integers")
        result.append(row)
    return result


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    args = parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))

    R = data.get("R")
    T = data.get("T")
    if not isinstance(R, int) or R <= 0:
        raise ValueError("R must be a positive integer")
    if not isinstance(T, int) or T <= 0:
        raise ValueError("T must be a positive integer")

    gamma = as_fraction(data.get("gamma"), "gamma")
    h = as_fraction(data.get("h", 0), "h")
    if not (0 < gamma < 1):
        raise ValueError("gamma must lie strictly between zero and one")
    if h < 0:
        raise ValueError("h must be nonnegative")

    movement_raw = data.get("movement_defects")
    if not isinstance(movement_raw, list) or not movement_raw:
        raise ValueError("movement_defects must be a nonempty matrix")
    M = len(movement_raw)
    movement = validate_matrix(movement_raw, M, T, "movement_defects")
    refill = validate_matrix(data.get("refill_defects"), M, T, "refill_defects")

    anchors_raw = data.get("anchor_counts")
    if not isinstance(anchors_raw, list) or len(anchors_raw) != M:
        raise ValueError(f"anchor_counts must have {M} macro blocks")
    anchors: list[list[list[int]]] = []
    for macro_index, block in enumerate(anchors_raw):
        anchors.append(validate_matrix(block, T, T, f"anchor_counts[{macro_index}]"))

    for name, matrix in (("movement_defects", movement), ("refill_defects", refill)):
        for macro_index, row in enumerate(matrix):
            for label_index, value in enumerate(row):
                if value > R:
                    raise ValueError(
                        f"{name}[{macro_index}][{label_index}] exceeds R"
                    )

    threshold = gamma * R
    denominator_base = (1 - gamma) * R

    graphs: list[list[list[bool]]] = []
    row_degrees: list[list[int]] = []
    column_degrees: list[list[int]] = []
    row_scores: list[list[Fraction]] = []
    column_scores: list[list[Fraction]] = []

    for macro_index in range(M):
        graph: list[list[bool]] = []
        for A in range(T):
            graph.append(
                [
                    Fraction(R - movement[macro_index][A] - refill[macro_index][B]
                             - anchors[macro_index][A][B])
                    >= threshold
                    for B in range(T)
                ]
            )
        graphs.append(graph)
        row_degrees.append([sum(row) for row in graph])
        column_degrees.append(
            [sum(1 for A in range(T) if graph[A][B]) for B in range(T)]
        )

        A_total = sum(movement[macro_index])
        B_total = sum(refill[macro_index])
        U_rows = [sum(anchors[macro_index][A]) for A in range(T)]
        V_cols = [sum(anchors[macro_index][A][B] for A in range(T)) for B in range(T)]

        macro_row_scores: list[Fraction] = []
        for A in range(T):
            denominator = denominator_base - movement[macro_index][A]
            score = Fraction(T) if denominator <= 0 else Fraction(B_total + U_rows[A], 1) / denominator
            macro_row_scores.append(min(Fraction(T), score))
        row_scores.append(macro_row_scores)

        macro_column_scores: list[Fraction] = []
        for B in range(T):
            denominator = denominator_base - refill[macro_index][B]
            score = Fraction(T) if denominator <= 0 else Fraction(A_total + V_cols[B], 1) / denominator
            macro_column_scores.append(min(Fraction(T), score))
        column_scores.append(macro_column_scores)

    average_column_scores = [
        sum(column_scores[macro_index][B] for macro_index in range(M)) / M
        for B in range(T)
    ]
    average_column_degrees = [
        Fraction(sum(column_degrees[macro_index][B] for macro_index in range(M)), M)
        for B in range(T)
    ]

    incompatible: list[dict[str, Any]] = []
    score_condition = True
    actual_degree_condition = True
    for macro_index in range(M):
        for A in range(T):
            for B in range(T):
                if graphs[macro_index][A][B]:
                    continue
                score_sum = row_scores[macro_index][A] + average_column_scores[B]
                degree_sum = Fraction(row_degrees[macro_index][A]) + average_column_degrees[B]
                score_ok = score_sum <= Fraction(T) - h
                degree_ok = degree_sum >= Fraction(T) + h
                score_condition &= score_ok
                actual_degree_condition &= degree_ok
                incompatible.append(
                    {
                        "macro": macro_index,
                        "movement_label": A,
                        "refill_label": B,
                        "row_degree": row_degrees[macro_index][A],
                        "average_refill_degree": fraction_text(average_column_degrees[B]),
                        "actual_degree_sum": fraction_text(degree_sum),
                        "row_score": fraction_text(row_scores[macro_index][A]),
                        "average_column_score": fraction_text(average_column_scores[B]),
                        "score_sum": fraction_text(score_sum),
                        "score_condition": score_ok,
                        "actual_degree_condition": degree_ok,
                    }
                )

    concentration_value = float(T * math.exp(-(float(h) ** 2) / (32 * T)))
    result = {
        "M": M,
        "R": R,
        "T": T,
        "gamma": fraction_text(gamma),
        "h": fraction_text(h),
        "certified_edge_counts": [sum(sum(row) for row in graph) for graph in graphs],
        "row_degrees": row_degrees,
        "column_degrees": column_degrees,
        "row_scores": [[fraction_text(value) for value in row] for row in row_scores],
        "average_column_scores": [fraction_text(value) for value in average_column_scores],
        "average_column_degrees": [fraction_text(value) for value in average_column_degrees],
        "incompatible_triples": incompatible,
        "pp3lz_score_condition": score_condition,
        "actual_complementary_degree_condition": actual_degree_condition,
        "balanced_ownership_union_bound_value": concentration_value,
        "balanced_ownership_union_bound_below_one": concentration_value < 1,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
