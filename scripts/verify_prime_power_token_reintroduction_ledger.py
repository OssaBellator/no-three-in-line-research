#!/usr/bin/env python3
"""Finite checks for CMR347--CMR350.

The checks cover the exact row-prefix stock, the dynamic inventory inequality,
the forced-or-paid arithmetic reduction, and the universal two-step
old-cell-clean rematching recurrence.
"""

from __future__ import annotations


def verify_row_prefix_stock() -> None:
    for p in (3, 5, 7):
        for height in range(1, 4):
            side = p**height
            for depth in range(height):
                modulus = p**depth
                expected = side * side // modulus
                for residue in range(modulus):
                    cells = {
                        (column, row)
                        for column in range(side)
                        for row in range(side)
                        if row % modulus == residue
                    }
                    assert len(cells) == expected


def verify_inventory_ledger() -> None:
    """Exhaust all short add/remove histories on a small edge universe."""

    for universe_size in range(1, 4):
        full_mask = (1 << universe_size) - 1
        for initial in range(full_mask + 1):
            states = {(initial, 0, 0)}
            for _ in range(6):
                next_states = set()
                for mask, visits, returns in states:
                    assert visits <= initial.bit_count() + returns
                    for edge in range(universe_size):
                        bit = 1 << edge
                        if mask & bit:
                            next_states.add((mask ^ bit, visits + 1, returns))
                            next_states.add((mask ^ bit, visits, returns))
                        else:
                            next_states.add((mask | bit, visits, returns + 1))
                states = next_states
            for _, visits, returns in states:
                assert visits <= initial.bit_count() + returns


def verify_forced_or_paid_reduction() -> None:
    for stock in range(20):
        for returns in range(20):
            for forced in range(20):
                for executable in range(stock + returns + 1):
                    visits = forced + executable
                    assert visits <= forced + stock + returns
                    assert returns >= executable - stock


def verify_two_step_rematching_return() -> None:
    for side in range(2, 30):
        initial = tuple(range(side))
        shift = tuple((index + 1) % side for index in range(side))
        shifted = tuple(initial[shift[index]] for index in range(side))
        returned = tuple(shifted[(index - 1) % side] for index in range(side))

        assert sorted(shift) == list(range(side))
        assert all(shift[index] != index for index in range(side))
        assert all(shifted[index] != initial[index] for index in range(side))
        assert all(returned[index] != shifted[index] for index in range(side))
        assert returned == initial

        initial_cells = {(row, initial[row]) for row in range(side)}
        returned_cells = {(row, returned[row]) for row in range(side)}
        assert returned_cells == initial_cells


def main() -> None:
    verify_row_prefix_stock()
    verify_inventory_ledger()
    verify_forced_or_paid_reduction()
    verify_two_step_rematching_return()
    print(
        "verified token reintroduction ledger: exact prefix stock, dynamic "
        "inventory, forced-or-paid reduction, and two-step rematching return"
    )


if __name__ == "__main__":
    main()
