#!/usr/bin/env python3
"""Finite checks for RI5bo--RI5bq."""

from itertools import permutations, product
from math import factorial


def falling(m: int, r: int) -> int:
    out = 1
    for j in range(r):
        out *= m - j
    return out


def main() -> None:
    state_checks = 0
    cylinder_checks = 0
    for m in range(1, 7):
        for h in range(1, 5):
            regions = [set(range(10 * a, 10 * a + 4)) for a in range(m)]
            assert all(regions[a].isdisjoint(regions[b]) for a in range(m) for b in range(a))

            states = []
            for sigma in permutations(range(m)):
                for shifts in product(range(h), repeat=m):
                    local = tuple((a, sigma[a], shifts[a], tuple(sorted(regions[a]))) for a in range(m))
                    states.append(local)
            assert len(states) == factorial(m) * h**m
            assert len(set(states)) == len(states)
            state_checks += len(states)

            for r in range(1, min(3, m) + 1):
                sources = tuple(range(r))
                targets = tuple(range(r))
                shifts = tuple(0 for _ in range(r))
                count = 0
                for state in states:
                    if all(state[a][1] == targets[a] and state[a][2] == shifts[a] for a in sources):
                        count += 1
                expected = factorial(m - r) * h ** (m - r)
                assert count == expected
                assert count * falling(m, r) * h**r == len(states)
                cylinder_checks += 1

    # Overlap and cross-region constraints are explicit failed witnesses.
    assert not {0, 1}.isdisjoint({1, 2})
    cross_constraint = {0, 10}
    assert len([a for a, region in enumerate([{0, 1}, {10, 11}]) if region & cross_constraint]) == 2

    print(f"verified {state_checks} physical product states and {cylinder_checks} cylinders")


if __name__ == "__main__":
    main()
