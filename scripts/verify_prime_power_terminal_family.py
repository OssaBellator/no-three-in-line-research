#!/usr/bin/env python3
"""Verify the all-prime terminal construction CMR33--CMR34."""
from __future__ import annotations

import argparse
from itertools import combinations


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


def terminal_permutation(p: int) -> list[int]:
    return [1 if x == 0 else (1 + pow(x, -1, p)) % p for x in range(p)]


def verify_prime(p: int, max_exponent: int) -> tuple[int, int]:
    permutation = terminal_permutation(p)
    assert sorted(permutation) == list(range(p))

    graph = [(x, permutation[x]) for x in range(p)]
    graph_checks = 0
    for triple in combinations(graph, 3):
        assert determinant(*triple) != 0, (p, triple)
        graph_checks += 1

    terminal_checks = 0
    for k in range(2, max_exponent + 1):
        a = p ** (k - 1)
        points = (
            [(x, a * permutation[x]) for x in range(p)]
            + [(x, 1 + a * permutation[x]) for x in range(p)]
        )
        assert len(set(points)) == 2 * p
        for triple in combinations(points, 3):
            assert determinant(*triple) != 0, (p, k, triple)
            terminal_checks += 1

    return graph_checks, terminal_checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=101)
    parser.add_argument("--max-exponent", type=int, default=4)
    args = parser.parse_args()

    graph_checks = 0
    terminal_checks = 0
    primes = 0
    for p in range(2, args.max_prime + 1):
        if not is_prime(p):
            continue
        g, t = verify_prime(p, args.max_exponent)
        graph_checks += g
        terminal_checks += t
        primes += 1

    print(
        f"verified terminal family for primes={primes}; "
        f"graph-triples={graph_checks}; terminal-triples={terminal_checks}"
    )


if __name__ == "__main__":
    main()
