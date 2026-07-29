#!/usr/bin/env python3
"""Finite checks for RI5hq--RI5ht."""

from __future__ import annotations

from collections import Counter
from math import ceil
from random import Random

SEED = 731
TRIALS = 2500


def greedy_independent(footprints: list[set[int]]) -> list[int]:
    remaining = set(range(len(footprints)))
    chosen: list[int] = []
    while remaining:
        vertex = min(remaining)
        chosen.append(vertex)
        remaining -= {
            other
            for other in remaining
            if footprints[vertex] & footprints[other]
        }
    return chosen


def verify() -> dict[str, int]:
    rng = Random(SEED)
    systems = repairs = selected = feasible = shortages = cost_total = 0

    for _ in range(TRIALS):
        primitive_count = rng.randint(4, 18)
        h = rng.randint(1, min(5, primitive_count))
        beta = rng.randint(1, 5)
        requested = rng.randint(1, 35)
        loads = [0] * primitive_count
        footprints: list[set[int]] = []

        for _ in range(requested):
            available = [x for x in range(primitive_count) if loads[x] < beta]
            if not available:
                break
            size = rng.randint(1, min(h, len(available)))
            footprint = set(rng.sample(available, size))
            for primitive in footprint:
                loads[primitive] += 1
            footprints.append(footprint)

        if not footprints:
            continue

        multiplicity = Counter(x for footprint in footprints for x in footprint)
        assert max(multiplicity.values()) <= beta
        degree_bound = h * (beta - 1)

        for index, footprint in enumerate(footprints):
            degree = sum(
                1
                for other, other_footprint in enumerate(footprints)
                if other != index and footprint & other_footprint
            )
            assert degree <= degree_bound

        independent = greedy_independent(footprints)
        assert len(independent) >= ceil(len(footprints) / (degree_bound + 1))
        assert all(
            not (footprints[left] & footprints[right])
            for position, left in enumerate(independent)
            for right in independent[position + 1 :]
        )

        dimensions = rng.randint(1, 5)
        costs = [
            [rng.randint(0, 4) for _ in range(dimensions)]
            for _ in footprints
        ]
        batch_cost = [
            sum(costs[index][coordinate] for index in independent)
            for coordinate in range(dimensions)
        ]
        reserve = [rng.randint(0, value + 3) for value in batch_cost]

        if all(value <= reserve[i] for i, value in enumerate(batch_cost)):
            feasible += 1
        else:
            shortages += 1
            coordinate = next(
                i for i, value in enumerate(batch_cost) if value > reserve[i]
            )
            assert batch_cost[coordinate] - reserve[coordinate] > 0

        kappa = max(sum(vector) for vector in costs)
        assert sum(batch_cost) <= kappa * len(independent)

        systems += 1
        repairs += len(footprints)
        selected += len(independent)
        cost_total += sum(batch_cost)

    epochs = 5000
    deficit = rng.randint(0, 20)
    initial_deficit = deficit
    churn_total = gain_total = ledger_cost = 0
    kappa = 7

    for _ in range(epochs):
        churn = rng.randint(0, 6)
        available = deficit + churn
        gain = rng.randint(0, available)
        cost = rng.randint(0, kappa * gain)
        deficit = available - gain
        churn_total += churn
        gain_total += gain
        ledger_cost += cost
        assert gain_total <= initial_deficit + churn_total
        assert ledger_cost <= kappa * gain_total

    return {
        "systems": systems,
        "repair_candidates": repairs,
        "commuting_repairs": selected,
        "reserve_feasible": feasible,
        "typed_shortages": shortages,
        "batch_cost": cost_total,
        "epochs": epochs,
        "churn": churn_total,
        "repair_gain": gain_total,
        "ledger_cost": ledger_cost,
    }


if __name__ == "__main__":
    result = verify()
    print("RI footprint-cost checks passed")
    for key, value in result.items():
        print(f"{key}: {value}")
