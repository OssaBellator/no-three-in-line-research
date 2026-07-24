#!/usr/bin/env python3
"""Exhaustively verify the Hall stationary-resampling criterion."""

from __future__ import annotations

from itertools import combinations


def all_subsets(size: int):
    for rank in range(size + 1):
        yield from combinations(range(size), rank)


def hall_holds(adjacency: tuple[frozenset[int], ...]) -> bool:
    return all(
        len(set().union(*(adjacency[left] for left in subset)))
        >= len(subset)
        for subset in all_subsets(len(adjacency))
    )


def saturating_matching(
    adjacency: tuple[frozenset[int], ...],
) -> tuple[int, ...] | None:
    chosen: list[int] = []

    def extend(left: int, used: set[int]) -> bool:
        if left == len(adjacency):
            return True
        for right in adjacency[left]:
            if right in used:
                continue
            chosen.append(right)
            used.add(right)
            if extend(left + 1, used):
                return True
            used.remove(right)
            chosen.pop()
        return False

    return tuple(chosen) if extend(0, set()) else None


def verify_kernel(matching: tuple[int, ...], right_size: int) -> None:
    left_size = len(matching)
    size = left_size + right_size
    kernel = [[0 for _ in range(size)] for _ in range(size)]
    matched_right = set(matching)

    for left, right in enumerate(matching):
        target = left_size + right
        kernel[left][target] = 1
        kernel[target][left] = 1
    for right in range(right_size):
        if right not in matched_right:
            index = left_size + right
            kernel[index][index] = 1

    assert all(sum(row) == 1 for row in kernel)
    assert all(
        kernel[row][column] == kernel[column][row]
        for row in range(size)
        for column in range(size)
    )
    assert all(
        sum(kernel[row][column] for row in range(size)) == 1
        for column in range(size)
    )
    assert all(
        sum(kernel[left][left_size:]) == 1 for left in range(left_size)
    )


def verify(max_left: int = 3, max_right: int = 4) -> None:
    for left_size in range(1, max_left + 1):
        for right_size in range(1, max_right + 1):
            for mask in range(1 << (left_size * right_size)):
                adjacency = tuple(
                    frozenset(
                        right
                        for right in range(right_size)
                        if mask & (1 << (left * right_size + right))
                    )
                    for left in range(left_size)
                )
                hall = hall_holds(adjacency)
                matching = saturating_matching(adjacency)
                assert hall == (matching is not None)
                if matching is not None:
                    assert all(
                        right in adjacency[left]
                        for left, right in enumerate(matching)
                    )
                    verify_kernel(matching, right_size)


def main() -> None:
    verify()
    print("Hall stationary resampling: verified through 3-by-4 switching graphs")


if __name__ == "__main__":
    main()
