#!/usr/bin/env python3
"""Finite audit for SRR2bv--SRR2bz threshold atom budgets."""

from __future__ import annotations

import collections
import random
from fractions import Fraction


def maximum_independent_weight(
    n: int, edges: list[tuple[int, int]], weights: list[int]
) -> int:
    edge_set = {tuple(sorted(edge)) for edge in edges}
    best = 0
    for mask in range(1 << n):
        if any(((mask >> u) & 1) and ((mask >> v) & 1) for u, v in edge_set):
            continue
        best = max(best, sum(weights[i] for i in range(n) if (mask >> i) & 1))
    return best


def main() -> None:
    rng = random.Random(1206)
    totals = collections.Counter()

    for _ in range(3500):
        n = rng.randint(2, 9)
        weights = [rng.randint(1, 6) for _ in range(n)]
        edges = [
            (u, v)
            for u in range(n)
            for v in range(u + 1, n)
            if rng.random() < 0.28
        ]
        n_atoms = rng.randint(1, max(1, min(7, len(edges) + 1)))
        witness_atom = [rng.randrange(n_atoms) for _ in edges]

        burden = [0] * n_atoms
        degree = [0] * n
        for (u, v), atom in zip(edges, witness_atom):
            burden[atom] += weights[u] + weights[v]
            degree[u] += 1
            degree[v] += 1

        total_burden = sum(weights[i] * degree[i] for i in range(n))
        assert total_burden == sum(burden)

        capacities: list[int] = []
        for atom_burden in burden:
            if rng.random() < 0.72:
                capacities.append(atom_burden + rng.randint(0, 5))
            else:
                capacities.append(
                    max(0, atom_burden - rng.randint(1, max(1, atom_burden)))
                )

        overloaded = [
            atom for atom in range(n_atoms) if burden[atom] > capacities[atom]
        ]
        total_weight = sum(weights)
        optimum = maximum_independent_weight(n, edges, weights)
        caro_wei = sum(
            Fraction(weights[i], degree[i] + 1) for i in range(n)
        )
        assert Fraction(optimum, 1) >= caro_wei
        assert caro_wei >= Fraction(
            total_weight * total_weight, total_weight + total_burden
        )

        if not overloaded:
            assert total_burden <= sum(capacities)
            assert Fraction(optimum, 1) >= Fraction(
                total_weight * total_weight,
                total_weight + sum(capacities),
            )
            totals["budget_paid_systems"] += 1
        else:
            totals["overloaded_systems"] += 1
            totals["overloaded_atoms"] += len(overloaded)

        totals["systems"] += 1
        totals["candidates"] += n
        totals["edges"] += len(edges)
        totals["atom_classes"] += n_atoms
        totals["burden_units"] += total_burden
        totals["capacity_units"] += sum(capacities)
        totals["bruteforce_checks"] += 1

    print("SRR threshold atom-budget audit")
    for key in (
        "systems", "candidates", "edges", "atom_classes", "burden_units",
        "capacity_units", "budget_paid_systems", "overloaded_systems",
        "overloaded_atoms", "bruteforce_checks",
    ):
        print(f"{key}: {totals[key]}")


if __name__ == "__main__":
    main()
