#!/usr/bin/env python3
"""Verify the universal arbitrary-map full-selector closure 2 x 6 -> 12."""
from __future__ import annotations

from itertools import combinations, permutations

Permutation = tuple[int, ...]
Point = tuple[int, int]
Factor = tuple[Permutation, Permutation]


def compose(first: Permutation, second: Permutation) -> Permutation:
    return tuple(first[second[index]] for index in range(len(first)))


def inverse(permutation: Permutation) -> Permutation:
    result = [0] * len(permutation)
    for index, value in enumerate(permutation):
        result[value] = index
    return tuple(result)


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def is_no_three(points: tuple[Point, ...] | list[Point]) -> bool:
    return all(determinant(*triple) != 0 for triple in combinations(points, 3))


def cycle_type(permutation: Permutation) -> tuple[int, ...]:
    seen: set[int] = set()
    lengths: list[int] = []
    for start in range(len(permutation)):
        if start in seen:
            continue
        length = 0
        current = start
        while current not in seen:
            seen.add(current)
            length += 1
            current = permutation[current]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def valid_factors() -> tuple[Factor, ...]:
    result: list[Factor] = []
    all_permutations = tuple(permutations(range(6)))
    for first in all_permutations:
        for second in all_permutations:
            if any(first[row] == second[row] for row in range(6)):
                continue
            points = [(row, first[row]) for row in range(6)]
            points.extend((row, second[row]) for row in range(6))
            if is_no_three(points):
                result.append((first, second))
    return tuple(result)


def canonical_host(
    relative: Permutation,
    target: Permutation,
    row_relative: Permutation,
    column_relative: Permutation,
    orientation: str,
) -> frozenset[Point]:
    identity = tuple(range(6))
    cells: set[Point] = set()
    for coarse_row in (0, 1):
        for coarse_column in (0, 1):
            for inner_layer in (0, 1):
                block_map = compose(
                    column_relative if coarse_column else identity,
                    compose(
                        target,
                        compose(
                            relative if inner_layer else identity,
                            row_relative if coarse_row else identity,
                        ),
                    ),
                )
                for fine_row, fine_column in enumerate(block_map):
                    x = (
                        6 * coarse_row + fine_row
                        if orientation[0] == "c"
                        else 2 * fine_row + coarse_row
                    )
                    y = (
                        6 * coarse_column + fine_column
                        if orientation[1] == "c"
                        else 2 * fine_column + coarse_column
                    )
                    cells.add((x, y))
    assert len(cells) == 48
    return frozenset(cells)


def original_host(
    factor: Factor,
    row_maps: tuple[Permutation, Permutation],
    column_maps: tuple[Permutation, Permutation],
    orientation: str,
) -> frozenset[Point]:
    cells: set[Point] = set()
    row_inverses = tuple(inverse(row_map) for row_map in row_maps)
    for coarse_row in (0, 1):
        for coarse_column in (0, 1):
            for inner_layer in (0, 1):
                block_map = compose(
                    column_maps[coarse_column],
                    compose(factor[inner_layer], row_inverses[coarse_row]),
                )
                for fine_row, fine_column in enumerate(block_map):
                    x = (
                        6 * coarse_row + fine_row
                        if orientation[0] == "c"
                        else 2 * fine_row + coarse_row
                    )
                    y = (
                        6 * coarse_column + fine_column
                        if orientation[1] == "c"
                        else 2 * fine_column + coarse_column
                    )
                    cells.add((x, y))
    assert len(cells) == 48
    return frozenset(cells)


def verify_selected(host: frozenset[Point], selected: tuple[Point, ...]) -> None:
    assert len(selected) == 24
    assert len(set(selected)) == 24
    assert set(selected).issubset(host)
    assert all(sum(x == row for x, _ in selected) == 2 for row in range(12))
    assert all(sum(y == column for _, y in selected) == 2 for column in range(12))
    assert is_no_three(selected)


def find_conjugator(relative: Permutation, target: Permutation) -> Permutation:
    for gamma in permutations(range(6)):
        if compose(gamma, compose(relative, inverse(gamma))) == target:
            return gamma
    raise AssertionError((relative, target))


TEMPLATES = {
    (6,): {
        "H": (1, 2, 3, 4, 5, 0),
        "T": (2, 1, 0, 5, 4, 3),
        "P": (5, 4, 3, 2, 1, 0),
        "Q": (5, 4, 3, 2, 1, 0),
        "orientation": "ff",
        "layers": (
            (2, 7, 0, 6, 10, 8, 3, 1, 5, 11, 4, 9),
            (4, 6, 9, 3, 0, 10, 1, 11, 8, 2, 5, 7),
        ),
    },
    (4, 2): {
        "H": (1, 4, 5, 0, 3, 2),
        "T": (4, 5, 0, 1, 2, 3),
        "P": (2, 4, 3, 5, 1, 0),
        "Q": (5, 4, 3, 2, 1, 0),
        "orientation": "cc",
        "layers": (
            (4, 6, 0, 1, 9, 8, 3, 2, 10, 11, 5, 7),
            (6, 9, 3, 4, 1, 11, 0, 10, 7, 8, 2, 5),
        ),
    },
    (3, 3): {
        "H": (1, 2, 0, 4, 5, 3),
        "T": (1, 3, 4, 2, 0, 5),
        "P": (4, 5, 3, 2, 0, 1),
        "Q": (3, 1, 5, 2, 4, 0),
        "orientation": "cf",
        "layers": (
            (2, 5, 3, 0, 7, 10, 1, 4, 11, 8, 6, 9),
            (5, 8, 2, 7, 10, 11, 0, 1, 4, 9, 3, 6),
        ),
    },
}


def main() -> None:
    factors = valid_factors()
    counts: dict[tuple[int, ...], int] = {}
    canonical: dict[tuple[int, ...], frozenset[Point]] = {}
    selected_by_type: dict[tuple[int, ...], tuple[Point, ...]] = {}

    for relative_type, data in TEMPLATES.items():
        host = canonical_host(
            data["H"], data["T"], data["P"], data["Q"], data["orientation"]
        )
        layers = data["layers"]
        selected = tuple(
            sorted(
                [(row, layers[0][row]) for row in range(12)]
                + [(row, layers[1][row]) for row in range(12)]
            )
        )
        verify_selected(host, selected)
        canonical[relative_type] = host
        selected_by_type[relative_type] = selected

    for factor in factors:
        relative = compose(inverse(factor[0]), factor[1])
        relative_type = cycle_type(relative)
        assert relative_type in TEMPLATES
        counts[relative_type] = counts.get(relative_type, 0) + 1
        data = TEMPLATES[relative_type]
        gamma = find_conjugator(relative, data["H"])
        row_maps = (gamma, compose(inverse(data["P"]), gamma))
        column_zero = compose(data["T"], compose(gamma, inverse(factor[0])))
        column_maps = (column_zero, compose(data["Q"], column_zero))
        transported = original_host(
            factor, row_maps, column_maps, data["orientation"]
        )
        assert transported == canonical[relative_type]
        verify_selected(transported, selected_by_type[relative_type])

    assert len(factors) == 116
    assert counts == {(6,): 84, (4, 2): 16, (3, 3): 16}
    print(f"ordered saturated side-six factors: {len(factors)}")
    print(f"relative-cycle counts: {counts}")
    for relative_type, data in TEMPLATES.items():
        print(
            f"type={relative_type}, orientation={data['orientation']}, "
            f"H={data['H']}, T={data['T']}, P={data['P']}, Q={data['Q']}"
        )
        print(f"  layers={data['layers']}")
    print("universal full-selector closure verified: 2 x 6 -> 12")


if __name__ == "__main__":
    main()
