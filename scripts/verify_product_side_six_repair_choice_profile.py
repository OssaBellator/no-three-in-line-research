#!/usr/bin/env python3
"""Verify optimal next-step choice counts in the canonical side-six repair graph."""
from __future__ import annotations

from collections import Counter

from verify_product_side_six_repair_barrier_profile import build_graph, minimax_profiles

EXPECTED = {
    0: 2,
    1: 102,
    2: 19,
    3: 14,
    4: 18,
    5: 17,
    6: 32,
    7: 25,
    8: 43,
    9: 22,
    10: 24,
    11: 34,
    12: 33,
    13: 32,
    14: 16,
    15: 11,
    16: 23,
    17: 20,
    18: 13,
    19: 12,
    20: 8,
    21: 11,
    22: 5,
    23: 4,
    24: 1,
    25: 2,
    34: 1,
    35: 2,
}
EXPECTED_EXCEPTIONAL = {3: 2, 6: 2, 7: 4, 8: 2}


def main() -> None:
    _, potentials, neighbours = build_graph()
    barriers, steps, _ = minimax_profiles(potentials, neighbours)

    choices: list[int] = []
    exceptional_choices: list[int] = []
    for vertex in range(len(potentials)):
        if steps[vertex] == 0:
            choices.append(0)
            continue
        optimal = [
            neighbour
            for neighbour in neighbours[vertex]
            if steps[neighbour] + 1 == steps[vertex]
            and max(potentials[vertex], barriers[neighbour]) == barriers[vertex]
        ]
        assert optimal
        choices.append(len(optimal))
        if barriers[vertex] > potentials[vertex]:
            exceptional_choices.append(len(optimal))

    assert dict(sorted(Counter(choices).items())) == EXPECTED
    assert dict(sorted(Counter(exceptional_choices).items())) == EXPECTED_EXCEPTIONAL
    positive = [value for value in choices if value]
    assert min(positive) == 1
    assert max(positive) == 35
    assert sum(positive) == 5004
    assert len(positive) == 544
    print(
        "PX1114--PX1117 side-six repair choice profile: "
        "states=546 nonsolutions=544 choice_sum=5004 "
        "forced=102 exceptional={3:2,6:2,7:4,8:2} maximum=35 PASS"
    )


if __name__ == "__main__":
    main()
