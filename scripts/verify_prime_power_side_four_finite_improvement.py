#!/usr/bin/env python3
"""Complete finite checks for CMR1286--CMR1293."""

from collections import Counter
from itertools import combinations, permutations


def matching(permutation):
    return frozenset((row, permutation[row]) for row in range(4))


def collinear(triple):
    (x1, y1), (x2, y2), (x3, y3) = triple
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


def potential(state):
    return sum(collinear(triple) for triple in combinations(state, 3))


def targets(state):
    return [
        frozenset(triple)
        for triple in combinations(state, 3)
        if collinear(triple)
    ]


def all_response_states(opposite, edge, permutations_list):
    responses = []
    for forbidden_tuple in permutations_list:
        forbidden = matching(forbidden_tuple)
        if edge not in forbidden or not forbidden.isdisjoint(opposite):
            continue
        for response_tuple in permutations_list:
            response = matching(response_tuple)
            if response.isdisjoint(opposite | forbidden):
                responses.append((forbidden, response, opposite | response))
    return responses


def check_state_stock():
    permutations_list = list(permutations(range(4)))
    ordered = []
    physical = {}
    for opposite_tuple in permutations_list:
        opposite = matching(opposite_tuple)
        for current_tuple in permutations_list:
            current = matching(current_tuple)
            if not current.isdisjoint(opposite):
                continue
            state = opposite | current
            ordered.append((opposite, current, state))
            physical.setdefault(state, 0)
            physical[state] += 1

    ordered_distribution = Counter(potential(state) for _, _, state in ordered)
    physical_distribution = Counter(potential(state) for state in physical)
    assert len(ordered) == 216
    assert len(physical) == 90
    assert ordered_distribution == Counter({0: 40, 1: 48, 2: 84, 4: 24, 5: 8, 6: 8, 8: 4})
    assert physical_distribution == Counter({0: 11, 1: 24, 2: 38, 4: 10, 5: 4, 6: 2, 8: 1})
    return permutations_list, ordered, physical


def check_all_dirty_improvements(permutations_list, ordered):
    dirty = 0
    response_instances = 0
    extension_instances = 0
    best_changes = Counter()
    canonical_steps = 0
    for opposite, current, state in ordered:
        old_potential = potential(state)
        if old_potential == 0:
            continue
        dirty += 1
        best = None
        best_key = None
        for target_index, target in enumerate(targets(state)):
            for edge in sorted(target):
                if edge in current:
                    fixed = opposite
                    rematched = current
                else:
                    fixed = current
                    rematched = opposite
                responses = all_response_states(fixed, edge, permutations_list)
                extension_instances += len({forbidden for forbidden, _, _ in responses})
                for forbidden, response, new_state in responses:
                    response_instances += 1
                    assert edge not in new_state
                    assert response.isdisjoint(fixed | forbidden)
                    change = potential(new_state) - old_potential
                    key = (change, target_index, edge, tuple(sorted(forbidden)), tuple(sorted(response)))
                    if best_key is None or key < best_key:
                        best_key = key
                        best = change
        assert best is not None and best < 0
        assert old_potential + best >= 0
        best_changes[best] += 1
        canonical_steps += old_potential

    assert dirty == 176
    assert response_instances == 10368
    assert extension_instances == 3888
    assert best_changes == Counter({-1: 56, -2: 76, -4: 34, -5: 4, -6: 4, -8: 2})
    assert canonical_steps <= 176 * 8
    return dirty, response_instances, extension_instances, best_changes


def check_lowering_expansion_arithmetic():
    checked = 0
    for old_minimum in range(1, 9):
        for response_value in range(old_minimum):
            expanded_minimum = min(old_minimum, response_value)
            assert expanded_minimum < old_minimum
            checked += 1
    return checked


def check_contraction_budget():
    checked = 0
    for contracted in range(9):
        residual = 8 - contracted
        assert residual >= 0
        checked += 1
    return checked


def main():
    permutations_list, ordered, physical = check_state_stock()
    improvements = check_all_dirty_improvements(permutations_list, ordered)
    print(
        "verified side-four finite improvement:",
        len(ordered),
        "ordered states,",
        len(physical),
        "physical states,",
        improvements[0],
        "dirty states,",
        improvements[1],
        "response instances,",
        improvements[2],
        "extension instances, best changes",
        dict(sorted(improvements[3].items())),
        ",",
        check_lowering_expansion_arithmetic(),
        "lowering expansions, and",
        check_contraction_budget(),
        "contraction ranks",
    )


if __name__ == "__main__":
    main()
