#!/usr/bin/env python3
"""Verify complete minimax-optimal path multiplicities in the side-six graph."""
from __future__ import annotations

from collections import Counter

from verify_product_side_six_repair_barrier_profile import build_graph, minimax_profiles

EXPECTED_HISTOGRAM = Counter({
    1: 102, 2: 18, 3: 12, 4: 12, 5: 11, 6: 29, 7: 22, 8: 30,
    9: 28, 10: 19, 11: 43, 12: 20, 13: 32, 14: 19, 15: 32,
    16: 8, 17: 17, 18: 13, 19: 10, 20: 16, 21: 9, 22: 10,
    23: 5, 24: 8, 25: 4, 26: 5, 27: 2, 28: 2, 29: 2, 30: 1,
    36: 1, 38: 2,
})
EXPECTED_EXCEPTIONAL = Counter({4: 2, 6: 2, 7: 2, 9: 2, 11: 2})


def main() -> None:
    _, potentials, neighbours = build_graph()
    barriers, steps, _ = minimax_profiles(potentials, neighbours)

    optimal_next: list[tuple[int, ...]] = []
    for vertex in range(len(potentials)):
        choices = tuple(
            neighbour
            for neighbour in neighbours[vertex]
            if steps[vertex] > 0
            and steps[neighbour] + 1 == steps[vertex]
            and max(potentials[vertex], barriers[neighbour]) == barriers[vertex]
        )
        if steps[vertex] > 0:
            assert choices
        optimal_next.append(choices)

    path_counts = [0] * len(potentials)
    for vertex, step in enumerate(steps):
        if step == 0:
            path_counts[vertex] = 1
    for step in range(1, max(steps) + 1):
        for vertex, value in enumerate(steps):
            if value == step:
                path_counts[vertex] = sum(
                    path_counts[neighbour] for neighbour in optimal_next[vertex]
                )

    nonsolutions = {vertex for vertex, step in enumerate(steps) if step > 0}
    forced_first = {
        vertex for vertex in nonsolutions if len(optimal_next[vertex]) == 1
    }
    unique_path = {
        vertex for vertex in nonsolutions if path_counts[vertex] == 1
    }
    exceptional = {
        vertex
        for vertex in nonsolutions
        if barriers[vertex] > potentials[vertex]
    }

    histogram = Counter(path_counts[vertex] for vertex in nonsolutions)
    exceptional_histogram = Counter(path_counts[vertex] for vertex in exceptional)
    assert histogram == EXPECTED_HISTOGRAM
    assert exceptional_histogram == EXPECTED_EXCEPTIONAL
    assert forced_first == unique_path
    assert len(forced_first) == 102
    assert len(nonsolutions - unique_path) == 442
    assert sum(path_counts[vertex] for vertex in nonsolutions) == 5_579
    assert max(path_counts[vertex] for vertex in nonsolutions) == 38

    three_step = [vertex for vertex in nonsolutions if steps[vertex] == 3]
    assert len(three_step) == 1
    assert path_counts[three_step[0]] == 30

    print(
        "PX1149--PX1152 side-six repair path multiplicity: "
        "nonsolutions=544 unique_paths=102 multiple_paths=442 "
        "path_sum=5579 maximum=38 exceptional=4:2,6:2,7:2,9:2,11:2 PASS"
    )


if __name__ == "__main__":
    main()
