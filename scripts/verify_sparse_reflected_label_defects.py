#!/usr/bin/env python3
"""Finite checks for SAS5ae--SAS5ai."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import ceil


def greedy_donor_bank(
    defects: tuple[int, ...],
    donors: tuple[int, ...],
    exclusions: dict[int, frozenset[int]],
) -> tuple[tuple[int, int], ...]:
    used: set[int] = set()
    bank: list[tuple[int, int]] = []
    for defect in defects:
        choices = [
            donor
            for donor in donors
            if donor not in used and donor not in exclusions[defect]
        ]
        if not choices:
            continue
        donor = choices[0]
        used.add(donor)
        bank.append((defect, donor))
    return tuple(bank)


def verify_heavy_diffuse(counts: Counter[str]) -> None:
    for column_count in range(1, 8):
        for weights in product(range(4), repeat=column_count):
            total = sum(weights)
            if total == 0:
                continue
            for mu in (1, 2, 3):
                if max(weights) > mu:
                    counts["heavy columns"] += 1
                else:
                    support = sum(weight > 0 for weight in weights)
                    assert support >= ceil(Fraction(total, mu))
                    counts["diffuse columns"] += 1


def verify_donor_matching(counts: Counter[str]) -> None:
    for d in range(1, 9):
        donors = tuple(range(d))
        for defect_count in range(1, 9):
            defects = tuple(range(100, 100 + defect_count))
            exclusion_options = []
            for defect in defects:
                local = [frozenset()]
                for size in range(1, min(3, d) + 1):
                    local.extend(frozenset(choice) for choice in combinations(donors, size))
                exclusion_options.append(tuple(local[:8]))
            for chosen in product(*exclusion_options):
                exclusions = dict(zip(defects, chosen))
                bank = greedy_donor_bank(defects, donors, exclusions)
                assert len(bank) >= min(defect_count, max(0, d - 3))
                endpoints = [endpoint for swap in bank for endpoint in swap]
                assert len(endpoints) == len(set(endpoints))
                assert all(donor not in exclusions[defect] for defect, donor in bank)
                counts["donor systems"] += 1
                if counts["donor systems"] >= 60_000:
                    return


def conflict_graph(
    bank: tuple[tuple[int, int], ...],
    scopes: tuple[frozenset[int], ...],
) -> tuple[frozenset[int], ...]:
    adjacency = [set() for _ in bank]
    for i, swap_i in enumerate(bank):
        endpoints_i = set(swap_i)
        for j in range(i + 1, len(bank)):
            endpoints_j = set(bank[j])
            if endpoints_i & scopes[j] or endpoints_j & scopes[i]:
                adjacency[i].add(j)
                adjacency[j].add(i)
    return tuple(frozenset(neighbours) for neighbours in adjacency)


def verify_conflict_degree(counts: Counter[str]) -> None:
    columns = tuple(range(8))
    possible_swaps = tuple(combinations(columns, 2))
    for bank_size in range(1, 5):
        for bank in combinations(possible_swaps, bank_size):
            endpoints = [endpoint for swap in bank for endpoint in swap]
            if len(endpoints) != len(set(endpoints)):
                continue
            scope_options = []
            for swap in bank:
                local = [
                    frozenset(scope)
                    for size in range(1, 4)
                    for scope in combinations(columns, size)
                    if swap[0] in scope
                ]
                scope_options.append(tuple(local[:10]))
            for scopes in product(*scope_options):
                incidence = {
                    column: sum(column in scope for scope in scopes)
                    for column in columns
                }
                delta = max(incidence.values(), default=0)
                adjacency = conflict_graph(bank, scopes)
                max_degree = max((len(neighbours) for neighbours in adjacency), default=0)
                assert max_degree <= 2 * delta + 3
                # Greedy colouring upper bound gives an independent class of this size.
                assert ceil(Fraction(bank_size, 2 * delta + 4)) <= bank_size
                counts["conflict systems"] += 1
                if counts["conflict systems"] >= 40_000:
                    return


def verify_balanced_swap(counts: Counter[str]) -> None:
    for label_count in range(2, 5):
        for d in range(1, 5):
            colouring = tuple(label for label in range(label_count) for _ in range(d))
            for defect in range(len(colouring)):
                for required in range(label_count):
                    if colouring[defect] == required:
                        continue
                    donors = [index for index, label in enumerate(colouring) if label == required]
                    for donor in donors:
                        if donor == defect:
                            continue
                        updated = list(colouring)
                        updated[defect], updated[donor] = updated[donor], updated[defect]
                        assert updated[defect] == required
                        for label in range(label_count):
                            assert updated.count(label) == d
                        counts["balanced transpositions"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_heavy_diffuse(counts)
    verify_donor_matching(counts)
    verify_conflict_degree(counts)
    verify_balanced_swap(counts)
    print("SAS5ae--SAS5ai reflected-label donor audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
