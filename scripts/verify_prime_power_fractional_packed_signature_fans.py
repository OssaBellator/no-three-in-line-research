#!/usr/bin/env python3
"""Finite checks for CMR1422--CMR1429."""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import ceil, floor, gcd, log2
import random


def matching(permutation):
    return frozenset((row, permutation[row]) for row in range(len(permutation)))


def line_key(first, second):
    x1, y1 = first
    x2, y2 = second
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1
    divisor = gcd(gcd(abs(a), abs(b)), abs(c))
    if divisor:
        a //= divisor
        b //= divisor
        c //= divisor
    if a < 0 or (a == 0 and b < 0) or (a == 0 and b == 0 and c < 0):
        a, b, c = -a, -b, -c
    return a, b, c


def collinear(triple):
    return line_key(triple[0], triple[1]) == line_key(triple[0], triple[2])


def compatible(edges):
    return (
        len({row for row, _column in edges}) == len(edges)
        and len({column for _row, column in edges}) == len(edges)
    )


def candidate_family(side, opposite, current, target):
    cells = {
        (row, column)
        for row in range(side)
        for column in range(side)
    }
    graph = cells - set(opposite) - {target}
    old_state = set(opposite) | set(current)
    result = []
    for value in combinations(tuple(set(opposite) | graph), 3):
        triple = frozenset(value)
        if triple <= old_state or not collinear(value):
            continue
        prescription = frozenset(triple - set(opposite))
        if not prescription or not compatible(prescription):
            continue
        entering = prescription - set(current)
        if not entering:
            continue
        owner = min(entering)
        partners = tuple(sorted(triple - {owner}))
        for partner in partners:
            if partner in opposite or partner in current or owner < partner:
                continue
            raise AssertionError("noneligible partner in an owned candidate")
        result.append((triple, prescription, owner, partners))
    return tuple(result)


def primitive_data(owner, partner):
    dx = partner[0] - owner[0]
    dy = partner[1] - owner[1]
    scale = gcd(abs(dx), abs(dy))
    u = dx // scale
    v = dy // scale
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
    u %= prime
    v %= prime
    if u:
        inverse = pow(u, -1, prime)
        return 1, (v * inverse) % prime
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


def greedy_fractional_packing(candidates, rng, denominator=12):
    residual = defaultdict(lambda: Fraction(1))
    weights = [Fraction(0) for _ in candidates]
    order = list(range(len(candidates)))
    rng.shuffle(order)
    for index in order:
        prescription = candidates[index][1]
        available = min(residual[edge] for edge in prescription)
        if available <= 0:
            continue
        if rng.random() < 0.7:
            value = available
        else:
            units = max(1, int(available * denominator))
            value = min(available, Fraction(rng.randint(1, units), denominator))
        weights[index] = value
        for edge in prescription:
            residual[edge] -= value
    for edge in {
        edge
        for _triple, prescription, _owner, _partners in candidates
        for edge in prescription
    }:
        assert sum(
            weights[index]
            for index, candidate in enumerate(candidates)
            if edge in candidate[1]
        ) <= 1
    return tuple(weights)


def check_packed_signature_extraction():
    rng = random.Random(1424)
    banks = 0
    candidates_checked = 0
    positive_threshold_banks = 0
    signature_classes = 0
    translated_classes = 0

    for side, prime, repetitions in ((5, 5, 100), (7, 7, 40)):
        opposite = matching(tuple(range(side)))
        derangements = [
            matching(value)
            for value in permutations(range(side))
            if all(value[index] != index for index in range(side))
        ]
        exponent = 1
        bands = 1 + int(log2(side - 1))
        class_stock = 2 * exponent * (prime + 1) * bands

        for _ in range(repetitions):
            current = rng.choice(derangements)
            target = rng.choice(tuple(current))
            candidates = candidate_family(side, opposite, current, target)
            weights = greedy_fractional_packing(candidates, rng)
            total_mass = sum(weights)

            class_mass = defaultdict(Fraction)
            owner_mass = defaultdict(Fraction)
            pair_mass = defaultdict(Fraction)
            response_partner_mass = defaultdict(Fraction)
            direction_mass = defaultdict(Fraction)
            displacement_mass = defaultdict(Fraction)

            for weight, candidate in zip(weights, candidates):
                if not weight:
                    continue
                _triple, _prescription, owner, partners = candidate
                owner_mass[owner] += 2 * weight
                for partner in partners:
                    key = signature(owner, partner, opposite, prime)
                    class_mass[key] += weight
                    pair_mass[(owner, partner)] += weight
                    if partner not in opposite:
                        response_partner_mass[partner] += weight
                    (
                        _scale,
                        u,
                        v,
                        _height,
                        signed_scale,
                    ) = primitive_data(owner, partner)
                    direction_mass[(key, (u, v))] += weight
                    displacement_mass[(key, (u, v), signed_scale)] += weight

            assert sum(class_mass.values()) == 2 * total_mass
            assert len(class_mass) <= class_stock
            if class_mass:
                assert max(class_mass.values()) * class_stock >= 2 * total_mass
            assert max(owner_mass.values(), default=Fraction(0)) <= 2
            assert max(pair_mass.values(), default=Fraction(0)) <= 1
            assert max(
                response_partner_mass.values(), default=Fraction(0)
            ) <= 1

            for key, mass in class_mass.items():
                _partner_type, depth, _theta, band = key
                directions = [
                    value
                    for (candidate_key, _direction), value in direction_mass.items()
                    if candidate_key == key
                ]
                direction_bound = direction_stock(prime, band)
                assert max(directions) * direction_bound >= mass

                scale_bound = floor((side - 1) / (prime**depth * band))
                assert scale_bound >= 1
                displacements = [
                    value
                    for (
                        candidate_key,
                        _direction,
                        _signed_scale,
                    ), value in displacement_mass.items()
                    if candidate_key == key
                ]
                assert (
                    max(displacements)
                    * direction_bound
                    * 2
                    * scale_bound
                    >= mass
                )
                signature_classes += 1
                translated_classes += len(displacements)

            if total_mass >= Fraction(side - 2, 3):
                positive_threshold_banks += 1
                heavy = max(class_mass.values())
                assert (
                    heavy
                    >= Fraction(side - 2, 3 * (prime + 1) * bands)
                )

            banks += 1
            candidates_checked += len(candidates)

    return (
        banks,
        candidates_checked,
        positive_threshold_banks,
        signature_classes,
        translated_classes,
    )


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
                    x, y = u, v
                    if x < 0 or (x == 0 and y < 0):
                        x, y = -x, -y
                    classes[projective_direction(x, y, prime)].add((x, y))
            actual = max((len(value) for value in classes.values()), default=0)
            assert actual <= direction_stock(prime, band)
            checks += 1
    return checks


def main():
    result = check_packed_signature_extraction()
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
