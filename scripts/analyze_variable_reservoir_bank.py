#!/usr/bin/env python3
"""Verify a finite state-dependent-deletion patch bank and evaluate PP2l--PP2n.

Bank JSON is a nonempty list or {"states": [...]}. Each state is an object with
optional "label", a "deleted" point list, and an "inserted" point list. The
source certificate is fixed, but deletion sets may vary between states.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any, Iterable

Point = tuple[int, int]
OldPair = tuple[Point, Point]
CandidatePair = tuple[Point, Point]


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


def parse_points(raw: Any, label: str) -> tuple[Point, ...]:
    if not isinstance(raw, list):
        raise ValueError(f"{label}: expected a point list")
    points = tuple(
        sorted(
            json_point(point, f"{label} point {index}")
            for index, point in enumerate(raw)
        )
    )
    if len(points) != len(set(points)):
        raise ValueError(f"{label}: duplicate point")
    return points


def load_case(path: Path, selected_n: int | None) -> tuple[int, tuple[Point, ...]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    raw_cases = payload if isinstance(payload, list) else [payload]
    cases: list[tuple[int, tuple[Point, ...]]] = []
    for ordinal, raw in enumerate(raw_cases, 1):
        if not isinstance(raw, dict):
            raise ValueError(f"case {ordinal}: expected an object")
        n = raw.get("n")
        if isinstance(n, bool) or not isinstance(n, int) or n < 2:
            raise ValueError(f"case {ordinal}: invalid n")
        points = parse_points(raw.get("points"), f"case {ordinal}")
        if not saturated(points, n) or not no_three(points):
            raise ValueError(f"case {ordinal}: invalid source certificate")
        if selected_n is None or n == selected_n:
            cases.append((n, points))
    if len(cases) != 1:
        raise ValueError("select exactly one source certificate with --n")
    return cases[0]


def load_bank(
    path: Path,
) -> list[tuple[str, tuple[Point, ...], tuple[Point, ...]]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    raw_states = payload.get("states") if isinstance(payload, dict) else payload
    if not isinstance(raw_states, list) or not raw_states:
        raise ValueError("bank must contain a nonempty state list")
    out = []
    for ordinal, raw in enumerate(raw_states, 1):
        if not isinstance(raw, dict):
            raise ValueError(f"state {ordinal}: expected an object")
        label = str(raw.get("label", f"state-{ordinal}"))
        deleted = parse_points(raw.get("deleted"), f"{label} deleted")
        inserted_raw = raw.get("inserted", raw.get("points"))
        inserted = parse_points(inserted_raw, f"{label} inserted")
        out.append((label, deleted, inserted))
    return out


def analyze(
    m: int,
    core: tuple[Point, ...],
    t: int,
    bank: list[tuple[str, tuple[Point, ...], tuple[Point, ...]]],
) -> dict[str, Any]:
    target_n = m + t
    core_set = set(core)
    checked = []
    support: set[Point] = set()
    cell_frequency: Counter[Point] = Counter()
    pair_frequency: Counter[CandidatePair] = Counter()
    joint_one: Counter[tuple[OldPair, Point]] = Counter()
    joint_two: Counter[tuple[Point, CandidatePair]] = Counter()
    histogram: Counter[int] = Counter()
    clean_states = []

    for label, deleted, inserted in bank:
        deleted_set = set(deleted)
        if not deleted_set.issubset(core_set):
            raise ValueError(f"{label}: deleted points are not all in the source")
        expected_inserted = len(deleted) + 2 * t
        if len(inserted) != expected_inserted:
            raise ValueError(
                f"{label}: expected {expected_inserted} inserted points, "
                f"found {len(inserted)}"
            )
        if any(
            not (1 <= x <= target_n and 1 <= y <= target_n)
            for x, y in inserted
        ):
            raise ValueError(f"{label}: inserted point outside [1,{target_n}]^2")
        retained = tuple(point for point in core if point not in deleted_set)
        retained_set = set(retained)
        overlap = retained_set.intersection(inserted)
        if overlap:
            raise ValueError(
                f"{label}: inserted points overlap retained points: {sorted(overlap)}"
            )
        if not no_three(inserted):
            raise ValueError(f"{label}: inserted set has an internal triple")
        final = tuple(sorted(retained + inserted))
        if not saturated(final, target_n):
            raise ValueError(f"{label}: final state is not saturated")

        old_pairs = tuple(combinations(retained, 2))
        inserted_pairs = tuple(combinations(inserted, 2))
        blocked_events = [
            (tuple(sorted((first, second))), point)
            for first, second in old_pairs
            for point in inserted
            if determinant(first, second, point) == 0
        ]
        anchored_events = [
            (anchor, tuple(sorted((first, second))))
            for anchor in retained
            for first, second in inserted_pairs
            if determinant(anchor, first, second) == 0
        ]
        defect_count = len(blocked_events) + len(anchored_events)
        histogram[defect_count] += 1
        joint_one.update(blocked_events)
        joint_two.update(anchored_events)
        cell_frequency.update(inserted)
        pair_frequency.update(inserted_pairs)
        support.update(inserted)
        checked.append((label, deleted, inserted, defect_count))
        if defect_count == 0:
            if not no_three(final):
                raise AssertionError("zero-certificate state is not no-three")
            clean_states.append(
                {
                    "label": label,
                    "deleted": [list(point) for point in deleted],
                    "inserted": [list(point) for point in inserted],
                    "points": [list(point) for point in final],
                }
            )

    state_count = len(checked)
    exact_expectation = Fraction(
        sum(count * multiplicity for count, multiplicity in histogram.items()),
        state_count,
    )
    support_tuple = tuple(sorted(support))
    c1 = {
        (tuple(sorted((first, second))), point)
        for first, second in combinations(core, 2)
        for point in support_tuple
        if point not in (first, second)
        and determinant(first, second, point) == 0
    }
    c2 = {
        (anchor, tuple(sorted((first, second))))
        for anchor in core
        for first, second in combinations(support_tuple, 2)
        if anchor not in (first, second)
        and determinant(anchor, first, second) == 0
    }
    max_joint_one = Fraction(max(joint_one.values(), default=0), state_count)
    max_joint_two = Fraction(max(joint_two.values(), default=0), state_count)
    uniform_joint_bound = max_joint_one * len(c1) + max_joint_two * len(c2)

    deletion_blind_bound = sum(
        (Fraction(cell_frequency[point], state_count) for _, point in c1),
        Fraction(),
    )
    deletion_blind_bound += sum(
        (Fraction(pair_frequency[pair], state_count) for _, pair in c2),
        Fraction(),
    )

    return {
        "source_n": m,
        "target_n": target_n,
        "t": t,
        "state_count": state_count,
        "inserted_support_cells": len(support_tuple),
        "geometric_C1_certificates": len(c1),
        "geometric_C2_certificates": len(c2),
        "observed_joint_C1_events": len(joint_one),
        "observed_joint_C2_events": len(joint_two),
        "exact_PP2l_expectation_fraction": str(exact_expectation),
        "exact_PP2l_criterion_passes": exact_expectation < 1,
        "maximum_joint_C1_probability_fraction": str(max_joint_one),
        "maximum_joint_C2_probability_fraction": str(max_joint_two),
        "PP2m_uniform_joint_bound_fraction": str(uniform_joint_bound),
        "PP2m_criterion_passes": uniform_joint_bound < 1,
        "PP2n_deletion_blind_bound_fraction": str(deletion_blind_bound),
        "PP2n_criterion_passes": deletion_blind_bound < 1,
        "minimum_certificate_count": min(histogram),
        "maximum_certificate_count": max(histogram),
        "certificate_histogram": {
            str(count): histogram[count] for count in sorted(histogram)
        },
        "clean_state_count": len(clean_states),
        "clean_states": clean_states,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("bank", type=Path)
    parser.add_argument("--n", type=int)
    parser.add_argument("--t", type=int, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.t < 1:
        raise SystemExit("t must be positive")
    try:
        m, core = load_case(args.certificate, args.n)
        result = analyze(m, core, args.t, load_bank(args.bank))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
