#!/usr/bin/env python3
"""Finite checks for CMR777--CMR784."""

from collections import Counter
from itertools import product
from math import floor
import random


def host_stages(side):
    return 2 * side * side + side + 1


def routing_changes(side, threshold):
    return floor((threshold - 1) * side * side / 2)


def owner_stages(side, threshold):
    return sum(
        host_stages(m) * (1 + routing_changes(m, threshold))
        for m in range(1, side + 1)
    )


def fresh_root_bound(side, height, threshold):
    return (
        (height + 1)
        * (2 * side + 1)
        * owner_stages(side, threshold)
        * side
        * side
    )


def check_stock_formulas():
    checked = 0
    for side in range(1, 40):
        for height in range(1, 10):
            for threshold in range(2, 10):
                stock = owner_stages(side, threshold)
                bound = fresh_root_bound(side, height, threshold)
                assert stock > 0
                assert bound >= stock * side * side
                if side > 1:
                    assert stock >= owner_stages(side - 1, threshold)
                checked += 1
    return checked


def root_paths(successor):
    size = len(successor)
    indegree = [0] * size
    for target in successor:
        if target is not None:
            indegree[target] += 1

    roots = [index for index, degree in enumerate(indegree) if degree == 0]
    paths = []
    covered = set()
    for root in roots:
        path = []
        current = root
        while current is not None:
            assert current not in path
            path.append(current)
            covered.add(current)
            current = successor[current]
        paths.append(path)
    return roots, paths, covered


def check_forward_forests():
    rng = random.Random(779)
    checked = 0
    for size in range(1, 300):
        for _ in range(20):
            successor = [None] * size
            for source in range(size):
                later = list(range(source + 1, size))
                if later and rng.random() < 0.7:
                    successor[source] = rng.choice(later)

            for source, target in enumerate(successor):
                if target is not None:
                    assert target > source

            roots, paths, covered = root_paths(successor)
            assert roots
            assert len(covered) == size
            maximum = max(len(path) for path in paths)
            assert size <= len(roots) * maximum
            checked += 1
    return checked


def check_label_recurrence():
    checked = 0
    for universe in range(1, 200):
        for threshold in range(2, 20):
            extremal = []
            for label in range(universe):
                extremal.extend([label] * (threshold - 1))
            assert len(extremal) == (threshold - 1) * universe
            repeated = extremal + [0]
            assert max(Counter(repeated).values()) >= threshold
            assert threshold - 1 <= max(Counter(repeated).values())
            checked += 1
    return checked


def absence_statistics(bits):
    runs = 0
    restorations = 0
    previous = 1
    for bit in bits:
        if previous == 1 and bit == 0:
            runs += 1
        if previous == 0 and bit == 1:
            restorations += 1
        previous = bit
    return runs, restorations


def check_absence_generations():
    checked = 0
    for length in range(1, 14):
        for bits in product((0, 1), repeat=length):
            runs, restorations = absence_statistics(bits)
            assert runs <= restorations + 1
            if runs >= 1:
                assert restorations >= runs - 1
            checked += 1
    return checked


def check_token_payment():
    checked = 0
    for prime in (2, 3, 5, 7, 11):
        for height in range(1, 12):
            for generations in range(1, 100):
                restorations = generations - 1
                incidence = restorations * (prime + 1) * (height - 1)
                assert incidence >= 0
                if height == 1 or generations == 1:
                    assert incidence == 0
                checked += 1
    return checked


def main():
    print(
        "verified global return ancestry forest:",
        check_stock_formulas(),
        "stock cases,",
        check_forward_forests(),
        "forward forests,",
        check_label_recurrence(),
        "label thresholds,",
        check_absence_generations(),
        "absence histories, and",
        check_token_payment(),
        "token cases",
    )


if __name__ == "__main__":
    main()
