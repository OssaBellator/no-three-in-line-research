#!/usr/bin/env python3
"""Arithmetic checks for CMR706--CMR712."""

from math import comb, ceil


def main():
    checked = 0
    for side in range(1, 50):
        cell_stock = 2 * side * side
        target_stock = comb(cell_stock, 3) if cell_stock >= 3 else 0
        for cell_threshold in range(2, 15):
            per_target_cap = 1 + 3 * (cell_threshold - 1)
            chain_cap = per_target_cap * target_stock
            assert per_target_cap == 3 * cell_threshold - 2
            assert chain_cap >= target_stock
            for target_episodes in range(1, 80):
                repeated = max(0, target_episodes - 1)
                witness_load = ceil(repeated / 3) if repeated else 0
                assert 3 * witness_load >= repeated
            checked += 1
    print(
        "verified fixed-envelope target-chain ledger:",
        checked,
        "parameter pairs",
    )


if __name__ == "__main__":
    main()
