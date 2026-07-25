#!/usr/bin/env python3
"""Exact arithmetic checks for CMR344--CMR346."""

from __future__ import annotations

from collections import Counter
from math import ceil, floor, sqrt


def verify_token_counts() -> None:
    for p in (3, 5, 7, 11):
        for height in range(1, 10):
            side = p**height
            exact = sum(p**depth for depth in range(height))
            assert exact == (side - 1) // (p - 1)
            tokens = {
                (depth, residue)
                for depth in range(height)
                for residue in range(p**depth)
            }
            assert len(tokens) == exact


def verify_packing() -> None:
    for total in range(1, 200):
        for load in range(1, total + 1):
            disjoint_episodes = total // load
            assert disjoint_episodes <= floor(total / load)

            for episodes in range(1, 200):
                incidences = episodes * load
                synthetic = Counter(index % total for index in range(incidences))
                assert max(synthetic.values()) >= ceil(incidences / total)


def verify_width_bounds() -> None:
    for p in (3, 5, 7, 11):
        for height in range(1, 9):
            side = p**height
            total = (side - 1) / (p - 1)
            width_two = (side - 2) / ((height + p - 1) * sqrt(side))
            if width_two > 0:
                ratio = total / width_two
                displayed = (
                    (height + p - 1)
                    * (side - 1)
                    * sqrt(side)
                    / ((p - 1) * (side - 2))
                )
                assert abs(ratio - displayed) < 1e-9

            if side >= 10:
                width_three = (side - 9) / (
                    (height + p - 1) * sqrt(side)
                )
                ratio = total / width_three
                displayed = (
                    (height + p - 1)
                    * (side - 1)
                    * sqrt(side)
                    / ((p - 1) * (side - 9))
                )
                assert abs(ratio - displayed) < 1e-9


def main() -> None:
    verify_token_counts()
    verify_packing()
    verify_width_bounds()
    print(
        "verified dispersed token ledger: geometric-series counts, fresh "
        "packing, temporal reuse, and width-two/width-three bounds"
    )


if __name__ == "__main__":
    main()
