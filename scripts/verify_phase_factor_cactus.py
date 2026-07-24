#!/usr/bin/env python3
"""Verify OP2d messages on high-arity factor-cactus flowers."""

from __future__ import annotations

from itertools import product

Pair = tuple[int, int]
Quadruple = tuple[int, int, int, int]
Domains = tuple[
    frozenset[int],
    frozenset[int],
    frozenset[int],
    frozenset[int],
]


def petal_message(
    left_domain: frozenset[int],
    right_domain: frozenset[int],
    central_forbidden: Pair,
    petal_forbidden: Pair,
) -> dict[int, Pair]:
    witnesses: dict[int, Pair] = {}
    for left, right in product(left_domain, right_domain):
        if (left, right) == petal_forbidden:
            continue
        bit = int(
            left != central_forbidden[0]
            or right != central_forbidden[1]
        )
        witnesses.setdefault(bit, (left, right))
    return witnesses


def message_solve(
    domains: Domains,
    central_forbidden: Quadruple,
    first_forbidden: Pair,
    second_forbidden: Pair,
) -> Quadruple | None:
    first = petal_message(
        domains[0],
        domains[1],
        central_forbidden[:2],
        first_forbidden,
    )
    second = petal_message(
        domains[2],
        domains[3],
        central_forbidden[2:],
        second_forbidden,
    )
    for first_bit, second_bit in product(first, second):
        if first_bit or second_bit:
            return first[first_bit] + second[second_bit]
    return None


def brute_force(
    domains: Domains,
    central_forbidden: Quadruple,
    first_forbidden: Pair,
    second_forbidden: Pair,
) -> Quadruple | None:
    for assignment in product(*domains):
        if assignment == central_forbidden:
            continue
        if assignment[:2] == first_forbidden:
            continue
        if assignment[2:] == second_forbidden:
            continue
        return assignment
    return None


def verify() -> None:
    patterns_two = tuple(product(range(2), repeat=2))
    patterns_four = tuple(product(range(2), repeat=4))
    nonempty_domains = (
        frozenset({0}),
        frozenset({1}),
        frozenset({0, 1}),
    )
    saw_check_saturation = False

    for domains in product(nonempty_domains, repeat=4):
        for central in patterns_four:
            for first_forbidden, second_forbidden in product(
                patterns_two, repeat=2
            ):
                solved = message_solve(
                    domains,
                    central,
                    first_forbidden,
                    second_forbidden,
                )
                brute = brute_force(
                    domains,
                    central,
                    first_forbidden,
                    second_forbidden,
                )
                assert (solved is None) == (brute is None)
                if solved is not None:
                    assert solved in product(*domains)
                    assert solved != central
                    assert solved[:2] != first_forbidden
                    assert solved[2:] != second_forbidden
                    continue

                first = petal_message(
                    domains[0],
                    domains[1],
                    central[:2],
                    first_forbidden,
                )
                second = petal_message(
                    domains[2],
                    domains[3],
                    central[2:],
                    second_forbidden,
                )
                combined = {
                    left | right for left, right in product(first, second)
                }
                assert not first or not second or 1 not in combined
                if first and second and combined == {0}:
                    saw_check_saturation = True

    assert saw_check_saturation


def main() -> None:
    verify()
    print("factor-cactus messages: exhaustive high-arity flowers passed")


if __name__ == "__main__":
    main()
