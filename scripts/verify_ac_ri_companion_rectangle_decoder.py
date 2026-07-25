#!/usr/bin/env python3
"""Finite checks for AC3et--AC3ey."""

from fractions import Fraction
from itertools import combinations, permutations, product


def derangements(n):
    return [p for p in permutations(range(n)) if all(p[i] != i for i in range(n))]


def repaired_blockers(active, blocker):
    selected = [i for i in range(len(active)) if active[i] == blocker[i]]
    options = []
    if not selected:
        options.append(blocker)
    elif len(selected) == 1:
        c = selected[0]
        for auxiliary in range(len(active)):
            if auxiliary == c:
                continue
            repaired = list(blocker)
            repaired[c], repaired[auxiliary] = repaired[auxiliary], repaired[c]
            options.append(tuple(repaired))
    else:
        rows = [blocker[c] for c in selected]
        for pi in derangements(len(selected)):
            repaired = list(blocker)
            for i, c in enumerate(selected):
                repaired[c] = rows[pi[i]]
            options.append(tuple(repaired))

    for repaired in options:
        assert sorted(repaired) == list(range(len(active)))
        assert all(active[i] != repaired[i] for i in range(len(active)))
    return selected, options


def direct_rectangle_checks():
    systems = repairs = 0
    occupancy = {0: 0, 1: 0, 2: 0}
    for n in range(3, 8):
        for c0, c1 in combinations(range(n), 2):
            switched = list(range(n))
            switched[c0], switched[c1] = c1, c0
            switched = tuple(switched)
            for blocker in derangements(n):
                systems += 1
                selected, options = repaired_blockers(switched, blocker)
                assert len(selected) <= 2
                occupancy[len(selected)] += 1
                repairs += len(options)
    return systems, repairs, occupancy


def absent_composite_checks():
    records = stage_one_repairs = stage_two_repairs = protected = 0
    occupancy_one = {0: 0, 1: 0, 2: 0}
    occupancy_two = {0: 0, 1: 0, 2: 0}

    for n in range(4, 7):
        for original_anchor, target_col, target_row in permutations(range(n), 3):
            installed = list(range(n))
            installed[target_col] = target_row
            installed[target_row] = target_col
            assert installed[original_anchor] == original_anchor
            installed = tuple(installed)

            final = list(installed)
            final[original_anchor] = target_row
            final[target_col] = original_anchor
            assert sorted(final) == list(range(n))
            final = tuple(final)

            available = set(range(n)) - {original_anchor, target_col, target_row}
            for support in combinations(sorted(available), min(2, len(available))):
                assert all(final[x] == x for x in support)
                protected += 1

            for blocker in derangements(n):
                records += 1
                selected_one, options_one = repaired_blockers(installed, blocker)
                assert len(selected_one) <= 2
                occupancy_one[len(selected_one)] += 1
                stage_one_repairs += len(options_one)

                for blocker_one in options_one:
                    selected_two, options_two = repaired_blockers(final, blocker_one)
                    assert len(selected_two) <= 2
                    occupancy_two[len(selected_two)] += 1
                    stage_two_repairs += len(options_two)

    return (
        records,
        stage_one_repairs,
        stage_two_repairs,
        protected,
        occupancy_one,
        occupancy_two,
    )


def geometry_checks():
    rectangles = line_points = midpoint_hits = 0
    for x0, y0, x1, y1 in product(range(-3, 4), repeat=4):
        if x0 == x1 or y0 == y1:
            continue
        a = (x0, y0)
        z = (x1, y1)
        c = (x0, y1)
        d = (x1, y0)
        rectangles += 1

        for px, py in product(range(-5, 6), repeat=2):
            if (px - x0) * (y1 - y0) != (py - y0) * (x1 - x0):
                continue
            line_points += 1
            determinant = (c[0] - px) * (d[1] - py) - (c[1] - py) * (d[0] - px)
            midpoint = 2 * px == a[0] + z[0] and 2 * py == a[1] + z[1]
            assert (determinant == 0) == midpoint
            midpoint_hits += int(midpoint)

    return rectangles, line_points, midpoint_hits


def ledger_checks():
    three_mask_ledgers = seven_mask_ledgers = 0
    for weights in product(range(4), repeat=3):
        total = sum(weights)
        for destroyed in range(1, 10):
            if total >= destroyed:
                assert max(weights) >= Fraction(destroyed, 3)
            three_mask_ledgers += 1

    for weights in product(range(3), repeat=7):
        total = sum(weights)
        for destroyed in range(1, 10):
            if total >= destroyed:
                assert max(weights) >= Fraction(destroyed, 7)
            seven_mask_ledgers += 1

    return three_mask_ledgers, seven_mask_ledgers


def constant_checks():
    checks = 0
    for k in range(1, 6):
        for source_weight in range(1, 10):
            assert Fraction(source_weight, 3 * 31 * k * 3) == Fraction(source_weight, 279 * k)
            assert Fraction(source_weight, 51 * k * 7) == Fraction(source_weight, 357 * k)
            checks += 2
    return checks


def main():
    direct = direct_rectangle_checks()
    absent = absent_composite_checks()
    geometry = geometry_checks()
    ledgers = ledger_checks()
    constants = constant_checks()
    print(
        "AC RI companion rectangle decoder: verified "
        f"direct={direct}, absent={absent}, geometry={geometry}, "
        f"ledgers={ledgers}, and {constants} constants"
    )


if __name__ == "__main__":
    main()
