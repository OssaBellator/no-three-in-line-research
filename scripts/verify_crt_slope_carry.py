#!/usr/bin/env python3
"""Verify CMCRT6 and the exact slope-carry identities CMCRT8--CMCRT9."""
from __future__ import annotations

from itertools import combinations, product


def determinant(a: tuple[int, int], b: tuple[int, int]) -> int:
    return a[0] * b[1] - a[1] * b[0]


def affine_collinear(a, b, c, p: int) -> bool:
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        - (c[0] - a[0]) * (b[1] - a[1])
    ) % p == 0


def verify_arc_bound_p3() -> int:
    p = 3
    points = list(product(range(p), repeat=2))
    maximum = 0
    for mask in range(1 << len(points)):
        chosen = [points[i] for i in range(len(points)) if mask & (1 << i)]
        if len(chosen) <= maximum:
            continue
        if any(affine_collinear(*triple, p) for triple in combinations(chosen, 3)):
            continue
        maximum = len(chosen)
    assert maximum == p + 2
    return 1 << len(points)


def verify_local_identity() -> int:
    checks = 0
    for m in (2, 3, 5, 7):
        for d in product(range(m), repeat=2):
            if d == (0, 0):
                continue
            for alpha in range(m):
                for beta in range(m):
                    for A in product(range(-2, 3), repeat=2):
                        for B in product(range(-2, 3), repeat=2):
                            U = (alpha * d[0] + m * A[0], alpha * d[1] + m * A[1])
                            V = (beta * d[0] + m * B[0], beta * d[1] + m * B[1])
                            signature = (
                                alpha * determinant(d, B)
                                - beta * determinant(d, A)
                                + m * determinant(A, B)
                            )
                            assert determinant(U, V) == m * signature
                            checks += 1
    return checks


def local_representation(U: tuple[int, int], V: tuple[int, int], p: int):
    u = (U[0] % p, U[1] % p)
    v = (V[0] % p, V[1] % p)
    assert determinant(u, v) % p == 0

    if u != (0, 0):
        d = u
        alpha = 1
        beta = next(
            scalar
            for scalar in range(p)
            if (scalar * d[0] % p, scalar * d[1] % p) == v
        )
    elif v != (0, 0):
        d = v
        alpha = 0
        beta = 1
    else:
        d = (1, 0)
        alpha = 0
        beta = 0

    A = ((U[0] - alpha * d[0]) // p, (U[1] - alpha * d[1]) // p)
    B = ((V[0] - beta * d[0]) // p, (V[1] - beta * d[1]) // p)
    assert U == (alpha * d[0] + p * A[0], alpha * d[1] + p * A[1])
    assert V == (beta * d[0] + p * B[0], beta * d[1] + p * B[1])
    signature = (
        alpha * determinant(d, B)
        - beta * determinant(d, A)
        + p * determinant(A, B)
    )
    return signature


def verify_two_factor_compatibility() -> int:
    checks = 0
    for u, v, radius in ((3, 5, 10), (5, 7, 8)):
        n = u * v
        vectors = list(product(range(-radius, radius + 1), repeat=2))
        for U in vectors:
            for V in vectors:
                delta = determinant(U, V)
                if delta % n:
                    continue
                Lu = local_representation(U, V, u)
                Lv = local_representation(U, V, v)
                q = delta // n
                assert Lu == v * q
                assert Lv == u * q
                assert (delta == 0) == (Lu == 0 and Lv == 0)
                checks += 1
    return checks


def main() -> None:
    arc_subsets = verify_arc_bound_p3()
    local_checks = verify_local_identity()
    compatibility_checks = verify_two_factor_compatibility()
    print(
        f"verified CRT slope carries: arc-subsets={arc_subsets}, "
        f"local-identities={local_checks}, compatibility={compatibility_checks}"
    )


if __name__ == "__main__":
    main()
