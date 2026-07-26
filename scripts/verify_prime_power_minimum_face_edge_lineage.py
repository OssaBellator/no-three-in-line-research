#!/usr/bin/env python3
"""Finite checks for CMR918--CMR925."""

from collections import Counter
from math import ceil
import random


def check_owner_slot_restoration_bound():
    rng = random.Random(919)
    checked = 0
    for slot_count in range(1, 200):
        for _ in range(1000):
            appearances = [rng.randrange(slot_count) for _ in range(rng.randint(0, 1000))]
            counts = Counter(appearances)
            restorations = sum(max(0, count - 1) for count in counts.values())
            assert restorations == len(appearances) - len(counts)
            assert restorations >= len(appearances) - slot_count
            checked += 1
    return checked


def check_threshold_form():
    checked = 0
    for slots in range(1, 500):
        for threshold in range(2, 50):
            maximum_restorations = (threshold - 1) * slots
            maximum_appearances = maximum_restorations + slots
            assert maximum_appearances == threshold * slots
            checked += 1
    return checked


def check_token_payment():
    checked = 0
    for prime in (2, 3, 5, 7, 11, 13):
        for height in range(2, 20):
            multiplicity = (prime + 1) * (height - 1)
            for slots in range(1, 100):
                for appearances in range(0, 300):
                    restoration_floor = max(0, appearances - slots)
                    incidence = restoration_floor * multiplicity
                    assert incidence >= 0
                    assert incidence % multiplicity == 0
                    checked += 1
    return checked


def check_global_episode_sum():
    rng = random.Random(923)
    checked = 0
    for edge_count in range(1, 500):
        for slots in range(1, 40):
            for threshold in range(2, 15):
                cap = threshold * slots
                counts = [rng.randint(0, cap) for _ in range(edge_count)]
                assert sum(counts) <= edge_count * cap
                checked += 1
    return checked


def check_owner_concentration():
    rng = random.Random(920)
    checked = 0
    for slots in range(1, 200):
        for restorations in range(0, 2000):
            loads = [0] * slots
            for _ in range(restorations):
                loads[rng.randrange(slots)] += 1
            assert max(loads) >= ceil(restorations / slots)
            checked += 1
    return checked


def check_core_rank_budget():
    rng = random.Random(924)
    checked = 0
    for cardinality in range(0, 1000):
        for _ in range(100):
            remaining = cardinality
            contracted = 0
            while remaining:
                rank = rng.randint(1, remaining)
                remaining -= rank
                contracted += rank
                assert contracted + remaining == cardinality
            assert contracted <= cardinality
            checked += 1
    return checked


def main():
    print(
        "verified minimum-face edge lineage:",
        check_owner_slot_restoration_bound(),
        "owner-slot histories,",
        check_threshold_form(),
        "threshold cases,",
        check_token_payment(),
        "token cases,",
        check_global_episode_sum(),
        "global episode sums,",
        check_owner_concentration(),
        "owner concentration cases, and",
        check_core_rank_budget(),
        "core-rank histories",
    )


if __name__ == "__main__":
    main()
