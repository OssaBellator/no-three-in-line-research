#!/usr/bin/env python3
"""Verify AC3by--AC3cb on exhaustive small finite-field line/channel models."""

from itertools import product
from math import comb


def normalize_line(a, b, c, prime):
    a %= prime
    b %= prime
    c %= prime
    assert a or b
    pivot = a if a else b
    inverse = pow(pivot, -1, prime)
    return a * inverse % prime, b * inverse % prime, c * inverse % prime


def modular_lines(prime):
    lines = set()
    for a in range(prime):
        for b in range(prime):
            if not (a or b):
                continue
            for c in range(prime):
                lines.add(normalize_line(a, b, c, prime))
    return tuple(lines)


def channel_points(prime, parameter):
    return tuple((x, parameter * pow(x, -1, prime) % prime) for x in range(1, prime))


def on_line(point, line, prime):
    x, y = point
    a, b, c = line
    return (a * x + b * y - c) % prime == 0


def quadratic_roots(prime, s, b, parameter):
    return {
        x
        for x in range(prime)
        if (s * x * x + b * x - parameter) % prime == 0
    }


def verify_normal_forms():
    vertical_checks = 0
    horizontal_checks = 0
    quadratic_checks = 0
    discriminant_checks = 0
    vieta_checks = 0
    difference_checks = 0
    branch_checks = 0

    for prime in (5, 7, 11, 13):
        lines = modular_lines(prime)
        parameters = tuple(range(1, prime))
        points = {parameter: channel_points(prime, parameter) for parameter in parameters}
        intersections = {}

        for line in lines:
            a, b_line, c = line
            for parameter in parameters:
                cells = tuple(
                    point for point in points[parameter] if on_line(point, line, prime)
                )
                intersections[(line, parameter)] = cells

                if b_line == 0:
                    x = c * pow(a, -1, prime) % prime
                    expected = () if x == 0 else ((x, parameter * pow(x, -1, prime) % prime),)
                    assert cells == expected
                    vertical_checks += 1
                    continue

                intercept = c * pow(b_line, -1, prime) % prime
                if a == 0:
                    expected_x = None if intercept == 0 else parameter * pow(intercept, -1, prime) % prime
                    expected = () if expected_x is None else ((expected_x, intercept),)
                    assert cells == expected
                    horizontal_checks += 1
                    continue

                slope = -a * pow(b_line, -1, prime) % prime
                roots = quadratic_roots(prime, slope, intercept, parameter)
                actual_roots = {x for x, _ in cells}
                assert roots == actual_roots
                assert len(roots) <= 2
                quadratic_checks += 1

                discriminant = (intercept * intercept + 4 * slope * parameter) % prime
                square_roots = {value for value in range(prime) if value * value % prime == discriminant}
                if not square_roots:
                    assert not roots
                elif discriminant == 0:
                    assert len(roots) == 1
                else:
                    assert len(square_roots) == 2
                    assert len(roots) == 2
                discriminant_checks += 1

                if len(roots) == 2:
                    x1, x2 = sorted(roots)
                    assert (x1 + x2 + intercept * pow(slope, -1, prime)) % prime == 0
                    assert (x1 * x2 + parameter * pow(slope, -1, prime)) % prime == 0
                    vieta_checks += 1

            # Branch-word bounds for every channel tuple on this line.
            linear_line = b_line == 0 or a == 0
            for first in parameters:
                first_cells = intersections[(line, first)]
                for second in parameters:
                    second_cells = intersections[(line, second)]
                    pair_count = len(first_cells) * len(second_cells)
                    repeated_count = comb(len(first_cells), 2) * len(second_cells)
                    assert pair_count <= (1 if linear_line else 4)
                    assert repeated_count <= (0 if linear_line else 2)
                    branch_checks += 2

                    if not linear_line:
                        slope = -a * pow(b_line, -1, prime) % prime
                        intercept = c * pow(b_line, -1, prime) % prime
                        for point1, point2 in product(first_cells, second_cells):
                            x1, _ = point1
                            x2, _ = point2
                            left = (first - second) % prime
                            right = (
                                (x1 - x2)
                                * (slope * (x1 + x2) + intercept)
                            ) % prime
                            assert left == right
                            difference_checks += 1

                    for third in parameters:
                        third_cells = intersections[(line, third)]
                        triple_count = pair_count * len(third_cells)
                        assert triple_count <= (1 if linear_line else 8)
                        branch_checks += 1

    return (
        vertical_checks,
        horizontal_checks,
        quadratic_checks,
        discriminant_checks,
        vieta_checks,
        difference_checks,
        branch_checks,
    )


def main():
    values = verify_normal_forms()
    print(
        "AC RI I6 line channels: verified "
        f"{values[0]} vertical cases, {values[1]} horizontal cases, "
        f"{values[2]} quadratic root sets, {values[3]} discriminants, "
        f"{values[4]} Vieta pairs, {values[5]} mixed-channel differences, "
        f"and {values[6]} branch-word bounds"
    )


if __name__ == "__main__":
    main()
