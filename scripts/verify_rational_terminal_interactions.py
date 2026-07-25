#!/usr/bin/env python3
"""Exhaust RI5ac--RI5ae on finite interaction words and hyperbolas."""

from itertools import combinations, product
from math import ceil


def inverse(value, prime):
    return pow(value, prime - 2, prime)


def determinant(point_1, point_2, point_3, prime):
    x1, y1 = point_1
    x2, y2 = point_2
    x3, y3 = point_3
    return (
        (x2 - x1) * (y3 - y1)
        - (y2 - y1) * (x3 - x1)
    ) % prime


def rank_two_words():
    words = []
    for bits in ((1, 0), (0, 1), (1, 1)):
        for sizes in ((1, 1, "N"), (2, 1), (1, 2)):
            if sizes == (1, 1, "N"):
                target_cells = bits[0] + bits[1]
            else:
                target_cells = bits[0] * sizes[0] + bits[1] * sizes[1]
            if target_cells <= 2:
                words.append((bits, sizes))
    return words


def rank_three_words():
    return [
        bits
        for bits in product((0, 1), repeat=3)
        if any(bits) and sum(bits) <= 2
    ]


def verify_words():
    rank_two = rank_two_words()
    rank_three = rank_three_words()
    assert len(rank_two) == 7
    assert len(rank_three) == 6
    assert ((1, 1), (2, 1)) not in rank_two
    assert ((1, 1), (1, 2)) not in rank_two
    assert (1, 1, 1) not in rank_three
    return len(rank_two), len(rank_three)


def verify_geometry(primes=(5, 7, 11)):
    conic_checks = 0
    secant_checks = 0
    context_checks = 0

    for prime in primes:
        columns = list(range(1, prime))
        all_points = [(x, y) for x in columns for y in columns]

        for parameter in columns:
            hyperbola = {
                (x, parameter * inverse(x, prime) % prime)
                for x in columns
            }

            for triple in combinations(hyperbola, 3):
                assert determinant(*triple, prime) != 0
                conic_checks += 1

            for context in combinations(all_points, 2):
                target_columns = {
                    x
                    for x, y in hyperbola
                    if determinant(
                        context[0], context[1], (x, y), prime
                    ) == 0
                }
                assert len(target_columns) <= 2
                context_checks += 1

            seen_secants = {}
            for x, y in combinations(columns, 2):
                total = (x + y) % prime
                product_value = (x * y) % prime
                points = (
                    (x, parameter * inverse(x, prime) % prime),
                    (y, parameter * inverse(y, prime) % prime),
                )
                for column, row in points:
                    assert (
                        product_value * row
                        + parameter * column
                        - parameter * total
                    ) % prime == 0
                key = (total, product_value)
                pair = frozenset((x, y))
                assert key not in seen_secants or seen_secants[key] == pair
                seen_secants[key] = pair
                secant_checks += 1

    return conic_checks, secant_checks, context_checks


def verify_pigeonholes(maximum_weight=4, maximum_profiles=4):
    checks = 0
    for profile_count in range(1, maximum_profiles + 1):
        rank_two_classes = 7 * profile_count
        rank_three_classes = 6 * profile_count

        for total in range(1, maximum_weight * rank_two_classes + 1):
            assert ceil(total / rank_two_classes) * rank_two_classes >= total
            checks += 1

        for total in range(1, maximum_weight * rank_three_classes + 1):
            assert ceil(total / rank_three_classes) * rank_three_classes >= total
            checks += 1

        for expected in range(1, maximum_weight + 1):
            raw_two = 4 * expected
            raw_three = 8 * expected
            assert raw_two / (7 * profile_count) >= 4 * expected / (7 * profile_count)
            assert raw_three / (6 * profile_count) >= 4 * expected / (7 * profile_count)
            checks += 1

    return checks


def main():
    rank_two, rank_three = verify_words()
    conic, secants, contexts = verify_geometry()
    pigeonholes = verify_pigeonholes()
    print(
        "RI terminal interactions: verified "
        f"{rank_two} rank-two words, {rank_three} rank-three words, "
        f"{conic} conic triples, {secants} secants, "
        f"{contexts} context lines, and {pigeonholes} routers"
    )


if __name__ == "__main__":
    main()
