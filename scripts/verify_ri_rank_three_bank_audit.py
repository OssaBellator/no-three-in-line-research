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
    for m in range(3, 7):
        for h in range(1, 5):
            bank = list(states(m, h))
            expected = factorial(m - 3) * h ** (m - 3)
            sources = (0, 1, 2)
            for targets in permutations(range(m), 3):
                for shifts in product(range(h), repeat=3):
                    count = sum(compatible(st, sources, targets, shifts) for st in bank)
                    assert count == expected
                    assert count * falling(m, 3) * h**3 == len(bank)
                    checks += 1

            # Repeated source/target prescriptions are not rank-three cylinders.
            repeated_source = (0, 0, 1)
            repeated_target = (0, 0, 1)
            assert len(set(repeated_source)) < 3
            assert len(set(repeated_target)) < 3

            # Weighted linearity check on a deterministic sample.
            sample = []
            for idx, targets in enumerate(permutations(range(m), 3)):
                if idx == 5:
                    break
                sample.append((sources, targets, (0, 0, 0), idx + 1))
            raw = sum(weight for *_, weight in sample)
            total = 0
            for st in bank:
                total += sum(weight for src, tgt, sh, weight in sample if compatible(st, src, tgt, sh))
            assert total * falling(m, 3) * h**3 == raw * len(bank)

    print(f"verified {checks} compatible rank-three I6 cylinders")


if __name__ == "__main__":
    main()
