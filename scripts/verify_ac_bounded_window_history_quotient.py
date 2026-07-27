#!/usr/bin/env python3
"""Finite audit for AC3sj--AC3sn bounded-window history quotient."""

from __future__ import annotations

from itertools import product
from random import Random


def shift_window(window: tuple[int, ...], symbol: int, width: int) -> tuple[int, ...]:
    if width == 0:
        return ()
    return (window + (symbol,))[-width:]


def apply_word(window: tuple[int, ...], word: tuple[int, ...], width: int) -> tuple[int, ...]:
    for symbol in word:
        window = shift_window(window, symbol, width)
    return window


def all_windows(alphabet_size: int, width: int) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = [()]
    for length in range(1, width + 1):
        out.extend(product(range(alphabet_size), repeat=length))
    return out


def first_simple_cycle(states: list[tuple]) -> tuple[int, int] | None:
    seen: dict[tuple, int] = {}
    for end, state in enumerate(states):
        if state in seen:
            return seen[state], end
        seen[state] = end
    return None


def exhaustive_window_audit() -> dict[str, int]:
    histories = 0
    return_words = 0
    for alphabet_size in range(1, 5):
        alphabet = range(alphabet_size)
        for width in range(0, 5):
            words: list[tuple[int, ...]] = [()]
            for length in range(1, 7):
                words.extend(product(alphabet, repeat=length))
            for history in words:
                iterative: tuple[int, ...] = ()
                for symbol in history:
                    iterative = shift_window(iterative, symbol, width)
                expected = tuple(history[-width:]) if width else ()
                assert iterative == expected
                histories += 1

            windows = all_windows(alphabet_size, width)
            for window in windows:
                for length in range(1, 6):
                    for word in product(alphabet, repeat=length):
                        returned = apply_word(window, word, width) == window
                        if returned:
                            return_words += 1
                            if width > 0 and length >= width:
                                assert window == tuple(word[-width:])
    return {"histories": histories, "return_words": return_words}


def random_transducer_audit(seed: int = 17391) -> dict[str, int]:
    rng = Random(seed)
    systems = 0
    exact_states = 0
    transitions = 0
    extracted_cycles = 0
    cycle_edges = 0

    for _ in range(12_000):
        x_size = rng.randint(1, 5)
        memory_size = rng.randint(1, 7)
        alphabet_size = rng.randint(1, 4)
        width = rng.randint(0, 4)
        windows = all_windows(alphabet_size, width)
        states = [
            (x, h, window)
            for x in range(x_size)
            for h in range(memory_size)
            for window in windows
        ]
        state_set = set(states)
        n_hist = len(states)
        assert n_hist == x_size * memory_size * sum(
            alphabet_size**j for j in range(width + 1)
        )

        table: dict[tuple[tuple, int], tuple] = {}
        for state in states:
            _, _, window = state
            for symbol in range(alphabet_size):
                next_window = shift_window(window, symbol, width)
                next_state = (
                    rng.randrange(x_size),
                    rng.randrange(memory_size),
                    next_window,
                )
                table[(state, symbol)] = next_state
                assert next_state in state_set
                transitions += 1

        for _check in range(8):
            state = rng.choice(states)
            symbol = rng.randrange(alphabet_size)
            assert table[(state, symbol)] == table[(state, symbol)]

        state = rng.choice(states)
        walk = [state]
        symbols: list[int] = []
        for _step in range(n_hist + 4):
            symbol = rng.randrange(alphabet_size)
            symbols.append(symbol)
            state = table[(state, symbol)]
            walk.append(state)
            repeat = first_simple_cycle(walk)
            if repeat is not None:
                start, end = repeat
                interior = walk[start:end]
                assert len(interior) == len(set(interior))
                assert 1 <= end - start <= n_hist
                assert walk[start] == walk[end]
                cycle_word = tuple(symbols[start:end])
                assert apply_word(walk[start][2], cycle_word, width) == walk[end][2]
                extracted_cycles += 1
                cycle_edges += end - start
                break
        else:
            raise AssertionError("finite walk failed to repeat")

        systems += 1
        exact_states += n_hist

    return {
        "systems": systems,
        "exact_states": exact_states,
        "transitions": transitions,
        "extracted_cycles": extracted_cycles,
        "cycle_edges": cycle_edges,
    }


def main() -> None:
    result = {}
    result.update(exhaustive_window_audit())
    result.update(random_transducer_audit())
    print(result)


if __name__ == "__main__":
    main()
