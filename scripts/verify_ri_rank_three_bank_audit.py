#!/usr/bin/env python3
"""Finite checks for RI5bl--RI5bn."""

from itertools import permutations, product
from math import factorial


def falling(m: int, r: int) -> int:
    out = 1
    for j in range(r):
        out *= m - j
    return out


def states(m: int, h: int):
    for sigma in permutations(range(m)):
        for shifts in product(range(h), repeat=m):
            yield sigma, shifts


def compatible(state, sources, targets, shifts) -> bool:
    sigma, t = state
    return all(sigma[a] == b and t[a] == s for a, b, s in zip(sources, targets, shifts))


def main() -> None:
    checks = 0

    # Exhaust the actual I6 state space for the small nontrivial range.
    for m in range(3, 5):
        for h in range(1, 4):
            bank = list(states(m, h))
            expected = factorial(m - 3) * h ** (m - 3)
            sources = (0, 1, 2)
            for targets in permutations(range(m), 3):
                for shifts in product(range(h), repeat=3):
                    count = sum(compatible(st, sources, targets, shifts) for st in bank)
                    assert count == expected
                    assert count * falling(m, 3) * h**3 == len(bank)
                    checks += 1

            sample = []
            for idx, targets in enumerate(permutations(range(m), 3)):
                if idx == 5:
                    break
                sample.append((sources, targets, (0, 0, 0), idx + 1))
            raw = sum(weight for *_, weight in sample)
            total = sum(
                sum(weight for src, tgt, sh, weight in sample if compatible(st, src, tgt, sh))
                for st in bank
            )
            assert total * falling(m, 3) * h**3 == raw * len(bank)

    # Check the exact counting identity algebraically in a wider range.
    for m in range(3, 10):
        for h in range(1, 9):
            count = factorial(m - 3) * h ** (m - 3)
            total = factorial(m) * h**m
            assert count * falling(m, 3) * h**3 == total
            checks += 1

    repeated_source = (0, 0, 1)
    repeated_target = (0, 0, 1)
    assert len(set(repeated_source)) < 3
    assert len(set(repeated_target)) < 3

    print(f"verified {checks} rank-three I6 count instances")


if __name__ == "__main__":
    main()
