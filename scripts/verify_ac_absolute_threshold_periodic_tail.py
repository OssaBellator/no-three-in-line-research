#!/usr/bin/env python3

"""Finite audit for AC3wf--AC3wj."""

from __future__ import annotations

import random


def main() -> None:
    rng = random.Random(20260728)
    systems = 0
    phase_cycles = 0
    positive = 0
    negative = 0
    zero = 0

    for control_count in range(1, 5):
        for modulus in range(1, 6):
            states = [
                (control, residue)
                for control in range(control_count)
                for residue in range(modulus)
            ]

            for _ in range(180):
                threshold = rng.randint(1, 9)
                increment = {state: rng.randint(-3, 4) for state in states}
                requirement = {
                    state: rng.randint(0, threshold + 4) for state in states
                }
                next_state = {
                    state: (
                        rng.randrange(control_count),
                        (state[1] + increment[state]) % modulus,
                    )
                    for state in states
                }
                systems += 1

                for initial in rng.sample(states, min(len(states), 4)):
                    seen: dict[tuple[int, int], int] = {}
                    path: list[tuple[int, int]] = []
                    state = initial
                    while state not in seen:
                        seen[state] = len(path)
                        path.append(state)
                        state = next_state[state]

                    cycle = path[seen[state] :]
                    phase_cycles += 1
                    drift = sum(increment[item] for item in cycle)
                    assert drift % modulus == 0

                    prefix = 0
                    block_threshold = threshold
                    for item in cycle:
                        block_threshold = max(
                            block_threshold,
                            threshold - prefix,
                            requirement[item] - prefix,
                        )
                        prefix += increment[item]
                    assert prefix == drift

                    initial_balance = block_threshold + rng.randint(0, 20)
                    balance = initial_balance
                    for item in cycle:
                        assert balance >= threshold
                        assert balance >= requirement[item]
                        balance += increment[item]
                    assert balance == initial_balance + drift

                    if drift > 0:
                        positive += 1
                        balance = initial_balance
                        for _ in range(5):
                            for item in cycle:
                                assert balance >= threshold
                                assert balance >= requirement[item]
                                balance += increment[item]
                        assert balance == initial_balance + 5 * drift
                    elif drift == 0:
                        zero += 1
                        assert balance == initial_balance
                    else:
                        negative += 1
                        legal_blocks = (
                            (initial_balance - block_threshold) // (-drift) + 1
                        )
                        for block_index in range(legal_blocks):
                            assert initial_balance + block_index * drift >= block_threshold
                        assert (
                            initial_balance + legal_blocks * drift < block_threshold
                        )

    print(f"systems={systems}")
    print(f"phase_cycles={phase_cycles}")
    print(f"positive={positive}")
    print(f"negative={negative}")
    print(f"zero={zero}")


if __name__ == "__main__":
    main()
