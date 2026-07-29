#!/usr/bin/env python3
"""Finite audit for SRR2bg--SRR2bk higher-order conflict shadows."""

from __future__ import annotations

from fractions import Fraction
import itertools
import random


SEED = 90215
SYSTEMS = 3_500


def main() -> None:
    rng = random.Random(SEED)
    vertices = 0
    conflict_hyperedges = 0
    higher_order_hyperedges = 0
    shadow_edges_total = 0
    candidate_weight_units = 0
    bound_checks = 0

    for _ in range(SYSTEMS):
        vertex_count = rng.randint(3, 10)
        weights = [rng.randint(1, 9) for _ in range(vertex_count)]

        hyperedges: list[tuple[int, ...]] = []
        for _edge in range(rng.randint(1, 12)):
            edge_size = rng.randint(2, min(4, vertex_count))
            edge = tuple(sorted(rng.sample(range(vertex_count), edge_size)))
            if edge not in hyperedges:
                hyperedges.append(edge)

        shadow_edges: set[tuple[int, int]] = set()
        incident: list[list[tuple[int, ...]]] = [
            [] for _ in range(vertex_count)
        ]
        for edge in hyperedges:
            if len(edge) >= 3:
                higher_order_hyperedges += 1
            for vertex in edge:
                incident[vertex].append(edge)
            for first, second in itertools.combinations(edge, 2):
                shadow_edges.add((first, second))

        degree = [0] * vertex_count
        for first, second in shadow_edges:
            degree[first] += 1
            degree[second] += 1

        local_shadow_bound = [
            sum(len(edge) - 1 for edge in incident[vertex])
            for vertex in range(vertex_count)
        ]
        assert all(
            degree[vertex] <= local_shadow_bound[vertex]
            for vertex in range(vertex_count)
        )

        best_weight = 0
        best_mask = 0
        for mask in range(1 << vertex_count):
            if any(
                ((mask >> first) & 1) and ((mask >> second) & 1)
                for first, second in shadow_edges
            ):
                continue
            weight = sum(
                weights[vertex]
                for vertex in range(vertex_count)
                if (mask >> vertex) & 1
            )
            if weight > best_weight:
                best_weight = weight
                best_mask = mask

        graph_bound = sum(
            Fraction(weights[vertex], degree[vertex] + 1)
            for vertex in range(vertex_count)
        )
        atom_local_bound = sum(
            Fraction(
                weights[vertex],
                local_shadow_bound[vertex] + 1,
            )
            for vertex in range(vertex_count)
        )
        assert Fraction(best_weight, 1) >= graph_bound
        assert graph_bound >= atom_local_bound

        for edge in hyperedges:
            assert sum(
                1
                for vertex in edge
                if (best_mask >> vertex) & 1
            ) <= 1

        vertices += vertex_count
        conflict_hyperedges += len(hyperedges)
        shadow_edges_total += len(shadow_edges)
        candidate_weight_units += sum(weights)
        bound_checks += 1

    print(f"systems={SYSTEMS}")
    print(f"vertices={vertices}")
    print(f"conflict_hyperedges={conflict_hyperedges}")
    print(f"higher_order_hyperedges={higher_order_hyperedges}")
    print(f"shadow_edges={shadow_edges_total}")
    print(f"candidate_weight_units={candidate_weight_units}")
    print(f"bound_checks={bound_checks}")


if __name__ == "__main__":
    main()
