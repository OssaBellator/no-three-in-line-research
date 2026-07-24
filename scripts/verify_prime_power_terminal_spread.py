#!/usr/bin/env python3
"""Verify CMR35--CMR37 and their exact cylinder counts."""
from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations, product


def determinant(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> int:
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        - (c[0] - a[0]) * (b[1] - a[1])
    )


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def nonsquares(p: int) -> list[int]:
    squares = {x * x % p for x in range(1, p)}
    return [x for x in range(1, p) if x not in squares]


def permutation(p: int, b: int, c: int) -> tuple[int, ...]:
    return tuple(b if x == 0 else (b + c * pow(x, -1, p)) % p for x in range(p))


def verify_prime(p: int) -> tuple[int, int, int]:
    h = (p - 1) // 2
    parameters = list(product(range(1, h + 1), nonsquares(p)))
    assert len(parameters) == h * h

    family: list[tuple[int, ...]] = []
    triple_checks = 0
    for b, c in parameters:
        values = permutation(p, b, c)
        assert sorted(values) == list(range(p))
        points = list(enumerate(values))
        for triple in combinations(points, 3):
            assert determinant(*triple) != 0, (p, b, c, triple)
            triple_checks += 1
        family.append(values)

    single_counts: Counter[tuple[int, int]] = Counter()
    pair_counts: Counter[tuple[tuple[int, int], tuple[int, int]]] = Counter()
    for values in family:
        cells = [(x, values[x]) for x in range(p)]
        single_counts.update(cells)
        for first, second in combinations(cells, 2):
            pair_counts[(first, second)] += 1

    assert max(single_counts.values(), default=0) <= h
    assert max(pair_counts.values(), default=0) <= 1

    terminal_checks = 0
    a = p
    for first_values in family:
        for second_values in family:
            points = (
                [(x, a * first_values[x]) for x in range(p)]
                + [(x, 1 + a * second_values[x]) for x in range(p)]
            )
            for triple in combinations(points, 3):
                assert determinant(*triple) != 0, (p, triple)
                terminal_checks += 1

    return len(family), triple_checks, terminal_checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=19)
    args = parser.parse_args()

    primes = 0
    states = 0
    graph_checks = 0
    terminal_checks = 0
    for p in range(3, args.max_prime + 1, 2):
        if not is_prime(p):
            continue
        count, graph, terminal = verify_prime(p)
        states += count
        graph_checks += graph
        terminal_checks += terminal
        primes += 1

    print(
        f"verified terminal spread primes={primes}; layer-states={states}; "
        f"graph-triples={graph_checks}; two-layer-triples={terminal_checks}"
    )


if __name__ == "__main__":
    main()
