#!/usr/bin/env python3
"""Finite checks for CMR1390--CMR1397."""

from collections import Counter, defaultdict
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
        frozenset(value)
        for value in combinations(state, 3)
        if collinear(value)
    }


def choose(total, count):
    if count < 0 or count > total:
        return 0
    return comb(total, count)


def rook_parameters(side, prescription, target):
    rows = {row for row, _column in prescription}
    columns = {column for _row, column in prescription}
    surviving = {
        value for value in range(side) if value not in rows and value not in columns
    }
    epsilon = int(target[0] not in rows and target[1] not in columns)
    adjacent = 0
    if epsilon:
        adjacent += int(target[0] in surviving)
        adjacent += int(target[1] in surviving)
    return len(surviving), adjacent, epsilon


def rook_completion_count(side, prescription, target):
    rank = len(prescription)
    q, adjacent, epsilon = rook_parameters(side, prescription, target)
    total = 0
    for rooks in range(side - rank + 1):
        rook_number = choose(q, rooks)
        if epsilon:
            rook_number += choose(q - adjacent, rooks - 1)
        total += (-1) ** rooks * rook_number * factorial(side - rank - rooks)
    return total


def candidates(side, opposite, current, target):
    cells = {(row, column) for row in range(side) for column in range(side)}
    graph = cells - set(opposite) - {target}
    old_triples = physical_triples(set(opposite) | set(current))
    result = []
    for triple in combinations(set(opposite) | graph, 3):
        triple = frozenset(triple)
        if triple in old_triples or not collinear(tuple(triple)):
            continue
        prescription = frozenset(triple - set(opposite))
        if not prescription or not compatible(prescription):
            continue
        entering = prescription - set(current)
        if not entering:
            continue
        result.append((triple, prescription, min(entering)))
    return result


def direct_bank_owner_totals(opposite, current, bank):
    old_triples = physical_triples(set(opposite) | set(current))
    totals = defaultdict(int)
    occurrence = defaultdict(int)
    total_new = 0
    for response in bank:
        entering = set(response) - set(current)
        new_triples = physical_triples(set(opposite) | set(response)) - old_triples
        total_new += len(new_triples)
        for edge in response:
            occurrence[edge] += 1
        for triple in new_triples:
            totals[min(edge for edge in triple if edge in entering)] += 1
    return totals, occurrence, total_new


def check_owner_class_formula():
    rng = random.Random(1392)
    checked = 0
    candidate_total = 0
    owner_classes = set()
    for side in range(4, 7):
        opposite = matching(tuple(range(side)))
        all_matchings = [matching(value) for value in permutations(range(side))]
        derangements = [state for state in all_matchings if state.isdisjoint(opposite)]
        for _ in range(160):
            current = rng.choice(derangements)
            target = rng.choice(tuple(current))
            bank = [state for state in derangements if target not in state]
            direct, occurrence, direct_new = direct_bank_owner_totals(
                opposite, current, bank
            )
            formula = defaultdict(int)
            class_counts = Counter()
            for _triple, prescription, owner in candidates(
                side, opposite, current, target
            ):
                completions = rook_completion_count(side, prescription, target)
                formula[owner] += completions
                q, adjacent, epsilon = rook_parameters(
                    side, prescription, target
                )
                class_counts[(owner, len(prescription), q, adjacent, epsilon)] += 1
                owner_classes.add(
                    (side, len(prescription), q, adjacent, epsilon)
                )
                candidate_total += 1
            assert dict(formula) == dict(direct)
            assert sum(formula.values()) == direct_new
            for owner, numerator in formula.items():
                marginal_count = rook_completion_count(
                    side, frozenset({owner}), target
                )
                assert marginal_count == occurrence[owner]
                closed_weight = Fraction(numerator, marginal_count)
                direct_weight = Fraction(direct[owner], occurrence[owner])
                assert closed_weight == direct_weight
            checked += 1
    return checked, candidate_total, len(owner_classes)


def check_fixed_owner_independence():
    rng = random.Random(1391)
    checked = 0
    occurrences = 0
    for side in range(4, 7):
        opposite = matching(tuple(range(side)))
        all_matchings = [matching(value) for value in permutations(range(side))]
        derangements = [state for state in all_matchings if state.isdisjoint(opposite)]
        for _ in range(120):
            current = rng.choice(derangements)
            target = rng.choice(tuple(current))
            bank = [state for state in derangements if target not in state]
            candidate_list = candidates(side, opposite, current, target)
            for triple, prescription, owner in rng.sample(
                candidate_list, min(80, len(candidate_list))
            ):
                containing = [state for state in bank if prescription <= state]
                assert len(containing) == rook_completion_count(
                    side, prescription, target
                )
                for response in containing:
                    entering = set(response) - set(current)
                    assert owner == min(edge for edge in triple if edge in entering)
                    occurrences += 1
                checked += 1
    return checked, occurrences


def check_assignment_reconstruction():
    rng = random.Random(1395)
    checked = 0
    for side in range(4, 7):
        opposite = matching(tuple(range(side)))
        all_matchings = [matching(value) for value in permutations(range(side))]
        derangements = [state for state in all_matchings if state.isdisjoint(opposite)]
        for _ in range(140):
            current = rng.choice(derangements)
            target = rng.choice(tuple(current))
            bank = [state for state in derangements if target not in state]
            direct, occurrence, total_new = direct_bank_owner_totals(
                opposite, current, bank
            )
            edge_weights = {
                edge: Fraction(direct.get(edge, 0), count)
                for edge, count in occurrence.items()
            }
            edge_probabilities = {
                edge: Fraction(count, len(bank))
                for edge, count in occurrence.items()
            }
            expectation = sum(
                edge_probabilities[edge] * edge_weights[edge]
                for edge in edge_probabilities
            )
            assert expectation == Fraction(total_new, len(bank))
            row_dual = sum(
                max(
                    edge_weights.get((row, column), Fraction(0))
                    for column in range(side)
                )
                for row in range(side)
            )
            assert expectation <= row_dual
            checked += 1
    return checked


def main():
    classes = check_owner_class_formula()
    fixed = check_fixed_owner_independence()
    print(
        "verified rook owner edge weights:",
        classes[0],
        "banks with",
        classes[1],
        "candidate triples across",
        classes[2],
        "rook classes,",
        fixed[0],
        "fixed-owner candidates over",
        fixed[1],
        "realized occurrences, and",
        check_assignment_reconstruction(),
        "assignment reconstructions",
    )


if __name__ == "__main__":
    main()
