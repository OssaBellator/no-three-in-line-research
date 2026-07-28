#!/usr/bin/env python3

"""Finite audit for GC2gy--GC2hc."""

from __future__ import annotations

import random


def main() -> None:
    rng = random.Random(2026072804)
    profiles = 0
    paid = 0
    overloaded = 0
    repeated_sequences = 0

    for _ in range(30000):
        cause_count = rng.randint(1, 9)
        loads = [rng.randint(0, 40) for _ in range(cause_count)]
        budgets = [rng.randint(0, 40) for _ in range(cause_count)]
        rectangle_mass = sum(loads)
        assert rectangle_mass == sum(loads)

        bad = [index for index in range(cause_count) if loads[index] > budgets[index]]
        if bad:
            overloaded += 1
            if rectangle_mass > sum(budgets):
                assert bad
        else:
            paid += 1
            assert rectangle_mass <= sum(budgets)
        profiles += 1

    for _ in range(5000):
        cause_count = rng.randint(1, 7)
        remaining = [rng.randint(5, 60) for _ in range(cause_count)]
        initial = sum(remaining)
        consumed = 0

        for _ in range(rng.randint(1, 20)):
            proposed = [
                rng.randint(0, max(1, capacity // 2))
                for capacity in remaining
            ]
            if any(proposed[index] > remaining[index] for index in range(cause_count)):
                break
            for index, value in enumerate(proposed):
                remaining[index] -= value
                consumed += value
            assert consumed <= initial

        assert consumed + sum(remaining) == initial
        repeated_sequences += 1

    print(f"profiles={profiles}")
    print(f"paid={paid}")
    print(f"overloaded={overloaded}")
    print(f"repeated_sequences={repeated_sequences}")


if __name__ == "__main__":
    main()
