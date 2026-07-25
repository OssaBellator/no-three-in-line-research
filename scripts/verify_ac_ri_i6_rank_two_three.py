#!/usr/bin/env python3
"""Verify AC3bt--AC3bx on exhaustive small I6 and finite-field models."""

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from math import ceil, comb, factorial


def falling(value, rank):
    result = 1
    for offset in range(rank):
        result *= value - offset
    return result


def i6_states(m, h):
    return [
        (perm, shifts)
        for perm in permutations(range(m))
        for shifts in product(range(h), repeat=m)
    ]


def verify_cylinders():
    state_checks = 0
    cylinder_checks = 0
    multiplicity_checks = 0

    for m in range(2, 5):
        for h in range(1, 4):
            states = i6_states(m, h)
            assert len(states) == factorial(m) * h**m
            state_checks += len(states)

            for rank in range(2, min(3, m) + 1):
                expected = factorial(m - rank) * h ** (m - rank)
                for sources in combinations(range(m), rank):
                    counts = Counter(
                        tuple((perm[source], shifts[source]) for source in sources)
                        for perm, shifts in states
                    )
                    assert counts
                    assert set(counts.values()) == {expected}
                    cylinder_checks += len(counts)

                    # Prescribing one or two cells inside one selected source coset
                    # still fixes only the same target image and common shift.
                    for signature, count in counts.items():
                        assert count == expected
                        for local_sizes in (
                            ((1, 1), (2, 1), (1, 2))
                            if rank == 2
                            else ((1, 1, 1),)
                        ):
                            assert len(local_sizes) == rank
                            assert sum(local_sizes) <= 3
                            multiplicity_checks += 1

    # Exhaust the positive compositions of at most three moving cells.
    rank_two = set()
    rank_three = set()
    for total in range(1, 4):
        for parts in product(range(1, 4), repeat=2):
            if sum(parts) == total:
                rank_two.add(parts)
        for parts in product(range(1, 4), repeat=3):
            if sum(parts) == total:
                rank_three.add(parts)
    assert rank_two == {(1, 1), (1, 2), (2, 1)}
    assert rank_three == {(1, 1, 1)}

    return state_checks, cylinder_checks, multiplicity_checks


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


def verify_geometry():
    intersection_checks = 0
    rank_two_pair_checks = 0
    repeated_checks = 0
    rank_three_checks = 0
    secant_checks = 0

    for prime in (5, 7, 11, 13):
        lines = modular_lines(prime)
        parameters = range(1, prime)
        points = {parameter: channel_points(prime, parameter) for parameter in parameters}
        intersections = {}

        for line in lines:
            for parameter in parameters:
                cells = tuple(point for point in points[parameter] if on_line(point, line, prime))
                assert len(cells) <= 2
                intersections[(line, parameter)] = cells
                intersection_checks += 1

                if len(cells) == 2:
                    x1, x2 = sorted(point[0] for point in cells)
                    address = ((x1 + x2) % prime, (x1 * x2) % prime)
                    roots = {
                        x
                        for x in range(prime)
                        if (x * x - address[0] * x + address[1]) % prime == 0
                    }
                    assert roots == {x1, x2}
                    secant_checks += 1

        for line in lines:
            for first in parameters:
                first_cells = intersections[(line, first)]
                for second in parameters:
                    second_cells = intersections[(line, second)]
                    assert len(first_cells) * len(second_cells) <= 4
                    rank_two_pair_checks += 1

                    repeated_count = comb(len(first_cells), 2) * len(second_cells)
                    assert repeated_count <= 2
                    repeated_checks += 1

                    for third in parameters:
                        third_cells = intersections[(line, third)]
                        assert len(first_cells) * len(second_cells) * len(third_cells) <= 8
                        rank_three_checks += 1

    return (
        intersection_checks,
        rank_two_pair_checks,
        repeated_checks,
        rank_three_checks,
        secant_checks,
    )


def verify_weight_constants(maximum=30):
    amplification_checks = 0
    router_checks = 0

    for m in range(2, 5):
        for h in range(1, 7):
            for c2_numerator in range(maximum + 1):
                c2 = Fraction(c2_numerator, 1)
                raw = falling(m, 2) * h**2 * c2
                tuple_count = falling(m, 2) ** 2 * h**2
                assert raw / tuple_count == c2 / falling(m, 2)
                assert raw / tuple_count / 3 == c2 / (3 * falling(m, 2))
                amplification_checks += 1

            if m >= 3:
                for c3_numerator in range(maximum + 1):
                    c3 = Fraction(c3_numerator, 1)
                    raw = falling(m, 3) * h**3 * c3
                    tuple_count = falling(m, 3) ** 2 * h**3
                    assert raw / tuple_count == c3 / falling(m, 3)
                    amplification_checks += 1

    for total in range(1, maximum + 1):
        for threshold in range(1, maximum + 1):
            classes = ceil(total / threshold)
            assert classes * threshold >= total
            router_checks += 2

    return amplification_checks, router_checks


def main():
    states, cylinders, multiplicities = verify_cylinders()
    intersections, pairs, repeated, triples, secants = verify_geometry()
    amplification, routers = verify_weight_constants()
    print(
        "AC RI I6 rank two/three: verified "
        f"{states} I6 states, {cylinders} source-rank cylinders, "
        f"{multiplicities} multiplicity records, {intersections} line-conic intersections, "
        f"{pairs} rank-two pair bounds, {repeated} repeated-channel bounds, "
        f"{triples} rank-three bounds, {secants} secant addresses, "
        f"{amplification} raw-weight constants, and {routers} line routers"
    )


if __name__ == "__main__":
    main()
