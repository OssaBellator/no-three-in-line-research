#!/usr/bin/env python3
"""Finite checks for CMR748--CMR754."""

from math import ceil, log2
import random


def has_perfect_matching(side, allowed):
    matched_target = {}

    def augment(source, seen):
        for target in range(side):
            if (source, target) not in allowed or target in seen:
                continue
            seen.add(target)
            if (
                target not in matched_target
                or augment(matched_target[target], seen)
            ):
                matched_target[target] = source
                return True
        return False

    return all(augment(source, set()) for source in range(side))


def grid_line_cells(side, first, second):
    x1, y1 = first
    x2, y2 = second
    return {
        (x, y)
        for x in range(side)
        for y in range(side)
        if (x - x1) * (y2 - y1) == (y - y1) * (x2 - x1)
    }


def exact_line_checks():
    checked = 0
    for side in range(2, 9):
        cells = [
            (source, target)
            for source in range(side)
            for target in range(side)
        ]
        for index, first in enumerate(cells):
            for second in cells[index + 1 :]:
                if first[0] == second[0] or first[1] == second[1]:
                    continue
                line = grid_line_cells(side, first, second)
                assert len({source for source, _ in line}) == len(line)
                assert len({target for _, target in line}) == len(line)
                checked += 1
    return checked


def random_matching_board_checks():
    rng = random.Random(20260726)
    checked = 0
    for side in range(4, 31):
        capacity = (side - 4) // 2
        for protected_count in range(capacity + 1):
            for _ in range(50):
                old = list(range(side))
                opposite = list(range(side))
                rng.shuffle(old)
                rng.shuffle(opposite)
                forbidden = {
                    (source, old[source])
                    for source in range(side)
                } | {
                    (source, opposite[source])
                    for source in range(side)
                }

                for _ in range(protected_count):
                    line_matching = list(range(side))
                    rng.shuffle(line_matching)
                    for source in range(side):
                        if rng.random() < 0.7:
                            forbidden.add(
                                (source, line_matching[source])
                            )

                allowed = {
                    (source, target)
                    for source in range(side)
                    for target in range(side)
                } - forbidden

                lower_bound = side - protected_count - 2
                assert lower_bound >= side / 2
                assert min(
                    sum(
                        (source, target) in allowed
                        for target in range(side)
                    )
                    for source in range(side)
                ) >= lower_bound
                assert min(
                    sum(
                        (source, target) in allowed
                        for source in range(side)
                    )
                    for target in range(side)
                ) >= lower_bound
                assert has_perfect_matching(side, allowed)
                checked += 1
    return checked


def arithmetic_checks():
    checked = 0
    for side in range(4, 500):
        capacity = (side - 4) // 2
        assert side >= 2 * capacity + 4
        if capacity + 1 > 0:
            assert side < 2 * (capacity + 1) + 4
        if side >= 6:
            assert capacity >= 1
        bands = ceil(log2(side))
        saturated = capacity + 1
        localized = ceil(saturated / bands)
        assert localized * bands >= saturated
        checked += 1
    return checked


def main():
    line_checks = exact_line_checks()
    board_checks = random_matching_board_checks()
    ledger_checks = arithmetic_checks()
    print(
        "verified recurrent target-line reserve:",
        line_checks,
        "nonaxis grid lines,",
        board_checks,
        "protected boards, and",
        ledger_checks,
        "capacity instances",
    )


if __name__ == "__main__":
    main()
