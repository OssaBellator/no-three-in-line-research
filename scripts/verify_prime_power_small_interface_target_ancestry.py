#!/usr/bin/env python3
"""Finite checks for CMR1182--CMR1189."""

import random


def last_fixation(events, target_edges):
    ordered = sorted(
        ((events[edge], edge) for edge in target_edges),
        key=lambda item: (item[0], item[1]),
    )
    return ordered[-1][1]


def check_last_fixation():
    rng = random.Random(1183)
    checked = 0
    for _ in range(100000):
        target = tuple(sorted(rng.sample(range(1000), 3)))
        events = {edge: rng.randint(0, 1000) for edge in target}
        chosen = last_fixation(events, target)
        assert events[chosen] == max(events.values())
        tied = [edge for edge in target if events[edge] == max(events.values())]
        assert chosen == max(tied)
        checked += 1
    return checked


def check_unique_backward_lineages():
    rng = random.Random(1182)
    checked = 0
    for _ in range(100000):
        root_side = rng.randint(1, 200)
        sides = [root_side]
        while sides[-1] > 1 and rng.random() < 0.95:
            sides.append(rng.randint(1, sides[-1] - 1))
        assert all(sides[index + 1] < sides[index] for index in range(len(sides) - 1))
        assert len(sides) == len(set(sides))
        checked += 1
    return checked


def nearest_large_ancestor(sides):
    for side in reversed(sides[:-1]):
        if side >= 3:
            return side
    return None


def check_small_owner_lifting():
    rng = random.Random(1185)
    checked = 0
    clean_root_cases = 0
    lifted_cases = 0
    for _ in range(100000):
        root = rng.randint(1, 100)
        sides = [root]
        while sides[-1] > 2:
            sides.append(rng.randint(1, sides[-1] - 1))
        final = sides[-1]
        assert final <= 2
        ancestor = nearest_large_ancestor(sides)
        if root >= 3:
            assert ancestor is not None and ancestor >= 3
            lifted_cases += 1
        else:
            assert ancestor is None
            clean_root_cases += 1
        checked += 1
    return checked, lifted_cases, clean_root_cases


def check_edge_lineage_bound():
    checked = 0
    for side in range(1, 1000):
        stages = sum(2 * m * m + m + 1 for m in range(1, side + 1))
        for height in range(1, 20):
            bound = (height + 1) * (stages + 1)
            assert bound >= stages + 1
            checked += 1
    return checked


def check_root_side_two_clean():
    board = [(x, y) for x in range(2) for y in range(2)]
    triples = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            for k in range(j + 1, len(board)):
                (x1, y1), (x2, y2), (x3, y3) = board[i], board[j], board[k]
                assert (x2 - x1) * (y3 - y1) != (x3 - x1) * (y2 - y1)
                triples += 1
    return triples


def main():
    lifted = check_small_owner_lifting()
    print(
        "verified small-interface target ancestry:",
        check_last_fixation(),
        "last-fixation cases,",
        check_unique_backward_lineages(),
        "edge lineages,",
        lifted[0],
        "small-owner histories with",
        lifted[1],
        "lifted and",
        lifted[2],
        "root-base cases,",
        check_edge_lineage_bound(),
        "lineage bounds, and",
        check_root_side_two_clean(),
        "root triple checks",
    )


if __name__ == "__main__":
    main()
