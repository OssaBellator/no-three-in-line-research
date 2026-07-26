#!/usr/bin/env python3
"""Finite checks for CMR807--CMR813."""

from collections import Counter
import random


def normalize(host, private):
    return set(host) - set(private)


def check_projection_identities():
    rng = random.Random(807)
    checked = 0
    for universe_size in range(1, 500):
        universe = list(range(universe_size))
        for _ in range(100):
            private = set(rng.sample(universe, rng.randint(0, universe_size)))
            host = set(rng.sample(universe, rng.randint(0, universe_size)))
            normalized = normalize(host, private)
            assert normalized.isdisjoint(private)
            assert normalize(normalized, private) == normalized

            restored = set(rng.sample(sorted(private), rng.randint(0, len(private))))
            assert normalize(host | restored, private) == normalized
            checked += 1
    return checked


def check_nonprivate_witness():
    rng = random.Random(810)
    checked = 0
    for universe_size in range(1, 500):
        universe = list(range(universe_size))
        for _ in range(100):
            private = set(rng.sample(universe, rng.randint(0, universe_size)))
            first = set(rng.sample(universe, rng.randint(0, universe_size)))
            second = set(rng.sample(universe, rng.randint(0, universe_size)))
            norm_first = normalize(first, private)
            norm_second = normalize(second, private)
            if norm_first != norm_second:
                witness = (first ^ second) - private
                assert witness
            checked += 1
    return checked


def check_context_recurrence():
    checked = 0
    for universe_size in range(1, 300):
        for threshold in range(2, 20):
            labels = []
            for edge in range(universe_size):
                labels.extend([edge] * (threshold - 1))
            assert len(labels) == (threshold - 1) * universe_size
            labels.append(0)
            assert max(Counter(labels).values()) >= threshold
            checked += 1
    return checked


def check_anchor_preservation():
    rng = random.Random(809)
    checked = 0
    for side in range(1, 100):
        universe = list(range(2 * side * side))
        for _ in range(100):
            anchor = set(rng.sample(universe, min(2 * side, len(universe))))
            outside = [edge for edge in universe if edge not in anchor]
            private = set(rng.sample(outside, rng.randint(0, len(outside))))
            host = set(rng.sample(universe, rng.randint(0, len(universe)))) | anchor
            normalized = normalize(host, private)
            assert anchor.issubset(normalized)
            reopened = set(rng.sample(sorted(private), rng.randint(0, len(private))))
            renormalized = normalize(host | reopened, private)
            assert renormalized == normalized
            assert anchor.issubset(renormalized)
            checked += 1
    return checked


def main():
    print(
        "verified private batch normalization:",
        check_projection_identities(),
        "projection cases,",
        check_nonprivate_witness(),
        "witness cases,",
        check_context_recurrence(),
        "recurrence cases, and",
        check_anchor_preservation(),
        "anchor cases",
    )


if __name__ == "__main__":
    main()
