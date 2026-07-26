#!/usr/bin/env python3
"""Exact finite audit for AC3mw--AC3nb.

The general arguments are in
``docs/alternating-core-ri-quotient-reconstruction.md``.  This script exhausts
small prime fields and checks the cyclic subgroup/coset dictionaries together
with the nondegenerate rational-inverse identities and their quotient addresses.
"""

from __future__ import annotations

from dataclasses import dataclass


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def prime_factors(n: int) -> list[int]:
    out: list[int] = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def primitive_root(p: int) -> int:
    order = p - 1
    factors = prime_factors(order)
    for candidate in range(2, p):
        if all(pow(candidate, order // q, p) != 1 for q in factors):
            return candidate
    raise AssertionError(f"no primitive root found for prime {p}")


def inv(value: int, p: int) -> int:
    if value % p == 0:
        raise ZeroDivisionError("attempted inversion of zero")
    return pow(value, p - 2, p)


@dataclass(frozen=True)
class QuotientData:
    subgroup: frozenset[int]
    index: int
    address: dict[int, int]


def quotient_data(p: int, generator: int, h: int) -> QuotientData:
    n = p - 1
    k = n // h
    subgroup = frozenset(pow(generator, k * t, p) for t in range(h))
    assert len(subgroup) == h

    address: dict[int, int] = {}
    cosets: list[frozenset[int]] = []
    for j in range(k):
        representative = pow(generator, j, p)
        coset = frozenset((representative * x) % p for x in subgroup)
        assert len(coset) == h
        cosets.append(coset)
        for value in coset:
            assert value not in address
            address[value] = j

    assert len(set(cosets)) == k
    assert set(address) == set(range(1, p))
    return QuotientData(subgroup=subgroup, index=k, address=address)


def main() -> None:
    counters = {
        "prime fields": 0,
        "subgroup orders": 0,
        "canonical cosets": 0,
        "stock inequalities": 0,
        "physical RI occurrences": 0,
        "quotient reconstructions": 0,
        "component-bound systems": 0,
    }

    for p in [q for q in range(5, 24) if is_prime(q)]:
        n = p - 1
        generator = primitive_root(p)
        counters["prime fields"] += 1

        quotients: dict[int, QuotientData] = {}
        for h in divisors(n):
            data = quotient_data(p, generator, h)
            quotients[h] = data
            counters["subgroup orders"] += 1
            counters["canonical cosets"] += data.index

            # Canonical quotient arithmetic in exponent addresses.
            for x in range(1, p):
                for y in range(1, p):
                    lhs = data.address[(x * y) % p]
                    rhs = (data.address[x] + data.address[y]) % data.index
                    assert lhs == rhs
                assert data.address[inv(x, p)] == (-data.address[x]) % data.index

        coset_stock = sum(n // h for h in divisors(n))
        assert coset_stock == counters["canonical cosets"] - sum(
            sum((q - 1) // h for h in divisors(q - 1))
            for q in [r for r in range(5, p) if is_prime(r)]
        )
        assert coset_stock <= n * len(divisors(n)) <= n * n
        counters["stock inequalities"] += 1

        # Safe normalized-component bounds from AC3mz.
        scale_free = sum(
            sum((n // h) ** (m + 3) for m in range(1, 5))
            for h in divisors(n)
        )
        scale_local = sum(
            sum((n // h) ** (m + 4) for m in range(1, 5))
            for h in divisors(n)
        )
        assert scale_free <= 4 * n**8
        assert scale_local <= 4 * n**9
        counters["component-bound systems"] += 2

        # Enumerate nondegenerate canonical RI occurrences through the
        # parameters r,c,a,x.  The physical tuple (a,b,x,u,z) is reconstructed.
        for r in range(2, p):  # r != 1
            for c in range(1, p):
                if c in (1, r):
                    continue

                image = c * (1 - c) * inv((r - c) % p, p) % p
                assert image != 0
                companion = r * (c - 1) * inv((c - r) % p, p) % p
                assert companion not in (0, r)

                # Rational-inverse identities.
                assert c * companion % p == r * image % p
                companion_image = (
                    companion
                    * (1 - companion)
                    * inv((r - companion) % p, p)
                    % p
                )
                assert companion_image == image

                for a in range(1, p):
                    b = r * a % p
                    for x in range(1, p):
                        u = image * x % p
                        z = c * x % p
                        assert b * inv(a, p) % p == r
                        assert z * inv(x, p) % p == c
                        assert u * inv(x, p) % p == image
                        counters["physical RI occurrences"] += 1

                        for data in quotients.values():
                            k = data.index
                            addr = data.address
                            a_coset = addr[c]
                            b_coset = addr[companion]
                            c_coset = addr[image]
                            r_coset = addr[r]
                            scale = addr[x]

                            assert b_coset == (r_coset + c_coset - a_coset) % k
                            assert addr[u] == (c_coset + scale) % k
                            assert addr[z] == (a_coset + scale) % k
                            counters["quotient reconstructions"] += 1

        # AC3na ambient physical occurrence stock with L_RI=1.
        assert len(divisors(n)) * n**5 <= n**6
        counters["stock inequalities"] += 1

    expected = {
        "prime fields": 7,
        "subgroup orders": 32,
        "canonical cosets": 171,
        "stock inequalities": 14,
        "physical RI occurrences": 369_024,
        "quotient reconstructions": 1_737_696,
        "component-bound systems": 14,
    }
    assert counters == expected, (counters, expected)

    print("AC3mw--AC3nb exact finite audit passed")
    for label, count in counters.items():
        print(f"  {label}: {count:,}")


if __name__ == "__main__":
    main()
