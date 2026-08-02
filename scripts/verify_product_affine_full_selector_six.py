#!/usr/bin/env python3
"""Compile the affine census and verify the universal 6-cycle transport."""
from __future__ import annotations

import re
import subprocess
import tempfile
from itertools import combinations, permutations, product
from pathlib import Path

from verify_product_one_outer_layer_six import (
    compose,
    determinant,
    inverse,
    relative_type,
    valid_factor_pairs,
)

Permutation = tuple[int, ...]
Point = tuple[int, int]

ORIENTATIONS = ("cc", "cf", "fc", "ff")
TYPE_NAMES = ("6", "4+2", "3+3")
EXPECTED = {
    ("6", "cc"): (0, 1_332_608, 3_512),
    ("6", "cf"): (0, 1_695_557, 5_948),
    ("6", "fc"): (0, 1_724_164, 9_799),
    ("6", "ff"): (1, 2_298_951, 11_875),
    ("4+2", "cc"): (0, 1_585_278, 3_389),
    ("4+2", "cf"): (0, 1_826_561, 3_498),
    ("4+2", "fc"): (0, 1_837_677, 9_255),
    ("4+2", "ff"): (0, 2_367_978, 9_475),
    ("3+3", "cc"): (0, 1_590_536, 3_420),
    ("3+3", "cf"): (0, 1_757_107, 4_270),
    ("3+3", "fc"): (0, 2_012_551, 6_275),
    ("3+3", "ff"): (0, 2_481_218, 10_882),
}
LINE_PATTERN = re.compile(
    r"type=(6|4\+2|3\+3) orientation=(cc|cf|fc|ff) "
    r"feasible_hosts=(\d+) total_nodes=(\d+) maximum_nodes=(\d+)"
)

TARGET: Permutation = (2, 1, 0, 5, 4, 3)
ROW_RELATIVE: Permutation = (5, 4, 3, 2, 1, 0)
COLUMN_RELATIVE: Permutation = (5, 4, 3, 2, 1, 0)
INNER_RELATIVE: Permutation = (1, 2, 3, 4, 5, 0)
SELECTED: tuple[Point, ...] = (
    (0, 2), (0, 4), (1, 6), (1, 7),
    (2, 0), (2, 9), (3, 3), (3, 6),
    (4, 0), (4, 10), (5, 8), (5, 10),
    (6, 1), (6, 3), (7, 1), (7, 11),
    (8, 5), (8, 8), (9, 2), (9, 11),
    (10, 4), (10, 5), (11, 7), (11, 9),
)
LAYERS = (
    (2, 7, 0, 6, 10, 8, 3, 1, 5, 11, 4, 9),
    (4, 6, 9, 3, 0, 10, 1, 11, 8, 2, 5, 7),
)


def identity(n: int) -> Permutation:
    return tuple(range(n))


def is_no_three(points: tuple[Point, ...]) -> bool:
    return all(determinant(*triple) != 0 for triple in combinations(points, 3))


def build_normal_host(
    target: Permutation,
    row_relative: Permutation,
    column_relative: Permutation,
    inner_relative: Permutation,
    orientation: str,
) -> tuple[Point, ...]:
    n = len(target)
    cells: set[Point] = set()
    unit = identity(n)
    for coarse_row, coarse_column, inner_layer in product((0, 1), repeat=3):
        block_map = compose(
            column_relative if coarse_column else unit,
            compose(
                target,
                compose(
                    inner_relative if inner_layer else unit,
                    row_relative if coarse_row else unit,
                ),
            ),
        )
        for fine_row, fine_column in enumerate(block_map):
            x = 2 * fine_row + coarse_row
            y = 2 * fine_column + coarse_column
            cells.add((x, y))
    assert len(cells) == 48
    return tuple(sorted(cells))


def build_factor_host(
    factor: tuple[Permutation, Permutation],
    row_maps: tuple[Permutation, Permutation],
    column_maps: tuple[Permutation, Permutation],
) -> tuple[Point, ...]:
    cells: set[Point] = set()
    for coarse_row, coarse_column, inner_layer in product((0, 1), repeat=3):
        block_map = compose(
            column_maps[coarse_column],
            compose(factor[inner_layer], inverse(row_maps[coarse_row])),
        )
        for fine_row, fine_column in enumerate(block_map):
            cells.add((2 * fine_row + coarse_row, 2 * fine_column + coarse_column))
    assert len(cells) == 48
    return tuple(sorted(cells))


def verify_selected(host: tuple[Point, ...]) -> None:
    assert set(SELECTED).issubset(host)
    assert len(SELECTED) == 24
    assert all(sum(x == row for x, _ in SELECTED) == 2 for row in range(12))
    assert all(sum(y == column for _, y in SELECTED) == 2 for column in range(12))
    assert is_no_three(SELECTED)
    layer_points = tuple(
        (row, LAYERS[layer][row])
        for layer in (0, 1)
        for row in range(12)
    )
    assert set(layer_points) == set(SELECTED)


def verify_transport() -> None:
    canonical_host = build_normal_host(
        TARGET,
        ROW_RELATIVE,
        COLUMN_RELATIVE,
        INNER_RELATIVE,
        "ff",
    )
    verify_selected(canonical_host)

    factors = valid_factor_pairs(6)
    six_cycle_factors = [factor for factor in factors if relative_type(factor) == (6,)]
    assert len(factors) == 116
    assert len(six_cycle_factors) == 84

    all_permutations = tuple(permutations(range(6)))
    inverse_row_relative = inverse(ROW_RELATIVE)
    for tau_0, tau_1 in six_cycle_factors:
        relative = compose(inverse(tau_0), tau_1)
        gamma = next(
            candidate
            for candidate in all_permutations
            if compose(candidate, compose(relative, inverse(candidate))) == INNER_RELATIVE
        )
        row_maps = (
            gamma,
            compose(inverse_row_relative, gamma),
        )
        beta_0 = compose(TARGET, compose(gamma, inverse(tau_0)))
        column_maps = (
            beta_0,
            compose(COLUMN_RELATIVE, beta_0),
        )
        transported_host = build_factor_host(
            (tau_0, tau_1),
            row_maps,
            column_maps,
        )
        assert transported_host == canonical_host
        verify_selected(transported_host)

    print("transported the unique affine 6-cycle template to all 84 ordered factors")
    print(f"side-twelve layers: {LAYERS}")


def verify_census() -> None:
    source = Path(__file__).with_suffix(".cpp")
    assert source.exists(), source
    with tempfile.TemporaryDirectory() as temporary_directory:
        binary = Path(temporary_directory) / "verify_product_affine_full_selector_six"
        subprocess.run(
            ["g++", "-O3", "-std=c++17", str(source), "-o", str(binary)],
            check=True,
        )
        completed = subprocess.run(
            [str(binary)],
            check=True,
            text=True,
            capture_output=True,
        )

    observed: dict[tuple[str, str], tuple[int, int, int]] = {}
    for match in LINE_PATTERN.finditer(completed.stdout):
        factor_type, orientation, feasible, total, maximum = match.groups()
        observed[(factor_type, orientation)] = (
            int(feasible),
            int(total),
            int(maximum),
        )
    assert observed == EXPECTED, (observed, EXPECTED, completed.stdout)
    assert "T=(2,1,0,5,4,3) P=(5,4,3,2,1,0) Q=(5,4,3,2,1,0)" in completed.stdout
    print("affine side-six full-selector census: exactly one of 20,736 hosts is feasible")


def main() -> None:
    verify_census()
    verify_transport()


if __name__ == "__main__":
    main()
