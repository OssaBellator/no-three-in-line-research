#!/usr/bin/env python3
"""Finite checks for CMR1382--CMR1389."""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import gcd
import random


def matching(permutation):
    return frozenset((row, permutation[row]) for row in range(len(permutation)))


def compatible(prescription):
    return (
        len({row for row, _column in prescription}) == len(prescription)
        and len({column for _row, column in prescription}) == len(prescription)
    )


def true_cost(response, candidates, weights):
    return sum(
        weights[index]
        for index, prescription in enumerate(candidates)
        if prescription <= response
    )


def selector_loads(candidates, weights, selector):
    loads = defaultdict(int)
    for index, edge in enumerate(selector):
        assert edge in candidates[index]
        loads[edge] += weights[index]
    return loads


def assignment_cost(response, loads):
    return sum(loads[edge] for edge in response)


def selector_from_optimum(candidates, optimum):
    selector = []
    for prescription in candidates:
        outside = tuple(prescription - optimum)
        selector.append(outside[0] if outside else tuple(prescription)[0])
    return selector


def random_host_system(rng, side):
    all_matchings = [matching(value) for value in permutations(range(side))]
    retained = rng.sample(all_matchings, rng.randint(1, min(len(all_matchings), 25)))
    host_edges = frozenset().union(*retained)
    responses = [state for state in all_matchings if state <= host_edges]
    assert responses

    prescriptions = set()
    for _ in range(rng.randint(1, 35)):
        witness = rng.choice(responses)
        rank = rng.randint(1, min(3, side))
        prescriptions.add(frozenset(rng.sample(tuple(witness), rank)))
    candidates = tuple(prescriptions)
    weights = tuple(rng.randint(1, 11) for _ in candidates)
    return responses, candidates, weights


def check_selector_equality():
    rng = random.Random(1384)
    systems = 0
    responses_checked = 0
    candidate_count = 0

    for side in range(2, 7):
        for _ in range(350):
            responses, candidates, weights = random_host_system(rng, side)
            costs = [true_cost(state, candidates, weights) for state in responses]
            optimum_value = min(costs)
            optimum = responses[costs.index(optimum_value)]

            selector = selector_from_optimum(candidates, optimum)
            loads = selector_loads(candidates, weights, selector)
            assignment_values = [assignment_cost(state, loads) for state in responses]
            assert min(assignment_values) == optimum_value
            assert assignment_cost(optimum, loads) == optimum_value

            for state, assignment in zip(responses, assignment_values):
                assert true_cost(state, candidates, weights) <= assignment

            for _trial in range(8):
                random_selector = [rng.choice(tuple(value)) for value in candidates]
                random_loads = selector_loads(candidates, weights, random_selector)
                assert min(
                    assignment_cost(state, random_loads) for state in responses
                ) >= optimum_value

            systems += 1
            responses_checked += len(responses)
            candidate_count += len(candidates)

    return systems, responses_checked, candidate_count


def fractional_coordinates(responses, coefficients):
    coordinates = defaultdict(Fraction)
    for coefficient, response in zip(coefficients, responses):
        for edge in response:
            coordinates[edge] += coefficient
    return coordinates


def fractional_function(coordinates, candidates, weights):
    return sum(
        weights[index] * min(coordinates[edge] for edge in prescription)
        for index, prescription in enumerate(candidates)
    )


def check_fractional_form():
    rng = random.Random(1385)
    systems = 0
    mixtures = 0

    for side in range(2, 7):
        for _ in range(250):
            responses, candidates, weights = random_host_system(rng, side)
            optimum = min(true_cost(state, candidates, weights) for state in responses)

            optimum_states = [
                state
                for state in responses
                if true_cost(state, candidates, weights) == optimum
            ]
            incidence = {edge: Fraction(1) for edge in optimum_states[0]}
            assert fractional_function(incidence, candidates, weights) == optimum

            sample = rng.sample(responses, min(len(responses), rng.randint(1, 8)))
            raw = [rng.randint(1, 20) for _ in sample]
            total = sum(raw)
            coefficients = [Fraction(value, total) for value in raw]
            coordinates = fractional_coordinates(sample, coefficients)
            value = fractional_function(coordinates, candidates, weights)
            assert value >= optimum

            minimizing_selector = [
                min(prescription, key=lambda edge: coordinates[edge])
                for prescription in candidates
            ]
            loads = selector_loads(candidates, weights, minimizing_selector)
            selector_average = sum(
                coordinates[edge] * load for edge, load in loads.items()
            )
            assert selector_average == value

            # Birkhoff averaging supplies one sampled response no more expensive than
            # the selector average.
            sampled_assignment_average = sum(
                coefficient * assignment_cost(response, loads)
                for coefficient, response in zip(coefficients, sample)
            )
            assert sampled_assignment_average == selector_average
            assert min(assignment_cost(response, loads) for response in sample) <= value

            systems += 1
            mixtures += len(sample)

    return systems, mixtures


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
        for value in combinations(tuple(state), 3)
        if collinear(value)
    }


def geometric_candidates(side, fixed, old, omitted_edge):
    cells = {
        (row, column)
        for row in range(side)
        for column in range(side)
    }
    graph = cells - set(fixed) - {omitted_edge}
    old_state = fixed | old
    result = []
    for value in combinations(tuple(set(fixed) | graph), 3):
        target = frozenset(value)
        if target <= old_state or not collinear(value):
            continue
        prescription = frozenset(target - set(fixed))
        if prescription and compatible(prescription):
            result.append(prescription)
    return tuple(result)


def check_side_five_witness():
    side = 5
    old = matching((0, 1, 2, 4, 3))
    fixed = matching((1, 3, 4, 0, 2))
    edge = (0, 0)
    response = matching((4, 1, 0, 2, 3))
    all_matchings = [matching(value) for value in permutations(range(side))]
    bank = [
        state
        for state in all_matchings
        if state.isdisjoint(fixed) and edge not in state
    ]
    assert response in bank

    old_targets = triples(fixed | old)
    response_targets = triples(fixed | response)
    assert len(response_targets - old_targets) == 0
    assert len(old_targets - response_targets) == 2

    candidates = geometric_candidates(side, fixed, old, edge)
    weights = tuple(1 for _ in candidates)
    selector = selector_from_optimum(candidates, response)
    loads = selector_loads(candidates, weights, selector)
    assert assignment_cost(response, loads) == 0
    assert min(assignment_cost(state, loads) for state in bank) == 0
    assert min(true_cost(state, candidates, weights) for state in bank) == 0
    return len(bank), len(candidates), len(old_targets)


def main():
    selectors = check_selector_equality()
    fractional = check_fractional_form()
    witness = check_side_five_witness()
    print(
        "verified cross-line edge assignment:",
        selectors[0],
        "weighted systems over",
        selectors[1],
        "response states and",
        selectors[2],
        "candidate prescriptions,",
        fractional[0],
        "fractional systems with",
        fractional[1],
        "mixture terms, and side-five witness",
        witness,
    )


if __name__ == "__main__":
    main()
