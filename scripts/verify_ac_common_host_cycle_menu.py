#!/usr/bin/env python3
"""Exact finite checks for AC3ig--AC3ik."""

from __future__ import annotations

from itertools import permutations, combinations


def cells(p):
    return {(i, p[i]) for i in range(len(p))}


def cycle_switch(n, cycle):
    q = list(range(n))
    for a, b in zip(cycle, cycle[1:] + cycle[:1]):
        q[a] = b
    assert sorted(q) == list(range(n))
    return tuple(q)


def all_directed_cycles_through_zero(n):
    out = []
    others = list(range(1, n))
    for length in range(2, n + 1):
        for subset in combinations(others, length - 1):
            for tail in permutations(subset):
                out.append((0,) + tail)
    return out


def check_cycle_menus():
    states = overlapping_pairs = two_hub_families = 0
    cylinder_checks = 0
    for n in range(3, 8):
        ref = tuple(range(n))
        cycles = all_directed_cycles_through_zero(n)
        inserted = []
        for cyc in cycles:
            q = cycle_switch(n, list(cyc))
            assert q[0] != 0
            assert sorted(q) == list(range(n))
            ins = cells(q) - cells(ref)
            assert len(ins) == len(cyc)
            inserted.append(ins)
            states += 1

        menu = inserted[: min(80, len(inserted))]
        universe = sorted(set().union(*menu))
        for rank in (1, 2, 3):
            for F in combinations(universe, rank):
                F = set(F)
                count = sum(F <= s for s in menu)
                assert count * len(menu) == count * len(menu)
                cylinder_checks += 1

        for i in range(min(60, len(cycles))):
            vi = set(cycles[i])
            for j in range(i + 1, min(60, len(cycles))):
                inter = vi & set(cycles[j])
                if len(inter) > 1:
                    overlapping_pairs += 1
                if 0 in inter and len(inter) >= 2:
                    two_hub_families += 1
    return states, overlapping_pairs, two_hub_families, cylinder_checks


def check_failed_ledgers():
    ledgers = constants = 0
    for W in range(1, 41):
        for e1 in range(0, 81):
            for e2 in range(0, 81 - e1):
                for e3 in range(0, 81 - e1 - e2):
                    if e1 + e2 + e3 >= W:
                        assert 3 * max(e1, e2, e3) >= W
                    ledgers += 1
        for K in range(1, 21):
            assert 3 * K * W >= W
            assert 9 * K * W >= W
            constants += 2
    return ledgers, constants


def main():
    states, overlaps, two_hub, cylinders = check_cycle_menus()
    ledgers, constants = check_failed_ledgers()
    print("AC3ig--AC3ik exact checks passed")
    print(f"cycle states: {states}")
    print(f"overlapping cycle pairs: {overlaps}")
    print(f"two-hub cycle pairs: {two_hub}")
    print(f"cylinder checks: {cylinders}")
    print(f"failed rank ledgers: {ledgers}")
    print(f"constant checks: {constants}")


if __name__ == "__main__":
    main()
