#!/usr/bin/env python3
"""Verify SRR2a deleted-matching extension and locality bounds."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial

Edge = tuple[int, int]
Partial = tuple[Edge, ...]
Matching = tuple[int, ...]


def partial_matchings(n: int, rank: int) -> list[Partial]:
    result: list[Partial] = []
    for rows in combinations(range(n), rank):
        for columns in combinations(range(n), rank):
            for ordered_columns in permutations(columns):
                result.append(tuple(zip(rows, ordered_columns)))
    return result


def host_valid(partial: Partial, missing: set[Edge]) -> bool:
    return all(edge not in missing for edge in partial)


def compatible(left: Partial, right: Partial) -> bool:
    return (
        {row for row, _ in left}.isdisjoint(row for row, _ in right)
        and {column for _, column in left}.isdisjoint(
            column for _, column in right
        )
    )


def contains(matching: Matching, partial: Partial) -> bool:
    return all(matching[row] == column for row, column in partial)


def extension_formula(n: int, missing: set[Edge], partial: Partial) -> int:
    used_rows = {row for row, _ in partial}
    used_columns = {column for _, column in partial}
    surviving = sum(
        row not in used_rows and column not in used_columns
        for row, column in missing
    )
    remaining = n - len(partial)
    return sum(
        (-1) ** count
        * comb(surviving, count)
        * factorial(remaining - count)
        for count in range(surviving + 1)
    )


def falling(number: int, rank: int) -> int:
    result = 1
    for offset in range(rank):
        result *= number - offset
    return result


def verify(n: int = 5, maximum_missing: int = 2) -> None:
    all_permutations = tuple(permutations(range(n)))
    partials = {
        rank: partial_matchings(n, rank)
        for rank in range(3)
    }
    for missing_rank in range(maximum_missing + 1):
        missing = {(index, index) for index in range(missing_rank)}
        states = [
            matching
            for matching in all_permutations
            if all(matching[row] != column for row, column in missing)
        ]
        counts: dict[Partial, int] = {}
        for rank in range(3):
            for partial in partials[rank]:
                if not host_valid(partial, missing):
                    continue
                observed = sum(
                    contains(matching, partial) for matching in states
                )
                expected = extension_formula(n, missing, partial)
                assert observed == expected
                counts[partial] = observed

        for flaw_rank in range(1, 3):
            for remote_rank in range(1, 3):
                if n - flaw_rank <= missing_rank:
                    continue
                if n - remote_rank <= missing_rank:
                    continue
                for flaw in partials[flaw_rank]:
                    if flaw not in counts:
                        continue
                    for remote in partials[remote_rank]:
                        if remote not in counts or not compatible(
                            flaw,
                            remote,
                        ):
                            continue
                        union = tuple(sorted(flaw + remote))
                        union_count = extension_formula(
                            n,
                            missing,
                            union,
                        )
                        ratio = Fraction(
                            union_count * len(states),
                            counts[flaw] * counts[remote],
                        )
                        complete_ratio = Fraction(
                            falling(n, remote_rank),
                            falling(n - flaw_rank, remote_rank),
                        )
                        hole_factor = (
                            Fraction(
                                n - flaw_rank,
                                n - flaw_rank - missing_rank,
                            )
                            * Fraction(
                                n - remote_rank,
                                n - remote_rank - missing_rank,
                            )
                        )
                        assert ratio <= complete_ratio * hole_factor


def main() -> None:
    verify()
    print("deleted-matching locality: all rank-two cylinders passed")


if __name__ == "__main__":
    main()
