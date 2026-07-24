#!/usr/bin/env python3
"""Exact checks for CMR113--CMR115 balanced-law classification."""

from __future__ import annotations

from itertools import combinations

from sympy import Matrix

Point = tuple[int, int]


def det(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def tau(x: int, p: int) -> int:
    return 0 if x == 0 else pow(x, -1, p)


def reciprocal_map(b: int, c: int, p: int) -> tuple[int, ...]:
    return tuple((b + c * tau(x, p)) % p for x in range(p))


def no_three(values: tuple[int, ...]) -> bool:
    points = [(x, y) for x, y in enumerate(values)]
    return all(det(*triple) != 0 for triple in combinations(points, 3))


def verify_fourier_rigidity(p: int) -> None:
    variables = [(b, c) for c in range(1, p) for b in range(p)]
    rows: list[list[int]] = []
    for u in range(p):
        for y in range(1, p):
            rows.append([
                (1 if (b + u * c) % p == y else 0)
                - (1 if (b + u * c) % p == 0 else 0)
                for b, c in variables
            ])

    matrix = Matrix(rows)
    nullspace = matrix.nullspace()
    assert len(nullspace) == p - 1
    for vector in nullspace:
        for c in range(1, p):
            values = [vector[variables.index((b, c))] for b in range(p)]
            assert len(set(values)) == 1


def verify_endpoint_classification(p: int) -> None:
    squares = {x * x % p for x in range(1, p)}
    for c in range(1, p):
        at_zero = no_three(reciprocal_map(0, c, p))
        at_top = no_three(reciprocal_map(p - 1, c, p))
        assert at_zero == (c not in squares)
        assert at_top == ((-c) % p not in squares)


def verify_balanced_family(p: int) -> None:
    squares = {x * x % p for x in range(1, p)}
    nonsquares = [c for c in range(1, p) if c not in squares]

    if p % 4 == 1:
        maps = [reciprocal_map(b, c, p) for c in nonsquares for b in range(p)]
        assert all(no_three(values) for values in maps)
        target = len(nonsquares)
        for x in range(p):
            counts = [sum(values[x] == y for values in maps) for y in range(p)]
            assert counts == [target] * p
    else:
        valid_zero = {
            c for c in range(1, p) if no_three(reciprocal_map(0, c, p))
        }
        valid_top = {
            c for c in range(1, p)
            if no_three(reciprocal_map(p - 1, c, p))
        }
        assert not (valid_zero & valid_top)


def main() -> None:
    checked = 0
    for p in range(3, 32):
        if not is_prime(p) or p == 2:
            continue
        verify_endpoint_classification(p)
        verify_balanced_family(p)
        if p <= 11:
            verify_fourier_rigidity(p)
        checked += 1
    print(f"verified balanced-law classification for {checked} odd primes through 31")


if __name__ == "__main__":
    main()
