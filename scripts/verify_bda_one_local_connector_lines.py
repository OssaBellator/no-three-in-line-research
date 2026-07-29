#!/usr/bin/env python3
"""Finite checks for BDA5br--BDA5bt."""

from itertools import combinations, product


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def scale(t, a):
    return (t * a[0], t * a[1])


def collinear(a, b, c):
    return det(sub(b, a), sub(c, a)) == 0


def main():
    checks = 0
    for a, b, h, q in product(range(1, 4), repeat=4):
        H = h + q
        vectors = {
            "A": (h * a, h * b),
            "B": (H * a, H * b),
            "C": (h * a, H * b),
            "D": (H * a, h * b),
        }
        P = (0, 0)
        cells = [(x, y) for x in range(-4, 5) for y in range(-4, 5)]
        for left, right in combinations(vectors, 2):
            z, zp = vectors[left], vectors[right]
            for u, v in ((1, 2), (1, 3), (2, 3)):
                U, V = scale(u, z), scale(v, zp)
                for X, Y in combinations(cells, 2):
                    both = collinear(U, X, Y) and collinear(V, X, Y)
                    collision = U == V
                    connector = collision or (collinear(U, V, X) and collinear(U, V, Y))
                    assert both == connector
                    checks += 1

        # Exact weighted overlap identity on deterministic address weights.
        wu = {i: (i * 3 + a + h) % 7 for i in range(12)}
        wv = {i: (i * 5 + b + q) % 7 for i in range(12)}
        overlap = sum(min(wu[i], wv[i]) for i in wu)
        ru = sum(wu.values()) - overlap
        rv = sum(wv.values()) - overlap
        assert overlap + ru == sum(wu.values())
        assert overlap + rv == sum(wv.values())
        Q = min(sum(wu.values()), sum(wv.values()))
        assert overlap >= Q / 2 or (ru > Q / 2 - 1e-9 and rv > Q / 2 - 1e-9)

    print(f"verified {checks} one-local connector instances")


if __name__ == "__main__":
    main()
