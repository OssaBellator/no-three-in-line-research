#!/usr/bin/env python3

"""Finite audit for RI5br--RI5bv."""

from __future__ import annotations

import itertools
import random


def main() -> None:
    rng = random.Random(9917)
    complete_states = 0
    immutable_transpositions = 0
    sampled_cycles = 0
    restoration_gates = 0

    for fibre_size in (1, 2):
        for owner_count in range(1, 5):
            for coherence_count in range(1, 4):
                states = [
                    (selected, owners, coherence)
                    for selected in range(fibre_size)
                    for owners in itertools.product(
                        range(owner_count), repeat=fibre_size
                    )
                    for coherence in range(coherence_count)
                ]
                assert len(states) == (
                    fibre_size * (owner_count**fibre_size) * coherence_count
                )
                complete_states += len(states)

                if fibre_size == 2:
                    for owners in itertools.product(
                        range(owner_count), repeat=fibre_size
                    ):
                        for coherence in range(coherence_count):
                            cycle = [
                                (0, owners, coherence),
                                (1, owners, coherence),
                                (0, owners, coherence),
                            ]
                            assert cycle[0] == cycle[-1]
                            immutable_transpositions += 1

                for _ in range(200):
                    length = rng.randint(2, 7)
                    word = [rng.choice(states) for _ in range(length)]
                    word.append(word[0])
                    if all(state == word[0] for state in word):
                        continue

                    fields = [[state[0] for state in word[:-1]]]
                    for owner_index in range(fibre_size):
                        fields.append(
                            [state[1][owner_index] for state in word[:-1]]
                        )
                    fields.append([state[2] for state in word[:-1]])

                    field_index = next(
                        index
                        for index, values in enumerate(fields)
                        if len(set(values)) > 1
                    )
                    values = fields[field_index]
                    least_value = min(values)
                    exits = [
                        index
                        for index in range(length)
                        if values[index] == least_value
                        and values[(index + 1) % length] != least_value
                    ]
                    assert exits
                    start = exits[0]
                    steps = 1
                    while values[(start + steps) % length] != least_value:
                        steps += 1
                        assert steps <= length

                    sampled_cycles += 1
                    restoration_gates += 1

    print(f"complete_states={complete_states}")
    print(f"immutable_transpositions={immutable_transpositions}")
    print(f"sampled_cycles={sampled_cycles}")
    print(f"restoration_gates={restoration_gates}")


if __name__ == "__main__":
    main()
