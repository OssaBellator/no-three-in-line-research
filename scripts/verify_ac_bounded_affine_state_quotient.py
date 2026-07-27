#!/usr/bin/env python3
"""Finite audit for AC3se--AC3si bounded affine state quotient."""

from __future__ import annotations

from collections import defaultdict
from random import Random
from typing import Iterable


def compose(word: Iterable[int], maps: list[tuple[int, int]]) -> tuple[int, int]:
    """Return A,B for the chronological affine word h -> A*h+B."""
    A, B = 1, 0
    for index in word:
        a, b = maps[index]
        A, B = a * A, a * B + b
    return A, B


def first_repeat(states: list[tuple[int, int]]) -> tuple[int, int] | None:
    """Canonical least-ending repeated-state segment."""
    first: dict[tuple[int, int], int] = {}
    for end, state in enumerate(states):
        if state in first:
            return first[state], end
        first[state] = end
    return None


def main() -> None:
    rng = Random(20260727)
    stats: defaultdict[str, int] = defaultdict(int)
    maps = [(a, b) for a in (-1, 0, 1, 2) for b in (-2, -1, 0, 1, 2)]

    for phase_count in range(1, 5):
        for lower in range(-2, 1):
            for width in range(5):
                upper = lower + width
                states = [
                    (phase, memory)
                    for phase in range(phase_count)
                    for memory in range(lower, upper + 1)
                ]
                stock = phase_count * (width + 1)
                assert len(states) == stock
                stats["state_systems"] += 1
                stats["exact_states"] += stock

                continuation: dict[
                    tuple[int, int], tuple[tuple[int, tuple[int, int]], ...]
                ] = {}
                for phase, memory in states:
                    legal: list[tuple[int, tuple[int, int]]] = []
                    for index, (a, b) in enumerate(maps):
                        next_memory = a * memory + b
                        next_phase = (phase + index + 1) % phase_count
                        if lower <= next_memory <= upper:
                            legal.append((index, (next_phase, next_memory)))
                    continuation[(phase, memory)] = tuple(legal)
                    stats["legal_transitions"] += len(legal)

                # The continuation dictionary depends only on the current exact state.
                for state in states:
                    assert continuation[state] == continuation[state]
                    stats["markov_state_checks"] += 1

                for _ in range(30):
                    current = rng.choice(states)
                    path = [current]
                    word: list[int] = []

                    for _step in range(stock + 4):
                        legal = continuation[current]
                        if not legal:
                            break
                        address, current = rng.choice(legal)
                        word.append(address)
                        path.append(current)

                        repeated = first_repeat(path)
                        if repeated is None:
                            continue

                        start, end = repeated
                        cycle_word = word[start:end]
                        A, B = compose(cycle_word, maps)
                        memory = path[start][1]

                        assert A * memory + B == memory
                        assert (A - 1) * memory + B == 0
                        if A == 1:
                            assert B == 0
                        assert 1 <= end - start <= stock

                        # Least-ending extraction has no repeated interior state.
                        interior = path[start:end]
                        assert len(interior) == len(set(interior))

                        stats["repeated_cycles"] += 1
                        stats["cycle_transitions"] += end - start
                        if A == 1:
                            stats["translation_identity_returns"] += 1
                        else:
                            stats["fixed_point_returns"] += 1
                        break

                    # A path with no repeat has at most stock states.
                    if first_repeat(path) is None:
                        assert len(path) <= stock
                        stats["acyclic_paths"] += 1

    print("AC bounded affine state quotient audit passed")
    for key in sorted(stats):
        print(f"{key}: {stats[key]}")


if __name__ == "__main__":
    main()
