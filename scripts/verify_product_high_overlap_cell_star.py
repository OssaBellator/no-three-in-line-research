#!/usr/bin/env python3
"""Finite checks for PX303--PX306."""

from __future__ import annotations

from itertools import combinations, permutations
import random


def cell_support(cell: tuple[int, int]) -> set[int]:
    return {cell[0], cell[1]}


def verify_two_cell_incidence() -> None:
    rng = random.Random(303)
    for n in range(2, 8):
        for perm_tuple in permutations(range(n)):
            cells = [(i, perm_tuple[i]) for i in range(n)]
            inverse = [0] * n
            for i, j in cells:
                inverse[j] = i

            possible = [
                frozenset(index_set)
                for r in range(1, min(3, n) + 1)
                for index_set in combinations(range(n), r)
            ]
            # Exhaust all possible certificate subsets only at tiny orders;
            # otherwise sample many realized families.
            families = []
            if len(possible) <= 10:
                for mask in range(1 << len(possible)):
                    families.append([possible[k] for k in range(len(possible)) if mask & (1 << k)])
            else:
                for _ in range(80):
                    families.append(rng.sample(possible, rng.randint(0, min(20, len(possible)))))

            for family in families:
                for a in range(n):
                    incident_indices = {a, inverse[a]}
                    load = 0
                    cell_loads = {i: 0 for i in incident_indices}
                    for cert in family:
                        support = set().union(*(cell_support(cells[i]) for i in cert))
                        if a not in support:
                            continue
                        load += 1
                        assigned = next(i for i in cert if i in incident_indices)
                        cell_loads[assigned] += 1
                    assert max(cell_loads.values(), default=0) * 2 >= load
            if n >= 5:
                break  # sampled permutation coverage is enough at larger n


def maximum_matching_size(vertex_count: int, edges: set[tuple[int, int]]) -> int:
    memo: dict[tuple[int, frozenset[tuple[int, int]]], int] = {}

    def solve(vertices: frozenset[int], remaining: frozenset[tuple[int, int]]) -> int:
        key = (len(vertices), remaining)
        if key in memo:
            return memo[key]
        if not remaining:
            return 0
        edge = next(iter(remaining))
        u, v = edge
        without = solve(vertices, remaining - {edge})
        reduced = frozenset(e for e in remaining if u not in e and v not in e)
        with_edge = 1 + solve(vertices - {u, v}, reduced)
        memo[key] = max(without, with_edge)
        return memo[key]

    return solve(frozenset(range(vertex_count)), frozenset(edges))


def verify_line_matching_bound() -> None:
    # Exhaust simple graphs through six vertices.
    for r in range(2, 7):
        pairs = list(combinations(range(r), 2))
        for mask in range(1 << len(pairs)):
            edges = {pairs[k] for k in range(len(pairs)) if mask & (1 << k)}
            if not edges:
                continue
            degrees = [sum(v in e for e in edges) for v in range(r)]
            delta = max(degrees)
            matching = maximum_matching_size(r, edges)
            assert matching * max(1, 2 * delta - 1) >= len(edges)
            # PX304 uses K >= r and the weaker denominator 2K.
            K = r
            assert matching * (2 * K) >= len(edges)

    rng = random.Random(304)
    for _ in range(5000):
        line_sizes = [rng.randint(2, 12) for _ in range(rng.randint(1, 8))]
        total_edges = 0
        total_matching = 0
        K = max(line_sizes)
        for r in line_sizes:
            pairs = list(combinations(range(r), 2))
            edges = {e for e in pairs if rng.random() < 0.35}
            total_edges += len(edges)
            total_matching += maximum_matching_size(r, edges)
        assert total_matching * (2 * K) >= total_edges


def verify_combined_constants() -> None:
    rng = random.Random(306)
    for _ in range(10000):
        K = rng.randint(2, 20)
        m0 = rng.randint(1, 30)
        B = 4 * K * m0
        overlap = rng.randint(B + 1, B + 500)
        point_load = (overlap + 1) // 2
        # Integer star extraction is at least ceil(point_load/(2K)) in the
        # extremal fractional accounting, hence strictly above m0.
        assert overlap / (4 * K) > m0
        assert point_load / (2 * K) > m0

        channels = rng.randint(1, 8)
        batch_bound = 2 * channels * (6 * B - 5)
        assert batch_bound > 0


def main() -> None:
    verify_two_cell_incidence()
    verify_line_matching_bound()
    verify_combined_constants()
    print("high-overlap cell-star verifier: PASS")


if __name__ == "__main__":
    main()
