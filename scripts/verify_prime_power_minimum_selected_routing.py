#!/usr/bin/env python3
"""Finite checks for CMR1094--CMR1101."""

from itertools import permutations, product as cartesian_product
from math import factorial
import random


def matching(permutation):
    return frozenset((i, permutation[i]) for i in range(len(permutation)))


def perfect_matchings(side, host):
    return {
        matching(pi)
        for pi in permutations(range(side))
        if matching(pi) <= set(host)
    }


def check_minimum_restriction():
    rng = random.Random(1094)
    checked = 0
    for side in range(1, 8):
        all_matchings = [matching(pi) for pi in permutations(range(side))]
        for _ in range(300):
            family = set(rng.sample(all_matchings, rng.randint(1, min(40, len(all_matchings)))))
            values = {state: rng.randint(0, 30) for state in family}
            minimum = min(values.values())
            anchor = next(state for state in family if values[state] == minimum)
            labels = {state: rng.randint(0, max(0, side - 1)) for state in family}
            anchor_label = labels[anchor]
            restricted = {state for state in family if labels[state] == anchor_label}
            assert anchor in restricted
            assert min(values[state] for state in restricted) == minimum
            checked += 1
    return checked


def multiply(values):
    result = 1
    for value in values:
        result *= value
    return result


def routed_product(child_sizes):
    """Complete hosts on disjoint routed vertex blocks."""
    offsets = []
    total = 0
    for size in child_sizes:
        offsets.append(total)
        total += size
    host = set()
    local_families = []
    for offset, size in zip(offsets, child_sizes):
        vertices = range(offset, offset + size)
        host.update((x, y) for x in vertices for y in vertices)
        local_families.append(
            {
                frozenset((offset + i, offset + pi[i]) for i in range(size))
                for pi in permutations(range(size))
            }
        )
    expected = {
        frozenset().union(*states)
        for states in cartesian_product(*local_families)
    }
    actual = perfect_matchings(total, host)
    return actual, expected


def check_exact_products_and_strict_children():
    rng = random.Random(1095)
    product_cases = 0
    strict_cases = 0
    for total in range(2, 9):
        for _ in range(400):
            part_count = rng.randint(2, min(total, 4))
            cuts = sorted(rng.sample(range(1, total), part_count - 1))
            child_sizes = []
            previous = 0
            for cut in cuts + [total]:
                child_sizes.append(cut - previous)
                previous = cut
            assert sum(child_sizes) == total
            assert len(child_sizes) >= 2
            assert all(1 <= size <= total - 1 for size in child_sizes)
            strict_cases += 1
            if total <= 7 and max(child_sizes) <= 5:
                actual, expected = routed_product(child_sizes)
                assert actual == expected
                assert len(actual) == multiply(factorial(size) for size in child_sizes)
                product_cases += 1
    return product_cases, strict_cases


def host_stages(side):
    return 2 * side * side + side + 1


def check_capacity_arithmetic():
    checked = 0
    for side in range(1, 400):
        owner_stages = sum(host_stages(m) for m in range(1, side + 1))
        protected_path = sum(2 * m * host_stages(m) for m in range(1, side + 1))
        deletion_path = sum(2 * m * m * host_stages(m) for m in range(1, side + 1))
        assert owner_stages >= host_stages(side)
        assert protected_path >= 2 * side * host_stages(side)
        assert deletion_path >= 2 * side * side * host_stages(side)
        for height in range(1, 12):
            wall_envelope = (height + 1) * (2 * side + 1)
            global_protected = wall_envelope * protected_path
            global_deletions = wall_envelope * deletion_path
            assert global_protected >= protected_path
            assert global_deletions >= deletion_path
            checked += 1
    return checked


def main():
    product_cases, strict_cases = check_exact_products_and_strict_children()
    print(
        "verified minimum-selected routing:",
        check_minimum_restriction(),
        "minimum restrictions,",
        product_cases,
        "exact products,",
        strict_cases,
        "strict-child cases, and",
        check_capacity_arithmetic(),
        "capacity cases",
    )


if __name__ == "__main__":
    main()
