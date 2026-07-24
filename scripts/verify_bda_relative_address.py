#!/usr/bin/env python3
"""Verify BDA3f relative coarse-address determinant accounting."""

from __future__ import annotations

from itertools import combinations, product

Point = tuple[int, int]


def determinant(points: tuple[Point, Point, Point]) -> int:
    first, second, third = points
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        - (third[0] - first[0]) * (second[1] - first[1])
    )


def quotient_residue(value: int, q: int) -> tuple[int, int]:
    quotient, residue = divmod(value, q)
    return quotient, residue


def relative_formula(
    points: tuple[Point, Point, Point],
    q: int,
) -> tuple[int, tuple[int, int, int, int]]:
    quotients: list[tuple[int, int]] = []
    residues: list[tuple[int, int]] = []
    for x, y in points:
        x_quotient, x_residue = quotient_residue(x, q)
        y_quotient, y_residue = quotient_residue(y, q)
        quotients.append((x_quotient, y_quotient))
        residues.append((x_residue, y_residue))

    delta_x2 = quotients[1][0] - quotients[0][0]
    delta_x3 = quotients[2][0] - quotients[0][0]
    delta_y2 = quotients[1][1] - quotients[0][1]
    delta_y3 = quotients[2][1] - quotients[0][1]
    value = (
        (q * delta_x2 + residues[1][0] - residues[0][0])
        * (q * delta_y3 + residues[2][1] - residues[0][1])
        - (q * delta_x3 + residues[2][0] - residues[0][0])
        * (q * delta_y2 + residues[1][1] - residues[0][1])
    )
    return value, (delta_x2, delta_x3, delta_y2, delta_y3)


def verify_identity() -> None:
    points = tuple(product(range(-3, 4), repeat=2))
    for q in range(2, 8):
        for triple in combinations(points, 3):
            value, relative = relative_formula(triple, q)
            assert value == determinant(triple)
            translated = tuple(
                (x + 3 * q, y - 2 * q) for x, y in triple
            )
            translated_value, translated_relative = relative_formula(
                translated,
                q,
            )
            assert translated_value == value
            assert translated_relative == relative


def verify_window_count() -> None:
    for width in range(4):
        addresses = set(product(range(-width, width + 1), repeat=4))
        assert len(addresses) == (2 * width + 1) ** 4


def verify_residue_wall() -> None:
    for q in range(2, 20):
        collinear = ((0, 0), (1, 1), (q, q))
        noncollinear = ((0, 0), (1, 1), (2 * q, q))
        first_residues = tuple(
            (x % q, y % q) for x, y in collinear
        )
        second_residues = tuple(
            (x % q, y % q) for x, y in noncollinear
        )
        assert first_residues == second_residues
        assert determinant(collinear) == 0
        assert determinant(noncollinear) == -q


def main() -> None:
    verify_identity()
    verify_window_count()
    verify_residue_wall()
    print("BDA relative coarse addresses: determinant regressions passed")


if __name__ == "__main__":
    main()
