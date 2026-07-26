#!/usr/bin/env python3
"""Finite checks for SAS5aj--SAS5an."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product


BANK = ((0, 1), (2, 3), (4, 5))
SCOPES = tuple(combinations(range(6), 3))


def apply_swap(colouring: tuple[int, ...], pair: tuple[int, int]) -> tuple[int, ...]:
    result = list(colouring)
    left, right = pair
    result[left], result[right] = result[right], result[left]
    return tuple(result)


def satisfied(
    colouring: tuple[int, ...],
    scope: tuple[int, int, int],
    required: tuple[int, int, int],
) -> bool:
    return all(colouring[column] == label for column, label in zip(scope, required))


def interaction_graph(
    family: tuple[tuple[int, int, int], ...],
) -> tuple[set[int], ...]:
    adjacency = [set() for _ in BANK]
    for first, second in combinations(range(len(BANK)), 2):
        for scope in family:
            if set(scope) & set(BANK[first]) and set(scope) & set(BANK[second]):
                adjacency[first].add(second)
                adjacency[second].add(first)
                break
    return tuple(adjacency)


def greedy_colours(adjacency: tuple[set[int], ...]) -> tuple[int, ...]:
    colours: list[int] = []
    for vertex in range(len(adjacency)):
        blocked = {
            colours[neighbour]
            for neighbour in adjacency[vertex]
            if neighbour < len(colours)
        }
        colour = 0
        while colour in blocked:
            colour += 1
        colours.append(colour)
    return tuple(colours)


def verify_degree_and_gain(counts: Counter[str]) -> None:
    for size in range(1, 5):
        for family in combinations(SCOPES, size):
            incidence = [
                sum(column in scope for scope in family)
                for column in range(6)
            ]
            lam = max(incidence)
            adjacency = interaction_graph(family)
            maximum_degree = max((len(neighbours) for neighbours in adjacency), default=0)
            assert maximum_degree <= 4 * lam

            colours = greedy_colours(adjacency)
            assert max(colours, default=0) + 1 <= maximum_degree + 1
            for gains in product(range(4), repeat=len(BANK)):
                total = sum(gains)
                if total == 0:
                    continue
                class_weights: dict[int, int] = {}
                for vertex, colour in enumerate(colours):
                    class_weights[colour] = class_weights.get(colour, 0) + gains[vertex]
                assert max(class_weights.values()) * (maximum_degree + 1) >= total
                counts["gain colourings"] += 1
            counts["constraint families"] += 1


def verify_record_additivity(counts: Counter[str]) -> None:
    for scope in SCOPES:
        for required in product((0, 1), repeat=3):
            for colouring in product((0, 1), repeat=6):
                base = int(satisfied(colouring, scope, required))
                individual_changes = []
                repair_count = 0
                for pair in BANK:
                    changed = apply_swap(colouring, pair)
                    value = int(satisfied(changed, scope, required))
                    individual_changes.append(value - base)
                    if base == 0 and value == 1:
                        repair_count += 1
                assert repair_count <= 3
                counts["repair multiplicity tests"] += 1

                for mask in range(1 << len(BANK)):
                    selected = [
                        index
                        for index in range(len(BANK))
                        if (mask >> index) & 1
                    ]
                    touched = sum(
                        bool(set(scope) & set(BANK[index]))
                        for index in selected
                    )
                    if touched > 1:
                        continue
                    batch = colouring
                    for index in selected:
                        batch = apply_swap(batch, BANK[index])
                    batch_change = int(satisfied(batch, scope, required)) - base
                    assert batch_change == sum(
                        individual_changes[index]
                        for index in selected
                    )
                    counts["additivity tests"] += 1


def verify_changed_record_cap(counts: Counter[str]) -> None:
    for size in range(1, 6):
        for family in combinations(SCOPES, size):
            incidence = [
                sum(column in scope for scope in family)
                for column in range(6)
            ]
            lam = max(incidence)
            for pair in BANK:
                changed_records = sum(
                    bool(set(scope) & set(pair))
                    for scope in family
                )
                assert changed_records <= 2 * lam
                counts["endpoint collateral systems"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_degree_and_gain(counts)
    verify_record_additivity(counts)
    verify_changed_record_cap(counts)
    print("SAS5aj--SAS5an donor batch energy audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
