#!/usr/bin/env python3
"""Finite checks for PX411--PX419 rectangle-label terminal return."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
import random


def rectangle_state(
    order: int,
    p: list[int],
    t: list[int],
    r: list[int],
) -> list[tuple[int, int]]:
    points: list[tuple[int, int]] = []
    for source in range(order):
        x0 = source
        x1 = order + p[source]
        y0 = t[source]
        y1 = order + r[source]
        points.extend(((x0, y0), (x1, y0), (x0, y1), (x1, y1)))
    return points


def assert_saturated(points: list[tuple[int, int]]) -> None:
    row_counts = Counter(x for x, _ in points)
    column_counts = Counter(y for _, y in points)
    assert set(row_counts.values()) == {2}
    assert set(column_counts.values()) == {2}


def check_label_permutation_invariance() -> None:
    rng = random.Random(20260726)
    for order in range(2, 9):
        for _ in range(300):
            p = list(range(order))
            t = list(range(order))
            r = list(range(order))
            rng.shuffle(p)
            rng.shuffle(t)
            rng.shuffle(r)
            assert_saturated(rectangle_state(order, p, t, r))

            sources = rng.sample(range(order), rng.randint(1, order))
            targets = sources.copy()
            rng.shuffle(targets)
            source_map = dict(zip(sources, targets))

            for family in ("t", "r"):
                new_t = t.copy()
                new_r = r.copy()
                labels = t if family == "t" else r
                changed = new_t if family == "t" else new_r
                for source in sources:
                    changed[source] = labels[source_map[source]]

                assert sorted(new_t) == list(range(order))
                assert sorted(new_r) == list(range(order))
                assert_saturated(rectangle_state(order, p, new_t, new_r))


def check_weight_compression() -> None:
    rng = random.Random(411)
    for _ in range(5000):
        order = rng.randint(1, 100)
        weights = {
            family: [rng.randint(0, 50) for _ in range(order)]
            for family in ("t", "r")
        }
        total = sum(sum(values) for values in weights.values())
        chosen = max(weights, key=lambda family: sum(weights[family]))
        chosen_total = sum(weights[chosen])
        assert 2 * chosen_total >= total

        threshold = rng.randint(1, order + 1)
        positive = [weight for weight in weights[chosen] if weight > 0]
        if len(positive) < threshold and total > 0:
            assert max(positive, default=0) * 2 * threshold >= total


def check_induced_forbidden_degree() -> None:
    rng = random.Random(415)
    for order in range(2, 40):
        for _ in range(200):
            # A geometric partial matching between 2*order paired source rows and
            # 2*order paired target columns.
            source_rows = list(range(2 * order))
            target_columns = list(range(2 * order))
            rng.shuffle(source_rows)
            rng.shuffle(target_columns)
            rank = rng.randint(0, 2 * order)
            geometric = list(zip(source_rows[:rank], target_columns[:rank]))

            label_edges: set[tuple[int, int]] = set()
            for source_row, target_column in geometric:
                source_label = source_row % order
                target_label = target_column % order
                label_edges.add((source_label, target_label))

            source_degree = Counter(source for source, _ in label_edges)
            target_degree = Counter(target for _, target in label_edges)
            assert max(source_degree.values(), default=0) <= 2
            assert max(target_degree.values(), default=0) <= 2


def collinear(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> bool:
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        == (b[1] - a[1]) * (c[0] - a[0])
    )


def check_transposition_internal_triples() -> None:
    rng = random.Random(416)
    for order in range(2, 30):
        for _ in range(200):
            p = list(range(order))
            labels = list(range(order))
            rng.shuffle(p)
            rng.shuffle(labels)
            u, a = rng.sample(range(order), 2)

            inserted = [
                (u, labels[a]),
                (order + p[u], labels[a]),
                (a, labels[u]),
                (order + p[a], labels[u]),
            ]
            for triple in combinations(inserted, 3):
                assert not collinear(*triple)


def check_amplification_constants() -> None:
    # D_(j+1) >= sqrt(n D_j / 96) has the same exponent recurrence as PX405.
    exponent = Fraction(0, 1)
    for generation in range(1, 4):
        exponent = (Fraction(1, 1) + exponent) / 2
    assert exponent == Fraction(7, 8)

    star = exponent - Fraction(1, 3)
    assert star == Fraction(13, 24)
    assert star > Fraction(1, 2)
    assert Fraction(1, 1) - Fraction(1, 3) == Fraction(2, 3)


def main() -> None:
    check_label_permutation_invariance()
    check_weight_compression()
    check_induced_forbidden_degree()
    check_transposition_internal_triples()
    check_amplification_constants()
    print("PX411--PX419 channel-free label-return verifier: PASS")


if __name__ == "__main__":
    main()
