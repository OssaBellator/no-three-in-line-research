#!/usr/bin/env python3
"""Finite checks for AC3oh--AC3ol."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product


def current(mask: int, required_one: tuple[int, ...], required_zero: tuple[int, ...]) -> bool:
    return all((mask >> bit) & 1 for bit in required_one) and all(
        not ((mask >> bit) & 1) for bit in required_zero
    )


def failed_literals(
    mask: int,
    required_one: tuple[int, ...],
    required_zero: tuple[int, ...],
) -> tuple[tuple[int, int], ...]:
    failed = [(bit, 1) for bit in required_one if not ((mask >> bit) & 1)]
    failed.extend((bit, 0) for bit in required_zero if (mask >> bit) & 1)
    return tuple(sorted(failed))


def verify_contract_paths(counts: Counter[str]) -> None:
    for bit_count in range(1, 6):
        bits = tuple(range(bit_count))
        masks = tuple(range(1 << bit_count))
        for one_size in range(bit_count + 1):
            for required_one in combinations(bits, one_size):
                remaining = tuple(bit for bit in bits if bit not in required_one)
                for zero_size in range(len(remaining) + 1):
                    for required_zero in combinations(remaining, zero_size):
                        if not required_one and not required_zero:
                            continue
                        parents = [
                            mask
                            for mask in masks
                            if current(mask, required_one, required_zero)
                        ]
                        children = [
                            mask
                            for mask in masks
                            if not current(mask, required_one, required_zero)
                        ]
                        for parent in parents:
                            for child in children:
                                failed = failed_literals(child, required_one, required_zero)
                                assert failed
                                literal = failed[0]
                                bit, desired = literal
                                for middle in masks:
                                    for end in parents:
                                        path = (child, middle, end)
                                        first = None
                                        for index in range(1, len(path)):
                                            before = (path[index - 1] >> bit) & 1
                                            after = (path[index] >> bit) & 1
                                            if before == 1 - desired and after == desired:
                                                first = index
                                                break
                                        assert first is not None
                                        assert all(
                                            ((path[index] >> bit) & 1) == 1 - desired
                                            for index in range(first)
                                        )
                                        counts["context paths"] += 1


def verify_monotone_words(counts: Counter[str]) -> None:
    for desired in (0, 1):
        for length in range(1, 9):
            for word in product((0, 1), repeat=length):
                if word[0] != 1 - desired:
                    continue
                away_monotone = all(value == 1 - desired for value in word)
                if away_monotone:
                    assert desired not in word
                    counts["monotone literal words"] += 1


def verify_ticket_accounting(counts: Counter[str]) -> None:
    for token_count in range(1, 5):
        for literal_count in range(1, 6):
            pairs = [
                (token, literal)
                for token in range(token_count)
                for literal in range(literal_count)
            ]
            for active_mask in range(1 << len(pairs)):
                remaining = {
                    pair: (active_mask >> index) & 1
                    for index, pair in enumerate(pairs)
                }
                used = 0
                for pair in pairs:
                    if remaining[pair]:
                        remaining[pair] = 0
                        used += 1
                assert used <= len(pairs)
                assert all(value == 0 for value in remaining.values())
                counts["ticket systems"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_contract_paths(counts)
    verify_monotone_words(counts)
    verify_ticket_accounting(counts)
    print("AC3oh--AC3ol context recreation audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
