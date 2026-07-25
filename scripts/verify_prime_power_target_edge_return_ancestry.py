#!/usr/bin/env python3
"""Finite checks for CMR720--CMR726."""

from itertools import permutations


def edges(permutation):
    return {(index, permutation[index]) for index in range(len(permutation))}


def perfect_matchings(side, host):
    return [
        permutation
        for permutation in permutations(range(side))
        if edges(permutation) <= host
    ]


def main():
    checked = 0
    for side in range(1, 4):
        universe = [
            (source, target)
            for source in range(side)
            for target in range(side)
        ]
        all_permutations = list(permutations(range(side)))
        for old_permutation in all_permutations:
            old_matching = edges(old_permutation)
            for edge in universe:
                if edge in old_matching:
                    continue
                for mask in range(1 << len(universe)):
                    host = {
                        universe[index]
                        for index in range(len(universe))
                        if (mask >> index) & 1
                    }
                    if edge not in host:
                        continue
                    matchings = perfect_matchings(side, host)
                    if not matchings:
                        continue
                    if old_matching <= host:
                        assert old_permutation in matchings
                        assert any(
                            edge not in edges(permutation)
                            for permutation in matchings
                        )
                    essential = all(
                        edge in edges(permutation)
                        for permutation in matchings
                    )
                    if essential:
                        assert not old_matching <= host
                        assert old_matching - host
                    checked += 1

    arithmetic = 0
    for matching_size in range(1, 100):
        for threshold in range(2, 15):
            bound = (threshold - 1) * matching_size
            assert bound >= matching_size
            arithmetic += 1

    print(
        "verified target-edge return ancestry:",
        checked,
        "host/matching cases and",
        arithmetic,
        "witness bounds",
    )


if __name__ == "__main__":
    main()
