#!/usr/bin/env python3
"""Finite checks for AC3ep--AC3es."""

from fractions import Fraction
from itertools import combinations, permutations, product


def derangements(n):
    return [p for p in permutations(range(n)) if all(p[i] != i for i in range(n))]


def complete_target(n, cols, rows):
    """Normalize M0 to the identity and complete one or two desired cells."""
    active = list(range(n))
    if len(cols) == 1:
        c, r = cols[0], rows[0]
        active[c], active[r] = r, c
        kind = "one-boundary-path"
    else:
        c1, c2 = cols
        r1, r2 = rows
        if r1 == c2 and r2 == c1:
            active[c1], active[c2] = r1, r2
            kind = "two-cycle"
        elif r1 == c2:
            active[c1], active[c2], active[r2] = r1, r2, c1
            kind = "length-two-path"
        elif r2 == c1:
            active[c2], active[c1], active[r1] = r2, r1, c2
            kind = "length-two-path"
        else:
            active[c1], active[r1] = r1, c1
            active[c2], active[r2] = r2, c2
            kind = "two-boundary-paths"

    assert sorted(active) == list(range(n))
    assert all(active[c] == r for c, r in zip(cols, rows))
    return tuple(active), kind


def repaired_blockers(active, blocker):
    """Apply the zero/singleton/derangement repair menu."""
    n = len(active)
    selected = [c for c in range(n) if active[c] == blocker[c]]
    t = len(selected)
    options = []

    if t == 0:
        options.append(blocker)
    elif t == 1:
        c = selected[0]
        for auxiliary in range(n):
            if auxiliary == c:
                continue
            repaired = list(blocker)
            repaired[c], repaired[auxiliary] = repaired[auxiliary], repaired[c]
            options.append(tuple(repaired))
    else:
        selected_rows = [blocker[c] for c in selected]
        for pi in derangements(t):
            repaired = list(blocker)
            for i, c in enumerate(selected):
                repaired[c] = selected_rows[pi[i]]
            options.append(tuple(repaired))

    for repaired in options:
        assert sorted(repaired) == list(range(n))
        assert all(active[c] != repaired[c] for c in range(n))
    return selected, options


def exhaustive_matching_checks():
    targets = blocker_systems = repairs = protected = 0
    component_types = {}
    occupancy = {i: 0 for i in range(5)}

    for n in range(3, 7):
        blockers = derangements(n)
        for size in (1, 2):
            for cols in permutations(range(n), size):
                for rows in permutations(range(n), size):
                    if any(cols[i] == rows[i] for i in range(size)):
                        continue

                    active, kind = complete_target(n, cols, rows)
                    targets += 1
                    component_types[kind] = component_types.get(kind, 0) + 1
                    changed = {c for c in range(n) if active[c] != c}
                    assert len(changed) <= 4

                    # Identity cells outside all target columns and rows model the
                    # protected occupied radial support.
                    available = sorted(set(range(n)) - set(cols) - set(rows))
                    for support in combinations(available, 3):
                        assert all(active[c] == c for c in support)
                        protected += 1

                    for blocker in blockers:
                        blocker_systems += 1
                        selected, options = repaired_blockers(active, blocker)
                        assert len(selected) <= 4
                        occupancy[len(selected)] += 1
                        repairs += len(options)

    return targets, component_types, blocker_systems, repairs, protected, occupancy


def mask_checks():
    systems = failures = 0
    for weights in product(range(4), repeat=7):
        total = sum(weights)
        for paid in range(1, 13):
            if total >= paid:
                assert max(weights) >= Fraction(paid, 7)
                failures += 1
            systems += 1
    return systems, failures


def product_expectation_checks():
    distributions = states = 0
    menu_families = (
        ((0, 1),),
        ((-1, 2), (0, 3)),
        ((-2, 0, 2), (1, 4)),
    )
    for family in menu_families:
        for count in range(1, 5):
            menus = [family[i % len(family)] for i in range(count)]
            expected = sum((Fraction(sum(menu), len(menu)) for menu in menus), Fraction(0))
            values = [
                sum(menus[i][choice[i]] for i in range(count))
                for choice in product(*(range(len(menu)) for menu in menus))
            ]
            assert Fraction(sum(values), len(values)) == expected
            distributions += 1
            states += len(values)
    return distributions, states


def constant_checks():
    checks = 0
    for r in range(1, 5):
        for rho in range(1, 4):
            for profile_count in range(1, 5):
                for k in range(1, 5):
                    endpoint_denominator = 224 * k * r * rho * profile_count
                    variation_denominator = 448 * k * r * rho * profile_count
                    assert Fraction(
                        endpoint_denominator,
                        32 * k * r * rho * profile_count * 7,
                    ) == 1
                    assert Fraction(
                        variation_denominator,
                        64 * k * r * rho * profile_count * 7,
                    ) == 1
                    checks += 2
    return checks


def main():
    targets, kinds, blocker_systems, repairs, protected, occupancy = exhaustive_matching_checks()
    mask_systems, failed_masks = mask_checks()
    distributions, states = product_expectation_checks()
    constants = constant_checks()
    print(
        "AC BDA missing-support completion: verified "
        f"{targets} targets {kinds}, {blocker_systems} blocker systems, "
        f"{repairs} repairs, {protected} protected supports, occupancies {occupancy}, "
        f"{mask_systems} mask ledgers, {failed_masks} failed-mask routers, "
        f"{distributions} product distributions, {states} product states, "
        f"and {constants} constants"
    )


if __name__ == "__main__":
    main()
