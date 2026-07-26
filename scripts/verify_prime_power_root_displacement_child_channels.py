#!/usr/bin/env python3
"""Finite checks for CMR1494--CMR1501."""

from collections import defaultdict
from fractions import Fraction
from math import ceil
import random


def valuation_zero(delta, prime):
    return not (
        delta[0] % prime == 0
        and delta[1] % prime == 0
    )


def root_channel(residue, delta, prime):
    partner_residue = (
        (residue[0] + delta[0]) % prime,
        (residue[1] + delta[1]) % prime,
    )
    quotient_carry = (
        (residue[0] + delta[0] - partner_residue[0]) // prime,
        (residue[1] + delta[1] - partner_residue[1]) // prime,
    )
    return partner_residue, quotient_carry


def all_arcs(side, delta):
    cells = {(x, y) for x in range(side) for y in range(side)}
    return [
        (a, (a[0] + delta[0], a[1] + delta[1]))
        for a in cells
        if (a[0] + delta[0], a[1] + delta[1]) in cells
    ]


def quotient(point, residue, prime):
    return (
        (point[0] - residue[0]) // prime,
        (point[1] - residue[1]) // prime,
    )


def check_channel_arithmetic():
    rng = random.Random(1494)
    residue_checks = 0
    arc_checks = 0
    prime_field_checks = 0

    for prime in (2, 3, 5, 7, 11):
        for exponent in (1, 2, 3):
            side = prime ** exponent
            for _ in range(120):
                while True:
                    delta = (
                        rng.randint(-(side - 1), side - 1),
                        rng.randint(-(side - 1), side - 1),
                    )
                    if delta != (0, 0) and valuation_zero(delta, prime):
                        break

                for _ in range(20):
                    residue = (
                        rng.randrange(prime),
                        rng.randrange(prime),
                    )
                    partner_residue, carry = root_channel(
                        residue, delta, prime
                    )
                    assert partner_residue != residue
                    residue_checks += 1

                    source = (
                        residue[0] + prime * rng.randrange(side // prime),
                        residue[1] + prime * rng.randrange(side // prime),
                    )
                    partner = (
                        source[0] + delta[0],
                        source[1] + delta[1],
                    )
                    if not (
                        0 <= partner[0] < side
                        and 0 <= partner[1] < side
                    ):
                        continue
                    assert (
                        partner[0] % prime,
                        partner[1] % prime,
                    ) == partner_residue
                    source_q = quotient(source, residue, prime)
                    partner_q = quotient(
                        partner, partner_residue, prime
                    )
                    assert (
                        partner_q[0] - source_q[0],
                        partner_q[1] - source_q[1],
                    ) == carry
                    arc_checks += 1

                    if exponent == 1:
                        assert source_q == (0, 0)
                        assert partner_q == (0, 0)
                        prime_field_checks += 1

    return residue_checks, arc_checks, prime_field_checks


def check_weighted_channels():
    rng = random.Random(1495)
    banks = 0
    weighted_arcs = 0
    channel_checks = 0
    private_support_checks = 0

    for prime, exponent, repetitions in (
        (2, 4, 120),
        (3, 3, 100),
        (5, 2, 80),
        (7, 2, 60),
    ):
        side = prime ** exponent
        for _ in range(repetitions):
            while True:
                delta = (
                    rng.randint(-(side - 1), side - 1),
                    rng.randint(-(side - 1), side - 1),
                )
                if delta != (0, 0) and valuation_zero(delta, prime):
                    break
            stock = all_arcs(side, delta)
            if not stock:
                continue
            arcs = rng.sample(stock, rng.randint(1, min(len(stock), 250)))
            weights = {
                arc: Fraction(rng.randint(1, 12), 12)
                for arc in arcs
            }
            classes = defaultdict(list)
            for arc in arcs:
                residue = (
                    arc[0][0] % prime,
                    arc[0][1] % prime,
                )
                classes[residue].append(arc)

            total = sum(weights.values())
            assert len(classes) <= prime * prime
            heavy_residue, heavy = max(
                classes.items(),
                key=lambda item: sum(weights[arc] for arc in item[1]),
            )
            heavy_mass = sum(weights[arc] for arc in heavy)
            assert heavy_mass * prime * prime >= total
            assert len(heavy) >= ceil(heavy_mass)

            partner_residue, carry = root_channel(
                heavy_residue, delta, prime
            )
            endpoints = []
            source_q_seen = set()
            partner_q_seen = set()
            for source, partner in heavy:
                assert (
                    source[0] % prime,
                    source[1] % prime,
                ) == heavy_residue
                assert (
                    partner[0] % prime,
                    partner[1] % prime,
                ) == partner_residue
                source_q = quotient(source, heavy_residue, prime)
                partner_q = quotient(partner, partner_residue, prime)
                assert (
                    partner_q[0] - source_q[0],
                    partner_q[1] - source_q[1],
                ) == carry
                source_q_seen.add(source_q)
                partner_q_seen.add(partner_q)
                endpoints.extend((source, partner))

            assert len(endpoints) == len(set(endpoints))
            assert len(source_q_seen) == len(heavy)
            assert len(partner_q_seen) == len(heavy)

            for response_partner in (False, True):
                supports = [
                    ({source, partner} if response_partner else {source})
                    for source, partner in heavy
                ]
                support_edges = [edge for support in supports for edge in support]
                assert len(support_edges) == len(set(support_edges))
                private_support_checks += 1

            banks += 1
            weighted_arcs += len(arcs)
            channel_checks += len(classes)

    return banks, weighted_arcs, channel_checks, private_support_checks


def factor_pattern(owner_factor, partner_factor, witness_factor, fixed_partner):
    counts = defaultdict(int)
    counts[owner_factor] += 1
    if not fixed_partner:
        counts[partner_factor] += 1
    if witness_factor is not None:
        counts[witness_factor] += 1
    return tuple(sorted((value for value in counts.values()), reverse=True))


def check_low_rank_patterns():
    rng = random.Random(1497)
    checks = 0
    allowed = {
        (1,),
        (2,),
        (1, 1),
        (2, 1),
        (1, 1, 1),
    }
    for prime in (2, 3, 5, 7):
        factors = list(range(prime * prime))
        for _ in range(2000):
            owner = rng.choice(factors)
            partner = rng.choice([value for value in factors if value != owner])
            fixed = bool(rng.randrange(2))
            witness = None if rng.randrange(3) == 0 else rng.choice(factors)
            pattern = factor_pattern(owner, partner, witness, fixed)
            assert pattern in allowed
            assert max(pattern) <= 2
            checks += 1
    return checks


def check_child_side_and_terminal():
    checks = 0
    for prime in (2, 3, 5, 7, 11):
        for exponent in range(1, 7):
            parent = prime ** exponent
            child = prime ** (exponent - 1)
            assert child < parent
            if exponent == 1:
                assert child == 1
            else:
                assert child >= prime
            checks += 1
    return checks


def main():
    arithmetic = check_channel_arithmetic()
    channels = check_weighted_channels()
    patterns = check_low_rank_patterns()
    child = check_child_side_and_terminal()
    print(
        "verified root displacement child channels:",
        arithmetic[0],
        "residue/carry checks,",
        arithmetic[1],
        "contained-arc quotient checks and",
        arithmetic[2],
        "prime-field terminal checks;",
        channels[0],
        "weighted banks with",
        channels[1],
        "arcs across",
        channels[2],
        "root channels and",
        channels[3],
        "private-support checks;",
        patterns,
        "low-rank factor patterns; and",
        child,
        "strict-child side checks",
    )


if __name__ == "__main__":
    main()
