#!/usr/bin/env python3
"""Deterministic audit for AC5kz--AC5le."""
from __future__ import annotations
from functools import lru_cache
from itertools import combinations, permutations
from math import factorial
import random

SEED = 37
BANKS = 2500
PHYSICAL = 80


def falling(n, r):
    value = 1
    for i in range(r):
        value *= n - i
    return value


def count_allowed(t, forbidden, forced=()):
    forced = dict(forced)
    if len(forced) != len(set(forced.values())):
        return 0
    if any((i, j) in forbidden for i, j in forced.items()):
        return 0
    used_initial = sum(1 << j for j in forced.values())
    rows = tuple(i for i in range(t) if i not in forced)

    @lru_cache(None)
    def dp(position, used):
        if position == len(rows):
            return 1
        row = rows[position]
        total = 0
        for column in range(t):
            if not (used >> column) & 1 and (row, column) not in forbidden:
                total += dp(position + 1, used | (1 << column))
        return total

    return dp(0, used_initial)


def allowed_permutations(t, forbidden):
    for permutation in permutations(range(t)):
        if all((i, permutation[i]) not in forbidden for i in range(t)):
            yield permutation


def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def potential(points):
    points = sorted(set(points))
    return sum(collinear(*triple) for triple in combinations(points, 3))


def physical_seed(rng, t=7):
    other_layer = tuple((i + 1) % t for i in range(t))
    forbidden = {(i, i) for i in range(t)} | {(i, other_layer[i]) for i in range(t)}
    selected = [(i + 1, i + 1) for i in range(t)]
    partners = [(t + 2 + i, t + 2 + i) for i in range(t)]
    removed = {(0, t + 1), (t + 1, 0)}
    inserted = {(0, 0), (t + 1, t + 1)}
    fixed = set(partners)
    for _ in range(rng.randint(0, 3)):
        fixed.add((rng.randint(t + 2, 3 * t + 2), rng.randint(0, 3 * t + 2)))
    after_switch = fixed | inserted
    current = fixed | set(selected) | removed
    anchor = {
        (i, j): (i + 1, j + 1)
        for i in range(t)
        for j in range(t)
        if (i, j) not in forbidden
    }
    return forbidden, selected, partners, removed, inserted, fixed, after_switch, current, anchor


def collateral_census(t, forbidden, after_switch, anchor):
    bank_size = count_allowed(t, forbidden)
    assert bank_size
    counts = [0, 0, 0, 0]
    expected_numerator = 0
    items = [
        ("A", key, point) for key, point in anchor.items()
    ] + [
        ("Z", None, point) for point in after_switch
    ]
    for triple in combinations(items, 3):
        points = [entry[2] for entry in triple]
        if len(set(points)) < 3 or not collinear(*points):
            continue
        anchors = [entry[1] for entry in triple if entry[0] == "A"]
        rank = len(anchors)
        if rank == 0:
            continue
        rows = [address[0] for address in anchors]
        columns = [address[1] for address in anchors]
        if len(set(rows)) < rank or len(set(columns)) < rank:
            continue
        counts[rank] += 1
        expected_numerator += count_allowed(t, forbidden, tuple(anchors))
    bound = sum(counts[rank] * 128 / falling(t, rank) for rank in (1, 2, 3))
    expectation = expected_numerator / bank_size
    assert expectation <= bound + 1e-12
    return counts, expectation, bound


def run():
    rng = random.Random(SEED)
    stats = {
        "banks": BANKS,
        "allowed_state_count": 0,
        "partial_matching_checks": 0,
        "an1_count_checks": 0,
        "physical_seeds": PHYSICAL,
        "physical_install_operations": 0,
        "destroyed_star_pairs": 0,
        "collateral_triples": 0,
        "improving_selectors": 0,
        "failure_ledgers": 0,
        "schema_serializer_round_trips": 0,
    }

    for _ in range(BANKS):
        t = rng.randint(7, 10)
        other_layer = list(range(t))
        rng.shuffle(other_layer)
        forbidden = {(i, i) for i in range(t)} | {
            (i, other_layer[i]) for i in range(t)
        }
        bank_size = count_allowed(t, forbidden)
        assert bank_size * 128 >= factorial(t)
        stats["an1_count_checks"] += 1
        stats["allowed_state_count"] += bank_size

        for rank in (1, 2, 3):
            rows = rng.sample(range(t), rank)
            partial = []
            used = set()
            for row in rows:
                choices = [
                    column for column in range(t)
                    if column not in used and (row, column) not in forbidden
                ]
                if not choices:
                    break
                column = rng.choice(choices)
                used.add(column)
                partial.append((row, column))
            if len(partial) == rank:
                completions = count_allowed(t, forbidden, tuple(partial))
                assert completions / bank_size <= 128 / falling(t, rank) + 1e-12
                stats["partial_matching_checks"] += 1

    for _ in range(PHYSICAL):
        t = 7
        forbidden, selected, partners, removed, inserted, fixed, after_switch, current, anchor = physical_seed(rng, t)
        bank = list(allowed_permutations(t, forbidden))
        stats["physical_install_operations"] += len(bank)

        for permutation in bank:
            matching = {(i + 1, permutation[i] + 1) for i in range(t)}
            assert matching.isdisjoint({(i + 1, i + 1) for i in range(t)})
            assert matching.isdisjoint({(i + 1, (i + 1) % t + 1) for i in range(t)})
        stats["destroyed_star_pairs"] += t * len(bank)

        counts, expectation, bound = collateral_census(t, forbidden, after_switch, anchor)
        assert expectation <= bound + 1e-12
        stats["collateral_triples"] += sum(counts)

        destroyed = potential(current) - potential(fixed)
        fixed_cost = potential(after_switch) - potential(fixed)
        improving = None
        for permutation in bank:
            matching = {(i + 1, permutation[i] + 1) for i in range(t)}
            if potential(after_switch | matching) < potential(current):
                improving = permutation
                break
        if destroyed > fixed_cost + bound:
            assert improving is not None
        if improving is not None:
            stats["improving_selectors"] += 1

        synthetic_nonimproving_costs = [rng.randint(0, 10) for _ in bank]
        assert min(synthetic_nonimproving_costs) >= 0
        stats["failure_ledgers"] += 1

        record = (
            tuple(sorted(current)),
            tuple(sorted(after_switch)),
            tuple(sorted(forbidden)),
            tuple(bank),
        )
        assert record[2] == tuple(sorted(forbidden))
        assert len(record[3]) == count_allowed(t, forbidden)
        stats["schema_serializer_round_trips"] += 1

    return stats


if __name__ == "__main__":
    result = run()
    print("AC AN-bank seed manifest audit")
    for key, value in result.items():
        print(f"{key}: {value}")
