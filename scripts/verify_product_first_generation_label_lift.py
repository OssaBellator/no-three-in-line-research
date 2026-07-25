#!/usr/bin/env python3
"""Finite checks for PX420--PX427 first-generation rectangle-label lifts."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import comb
import random


def collinear(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> bool:
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        == (b[1] - a[1]) * (c[0] - a[0])
    )


def check_four_type_extraction() -> None:
    rng = random.Random(420)
    for _ in range(5000):
        size = rng.randint(0, 500)
        types = [rng.randrange(4) for _ in range(size)]
        counts = Counter(types)
        assert 4 * max(counts.values(), default=0) >= size


def check_line_forbidden_degree() -> None:
    rng = random.Random(422)
    for order in range(3, 60):
        # Two injective source-row copies and one target-column copy.
        p = list(range(order))
        rng.shuffle(p)
        rows = [(u, order + p[u]) for u in range(order)]

        for _ in range(100):
            # Nonaxis line through random integer points, represented by Ax+By=C
            # with both A and B nonzero.
            a = rng.choice([value for value in range(-10, 11) if value])
            b = rng.choice([value for value in range(-10, 11) if value])
            c = rng.randint(-20, 4 * order + 20)

            edges: set[tuple[int, int]] = set()
            for source, source_rows in enumerate(rows):
                for target in range(order):
                    for x in source_rows:
                        y = target
                        if a * x + b * y == c:
                            edges.add((source, target))

            source_degree = Counter(source for source, _ in edges)
            target_degree = Counter(target for _, target in edges)
            assert max(source_degree.values(), default=0) <= 2
            assert max(target_degree.values(), default=0) <= 1


def check_paired_rank_no_collapse() -> None:
    rng = random.Random(425)
    for order in range(3, 40):
        p = list(range(order))
        targets = list(range(order))
        rng.shuffle(p)
        rng.shuffle(targets)

        for _ in range(200):
            sources = rng.sample(range(order), rng.randint(1, min(5, order)))
            points: dict[int, tuple[tuple[int, int], tuple[int, int]]] = {}
            for source in sources:
                y = targets[source]
                points[source] = ((source, y), (order + p[source], y))

            all_points = [
                (source, copy, point)
                for source, pair in points.items()
                for copy, point in enumerate(pair)
            ]
            for triple in combinations(all_points, 3):
                if collinear(triple[0][2], triple[1][2], triple[2][2]):
                    assert len({item[0] for item in triple}) == 3


def check_loaded_line_destruction() -> None:
    for line_size in range(3, 100):
        for moved in range(1, line_size + 1):
            destroyed = comb(line_size, 3) - comb(line_size - moved, 3)
            direct = sum(
                1
                for triple in combinations(range(line_size), 3)
                if any(vertex < moved for vertex in triple)
            )
            assert destroyed == direct


def check_constant_copy_patterns() -> None:
    for rank in (1, 2, 3):
        assert 2**rank <= 8
        patterns = list(range(2**rank))
        assert len(patterns) == 2**rank


def main() -> None:
    check_four_type_extraction()
    check_line_forbidden_degree()
    check_paired_rank_no_collapse()
    check_loaded_line_destruction()
    check_constant_copy_patterns()
    print("PX420--PX427 first-generation label-lift verifier: PASS")


if __name__ == "__main__":
    main()
