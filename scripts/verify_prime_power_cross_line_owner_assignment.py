#!/usr/bin/env python3
"""Finite checks for CMR1382--CMR1389."""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import gcd
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


def direct_owner_loads(opposite, current, response):
    old_triples = triples(set(opposite) | set(current))
    new_triples = triples(set(opposite) | set(response)) - old_triples
    entering = set(response) - set(current)
    loads = defaultdict(int)
    for triple in new_triples:
        owner = min(edge for edge in triple if edge in entering)
        loads[owner] += 1
    return new_triples, loads


def line_owner_loads(opposite, current, response):
    entering = set(response) - set(current)
    loads = defaultdict(int)
    current_state = set(opposite) | set(response)
    for owner in entering:
        earlier = {edge for edge in entering if edge < owner}
        eligible = current_state - {owner} - earlier
        line_populations = defaultdict(int)
        for cell in eligible:
            key = line_key(owner, cell)
            if key[0] == 0 or key[1] == 0:
                continue
            line_populations[key] += 1
        loads[owner] = sum(
            population * (population - 1) // 2
            for population in line_populations.values()
        )
    return loads


def bank_for(opposite, target, all_matchings):
    return [
        state
        for state in all_matchings
        if state.isdisjoint(opposite) and target not in state
    ]


def conditional_owner_weights(opposite, current, bank):
    occurrence = defaultdict(int)
    owner_total = defaultdict(int)
    direct_total = 0
    for response in bank:
        new_triples, loads = direct_owner_loads(opposite, current, response)
        direct_total += len(new_triples)
        for edge in response:
            occurrence[edge] += 1
            owner_total[edge] += loads.get(edge, 0)
    probability = {
        edge: Fraction(count, len(bank)) for edge, count in occurrence.items()
    }
    conditional = {
        edge: Fraction(owner_total[edge], count)
        for edge, count in occurrence.items()
    }
    expectation = Fraction(direct_total, len(bank))
    return probability, conditional, expectation


def check_owner_line_formula():
    rng = random.Random(1382)
    checked = 0
    owned_triples = 0
    for side in range(4, 8):
        all_matchings = [matching(value) for value in permutations(range(side))]
        samples = 250 if side <= 6 else 80
        for _ in range(samples):
            opposite = rng.choice(all_matchings)
            disjoint = [state for state in all_matchings if state.isdisjoint(opposite)]
            current = rng.choice(disjoint)
            target = rng.choice(tuple(current))
            bank = bank_for(opposite, target, all_matchings)
            response = rng.choice(bank)
            new_triples, direct = direct_owner_loads(opposite, current, response)
            linewise = line_owner_loads(opposite, current, response)
            assert dict(direct) == dict(linewise)
            assert sum(direct.values()) == len(new_triples)
            owned_triples += len(new_triples)
            checked += 1
    return checked, owned_triples


def check_exact_assignment_identity():
    rng = random.Random(1384)
    checked = 0
    exact_credits = 0
    for side in range(4, 7):
        all_matchings = [matching(value) for value in permutations(range(side))]
        for _ in range(180):
            opposite = rng.choice(all_matchings)
            disjoint = [state for state in all_matchings if state.isdisjoint(opposite)]
            current = rng.choice(disjoint)
            target = rng.choice(tuple(current))
            bank = bank_for(opposite, target, all_matchings)
            probability, conditional, expectation = conditional_owner_weights(
                opposite, current, bank
            )
            assignment_value = sum(
                probability[edge] * conditional[edge] for edge in probability
            )
            assert assignment_value == expectation
            for row in range(side):
                assert sum(
                    probability.get((row, column), Fraction(0))
                    for column in range(side)
                ) == 1
            for column in range(side):
                assert sum(
                    probability.get((row, column), Fraction(0))
                    for row in range(side)
                ) == 1
            maximum = max(
                sum(conditional.get(edge, Fraction(0)) for edge in response)
                for response in bank
            )
            assert expectation <= maximum
            exact_credits += expectation.numerator
            checked += 1
    return checked, exact_credits


def check_dual_certificates():
    rng = random.Random(1387)
    checked = 0
    integer_checks = 0
    for side in range(4, 7):
        all_matchings = [matching(value) for value in permutations(range(side))]
        for _ in range(150):
            opposite = rng.choice(all_matchings)
            disjoint = [state for state in all_matchings if state.isdisjoint(opposite)]
            current = rng.choice(disjoint)
            target = rng.choice(tuple(current))
            bank = bank_for(opposite, target, all_matchings)
            probability, conditional, expectation = conditional_owner_weights(
                opposite, current, bank
            )
            alpha = {}
            for row in range(side):
                alpha[row] = max(
                    (
                        conditional.get((row, column), Fraction(0))
                        for column in range(side)
                        if (row, column) in probability
                    ),
                    default=Fraction(0),
                )
            beta = {column: Fraction(0) for column in range(side)}
            for edge, weight in conditional.items():
                assert alpha[edge[0]] + beta[edge[1]] >= weight
            dual = sum(alpha.values()) + sum(beta.values())
            assert expectation <= dual

            denominators = [value.denominator for value in conditional.values()]
            denominators += [value.denominator for value in alpha.values()]
            common = 1
            for denominator in denominators:
                # The product is intentionally coarse but exact for this verifier.
                common *= denominator
            for edge, weight in conditional.items():
                left = common * (alpha[edge[0]] + beta[edge[1]])
                right = common * weight
                assert left.denominator == 1 and right.denominator == 1
                assert left >= right
                integer_checks += 1
            checked += 1
    return checked, integer_checks


def check_random_weight_assignment():
    rng = random.Random(1386)
    checked = 0
    for side in range(3, 9):
        all_matchings = [matching(value) for value in permutations(range(side))]
        for _ in range(300):
            family = rng.sample(all_matchings, rng.randint(1, min(80, len(all_matchings))))
            probability = defaultdict(Fraction)
            masses = [rng.randint(1, 20) for _state in family]
            denominator = sum(masses)
            for state, mass in zip(family, masses):
                for edge in state:
                    probability[edge] += Fraction(mass, denominator)
            weights = {
                (row, column): Fraction(rng.randint(0, 100), rng.randint(1, 20))
                for row in range(side)
                for column in range(side)
            }
            expected = sum(probability[edge] * weights[edge] for edge in probability)
            maximum = max(sum(weights[edge] for edge in state) for state in family)
            assert expected <= maximum
            checked += 1
    return checked


def main():
    linewise = check_owner_line_formula()
    exact = check_exact_assignment_identity()
    dual = check_dual_certificates()
    print(
        "verified cross-line owner assignment:",
        linewise[0],
        "response states with",
        linewise[1],
        "owned triples,",
        exact[0],
        "exact bank assignments,",
        dual[0],
        "dual certificates with",
        dual[1],
        "integer edge inequalities, and",
        check_random_weight_assignment(),
        "random convex assignment cases",
    )


if __name__ == "__main__":
    main()
