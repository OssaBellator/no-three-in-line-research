#!/usr/bin/env python3
"""Finite audit for SAS5ec--SAS5eh common-step pair execution."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from random import Random


def path_matching(length: int, rng: Random) -> list[tuple[int, int]]:
    edges: list[tuple[int, int]] = []
    parameter = 0
    while parameter < length - 1:
        if rng.random() < 0.65:
            edges.append((parameter, parameter + 1))
            parameter += 2
        else:
            parameter += 1
    return edges


def maximum_support_reuse(supports: list[set[int]]) -> int:
    incidence: defaultdict[int, int] = defaultdict(int)
    for support in supports:
        for coordinate in support:
            incidence[coordinate] += 1
    return max(incidence.values(), default=0)


def greedy_coloring(adjacency: list[set[int]]) -> list[int]:
    order = sorted(
        range(len(adjacency)),
        key=lambda vertex: (len(adjacency[vertex]), vertex),
        reverse=True,
    )
    colours = [-1] * len(adjacency)
    for vertex in order:
        used = {colours[n] for n in adjacency[vertex] if colours[n] >= 0}
        colour = 0
        while colour in used:
            colour += 1
        colours[vertex] = colour
    return colours


def main() -> None:
    rng = Random(314159)
    stats: defaultdict[str, int] = defaultdict(int)

    for _ in range(60_000):
        length = rng.randint(2, 32)
        edges = path_matching(length, rng)

        direction = rng.choice([value for value in range(-6, 7) if value])
        offset = rng.randint(-20, 20)
        double_supports = [
            {offset + direction * left, offset + direction * right}
            for left, right in edges
        ]
        assert maximum_support_reuse(double_supports) <= 1

        first, second = rng.sample(
            [value for value in range(-6, 7) if value],
            2,
        )
        centre = rng.randint(-20, 20)
        singleton_supports = [
            {
                centre + first * left,
                centre + second * left,
                centre + first * right,
                centre + second * right,
            }
            for left, right in edges
        ]
        assert maximum_support_reuse(singleton_supports) <= 2

        row_offsets = sorted(rng.sample(range(-7, 8), 3))
        row_supports = [
            {
                left + row_offsets[0],
                left + row_offsets[1],
                left + row_offsets[2],
                right + row_offsets[0],
                right + row_offsets[1],
                right + row_offsets[2],
            }
            for left, right in edges
        ]
        assert maximum_support_reuse(row_supports) <= 3

        stats["coordinate_systems"] += 1
        stats["adjacent_pairs"] += len(edges)

    for _ in range(25_000):
        kind = rng.choice(("double", "singleton"))
        length = rng.randint(4, 20)
        edges = path_matching(length, rng)
        if not edges:
            continue

        if kind == "double":
            direction = rng.choice([value for value in range(-5, 6) if value])
            offset = rng.randint(-10, 10)
            supports = [
                {offset + direction * left, offset + direction * right}
                for left, right in edges
            ]
            support_size, reuse = 2, 1
        else:
            first, second = rng.sample(
                [value for value in range(-5, 6) if value],
                2,
            )
            centre = rng.randint(-10, 10)
            supports = [
                {
                    centre + first * left,
                    centre + second * left,
                    centre + first * right,
                    centre + second * right,
                }
                for left, right in edges
            ]
            support_size, reuse = 4, 2

        assert maximum_support_reuse(supports) <= reuse

        universe = set(range(-30, 50))
        universe.update(set().union(*supports))
        columns = sorted(universe)
        incidence_cap = rng.randint(1, 6)

        incidence: defaultdict[int, int] = defaultdict(int)
        scopes: list[tuple[int, int, int]] = []
        target_scope_count = rng.randint(6, 48)
        attempts = 0
        while len(scopes) < target_scope_count and attempts < 2_000:
            attempts += 1
            scope = tuple(rng.sample(columns, 3))
            if all(incidence[column] < incidence_cap for column in scope):
                scopes.append(scope)
                for column in scope:
                    incidence[column] += 1

        adjacency = [set() for _ in supports]
        for left, right in combinations(range(len(supports)), 2):
            if any(
                set(scope) & supports[left] and set(scope) & supports[right]
                for scope in scopes
            ):
                adjacency[left].add(right)
                adjacency[right].add(left)

        degree_cap = support_size * incidence_cap * (3 * reuse - 1)
        assert max((len(row) for row in adjacency), default=0) <= degree_cap

        colours = greedy_coloring(adjacency)
        assert max(colours, default=-1) + 1 <= degree_cap + 1

        bottleneck = [
            Fraction(rng.randint(1, 30), rng.randint(1, 8))
            for _ in supports
        ]
        colour_weight: defaultdict[int, Fraction] = defaultdict(Fraction)
        for vertex, colour in enumerate(colours):
            colour_weight[colour] += bottleneck[vertex]
        selected_colour = max(colour_weight, key=colour_weight.get)
        selected = [
            vertex
            for vertex, colour in enumerate(colours)
            if colour == selected_colour
        ]
        assert colour_weight[selected_colour] >= (
            sum(bottleneck, Fraction()) / (degree_cap + 1)
        )

        state = {column: rng.randrange(2) for column in columns}
        requirements = [
            {column: rng.randrange(2) for column in scope}
            for scope in scopes
        ]

        def energy(configuration: dict[int, int]) -> int:
            return sum(
                all(configuration[column] == value for column, value in record.items())
                for record in requirements
            )

        base_energy = energy(state)
        individual_changes: list[int] = []
        changed_record_sets: list[set[int]] = []

        for vertex in selected:
            updated = state.copy()
            for column in supports[vertex]:
                updated[column] ^= 1
            individual_changes.append(energy(updated) - base_energy)
            changed_record_sets.append(
                {
                    index
                    for index, record in enumerate(requirements)
                    if any(column in supports[vertex] for column in record)
                }
            )

        for left, right in combinations(range(len(selected)), 2):
            assert changed_record_sets[left].isdisjoint(
                changed_record_sets[right]
            )

        batch = state.copy()
        for vertex in selected:
            for column in supports[vertex]:
                batch[column] ^= 1
        assert energy(batch) - base_energy == sum(individual_changes)

        stats["interaction_systems"] += 1
        stats["constraint_scopes"] += len(scopes)
        stats["selected_operations"] += len(selected)
        if kind == "double":
            stats["double_systems"] += 1
        else:
            stats["singleton_systems"] += 1

    print("SAS common-step pair execution audit passed")
    for key in sorted(stats):
        print(f"{key}: {stats[key]}")


if __name__ == "__main__":
    main()
