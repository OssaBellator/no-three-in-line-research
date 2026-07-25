#!/usr/bin/env python3
"""Verify AC3cc--AC3cg on small I6 banks and closure-incidence systems."""

from collections import defaultdict
from itertools import combinations, permutations, product


def i6_states(m, h):
    states = []
    for perm in permutations(range(m)):
        for shifts in product(range(h), repeat=m):
            cells = set()
            for source in range(m):
                for g in range(h):
                    column = (source, g)
                    row = (perm[source], (shifts[source] - g) % h)
                    cells.add((column, row))
            states.append(cells)
    return states


def verify_common_support():
    bank_checks = 0
    cell_checks = 0
    for m in range(1, 5):
        for h in range(1, 6):
            if m * h < 2:
                continue
            states = i6_states(m, h)
            common = set.intersection(*states)
            assert not common
            bank_checks += 1

            universe = set.union(*states)
            for cell in universe:
                count = sum(cell in state for state in states)
                assert count * m * h == len(states)
                assert count < len(states)
                cell_checks += 1
    return bank_checks, cell_checks


def support_subsets(size):
    cells = range(size)
    return [
        subset
        for rank in range(1, min(3, size) + 1)
        for subset in combinations(cells, rank)
    ]


def verify_closure_incidence():
    systems = 0
    load_checks = 0
    split_checks = 0
    profile_checks = 0

    for closure_count in range(1, 5):
        supports = support_subsets(closure_count)
        max_supports = min(4, len(supports))
        for support_number in range(1, max_supports + 1):
            for chosen in combinations(supports, support_number):
                for weights in product(range(1, 4), repeat=support_number):
                    total = sum(weights)
                    loads = [0] * closure_count
                    by_rank = [0, 0, 0, 0]
                    for subset, weight in zip(chosen, weights, strict=True):
                        by_rank[len(subset)] += weight
                        for cell in subset:
                            loads[cell] += weight

                    incidence = sum(loads)
                    expected_incidence = sum(
                        len(subset) * weight
                        for subset, weight in zip(chosen, weights, strict=True)
                    )
                    assert incidence == expected_incidence
                    assert incidence >= total
                    assert max(loads) * closure_count >= total
                    load_checks += 1

                    assert total == by_rank[1] + by_rank[2] + by_rank[3]
                    assert max(by_rank[1:]) * 3 >= total
                    split_checks += 1

                    for profile_count in range(1, 5):
                        classes = defaultdict(int)
                        for index, (subset, weight) in enumerate(
                            zip(chosen, weights, strict=True)
                        ):
                            classes[(len(subset), index % profile_count)] += weight
                        assert max(classes.values()) * 3 * profile_count >= total
                        profile_checks += 1

                    for cap in range(1, total + 1):
                        if max(loads) <= cap:
                            assert closure_count * cap >= total
                        load_checks += 1

                    systems += 1

    return systems, load_checks, split_checks, profile_checks


def main():
    banks, cells = verify_common_support()
    systems, loads, splits, profiles = verify_closure_incidence()
    print(
        "AC RI closure collateral: verified "
        f"{banks} nontrivial I6 banks, {cells} cell probabilities, "
        f"{systems} closure systems, {loads} load/spread bounds, "
        f"{splits} closure-count splits, and {profiles} profile losses"
    )


if __name__ == "__main__":
    main()
