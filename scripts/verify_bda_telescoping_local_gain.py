#!/usr/bin/env python3
"""Finite audit for BDA5do--BDA5ds telescoping local gain certificates."""

from __future__ import annotations

import collections
import random
from fractions import Fraction


def simple_cycles(n: int, adjacency: dict[int, list[tuple[int, Fraction]]]) -> list[tuple[tuple[int, ...], Fraction]]:
    found: dict[tuple[int, ...], Fraction] = {}

    def canonical(nodes: list[int]) -> tuple[int, ...]:
        rotations = [tuple(nodes[i:] + nodes[:i]) for i in range(len(nodes))]
        return min(rotations)

    for start in range(n):
        stack: list[tuple[int, list[int], Fraction]] = [(start, [start], Fraction(1))]
        while stack:
            u, path, product = stack.pop()
            for v, gain in adjacency.get(u, []):
                if v == start and len(path) >= 2:
                    found[canonical(path)] = product * gain
                elif v not in path and len(path) < n:
                    stack.append((v, path + [v], product * gain))
    return list(found.items())


def main() -> None:
    rng = random.Random(1202)
    totals = collections.Counter()

    for _ in range(6000):
        n = rng.randint(2, 7)
        potentials = [Fraction(rng.randint(1, 9), rng.randint(1, 5)) for _ in range(n)]
        edge_gain: dict[tuple[int, int], Fraction] = {}

        for u in range(n):
            v = (u + 1) % n
            numerator = rng.randint(1, 5)
            denominator = rng.randint(numerator, 7)
            damping = Fraction(numerator, denominator)
            edge_gain[(u, v)] = damping * potentials[u] / potentials[v]

        for u in range(n):
            for v in range(n):
                if u != v and (u, v) not in edge_gain and rng.random() < 0.22:
                    numerator = rng.randint(1, 5)
                    denominator = rng.randint(numerator, 8)
                    damping = Fraction(numerator, denominator)
                    edge_gain[(u, v)] = damping * potentials[u] / potentials[v]

        if rng.random() < 0.22:
            u, v = rng.choice(list(edge_gain))
            damping = Fraction(rng.randint(6, 10), rng.randint(1, 5))
            if damping <= 1:
                damping = Fraction(3, 2)
            edge_gain[(u, v)] = damping * potentials[u] / potentials[v]

        adjacency: dict[int, list[tuple[int, Fraction]]] = collections.defaultdict(list)
        all_local = True
        for (u, v), gain in edge_gain.items():
            adjacency[u].append((v, gain))
            if gain * potentials[v] > potentials[u]:
                all_local = False
                totals["local_factor_violations"] += 1

        cycles = simple_cycles(n, adjacency)
        if all_local:
            assert all(product <= 1 for _, product in cycles)
            totals["certified_systems"] += 1
        else:
            totals["uncertified_systems"] += 1

        for (u, v), gain in list(edge_gain.items())[: min(8, len(edge_gain))]:
            input_mass = Fraction(rng.randint(1, 10), 1)
            output_mass = gain * input_mass * Fraction(rng.randint(0, 10), 10)
            if gain * potentials[v] <= potentials[u]:
                assert potentials[v] * output_mass <= potentials[u] * input_mass
            totals["transfer_checks"] += 1

        totals["systems"] += 1
        totals["vertices"] += n
        totals["edges"] += len(edge_gain)
        totals["simple_cycle_checks"] += len(cycles)

    print("BDA telescoping local gain certificate audit")
    for key in (
        "systems", "vertices", "edges", "simple_cycle_checks",
        "transfer_checks", "certified_systems", "uncertified_systems",
        "local_factor_violations",
    ):
        print(f"{key}: {totals[key]}")


if __name__ == "__main__":
    main()
