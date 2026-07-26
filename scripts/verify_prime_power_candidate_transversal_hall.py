#!/usr/bin/env python3
"""Finite checks for CMR1390--CMR1397."""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product
from math import gcd
import random


def matching(permutation):
    return frozenset((row, permutation[row]) for row in range(len(permutation)))


def compatible(prescription):
    return (
        len({row for row, _column in prescription}) == len(prescription)
        and len({column for _row, column in prescription}) == len(prescription)
    )


def weighted_true_cost(response, candidates, weights):
    return sum(
        weights[index]
        for index, prescription in enumerate(candidates)
        if prescription <= response
    )


def exact_transversal_value(responses, candidates, weights):
    """Enumerate exempt-or-delete choices, one choice per candidate."""
    best = None
    witness = None
    options = [tuple([None] + sorted(prescription)) for prescription in candidates]
    for actions in product(*options):
        exempt_weight = sum(
            weights[index] for index, action in enumerate(actions) if action is None
        )
        if best is not None and exempt_weight >= best:
            continue
        deleted = frozenset(action for action in actions if action is not None)
        surviving = next(
            (response for response in responses if response.isdisjoint(deleted)), None
        )
        if surviving is not None:
            best = exempt_weight
            witness = actions, deleted, surviving
    assert best is not None
    return best, witness


def random_host_system(rng, side):
    all_matchings = [matching(value) for value in permutations(range(side))]
    retained = rng.sample(all_matchings, rng.randint(1, min(len(all_matchings), 10)))
    host_edges = frozenset().union(*retained)
    responses = tuple(state for state in all_matchings if state <= host_edges)
    assert responses

    prescriptions = set()
    for _ in range(rng.randint(1, 7)):
        witness = rng.choice(responses)
        rank = rng.randint(1, min(3, side))
        prescriptions.add(frozenset(rng.sample(tuple(witness), rank)))
    candidates = tuple(sorted(prescriptions, key=lambda value: (len(value), sorted(value))))
    weights = tuple(rng.randint(1, 7) for _ in candidates)
    return host_edges, responses, candidates, weights


def neighbourhood(host_edges, rows, side):
    return {
        column
        for row, column in host_edges
        if row in rows and 0 <= column < side
    }


def hall_witness(host_edges, side):
    rows = range(side)
    for size in range(1, side + 1):
        for subset in combinations(rows, size):
            row_set = frozenset(subset)
            neighbours = neighbourhood(host_edges, row_set, side)
            if len(neighbours) < len(row_set):
                return row_set, frozenset(neighbours)
    return None


def maximum_matching_size(host_edges, side):
    adjacency = {
        row: tuple(column for r, column in host_edges if r == row)
        for row in range(side)
    }
    matched_row = {}

    def augment(row, seen):
        for column in adjacency[row]:
            if column in seen:
                continue
            seen.add(column)
            if column not in matched_row or augment(matched_row[column], seen):
                matched_row[column] = row
                return True
        return False

    value = 0
    for row in range(side):
        if augment(row, set()):
            value += 1
    return value


def inclusion_minimal_blocker(host_edges, deleted, side):
    blocker = set(deleted)
    changed = True
    while changed:
        changed = False
        for edge in tuple(blocker):
            trial = blocker - {edge}
            if maximum_matching_size(host_edges - trial, side) < side:
                blocker = trial
                changed = True
                break
    return frozenset(blocker)


def check_random_weighted_systems():
    rng = random.Random(1390)
    systems = 0
    actions_checked = 0
    blocked_actions = 0
    minimal_blockers = 0

    for side in range(2, 6):
        for _ in range(180):
            host_edges, responses, candidates, weights = random_host_system(rng, side)
            direct = min(
                weighted_true_cost(response, candidates, weights)
                for response in responses
            )
            transversal, witness = exact_transversal_value(
                responses, candidates, weights
            )
            assert transversal == direct

            actions, deleted, surviving = witness
            assert surviving.isdisjoint(deleted)
            for index, prescription in enumerate(candidates):
                if actions[index] is not None:
                    assert actions[index] in prescription
                    assert not prescription <= surviving

            option_lists = [tuple(sorted(value)) for value in candidates]
            for selector in list(product(*option_lists))[:60]:
                selected = frozenset(selector)
                residual = host_edges - selected
                actions_checked += 1
                if maximum_matching_size(residual, side) == side:
                    assert hall_witness(residual, side) is None
                    continue
                blocked_actions += 1
                witness_rows = hall_witness(residual, side)
                assert witness_rows is not None
                blocker = inclusion_minimal_blocker(host_edges, selected, side)
                assert blocker <= selected
                assert maximum_matching_size(host_edges - blocker, side) == side - 1
                for edge in blocker:
                    assert maximum_matching_size(
                        host_edges - (blocker - {edge}), side
                    ) == side
                minimal_blockers += 1

            systems += 1

    return systems, actions_checked, blocked_actions, minimal_blockers


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


def equal_share_loads(candidates):
    loads = defaultdict(Fraction)
    for prescription in candidates:
        share = Fraction(1, len(prescription))
        for edge in prescription:
            loads[edge] += share
    return loads


def assignment_cost(response, loads):
    return sum(loads[edge] for edge in response)


def check_side_four_equal_share_obstruction():
    side = 4
    fixed = matching((0, 1, 3, 2))
    old = matching((1, 3, 2, 0))
    all_matchings = tuple(matching(value) for value in permutations(range(side)))
    old_targets = triples(fixed | old)
    assert len(old_targets) == 1

    bank_data = []
    for fixed_layer, target_layer in ((fixed, old), (old, fixed)):
        for edge in target_layer:
            destroyed = sum(1 for target in old_targets if edge in target)
            if not destroyed:
                continue
            candidates = geometric_candidates(
                side, fixed_layer, target_layer, edge
            )
            bank = tuple(
                response
                for response in all_matchings
                if response.isdisjoint(fixed_layer) and edge not in response
            )
            loads = equal_share_loads(candidates)
            assignment_minimum = min(
                assignment_cost(response, loads) for response in bank
            )
            true_minimum = min(
                weighted_true_cost(
                    response, candidates, tuple(1 for _ in candidates)
                )
                for response in bank
            )
            assert assignment_minimum >= destroyed
            assert true_minimum == 0
            bank_data.append(
                (edge, destroyed, assignment_minimum, true_minimum, len(candidates))
            )

    assert len(bank_data) == 3
    return tuple(bank_data)


def check_side_five_clean_transversal():
    side = 5
    old = matching((0, 1, 2, 4, 3))
    fixed = matching((1, 3, 4, 0, 2))
    edge = (0, 0)
    response = matching((4, 1, 0, 2, 3))
    candidates = geometric_candidates(side, fixed, old, edge)

    selector = []
    for prescription in candidates:
        outside = tuple(prescription - response)
        assert outside
        selector.append(outside[0])
    deleted = frozenset(selector)
    assert response.isdisjoint(deleted)
    assert all(not prescription <= response for prescription in candidates)

    host_edges = frozenset(
        (row, column)
        for row in range(side)
        for column in range(side)
        if (row, column) not in fixed and (row, column) != edge
    )
    assert response <= host_edges - deleted
    return len(candidates), len(deleted)


def main():
    random_counts = check_random_weighted_systems()
    side_four = check_side_four_equal_share_obstruction()
    side_five = check_side_five_clean_transversal()
    print(
        "verified candidate-transversal/Hall normal form:",
        random_counts[0],
        "weighted systems,",
        random_counts[1],
        "selector actions,",
        random_counts[2],
        "blocked actions,",
        random_counts[3],
        "minimal deficiency-one blockers; side-four equal-share obstruction",
        side_four,
        "and side-five clean transversal",
        side_five,
    )


if __name__ == "__main__":
    main()
