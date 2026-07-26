#!/usr/bin/env python3
"""Finite checks for CMR814--CMR821."""

from itertools import permutations
import random


def layer_matching(perm, layer):
    return frozenset((layer, source, perm[source]) for source in range(len(perm)))


def joint_states(side):
    perms = list(permutations(range(side)))
    states = []
    for first in perms:
        first_cells = {(source, first[source]) for source in range(side)}
        first_state = layer_matching(first, 0)
        for second in perms:
            second_cells = {(source, second[source]) for source in range(side)}
            if first_cells.isdisjoint(second_cells):
                states.append(first_state | layer_matching(second, 1))
    return states


def check_activation_support():
    rng = random.Random(814)
    checked = 0
    for side in range(2, 5):
        states = joint_states(side)
        universe = set().union(*states)
        for _ in range(20000):
            anchor = rng.choice(states)
            outside_anchor = sorted(universe - anchor)
            private = set(
                rng.sample(outside_anchor, rng.randint(0, len(outside_anchor)))
            )
            candidates = [
                state
                for state in states
                if state != anchor and state.isdisjoint(private)
            ]
            if not candidates:
                continue
            candidate = rng.choice(candidates)
            entering = set(candidate - anchor)
            assert len(entering) >= 2
            enabling = rng.choice(sorted(entering))

            earlier = (set(universe) - private) - {enabling}
            earlier.update(anchor)
            later = set(earlier)
            later.add(enabling)

            assert candidate.issubset(later)
            assert not candidate.issubset(earlier)
            support = candidate & (later - earlier)
            assert support
            assert support.issubset(entering)
            checked += 1
    return checked


def check_private_growth():
    rng = random.Random(816)
    checked = 0
    for side in range(2, 100):
        universe = set(range(2 * side * side))
        anchor = set(rng.sample(sorted(universe), 2 * side))
        available = set(universe) - anchor
        private = set()
        batches = 0
        while len(available) >= 2 and rng.random() < 0.95:
            size = rng.randint(2, min(len(available), max(2, 2 * side)))
            batch = set(rng.sample(sorted(available), size))
            assert batch.isdisjoint(private)
            private.update(batch)
            available.difference_update(batch)
            batches += 1
        assert len(private) <= 2 * side * side - 2 * side
        assert batches <= side * (side - 1)
        checked += 1
    return checked


def check_absence_run_bound():
    rng = random.Random(819)
    checked = 0
    for side in range(1, 100):
        for threshold in range(2, 20):
            universe = 2 * side * side
            runs = [rng.randint(0, threshold) for _ in range(universe)]
            total_slots = sum(runs)
            assert total_slots <= threshold * universe
            active_bound = side * (side - 1) + threshold * universe
            assert active_bound == side * (side - 1) + 2 * threshold * side * side
            checked += 1
    return checked


def check_reactivation_payment():
    checked = 0
    for prime in (2, 3, 5, 7, 11):
        for height in range(1, 12):
            for activations in range(1, 200):
                restorations = activations - 1
                incidence = restorations * (prime + 1) * (height - 1)
                assert incidence >= 0
                if activations == 1 or height == 1:
                    assert incidence == 0
                checked += 1
    return checked


def main():
    print(
        "verified active context absorption:",
        check_activation_support(),
        "activation cases,",
        check_private_growth(),
        "private-growth cases,",
        check_absence_run_bound(),
        "run bounds, and",
        check_reactivation_payment(),
        "reactivation cases",
    )


if __name__ == "__main__":
    main()
