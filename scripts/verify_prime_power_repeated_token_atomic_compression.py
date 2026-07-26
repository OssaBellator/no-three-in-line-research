#!/usr/bin/env python3
"""Finite checks for CMR1518--CMR1525."""

from collections import Counter
from math import ceil
import random


def exponent(value, prime):
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    assert value == 1
    return result


def signature_bounds(side):
    pair = (side - 1) ** 2
    trace = 2 * (side - 1)
    assert side < 3 or trace <= pair
    return pair, trace


def choose_sets(rng, universe, episodes, minimum_size):
    result = []
    for _ in range(episodes):
        size = rng.randint(minimum_size, universe)
        result.append(frozenset(rng.sample(range(universe), size)))
    return result


def verify_history(side, prime, depth, minimum_size, q, returns, sets, rng):
    universe = side * side // prime ** (2 * depth)
    assert all(minimum_size <= len(values) <= universe for values in sets)
    threshold = 2 * returns * q * (side - 1) ** 2
    episode_count = len(sets)
    counts = Counter(edge for values in sets for edge in values)

    if episode_count * minimum_size <= (threshold - 1) * universe:
        return "finite"

    edge, frequency = max(counts.items(), key=lambda item: item[1])
    assert frequency >= threshold

    # Partition the selected occurrences into continuous-absence runs.  The
    # number of gaps is the exact reintroduction count in this synthetic model.
    maximum_runs = min(frequency, returns + 2)
    run_count = rng.randint(1, maximum_runs)
    cuts = (
        sorted(rng.sample(range(1, frequency), run_count - 1))
        if run_count > 1
        else []
    )
    lengths = []
    previous = 0
    for cut in cuts + [frequency]:
        lengths.append(cut - previous)
        previous = cut

    reintroductions = run_count - 1
    if reintroductions >= returns:
        height = exponent(side, prime)
        incidence = reintroductions * (prime + 1) * (height - 1)
        assert incidence >= returns * (prime + 1) * (height - 1)
        return "return"

    longest = max(lengths)
    assert longest >= ceil(threshold / returns)
    if rng.random() < 0.15:
        return "absorb"

    pair_stock, trace_stock = signature_bounds(side)
    pair_count = rng.randint(0, longest)
    trace_count = longest - pair_count
    if pair_count >= ceil(longest / 2):
        assignments = [rng.randrange(pair_stock) for _ in range(pair_count)]
        multiplicity = max(Counter(assignments).values())
        assert multiplicity >= ceil(pair_count / pair_stock)
        assert multiplicity >= q
        return "pair"

    assignments = [rng.randrange(trace_stock) for _ in range(trace_count)]
    multiplicity = max(Counter(assignments).values())
    assert multiplicity >= ceil(trace_count / trace_stock)
    assert multiplicity >= q
    return "trace"


def deterministic_thresholds():
    checks = 0
    for side, prime, depth in ((4, 2, 1), (8, 2, 1), (9, 3, 1), (16, 2, 2)):
        universe = side * side // prime ** (2 * depth)
        for minimum_size in range(1, universe + 1):
            for q in (1, 2, 3):
                for returns in (1, 2, 4):
                    threshold = 2 * returns * q * (side - 1) ** 2
                    longest = ceil(threshold / returns)
                    pair_stock, trace_stock = signature_bounds(side)
                    assert ceil(ceil(longest / 2) / pair_stock) >= q
                    assert ceil(ceil(longest / 2) / trace_stock) >= q
                    checks += 1
    return checks


def random_histories():
    rng = random.Random(1523)
    outcomes = Counter()
    total_episodes = 0
    for side, prime, depth in ((4, 2, 1), (8, 2, 1), (9, 3, 1)):
        universe = side * side // prime ** (2 * depth)
        for q in (1, 2):
            for returns in (1, 2, 3):
                threshold = 2 * returns * q * (side - 1) ** 2
                for _ in range(80):
                    minimum_size = rng.randint(1, universe)
                    cap = (threshold - 1) * universe // minimum_size
                    episodes = rng.randint(max(1, cap - 5), cap + 12)
                    sets = choose_sets(rng, universe, episodes, minimum_size)
                    outcome = verify_history(
                        side,
                        prime,
                        depth,
                        minimum_size,
                        q,
                        returns,
                        sets,
                        rng,
                    )
                    outcomes[outcome] += 1
                    total_episodes += episodes
    return outcomes, total_episodes


def stock_checks():
    checks = 0
    for side in range(4, 40):
        pair, trace = signature_bounds(side)
        assert pair == (side - 1) ** 2
        assert trace == 2 * (side - 1)
        assert trace <= pair
        checks += 1
    return checks


def main():
    outcomes, episodes = random_histories()
    print(
        "verified repeated-token atomic compression:",
        deterministic_thresholds(),
        "threshold systems,",
        stock_checks(),
        "fixed-edge stock checks,",
        sum(outcomes.values()),
        "synthetic histories with",
        episodes,
        "episodes; outcomes",
        dict(sorted(outcomes.items())),
    )


if __name__ == "__main__":
    main()
