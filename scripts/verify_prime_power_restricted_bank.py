#!/usr/bin/env python3
"""Verify CMR43--CMR46 on small restricted prime-power lift banks."""
from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations, product

Point = tuple[int, int]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        - (c[0] - a[0]) * (b[1] - a[1])
    )


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def nonsquares(p: int) -> list[int]:
    squares = {x * x % p for x in range(1, p)}
    return [value for value in range(1, p) if value not in squares]


def fibre_family(p: int) -> list[tuple[int, ...]]:
    h = (p - 1) // 2
    return [
        tuple(
            b if digit == 0 else (b + c * pow(digit, -1, p)) % p
            for digit in range(p)
        )
        for b, c in product(range(1, h + 1), nonsquares(p))
    ]


def quotient_layers(a: int) -> tuple[list[int], list[int]]:
    first = list(range(a))
    second = [(value + 1) % a for value in range(a)]
    return first, second


def verify_cylinders(p: int, family: list[tuple[int, ...]]) -> int:
    h = (p - 1) // 2
    singles: Counter[tuple[int, int]] = Counter()
    pairs: Counter[tuple[tuple[int, int], tuple[int, int]]] = Counter()
    for values in family:
        cells = [(digit, values[digit]) for digit in range(p)]
        singles.update(cells)
        pairs.update(combinations(cells, 2))
    assert max(singles.values(), default=0) <= h
    assert max(pairs.values(), default=0) <= 1
    return len(singles) + len(pairs)


def verify_one_fibre(p: int, a: int, family: list[tuple[int, ...]]) -> int:
    checks = 0
    for row0 in range(a):
        for row1 in range(a):
            if row0 == row1:
                continue
            for values0, values1 in product(family, repeat=2):
                points = (
                    [(a * digit, row0 + a * values0[digit]) for digit in range(p)]
                    + [(a * digit, row1 + a * values1[digit]) for digit in range(p)]
                )
                assert len(set(points)) == 2 * p
                for triple in combinations(points, 3):
                    assert determinant(*triple) != 0, (
                        p,
                        a,
                        row0,
                        row1,
                        triple,
                    )
                    checks += 1
    return checks


def build_sample_state(
    p: int,
    a: int,
    family: list[tuple[int, ...]],
) -> tuple[list[Point], list[tuple[int, int, int]]]:
    quotient0, quotient1 = quotient_layers(a)
    points: list[Point] = []
    metadata: list[tuple[int, int, int]] = []
    for residue in range(a):
        for layer, quotient in enumerate((quotient0, quotient1)):
            values = family[(2 * residue + layer) % len(family)]
            for digit in range(p):
                points.append(
                    (
                        residue + a * digit,
                        quotient[residue] + a * values[digit],
                    )
                )
                metadata.append((residue, layer, digit))
    return points, metadata


def verify_saturation(p: int, a: int, family: list[tuple[int, ...]]) -> int:
    points, _ = build_sample_state(p, a, family)
    n = p * a
    assert len(points) == 2 * n
    assert len(set(points)) == 2 * n
    column_counts = Counter(x for x, _ in points)
    row_counts = Counter(y for _, y in points)
    assert set(column_counts.values()) == {2}
    assert set(row_counts.values()) == {2}
    return 2 * n


def verify_first_separation(p: int, a: int, family: list[tuple[int, ...]]) -> int:
    """Check the CMR46 count after fixing all but one unique fibre choice."""
    h = (p - 1) // 2
    points, metadata = build_sample_state(p, a, family)
    checks = 0

    for first_index, second_index in combinations(range(len(points)), 2):
        first_meta = metadata[first_index]
        second_meta = metadata[second_index]
        first_residue = first_meta[0]
        second_residue = second_meta[0]

        for unique_residue in range(a):
            if unique_residue in (first_residue, second_residue):
                continue
            for layer in (0, 1):
                quotient_row = (
                    unique_residue
                    if layer == 0
                    else (unique_residue + 1) % a
                )
                for digit in range(p):
                    column = unique_residue + a * digit
                    successful = 0
                    for values in family:
                        third = (column, quotient_row + a * values[digit])
                        if determinant(points[first_index], points[second_index], third) == 0:
                            successful += 1
                    assert successful <= h, (
                        p,
                        a,
                        first_index,
                        second_index,
                        unique_residue,
                        layer,
                        digit,
                        successful,
                        h,
                    )
                    checks += len(family)
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=7)
    args = parser.parse_args()

    cylinder_checks = 0
    fibre_triples = 0
    saturation_checks = 0
    separation_checks = 0
    instances = 0

    for p in range(3, args.max_prime + 1, 2):
        if not is_prime(p):
            continue
        family = fibre_family(p)
        assert len(family) == ((p - 1) // 2) ** 2
        cylinder_checks += verify_cylinders(p, family)
        a = p
        fibre_triples += verify_one_fibre(p, a, family)
        saturation_checks += verify_saturation(p, a, family)
        separation_checks += verify_first_separation(p, a, family)
        instances += 1

    print(
        f"verified restricted-bank instances={instances}; "
        f"cylinders={cylinder_checks}; one-fibre-triples={fibre_triples}; "
        f"saturation={saturation_checks}; separation-exposures={separation_checks}"
    )


if __name__ == "__main__":
    main()
