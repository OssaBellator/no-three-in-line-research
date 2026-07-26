#!/usr/bin/env python3
"""Finite checks for CMR1462--CMR1469."""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import ceil, floor, gcd, log2
import random


def matching(value):
    return frozenset((row, value[row]) for row in range(len(value)))


def line_key(a, b):
    x1, y1 = a
    x2, y2 = b
    value = [y1 - y2, x2 - x1, x1 * y2 - x2 * y1]
    divisor = gcd(gcd(abs(value[0]), abs(value[1])), abs(value[2]))
    if divisor:
        value = [entry // divisor for entry in value]
    if value[0] < 0 or (
        value[0] == 0
        and (value[1] < 0 or (value[1] == 0 and value[2] < 0))
    ):
        value = [-entry for entry in value]
    return tuple(value)


def collinear(triple):
    return line_key(triple[0], triple[1]) == line_key(triple[0], triple[2])


def compatible(edges):
    return (
        len({row for row, _column in edges}) == len(edges)
        and len({column for _row, column in edges}) == len(edges)
    )


def candidate_family(side, opposite, current, target):
    cells = {(row, column) for row in range(side) for column in range(side)}
    graph = cells - set(opposite) - {target}
    old = set(opposite) | set(current)
    result = []
    for values in combinations(tuple(set(opposite) | graph), 3):
        triple = frozenset(values)
        if triple <= old or not collinear(values):
            continue
        prescription = frozenset(triple - set(opposite))
        if not prescription or not compatible(prescription):
            continue
        entering = prescription - set(current)
        if not entering:
            continue
        owner = min(entering)
        partners = tuple(sorted(triple - {owner}))
        assert all(
            partner in opposite or partner in current or owner < partner
            for partner in partners
        )
        result.append((prescription, owner, partners))
    return tuple(result)


def primitive_data(owner, partner):
    dx = partner[0] - owner[0]
    dy = partner[1] - owner[1]
    scale = gcd(abs(dx), abs(dy))
    u, v = dx // scale, dy // scale
    signed_scale = scale
    if u < 0 or (u == 0 and v < 0):
        u, v = -u, -v
        signed_scale = -scale
    return scale, u, v, max(abs(u), abs(v)), signed_scale


def valuation(value, prime):
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def projective_direction(u, v, prime):
    u, v = u % prime, v % prime
    if u:
        return 1, v * pow(u, -1, prime) % prime
    return 0, 1


def signature(owner, partner, opposite, prime):
    scale, u, v, height, _signed_scale = primitive_data(owner, partner)
    return (
        "fixed" if partner in opposite else "response",
        valuation(scale, prime),
        projective_direction(u, v, prime),
        1 << int(log2(height)),
    )


def direction_stock(prime, band):
    return (prime - 1) * ceil(4 * band / prime) ** 2


def greedy_packing(candidates, rng):
    residual = defaultdict(lambda: Fraction(1))
    weights = [Fraction(0) for _ in candidates]
    order = list(range(len(candidates)))
    rng.shuffle(order)
    for index in order:
        prescription = candidates[index][0]
        available = min(residual[edge] for edge in prescription)
        if available <= 0:
            continue
        value = available
        if rng.random() >= 0.7:
            units = max(1, int(12 * available))
            value = min(available, Fraction(rng.randint(1, units), 12))
        weights[index] = value
        for edge in prescription:
            residual[edge] -= value
    for edge in {edge for candidate in candidates for edge in candidate[0]}:
        assert sum(
            weight
            for weight, candidate in zip(weights, candidates)
            if edge in candidate[0]
        ) <= 1
    return tuple(weights)


def check_banks():
    rng = random.Random(1464)
    totals = [0, 0, 0, 0, 0]
    for side, prime, repetitions in ((5, 5, 100), (7, 7, 40)):
        opposite = matching(tuple(range(side)))
        derangements = [
            matching(value)
            for value in permutations(range(side))
            if all(value[index] != index for index in range(side))
        ]
        bands = 1 + int(log2(side - 1))
        class_stock = 2 * (prime + 1) * bands
        for _ in range(repetitions):
            current = rng.choice(derangements)
            target = rng.choice(tuple(current))
            candidates = candidate_family(side, opposite, current, target)
            weights = greedy_packing(candidates, rng)
            mass = sum(weights)

            classes = defaultdict(Fraction)
            owners = defaultdict(Fraction)
            pairs = defaultdict(Fraction)
            response_partners = defaultdict(Fraction)
            directions = defaultdict(Fraction)
            displacements = defaultdict(Fraction)

            for weight, (prescription, owner, partners) in zip(weights, candidates):
                if not weight:
                    continue
                owners[owner] += 2 * weight
                for partner in partners:
                    key = signature(owner, partner, opposite, prime)
                    classes[key] += weight
                    pairs[(owner, partner)] += weight
                    if partner not in opposite:
                        response_partners[partner] += weight
                    _scale, u, v, _height, signed = primitive_data(owner, partner)
                    directions[(key, (u, v))] += weight
                    displacements[(key, (u, v), signed)] += weight

            assert sum(classes.values()) == 2 * mass
            assert len(classes) <= class_stock
            assert max(classes.values()) * class_stock >= 2 * mass
            assert max(owners.values(), default=0) <= 2
            assert max(pairs.values(), default=0) <= 1
            assert max(response_partners.values(), default=0) <= 1

            for key, class_mass in classes.items():
                _kind, depth, _theta, band = key
                direction_bound = direction_stock(prime, band)
                direction_values = [
                    value
                    for (candidate_key, _direction), value in directions.items()
                    if candidate_key == key
                ]
                assert max(direction_values) * direction_bound >= class_mass

                scale_bound = floor((side - 1) / (prime**depth * band))
                assert scale_bound >= 1
                displacement_values = [
                    value
                    for (candidate_key, _direction, _signed), value
                    in displacements.items()
                    if candidate_key == key
                ]
                assert (
                    max(displacement_values)
                    * direction_bound
                    * 2
                    * scale_bound
                    >= class_mass
                )
                totals[3] += 1
                totals[4] += len(displacement_values)

            if mass >= Fraction(side - 2, 3):
                assert max(classes.values()) >= Fraction(
                    side - 2, 3 * (prime + 1) * bands
                )
                totals[2] += 1
            totals[0] += 1
            totals[1] += len(candidates)
    return tuple(totals)


def check_direction_stock():
    checks = 0
    for prime in (2, 3, 5, 7, 11, 13):
        for band in (1, 2, 4, 8, 16, 32):
            classes = defaultdict(set)
            limit = 2 * band
            for u in range(-limit + 1, limit):
                for v in range(-limit + 1, limit):
                    if (u, v) == (0, 0) or gcd(abs(u), abs(v)) != 1:
                        continue
                    if not (band <= max(abs(u), abs(v)) < 2 * band):
                        continue
                    if u < 0 or (u == 0 and v < 0):
                        u0, v0 = -u, -v
                    else:
                        u0, v0 = u, v
                    classes[projective_direction(u0, v0, prime)].add((u0, v0))
            assert max(map(len, classes.values()), default=0) <= direction_stock(
                prime, band
            )
            checks += 1
    return checks


def main():
    result = check_banks()
    print(
        "verified fractional packed signature fans:",
        result[0],
        "banks with",
        result[1],
        "candidate triples,",
        result[2],
        "packings above the positive-minimum threshold,",
        result[3],
        "signature classes,",
        result[4],
        "translated displacement classes, and",
        check_direction_stock(),
        "direction-stock checks",
    )


if __name__ == "__main__":
    main()
