#!/usr/bin/env python3
"""Finite checks for BDA5bl--BDA5bn."""

from __future__ import annotations

from itertools import combinations, product


def det(x: tuple[int, int], y: tuple[int, int]) -> int:
    return x[0] * y[1] - x[1] * y[0]


def sub(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return x[0] - y[0], x[1] - y[1]


def add(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return x[0] + y[0], x[1] + y[1]


def scale(w: int, z: tuple[int, int]) -> tuple[int, int]:
    return w * z[0], w * z[1]


def collinear(a, b, c) -> bool:
    return det(sub(b, a), sub(c, a)) == 0


def main() -> None:
    checked = 0
    points = [(x, y) for x in range(-4, 5) for y in range(-4, 5)]
    P = (0, 0)
    for a, b, h, q, u, v in product(range(1, 3), repeat=6):
        if u == v:
            continue
        H = h + q
        d = (a, b)
        vectors = {
            "A": (h * a, h * b),
            "B": (H * a, H * b),
            "C": (h * a, H * b),
            "D": (H * a, h * b),
        }

        for z in vectors.values():
            for X, Y in combinations(points, 2):
                common = collinear(add(P, scale(u, z)), X, Y) and collinear(
                    add(P, scale(v, z)), X, Y
                )
                if common:
                    assert det(z, sub(Y, X)) == 0
                    assert det(sub(X, P), sub(Y, P)) == 0
                checked += 1

        zC, zD = vectors["C"], vectors["D"]
        cd_u = {X for X in points if collinear(add(P, scale(u, zC)), add(P, scale(u, zD)), X)}
        cd_v = {X for X in points if collinear(add(P, scale(v, zC)), add(P, scale(v, zD)), X)}
        assert cd_u.isdisjoint(cd_v)

        zA, zB = vectors["A"], vectors["B"]
        ab_u = {X for X in points if collinear(add(P, scale(u, zA)), add(P, scale(u, zB)), X)}
        ab_v = {X for X in points if collinear(add(P, scale(v, zA)), add(P, scale(v, zB)), X)}
        radial = {X for X in points if det(d, sub(X, P)) == 0}
        assert ab_u == ab_v == radial

    for Q in range(1, 20):
        for wall_u in range(Q + 1):
            for wall_v in range(Q + 1):
                assert (
                    wall_u * 2 >= Q
                    or wall_v * 2 >= Q
                    or (Q - wall_u) * 2 > Q and (Q - wall_v) * 2 > Q
                )

    print(f"verified BDA diagonal role separation on {checked} context-pair tests")


if __name__ == "__main__":
    main()
