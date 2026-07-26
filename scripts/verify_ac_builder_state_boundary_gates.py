#!/usr/bin/env python3
"""Finite checks for AC3oq--AC3ot."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import product


def verify_boundaries(counts: Counter[str]) -> None:
    for state_count in range(2, 8):
        states = tuple(range(state_count))
        for truth_mask in range(1, (1 << state_count) - 1):
            current = {
                state: (truth_mask >> state) & 1
                for state in states
            }
            zero = tuple(state for state in states if not current[state])
            one = tuple(state for state in states if current[state])
            assert len(zero) * len(one) <= (state_count * state_count) // 4

            graphs = [
                {
                    (source, target)
                    for source in states
                    for target in states
                    if source != target
                },
                {
                    (source, target)
                    for source in states
                    for target in states
                    if source != target and (source + target) % 2 == 0
                },
                {(state, (state + 1) % state_count) for state in states},
            ]

            for edges in graphs:
                crossing = {
                    edge
                    for edge in edges
                    if not current[edge[0]] and current[edge[1]]
                }
                outdegree = max(
                    sum(source == state for source, _ in edges)
                    for state in states
                )
                assert len(crossing) <= len(edges)
                assert len(crossing) <= len(zero) * outdegree

                for path_length in range(1, 5):
                    for path in product(states, repeat=path_length + 1):
                        if current[path[0]] or not current[path[-1]]:
                            continue
                        if any(
                            (path[index], path[index + 1]) not in edges
                            for index in range(path_length)
                        ):
                            continue
                        first = next(
                            index
                            for index in range(1, len(path))
                            if current[path[index]]
                        )
                        assert not current[path[first - 1]]
                        assert current[path[first]]
                        assert all(
                            not current[path[index]]
                            for index in range(first)
                        )
                        counts["normalized recreation paths"] += 1
                counts["predicate graph systems"] += 1


def verify_builder_partitions(counts: Counter[str]) -> None:
    for state_count in range(2, 9):
        states = tuple(range(state_count))
        for builder_count in range(1, min(4, state_count) + 1):
            builder = {
                state: state % builder_count
                for state in states
            }
            cross_builder = [
                (source, target)
                for source in states
                for target in states
                if builder[source] != builder[target]
            ]
            for source, target in cross_builder:
                assert (builder[source], source) != (builder[target], target)
                counts["changing-builder edges"] += 1


def verify_weight_and_tickets(counts: Counter[str]) -> None:
    for address_count in range(1, 9):
        for weight_word in product((0, 1, 3), repeat=address_count):
            total = sum(weight_word)
            if total:
                assert max(weight_word) >= Fraction(total, address_count)
            capacities = tuple(index % 3 for index in range(address_count))
            charged = sum(capacities)
            remaining = list(capacities)
            used = 0
            for index in range(address_count):
                while remaining[index]:
                    remaining[index] -= 1
                    used += 1
            assert used == charged
            assert all(value == 0 for value in remaining)
            counts["weighted ticket systems"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_boundaries(counts)
    verify_builder_partitions(counts)
    verify_weight_and_tickets(counts)
    print("AC3oq--AC3ot normalized builder-state audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
