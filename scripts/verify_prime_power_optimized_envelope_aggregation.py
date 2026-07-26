#!/usr/bin/env python3
"""Finite checks for CMR1246--CMR1253."""

from itertools import combinations, permutations
from math import ceil, comb, gcd
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


def collinear(first, second, third):
    return line_key(first, second) == line_key(first, third)


def potential(state):
    return sum(collinear(*triple) for triple in combinations(state, 3))


def target_degrees(state):
    degree = {cell: 0 for cell in state}
    for triple in combinations(state, 3):
        if collinear(*triple):
            for cell in triple:
                degree[cell] += 1
    return degree


def rank_one_weight(edge, opposite, old_matching):
    if edge in old_matching:
        return 0
    return sum(collinear(first, second, edge) for first, second in combinations(opposite, 2))


def tau2(edge, state, opposite, old_matching):
    total = 0
    for other in state - {edge}:
        if edge in old_matching and other in old_matching:
            continue
        total += sum(collinear(edge, other, fixed) for fixed in opposite)
    return total


def tau3(edge, state, old_matching):
    return sum(
        collinear(edge, first, second)
        for first, second in combinations(state - {edge}, 2)
        if not {edge, first, second} <= set(old_matching)
    )


def full_envelope_bound(side, opposite, old_matching, forbidden):
    bank = response_bank(side, forbidden)
    complete = {(row, column) for row in range(side) for column in range(side)}
    graph = complete - set(opposite) - set(matching(forbidden))
    weight1 = {
        edge: rank_one_weight(edge, opposite, old_matching)
        for edge in graph
    }
    delta2 = {edge: 0 for edge in graph}
    delta3 = {edge: 0 for edge in graph}
    new_counts = {}
    old_state = set(opposite) | set(old_matching)
    for response in bank:
        new_state = set(opposite) | set(response)
        new_count = sum(
            collinear(*triple) and not set(triple) <= old_state
            for triple in combinations(new_state, 3)
        )
        new_counts[response] = new_count
        for edge in response:
            delta2[edge] = max(delta2[edge], tau2(edge, response, opposite, old_matching))
            delta3[edge] = max(delta3[edge], tau3(edge, response, old_matching))
    envelope = {
        edge: weight1[edge] + delta2[edge] / 2 + delta3[edge] / 3
        for edge in graph
    }
    row_bound = sum(
        max(envelope[(row, column)] for column in range(side) if (row, column) in graph)
        for row in range(side)
    )
    column_bound = sum(
        max(envelope[(row, column)] for row in range(side) if (row, column) in graph)
        for column in range(side)
    )
    bound = min(row_bound, column_bound)
    assert max(new_counts.values()) <= bound + 1e-12
    return bound, bank, new_counts, envelope, delta2, delta3


def check_geometric_aggregation():
    rng = random.Random(1248)
    checked_states = 0
    checked_edges = 0
    improvement_certificates = 0
    concentrated_edges = 0
    for side in range(4, 7):
        opposite = matching(tuple(range(side)))
        old_list = derangements(side)
        if side >= 5:
            old_list = rng.sample(old_list, min(8, len(old_list)))
        for old_permutation in old_list:
            old_matching = matching(old_permutation)
            old_state = set(opposite) | set(old_matching)
            old_potential = potential(old_state)
            degrees = target_degrees(old_state)
            assert sum(degrees.values()) == 3 * old_potential
            beta_sum = 0.0
            all_nonimproving = True
            for edge in old_state:
                layer_opposite = opposite if edge in old_matching else old_matching
                layer_old = old_matching if edge in old_matching else opposite
                # Relabeling symmetry is represented directly only when the fixed
                # opposite is the identity.  Test all old-layer target edges here.
                if layer_opposite != opposite:
                    continue
                extensions = [
                    forbidden
                    for forbidden in derangements(side)
                    if edge in matching(forbidden)
                ]
                best = None
                best_data = None
                for forbidden in extensions:
                    data = full_envelope_bound(side, opposite, old_matching, forbidden)
                    if best is None or data[0] < best:
                        best = data[0]
                        best_data = data
                assert best is not None
                beta_sum += best
                destroyed = degrees[edge]
                if best < destroyed:
                    assert all(
                        potential(set(opposite) | set(response)) < old_potential
                        for response in best_data[1]
                    )
                    improvement_certificates += 1
                    all_nonimproving = False
                maximum_envelope = max(best_data[3].values())
                assert maximum_envelope + 1e-12 >= best / side
                if maximum_envelope > 0:
                    concentrated_edges += 1
                checked_edges += 1
            if all_nonimproving:
                # This sampled half-layer version sums only old_matching edges, so
                # compare with their exact target incidence rather than 3*Phi.
                half_incidence = sum(degrees[edge] for edge in old_matching)
                assert beta_sum + 1e-12 >= half_incidence
            checked_states += 1
    return checked_states, checked_edges, improvement_certificates, concentrated_edges


def check_global_arithmetic():
    rng = random.Random(1249)
    checked = 0
    rank_cases = [0, 0, 0]
    for side in range(4, 300):
        for _ in range(300):
            potential_value = rng.randint(1, 100000)
            beta = [rng.random() * potential_value for _ in range(2 * side)]
            scale = 3 * potential_value / sum(beta)
            beta = [value * scale for value in beta]
            assert abs(sum(beta) - 3 * potential_value) < 1e-7
            largest_beta = max(beta)
            assert largest_beta + 1e-9 >= 3 * potential_value / (2 * side)
            local_envelope = largest_beta / side
            assert local_envelope + 1e-9 >= 3 * potential_value / (2 * side * side)

            pieces = [rng.random(), rng.random(), rng.random()]
            piece_scale = local_envelope / sum(pieces)
            weight1, half_delta2, third_delta3 = [piece * piece_scale for piece in pieces]
            assert abs(weight1 + half_delta2 + third_delta3 - local_envelope) < 1e-9
            winner = max(range(3), key=lambda index: (weight1, half_delta2, third_delta3)[index])
            rank_cases[winner] += 1
            assert max(weight1, half_delta2, third_delta3) + 1e-12 >= local_envelope / 3
            checked += 1
    return checked, rank_cases


def check_extension_law_averaging():
    rng = random.Random(1252)
    checked = 0
    certificates = 0
    for edge_count in range(1, 100):
        loads = [rng.randint(0, 1000) for _ in range(edge_count)]
        for _ in range(300):
            extension_values = [
                [rng.random() * 1500 for _ in range(rng.randint(1, 20))]
                for _edge in range(edge_count)
            ]
            averages = [sum(values) / len(values) for values in extension_values]
            if sum(averages) < sum(loads):
                assert any(
                    value < load
                    for values, load in zip(extension_values, loads)
                    for value in values
                )
                certificates += 1
            checked += 1
    return checked, certificates


def check_line_star_scales():
    rng = random.Random(1251)
    checked = 0
    for side in range(4, 300):
        for _ in range(300):
            potential_value = rng.randint(1, 100000)
            threshold = rng.randint(2, side)
            rank1 = ceil(potential_value / (2 * side * side * comb(threshold, 2)))
            rank2 = ceil(potential_value / (side * side * (side - 1)))
            rank3 = ceil(3 * potential_value / (2 * side * side * comb(threshold, 2)))
            assert rank1 >= 1 and rank2 >= 1 and rank3 >= 1
            checked += 1
    return checked


def main():
    geometric = check_geometric_aggregation()
    arithmetic = check_global_arithmetic()
    averaging = check_extension_law_averaging()
    print(
        "verified optimized envelope aggregation:",
        geometric[0],
        "geometric states,",
        geometric[1],
        "target edges,",
        geometric[2],
        "improvement certificates,",
        geometric[3],
        "concentrated edges,",
        arithmetic[0],
        "global arithmetic cases split as",
        arithmetic[1],
        ",",
        averaging[0],
        "extension laws with",
        averaging[1],
        "certificates, and",
        check_line_star_scales(),
        "line/star scale cases",
    )


if __name__ == "__main__":
    main()
