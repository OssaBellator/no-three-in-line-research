#!/usr/bin/env python3
"""Exhaustive finite checks for AC3jn--AC3jq."""

from __future__ import annotations

from collections import Counter
from itertools import permutations


def neighbourhood(edge_mask: int, n: int, source_mask: int) -> int:
    result = 0
    row_mask = (1 << n) - 1
    for source in range(n):
        if source_mask >> source & 1:
            result |= (edge_mask >> (source * n)) & row_mask
    return result


def canonical_minimal_core(edge_mask: int, n: int) -> int | None:
    cores = []
    for source_mask in range(1, 1 << n):
        if neighbourhood(edge_mask, n, source_mask).bit_count() >= source_mask.bit_count():
            continue
        minimal = True
        submask = (source_mask - 1) & source_mask
        while submask:
            if neighbourhood(edge_mask, n, submask).bit_count() < submask.bit_count():
                minimal = False
                break
            submask = (submask - 1) & source_mask
        if minimal:
            cores.append(source_mask)
    if not cores:
        return None
    return min(cores, key=lambda mask: (mask.bit_count(), mask))


def has_perfect_matching(edge_mask: int, n: int) -> bool:
    return any(
        all(edge_mask >> (source * n + destination) & 1
            for source, destination in enumerate(permutation))
        for permutation in permutations(range(n))
    )


def saturates_core(edge_mask: int, n: int, source_mask: int) -> bool:
    sources = [source for source in range(n) if source_mask >> source & 1]
    size = len(sources)
    return any(
        all(edge_mask >> (source * n + destination) & 1
            for source, destination in zip(sources, destinations))
        for destinations in permutations(range(n), size)
    )


def verify_core_breaking(counts: Counter[str]) -> None:
    for n in range(1, 5):
        full_destination_mask = (1 << n) - 1
        for edge_mask in range(1 << (n * n)):
            core = canonical_minimal_core(edge_mask, n)
            if core is None:
                assert has_perfect_matching(edge_mask, n)
                counts["perfect exchange graphs"] += 1
                continue

            neighbours = neighbourhood(edge_mask, n, core)
            assert neighbours.bit_count() == core.bit_count() - 1
            complement = full_destination_mask ^ neighbours

            for source in range(n):
                if not (core >> source & 1):
                    continue
                for destination in range(n):
                    if not (complement >> destination & 1):
                        continue
                    edge = 1 << (source * n + destination)
                    assert not edge_mask & edge
                    enlarged = edge_mask | edge
                    assert neighbourhood(enlarged, n, core).bit_count() == core.bit_count()
                    assert saturates_core(enlarged, n, core)
                    if not has_perfect_matching(enlarged, n):
                        next_core = canonical_minimal_core(enlarged, n)
                        assert next_core is not None
                        assert next_core != core
                    counts["canonical cut-edge additions"] += 1

            counts["deficient exchange graphs"] += 1


def verify_expansion_potential(counts: Counter[str]) -> None:
    for n in range(1, 20):
        capacity = n * n
        for initial_size in range(capacity + 1):
            strict_steps = capacity - initial_size
            potential = initial_size
            for _ in range(strict_steps):
                next_potential = potential + 1
                assert next_potential > potential
                potential = next_potential
                counts["strict host expansions"] += 1
            assert potential == capacity
            assert strict_steps <= n * n - initial_size
            counts["host expansion bounds"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_core_breaking(counts)
    verify_expansion_potential(counts)

    print("AC3jn--AC3jq Hall-edge reopening verification passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
