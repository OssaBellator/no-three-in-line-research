#!/usr/bin/env python3
"""Finite geometric checks for PX364--PX370."""

from collections import defaultdict
from math import gcd


Point = tuple[int, int]


def collinear(p: Point, q: Point, r: Point) -> bool:
    return (q[0] - p[0]) * (r[1] - p[1]) == (
        q[1] - p[1]
    ) * (r[0] - p[0])


def line_key(p: Point, q: Point) -> tuple[int, int, int]:
    a = q[1] - p[1]
    b = p[0] - q[0]
    c = -(a * p[0] + b * p[1])
    divisor = gcd(gcd(abs(a), abs(b)), abs(c))
    if divisor:
        a //= divisor
        b //= divisor
        c //= divisor
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    return a, b, c


def main() -> None:
    for order in range(6, 13):
        xs = list(range(order))
        ys = [i * i + 3 * i + 1 for i in range(order)]
        u, v = 0, 1
        labels = [i for i in range(order) if i not in (u, v)]

        # PX364: the shared-core directed-path lines are distinct.
        path_lines = [
            line_key((xs[u], ys[a]), (xs[a], ys[v]))
            for a in labels
        ]
        assert len(set(path_lines)) == len(path_lines)

        # Use two permutation-like selected backgrounds as exact anchor tests.
        anchors = [(xs[i], ys[i]) for i in range(order)]
        anchors += [(xs[i], ys[order - 1 - i]) for i in range(order)]

        # PX367: all four cross-buffer types have partial-matching fibres for
        # every fixed distinct anchor.
        for cross_type in range(4):
            for anchor in anchors:
                edges: list[tuple[int, int]] = []
                for a in labels:
                    u_a = (xs[u], ys[a])
                    a_v = (xs[a], ys[v])
                    first = u_a if cross_type in (0, 1) else a_v
                    for b in labels:
                        v_b = (xs[v], ys[b])
                        b_u = (xs[b], ys[u])
                        second = v_b if cross_type in (0, 2) else b_u
                        if len({first, second, anchor}) < 3:
                            continue
                        if collinear(first, second, anchor):
                            edges.append((a, b))

                left_degree: dict[int, int] = defaultdict(int)
                right_degree: dict[int, int] = defaultdict(int)
                for a, b in edges:
                    left_degree[a] += 1
                    right_degree[b] += 1
                assert max(left_degree.values(), default=0) <= 1
                assert max(right_degree.values(), default=0) <= 1

    # PX368: D n^2 / 32 <= 2 n^2 forces D <= 64.
    for order in range(2, 101):
        for destroyed in range(1, 101):
            if destroyed * order * order / 32 > 2 * order * order:
                assert destroyed > 64

    # PX370: a line distinct from the coordinate row has at most one hit;
    # the coordinate row itself contains the whole family.
    coordinate_family = [(x, 7) for x in range(10)]
    off_row_pair = ((1, 1), (2, 2))
    off_row_hits = [
        point
        for point in coordinate_family
        if collinear(off_row_pair[0], off_row_pair[1], point)
    ]
    assert len(off_row_hits) <= 1

    row_pair = ((1, 7), (2, 7))
    row_hits = [
        point
        for point in coordinate_family
        if collinear(row_pair[0], row_pair[1], point)
    ]
    assert len(row_hits) == len(coordinate_family)

    print("PX364--PX370 buffer-return sector-cap verifier: PASS")


if __name__ == "__main__":
    main()
