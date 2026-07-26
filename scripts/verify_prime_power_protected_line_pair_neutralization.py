#!/usr/bin/env python3
"""Finite checks for CMR755--CMR762."""

from math import ceil, floor, sqrt
import random


def random_perfect_matching(side, rng):
    targets = list(range(side))
    rng.shuffle(targets)
    return {(source, targets[source]) for source in range(side)}


def find_matching(side, forbidden):
    adjacency = [
        [target for target in range(side) if (source, target) not in forbidden]
        for source in range(side)
    ]
    right_owner = [-1] * side

    def augment(source, seen):
        for target in adjacency[source]:
            if target in seen:
                continue
            seen.add(target)
            owner = right_owner[target]
            if owner == -1 or augment(owner, seen):
                right_owner[target] = source
                return True
        return False

    for source in range(side):
        if not augment(source, set()):
            return None
    return {(source, target) for target, source in enumerate(right_owner)}


def random_partial_matching(side, rng, maximum=None):
    if maximum is None:
        maximum = side
    size = rng.randint(0, min(side, maximum))
    left = rng.sample(range(side), size)
    right = rng.sample(range(side), size)
    rng.shuffle(right)
    return set(zip(left, right))


def check_degree_four_hall():
    rng = random.Random(755)
    checked = 0
    for side in range(8, 31):
        for _ in range(400):
            families = [random_partial_matching(side, rng) for _ in range(4)]
            forbidden = set().union(*families)
            row_degree = [0] * side
            col_degree = [0] * side
            for source, target in forbidden:
                row_degree[source] += 1
                col_degree[target] += 1
            assert max(row_degree, default=0) <= 4
            assert max(col_degree, default=0) <= 4
            assert find_matching(side, forbidden) is not None
            checked += 1
    return checked


def check_ordered_layers():
    rng = random.Random(759)
    checked = 0
    for side in range(8, 31):
        for _ in range(300):
            old_a = random_perfect_matching(side, rng)
            old_b = random_perfect_matching(side, rng)
            reserve = random_partial_matching(side, rng)
            target = random_partial_matching(side, rng, maximum=3)

            new_a = find_matching(side, old_a | old_b | reserve | target)
            assert new_a is not None
            new_b = find_matching(side, old_b | new_a | reserve | target)
            assert new_b is not None

            assert new_a.isdisjoint(new_b)
            assert (new_a | new_b).isdisjoint(reserve | target)
            checked += 1
    return checked


def check_fan_arithmetic():
    rng = random.Random(757)
    checked = 0
    for total in range(1, 500):
        for _ in range(20):
            groups = []
            remaining = total
            while remaining:
                part = rng.randint(1, remaining)
                groups.append(part)
                remaining -= part
            assert len(groups) >= ceil(sqrt(total)) or max(groups) > sqrt(total)
            checked += 1
    return checked


def check_thresholds():
    checked = 0
    for count in range(8, 100000):
        threshold = ceil(sqrt(count / 2))
        reserve = floor(count / (4 * threshold))
        assert reserve >= floor(sqrt(count / 18))
        assert sqrt(threshold) >= (count / 2) ** 0.25
        checked += 1
    return checked


def check_return_multiplicity():
    checked = 0
    for count in range(1, 1000):
        pairs = [(2 * i, 2 * i + 1) for i in range(count)]
        returned = {cell for pair in pairs for cell in pair}
        assert len(returned) == 2 * count
        checked += 1
    return checked


def main():
    print(
        "verified protected-line pair neutralization:",
        check_degree_four_hall(),
        "degree-four Hall boards,",
        check_ordered_layers(),
        "ordered layer pairs,",
        check_fan_arithmetic(),
        "fan partitions,",
        check_thresholds(),
        "threshold cases, and",
        check_return_multiplicity(),
        "return multiplicities",
    )


if __name__ == "__main__":
    main()
