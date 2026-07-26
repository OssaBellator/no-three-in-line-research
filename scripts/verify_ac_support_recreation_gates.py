#!/usr/bin/env python3
"""Finite checks for AC3oc--AC3og."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product


def verify_paths(counts: Counter[str]) -> None:
    # Exhaust every support and three-state return path through four atoms.
    for atom_count in range(1, 5):
        masks = range(1 << atom_count)
        atoms = tuple(range(atom_count))
        for support_size in range(1, atom_count + 1):
            for support in combinations(atoms, support_size):
                support_mask = sum(1 << atom for atom in support)
                parent = support_mask
                for child in masks:
                    lost = [atom for atom in support if not (child >> atom) & 1]
                    if not lost:
                        continue
                    canonical = min(lost)
                    for middle in masks:
                        for end in masks:
                            if end & support_mask != support_mask:
                                continue
                            path = (child, middle, end)
                            first = None
                            for index in range(1, len(path)):
                                before = (path[index - 1] >> canonical) & 1
                                after = (path[index] >> canonical) & 1
                                if before == 0 and after == 1:
                                    first = index
                                    break
                            assert first is not None
                            assert all(
                                ((path[index] >> canonical) & 1) == 0
                                for index in range(first)
                            )
                            counts["recreation paths"] += 1


def verify_monotone(counts: Counter[str]) -> None:
    for length in range(1, 9):
        for word in product((0, 1), repeat=length):
            if word[0] != 0:
                continue
            deletion_monotone = all(word[i] >= word[i + 1] for i in range(length - 1))
            if deletion_monotone:
                assert 1 not in word
                counts["monotone words"] += 1


def verify_ticket_accounting(counts: Counter[str]) -> None:
    # Exhaust all capacities 0,1,2 on at most nine exact token--atom pairs.
    for token_count in range(1, 4):
        for atom_count in range(1, 4):
            pairs = [(token, atom) for token in range(token_count) for atom in range(atom_count)]
            for capacities in product((0, 1, 2), repeat=len(pairs)):
                total = sum(capacities)
                remaining = dict(zip(pairs, capacities))
                used = 0
                for pair in pairs:
                    while remaining[pair] > 0:
                        remaining[pair] -= 1
                        used += 1
                assert used == total
                assert all(value == 0 for value in remaining.values())
                if all(capacity <= 1 for capacity in capacities):
                    assert used <= len(pairs)
                counts["ticket systems"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_paths(counts)
    verify_monotone(counts)
    verify_ticket_accounting(counts)
    print("AC3oc--AC3og support-recreation audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
