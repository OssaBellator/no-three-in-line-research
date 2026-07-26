#!/usr/bin/env python3
"""Finite checks for CMR1470--CMR1477."""

from collections import defaultdict
from fractions import Fraction
from math import gcd
import random


def valuation(value, prime):
    value = abs(value)
    result = 0
    while value and value % prime == 0:
        value //= prime
        result += 1
    return result


def primitive(vector):
    return gcd(abs(vector[0]), abs(vector[1])) == 1


def add(first, second):
    return first[0] + second[0], first[1] + second[1]


def scale(value, vector):
    return value * vector[0], value * vector[1]


def inside(cell, side):
    return 0 <= cell[0] < side and 0 <= cell[1] < side


def check_endpoint_cells():
    rng = random.Random(1470)
    checked = 0
    for prime in (2, 3, 5, 7):
        for exponent in range(1, 7):
            side = prime**exponent
            for depth in range(exponent):
                modulus = prime**depth
                for _ in range(250):
                    while True:
                        q = (rng.randint(-12, 12), rng.randint(-12, 12))
                        if q != (0, 0) and primitive(q):
                            break
                    unit = rng.randint(1, 20)
                    while unit % prime == 0:
                        unit += 1
                    displacement = scale(modulus * unit, q)
                    lower_x = max(0, -displacement[0])
                    upper_x = min(side - 1, side - 1 - displacement[0])
                    lower_y = max(0, -displacement[1])
                    upper_y = min(side - 1, side - 1 - displacement[1])
                    if lower_x > upper_x or lower_y > upper_y:
                        continue
                    owner = (rng.randint(lower_x, upper_x), rng.randint(lower_y, upper_y))
                    partner = add(owner, displacement)
                    assert inside(partner, side)
                    assert owner[0] % modulus == partner[0] % modulus
                    assert owner[1] % modulus == partner[1] % modulus
                    next_modulus = modulus * prime
                    assert (
                        owner[0] % next_modulus != partner[0] % next_modulus
                        or owner[1] % next_modulus != partner[1] % next_modulus
                    )
                    checked += 1
    return checked


def check_weighted_cell_pigeonhole():
    rng = random.Random(1471)
    checked = 0
    for prime in (2, 3, 5, 7, 11):
        for depth in range(8):
            stock = prime ** (2 * depth)
            for _ in range(300):
                by_cell = defaultdict(Fraction)
                for _incidence in range(rng.randint(1, 600)):
                    cell = rng.randrange(stock)
                    by_cell[cell] += Fraction(rng.randint(1, 30), rng.randint(1, 20))
                total = sum(by_cell.values(), Fraction(0))
                assert max(by_cell.values()) >= total / stock
                checked += 1
    return checked


def check_internal_crossing_routing():
    rng = random.Random(1472)
    checked = 0
    exit_checks = 0
    for prime in (2, 3, 5, 7):
        for depth in range(6):
            modulus = prime**depth
            for _ in range(400):
                events = []
                for _event in range(rng.randint(1, 100)):
                    parameter = rng.randint(-10000, 10000) or 1
                    weight = Fraction(rng.randint(1, 20), rng.randint(1, 20))
                    events.append((parameter, weight, parameter % modulus == 0))
                internal_mass = sum(
                    (weight for _parameter, weight, internal in events if internal),
                    Fraction(0),
                )
                crossing_mass = sum(
                    (weight for _parameter, weight, internal in events if not internal),
                    Fraction(0),
                )
                total = internal_mass + crossing_mass
                assert max(internal_mass, crossing_mass) >= total / 2
                if depth and crossing_mass:
                    by_exit = defaultdict(Fraction)
                    for parameter, weight, internal in events:
                        if not internal:
                            exit_depth = valuation(parameter, prime)
                            assert exit_depth < depth
                            by_exit[exit_depth] += weight
                    assert max(by_exit.values()) >= crossing_mass / depth
                    exit_checks += 1
                checked += 1
    return checked, exit_checks


def check_internal_scaling():
    rng = random.Random(1474)
    checked = 0
    for prime in (2, 3, 5):
        for exponent in range(2, 8):
            side = prime**exponent
            for depth in range(1, exponent):
                modulus = prime**depth
                reduced_side = prime ** (exponent - depth)
                for _ in range(250):
                    residue = (rng.randrange(modulus), rng.randrange(modulus))
                    owner_reduced = (
                        rng.randrange(reduced_side),
                        rng.randrange(reduced_side),
                    )
                    while True:
                        q = (rng.randint(-5, 5), rng.randint(-5, 5))
                        if q != (0, 0) and primitive(q):
                            break
                    unit = rng.randint(1, 10)
                    while unit % prime == 0:
                        unit += 1
                    partner_reduced = add(owner_reduced, scale(unit, q))
                    witness_reduced = add(owner_reduced, scale(rng.randint(-10, 10), q))
                    if not inside(partner_reduced, reduced_side):
                        continue
                    if not inside(witness_reduced, reduced_side):
                        continue
                    owner = add(residue, scale(modulus, owner_reduced))
                    partner = add(residue, scale(modulus, partner_reduced))
                    witness = add(residue, scale(modulus, witness_reduced))
                    assert inside(owner, side) and inside(partner, side)
                    assert inside(witness, side)
                    assert (
                        ((partner[0] - owner[0]) // modulus,
                         (partner[1] - owner[1]) // modulus)
                        == scale(unit, q)
                    )
                    assert unit % prime != 0
                    checked += 1
    return checked


def check_quantitative_splice():
    rng = random.Random(1475)
    checked = 0
    for _ in range(60000):
        prime = rng.choice((2, 3, 5, 7))
        depth = rng.randint(0, 10)
        mass = Fraction(rng.randint(1, 100000), rng.randint(1, 1000))
        cell_mass = mass / prime ** (2 * depth)
        assert cell_mass * prime ** (2 * depth) == mass
        assert cell_mass / 2 == mass / (2 * prime ** (2 * depth))
        if depth:
            assert cell_mass / (2 * depth) == mass / (
                2 * depth * prime ** (2 * depth)
            )
        checked += 1
    return checked


def check_token_stock():
    rng = random.Random(1476)
    checked = 0
    for prime in (2, 3, 5, 7, 11):
        for depth in range(10):
            side = prime**depth
            stock = prime ** (2 * depth)
            assert stock == side * side
            for _ in range(250):
                by_token = defaultdict(Fraction)
                for _bank in range(rng.randint(1, 300)):
                    token_id = rng.randrange(stock)
                    by_token[token_id] += Fraction(
                        rng.randint(1, 30), rng.randint(1, 30)
                    )
                total_mass = sum(by_token.values(), Fraction(0))
                assert max(by_token.values()) >= total_mass / stock
                checked += 1
    return checked


def main():
    routing = check_internal_crossing_routing()
    print(
        "verified weighted displacement carry routing:",
        check_endpoint_cells(),
        "endpoint-cell cases,",
        check_weighted_cell_pigeonhole(),
        "weighted sparse cell distributions,",
        routing[0],
        "internal/crossing splits with",
        routing[1],
        "exit-depth checks,",
        check_internal_scaling(),
        "strict scalings,",
        check_quantitative_splice(),
        "quantitative splice cases, and",
        check_token_stock(),
        "symbolic token-stock cases",
    )


if __name__ == "__main__":
    main()
