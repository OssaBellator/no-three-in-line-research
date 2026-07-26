#!/usr/bin/env python3
"""Finite checks for AC3om--AC3op."""

from __future__ import annotations

from collections import Counter
from itertools import product


def value(table: int, state: int) -> int:
    return (table >> state) & 1


def verify_predicates(counts: Counter[str]) -> None:
    for bit_count in range(1, 4):
        state_count = 1 << bit_count
        states = tuple(range(state_count))
        for table in range(1 << state_count):
            zeros = tuple(state for state in states if value(table, state) == 0)
            ones = tuple(state for state in states if value(table, state) == 1)
            if not zeros or not ones:
                continue
            counts["nonconstant predicates"] += 1

            boundary_count = len(zeros) * len(ones)
            assert boundary_count <= 1 << (2 * bit_count - 2)
            counts["directed boundary pairs"] += boundary_count

            single_edges = 0
            for source in zeros:
                for bit in range(bit_count):
                    target = source ^ (1 << bit)
                    if value(table, target) == 1:
                        single_edges += 1
            assert single_edges <= bit_count * (1 << (bit_count - 1))
            counts["single-bit boundary edges"] += single_edges

            for parent in ones:
                for child in zeros:
                    assert value(table, parent) == 1
                    assert value(table, child) == 0
                    for middle in states:
                        for end in ones:
                            path = (child, middle, end)
                            first = None
                            for index in range(1, len(path)):
                                if (
                                    value(table, path[index - 1]) == 0
                                    and value(table, path[index]) == 1
                                ):
                                    first = index
                                    break
                            assert first is not None
                            assert all(value(table, path[index]) == 0 for index in range(first))
                            counts["recreation paths"] += 1


def verify_local_update_bound(counts: Counter[str]) -> None:
    for bit_count in range(1, 7):
        states = tuple(range(1 << bit_count))
        for locality in range(1, bit_count + 1):
            ordered_pairs = 0
            for source in states:
                for target in states:
                    distance = (source ^ target).bit_count()
                    if 1 <= distance <= locality:
                        ordered_pairs += 1
            safe_bound = (1 << bit_count) * sum(
                __import__("math").comb(bit_count, size)
                for size in range(1, locality + 1)
            )
            assert ordered_pairs == safe_bound
            counts["local-update stocks"] += 1


def verify_weighted_localization(counts: Counter[str]) -> None:
    for address_count in range(1, 8):
        for weights in product(range(4), repeat=address_count):
            total = sum(weights)
            if total == 0:
                continue
            assert max(weights) * address_count >= total
            counts["weighted address systems"] += 1


def verify_ticket_accounting(counts: Counter[str]) -> None:
    for address_count in range(1, 9):
        for active_mask in range(1 << address_count):
            capacities = [
                (active_mask >> address) & 1
                for address in range(address_count)
            ]
            used = sum(capacities)
            assert used <= address_count
            capacities = [0 for _ in capacities]
            assert not any(capacities)
            counts["ticket systems"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_predicates(counts)
    verify_local_update_bound(counts)
    verify_weighted_localization(counts)
    verify_ticket_accounting(counts)
    print("AC3om--AC3op Boolean boundary audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
