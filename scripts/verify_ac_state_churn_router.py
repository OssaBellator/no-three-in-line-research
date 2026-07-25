#!/usr/bin/env python3
"""Exact finite checks for AC3iq--AC3it."""

from __future__ import annotations

from itertools import permutations, product
from math import ceil


def cells(p):
    return {(i, p[i]) for i in range(len(p))}


def check_permutation_churn():
    pair_checks = inserted_incidences = 0
    for n in range(2, 7):
        ps = list(permutations(range(n)))
        for p in ps:
            old = cells(p)
            for q in ps:
                if p == q:
                    continue
                inserted = len(cells(q) - old)
                assert inserted >= 2
                pair_checks += 1
                inserted_incidences += inserted
    return pair_checks, inserted_incidences


def check_binary_presence():
    checks = 0
    for transitions in range(1, 15):
        for bits in product((0, 1), repeat=transitions + 1):
            inserted = sum(
                bits[t] == 0 and bits[t + 1] == 1
                for t in range(transitions)
            )
            removed = sum(
                bits[t] == 1 and bits[t + 1] == 0
                for t in range(transitions)
            )
            assert removed >= inserted - 1
            assert inserted >= removed - 1
            checks += 1
    return checks


def check_cross_router():
    router_checks = threshold_checks = 0
    for n in range(2, 20):
        for labels in range(1, 9):
            stock = labels * (n - 1) ** 2
            samples = {
                0,
                1,
                stock,
                stock + 1,
                2 * stock,
                stock * stock,
                2 * stock * stock + stock,
                5 * stock * stock + 3 * stock + 9,
            }
            for inserted in sorted(samples):
                removals = max(0, inserted - 1)
                repeated_removal = (
                    ceil(removals / stock) if removals else 0
                )
                assert repeated_removal == (
                    (removals + stock - 1) // stock if removals else 0
                )
                long_returns = (
                    ceil(max(0, repeated_removal - 1 - stock) / stock)
                    if repeated_removal
                    else 0
                )
                assert long_returns >= 0
                router_checks += 1

            for multiplicity in range(1, 8):
                bound = multiplicity * stock * stock + stock + 1
                history = n * n * bound
                assert ceil(history / (n * n)) == bound
                assert ceil((history + 1) / (n * n)) >= bound + 1

                inserted = bound + 1
                repeated_removal = ceil((inserted - 1) / stock)
                long_returns = ceil(
                    max(0, repeated_removal - 1 - stock) / stock
                )
                assert long_returns >= multiplicity
                threshold_checks += 1
    return router_checks, threshold_checks


def check_mask_chains():
    checks = 0

    def enumerate_sizes(max_size, remaining, prefix):
        nonlocal checks
        if remaining == 0:
            strict = sum(
                prefix[i + 1] > prefix[i]
                for i in range(len(prefix) - 1)
            )
            assert strict <= max_size
            checks += 1
            return
        start = prefix[-1] if prefix else 0
        for value in range(start, max_size + 1):
            enumerate_sizes(max_size, remaining - 1, prefix + [value])

    for universe_size in range(0, 7):
        for length in range(0, 8):
            enumerate_sizes(universe_size, length, [])
    return checks


def check_epoch_bound():
    checks = 0
    for n in range(2, 13):
        for labels in range(1, 7):
            stock = labels * (n - 1) ** 2
            for multiplicity in range(1, 7):
                local_bound = n * n * (
                    multiplicity * stock * stock + stock + 1
                )
                for resources in range(0, 13):
                    total_bound = resources + (resources + 1) * local_bound
                    # At the bound, all constant-mask intervals may have size H.
                    assert total_bound >= local_bound
                    # One more step forces some interval above H after at most B
                    # strict mask-growth steps.
                    remaining = total_bound + 1 - resources
                    assert ceil(remaining / (resources + 1)) >= local_bound + 1
                    checks += 1
    return checks


def main():
    pair_checks, inserted = check_permutation_churn()
    binary = check_binary_presence()
    routers, thresholds = check_cross_router()
    masks = check_mask_chains()
    epochs = check_epoch_bound()
    print("AC3iq--AC3it exact checks passed")
    print(f"nontrivial permutation pairs: {pair_checks}")
    print(f"inserted cell incidences: {inserted}")
    print(f"binary presence histories: {binary}")
    print(f"cross-router systems: {routers}")
    print(f"polynomial threshold systems: {thresholds}")
    print(f"monotone mask chains: {masks}")
    print(f"epoch-bound systems: {epochs}")


if __name__ == "__main__":
    main()
