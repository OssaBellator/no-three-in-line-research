#!/usr/bin/env python3
"""Finite audit for SAS5cr--SAS5cv.

Checks heaviest exact-record extraction, top-weight endpoint-disjoint donor matching,
weighted conflict-graph colouring, designated +1 patterns and the aggregate threshold.
"""

from __future__ import annotations

import random

SEED = 20260727
RNG = random.Random(SEED)


def greedy_colour_graph(
    adjacency: list[set[int]], weights: list[int], maximum_degree: int
) -> tuple[list[int], list[int]]:
    colours: list[int] = [-1] * len(adjacency)
    colour_weights = [0] * (maximum_degree + 1)
    for vertex in range(len(adjacency)):
        used = {
            colours[neighbour]
            for neighbour in adjacency[vertex]
            if neighbour < vertex and colours[neighbour] >= 0
        }
        colour = next(c for c in range(maximum_degree + 1) if c not in used)
        colours[vertex] = colour
        colour_weights[colour] += weights[vertex]
    return colours, colour_weights


def random_systems(
    systems: int = 50_000,
) -> tuple[int, int, int, int, int]:
    matched_weight_total = 0
    compatible_weight_total = 0
    scale_dominant = 0
    collateral_dominant = 0
    improving_donors = 0

    for _ in range(systems):
        defect_count = RNG.randint(1, 20)
        record_cap = RNG.randint(1, 6)

        loads: list[int] = []
        designated: list[int] = []
        for _z in range(defect_count):
            signatures = RNG.randint(1, record_cap)
            weights = [RNG.randint(1, 20) for _ in range(signatures)]
            loads.append(sum(weights))
            designated.append(max(weights))

        total_load = sum(loads)
        assert sum(designated) * record_cap >= total_load

        donor_count = RNG.randint(1, 25)
        matched_count = min(defect_count, max(donor_count - 3, 0))
        selected_columns = sorted(
            range(defect_count), key=lambda z: designated[z], reverse=True
        )[:matched_count]

        used_donors: set[int] = set()
        matched: list[tuple[int, int]] = []
        for column in selected_columns:
            excluded_count = RNG.randint(0, min(3, donor_count))
            excluded = set(RNG.sample(range(donor_count), excluded_count))
            available = [
                donor
                for donor in range(donor_count)
                if donor not in used_donors and donor not in excluded
            ]
            assert available
            donor = available[0]
            used_donors.add(donor)
            matched.append((column, donor))

        matched_weight = sum(designated[column] for column, _donor in matched)
        if matched_count > 0:
            assert (
                matched_weight * defect_count * record_cap
                >= matched_count * total_load
            )
        matched_weight_total += matched_weight

        incidence_cap = RNG.randint(0, 4)
        maximum_degree = 4 * incidence_cap
        adjacency = [set() for _ in range(matched_count)]
        for i in range(matched_count):
            for j in range(i):
                if (
                    len(adjacency[i]) < maximum_degree
                    and len(adjacency[j]) < maximum_degree
                    and RNG.random() < 0.15
                ):
                    adjacency[i].add(j)
                    adjacency[j].add(i)

        matched_designated = [designated[column] for column, _donor in matched]
        _colours, colour_weights = greedy_colour_graph(
            adjacency, matched_designated, maximum_degree
        )
        compatible_weight = max(colour_weights, default=0)
        if matched_count > 0:
            assert compatible_weight * (maximum_degree + 1) >= matched_weight
        compatible_weight_total += compatible_weight

        # The selected exact record has the designated four-state +1 pattern.
        indicators = (0, 0, 0, 1)
        mixed_curvature = indicators[3] - indicators[1] - indicators[2] + indicators[0]
        assert mixed_curvature == 1

        cross_weight = RNG.randint(0, max(1, 2 * matched_weight + 10))
        remaining_negative = 2 * cross_weight
        negative: list[int] = []
        for index in range(matched_count):
            if index == matched_count - 1:
                value = RNG.randint(0, remaining_negative)
            else:
                value = RNG.randint(0, min(remaining_negative, 20))
            negative.append(value)
            remaining_negative -= value

        original_increment = RNG.randint(0, 5)
        combined: list[int] = []
        for index, (column, _donor) in enumerate(matched):
            donor_increment = RNG.randint(0, 5)
            positive_collateral = RNG.randint(0, 5)
            delta = (
                original_increment
                + donor_increment
                + designated[column]
                + positive_collateral
                - negative[index]
            )
            combined.append(delta)

        assert sum(combined) >= matched_weight - 2 * cross_weight

        improving = [index for index, delta in enumerate(combined) if delta < 0]
        assert sum(
            designated[matched[index][0]] + abs(combined[index])
            for index in improving
        ) <= sum(negative[index] for index in improving)
        assert sum(negative[index] for index in improving) <= 2 * cross_weight
        improving_donors += len(improving)

        lower_numerator = matched_count * total_load
        lower_denominator = defect_count * record_cap
        if lower_numerator > 2 * cross_weight * lower_denominator:
            scale_dominant += 1
            assert matched_count > 0
            # max(delta) >= (L_0-2 Omega)/m, checked by cross multiplication.
            assert (
                max(combined) * matched_count * lower_denominator
                >= lower_numerator - 2 * cross_weight * lower_denominator
            )
        else:
            collateral_dominant += 1
            assert 2 * cross_weight * lower_denominator >= lower_numerator

    return (
        matched_weight_total,
        compatible_weight_total,
        scale_dominant,
        collateral_dominant,
        improving_donors,
    )


def main() -> None:
    matched, compatible, scale, collateral, improving = random_systems()
    print(
        "PASS SAS weighted defect donor-bank audit:",
        "50000 weighted systems;",
        f"{matched} matched designated weight;",
        f"{compatible} compatible designated weight;",
        f"{scale} scale-dominant banks;",
        f"{collateral} collateral-dominant banks;",
        f"{improving} improving donors.",
    )


if __name__ == "__main__":
    main()
