#!/usr/bin/env python3
"""Verify the exact two-cycle batch improvement census in the 2 x 3 cf host."""
from __future__ import annotations

from verify_product_hybrid_repair import (
    FactorPair,
    enumerate_degree_two_states,
    product_host,
    single_cycle_neighbours,
    triple_potential,
)


def main() -> None:
    outer: FactorPair = ((0, 1), (1, 0))
    inner: FactorPair = ((0, 2, 1), (1, 0, 2))
    host = product_host(outer, inner, "cf")
    states = enumerate_degree_two_states(host)
    potentials = tuple(triple_potential(state) for state in states)

    neighbours: list[list[int]] = [[] for _ in states]
    for first in range(len(states)):
        for second in range(first + 1, len(states)):
            if single_cycle_neighbours(states[first], states[second]):
                neighbours[first].append(second)
                neighbours[second].append(first)

    one_step = 0
    two_step = 0
    witnesses: list[tuple[int, int, int]] = []
    for state, value in enumerate(potentials):
        if value == 0:
            continue

        lower_neighbour = next(
            (
                neighbour
                for neighbour in neighbours[state]
                if potentials[neighbour] < value
            ),
            None,
        )
        if lower_neighbour is not None:
            one_step += 1
            continue

        candidates = [
            (potentials[middle], potentials[endpoint], middle, endpoint)
            for middle in neighbours[state]
            for endpoint in neighbours[middle]
            if potentials[endpoint] < value
        ]
        assert candidates, (state, value)
        _, _, middle, endpoint = min(candidates)
        two_step += 1
        witnesses.append((state, middle, endpoint))

    assert len(states) == 546
    assert sum(value == 0 for value in potentials) == 2
    assert one_step == 534
    assert two_step == 10
    assert all(
        potentials[start] == 1
        and potentials[middle] == 2
        and potentials[endpoint] == 0
        for start, middle, endpoint in witnesses
    )

    print(
        "2x3 cf two-cycle census: bad_states=544, "
        "one_cycle_improvable=534, two_cycle_batches=10"
    )
    print("all ten exceptional batches have potential profile 1 -> 2 -> 0")


if __name__ == "__main__":
    main()
