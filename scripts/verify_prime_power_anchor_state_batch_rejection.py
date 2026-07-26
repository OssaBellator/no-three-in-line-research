#!/usr/bin/env python3
"""Finite checks for CMR785--CMR792."""

from itertools import combinations, permutations


def layer_matching(perm, layer):
    return frozenset((layer, source, perm[source]) for source in range(len(perm)))


def physical_cells(state):
    return frozenset((source, target) for _, source, target in state)


def joint_states(side):
    perms = list(permutations(range(side)))
    states = []
    for first in perms:
        first_state = layer_matching(first, 0)
        first_cells = {(source, first[source]) for source in range(side)}
        for second in perms:
            second_cells = {(source, second[source]) for source in range(side)}
            if first_cells.isdisjoint(second_cells):
                states.append(first_state | layer_matching(second, 1))
    return states


def chosen_pair(anchor, target):
    by_layer = {0: [], 1: []}
    for edge in anchor:
        _, source, target_vertex = edge
        if (source, target_vertex) in target:
            by_layer[edge[0]].append(edge)
    layer = min(index for index in by_layer if len(by_layer[index]) >= 2)
    return frozenset(sorted(by_layer[layer])[:2])


def first_state(states, predicate):
    candidates = [state for state in states if predicate(state)]
    if not candidates:
        return None
    return min(candidates, key=lambda state: tuple(sorted(state)))


def run_rejection_pass(states, anchor, target):
    family = set(states)
    deleted = set()
    batches = 0

    while True:
        candidate = first_state(
            family,
            lambda state: not target.issubset(physical_cells(state)),
        )
        if candidate is None:
            break
        entering = set(candidate - anchor)
        assert len(entering) >= 2
        assert entering.isdisjoint(anchor)
        assert entering.isdisjoint(deleted)
        deleted.update(entering)
        family = {state for state in family if set(state).isdisjoint(entering)}
        assert anchor in family
        batches += 1

    assert all(target.issubset(physical_cells(state)) for state in family)

    pair = chosen_pair(anchor, target)
    while True:
        candidate = first_state(family, lambda state: not pair.issubset(state))
        if candidate is None:
            break
        entering = set(candidate - anchor)
        assert len(entering) >= 2
        assert entering.isdisjoint(anchor)
        assert entering.isdisjoint(deleted)
        deleted.update(entering)
        family = {state for state in family if set(state).isdisjoint(entering)}
        assert anchor in family
        batches += 1

    side = len(anchor) // 2
    assert all(pair.issubset(state) for state in family)
    assert batches <= side * (side - 1)
    assert len(deleted) <= 2 * side * side - 2 * side

    residual = {frozenset(state - pair) for state in family}
    assert len(residual) == len(family)
    assert all(len(state) == 2 * side - 2 for state in residual)
    return batches


def check_all():
    checked = 0
    maximum_batches = 0
    for side in range(2, 5):
        states = joint_states(side)
        for anchor in states:
            cells = sorted(physical_cells(anchor))
            for target in combinations(cells, 3):
                maximum_batches = max(
                    maximum_batches,
                    run_rejection_pass(states, anchor, frozenset(target)),
                )
                checked += 1
    return checked, maximum_batches


def main():
    checked, maximum = check_all()
    print(
        "verified anchor-state batch rejection:",
        checked,
        "anchor/target instances; maximum rejected batches",
        maximum,
    )


if __name__ == "__main__":
    main()
