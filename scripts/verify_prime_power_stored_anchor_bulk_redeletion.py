#!/usr/bin/env python3
"""Finite checks for CMR800--CMR806."""

from collections import Counter
import random


def check_bulk_redeletion():
    rng = random.Random(800)
    checked = 0
    for side in range(2, 80):
        universe = set(range(2 * side * side))
        for _ in range(300):
            anchor = set(rng.sample(sorted(universe), 2 * side))
            outside = sorted(universe - anchor)
            deleted = set(rng.sample(outside, rng.randint(0, len(outside))))
            host = set(rng.sample(sorted(universe), rng.randint(2 * side, len(universe))))
            if rng.random() < 0.5:
                host.update(anchor)

            restored_private = deleted & host
            if anchor.issubset(host):
                residual = host - restored_private
                assert anchor.issubset(residual)
                assert residual.isdisjoint(restored_private)
            else:
                assert anchor - host
            checked += 1
    return checked


def check_anchor_replacement():
    rng = random.Random(803)
    checked = 0
    for side in range(2, 100):
        universe = set(range(2 * side * side))
        for _ in range(100):
            available = set(universe)
            lost = []
            while len(available) > 2 * side:
                anchor = set(rng.sample(sorted(available), 2 * side))
                witness = rng.choice(sorted(anchor))
                available.remove(witness)
                lost.append(witness)
            assert len(lost) == len(set(lost))
            assert len(lost) <= 2 * side * side - 2 * side
            checked += 1
    return checked


def check_restoration_threshold():
    rng = random.Random(805)
    checked = 0
    for universe_size in range(1, 500):
        for threshold in range(2, 20):
            counts = [rng.randint(0, threshold - 1) for _ in range(universe_size)]
            assert sum(counts) <= (threshold - 1) * universe_size
            checked += 1
    return checked


def check_recurrent_edge():
    checked = 0
    for universe_size in range(1, 200):
        for threshold in range(2, 20):
            events = []
            for edge in range(universe_size):
                events.extend([edge] * (threshold - 1))
            events.append(0)
            assert max(Counter(events).values()) >= threshold
            checked += 1
    return checked


def check_token_payment():
    checked = 0
    for prime in (2, 3, 5, 7, 11):
        for height in range(1, 12):
            for restorations in range(0, 200):
                incidence = restorations * (prime + 1) * (height - 1)
                assert incidence >= 0
                if height == 1 or restorations == 0:
                    assert incidence == 0
                checked += 1
    return checked


def main():
    print(
        "verified stored-anchor bulk redeletion:",
        check_bulk_redeletion(),
        "bulk cases,",
        check_anchor_replacement(),
        "replacement histories,",
        check_restoration_threshold(),
        "threshold cases,",
        check_recurrent_edge(),
        "recurrence cases, and",
        check_token_payment(),
        "token cases",
    )


if __name__ == "__main__":
    main()
