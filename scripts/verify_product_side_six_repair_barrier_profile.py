#!/usr/bin/env python3
"""Exact distance and minimax-barrier profile of the canonical side-six repair graph."""
from __future__ import annotations

from collections import Counter, deque
from heapq import heappop, heappush
from math import inf
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from verify_product_hybrid_repair import (  # noqa: E402
    decompose,
    enumerate_degree_two_states,
    product_host,
    single_cycle_neighbours,
    triple_potential,
)

FactorPair = tuple[tuple[int, ...], tuple[int, ...]]

EXPECTED_POTENTIALS = {
    0: 2,
    1: 10,
    2: 57,
    3: 92,
    4: 109,
    5: 60,
    6: 68,
    7: 30,
    8: 19,
    9: 6,
    10: 9,
    11: 24,
    12: 20,
    13: 12,
    14: 4,
    15: 4,
    20: 2,
    21: 6,
    22: 5,
    23: 6,
    26: 1,
}
EXPECTED_DEGREES = {52: 32, 58: 224, 66: 48, 72: 96, 76: 16, 96: 2, 123: 128}
EXPECTED_DISTANCE = {0: 2, 1: 112, 2: 432}
EXPECTED_OPTIMAL_STEPS = {0: 2, 1: 112, 2: 431, 3: 1}
EXPECTED_PATH = (291, 92, 124, 537)
EXPECTED_PATH_POTENTIALS = (2, 2, 2, 0)
EXPECTED_PATH_LAYERS = (
    ((1, 0, 2, 3, 5, 4), (2, 4, 5, 0, 1, 3)),
    ((0, 4, 2, 1, 5, 3), (2, 0, 5, 3, 1, 4)),
    ((0, 4, 3, 1, 5, 2), (2, 1, 5, 0, 4, 3)),
    ((2, 1, 5, 0, 4, 3), (3, 5, 4, 1, 0, 2)),
)


def build_graph() -> tuple[
    tuple[tuple[tuple[int, int], ...], ...],
    tuple[int, ...],
    tuple[tuple[int, ...], ...],
]:
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
    return states, potentials, tuple(tuple(values) for values in neighbours)


def unweighted_distances(
    potentials: tuple[int, ...],
    neighbours: tuple[tuple[int, ...], ...],
) -> tuple[int, ...]:
    distance = [-1] * len(potentials)
    queue: deque[int] = deque()
    for vertex, potential in enumerate(potentials):
        if potential == 0:
            distance[vertex] = 0
            queue.append(vertex)
    while queue:
        vertex = queue.popleft()
        for neighbour in neighbours[vertex]:
            if distance[neighbour] < 0:
                distance[neighbour] = distance[vertex] + 1
                queue.append(neighbour)
    assert min(distance) == 0
    return tuple(distance)


def minimax_profiles(
    potentials: tuple[int, ...],
    neighbours: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    best_barrier = [inf] * len(potentials)
    best_steps = [10**9] * len(potentials)
    predecessor = [-1] * len(potentials)
    queue: list[tuple[int, int, int]] = []
    for vertex, potential in enumerate(potentials):
        if potential == 0:
            best_barrier[vertex] = 0
            best_steps[vertex] = 0
            heappush(queue, (0, 0, vertex))

    while queue:
        barrier, steps, vertex = heappop(queue)
        if (barrier, steps) != (best_barrier[vertex], best_steps[vertex]):
            continue
        for neighbour in neighbours[vertex]:
            candidate = (max(barrier, potentials[neighbour]), steps + 1)
            if candidate < (best_barrier[neighbour], best_steps[neighbour]):
                best_barrier[neighbour], best_steps[neighbour] = candidate
                predecessor[neighbour] = vertex
                heappush(queue, (*candidate, neighbour))

    return (
        tuple(int(value) for value in best_barrier),
        tuple(best_steps),
        tuple(predecessor),
    )


def main() -> None:
    states, potentials, neighbours = build_graph()
    assert len(states) == 546
    assert sum(map(len, neighbours)) // 2 == 20_944
    assert dict(sorted(Counter(potentials).items())) == EXPECTED_POTENTIALS
    assert dict(sorted(Counter(map(len, neighbours)).items())) == EXPECTED_DEGREES

    distance = unweighted_distances(potentials, neighbours)
    assert dict(sorted(Counter(distance).items())) == EXPECTED_DISTANCE

    barriers, steps, predecessor = minimax_profiles(potentials, neighbours)
    excess = Counter(barriers[index] - potentials[index] for index in range(len(states)))
    assert excess == Counter({0: 536, 1: 10})
    assert dict(sorted(Counter(steps).items())) == EXPECTED_OPTIMAL_STEPS

    traps = [
        vertex
        for vertex, potential in enumerate(potentials)
        if potential == 1
        and all(potentials[neighbour] >= potential for neighbour in neighbours[vertex])
    ]
    assert len(traps) == 10
    assert all((barriers[vertex], steps[vertex]) == (2, 2) for vertex in traps)

    three_step = [vertex for vertex, value in enumerate(steps) if value == 3]
    assert three_step == [EXPECTED_PATH[0]]
    path = [three_step[0]]
    while predecessor[path[-1]] >= 0:
        path.append(predecessor[path[-1]])
    assert tuple(path) == EXPECTED_PATH
    assert tuple(potentials[vertex] for vertex in path) == EXPECTED_PATH_POTENTIALS
    assert tuple(decompose(states[vertex]) for vertex in path) == EXPECTED_PATH_LAYERS

    start = EXPECTED_PATH[0]
    two_step_intermediates = Counter(
        potentials[middle]
        for middle in neighbours[start]
        if any(potentials[target] == 0 for target in neighbours[middle])
    )
    assert two_step_intermediates == Counter({4: 4, 3: 2})

    print(
        "side-six repair profile: states=546 edges=20944 solutions=2 "
        "distance={0:2,1:112,2:432} barrier_excess={0:536,1:10} "
        "optimal_steps={0:2,1:112,2:431,3:1} PASS"
    )
    print(
        "explicit barrier-preserving path: indices=291,92,124,537 "
        "potentials=2,2,2,0; every two-step path rises to at least 3"
    )
    print("PX1036--PX1039 side-six repair barrier profile: PASS")


if __name__ == "__main__":
    main()
