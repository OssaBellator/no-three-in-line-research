#!/usr/bin/env python3
"""Finite checks for CMR1398--CMR1405."""

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


def owner_loads(opposite, current, response):
    old = triples(set(opposite) | set(current))
    new = triples(set(opposite) | set(response)) - old
    entering = set(response) - set(current)
    loads = defaultdict(int)
    for triple in new:
        loads[min(edge for edge in triple if edge in entering)] += 1
    return loads


def harmonic_star(opposite, response, owner, eligible=None):
    if eligible is None:
        eligible = (set(opposite) | set(response)) - {owner}
    return sum(
        Fraction(1, primitive_height(owner, cell))
        for cell in eligible
        if owner[0] != cell[0] and owner[1] != cell[1]
    )


def check_line_capacity():
    checked = 0
    for side in range(2, 35):
        cells = [(row, column) for row in range(side) for column in range(side)]
        lines = defaultdict(set)
        for first, second in combinations(cells, 2):
            key = line_key(first, second)
            if key[0] == 0 or key[1] == 0:
                continue
            lines[key].add(first)
            lines[key].add(second)
        for members in lines.values():
            first, second = next(iter(combinations(tuple(members), 2)))
            height = primitive_height(first, second)
            assert len(members) <= 1 + (side - 1) // height
            checked += 1
    return checked


def check_realized_owner_bound():
    rng = random.Random(1399)
    checked = 0
    owners = 0
    for side in range(4, 8):
        all_matchings = [matching(value) for value in permutations(range(side))]
        for _ in range(350 if side <= 6 else 100):
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
                energy = harmonic_star(opposite, response, owner, eligible)
                assert loads.get(owner, 0) <= Fraction(side - 1, 2) * energy
                owners += 1
            checked += 1
    return checked, owners


def check_conditional_star_identity():
    rng = random.Random(1400)
    checked = 0
    edge_checks = 0
    for side in range(4, 7):
        all_matchings = [matching(value) for value in permutations(range(side))]
        for _ in range(120):
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
            star_total = defaultdict(Fraction)
            for response in bank:
                loads = owner_loads(opposite, current, response)
                for owner in response:
                    occurrence[owner] += 1
                    owner_total[owner] += loads.get(owner, 0)
                    star_total[owner] += harmonic_star(opposite, response, owner)
                for first, second in combinations(response, 2):
                    pair_occurrence[(first, second)] += 1
                    pair_occurrence[(second, first)] += 1
            for owner, count in occurrence.items():
                fixed = harmonic_star(opposite, frozenset({owner}), owner, set(opposite))
                response_part = Fraction(0)
                for other in occurrence:
                    if other == owner:
                        continue
                    if owner[0] == other[0] or owner[1] == other[1]:
                        continue
                    response_part += Fraction(
                        pair_occurrence.get((owner, other), 0),
                        count * primitive_height(owner, other),
                    )
                formula = fixed + response_part
                assert formula == star_total[owner] / count
                conditional_owner = Fraction(owner_total[owner], count)
                assert conditional_owner <= Fraction(side - 1, 2) * formula
                edge_checks += 1
            checked += 1
    return checked, edge_checks


def check_high_height_tail():
    rng = random.Random(1404)
    checked = 0
    for side in range(4, 50):
        cells = [(row, column) for row in range(side) for column in range(side)]
        for _ in range(500):
            owner = rng.choice(cells)
            others = rng.sample(
                [cell for cell in cells if cell != owner],
                min(2 * side - 1, len(cells) - 1),
            )
            threshold = rng.randint(1, side)
            tail = sum(
                Fraction(1, primitive_height(owner, cell))
                for cell in others
                if owner[0] != cell[0]
                and owner[1] != cell[1]
                and primitive_height(owner, cell) >= threshold
            )
            assert tail <= Fraction(2 * side - 1, threshold)
            checked += 1
    return checked


def main():
    realized = check_realized_owner_bound()
    conditional = check_conditional_star_identity()
    print(
        "verified harmonic owner bounds:",
        check_line_capacity(),
        "line capacities,",
        realized[0],
        "responses over",
        realized[1],
        "owner edges,",
        conditional[0],
        "conditional banks over",
        conditional[1],
        "edge stars, and",
        check_high_height_tail(),
        "high-height tails",
    )


if __name__ == "__main__":
    main()
