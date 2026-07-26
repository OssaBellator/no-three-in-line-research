#!/usr/bin/env python3
"""Finite checks for CMR1374--CMR1381."""

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial, gcd
import random


def matching(permutation):
    return frozenset((row, permutation[row]) for row in range(len(permutation)))


def compatible(edges):
    return (
        len({row for row, _column in edges}) == len(edges)
        and len({column for _row, column in edges}) == len(edges)
    )


def derangement_number(side):
    values = [0] * (side + 1)
    values[0] = 1
    if side:
        values[1] = 0
    for value in range(2, side + 1):
        values[value] = (value - 1) * (values[value - 1] + values[value - 2])
    return values[side]


def rook_parameters(side, prescription, target=(0, 1)):
    rows = {row for row, _column in prescription}
    columns = {column for _row, column in prescription}
    surviving_diagonal = {
        value for value in range(side) if value not in rows and value not in columns
    }
    epsilon = int(target[0] not in rows and target[1] not in columns)
    adjacent = 0
    if epsilon:
        adjacent += int(target[0] in surviving_diagonal)
        adjacent += int(target[1] in surviving_diagonal)
    return len(surviving_diagonal), adjacent, epsilon


def choose(total, count):
    if count < 0 or count > total:
        return 0
    return comb(total, count)


def rook_completion_count(side, prescription, target=(0, 1)):
    rank = len(prescription)
    q, adjacent, epsilon = rook_parameters(side, prescription, target)
    total = 0
    for rooks in range(side - rank + 1):
        rook_number = choose(q, rooks)
        if epsilon:
            rook_number += choose(q - adjacent, rooks - 1)
        total += (-1) ** rooks * rook_number * factorial(side - rank - rooks)
    return total


def brute_completion_count(side, prescription, target=(0, 1)):
    total = 0
    for permutation in permutations(range(side)):
        if any(permutation[row] == row for row in range(side)):
            continue
        if permutation[target[0]] == target[1]:
            continue
        if all(permutation[row] == column for row, column in prescription):
            total += 1
    return total


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


def physical_triples(state):
    return {
        frozenset(triple)
        for triple in combinations(state, 3)
        if collinear(triple)
    }


def check_rook_counts():
    rng = random.Random(1375)
    checked = 0
    parameter_classes = set()
    for side in range(4, 8):
        target = (0, 1)
        edges = [
            (row, column)
            for row in range(side)
            for column in range(side)
            if row != column and (row, column) != target
        ]
        for rank in (1, 2, 3):
            prescriptions = [
                frozenset(value)
                for value in combinations(edges, rank)
                if compatible(value)
            ]
            if side >= 6:
                prescriptions = rng.sample(
                    prescriptions, min(1200, len(prescriptions))
                )
            for prescription in prescriptions:
                exact = rook_completion_count(side, prescription, target)
                brute = brute_completion_count(side, prescription, target)
                assert exact == brute
                q, adjacent, epsilon = rook_parameters(side, prescription, target)
                parameter_classes.add((side, rank, q, adjacent, epsilon, exact))
                checked += 1
    return checked, len(parameter_classes)


def check_probability_bounds():
    rng = random.Random(1378)
    checked = 0
    exact_classes = set()
    for side in range(4, 10):
        target = (0, 1)
        bank_size = derangement_number(side) * (side - 2) // (side - 1)
        lambda_value = Fraction(
            factorial(side) * (side - 1),
            derangement_number(side) * (side - 2),
        )
        edges = [
            (row, column)
            for row in range(side)
            for column in range(side)
            if row != column and (row, column) != target
        ]
        for rank in (1, 2, 3):
            candidates = []
            for _ in range(2500):
                rng.shuffle(edges)
                prescription = []
                for edge in edges:
                    if all(
                        edge[0] != old[0] and edge[1] != old[1]
                        for old in prescription
                    ):
                        prescription.append(edge)
                        if len(prescription) == rank:
                            break
                candidates.append(frozenset(prescription))
            for prescription in candidates:
                numerator = rook_completion_count(side, prescription, target)
                probability = Fraction(numerator, bank_size)
                q, adjacent, epsilon = rook_parameters(side, prescription, target)
                exact_classes.add((side, rank, q, adjacent, epsilon, probability))
                if rank == 1:
                    assert probability <= Fraction(1, side - 2)
                else:
                    falling = factorial(side) // factorial(side - rank)
                    assert probability <= lambda_value / falling
                checked += 1
    return checked, len(exact_classes)


def check_exact_expected_collateral():
    rng = random.Random(1379)
    checked = 0
    candidates_counted = 0
    for side in range(4, 7):
        identity = matching(tuple(range(side)))
        all_matchings = [matching(value) for value in permutations(range(side))]
        derangements = [state for state in all_matchings if state.isdisjoint(identity)]
        pairs = []
        for _ in range(80):
            current = rng.choice(derangements)
            target = rng.choice(tuple(current))
            pairs.append((current, target))
        old_triples_cache = {}
        for current, target in pairs:
            bank = [state for state in derangements if target not in state]
            old_state = set(identity) | set(current)
            old_triples = old_triples_cache.setdefault(
                current, physical_triples(old_state)
            )
            direct_total = 0
            class_counts = Counter()
            for response in bank:
                new_triples = physical_triples(set(identity) | set(response)) - old_triples
                direct_total += len(new_triples)
            cells = {
                (row, column)
                for row in range(side)
                for column in range(side)
            }
            graph = cells - set(identity) - {target}
            for triple in combinations(set(identity) | graph, 3):
                triple_set = frozenset(triple)
                if triple_set in old_triples or not collinear(triple):
                    continue
                prescription = frozenset(triple_set - set(identity))
                if not prescription or not compatible(prescription):
                    continue
                q, adjacent, epsilon = rook_parameters(
                    side, prescription, target
                )
                class_counts[(len(prescription), q, adjacent, epsilon)] += 1
                candidates_counted += 1
            formula_total = 0
            for (rank, q, adjacent, epsilon), count in class_counts.items():
                representative = None
                for prescription in combinations(graph, rank):
                    prescription = frozenset(prescription)
                    if not compatible(prescription):
                        continue
                    if rook_parameters(side, prescription, target) == (
                        q,
                        adjacent,
                        epsilon,
                    ):
                        representative = prescription
                        break
                assert representative is not None
                formula_total += count * rook_completion_count(
                    side, representative, target
                )
            assert formula_total == direct_total
            checked += 1
    return checked, candidates_counted


def check_unavailable_edge_identity():
    rng = random.Random(1380)
    checked = 0
    for side in range(4, 8):
        identity = matching(tuple(range(side)))
        all_matchings = [matching(value) for value in permutations(range(side))]
        nonidentity = {
            (row, column)
            for row in range(side)
            for column in range(side)
            if row != column
        }
        for _ in range(100):
            target = rng.choice(tuple(nonidentity))
            bank = [
                state
                for state in all_matchings
                if state.isdisjoint(identity) and target not in state
            ]
            allowed = tuple(nonidentity - {target})
            unavailable = set(rng.sample(allowed, rng.randint(0, len(allowed))))
            direct = Fraction(
                sum(len(state & unavailable) for state in bank), len(bank)
            )
            marginal = Fraction(0)
            for edge in unavailable:
                numerator = rook_completion_count(side, frozenset({edge}), target)
                marginal += Fraction(numerator, len(bank))
            assert direct == marginal
            checked += 1
    return checked


def main():
    rook = check_rook_counts()
    bounds = check_probability_bounds()
    expected = check_exact_expected_collateral()
    print(
        "verified extension-free rook probabilities:",
        rook[0],
        "exact completion counts across",
        rook[1],
        "parameter classes,",
        bounds[0],
        "probability bounds across",
        bounds[1],
        "exact classes,",
        expected[0],
        "exact collateral expectations with",
        expected[1],
        "candidate triples, and",
        check_unavailable_edge_identity(),
        "unavailable-edge identities",
    )


if __name__ == "__main__":
    main()
