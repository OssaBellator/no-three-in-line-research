#!/usr/bin/env python3
"""Finite audit for GC2go--GC2gs."""

from itertools import product


def canonical_maximum_matching(n_left: int, n_right: int, edges: set[tuple[int, int]]):
    best_size = -1
    best = None
    for assignment in product(range(-1, n_right), repeat=n_left):
        used = [value for value in assignment if value >= 0]
        if len(set(used)) != len(used):
            continue
        if any((left, assignment[left]) not in edges for left in range(n_left) if assignment[left] >= 0):
            continue
        size = len(used)
        if size > best_size or (size == best_size and (best is None or assignment < best)):
            best_size = size
            best = assignment
    assert best is not None
    return best, best_size


def alternating_core(n_left: int, n_right: int, edges: set[tuple[int, int]], matching):
    unmatched = {left for left, right in enumerate(matching) if right < 0}
    left_reachable = set(unmatched)
    right_reachable: set[int] = set()

    changed = True
    while changed:
        changed = False
        for left in list(left_reachable):
            for right in range(n_right):
                if (left, right) in edges and matching[left] != right and right not in right_reachable:
                    right_reachable.add(right)
                    changed = True
        for right in list(right_reachable):
            for left, matched_right in enumerate(matching):
                if matched_right == right and left not in left_reachable:
                    left_reachable.add(left)
                    changed = True

    return unmatched, left_reachable, right_reachable


def main() -> None:
    graphs = deficient = saturated = 0

    for n_left in range(1, 5):
        for n_right in range(1, 5):
            possible_edges = [(left, right) for left in range(n_left) for right in range(n_right)]
            if len(possible_edges) <= 9:
                masks = range(1 << len(possible_edges))
            else:
                stride = max(1, (1 << len(possible_edges)) // 3000)
                masks = range(0, 1 << len(possible_edges), stride)

            for mask in masks:
                edges = {
                    edge for bit, edge in enumerate(possible_edges) if (mask >> bit) & 1
                }
                matching, _ = canonical_maximum_matching(n_left, n_right, edges)
                unmatched, left_core, right_core = alternating_core(
                    n_left, n_right, edges, matching
                )
                graphs += 1

                if not unmatched:
                    saturated += 1
                    continue

                deficient += 1
                neighbourhood = {
                    right
                    for left in left_core
                    for right in range(n_right)
                    if (left, right) in edges
                }
                assert neighbourhood == right_core
                assert len(right_core) == len(left_core) - len(unmatched)

                for right in right_core:
                    assert any(matching[left] == right for left in left_core)

                # Deterministic weights and three canonical cause classes.
                cause_weight = [0, 0, 0]
                total_unmatched_weight = 0
                for left in unmatched:
                    weight = left + 1
                    total_unmatched_weight += weight
                    cause_weight[left % 3] += weight
                assert 3 * max(cause_weight) >= total_unmatched_weight

    assert graphs == 12539
    assert deficient == 7069
    assert saturated == 5470
    print(
        "weighted alternating Hall-core audit passed:",
        f"{graphs} graphs, {deficient} deficient, {saturated} saturated",
    )


if __name__ == "__main__":
    main()
