#!/usr/bin/env python3
"""Finite checks for corrected SAS5ao--SAS5as composed mirror repairs."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from math import ceil


def satisfied(labels: dict[int, int], scope: tuple[int, int, int], required: dict[int, int]) -> bool:
    return all(labels[column] == required[column] for column in scope)


def apply_swap(labels: dict[int, int], left: int, right: int) -> dict[int, int]:
    result = dict(labels)
    result[left], result[right] = result[right], result[left]
    return result


def greedy_colour_classes(vertices: tuple[int, ...], adjacency: dict[int, set[int]]) -> list[list[int]]:
    colours: dict[int, int] = {}
    for vertex in vertices:
        used = {colours[n] for n in adjacency[vertex] if n in colours}
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
        x = 2 * bank_size
        y = x + 1
        fixed = (x + 2, x + 3, x + 4)

        for mode in range(4):
            labels = {column: 0 for column in defects}
            labels.update({column: 2 for column in donors})
            labels[x] = 0
            labels[y] = 1
            labels.update({column: 1 for column in fixed})

            scopes: list[tuple[int, int, int]] = []
            requirements: list[dict[int, int]] = []

            for index in range(bank_size):
                defect = defects[index]
                if mode == 0:
                    # Double-scope mirror record.
                    scope = (x, y, defect)
                    required = {x: 1, y: 0, defect: 2}
                elif mode == 1:
                    # Singleton x-word with one fixed non-swapped column.
                    other = fixed[index % len(fixed)]
                    scope = (x, defect, other)
                    required = {x: 1, defect: 2, other: labels[other]}
                elif mode == 2:
                    # Singleton y-word.
                    other = fixed[index % len(fixed)]
                    scope = (y, defect, other)
                    required = {y: 0, defect: 2, other: labels[other]}
                else:
                    # Create cross-record donor interactions while keeping own donor outside.
                    other = donors[(index + 1) % bank_size] if bank_size > 1 else fixed[0]
                    scope = (x, defect, other)
                    required = {x: 1, defect: 2, other: labels[other]}
                assert donors[index] not in scope
                scopes.append(scope)
                requirements.append(required)

            records = [(scopes[i], tuple(sorted(requirements[i].items())), i) for i in range(bank_size)]
            assert len(set(records)) == bank_size

            post_omega = apply_swap(labels, x, y)
            for index in range(bank_size):
                before = satisfied(labels, scopes[index], requirements[index])
                donor_after = apply_swap(labels, defects[index], donors[index])
                composed = apply_swap(post_omega, defects[index], donors[index])
                assert not before
                # Donor alone is not required to repair the mirror record.
                if mode == 0:
                    assert not satisfied(donor_after, scopes[index], requirements[index])
                assert satisfied(composed, scopes[index], requirements[index])
                counts["individual composed repairs"] += 1

            adjacency = {index: set() for index in range(bank_size)}
            for left, right in combinations(range(bank_size), 2):
                left_endpoints = {defects[left], donors[left]}
                right_endpoints = {defects[right], donors[right]}
                if any(
                    set(scope) & left_endpoints and set(scope) & right_endpoints
                    for scope in scopes
                ):
                    adjacency[left].add(right)
                    adjacency[right].add(left)

            incidence = Counter(column for scope in scopes for column in scope)
            lambda_cap = max(incidence.values(), default=0)
            maximum_degree = max((len(adjacency[i]) for i in range(bank_size)), default=0)
            assert maximum_degree <= 4 * lambda_cap

            classes = greedy_colour_classes(tuple(range(bank_size)), adjacency)
            independent = max(classes, key=len)
            assert len(independent) >= ceil(bank_size / (4 * lambda_cap + 1))

            simultaneous = dict(post_omega)
            for index in independent:
                simultaneous = apply_swap(simultaneous, defects[index], donors[index])
            for index in independent:
                assert satisfied(simultaneous, scopes[index], requirements[index])
                counts["simultaneous composed repairs"] += 1

            # Exact donor additivity relative to the post-omega coloring.
            base_energy = sum(satisfied(post_omega, scopes[i], requirements[i]) for i in range(bank_size))
            individual_delta = 0
            for index in independent:
                one = apply_swap(post_omega, defects[index], donors[index])
                individual_delta += sum(
                    satisfied(one, scopes[i], requirements[i])
                    - satisfied(post_omega, scopes[i], requirements[i])
                    for i in range(bank_size)
                )
            combined_delta = sum(
                satisfied(simultaneous, scopes[i], requirements[i])
                - satisfied(post_omega, scopes[i], requirements[i])
                for i in range(bank_size)
            )
            assert combined_delta == individual_delta
            assert base_energy + combined_delta == sum(
                satisfied(simultaneous, scopes[i], requirements[i]) for i in range(bank_size)
            )
            counts["post-swap additive banks"] += 1


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
                        compatible = ceil(bank_bound / (4 * lambda_cap + 1))
                        assert 0 <= compatible <= bank_bound
                        counts["quantitative routers"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_banks(counts)
    verify_quantitative_router(counts)
    print("SAS5ao--SAS5as composed mirror-repair audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
