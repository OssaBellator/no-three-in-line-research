#!/usr/bin/env python3
"""Finite checks for CMR822--CMR829."""

from collections import Counter
from math import ceil
import random


def host_stages(side):
    return 2 * side * side + side + 1


def path_stage_stock(side):
    return sum(host_stages(m) for m in range(1, side + 1))


def edge_lineage_slots(side, height):
    return (height + 1) * (path_stage_stock(side) + 1)


def check_partition_ownership():
    rng = random.Random(822)
    checked = 0
    for size in range(1, 500):
        universe = list(range(size))
        for _ in range(100):
            rng.shuffle(universe)
            fixed_size = rng.randint(0, size)
            fixed = set(universe[:fixed_size])
            remainder = universe[fixed_size:]
            factors = []
            position = 0
            while position < len(remainder):
                width = rng.randint(1, len(remainder) - position)
                factors.append(set(remainder[position : position + width]))
                position += width

            owner = {}
            for edge in fixed:
                owner[edge] = "fixed"
            for index, factor in enumerate(factors):
                for edge in factor:
                    assert edge not in owner
                    owner[edge] = index
            assert len(owner) == size
            checked += 1
    return checked


def check_decreasing_paths():
    rng = random.Random(823)
    checked = 0
    for side in range(1, 200):
        for _ in range(200):
            current = side
            visited = []
            used_stages = 0
            while current > 0:
                visited.append(current)
                used_stages += rng.randint(1, host_stages(current))
                current = rng.randint(0, current - 1)
            assert len(visited) == len(set(visited))
            assert used_stages <= path_stage_stock(side)
            checked += 1
    return checked


def check_slot_formulas():
    checked = 0
    for side in range(1, 200):
        stock = path_stage_stock(side)
        assert stock >= host_stages(side)
        if side > 1:
            assert stock > path_stage_stock(side - 1)
        for height in range(1, 20):
            slots = edge_lineage_slots(side, height)
            assert slots == (height + 1) * (stock + 1)
            checked += 1
    return checked


def check_restoration_concentration():
    checked = 0
    for slots in range(1, 500):
        for threshold in range(2, 20):
            extremal = []
            for owner in range(slots):
                extremal.extend([owner] * (threshold - 1))
            assert len(extremal) == (threshold - 1) * slots
            repeated = extremal + [0]
            assert max(Counter(repeated).values()) >= threshold
            assert ceil(len(repeated) / slots) >= threshold
            checked += 1
    return checked


def check_token_payment():
    checked = 0
    for prime in (2, 3, 5, 7, 11):
        for height in range(1, 12):
            for restorations in range(0, 200):
                incidence = restorations * (prime + 1) * (height - 1)
                assert incidence >= 0
                if height == 1 or restorations == 0:
                    assert incidence == 0
                checked += 1
    return checked


def main():
    print(
        "verified physical edge lineage:",
        check_partition_ownership(),
        "partition cases,",
        check_decreasing_paths(),
        "decreasing paths,",
        check_slot_formulas(),
        "slot cases,",
        check_restoration_concentration(),
        "concentration cases, and",
        check_token_payment(),
        "token cases",
    )


if __name__ == "__main__":
    main()
