#!/usr/bin/env python3
"""Finite checks for CMR1406--CMR1413."""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import gcd
import random


def matching(permutation):
    return frozenset((row, permutation[row]) for row in range(len(permutation)))


def primitive_height(first, second):
    dx = second[0] - first[0]
    dy = second[1] - first[1]
    divisor = gcd(abs(dx), abs(dy))
    return max(abs(dx // divisor), abs(dy // divisor))


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


def triples(state):
    return {
        frozenset(value)
        for value in combinations(state, 3)
        if collinear(value)
    }


def capacity(side, height):
    return max((side - 1) // height - 1, 0)


def owner_loads(opposite, current, response):
    old = triples(set(opposite) | set(current))
    new = triples(set(opposite) | set(response)) - old
    entering = set(response) - set(current)
    loads = defaultdict(int)
    for triple in new:
        loads[min(edge for edge in triple if edge in entering)] += 1
    return loads


def capacity_star(opposite, response, owner, eligible=None):
    if eligible is None:
        eligible = (set(opposite) | set(response)) - {owner}
    side = len(opposite)
    return sum(
        capacity(side, primitive_height(owner, cell))
        for cell in eligible
        if owner[0] != cell[0] and owner[1] != cell[1]
    )


def harmonic_star(opposite, response, owner, eligible=None):
    if eligible is None:
        eligible = (set(opposite) | set(response)) - {owner}
    return sum(
        Fraction(1, primitive_height(owner, cell))
        for cell in eligible
        if owner[0] != cell[0] and owner[1] != cell[1]
    )


def check_scalar_capacity():
    checked = 0
    for side in range(2, 1000):
        for height in range(1, side):
            q = (side - 1) // height
            populations = {0, 1, q}
            if q >= 2:
                populations.add(q // 2)
            for population in populations:
                assert Fraction(population * (population - 1), 2) <= Fraction(
                    (q - 1) * population, 2
                )
                checked += 1
            assert Fraction(capacity(side, height), 2) <= Fraction(
                side - 1, 2 * height
            )
            if 2 * height > side - 1:
                assert capacity(side, height) == 0
    return checked


def check_realized_capacity_bound():
    rng = random.Random(1407)
    checked = 0
    owners = 0
    strict_improvements = 0
    for side in range(4, 8):
        all_matchings = [matching(value) for value in permutations(range(side))]
        for _ in range(300 if side <= 6 else 80):
            opposite = rng.choice(all_matchings)
            current = rng.choice(
                [state for state in all_matchings if state.isdisjoint(opposite)]
            )
            target = rng.choice(tuple(current))
            bank = [
                state
                for state in all_matchings
                if state.isdisjoint(opposite) and target not in state
            ]
            response = rng.choice(bank)
            entering = set(response) - set(current)
            loads = owner_loads(opposite, current, response)
            state = set(opposite) | set(response)
            for owner in entering:
                eligible = state - {owner} - {edge for edge in entering if edge < owner}
                cap_bound = Fraction(
                    capacity_star(opposite, response, owner, eligible), 2
                )
                harm_bound = Fraction(side - 1, 2) * harmonic_star(
                    opposite, response, owner, eligible
                )
                assert loads.get(owner, 0) <= cap_bound <= harm_bound
                strict_improvements += int(cap_bound < harm_bound)
                owners += 1
            checked += 1
    return checked, owners, strict_improvements


def check_conditional_capacity_identity():
    rng = random.Random(1408)
    checked = 0
    edge_checks = 0
    for side in range(4, 7):
        all_matchings = [matching(value) for value in permutations(range(side))]
        for _ in range(100):
            opposite = rng.choice(all_matchings)
            current = rng.choice(
                [state for state in all_matchings if state.isdisjoint(opposite)]
            )
            target = rng.choice(tuple(current))
            bank = [
                state
                for state in all_matchings
                if state.isdisjoint(opposite) and target not in state
            ]
            occurrence = defaultdict(int)
            pair_occurrence = defaultdict(int)
            owner_total = defaultdict(int)
            capacity_total = defaultdict(int)
            for response in bank:
                loads = owner_loads(opposite, current, response)
                for owner in response:
                    occurrence[owner] += 1
                    owner_total[owner] += loads.get(owner, 0)
                    capacity_total[owner] += capacity_star(opposite, response, owner)
                for first, second in combinations(response, 2):
                    pair_occurrence[(first, second)] += 1
                    pair_occurrence[(second, first)] += 1
            for owner, count in occurrence.items():
                fixed = capacity_star(
                    opposite, frozenset({owner}), owner, set(opposite)
                )
                response_part = Fraction(0)
                for other in occurrence:
                    if other == owner:
                        continue
                    if owner[0] == other[0] or owner[1] == other[1]:
                        continue
                    response_part += Fraction(
                        pair_occurrence.get((owner, other), 0)
                        * capacity(side, primitive_height(owner, other)),
                        count,
                    )
                formula = Fraction(fixed) + response_part
                assert formula == Fraction(capacity_total[owner], count)
                assert Fraction(owner_total[owner], count) <= formula / 2
                edge_checks += 1
            checked += 1
    return checked, edge_checks


def check_dyadic_band_maxima():
    rng = random.Random(1413)
    checked = 0
    for side in range(3, 10000):
        height = 1
        while height <= side - 1:
            upper = min(2 * height, side)
            coefficient = capacity(side, height)
            candidates = {height, upper - 1}
            if upper - height > 2:
                candidates.add(rng.randrange(height, upper))
            for actual in candidates:
                assert capacity(side, actual) <= coefficient
                checked += 1
            height *= 2
    return checked


def main():
    realized = check_realized_capacity_bound()
    conditional = check_conditional_capacity_identity()
    print(
        "verified lattice-capacity owner envelope:",
        check_scalar_capacity(),
        "scalar inequalities,",
        realized[0],
        "responses over",
        realized[1],
        "owners with",
        realized[2],
        "strict improvements over the harmonic coefficient,",
        conditional[0],
        "conditional banks over",
        conditional[1],
        "edge weights, and",
        check_dyadic_band_maxima(),
        "dyadic coefficient checks",
    )


if __name__ == "__main__":
    main()
