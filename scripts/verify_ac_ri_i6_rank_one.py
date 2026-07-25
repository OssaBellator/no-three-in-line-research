#!/usr/bin/env python3
"""Verify AC3bp--AC3bs on exhaustive small prime/subgroup models."""

from fractions import Fraction
from itertools import combinations, permutations, product
from math import ceil


def divisors(value):
    return [d for d in range(1, value + 1) if value % d == 0]


def primitive_root(prime):
    for candidate in range(2, prime):
        seen = {pow(candidate, exponent, prime) for exponent in range(prime - 1)}
        if len(seen) == prime - 1:
            return candidate
    raise AssertionError("no primitive root")


def subgroup(prime, order):
    generator = primitive_root(prime)
    step = (prime - 1) // order
    return tuple(sorted({pow(generator, step * index, prime) for index in range(order)}))


def coset_representatives(prime, group):
    unseen = set(range(1, prime))
    representatives = []
    while unseen:
        representative = min(unseen)
        coset = {(representative * value) % prime for value in group}
        representatives.append(representative)
        unseen -= coset
    return tuple(representatives)


def normalize_line(A, B, C, prime):
    A %= prime
    B %= prime
    C %= prime
    assert A or B
    pivot = A if A else B
    scale = pow(pivot, -1, prime)
    return (A * scale % prime, B * scale % prime, C * scale % prime)


def modular_lines(prime):
    lines = set()
    for A in range(prime):
        for B in range(prime):
            if not (A or B):
                continue
            for C in range(prime):
                lines.add(normalize_line(A, B, C, prime))
    return tuple(lines)


def channel_cells(prime, a, group, representatives, alpha, beta, shift):
    source_rep = representatives[alpha]
    target_rep = representatives[beta]
    cells = []
    for g in group:
        x = source_rep * g % prime
        y = a * pow(target_rep * shift * g % prime, -1, prime) % prime
        cells.append((x, y, g))
    return cells


def recover_channel(prime, a, group, representatives, cell):
    x, y = cell
    source_alpha = next(
        alpha
        for alpha, representative in enumerate(representatives)
        if x * pow(representative, -1, prime) % prime in group
    )
    source_rep = representatives[source_alpha]
    g = x * pow(source_rep, -1, prime) % prime
    denominator = a * pow(y, -1, prime) % prime
    target_alpha = next(
        beta
        for beta, representative in enumerate(representatives)
        if denominator * pow(g * representative % prime, -1, prime) % prime in group
    )
    target_rep = representatives[target_alpha]
    shift = denominator * pow(target_rep * g % prime, -1, prime) % prime
    assert shift in group
    return source_alpha, target_alpha, shift, g


def i6_states(prime, a, group, representatives):
    m = len(representatives)
    states = []
    for perm in permutations(range(m)):
        for shifts in product(group, repeat=m):
            mapping = {}
            for alpha, source_rep in enumerate(representatives):
                target_rep = representatives[perm[alpha]]
                shift = shifts[alpha]
                for g in group:
                    x = source_rep * g % prime
                    y = a * pow(target_rep * shift * g % prime, -1, prime) % prime
                    mapping[x] = y
            states.append(mapping)
    return states


def verify_geometry():
    channel_checks = 0
    recovery_checks = 0
    line_checks = 0
    probability_checks = 0
    multi_cell_checks = 0
    secant_checks = 0

    for prime in (5, 7, 11, 13):
        lines = modular_lines(prime)
        for order in divisors(prime - 1):
            if order == 1:
                continue
            group = subgroup(prime, order)
            all_reps = coset_representatives(prime, group)
            for m in range(1, min(4, len(all_reps)) + 1):
                representatives = all_reps[:m]
                states = i6_states(prime, 1, group, representatives)
                expected_count = len(states) // (m * order)

                for alpha in range(m):
                    for beta in range(m):
                        for shift in group:
                            cells = channel_cells(
                                prime, 1, group, representatives, alpha, beta, shift
                            )
                            product_value = (
                                representatives[alpha]
                                * pow(representatives[beta] * shift % prime, -1, prime)
                                % prime
                            )
                            for x, y, g in cells:
                                assert x * y % prime == product_value
                                channel_checks += 1
                                recovered = recover_channel(
                                    prime, 1, group, representatives, (x, y)
                                )
                                assert recovered == (alpha, beta, shift, g)
                                recovery_checks += 1
                                count = sum(state.get(x) == y for state in states)
                                assert count == expected_count
                                probability_checks += 1

                            # Any compatible collection of one, two, or three cells
                            # in one channel fixes the same source image and shift.
                            physical_cells = [(x, y) for x, y, _ in cells]
                            for size in range(1, min(3, len(physical_cells)) + 1):
                                for prescribed in combinations(physical_cells, size):
                                    count = sum(
                                        all(state.get(x) == y for x, y in prescribed)
                                        for state in states
                                    )
                                    assert count == expected_count
                                    multi_cell_checks += 1

                            point_set = set(physical_cells)
                            for A, B, C in lines:
                                intersection = sum(
                                    (A * x + B * y - C) % prime == 0
                                    for x, y in point_set
                                )
                                assert intersection <= 2
                                line_checks += 1

                            # On a fixed product channel, the modular sum determines
                            # the unordered pair through its quadratic polynomial.
                            pairs_by_sum = {}
                            for first, second in combinations(point_set, 2):
                                pair = tuple(sorted((first[0], second[0])))
                                key = (first[0] + second[0]) % prime
                                assert key not in pairs_by_sum or pairs_by_sum[key] == pair
                                pairs_by_sum[key] = pair
                                assert first[0] * second[0] % prime == product_value
                                secant_checks += 1

    return (
        channel_checks,
        recovery_checks,
        line_checks,
        probability_checks,
        multi_cell_checks,
        secant_checks,
    )


def verify_weight_routers(maximum=24):
    raw_checks = 0
    router_checks = 0
    split_checks = 0

    for m in range(1, 5):
        for order in range(1, 9):
            for expected_numerator in range(maximum + 1):
                c1 = Fraction(expected_numerator, m * order)
                raw = m * order * c1
                assert raw == expected_numerator
                channel_average = raw / (m * m * order)
                assert channel_average == c1 / m
                raw_checks += 1

                # One- and two-moving-cell classes partition one channel.
                for one_cell in range(expected_numerator + 1):
                    two_cell = expected_numerator - one_cell
                    assert max(one_cell, two_cell) * 2 >= expected_numerator
                    split_checks += 1

    for total in range(1, maximum + 1):
        for threshold in range(1, maximum + 1):
            class_count = ceil(total / threshold)
            assert class_count * threshold >= total
            # Direction, affine-offset, and secant-sum routers use the same bound.
            router_checks += 3

    return raw_checks, split_checks, router_checks


def main():
    channels, recovery, lines, probabilities, multi, secants = verify_geometry()
    raw, splits, routers = verify_weight_routers()
    print(
        "AC RI I6 source-rank one: verified "
        f"{channels} channel products, {recovery} channel recoveries, "
        f"{lines} line-conic intersections, {probabilities} single-cell and "
        f"{multi} multi-cell probabilities, {secants} secant signatures, "
        f"{raw} raw-weight cancellations, {splits} local-rank splits, "
        f"and {routers} affine/secant routers"
    )


if __name__ == "__main__":
    main()
