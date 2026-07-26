#!/usr/bin/env python3
"""Finite checks for SAS5ao--SAS5as."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from math import ceil


def greedy_colour_classes(
    vertices: tuple[int, ...],
    adjacency: dict[int, set[int]],
) -> list[list[int]]:
    colours: dict[int, int] = {}
    for vertex in vertices:
        used = {
            colours[neighbour]
            for neighbour in adjacency[vertex]
            if neighbour in colours
        }
        colour = 0
        while colour in used:
            colour += 1
        colours[vertex] = colour
    classes: defaultdict[int, list[int]] = defaultdict(list)
    for vertex, colour in colours.items():
        classes[colour].append(vertex)
    return list(classes.values())


def verify_banks(counts: Counter[str]) -> None:
    for bank_size in range(1, 8):
        defects = tuple(range(bank_size))
        donors = tuple(range(bank_size, 2 * bank_size))
        fixed = (2 * bank_size, 2 * bank_size + 1, 2 * bank_size + 2)

        for mode in range(4):
            labels = {column: 0 for column in defects}
            labels.update({column: 1 for column in donors})
            labels.update({column: 2 for column in fixed})

            scopes: list[tuple[int, int, int]] = []
            requirements: list[dict[int, int]] = []

            for index in range(bank_size):
                if mode == 0 or bank_size == 1:
                    candidates = [fixed[0], fixed[1], fixed[2]]
                elif mode == 1:
                    candidates = [
                        donors[(index + 1) % bank_size],
                        fixed[0],
                        fixed[1],
                        fixed[2],
                    ]
                elif mode == 2:
                    candidates = [
                        defects[(index + 1) % bank_size],
                        donors[(index + 2) % bank_size],
                        fixed[0],
                        fixed[1],
                        fixed[2],
                    ]
                else:
                    candidates = [
                        donors[(index + 1) % bank_size],
                        defects[(index + 2) % bank_size],
                        fixed[0],
                        fixed[1],
                        fixed[2],
                    ]

                selected = [defects[index]]
                for candidate in candidates:
                    if candidate == donors[index]:
                        continue
                    if candidate not in selected:
                        selected.append(candidate)
                    if len(selected) == 3:
                        break
                assert len(selected) == 3

                scope = tuple(selected)
                required = {column: labels[column] for column in scope}
                required[defects[index]] = 1
                scopes.append(scope)
                requirements.append(required)

            records = [
                (
                    scopes[index],
                    tuple(sorted(requirements[index].items())),
                    index,
                )
                for index in range(bank_size)
            ]
            assert len(set(records)) == bank_size

            for index in range(bank_size):
                before = all(
                    labels[column] == requirements[index][column]
                    for column in scopes[index]
                )
                after = dict(labels)
                defect = defects[index]
                donor = donors[index]
                after[defect], after[donor] = after[donor], after[defect]
                assert not before
                assert all(
                    after[column] == requirements[index][column]
                    for column in scopes[index]
                )
                counts["individual designated repairs"] += 1

            adjacency = {index: set() for index in range(bank_size)}
            for left, right in combinations(range(bank_size), 2):
                left_endpoints = {defects[left], donors[left]}
                right_endpoints = {defects[right], donors[right]}
                if any(
                    set(scope) & left_endpoints
                    and set(scope) & right_endpoints
                    for scope in scopes
                ):
                    adjacency[left].add(right)
                    adjacency[right].add(left)

            incidence = Counter(
                column
                for scope in scopes
                for column in scope
            )
            lambda_cap = max(incidence.values(), default=0)
            maximum_degree = max(
                (len(adjacency[index]) for index in range(bank_size)),
                default=0,
            )
            assert maximum_degree <= 4 * lambda_cap

            classes = greedy_colour_classes(
                tuple(range(bank_size)),
                adjacency,
            )
            independent = max(classes, key=len)
            assert len(independent) >= ceil(
                bank_size / (4 * lambda_cap + 1)
            )

            simultaneous = dict(labels)
            for index in independent:
                defect = defects[index]
                donor = donors[index]
                simultaneous[defect], simultaneous[donor] = (
                    simultaneous[donor],
                    simultaneous[defect],
                )
            for index in independent:
                assert all(
                    simultaneous[column] == requirements[index][column]
                    for column in scopes[index]
                )
                counts["simultaneous designated repairs"] += 1
            counts["donor bank systems"] += 1


def verify_quantitative_router(counts: Counter[str]) -> None:
    for weight in range(1, 31):
        for label_count in range(1, 6):
            for threshold in range(1, 7):
                for donor_count in range(1, 11):
                    for lambda_cap in range(1, 6):
                        bank_bound = min(
                            ceil(weight / (label_count * threshold)),
                            max(0, donor_count - 3),
                        )
                        compatible = ceil(
                            bank_bound / (4 * lambda_cap + 1)
                        )
                        assert compatible >= 0
                        assert compatible <= bank_bound
                        counts["quantitative routers"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_banks(counts)
    verify_quantitative_router(counts)
    print("SAS5ao--SAS5as designated mirror-repair audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
