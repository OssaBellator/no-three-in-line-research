#!/usr/bin/env python3
"""Finite audit for SAS5dm--SAS5dq."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations
import random


def donor_pairs(columns: list[int]) -> list[tuple[int, int]]:
    return [(columns[i], columns[i + 1]) for i in range(0, len(columns) - 1, 2)]


def main() -> None:
    rng = random.Random(20260727)
    stats: Counter[str] = Counter()

    for N in range(5, 11):
        columns = list(range(N))
        omega = {0, 1}
        donors = donor_pairs(columns[2:])
        for scope_tuple in combinations(columns, 3):
            scope = set(scope_tuple)
            repair_incidence = sum(bool(scope & set(tau)) for tau in donors)
            assert repair_incidence <= 3
            stats["repair_scope_tests"] += 1
            if scope & omega:
                positive_incidence = sum(bool(scope & set(tau)) for tau in donors)
                assert positive_incidence <= 2
                stats["positive_scope_tests"] += 1

    for _ in range(30_000):
        donor_count = rng.randint(1, 20)
        record_count = rng.randint(1, 50)
        weights = [rng.randint(1, 20) for _ in range(record_count)]

        donor_selected = [0] * donor_count
        donor_incidence: list[list[int]] = []
        for weight in weights:
            incidence = rng.sample(
                range(donor_count), rng.randint(0, min(3, donor_count))
            )
            donor_incidence.append(incidence)
            for donor in incidence:
                donor_selected[donor] += weight
        donor_union = sum(
            weight for weight, incidence in zip(weights, donor_incidence) if incidence
        )
        assert sum(donor_selected) <= 3 * donor_union
        stats["donor_incidence_systems"] += 1
        stats["donor_selected_mass"] += sum(donor_selected)
        stats["donor_union_mass"] += donor_union

        positive_selected = [0] * donor_count
        positive_incidence: list[list[int]] = []
        for weight in weights:
            incidence = rng.sample(
                range(donor_count), rng.randint(0, min(2, donor_count))
            )
            positive_incidence.append(incidence)
            for donor in incidence:
                positive_selected[donor] += weight
        positive_union = sum(
            weight for weight, incidence in zip(weights, positive_incidence) if incidence
        )
        assert sum(positive_selected) <= 2 * positive_union
        stats["positive_incidence_systems"] += 1
        stats["positive_selected_mass"] += sum(positive_selected)
        stats["positive_union_mass"] += positive_union

    K_0 = 500  # surrogate upper bound with every sampled peel length <= K_0
    for _ in range(100_000):
        peel_count = rng.randint(1, 60)
        assert peel_count <= K_0
        record_weights = [rng.randint(1, 10_000) for _ in range(peel_count)]
        output_types = [rng.choice("ODLP") for _ in range(peel_count)]
        masses = {
            output_type: sum(
                weight
                for weight, assigned in zip(record_weights, output_types)
                if assigned == output_type
            )
            for output_type in "ODLP"
        }

        original_word = max(
            [
                Fraction(weight, 48)
                for weight, output_type in zip(record_weights, output_types)
                if output_type == "O"
            ],
            default=Fraction(),
        )
        assert original_word >= Fraction(masses["O"], 48 * K_0)

        donor_selected_mass = Fraction(masses["D"], 48)
        donor_class_mass = donor_selected_mass / 12
        donor_distinct_union = donor_class_mass / 3
        assert donor_distinct_union >= Fraction(masses["D"], 1728)

        designated_mass = Fraction(masses["L"], 4)
        assert designated_mass >= Fraction(masses["L"], 4)

        positive_selected_mass = Fraction(masses["P"], 96)
        positive_class_mass = positive_selected_mass / 24
        positive_distinct_union = positive_class_mass / 2
        assert positive_distinct_union >= Fraction(masses["P"], 4608)

        total = sum(record_weights)
        dominant = max(masses, key=masses.get)
        assert 4 * masses[dominant] >= total
        if dominant == "O":
            assert original_word >= Fraction(total, 192 * K_0)
        elif dominant == "D":
            assert donor_distinct_union >= Fraction(total, 6912)
        elif dominant == "L":
            assert designated_mass >= Fraction(total, 16)
        else:
            assert positive_distinct_union >= Fraction(total, 18432)

        stats["peel_systems"] += 1
        stats["peel_steps"] += peel_count
        stats[f"dominant_{dominant}"] += 1

    print("SAS multi-peel output batching audit passed")
    for key in sorted(stats):
        print(f"{key}: {stats[key]}")


if __name__ == "__main__":
    main()
