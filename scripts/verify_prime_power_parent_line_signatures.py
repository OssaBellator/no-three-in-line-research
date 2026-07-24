#!/usr/bin/env python3
"""Finite checks for CMR196--CMR198."""

from __future__ import annotations

from itertools import combinations


def line_cells(t: int, a: int, b: int, c: int) -> list[tuple[int, int]]:
    return [
        (x, y)
        for x in range(t)
        for y in range(t)
        if a * x + b * y == c
    ]


def verify_nonaxis_lines_are_partial_matchings(max_t: int) -> None:
    for t in range(5, max_t + 1):
        bound = 2 * (t - 1)
        for a in range(-bound, bound + 1):
            for b in range(-bound, bound + 1):
                if a == 0 or b == 0:
                    continue
                for c in range(-bound * t, bound * t + 1):
                    cells = line_cells(t, a, b, c)
                    assert len({x for x, _ in cells}) == len(cells)
                    assert len({y for _, y in cells}) == len(cells)


def has_perfect_matching(allowed_masks: list[int], t: int) -> bool:
    reachable = {0}
    for row in range(t):
        next_reachable = set()
        for used in reachable:
            available = allowed_masks[row] & ~used
            while available:
                bit = available & -available
                available -= bit
                next_reachable.add(used | bit)
        reachable = next_reachable
        if not reachable:
            return False
    return bool(reachable)


def verify_cyclic_forbidden_families(max_t: int) -> None:
    for t in range(5, max_t + 1):
        permutations = [tuple((row + shift) % t for row in range(t)) for shift in range(t)]
        maximum_q = (t // 2) - 1
        for q in range(maximum_q + 1):
            for chosen in combinations(permutations, q):
                masks = []
                for row in range(t):
                    forbidden = {row}
                    forbidden.update(permutation[row] for permutation in chosen)
                    mask = sum(1 << column for column in range(t) if column not in forbidden)
                    masks.append(mask)
                assert min(mask.bit_count() for mask in masks) >= (t + 1) // 2
                assert has_perfect_matching(masks, t)


def verify_degree_threshold(max_t: int) -> None:
    for t in range(5, max_t + 1):
        for q in range(t):
            if q < t // 2:
                assert t - q - 1 >= (t + 1) // 2


def main() -> None:
    verify_nonaxis_lines_are_partial_matchings(max_t=8)
    verify_cyclic_forbidden_families(max_t=12)
    verify_degree_threshold(max_t=10_000)
    print(
        "verified parent line signatures: nonaxis lines are partial matchings "
        "and fewer than floor(t/2) line matchings are avoidable"
    )


if __name__ == "__main__":
    main()
