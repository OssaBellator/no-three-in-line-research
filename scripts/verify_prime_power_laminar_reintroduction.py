#!/usr/bin/env python3
"""Exact checks for CMR378--CMR381."""

from __future__ import annotations

from itertools import permutations


def token_rows(t: int, modulus: int, residue: int) -> set[int]:
    return {row for row in range(t) if row % modulus == residue}


def vacated_token_edges(
    old_matching: tuple[int, ...],
    new_matching: tuple[int, ...],
    columns: tuple[int, ...],
    rows: set[int],
) -> int:
    return sum(
        old_matching[column] in rows
        and new_matching[column] != old_matching[column]
        for column in columns
    )


def verify_one_block_exact() -> None:
    for t in range(3, 9):
        old = tuple(range(t))
        for modulus in range(1, t + 1):
            if t % modulus:
                continue
            for residue in range(modulus):
                rows = token_rows(t, modulus, residue)
                for size in range(2, min(t, 5) + 1):
                    columns = tuple(range(size))
                    old_rows = tuple(old[column] for column in columns)
                    for replacement in permutations(old_rows):
                        new = list(old)
                        for column, row in zip(columns, replacement):
                            new[column] = row
                        observed = vacated_token_edges(
                            old, tuple(new), columns, rows
                        )
                        available_rows = sum(row in rows for row in old_rows)
                        assert observed <= available_rows


def verify_disjoint_depth_partition() -> None:
    for p in (3, 5, 7):
        for h in range(1, 5):
            t = p**h
            for b in range(h):
                modulus = p**b
                for residue in range(modulus):
                    rows = token_rows(t, modulus, residue)
                    assert len(rows) == t // modulus

                    for a in range(h + 1):
                        block_modulus = p**a
                        blocks = [
                            tuple(range(start, t, block_modulus))
                            for start in range(block_modulus)
                        ]
                        seen_rows: set[int] = set()
                        total = 0
                        for block in blocks:
                            block_rows = set(block)
                            assert seen_rows.isdisjoint(block_rows)
                            seen_rows |= block_rows
                            total += len(block_rows & rows)
                        assert total == t // modulus
                        assert seen_rows == set(range(t))


def verify_sweep_arithmetic() -> None:
    for p in (3, 5, 7, 11, 13):
        for h in range(1, 30):
            t = p**h
            for b in range(h):
                per_depth = t // (p**b)
                one_layer = h * per_depth
                two_layer = 2 * one_layer
                assert one_layer == h * t // (p**b)
                assert two_layer == 2 * h * t // (p**b)

                if 3 * b >= 2 * h:
                    assert two_layer**3 <= (2 * h) ** 3 * t


def main() -> None:
    verify_one_block_exact()
    verify_disjoint_depth_partition()
    verify_sweep_arithmetic()
    print(
        "verified laminar reintroduction: one-block vacated-row bounds, "
        "disjoint depth accounting, and full-sweep scale arithmetic"
    )


if __name__ == "__main__":
    main()
