#!/usr/bin/env python3
"""Enumerate a small row-lift reservoir bank and its exact certificate spread.

Choose t old reservoir rows, delete their 2t points, move those points into the
t new rows while preserving old columns, and refill the old rows from the t new
columns. The construction is the finite bank from Theorem PP3i.

Enumeration is intended for t<=4. All geometry uses exact integer determinants.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
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


def balanced_coloring(deleted: tuple[Point, ...], t: int) -> tuple[tuple[Point, ...], tuple[Point, ...]]:
    by_column: dict[int, list[Point]] = defaultdict(list)
    for point in deleted:
        by_column[point[0]].append(point)

    red: list[Point] = []
    blue: list[Point] = []
    singletons: list[Point] = []
    for column in sorted(by_column):
        points = sorted(by_column[column])
        if len(points) == 2:
            red.append(points[0])
            blue.append(points[1])
        elif len(points) == 1:
            singletons.append(points[0])
        else:
            raise AssertionError("a saturated column contains at most two deleted points")

    need_red = t - len(red)
    red.extend(singletons[:need_red])
    blue.extend(singletons[need_red:])
    if len(red) != t or len(blue) != t:
        raise AssertionError("balanced coloring failed")
    if len({point[0] for point in red}) != t or len({point[0] for point in blue}) != t:
        raise AssertionError("a color repeats an old column")
    return tuple(red), tuple(blue)


def movement_states(
    red: tuple[Point, ...],
    blue: tuple[Point, ...],
    new_rows: tuple[int, ...],
) -> list[tuple[Point, ...]]:
    out: list[tuple[Point, ...]] = []
    for red_rows in permutations(new_rows):
        red_assignment = {red[index]: red_rows[index] for index in range(len(red))}
        for blue_rows in permutations(new_rows):
            collision = False
            for index, blue_point in enumerate(blue):
                for red_point in red:
                    if (
                        red_point[0] == blue_point[0]
                        and red_assignment[red_point] == blue_rows[index]
                    ):
                        collision = True
                        break
                if collision:
                    break
            if collision:
                continue
            points = tuple(
                sorted(
                    [(point[0], red_assignment[point]) for point in red]
                    + [(point[0], blue_rows[index]) for index, point in enumerate(blue)]
                )
            )
            if len(points) != len(set(points)):
                raise AssertionError("movement state has a duplicate cell")
            out.append(points)
    return out


def refill_states(
    old_rows: tuple[int, ...],
    new_columns: tuple[int, ...],
) -> list[tuple[Point, ...]]:
    out: list[tuple[Point, ...]] = []
    for first in permutations(new_columns):
        for second in permutations(new_columns):
            if any(first[index] == second[index] for index in range(len(old_rows))):
                continue
            points = tuple(
                sorted(
                    [(first[index], old_rows[index]) for index in range(len(old_rows))]
                    + [(second[index], old_rows[index]) for index in range(len(old_rows))]
                )
            )
            out.append(points)
    return out


def analyze(
    m: int,
    core: tuple[Point, ...],
    old_rows: tuple[int, ...],
    max_states: int,
) -> dict[str, Any]:
    t = len(old_rows)
    target_n = m + t
    new_rows = tuple(range(m + 1, target_n + 1))
    new_columns = new_rows

    old_row_set = set(old_rows)
    deleted = tuple(point for point in core if point[1] in old_row_set)
    if len(deleted) != 2 * t:
        raise ValueError("the selected rows do not contain exactly two points each")
    deleted_set = set(deleted)
    retained = tuple(point for point in core if point not in deleted_set)
    red, blue = balanced_coloring(deleted, t)

    movements = movement_states(red, blue, new_rows)
    refills = refill_states(old_rows, new_columns)
    total_states = len(movements) * len(refills)
    if total_states > max_states:
        raise ValueError(
            f"bank has {total_states} states, above --max-states={max_states}"
        )

    support = set().union(*movements, *refills)
    retained_pairs = tuple(combinations(retained, 2))
    blocked_cells = {
        point
        for point in support
        if any(determinant(first, second, point) == 0 for first, second in retained_pairs)
    }
    anchored_pairs = {
        pair
        for pair in combinations(sorted(support), 2)
        if any(determinant(pair[0], pair[1], anchor) == 0 for anchor in retained)
    }
    internal_triples = {
        triple
        for triple in combinations(sorted(support), 3)
        if determinant(*triple) == 0
    }

    cell_frequency: Counter[Point] = Counter()
    pair_frequency: Counter[tuple[Point, Point]] = Counter()
    triple_frequency: Counter[tuple[Point, Point, Point]] = Counter()
    defect_histogram: Counter[int] = Counter()
    clean_states: list[dict[str, Any]] = []

    for movement in movements:
        for refill in refills:
            inserted = tuple(sorted(movement + refill))
            if len(inserted) != len(set(inserted)):
                raise AssertionError("components overlap")
            final = tuple(sorted(retained + inserted))
            if not saturated(final, target_n):
                raise AssertionError("bank state does not fill the deficits")

            inserted_set = set(inserted)
            defect_count = sum(point in blocked_cells for point in inserted)
            defect_count += sum(
                first in inserted_set and second in inserted_set
                for first, second in anchored_pairs
            )
            defect_count += sum(
                first in inserted_set and second in inserted_set and third in inserted_set
                for first, second, third in internal_triples
            )
            defect_histogram[defect_count] += 1
            if defect_count == 0:
                if not no_three(final):
                    raise AssertionError("zero-certificate state is not no-three")
                clean_states.append(
                    {
                        "inserted": [list(point) for point in inserted],
                        "points": [list(point) for point in final],
                    }
                )

            cell_frequency.update(inserted)
            pair_frequency.update(combinations(inserted, 2))
            triple_frequency.update(combinations(inserted, 3))

    state_count = total_states
    total_defects = sum(count * multiplicity for count, multiplicity in defect_histogram.items())
    expectation = Fraction(total_defects, state_count)
    max_cell = Fraction(max(cell_frequency.values(), default=0), state_count)
    max_pair = Fraction(max(pair_frequency.values(), default=0), state_count)
    max_triple = Fraction(max(triple_frequency.values(), default=0), state_count)

    theorem_bound = (
        Fraction(6 * len(blocked_cells), t)
        + Fraction(36 * len(anchored_pairs), t * (t - 1))
        + (
            Fraction(72 * len(internal_triples), t * (t - 1) * (t - 2))
            if t >= 3
            else Fraction(0, 1)
        )
    )

    return {
        "source_n": m,
        "target_n": target_n,
        "t": t,
        "old_rows": list(old_rows),
        "deleted": [list(point) for point in deleted],
        "red_points": [list(point) for point in red],
        "blue_points": [list(point) for point in blue],
        "movement_state_count": len(movements),
        "refill_state_count": len(refills),
        "state_count": state_count,
        "support_cells": len(support),
        "blocked_support_cells": len(blocked_cells),
        "anchored_support_pairs": len(anchored_pairs),
        "internal_support_triples": len(internal_triples),
        "maximum_cell_probability_fraction": f"{max_cell.numerator}/{max_cell.denominator}",
        "maximum_pair_probability_fraction": f"{max_pair.numerator}/{max_pair.denominator}",
        "maximum_triple_probability_fraction": (
            f"{max_triple.numerator}/{max_triple.denominator}"
        ),
        "exact_expected_certificate_count_fraction": (
            f"{expectation.numerator}/{expectation.denominator}"
        ),
        "minimum_certificate_count": min(defect_histogram),
        "maximum_certificate_count": max(defect_histogram),
        "clean_state_count": len(clean_states),
        "defect_histogram": {
            str(count): defect_histogram[count] for count in sorted(defect_histogram)
        },
        "PP3j_bound_fraction": f"{theorem_bound.numerator}/{theorem_bound.denominator}",
        "PP3j_criterion_passes": theorem_bound < 1,
        "clean_states": clean_states,
    }


def parse_rows(text: str, m: int) -> tuple[int, ...]:
    try:
        rows = tuple(sorted({int(part) for part in text.split(",") if part.strip()}))
    except ValueError as exc:
        raise ValueError("rows must be comma-separated integers") from exc
    if len(rows) < 2:
        raise ValueError("choose at least two reservoir rows")
    if any(row < 1 or row > m for row in rows):
        raise ValueError(f"rows must lie in [1,{m}]")
    if len(rows) > 4:
        raise ValueError("exact enumeration is limited to at most four rows")
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int)
    parser.add_argument("--rows", required=True, help="comma-separated old row indices")
    parser.add_argument("--max-states", type=int, default=100_000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        m, core = load_case(args.certificate, args.n)
        rows = parse_rows(args.rows, m)
        result = analyze(m, core, rows, args.max_states)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
