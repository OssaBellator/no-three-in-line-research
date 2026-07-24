#!/usr/bin/env python3
"""Verify exact F_r fibres and the RI1/RI4 obstruction examples."""

from __future__ import annotations

from itertools import combinations


def primes_through(limit: int) -> list[int]:
    return [
        n
        for n in range(3, limit + 1, 2)
        if all(n % d for d in range(2, int(n**0.5) + 1))
    ]


def f_r(x: int, r: int, p: int) -> int:
    assert x != r
    return x * (1 - x) * pow(r - x, -1, p) % p


def tau_r(x: int, r: int, p: int) -> int:
    assert x != r
    return r * (x - 1) * pow(x - r, -1, p) % p


def verify_fibres(limit: int = 43) -> None:
    for p in primes_through(limit):
        for r in range(2, p):
            domain = [x for x in range(1, p) if x not in (1, r)]
            fibres: dict[int, set[int]] = {}
            for x in domain:
                partner = tau_r(x, r, p)
                assert partner in domain
                assert tau_r(partner, r, p) == x
                assert f_r(partner, r, p) == f_r(x, r, p)
                fibres.setdefault(f_r(x, r, p), set()).add(x)
                for z in domain:
                    left = (f_r(x, r, p) - f_r(z, r, p)) % p
                    right = (
                        (x - z)
                        * (r - r * (x + z) + x * z)
                        * pow((r - x) * (r - z), -1, p)
                    ) % p
                    assert left == right

            for fibre in fibres.values():
                assert 1 <= len(fibre) <= 2
                first = next(iter(fibre))
                assert fibre == {first, tau_r(first, r, p)}


def verify_all_small_subsets(limit: int = 11) -> None:
    for p in primes_through(limit):
        for r in range(2, p):
            domain = [x for x in range(1, p) if x not in (1, r)]
            for size in range(len(domain) + 1):
                for subset in combinations(domain, size):
                    image = {f_r(x, r, p) for x in subset}
                    assert len(image) >= (size + 1) // 2


def verify_full_subgroup_obstruction() -> None:
    p = 101
    r = 7
    epsilon = 0.4
    domain = {x for x in range(1, p) if x not in (1, r)}
    image = {f_r(x, r, p) for x in domain}
    assert len(domain) > (0.5 + epsilon) * (p - 1)
    assert image <= set(range(1, p))
    # H = F_p^* has exactly one multiplicative coset.
    assert len(image) <= p - 1


def verify_singleton_chain() -> None:
    p = 29
    values = list(range(2, 13))
    ratios: list[int] = []
    for source, target in zip(values, values[1:]):
        ratio = (
            source
            + source * (1 - source) * pow(target, -1, p)
        ) % p
        assert ratio not in (0, 1, source)
        assert f_r(source, ratio, p) == target
        ratios.append(ratio)

    assert len(set(values)) == len(values)
    assert ratios == [11, 16, 19, 21, 10, 9, 5, 25, 15, 26]


def verify(limit: int = 43) -> None:
    verify_fibres(limit)
    verify_all_small_subsets()
    verify_full_subgroup_obstruction()
    verify_singleton_chain()


def main() -> None:
    verify()
    print("rational inverse fibres and obstruction regressions: verified")


if __name__ == "__main__":
    main()
