#!/usr/bin/env python3
"""Finite audit for GC2cb--GC2cg.

Checks the multiplicative collateral inequality, inserted-cell/rank localization,
rank-two multiplicity extraction and rank-three weighted link extraction.
"""

from __future__ import annotations

import random
from collections import Counter, defaultdict
from fractions import Fraction

SEED = 20260727
RNG = random.Random(SEED)


def split_positive(total: int, parts: int) -> list[int]:
    if parts == 1:
        return [total]
    cuts = sorted(RNG.sample(range(1, total), parts - 1))
    points = [0, *cuts, total]
    return [points[i + 1] - points[i] for i in range(parts)]


def exhaustive_ratio_checks() -> int:
    checked = 0
    for destroyed in range(2, 21):
        for gain in range(1, destroyed + 1):
            density = Fraction(gain, destroyed)
            for factor_weight in range(1, destroyed + 1):
                raw = density * factor_weight
                for capacity in range(factor_weight + 1):
                    ratio = Fraction(capacity, 1) / raw
                    if ratio <= 1:
                        continue
                    created = destroyed - gain
                    assert Fraction(created, 1) >= (
                        1 - Fraction(1, 1) / ratio
                    ) * destroyed
                    checked += 1
    return checked


def rank_two_extract(
    items: list[tuple[int, Fraction]], delta: int
) -> tuple[str, Fraction]:
    counts = Counter(endpoint for endpoint, _weight in items)
    total = sum(weight for _endpoint, weight in items)
    if max(counts.values(), default=0) > delta:
        return "pair", total

    local_index: Counter[int] = Counter()
    colour_weights = [Fraction(0) for _ in range(delta)]
    for endpoint, weight in items:
        colour = local_index[endpoint]
        assert colour < delta
        colour_weights[colour] += weight
        local_index[endpoint] += 1

    retained = max(colour_weights, default=Fraction(0))
    assert retained >= total / delta
    return "star", retained


def rank_three_extract(
    items: list[tuple[int, int, Fraction]], delta: int
) -> tuple[str, Fraction]:
    degrees: Counter[int] = Counter()
    total = sum(weight for _u, _v, weight in items)
    for u, v, _weight in items:
        degrees[u] += 1
        degrees[v] += 1

    if max(degrees.values(), default=0) > delta:
        return "pair", total

    used_colours: dict[int, set[int]] = defaultdict(set)
    colour_weights: list[Fraction] = []
    for u, v, weight in items:
        colour = 0
        while colour in used_colours[u] or colour in used_colours[v]:
            colour += 1
        assert colour < 2 * delta - 1
        while len(colour_weights) <= colour:
            colour_weights.append(Fraction(0))
        colour_weights[colour] += weight
        used_colours[u].add(colour)
        used_colours[v].add(colour)

    retained = max(colour_weights, default=Fraction(0))
    assert retained >= total / (2 * delta - 1)
    return "star", retained


def random_created_factor_systems(
    systems: int = 50_000,
) -> tuple[int, int, int, int]:
    total_factors = 0
    atomic_outputs = 0
    pair_outputs = 0
    star_outputs = 0

    for _ in range(systems):
        destroyed = RNG.randint(2, 60)
        gain = RNG.randint(1, destroyed - 1)
        created = destroyed - gain
        density = Fraction(gain, destroyed)

        selected_weight = RNG.randint(1, destroyed)
        selected_capacity = selected_weight
        raw = density * selected_weight
        ratio = Fraction(selected_capacity, 1) / raw
        assert ratio > 1
        assert Fraction(created, 1) >= (
            1 - Fraction(1, 1) / ratio
        ) * destroyed

        factor_count = RNG.randint(1, min(created, 25))
        factor_weights = split_positive(created, factor_count)
        groups: dict[tuple[int, int], list[tuple]] = defaultdict(list)

        for integer_weight in factor_weights:
            rank = RNG.randint(1, 3)
            anchor = RNG.randint(0, 1)
            weight = Fraction(integer_weight)
            if rank == 1:
                record = (weight,)
            elif rank == 2:
                record = (RNG.randint(0, 8), weight)
            else:
                u, v = RNG.sample(range(9), 2)
                record = (u, v, weight)
            groups[(anchor, rank)].append(record)
            total_factors += 1

        selected_key = max(
            groups,
            key=lambda key: sum(record[-1] for record in groups[key]),
        )
        selected = groups[selected_key]
        selected_total = sum(record[-1] for record in selected)
        assert selected_total >= Fraction(created, 6)

        delta = RNG.randint(1, 5)
        rank = selected_key[1]
        if rank == 1:
            atomic_outputs += 1
            retained = selected_total
        elif rank == 2:
            outcome, retained = rank_two_extract(selected, delta)
            if outcome == "pair":
                pair_outputs += 1
                continue
            star_outputs += 1
        else:
            outcome, retained = rank_three_extract(selected, delta)
            if outcome == "pair":
                pair_outputs += 1
                continue
            star_outputs += 1

        assert retained >= Fraction(created, 6 * (2 * delta - 1))
        assert retained >= (
            1 - Fraction(1, 1) / ratio
        ) * destroyed / (6 * (2 * delta - 1))

    return total_factors, atomic_outputs, pair_outputs, star_outputs


def main() -> None:
    ratio_cases = exhaustive_ratio_checks()
    total_factors, atomic, pair, star = random_created_factor_systems()
    print(
        "PASS GC multiplicative-overload collateral audit:",
        f"{ratio_cases} exhaustive ratio systems;",
        f"{total_factors} created factor occurrences;",
        f"{atomic} atomic outputs;",
        f"{pair} high-pair outputs;",
        f"{star} endpoint-disjoint star outputs.",
    )


if __name__ == "__main__":
    main()
