#!/usr/bin/env python3
"""Exhaustively verify OP2e on binary canonical theta instances."""

from __future__ import annotations

from itertools import product

BitPair = tuple[int, int]
Assignment = tuple[int, int, int, int, int]


def satisfies(
    assignment: Assignment,
    forbidden: tuple[BitPair, ...],
) -> bool:
    s, t, u0, u1, u2 = assignment
    internal = (u0, u1, u2)
    for index, value in enumerate(internal):
        if (s, value) == forbidden[2 * index]:
            return False
        if (value, t) == forbidden[2 * index + 1]:
            return False
    return True


def brute_force(
    forbidden: tuple[BitPair, ...],
) -> Assignment | None:
    for assignment in product(range(2), repeat=5):
        if satisfies(assignment, forbidden):
            return assignment
    return None


def conditioned_solve(
    forbidden: tuple[BitPair, ...],
) -> Assignment | None:
    """Delete s; the residual factor graph is a tree for each branch."""
    for s in range(2):
        domains: list[set[int]] = [{0, 1} for _ in range(3)]

        # Each left check becomes either already satisfied or unary.
        for index in range(3):
            left = forbidden[2 * index]
            if s == left[0]:
                domains[index].discard(left[1])
            if not domains[index]:
                break
        else:
            # Fixing t separates the three residual paths. This is the
            # tree-message recurrence specialized to the theta graph.
            for t in range(2):
                witnesses: list[int] = []
                for index in range(3):
                    right = forbidden[2 * index + 1]
                    allowed = [
                        value
                        for value in domains[index]
                        if (value, t) != right
                    ]
                    if not allowed:
                        break
                    witnesses.append(allowed[0])
                else:
                    candidate = (s, t, *witnesses)
                    assert satisfies(candidate, forbidden)
                    return candidate
    return None


def verify() -> None:
    binary_patterns = tuple(product(range(2), repeat=2))
    for forbidden in product(binary_patterns, repeat=6):
        conditioned = conditioned_solve(forbidden)
        brute = brute_force(forbidden)
        assert (conditioned is None) == (brute is None)
        assert conditioned is not None
        assert satisfies(conditioned, forbidden)


def main() -> None:
    verify()
    print("bounded-feedback completion: all binary theta instances passed")


if __name__ == "__main__":
    main()
