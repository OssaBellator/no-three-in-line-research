#!/usr/bin/env python3
"""Verify CMR70--CMR72 on finite prime-power column trees."""
from __future__ import annotations

import argparse
from itertools import combinations, product


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def valuation(n: int, p: int) -> int:
    assert n != 0
    n = abs(n)
    value = 0
    while n % p == 0:
        n //= p
        value += 1
    return value


def prime_power_data(n: int) -> tuple[int, int] | None:
    for p in range(3, n + 1, 2):
        if not is_prime(p):
            continue
        value = p
        k = 1
        while value < n:
            value *= p
            k += 1
        if value == n:
            return p, k
    return None


def clustering(
    columns: tuple[int, int, int], p: int
) -> tuple[int, int, tuple[int, int] | None, tuple[int, ...]]:
    x1, x2, x3 = columns
    pairs = ((0, 1), (0, 2), (1, 2))
    values = tuple(valuation(columns[i] - columns[j], p) for i, j in pairs)
    r = min(values)
    s = max(values)
    closest = pairs[values.index(s)] if s > r else None

    kappas = (x3 - x2, x1 - x3, x2 - x1)
    common = min(valuation(value, p) for value in kappas)
    reduced = tuple(value // (p**common) for value in kappas)
    units = tuple(i for i, value in enumerate(reduced) if value % p != 0)
    assert len(units) >= 2
    return r, s, closest, units


def is_transverse(
    layers: tuple[int, int, int],
    r: int,
    s: int,
    closest: tuple[int, int] | None,
) -> bool:
    if s == r:
        return len(set(layers)) > 1
    assert closest is not None
    return layers[closest[0]] != layers[closest[1]]


def has_unique_unit_key(
    columns: tuple[int, int, int],
    layers: tuple[int, int, int],
    units: tuple[int, ...],
    p: int,
    depth: int,
) -> bool:
    modulus = p**depth
    keys = [(layers[i], columns[i] % modulus) for i in range(3)]
    return any(keys.count(keys[i]) == 1 for i in units)


def verify_instance(p: int, k: int) -> tuple[int, int, int]:
    n = p**k
    transverse = 0
    nontransverse = 0
    depth_checks = 0

    for columns in combinations(range(n), 3):
        r, s, closest, units = clustering(columns, p)
        local_nontransverse = 0
        for layers in product((0, 1), repeat=3):
            if is_transverse(layers, r, s, closest):
                transverse += 1
                for depth in range(k):
                    assert has_unique_unit_key(
                        columns, layers, units, p, depth
                    ), (p, k, columns, layers, depth, units)
                    depth_checks += 1
            else:
                nontransverse += 1
                local_nontransverse += 1
                for depth in range(s + 1, k):
                    assert has_unique_unit_key(
                        columns, layers, units, p, depth
                    )
                    depth_checks += 1
        assert local_nontransverse <= 4

    # Verify the elementary pair-codegree counting bounds before probabilities
    # are inserted.  Exact third-column populations are no larger than the
    # N and 2N/p^t bounds used in CMR72.
    for x1, x2 in combinations(range(n), 2):
        u = valuation(x1 - x2, p)
        by_t = [0] * k
        for x3 in range(n):
            if x3 in (x1, x2):
                continue
            t = max(
                u,
                valuation(x1 - x3, p),
                valuation(x2 - x3, p),
            )
            by_t[t] += 1
        assert by_t[u] < n
        for t in range(u + 1, k):
            assert by_t[t] <= 2 * n // (p**t)

    return transverse, nontransverse, depth_checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=125)
    args = parser.parse_args()

    instances = 0
    transverse = 0
    nontransverse = 0
    checks = 0
    for n in range(9, args.max_modulus + 1):
        data = prime_power_data(n)
        if data is None:
            continue
        p, k = data
        if k < 2 or p % 4 != 1:
            continue
        a, b, c = verify_instance(p, k)
        instances += 1
        transverse += a
        nontransverse += b
        checks += c

    print(
        "verified layer-transverse certificates "
        f"instances={instances}; transverse={transverse}; "
        f"nontransverse={nontransverse}; depth-checks={checks}"
    )


if __name__ == "__main__":
    main()
