#!/usr/bin/env python3
from __future__ import annotations

from collections import defaultdict
from itertools import combinations, permutations
from math import gcd

PRIMES = (11, 13, 17, 19, 23, 29, 31, 37)
EXPECTED = {
    11: (4, 0, {}),
    13: (4, 0, {}),
    17: (5, 0, {}),
    19: (7, 56, {7: 56}),
    23: (7, 144, {6: 240, 7: 144}),
    29: (8, 600, {6: 1304, 7: 504, 8: 96}),
    31: (8, 216, {6: 2696, 7: 112, 8: 104}),
    37: (10, 2512, {6: 8032, 7: 1992, 8: 392, 10: 128}),
}


def hyperbola(prime: int, channel: int) -> set[tuple[int, int]]:
    return {
        (x, channel * pow(x, -1, prime) % prime)
        for x in range(1, prime)
    }


def direction(
    centre: tuple[int, int], point: tuple[int, int]
) -> tuple[int, int]:
    dx = point[0] - centre[0]
    dy = point[1] - centre[1]
    divisor = gcd(abs(dx), abs(dy))
    dx //= divisor
    dy //= divisor
    if dx < 0 or (dx == 0 and dy < 0):
        dx, dy = -dx, -dy
    return dx, dy


def collinear(
    first: tuple[int, int],
    second: tuple[int, int],
    third: tuple[int, int],
) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def potential(points: set[tuple[int, int]]) -> int:
    return sum(
        collinear(*triple)
        for triple in combinations(sorted(points), 3)
    )


def pair_lookup(prime: int):
    hyperbolas = {
        channel: hyperbola(prime, channel)
        for channel in range(1, prime)
    }
    lookup = {}
    for channel, layer in hyperbolas.items():
        for x in range(1, prime):
            for y in range(1, prime):
                centre = (x, y)
                groups: dict[tuple[int, int], list[tuple[int, int]]] = (
                    defaultdict(list)
                )
                for point in layer:
                    if point != centre:
                        groups[direction(centre, point)].append(point)
                pairs = tuple(
                    sorted(
                        pair
                        for group in groups.values()
                        for pair in combinations(sorted(group), 2)
                    )
                )
                lookup[(channel, centre)] = pairs
    return hyperbolas, lookup


def enumerate_seeds(prime: int):
    hyperbolas, lookup = pair_lookup(prime)
    records = []
    histogram: dict[int, int] = defaultdict(int)
    maximum = 0
    for anchor_channel in range(1, prime):
        anchor_layer = hyperbolas[anchor_channel]
        for switch_channel in range(1, prime):
            if anchor_channel == switch_channel:
                continue
            switch_layer = hyperbolas[switch_channel]
            by_column = dict(switch_layer)
            for first_row in range(1, prime):
                first_image = by_column[first_row]
                for second_row in range(first_row + 1, prime):
                    second_image = by_column[second_row]
                    inserted = (
                        (first_row, second_image),
                        (second_row, first_image),
                    )
                    if (
                        inserted[0] in anchor_layer
                        or inserted[1] in anchor_layer
                    ):
                        continue
                    for candidate in inserted:
                        pairs = lookup[(anchor_channel, candidate)]
                        pair_count = len(pairs)
                        maximum = max(maximum, pair_count)
                        if pair_count >= 6:
                            histogram[pair_count] += 1
                        if pair_count >= 7:
                            records.append(
                                (
                                    anchor_channel,
                                    switch_channel,
                                    first_row,
                                    second_row,
                                    candidate,
                                    pairs,
                                )
                            )
    return hyperbolas, records, maximum, dict(histogram)


def evaluate_seed(hyperbolas, record):
    (
        anchor_channel,
        switch_channel,
        first_row,
        second_row,
        _candidate,
        pairs,
    ) = record
    selected = [first for first, _ in pairs[:7]]
    columns = [point[0] for point in selected]
    rows = [point[1] for point in selected]

    switch_layer = hyperbolas[switch_channel]
    by_column = dict(switch_layer)
    removed = {
        (first_row, by_column[first_row]),
        (second_row, by_column[second_row]),
    }
    inserted = {
        (first_row, by_column[second_row]),
        (second_row, by_column[first_row]),
    }
    switched = (switch_layer - removed) | inserted

    forbidden = {(index, index) for index in range(7)}
    switched_by_column = dict(switched)
    for index, column in enumerate(columns):
        opposite_row = switched_by_column[column]
        if opposite_row in rows:
            forbidden.add((index, rows.index(opposite_row)))

    current = hyperbolas[anchor_channel] | switch_layer
    fixed_state = (current - set(selected) - removed) | inserted
    fixed_potential = potential(fixed_state)

    rank_one = [0] * 49
    rank_two: dict[tuple[int, int], int] = defaultdict(int)
    rank_three: dict[tuple[int, int, int], int] = defaultdict(int)
    items = [
        (True, source, target, (columns[source], rows[target]))
        for source in range(7)
        for target in range(7)
        if (source, target) not in forbidden
    ]
    items += [
        (False, -1, -1, point)
        for point in sorted(fixed_state)
    ]

    for triple in combinations(items, 3):
        if not collinear(
            triple[0][3], triple[1][3], triple[2][3]
        ):
            continue
        addresses = sorted(
            item[1] * 7 + item[2]
            for item in triple
            if item[0]
        )
        rank = len(addresses)
        if rank == 0:
            continue
        if (
            len({address // 7 for address in addresses}) != rank
            or len({address % 7 for address in addresses}) != rank
        ):
            continue
        if rank == 1:
            rank_one[addresses[0]] += 1
        elif rank == 2:
            rank_two[tuple(addresses)] += 1
        else:
            rank_three[tuple(addresses)] += 1

    current_potential = potential(current)
    best_potential = 10**9
    best_permutation = None
    bank_size = 0
    improving = 0
    potential_sum = 0
    for permutation in permutations(range(7)):
        if any(
            (source, permutation[source]) in forbidden
            for source in range(7)
        ):
            continue
        bank_size += 1
        addresses = [
            source * 7 + permutation[source]
            for source in range(7)
        ]
        score = fixed_potential + sum(
            rank_one[address] for address in addresses
        )
        score += sum(
            rank_two.get(tuple(sorted((addresses[i], addresses[j]))), 0)
            for i in range(7)
            for j in range(i + 1, 7)
        )
        score += sum(
            rank_three.get(
                tuple(sorted((addresses[i], addresses[j], addresses[k]))),
                0,
            )
            for i in range(7)
            for j in range(i + 1, 7)
            for k in range(j + 1, 7)
        )
        potential_sum += score
        improving += score < current_potential
        if (
            score < best_potential
            or (
                score == best_potential
                and (
                    best_permutation is None
                    or permutation < best_permutation
                )
            )
        ):
            best_potential = score
            best_permutation = permutation

    return {
        "current": current_potential,
        "fixed": fixed_potential,
        "bank": bank_size,
        "best": best_potential,
        "improving": improving,
        "sum": potential_sum,
        "best_permutation": best_permutation,
    }


def main() -> None:
    p31_cache = None
    for prime in PRIMES:
        hyperbolas, seeds, maximum, histogram = enumerate_seeds(prime)
        expected_maximum, expected_count, expected_histogram = EXPECTED[prime]
        assert (
            maximum,
            len(seeds),
            histogram,
        ) == (
            expected_maximum,
            expected_count,
            expected_histogram,
        )
        if prime == 31:
            p31_cache = hyperbolas, seeds

    assert p31_cache is not None
    hyperbolas, seeds = p31_cache
    results = [evaluate_seed(hyperbolas, seed) for seed in seeds]
    assert len(results) == 216
    assert sum(result["improving"] > 0 for result in results) == 140
    assert sum(result["improving"] == 0 for result in results) == 76
    assert max(
        result["current"] - result["best"]
        for result in results
    ) == 33

    best_drop = next(
        (seed, result)
        for seed, result in zip(seeds, results)
        if seed[:5] == (1, 12, 16, 24, (16, 16))
    )
    seed, result = best_drop
    assert (
        len(seed[5]),
        result["bank"],
        result["current"],
        result["fixed"],
        result["best"],
        result["improving"],
        result["best_permutation"],
    ) == (8, 1094, 108, 59, 75, 1083, (2, 0, 6, 4, 5, 3, 1))

    canonical_failure = next(
        (seed, result)
        for seed, result in zip(seeds, results)
        if seed[:5] == (1, 2, 4, 16, (16, 16))
    )
    _, failure = canonical_failure
    assert (
        failure["bank"],
        failure["current"],
        failure["fixed"],
        failure["best"],
        failure["improving"],
        failure["sum"],
    ) == (1088, 106, 88, 108, 0, 135141)

    # Regression guardrail: unchanged switch-layer points remain in every
    # complete successor. Omitting them falsely reports low p=31 values.
    assert failure["fixed"] == 88

    print("AC prime-minus-one seed census audit")
    print("prime_seed_orientations_p31: 216")
    print("improving_orientations_p31: 140")
    print("nonimproving_orientations_p31: 76")
    print("maximum_p31_drop: 33")
    print("best_drop_successor: 75")
    print("canonical_nonimproving_best: 108")


if __name__ == "__main__":
    main()
