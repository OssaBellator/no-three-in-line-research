#!/usr/bin/env python3
"""Measure optimal next-step choices in the canonical side-six repair graph."""
from __future__ import annotations

from collections import Counter

from verify_product_side_six_repair_barrier_profile import build_graph, minimax_profiles


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

    histogram = dict(sorted(Counter(choices).items()))
    exceptional_histogram = dict(sorted(Counter(exceptional_choices).items()))
    positive = [value for value in choices if value]
    assert len(positive) == len(potentials) - 2
    assert len(exceptional_choices) == 10
    print(
        "FINAL states=546 solutions=2 "
        f"choices={histogram} exceptional_choices={exceptional_histogram} "
        f"minimum_positive={min(positive)} maximum={max(positive)} "
        f"choice_sum={sum(positive)} nonsolutions={len(positive)} PASS"
    )


if __name__ == "__main__":
    main()
