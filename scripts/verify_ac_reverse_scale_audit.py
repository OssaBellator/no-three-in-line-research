#!/usr/bin/env python3
"""Exact finite checks for AC5b--AC5f."""

from __future__ import annotations

from itertools import combinations, product
from math import gcd


Point = tuple[int, int]
Line = tuple[frozenset[Point], int]


def grid_lines(side: int) -> tuple[list[Point], list[Line]]:
    points = [(x, y) for x in range(side) for y in range(side)]
    line_keys: dict[tuple[int, int, int], tuple[frozenset[Point], int]] = {}

    for left, right in combinations(points, 2):
        dx = right[0] - left[0]
        dy = right[1] - left[1]
        step_gcd = gcd(abs(dx), abs(dy))
        ux = dx // step_gcd
        uy = dy // step_gcd
        if ux < 0 or (ux == 0 and uy < 0):
            ux = -ux
            uy = -uy

        a = uy
        b = -ux
        c = a * left[0] + b * left[1]
        coeff_gcd = gcd(gcd(abs(a), abs(b)), abs(c))
        if coeff_gcd:
            a //= coeff_gcd
            b //= coeff_gcd
            c //= coeff_gcd
        if a < 0 or (a == 0 and b < 0):
            a = -a
            b = -b
            c = -c

        key = (a, b, c)
        line_points = frozenset(
            point for point in points if a * point[0] + b * point[1] == c
        )
        if len(line_points) >= 2:
            height = max(abs(a), abs(b))
            line_keys[key] = (line_points, height)

    return points, list(line_keys.values())


def all_states(points: list[Point]) -> list[frozenset[Point]]:
    states: list[frozenset[Point]] = []
    for mask in range(1 << len(points)):
        states.append(
            frozenset(
                point
                for index, point in enumerate(points)
                if (mask >> index) & 1
            )
        )
    return states


def psi(state: frozenset[Point], lines: list[Line], threshold: int) -> int:
    return sum(
        max(len(state & line) - 2, 0)
        for line, height in lines
        if height >= threshold
    )


def new_triples(
    base: frozenset[Point],
    final: frozenset[Point],
    lines: list[Line],
    threshold: int,
) -> int:
    triples: set[frozenset[Point]] = set()
    for line, height in lines:
        if height < threshold:
            continue
        for triple in combinations(sorted(final & line), 3):
            triple_set = frozenset(triple)
            if not triple_set.issubset(base):
                triples.add(triple_set)
    return len(triples)


def certified_union(
    state: frozenset[Point],
    lines: list[Line],
    threshold: int,
) -> list[Point]:
    certified: set[Point] = set()
    for line, height in lines:
        if height < threshold:
            continue
        selected = sorted(state & line)
        excess = max(len(selected) - 2, 0)
        certified.update(selected[:excess])
    return sorted(certified)


def verify_grid(side: int = 3) -> dict[str, int]:
    points, lines = grid_lines(side)
    states = all_states(points)

    totals = {
        "grid_points": len(points),
        "grid_lines": len(lines),
        "state_pairs": 0,
        "high_line_preservation_checks": 0,
        "excess_vs_triple_checks": 0,
        "certified_deletion_checks": 0,
        "drift_implications": 0,
    }

    for threshold in (1, 2):
        for base in states:
            for final in states:
                totals["state_pairs"] += 1

                created_high = new_triples(
                    base,
                    final,
                    lines,
                    2 * threshold,
                )
                if psi(base, lines, 2 * threshold) == 0 and created_high == 0:
                    assert psi(final, lines, 2 * threshold) == 0
                    totals["high_line_preservation_checks"] += 1

                difference = psi(final, lines, threshold) - psi(
                    base,
                    lines,
                    threshold,
                )
                if difference > 0:
                    assert difference <= new_triples(
                        base,
                        final,
                        lines,
                        threshold,
                    )
                totals["excess_vs_triple_checks"] += 1

            certified = certified_union(base, lines, threshold)
            for mask in range(1 << len(certified)):
                batch = frozenset(
                    certified[index]
                    for index in range(len(certified))
                    if (mask >> index) & 1
                )
                reduced = base - batch
                assert (
                    psi(base, lines, threshold)
                    - psi(reduced, lines, threshold)
                    >= len(batch)
                )
                totals["certified_deletion_checks"] += 1

                for final in states:
                    created = new_triples(
                        reduced,
                        final,
                        lines,
                        threshold,
                    )
                    if created <= len(batch) - 1:
                        assert psi(final, lines, threshold) < psi(
                            base,
                            lines,
                            threshold,
                        )
                        totals["drift_implications"] += 1

    return totals


def verify_abstract_expectations() -> int:
    checks = 0
    for batch_size in range(1, 31):
        for menu_size in range(1, 9):
            for counts in product(range(batch_size + 2), repeat=menu_size):
                average = sum(counts) / menu_size
                if average < batch_size:
                    assert min(counts) <= batch_size - 1
                checks += 1
                if checks >= 250000:
                    return checks
    return checks


def main() -> None:
    totals = verify_grid()
    totals["expectation_ledgers"] = verify_abstract_expectations()

    print("AC5b--AC5f verification passed")
    for key, value in totals.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
