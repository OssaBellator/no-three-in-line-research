#!/usr/bin/env python3
"""Finite audit for BDA5cz--BDA5dd gain-potential source conservation."""

from __future__ import annotations

from fractions import Fraction
import random


SEED = 90211
SYSTEMS = 10_000


def main() -> None:
    rng = random.Random(SEED)
    edge_count = 0
    transfer_count = 0
    terminal_source_units = 0
    sampled_gain_violations = 0
    maximum_nodes = 0

    for _ in range(SYSTEMS):
        node_count = rng.randint(2, 7)
        maximum_nodes = max(maximum_nodes, node_count)
        potential = [rng.randint(1, 12) for _ in range(node_count)]

        edges: list[tuple[int, int, Fraction]] = []
        for source in range(node_count):
            for target in range(node_count):
                if source == target or rng.random() > 0.25:
                    continue
                denominator = rng.randint(1, 6)
                maximum_numerator = (
                    potential[source] * denominator // potential[target]
                )
                if maximum_numerator >= 1:
                    numerator = rng.randint(1, maximum_numerator)
                    gain = Fraction(numerator, denominator)
                    assert potential[target] * gain <= potential[source]
                    edges.append((source, target, gain))

        edge_count += len(edges)
        live_mass = [rng.randint(0, 8) for _ in range(node_count)]
        initial_potential = sum(
            potential[node] * live_mass[node] for node in range(node_count)
        )
        deposited_potential = 0
        terminal_potential = 0

        for _step in range(rng.randint(4, 18)):
            if rng.random() < 0.15:
                node = rng.randrange(node_count)
                mass = rng.randint(1, 4)
                live_mass[node] += mass
                deposited_potential += potential[node] * mass

            available = [edge for edge in edges if live_mass[edge[0]] > 0]
            if available and rng.random() < 0.75:
                source, target, gain = rng.choice(available)
                input_mass = rng.randint(1, live_mass[source])
                output_mass = (
                    gain.numerator * input_mass // gain.denominator
                )
                live_mass[source] -= input_mass
                live_mass[target] += output_mass
                assert (
                    potential[target] * output_mass
                    <= potential[source] * input_mass
                )
                transfer_count += 1
            else:
                available_nodes = [
                    node for node, mass in enumerate(live_mass) if mass > 0
                ]
                if available_nodes:
                    node = rng.choice(available_nodes)
                    mass = rng.randint(1, live_mass[node])
                    live_mass[node] -= mass
                    terminal_potential += potential[node] * mass
                    terminal_source_units += mass

            assert (
                terminal_potential
                + sum(
                    potential[node] * live_mass[node]
                    for node in range(node_count)
                )
                <= initial_potential + deposited_potential
            )

        if rng.random() < 0.18:
            source = rng.randrange(node_count)
            target = rng.randrange(node_count)
            denominator = rng.randint(1, 5)
            numerator = (
                potential[source] * denominator // potential[target]
            ) + 1
            violating_gain = Fraction(numerator, denominator)
            assert potential[target] * violating_gain > potential[source]
            sampled_gain_violations += 1

    print(f"systems={SYSTEMS}")
    print(f"edges={edge_count}")
    print(f"transfers={transfer_count}")
    print(f"terminal_source_units={terminal_source_units}")
    print(f"sampled_gain_violations={sampled_gain_violations}")
    print(f"maximum_nodes={maximum_nodes}")


if __name__ == "__main__":
    main()
