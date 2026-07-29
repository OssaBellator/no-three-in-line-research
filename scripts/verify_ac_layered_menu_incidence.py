#!/usr/bin/env python3
"""Finite audit for AC5bo--AC5bs layered menu incidence aggregation."""

from __future__ import annotations

import collections
import random


SEED = 90210
SYSTEMS = 8_000


def nonempty_subsets(n: int):
    for mask in range(1, 1 << n):
        yield [i for i in range(n) if (mask >> i) & 1]


def main() -> None:
    rng = random.Random(SEED)
    total_layers = 0
    total_layer_edges = 0
    conditioned_deletions = 0
    deficient_systems = 0
    missing_rectangle_incidences = 0

    for _ in range(SYSTEMS):
        n_left = rng.randint(2, 6)
        n_right = rng.randint(3, 8)
        layer_count = rng.randint(2, 4)

        layers: list[set[tuple[int, int]]] = []
        for _layer in range(layer_count):
            edge_probability = rng.uniform(0.2, 0.65)
            edges = {
                (left, right)
                for left in range(n_left)
                for right in range(n_right)
                if rng.random() < edge_probability
            }
            layers.append(edges)

        total_layers += layer_count
        total_layer_edges += sum(len(edges) for edges in layers)

        conditioned_layers: list[set[tuple[int, int]]] = []
        for edges in layers:
            deletion_probability = rng.uniform(0.0, 0.25)
            conditioned = {
                edge for edge in edges if rng.random() > deletion_probability
            }
            conditioned_deletions += len(edges) - len(conditioned)
            conditioned_layers.append(conditioned)

        union_edges = set().union(*conditioned_layers)

        left_degrees: list[int] = []
        for left in range(n_left):
            multiplicity = collections.Counter(
                right
                for edges in conditioned_layers
                for edge_left, right in edges
                if edge_left == left
            )
            layer_degree_sum = sum(multiplicity.values())
            overlap_excess = sum(max(0, count - 1) for count in multiplicity.values())
            union_degree = len(multiplicity)
            assert union_degree == layer_degree_sum - overlap_excess
            left_degrees.append(union_degree)

        minimum_left_degree = min(left_degrees)

        layer_reverse_loads: list[int] = []
        for edges in conditioned_layers:
            loads = [
                sum(1 for _left, edge_right in edges if edge_right == right)
                for right in range(n_right)
            ]
            layer_reverse_loads.append(max(loads, default=0))

        reverse_load_sum = sum(layer_reverse_loads)
        actual_reverse_load = max(
            (
                sum(1 for _left, edge_right in union_edges if edge_right == right)
                for right in range(n_right)
            ),
            default=0,
        )
        assert actual_reverse_load <= reverse_load_sum

        maximum_deficit = 0
        maximum_missing_rectangle = 0
        for left_subset in nonempty_subsets(n_left):
            neighborhood = {
                right
                for left, right in union_edges
                if left in left_subset
            }
            deficit = len(left_subset) - len(neighborhood)
            maximum_deficit = max(maximum_deficit, deficit)
            maximum_missing_rectangle = max(
                maximum_missing_rectangle,
                len(left_subset) * (n_right - len(neighborhood)),
            )

            if actual_reverse_load > 0:
                assert (
                    actual_reverse_load * max(0, deficit)
                    <= len(left_subset)
                    * max(0, actual_reverse_load - minimum_left_degree)
                )
            elif deficit > 0:
                assert minimum_left_degree == 0

        if maximum_deficit > 0:
            deficient_systems += 1
            missing_rectangle_incidences += maximum_missing_rectangle

    print(f"systems={SYSTEMS}")
    print(f"layers={total_layers}")
    print(f"layer_edges={total_layer_edges}")
    print(f"conditioned_deletions={conditioned_deletions}")
    print(f"deficient_systems={deficient_systems}")
    print(f"missing_rectangle_incidences={missing_rectangle_incidences}")


if __name__ == "__main__":
    main()
