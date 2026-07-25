#!/usr/bin/env python3
"""Finite checks for CMR492--CMR496."""

from __future__ import annotations

from itertools import combinations, permutations
from math import factorial


Point = tuple[int, int]


def derangement_number(size: int) -> int:
    return round(
        factorial(size)
        * sum(((-1) ** index) / factorial(index) for index in range(size + 1))
    )


def collinear(first: Point, second: Point, third: Point) -> bool:
    x1, y1 = first
    x2, y2 = second
    x3, y3 = third
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


def cells_on_line(side: int, first: Point, second: Point) -> list[Point]:
    return [
        (source, target)
        for source in range(side)
        for target in range(side)
        if collinear(first, second, (source, target))
    ]


def extend_partial_matching(
    rows: list[int],
    columns: list[int],
    partial: dict[int, int],
) -> dict[int, int]:
    used_columns = set(partial.values())
    free_rows = [row for row in rows if row not in partial]
    free_columns = [column for column in columns if column not in used_columns]
    extension = dict(partial)
    extension.update(zip(free_rows, free_columns))
    assert set(extension) == set(rows)
    assert set(extension.values()) == set(columns)
    return extension


def verify_universal_cylinders() -> None:
    expected = {2: 2, 3: 18, 4: 72, 5: 200, 6: 450}
    observed: dict[int, int] = {}

    for side in range(2, 7):
        cells = [
            (source, target)
            for source in range(side)
            for target in range(side)
        ]
        instances = 0

        for first, second in combinations(cells, 2):
            if first[0] == second[0] or first[1] == second[1]:
                continue

            used_rows = {first[0], second[0]}
            used_columns = {first[1], second[1]}
            rows = [row for row in range(side) if row not in used_rows]
            columns = [
                column for column in range(side) if column not in used_columns
            ]

            residual_line = [
                cell
                for cell in cells_on_line(side, first, second)
                if cell not in {first, second}
                and cell[0] in rows
                and cell[1] in columns
            ]

            # CMR492: the remaining line cells form a partial matching.
            assert len({cell[0] for cell in residual_line}) == len(residual_line)
            assert len({cell[1] for cell in residual_line}) == len(residual_line)

            forbidden = extend_partial_matching(
                rows,
                columns,
                {source: target for source, target in residual_line},
            )

            completions: list[set[Point]] = []
            for permutation in permutations(columns):
                matching = set(zip(rows, permutation))
                if all((row, forbidden[row]) not in matching for row in rows):
                    completions.append(matching)

            # Exact derangement cylinder size.
            assert len(completions) == derangement_number(side - 2)

            joining_line = set(cells_on_line(side, first, second))
            for completion in completions:
                full_state = {first, second} | completion
                assert full_state.intersection(joining_line) == {first, second}

            instances += 1

        observed[side] = instances

    assert observed == expected


def clean_matching(points: list[Point]) -> bool:
    return all(
        not collinear(points[first], points[second], points[third])
        for first, second, third in combinations(range(len(points)), 3)
    )


def verify_rooted_arm_application() -> None:
    for side in range(3, 7):
        for permutation in permutations(range(side)):
            base = [(source, permutation[source]) for source in range(side)]
            if not clean_matching(base):
                continue
            base_set = set(base)

            for centre in (
                (source, target)
                for source in range(side)
                for target in range(side)
                if (source, target) not in base_set
            ):
                for first, second in combinations(base, 2):
                    if not collinear(centre, first, second):
                        continue

                    # CMR494: either centre/outside pair is compatible because
                    # the rooted line is nonaxis.
                    assert centre[0] != first[0] and centre[1] != first[1]
                    assert centre[0] != second[0] and centre[1] != second[1]

                    line = set(cells_on_line(side, centre, first))
                    assert second in line


def main() -> None:
    verify_universal_cylinders()
    verify_rooted_arm_application()
    print(
        "verified universal compatible-pair line-clean cylinders: exact "
        "derangement size, full joining-line avoidance, and rooted-arm "
        "compatibility through side six"
    )


if __name__ == "__main__":
    main()
