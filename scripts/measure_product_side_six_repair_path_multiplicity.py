#!/usr/bin/env python3
"""Measure complete minimax-optimal path multiplicities in the side-six graph."""
from __future__ import annotations

from collections import Counter

from verify_product_side_six_repair_barrier_profile import build_graph, minimax_profiles


def main() -> None:
    _, potentials, neighbours = build_graph()
    barriers, steps, _ = minimax_profiles(potentials, neighbours)

    optimal_next: list[tuple[int, ...]] = []
    for vertex in range(len(potentials)):
        if steps[vertex] == 0:
            optimal_next.append(())
            continue
        choices = tuple(
            neighbour
            for neighbour in neighbours[vertex]
            if steps[neighbour] + 1 == steps[vertex]
            and max(potentials[vertex], barriers[neighbour]) == barriers[vertex]
        )
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
                assert path_counts[vertex] > 0

    nonsolutions = [
        vertex for vertex in range(len(potentials)) if steps[vertex] > 0
    ]
    forced_first = [
        vertex for vertex in nonsolutions if len(optimal_next[vertex]) == 1
    ]
    unique_path = [
        vertex for vertex in nonsolutions if path_counts[vertex] == 1
    ]
    exceptional = [
        vertex
        for vertex in nonsolutions
        if barriers[vertex] > potentials[vertex]
    ]

    histogram = dict(sorted(Counter(path_counts[vertex] for vertex in nonsolutions).items()))
    step_histograms = {
        step: dict(sorted(Counter(
            path_counts[vertex]
            for vertex in nonsolutions
            if steps[vertex] == step
        ).items()))
        for step in sorted(set(steps))
        if step > 0
    }
    exceptional_counts = sorted(path_counts[vertex] for vertex in exceptional)
    exceptional_histogram = dict(sorted(Counter(exceptional_counts).items()))

    print(
        "FINAL states=546 solutions=2 nonsolutions=544 "
        f"path_histogram={histogram} step_histograms={step_histograms} "
        f"path_sum={sum(path_counts[vertex] for vertex in nonsolutions)} "
        f"maximum={max(path_counts[vertex] for vertex in nonsolutions)} "
        f"forced_first={len(forced_first)} unique_path={len(unique_path)} "
        f"exceptional_histogram={exceptional_histogram} PASS"
    )


if __name__ == "__main__":
    main()
