#!/usr/bin/env python3
"""Finite checks for AC3nn--AC3nr."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations, product


def subsets(atom_count: int) -> tuple[frozenset[int], ...]:
    return tuple(
        frozenset(index for index, bit in enumerate(bits) if bit)
        for bits in product((0, 1), repeat=atom_count)
    )


def first_reverse_gate(
    cycle: tuple[frozenset[int], ...], atom: int
) -> tuple[int, frozenset[int], frozenset[int]]:
    """Return the first post-departure edge restoring the initial atom bit."""
    alpha = cycle[0]
    for index in range(1, len(cycle)):
        source = cycle[index]
        target = cycle[(index + 1) % len(cycle)]
        if (atom in source) != (atom in target):
            assert (atom in target) == (atom in alpha)
            return index, source, target
    raise AssertionError("a changed departure atom must return on a closed cycle")


def verify_reverse_gates(counts: Counter[str]) -> None:
    states = subsets(3)
    for length in range(2, 6):
        for chosen in combinations(states, length):
            for cycle in permutations(chosen):
                alpha, beta = cycle[0], cycle[1]
                changed = sorted(alpha ^ beta)
                if not changed:
                    continue
                atom = changed[0]
                departure_adds = atom not in alpha and atom in beta
                gate_index, source, target = first_reverse_gate(cycle, atom)

                assert 1 <= gate_index < len(cycle)
                assert all(
                    (atom in cycle[index]) == (atom in beta)
                    for index in range(1, gate_index + 1)
                )
                return_adds = atom not in source and atom in target
                assert return_adds != departure_adds
                assert (atom in target) == (atom in alpha)

                if len(changed) > 1:
                    counts["batch departure edges"] += 1
                counts["simple subset cycles"] += 1


def verify_monotone_impossibility(counts: Counter[str]) -> None:
    states = subsets(3)
    for length in range(2, 6):
        for chosen in combinations(states, length):
            for cycle in permutations(chosen):
                additions = 0
                removals = 0
                changed_edges = 0
                for index, source in enumerate(cycle):
                    target = cycle[(index + 1) % length]
                    if source == target:
                        continue
                    changed_edges += 1
                    additions += len(target - source)
                    removals += len(source - target)
                if changed_edges:
                    assert additions > 0
                    assert removals > 0
                counts["monotone audits"] += 1


def verify_gate_stock(counts: Counter[str]) -> None:
    for atom_stocks in product(range(1, 6), repeat=3):
        for kind_stocks in product(range(1, 5), repeat=3):
            addresses = {
                (field, atom, direction, kind)
                for field, (atom_stock, kind_stock) in enumerate(
                    zip(atom_stocks, kind_stocks, strict=True)
                )
                for atom in range(atom_stock)
                for direction in (-1, 1)
                for kind in range(kind_stock)
            }
            formula = 2 * sum(
                atom_stock * kind_stock
                for atom_stock, kind_stock in zip(
                    atom_stocks, kind_stocks, strict=True
                )
            )
            assert len(addresses) == formula
            counts["gate-stock formulas"] += 1


def verify_ticket_budget(counts: Counter[str]) -> None:
    for ticket_stock in range(9):
        used: set[int] = set()
        for ticket in range(ticket_stock):
            before = len(used)
            assert ticket not in used
            used.add(ticket)
            assert len(used) == before + 1
            counts["ticket consumptions"] += 1
        assert len(used) <= ticket_stock
        counts["ticket budgets"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_reverse_gates(counts)
    verify_monotone_impossibility(counts)
    verify_gate_stock(counts)
    verify_ticket_budget(counts)

    print("AC3nn--AC3nr set-generator cycle audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
