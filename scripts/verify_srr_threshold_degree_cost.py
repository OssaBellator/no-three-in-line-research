#!/usr/bin/env python3
"""Finite audit for SRR2n--SRR2r."""

from itertools import permutations
from math import ceil
import random

SEED = 20260728


def minimum_matching_cost(adjacency, costs):
    n = len(adjacency)
    m = len(costs)
    best = None
    for endpoints in permutations(range(m), n):
        if all(endpoints[a] in adjacency[a] for a in range(n)):
            value = sum(costs[b] for b in endpoints)
            best = value if best is None else min(best, value)
    return best


def threshold_deficiency(adjacency, costs, threshold):
    n = len(adjacency)
    best = 0
    for mask in range(1 << n):
        left = [a for a in range(n) if mask >> a & 1]
        neighbours = set()
        for a in left:
            neighbours.update(
                b for b in adjacency[a]
                if costs[b] < threshold
            )
        best = max(best, len(left) - len(neighbours))
    return best


def degree_bound(adjacency, costs, threshold):
    n = len(adjacency)
    low = [b for b, value in enumerate(costs) if value < threshold]
    if not low:
        return n, 0, 0

    low_set = set(low)
    left_degrees = [
        sum(1 for b in adjacency[a] if b in low_set)
        for a in range(n)
    ]
    d = min(left_degrees)
    right_degrees = [
        sum(1 for a in range(n) if b in adjacency[a])
        for b in low
    ]
    D = max(right_degrees) if right_degrees else 0
    if d == 0 or D == 0:
        return n, d, D

    delta = max(
        max(0, size - ceil(d * size / D))
        for size in range(1, n + 1)
    )
    return delta, d, D


def main():
    rng = random.Random(SEED)
    counters = {
        "hall_graphs": 0,
        "thresholds": 0,
        "conditioned_graphs": 0,
        "conditioned_thresholds": 0,
    }

    for _ in range(12_000):
        n = rng.randint(1, 5)
        m = rng.randint(n, 7)
        adjacency = []
        for _a in range(n):
            neighbours = {b for b in range(m) if rng.random() < 0.6}
            if not neighbours:
                neighbours.add(rng.randrange(m))
            adjacency.append(neighbours)
        costs = [rng.randint(0, 5) for _ in range(m)]

        optimum = minimum_matching_cost(adjacency, costs)
        if optimum is None:
            continue
        counters["hall_graphs"] += 1

        deficiencies = []
        for threshold in range(1, max(costs) + 1):
            deficiency = threshold_deficiency(adjacency, costs, threshold)
            bound, _d, _D = degree_bound(adjacency, costs, threshold)
            assert deficiency <= bound
            deficiencies.append(deficiency)
            counters["thresholds"] += 1
        assert optimum == sum(deficiencies)

        # Delete a bounded random set of incidences, retaining only Hall-feasible cases.
        conditioned = [set(row) for row in adjacency]
        deletions_per_left = [0] * n
        for _ in range(rng.randint(0, 3)):
            a = rng.randrange(n)
            if conditioned[a]:
                b = rng.choice(tuple(conditioned[a]))
                conditioned[a].remove(b)
                deletions_per_left[a] += 1

        conditioned_optimum = minimum_matching_cost(conditioned, costs)
        if conditioned_optimum is None:
            continue
        counters["conditioned_graphs"] += 1

        conditioned_deficiencies = []
        for threshold in range(1, max(costs) + 1):
            deficiency = threshold_deficiency(conditioned, costs, threshold)
            bound, _d, _D = degree_bound(conditioned, costs, threshold)
            assert deficiency <= bound
            conditioned_deficiencies.append(deficiency)
            counters["conditioned_thresholds"] += 1
        assert conditioned_optimum == sum(conditioned_deficiencies)

    assert counters["hall_graphs"] >= 10_000
    print("SRR threshold-degree cost audit passed")
    for key in sorted(counters):
        print(f"  {key.replace('_', ' ')}: {counters[key]}")


if __name__ == "__main__":
    main()
