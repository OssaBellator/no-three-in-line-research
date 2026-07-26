#!/usr/bin/env python3
"""Finite checks for CMR793--CMR799."""

from collections import Counter
from math import floor
import random


def random_batches(side, rng):
    universe = list(range(2 * side * side))
    anchor = set(rng.sample(universe, 2 * side))
    available = set(universe) - anchor
    batches = []
    while len(available) >= 2 and rng.random() < 0.9:
        size = rng.randint(2, min(len(available), max(2, 2 * side)))
        batch = set(rng.sample(sorted(available), size))
        batches.append(batch)
        available.difference_update(batch)
    return universe, anchor, batches


def check_disjoint_batches():
    rng = random.Random(793)
    checked = 0
    for side in range(2, 60):
        for _ in range(200):
            universe, anchor, batches = random_batches(side, rng)
            for index, batch in enumerate(batches):
                assert len(batch) >= 2
                assert batch.isdisjoint(anchor)
                for later in batches[index + 1 :]:
                    assert batch.isdisjoint(later)
            total = sum(len(batch) for batch in batches)
            assert total <= 2 * side * side - 2 * side
            assert len(batches) <= side * (side - 1)
            checked += 1
    return checked


def reopened_batches(restored, batches):
    return [index for index, batch in enumerate(batches) if batch & restored]


def check_reopening_injection():
    rng = random.Random(795)
    checked = 0
    for side in range(2, 60):
        for _ in range(200):
            universe, _, batches = random_batches(side, rng)
            restored = set(rng.sample(universe, rng.randint(0, min(len(universe), 30))))
            reopened = reopened_batches(restored, batches)
            witnesses = []
            for index in reopened:
                witnesses.append(min(restored & batches[index]))
            assert len(witnesses) == len(set(witnesses))
            assert len(restored) >= len(reopened)
            checked += 1
    return checked


def check_cumulative_thresholds():
    rng = random.Random(796)
    checked = 0
    for universe_size in range(1, 500):
        for threshold in range(2, 15):
            multiplicity = [rng.randint(0, threshold - 1) for _ in range(universe_size)]
            total = sum(multiplicity)
            assert total <= (threshold - 1) * universe_size
            for minimum in range(1, 20):
                resets = total // minimum
                assert resets <= floor((threshold - 1) * universe_size / minimum)
                checked += 1
    return checked


def check_token_identity():
    checked = 0
    for prime in (2, 3, 5, 7, 11):
        for height in range(1, 12):
            for restored in range(0, 200):
                incidence = restored * (prime + 1) * (height - 1)
                assert incidence >= 0
                if restored == 0 or height == 1:
                    assert incidence == 0
                checked += 1
    return checked


def check_one_edge_recurrence():
    checked = 0
    for universe_size in range(1, 200):
        for threshold in range(2, 20):
            labels = []
            for edge in range(universe_size):
                labels.extend([edge] * (threshold - 1))
            labels.append(0)
            assert max(Counter(labels).values()) >= threshold
            checked += 1
    return checked


def main():
    print(
        "verified anchor batch restoration ledger:",
        check_disjoint_batches(),
        "batch systems,",
        check_reopening_injection(),
        "reopening injections,",
        check_cumulative_thresholds(),
        "threshold cases,",
        check_token_identity(),
        "token cases, and",
        check_one_edge_recurrence(),
        "recurrence cases",
    )


if __name__ == "__main__":
    main()
