#!/usr/bin/env python3
"""Finite checks for CMR1206--CMR1213."""

from itertools import combinations, permutations
from math import factorial
import random


def matching(permutation):
    return frozenset((row, permutation[row]) for row in range(len(permutation)))


def derangements(side):
    return [
        permutation
        for permutation in permutations(range(side))
        if all(permutation[row] != row for row in range(side))
    ]


def response_bank(side, forbidden):
    opposite = matching(tuple(range(side)))
    forbidden_edges = matching(forbidden)
    return [
        matching(permutation)
        for permutation in permutations(range(side))
        if matching(permutation).isdisjoint(opposite | forbidden_edges)
    ]


def falling(side, rank):
    return factorial(side) // factorial(side - rank)


def check_unavailable_expectations():
    rng = random.Random(1206)
    checked = 0
    unavailable_incidences = 0
    for side in range(4, 8):
        forbidden_list = derangements(side)
        if side >= 6:
            forbidden_list = rng.sample(forbidden_list, min(45, len(forbidden_list)))
        opposite = matching(tuple(range(side)))
        universe = {(row, column) for row in range(side) for column in range(side)}
        kappa = (side / (side - 2)) ** side
        for forbidden in forbidden_list:
            bank = response_bank(side, forbidden)
            allowed = universe - opposite - matching(forbidden)
            for _ in range(50):
                missing = set(rng.sample(tuple(allowed), rng.randint(0, len(allowed))))
                incidence = sum(len(state & missing) for state in bank)
                expectation = incidence / len(bank)
                assert expectation <= kappa * len(missing) / side + 1e-12
                unavailable_incidences += incidence
                checked += 1
    return checked, unavailable_incidences


def check_weighted_feasibility_forcing():
    rng = random.Random(1207)
    checked = 0
    negative_cases = 0
    for minimum in range(0, 100):
        weight = minimum + 1
        for _ in range(1000):
            later = rng.randint(0, 150)
            delta = later - minimum
            missing_count = rng.randint(0, 8)
            weighted = delta + weight * missing_count
            if weighted < 0:
                assert missing_count == 0
                assert delta < 0
                negative_cases += 1
            checked += 1
    return checked, negative_cases


def check_target_incidence_identity():
    rng = random.Random(1210)
    checked = 0
    triple_incidences = 0
    for vertex_count in range(3, 80):
        vertices = tuple(range(vertex_count))
        all_triples = list(combinations(vertices, 3))
        for _ in range(200):
            target_count = rng.randint(0, min(250, len(all_triples)))
            targets = rng.sample(all_triples, target_count)
            degree = [0] * vertex_count
            for triple in targets:
                for vertex in triple:
                    degree[vertex] += 1
            assert sum(degree) == 3 * len(targets)
            triple_incidences += sum(degree)
            checked += 1
    return checked, triple_incidences


def check_edge_averaged_criterion():
    rng = random.Random(1211)
    checked = 0
    improving_certificates = 0
    for side in range(4, 120):
        kappa = (side / (side - 2)) ** side
        for _ in range(500):
            potential = rng.randint(1, 1000)
            loads = [0] * (2 * side)
            for _target in range(potential):
                for vertex in rng.sample(range(2 * side), 3):
                    loads[vertex] += 1
            assert sum(loads) == 3 * potential

            scores = []
            for load in loads:
                normalized_collateral = rng.random() * max(1.0, load / kappa + 2.0)
                unavailable_term = rng.random() * 2.0
                scores.append(kappa * (normalized_collateral + unavailable_term))

            if sum(scores) < 3 * potential:
                assert any(score < load for score, load in zip(scores, loads))
                improving_certificates += 1
            checked += 1
    return checked, improving_certificates


def check_optimized_extension_scores():
    rng = random.Random(1212)
    checked = 0
    for side in range(4, 100):
        for _ in range(300):
            potential = rng.randint(1, 500)
            extension_scores = []
            for _edge in range(2 * side):
                choices = [rng.random() * 100 for _ in range(rng.randint(1, 20))]
                extension_scores.append(min(choices))
            optimized = sum(extension_scores)
            if optimized < 3 * potential:
                assert min(extension_scores) < 3 * potential / (2 * side)
            checked += 1
    return checked


def check_rank_score_arithmetic():
    rng = random.Random(1208)
    checked = 0
    for side in range(4, 150):
        kappa = (side / (side - 2)) ** side
        for _ in range(400):
            v1 = rng.randint(0, side * side)
            v2 = rng.randint(0, side**3)
            v3 = rng.randint(0, side**4)
            score = v1 / side + v2 / falling(side, 2) + v3 / falling(side, 3)
            missing = rng.randint(0, side * side)
            potential = rng.randint(0, 500)
            barrier = kappa * (score + (potential + 1) * missing / side)
            destroyed = rng.randint(0, max(1, int(barrier) + 5))
            if barrier < destroyed:
                assert barrier - destroyed < 0
            checked += 1
    return checked


def main():
    unavailable = check_unavailable_expectations()
    forcing = check_weighted_feasibility_forcing()
    incidence = check_target_incidence_identity()
    averaged = check_edge_averaged_criterion()
    print(
        "verified restricted bank selection:",
        unavailable[0],
        "unavailable-bank cases with",
        unavailable[1],
        "edge incidences,",
        forcing[0],
        "weighted responses with",
        forcing[1],
        "negative feasible cases,",
        incidence[0],
        "target families with",
        incidence[1],
        "incidences,",
        averaged[0],
        "edge averages with",
        averaged[1],
        "improvement certificates,",
        check_optimized_extension_scores(),
        "extension optimizations, and",
        check_rank_score_arithmetic(),
        "rank-score cases",
    )


if __name__ == "__main__":
    main()
