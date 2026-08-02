#!/usr/bin/env python3
"""Verify the three-labeling normal form and low-syndrome rectangle bounds."""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb
from random import Random

Permutation = tuple[int, ...]
Point = tuple[int, int]
TaggedPoint = tuple[int, int, int, int, int]
ORIENTATIONS = ("cc", "cf", "fc", "ff")


def compose(first: Permutation, second: Permutation) -> Permutation:
    return tuple(first[second[index]] for index in range(len(first)))


def inverse(permutation: Permutation) -> Permutation:
    result = [0] * len(permutation)
    for index, value in enumerate(permutation):
        result[value] = index
    return tuple(result)


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def flatten(n: int, i: int, u: int, mode: str) -> int:
    return n * i + u if mode == "c" else 2 * u + i


def normal_form_host(
    h: Permutation,
    target: Permutation,
    row_relative: Permutation,
    column_relative: Permutation,
    orientation: str,
) -> frozenset[Point]:
    n = len(h)
    identity = tuple(range(n))
    cells: set[Point] = set()
    for i, j, s in product((0, 1), repeat=3):
        block_map = compose(
            column_relative if j else identity,
            compose(
                target,
                compose(h if s else identity, row_relative if i else identity),
            ),
        )
        for u, v in enumerate(block_map):
            cells.add(
                (
                    flatten(n, i, u, orientation[0]),
                    flatten(n, j, v, orientation[1]),
                )
            )
    assert len(cells) == 8 * n
    return frozenset(cells)


def three_label_host(
    h: Permutation,
    second_row_labels: Permutation,
    first_column_labels: Permutation,
    second_column_labels: Permutation,
    orientation: str,
) -> frozenset[Point]:
    n = len(h)
    cells: set[Point] = set()
    for i, j, s in product((0, 1), repeat=3):
        for abstract_row in range(n):
            row_digit = (
                abstract_row if i == 0 else second_row_labels[abstract_row]
            )
            abstract_column = h[abstract_row] if s else abstract_row
            column_digit = (
                first_column_labels[abstract_column]
                if j == 0
                else second_column_labels[abstract_column]
            )
            cells.add(
                (
                    flatten(n, i, row_digit, orientation[0]),
                    flatten(n, j, column_digit, orientation[1]),
                )
            )
    assert len(cells) == 8 * n
    return frozenset(cells)


def tagged_rectangles(
    p: Permutation,
    t: Permutation,
    r: Permutation,
    orientation: str = "cc",
) -> tuple[TaggedPoint, ...]:
    n = len(p)
    points: list[TaggedPoint] = []
    for u in range(n):
        x_digits = (u, p[u])
        y_digits = (t[u], r[u])
        for i, j in product((0, 1), repeat=2):
            points.append(
                (
                    flatten(n, i, x_digits[i], orientation[0]),
                    flatten(n, j, y_digits[j], orientation[1]),
                    u,
                    i,
                    j,
                )
            )
    return tuple(points)


def verify_saturation(points: tuple[TaggedPoint, ...]) -> None:
    side = len(points) // 2
    assert len(points) == 2 * side
    assert len({(x, y) for x, y, *_ in points}) == len(points)
    assert all(sum(x == row for x, *_ in points) == 2 for row in range(side))
    assert all(sum(y == column for _, y, *_ in points) == 2 for column in range(side))


def defect_split(points: tuple[TaggedPoint, ...]) -> tuple[int, int]:
    diagonal = 0
    transversal = 0
    for first, second, third in combinations(points, 3):
        if determinant(first[:2], second[:2], third[:2]) != 0:
            continue
        rectangle_count = len({first[2], second[2], third[2]})
        assert rectangle_count in (2, 3)
        if rectangle_count == 2:
            diagonal += 1
        else:
            transversal += 1
    return diagonal, transversal


def harmonic(number: int) -> Fraction:
    return sum((Fraction(1, value) for value in range(1, number + 1)), Fraction())


def line_count_bound(side: int) -> Fraction:
    return 2 * side**4 * harmonic(side - 1)


def exact_collinear_triples(side: int) -> int:
    points = tuple(product(range(side), repeat=2))
    return sum(1 for triple in combinations(points, 3) if determinant(*triple) == 0)


def expected_bound(n: int) -> Fraction:
    assert n >= 3
    diagonal = Fraction(8 * n * n, n - 1)
    transversal = (
        Fraction(64 * 12 * (2 * n) ** 4, n * (n - 1) * (n - 2))
        * harmonic(2 * n - 1)
    )
    return diagonal + transversal


def verify_label_normal_form() -> None:
    rng = Random(20260724)
    for n in range(2, 8):
        identity = tuple(range(n))
        for orientation in ORIENTATIONS:
            for _ in range(20):
                permutations_list: list[Permutation] = []
                for _ in range(4):
                    values = list(identity)
                    rng.shuffle(values)
                    permutations_list.append(tuple(values))
                h, target, row_relative, column_relative = permutations_list
                while any(h[index] == index for index in range(n)):
                    values = list(identity)
                    rng.shuffle(values)
                    h = tuple(values)
                first = normal_form_host(
                    h, target, row_relative, column_relative, orientation
                )
                second = three_label_host(
                    h,
                    inverse(row_relative),
                    target,
                    compose(column_relative, target),
                    orientation,
                )
                assert first == second
    print("PX61 three-labeling normal form: random equivalence checks passed")


def verify_line_count() -> None:
    for side in range(2, 9):
        exact = exact_collinear_triples(side)
        bound = line_count_bound(side)
        assert exact <= bound
        print(f"grid side={side}: collinear triples={exact}, primitive bound={bound}")


def verify_exact_rectangle_averages() -> None:
    expected = {
        2: (Fraction(5, 2), Fraction(0, 1)),
        3: (Fraction(76, 27), Fraction(130, 27)),
        4: (Fraction(27, 8), Fraction(125, 12)),
    }
    for n in range(2, 5):
        all_permutations = tuple(permutations(range(n)))
        diagonal = 0
        transversal = 0
        state_count = 0
        for p in all_permutations:
            for t in all_permutations:
                for r in all_permutations:
                    points = tagged_rectangles(p, t, r)
                    verify_saturation(points)
                    current_diagonal, current_transversal = defect_split(points)
                    diagonal += current_diagonal
                    transversal += current_transversal
                    state_count += 1
        averages = (Fraction(diagonal, state_count), Fraction(transversal, state_count))
        assert averages == expected[n]
        if n >= 3:
            assert sum(averages) <= expected_bound(n)
        print(
            f"n={n}: exact states={state_count}, "
            f"E diagonal={averages[0]}, E transversal={averages[1]}"
        )


def verify_random_orientations() -> None:
    rng = Random(61012)
    for n in range(5, 11):
        identity = list(range(n))
        for orientation in ORIENTATIONS:
            for _ in range(20):
                p = identity.copy()
                t = identity.copy()
                r = identity.copy()
                rng.shuffle(p)
                rng.shuffle(t)
                rng.shuffle(r)
                points = tagged_rectangles(tuple(p), tuple(t), tuple(r), orientation)
                verify_saturation(points)
                diagonal, transversal = defect_split(points)
                assert diagonal + transversal <= comb(4 * n, 3)
        print(f"n={n}: random rectangle states checked in all orientations")


def main() -> None:
    verify_label_normal_form()
    verify_line_count()
    verify_exact_rectangle_averages()
    verify_random_orientations()
    print("universal O(n log n) low-syndrome doubling checks passed")


if __name__ == "__main__":
    main()
