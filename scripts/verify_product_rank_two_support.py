#!/usr/bin/env python3
"""Verify PX205--PX206 rank-two support classification and scales."""
from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations
from math import comb, exp


def support(partial: tuple[tuple[int, int], ...]) -> frozenset[int]:
    return frozenset(index for edge in partial for index in edge)


def rank_two_matchings(size: int) -> tuple[tuple[tuple[int, int], ...], ...]:
    result = []
    for rows in combinations(range(size), 2):
        for columns in combinations(range(size), 2):
            for image in permutations(columns):
                partial = tuple(zip(rows, image))
                if any(row == column for row, column in partial):
                    continue
                result.append(partial)
    return tuple(result)


def classify(partial: tuple[tuple[int, int], ...]) -> str:
    used = support(partial)
    union_size = len(used)
    mapping = dict(partial)

    if union_size == 2:
        first, second = tuple(used)
        assert mapping[first] == second
        assert mapping[second] == first
        return "two-cycle"

    if union_size == 3:
        sources = set(mapping)
        targets = set(mapping.values())
        middle = next(iter(sources & targets))
        predecessor = next(source for source in sources if mapping[source] == middle)
        successor = mapping[middle]
        assert len({predecessor, middle, successor}) == 3
        return "two-path"

    assert union_size == 4
    assert set(mapping).isdisjoint(mapping.values())
    return "disjoint-arcs"


def verify_exact_counts() -> None:
    for size in range(2, 11):
        profile: Counter[str] = Counter(classify(partial) for partial in rank_two_matchings(size))
        assert profile["two-cycle"] == comb(size, 2)
        assert profile["two-path"] == size * (size - 1) * (size - 2)
        assert profile["disjoint-arcs"] == 12 * comb(size, 4)
        print(f"t={size}: {dict(profile)}")


def verify_square_root_bounds() -> None:
    line_load = 12
    delta = 2
    constant = exp(4 * delta)
    for size in (1024, 1600, 2500, 4096):
        thinned_order = size**0.5 / 2
        support_two = 256 * constant * line_load * comb(size, 2) / size**2
        support_three = (
            256
            * constant
            * line_load
            * size
            * (size - 1)
            * (size - 2)
            / size**2.5
        )
        support_four = (
            256
            * constant
            * line_load
            * 12
            * comb(size, 4)
            / size**3
        )
        assert support_two <= 128 * constant * line_load
        assert support_three <= 256 * constant * line_load * size**0.5
        assert support_three <= 512 * constant * line_load * thinned_order
        assert support_four <= 128 * constant * line_load * size
    print("PX206 square-root sector bounds verified")


def main() -> None:
    verify_exact_counts()
    verify_square_root_bounds()
    print("PX205--PX206 verified")


if __name__ == "__main__":
    main()
