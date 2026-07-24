#!/usr/bin/env python3
"""Verify exact subgroup-overlap identities for the rational inverse map."""

from __future__ import annotations


def primes_through(limit: int) -> list[int]:
    return [
        n
        for n in range(3, limit + 1, 2)
        if all(n % d for d in range(2, int(n**0.5) + 1))
    ]


def prime_factors(number: int) -> set[int]:
    factors: set[int] = set()
    divisor = 2
    while divisor * divisor <= number:
        while number % divisor == 0:
            factors.add(divisor)
            number //= divisor
        divisor += 1
    if number > 1:
        factors.add(number)
    return factors


def primitive_root(p: int) -> int:
    factors = prime_factors(p - 1)
    return next(
        candidate
        for candidate in range(2, p)
        if all(pow(candidate, (p - 1) // factor, p) != 1 for factor in factors)
    )


def divisors(number: int) -> list[int]:
    return [value for value in range(1, number + 1) if number % value == 0]


def f_r(x: int, r: int, p: int) -> int:
    return x * (1 - x) * pow(r - x, -1, p) % p


def tau_r(x: int, r: int, p: int) -> int:
    return r * (x - 1) * pow(x - r, -1, p) % p


def phi(u: int, r: int, x0: int, p: int) -> int:
    numerator = r * (x0 * u - 1)
    denominator = x0 * (x0 * u - r)
    return numerator * pow(denominator, -1, p) % p


def verify(limit: int = 31) -> None:
    for p in primes_through(limit):
        generator = primitive_root(p)
        logarithm = {
            pow(generator, exponent, p): exponent for exponent in range(p - 1)
        }
        for order in divisors(p - 1):
            if order == 1:
                continue
            index = (p - 1) // order
            subgroup = {
                pow(generator, index * exponent, p) for exponent in range(order)
            }
            for coset_index in range(index):
                x0 = pow(generator, coset_index, p)
                coset = {x0 * u % p for u in subgroup}
                for r in range(2, p):
                    source = coset - {1, r}
                    overlap = {
                        u
                        for u in subgroup
                        if x0 * u % p not in (1, r)
                        and phi(u, r, x0, p) in subgroup
                    }
                    paired_points = {
                        x for x in source if tau_r(x, r, p) in source
                    }
                    assert len(overlap) == len(paired_points)

                    fixed = {x for x in source if tau_r(x, r, p) == x}
                    assert len(fixed) <= 2
                    assert all((x - r) ** 2 % p == r * (r - 1) % p for x in fixed)
                    nonfixed_pairs = {
                        tuple(sorted((x, tau_r(x, r, p))))
                        for x in paired_points
                        if tau_r(x, r, p) != x
                    }
                    assert len(nonfixed_pairs) == (len(overlap) - len(fixed)) // 2
                    image = {f_r(x, r, p) for x in source}
                    assert len(image) == len(source) - len(nonfixed_pairs)

                    for u in overlap:
                        v = phi(u, r, x0, p)
                        curve = (
                            x0 * x0 * u * v
                            - r * x0 * (u + v)
                            + r
                        ) % p
                        assert curve == 0

                    excluded = {
                        pow(x0, -1, p),
                        r * pow(x0, -1, p) % p,
                    }
                    orthogonality_total = 0
                    for u in set(range(1, p)) - excluded:
                        value = phi(u, r, x0, p)
                        sum_u = index if logarithm[u] % index == 0 else 0
                        sum_value = (
                            index if logarithm[value] % index == 0 else 0
                        )
                        orthogonality_total += sum_u * sum_value
                    assert orthogonality_total == index * index * len(overlap)


def main() -> None:
    verify()
    print("rational subgroup overlap: verified through prime 31")


if __name__ == "__main__":
    main()
