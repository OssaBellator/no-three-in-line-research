#!/usr/bin/env python3
"""Verify SRR2b for arbitrary small missing-cell sets."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
from math import factorial

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


def rook_numbers(
    n: int,
    missing: set[Edge],
    partial: Partial,
) -> list[int]:
    used_rows = {row for row, _ in partial}
    used_columns = {column for _, column in partial}
    surviving = tuple(
        edge
        for edge in missing
        if edge[0] not in used_rows and edge[1] not in used_columns
    )
    remaining = n - len(partial)
    numbers: list[int] = []
    for rank in range(remaining + 1):
        numbers.append(
            sum(
                len({row for row, _ in chosen}) == rank
                and len({column for _, column in chosen}) == rank
                for chosen in combinations(surviving, rank)
            )
        )
    return numbers


def extension_formula(n: int, missing: set[Edge], partial: Partial) -> int:
    remaining = n - len(partial)
    return sum(
        (-1) ** rank * count * factorial(remaining - rank)
        for rank, count in enumerate(rook_numbers(n, missing, partial))
    )


def falling(number: int, rank: int) -> int:
    result = 1
    for offset in range(rank):
        result *= number - offset
    return result


def verify(n: int = 4, maximum_missing: int = 3) -> None:
    all_edges = tuple((row, column) for row in range(n) for column in range(n))
    all_permutations = tuple(permutations(range(n)))
    partials = {
        rank: partial_matchings(n, rank)
        for rank in range(3)
    }

    for missing_size in range(maximum_missing + 1):
        for missing_tuple in combinations(all_edges, missing_size):
            missing = set(missing_tuple)
            states = [
                matching
                for matching in all_permutations
                if all(matching[row] != column for row, column in missing)
            ]
            assert states

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

                    remaining = n - rank
                    if remaining > missing_size:
                        alpha = Fraction(expected, factorial(remaining))
                        assert (
                            Fraction(1) - Fraction(missing_size, remaining)
                            <= alpha
                            <= 1
                        )

            row_degrees = [
                n - sum(row == index for row, _ in missing)
                for index in range(n)
            ]
            column_degrees = [
                n - sum(column == index for _, column in missing)
                for index in range(n)
            ]
            for matching in states:
                for row, column in enumerate(matching):
                    partners = [
                        other
                        for other in range(n)
                        if other != row
                        and (row, matching[other]) not in missing
                        and (other, column) not in missing
                    ]
                    local_lower = (
                        row_degrees[row]
                        + column_degrees[column]
                        - n
                        - 1
                    )
                    assert len(partners) >= local_lower
                    assert local_lower >= n - 2 * missing_size - 1

            for flaw_rank in range(1, 3):
                for remote_rank in range(1, 3):
                    if n - flaw_rank <= missing_size:
                        continue
                    if n - remote_rank <= missing_size:
                        continue
                    for flaw in partials[flaw_rank]:
                        if flaw not in counts or not counts[flaw]:
                            continue
                        for remote in partials[remote_rank]:
                            if (
                                remote not in counts
                                or not counts[remote]
                                or not compatible(flaw, remote)
                            ):
                                continue
                            union = tuple(sorted(flaw + remote))
                            union_count = extension_formula(n, missing, union)
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
                                    n - flaw_rank - missing_size,
                                )
                                * Fraction(
                                    n - remote_rank,
                                    n - remote_rank - missing_size,
                                )
                            )
                            assert ratio <= complete_ratio * hole_factor


def main() -> None:
    verify()
    print("sparse-hole locality: all K4,4 regressions passed")


if __name__ == "__main__":
    main()
