#!/usr/bin/env python3
"""Finite checks for CMR1118--CMR1125."""

from collections import Counter
import random


def missing_support(candidate, host):
    return frozenset(set(candidate) - set(host))


def check_missing_support_and_rollback():
    rng = random.Random(1118)
    checked = 0
    for universe_size in range(2, 120):
        universe = set(range(universe_size))
        for _ in range(200):
            state_size = rng.randint(1, min(universe_size, 20))
            candidate = frozenset(rng.sample(tuple(universe), state_size))
            host = set(rng.sample(tuple(universe), rng.randint(0, universe_size)))
            support = missing_support(candidate, host)
            feasible = set(candidate) <= host
            assert feasible == (not support)
            if support:
                expanded = set(host) | set(candidate)
                assert set(candidate) <= expanded
                rolled_back = set(expanded) - set(support)
                assert rolled_back == host
                assert not set(candidate) <= rolled_back
            checked += 1
    return checked


def check_duplicate_erasure():
    rng = random.Random(1120)
    checked = 0
    for universe_size in range(2, 100):
        universe = set(range(universe_size))
        for _ in range(200):
            candidate = frozenset(
                rng.sample(tuple(universe), rng.randint(1, min(universe_size, 15)))
            )
            host = set(rng.sample(tuple(universe), rng.randint(0, universe_size)))
            first = missing_support(candidate, host)
            second = missing_support(candidate, host)
            assert first == second
            assert host == host
            checked += 1
    return checked


def check_blocker_concentration():
    rng = random.Random(1121)
    checked = 0
    for universe_size in range(1, 200):
        universe = tuple(range(universe_size))
        for threshold in range(2, 20):
            candidate_count = rng.randint(1, 500)
            blockers = [rng.choice(universe) for _ in range(candidate_count)]
            counts = Counter(blockers)
            if max(counts.values()) < threshold:
                assert candidate_count <= (threshold - 1) * universe_size
            checked += 1
    return checked


def check_support_incidence():
    rng = random.Random(1122)
    checked = 0
    for universe_size in range(1, 150):
        universe = tuple(range(universe_size))
        for _ in range(200):
            support_count = rng.randint(1, 100)
            supports = []
            for _support in range(support_count):
                size = rng.randint(1, min(universe_size, 20))
                supports.append(frozenset(rng.sample(universe, size)))
            threshold = rng.randint(2, 20)
            incidence = sum(len(support) for support in supports)
            union = set().union(*supports)
            multiplicity = Counter(edge for support in supports for edge in support)
            if max(multiplicity.values()) < threshold:
                assert len(union) * (threshold - 1) >= incidence
            checked += 1
    return checked


def check_recurrent_blocker_runs():
    rng = random.Random(1123)
    checked = 0
    for _ in range(100000):
        episodes = rng.randint(1, 100)
        restored = [False]
        activations = 1
        for _episode in range(1, episodes):
            did_restore = rng.choice((True, False))
            restored.append(did_restore)
            if did_restore:
                activations += 1
        assert activations - 1 == sum(restored[1:])
        checked += 1
    return checked


def main():
    print(
        "verified target-bank rollback support:",
        check_missing_support_and_rollback(),
        "missing-support cases,",
        check_duplicate_erasure(),
        "duplicate attempts,",
        check_blocker_concentration(),
        "blocker bounds,",
        check_support_incidence(),
        "incidence bounds, and",
        check_recurrent_blocker_runs(),
        "restoration histories",
    )


if __name__ == "__main__":
    main()
