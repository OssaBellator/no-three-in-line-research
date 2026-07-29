#!/usr/bin/env python3
"""Finite checks for SAS5hi--SAS5hl."""

from __future__ import annotations

from itertools import combinations, permutations


def swap_rows(pi: tuple[int, ...], i: int, j: int) -> tuple[int, ...]:
    out = list(pi)
    out[i], out[j] = out[j], out[i]
    return tuple(out)


def is_host_matching(pi: tuple[int, ...], host: tuple[int, ...]) -> bool:
    return len(set(pi)) == len(pi) and all(host[r] & (1 << pi[r]) for r in range(len(pi)))


def edge_disjoint(pi: tuple[int, ...], rho: tuple[int, ...]) -> bool:
    return all(pi[r] != rho[r] for r in range(len(pi)))


def main() -> None:
    checked_one = 0
    checked_two = 0
    for n in range(2, 6):
        perms = list(permutations(range(n)))
        for pi in perms:
            base = tuple(1 << pi[r] for r in range(n))
            optional = [(r, c) for r in range(n) for c in range(n) if c != pi[r]]
            masks = range(1 << len(optional)) if n <= 3 else range(0, 1 << min(len(optional), 8))
            for code in masks:
                host = list(base)
                for k, (r, c) in enumerate(optional[:8] if n > 3 else optional):
                    if code & (1 << k):
                        host[r] |= 1 << c
                host_t = tuple(host)
                assert is_host_matching(pi, host_t)
                for i, j in combinations(range(n), 2):
                    pi2 = swap_rows(pi, i, j)
                    criterion = bool(host_t[i] & (1 << pi[j])) and bool(host_t[j] & (1 << pi[i]))
                    assert is_host_matching(pi2, host_t) == criterion
                    assert swap_rows(pi2, i, j) == pi
                    if criterion:
                        changed = {r for r in range(n) if pi[r] != pi2[r]}
                        assert changed == {i, j}
                    checked_one += 1

                    for rho in perms:
                        if not is_host_matching(rho, host_t) or not edge_disjoint(pi, rho):
                            continue
                        direct = is_host_matching(pi2, host_t) and edge_disjoint(pi2, rho)
                        criterion_two = criterion and pi[j] != rho[i] and pi[i] != rho[j]
                        assert direct == criterion_two
                        if direct:
                            assert edge_disjoint(swap_rows(pi2, i, j), rho)
                        checked_two += 1

    print(f"verified {checked_one} one-layer and {checked_two} two-layer swap checks")


if __name__ == "__main__":
    main()
