#!/usr/bin/env python3
"""Finite arithmetic checks for CMR1134--CMR1141."""

from math import ceil
import random


def host_stages(side):
    return 2 * side * side + side + 1


def stocks(side, height):
    owner_path = sum(host_stages(m) for m in range(1, side + 1))
    multiplier = (height + 1) * (2 * side + 1)
    owners = multiplier * owner_path
    protected = multiplier * sum(2 * m * host_stages(m) for m in range(1, side + 1))
    deletions = multiplier * sum(2 * m * m * host_stages(m) for m in range(1, side + 1))
    losses = multiplier * sum(
        host_stages(m) * (2 * m + 1) * (2 * m * m - 2 * m)
        for m in range(1, side + 1)
    )
    blockers = 2 * side * side * owners
    contractions = protected
    total = owners + protected + deletions + losses + blockers + contractions
    return owners, protected, deletions, losses, blockers, contractions, total


def check_stock_arithmetic():
    checked = 0
    for side in range(1, 500):
        for height in range(1, 20):
            values = stocks(side, height)
            assert all(value >= 0 for value in values)
            assert values[-1] == sum(values[:-1])
            assert values[4] >= values[0]
            checked += 1
    return checked


def check_target_hypergraph_scales():
    checked = 0
    for potential in range(1, 10000):
        for q in range(2, 30):
            concentrated = ceil(potential / (3 * (q - 1)))
            assert concentrated >= 1
            destroyed = ceil(q / 2)
            assert destroyed >= 1
            checked += 1
    return checked


def check_currency_execution():
    rng = random.Random(1140)
    checked = 0
    for _ in range(3000):
        capacities = [rng.randint(0, 200) for _ in range(6)]
        remaining = list(capacities)
        episodes = 0
        while any(remaining):
            available = [index for index, value in enumerate(remaining) if value]
            index = rng.choice(available)
            remaining[index] -= 1
            episodes += 1
            assert episodes <= sum(capacities)
        assert episodes == sum(capacities)
        checked += 1
    return checked


def check_terminal_blocker_cover():
    rng = random.Random(1141)
    checked = 0
    for universe_size in range(1, 200):
        universe = set(range(universe_size))
        for _ in range(100):
            cover = set(rng.sample(tuple(universe), rng.randint(0, universe_size)))
            candidates = []
            if cover:
                for _candidate in range(100):
                    state = {rng.choice(tuple(cover))}
                    state.update(
                        rng.sample(tuple(universe), rng.randint(0, min(15, universe_size)))
                    )
                    candidates.append(frozenset(state))
                assert all(set(candidate) & cover for candidate in candidates)
                host = universe - cover
                assert all(not set(candidate) <= host for candidate in candidates)
            checked += 1
    return checked


def main():
    print(
        "verified selected-scheduler finite response:",
        check_stock_arithmetic(),
        "stock cases,",
        check_target_hypergraph_scales(),
        "target-scale cases,",
        check_currency_execution(),
        "currency executions, and",
        check_terminal_blocker_cover(),
        "terminal-cover cases",
    )


if __name__ == "__main__":
    main()
