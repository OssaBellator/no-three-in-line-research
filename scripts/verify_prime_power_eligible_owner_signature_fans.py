#!/usr/bin/env python3
"""Finite checks for CMR1414--CMR1421."""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import ceil, gcd, log2
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


def triples(state):
    return {
        frozenset(value)
        for value in combinations(state, 3)
        if collinear(value)
    }


def primitive_data(first, second):
    dx = second[0] - first[0]
    dy = second[1] - first[1]
    scale = gcd(abs(dx), abs(dy))
    u = dx // scale
    v = dy // scale
    if u < 0 or (u == 0 and v < 0):
        u, v = -u, -v
    return scale, u, v, max(abs(u), abs(v))


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


def signature(owner, partner, partner_type, prime):
    scale, u, v, height = primitive_data(owner, partner)
    return (
        partner_type,
        valuation(scale, prime),
        projective_direction(u, v, prime),
        1 << int(log2(height)),
    )


def capacity(side, height):
    return max((side - 1) // height - 1, 0)


def eligible(owner, partner, current):
    return partner in current or owner < partner


def owner_loads(opposite, current, response):
    old = triples(set(opposite) | set(current))
    new = triples(set(opposite) | set(response)) - old
    entering = set(response) - set(current)
    loads = defaultdict(int)
    for triple in new:
        loads[min(edge for edge in triple if edge in entering)] += 1
    return loads


def selected_signature_counts(opposite, current, response, owner, prime):
    counts = Counter()
    for partner in opposite:
        if owner[0] != partner[0] and owner[1] != partner[1]:
            counts[signature(owner, partner, "fixed", prime)] += 1
    for partner in response - {owner}:
        if eligible(owner, partner, current):
            if owner[0] != partner[0] and owner[1] != partner[1]:
                counts[signature(owner, partner, "response", prime)] += 1
    return counts


def exact_eligible_capacity(opposite, current, response, owner):
    total = 0
    for partner in opposite:
        if owner[0] != partner[0] and owner[1] != partner[1]:
            total += capacity(len(opposite), primitive_data(owner, partner)[3])
    for partner in response - {owner}:
        if eligible(owner, partner, current):
            if owner[0] != partner[0] and owner[1] != partner[1]:
                total += capacity(len(opposite), primitive_data(owner, partner)[3])
    return total


def check_full_banks():
    rng = random.Random(1417)
    checked = 0
    edge_classes = 0
    simultaneous = 0
    for side, prime in ((5, 5), (7, 7)):
        all_matchings = [matching(value) for value in permutations(range(side))]
        opposite = matching(tuple(range(side)))
        derangements = [state for state in all_matchings if state.isdisjoint(opposite)]
        for _ in range(60 if side == 5 else 18):
            current = rng.choice(derangements)
            target = rng.choice(tuple(current))
            bank = [state for state in derangements if target not in state]
            occurrence = defaultdict(int)
            owner_total = defaultdict(int)
            capacity_total = defaultdict(int)
            class_total = defaultdict(Counter)
            class_maximum = defaultdict(Counter)
            for response in bank:
                loads = owner_loads(opposite, current, response)
                for owner in response - current:
                    occurrence[owner] += 1
                    owner_total[owner] += loads.get(owner, 0)
                    capacity_total[owner] += exact_eligible_capacity(
                        opposite, current, response, owner
                    )
                    counts = selected_signature_counts(
                        opposite, current, response, owner, prime
                    )
                    class_total[owner].update(counts)
                    for key, value in counts.items():
                        class_maximum[owner][key] = max(
                            class_maximum[owner][key], value
                        )
            bands = 1 + int(log2(side - 1))
            class_bound = 2 * (prime + 1) * bands
            for owner, count in occurrence.items():
                mean_capacity = Fraction(capacity_total[owner], count)
                assert Fraction(owner_total[owner], count) <= mean_capacity / 2
                assert len(class_total[owner]) <= class_bound
                upper = Fraction(0)
                for key, total in class_total[owner].items():
                    mean = Fraction(total, count)
                    upper += capacity(side, key[3]) * mean
                    assert class_maximum[owner][key] >= ceil(mean)
                    simultaneous += 1
                assert mean_capacity <= upper
                edge_classes += len(class_total[owner])
            checked += 1
    return checked, edge_classes, simultaneous


def random_derangement(side, rng):
    while True:
        value = list(range(side))
        rng.shuffle(value)
        if all(value[index] != index for index in range(side)):
            return matching(tuple(value))


def check_nontrivial_depths():
    rng = random.Random(1416)
    opposite = matching(tuple(range(9)))
    depths = set()
    classes = set()
    checked = 0
    for _ in range(180):
        current = random_derangement(9, rng)
        target = rng.choice(tuple(current))
        responses = []
        while len(responses) < 80:
            response = random_derangement(9, rng)
            if target not in response:
                responses.append(response)
        for response in responses:
            for owner in response - current:
                for key in selected_signature_counts(
                    opposite, current, response, owner, 3
                ):
                    depths.add(key[1])
                    classes.add(key)
                    assert 0 <= key[1] <= 1
                    checked += 1
    assert depths == {0, 1}
    return checked, len(classes)


def direction_count(prime, band):
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
    return max((len(value) for value in classes.values()), default=0)


def check_direction_and_concentration():
    rng = random.Random(1420)
    checked = 0
    for prime in (2, 3, 5, 7, 11, 13):
        for band in (1, 2, 4, 8, 16, 32, 64):
            actual = direction_count(prime, band)
            bound = (prime - 1) * ceil(4 * band / prime) ** 2
            assert actual <= bound
            if actual:
                population = [rng.randrange(actual) for _ in range(500)]
                assert max(Counter(population).values()) >= ceil(500 / bound)
            checked += 1
    return checked


def main():
    full = check_full_banks()
    depth = check_nontrivial_depths()
    print(
        "verified eligible owner signature fans:",
        full[0],
        "complete banks with",
        full[1],
        "entering-owner classes and",
        full[2],
        "simultaneous realizations,",
        depth[0],
        "side-nine signatures across",
        depth[1],
        "classes, and",
        check_direction_and_concentration(),
        "direction/concentration checks",
    )


if __name__ == "__main__":
    main()
